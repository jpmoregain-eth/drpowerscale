#!/usr/bin/env python3
"""
Dr PowerScale — PDF Indexer with Voyage AI + Supabase

Extracts PDFs, generates real embeddings, stores in Supabase pgvector.

Usage:
    python3 scripts/index-docs.py

Requirements:
    pip install --break-system-packages PyMuPDF supabase
"""

import os
import json
import sys
import time
import re
import email
import urllib.request
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

try:
    import fitz  # PyMuPDF
except ImportError:
    print("❌ PyMuPDF not installed. Run: pip install --break-system-packages PyMuPDF")
    sys.exit(1)

try:
    from supabase import create_client
except ImportError:
    print("❌ supabase not installed. Run: pip install --break-system-packages supabase")
    sys.exit(1)

# ─── CONFIG ──────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
PDF_DIR = PROJECT_DIR / "docs" / "raw-pdfs"
PROCESSED_DIR = PROJECT_DIR / "docs" / "processed"
ENV_FILE = PROJECT_DIR / ".env.local"

CHUNK_SIZE = 500       # Target tokens per chunk (~2000 chars)
CHUNK_OVERLAP = 50     # Overlap tokens between chunks
EMBED_BATCH_SIZE = 25  # Smaller batches to avoid rate limits
VOYAGE_MODEL = "voyage-3"

# ─── LOAD ENV ────────────────────────────────────────────────────────────────

def load_env():
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if '=' in line and not line.strip().startswith('#'):
                key, _, value = line.partition('=')
                env[key.strip()] = value.strip()
    return env

# ─── HTML TEXT EXTRACTOR ─────────────────────────────────────────────────────

class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_tags = {'script', 'style', 'noscript'}
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self._skip = True
        if tag in ('br', 'p', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'tr'):
            self.text_parts.append('\n')

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            self.text_parts.append(data)

    def get_text(self):
        return ' '.join(self.text_parts)


def html_to_text(html_content):
    extractor = HTMLTextExtractor()
    extractor.feed(html_content)
    text = extractor.get_text()
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()


# ─── EXTRACTION ──────────────────────────────────────────────────────────────

def is_mhtml(filepath):
    try:
        with open(filepath, 'rb') as f:
            header = f.read(100)
        return header.startswith(b'From: <Saved') or header.startswith(b'From:')
    except:
        return False


def extract_mhtml_text(filepath):
    try:
        with open(filepath, 'r', errors='ignore') as f:
            msg = email.message_from_string(f.read())
        for part in msg.walk():
            if part.get_content_type() == 'text/html':
                payload = part.get_payload(decode=True)
                if payload:
                    charset = part.get_content_charset() or 'utf-8'
                    html = payload.decode(charset, errors='ignore')
                    return html_to_text(html)
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read()
        html_start = content.find('<!DOCTYPE')
        if html_start == -1:
            html_start = content.find('<html')
        if html_start == -1:
            html_start = content.find('<HTML')
        if html_start != -1:
            return html_to_text(content[html_start:])
        return html_to_text(content)
    except:
        return None


def extract_pdf_text(filepath):
    try:
        doc = fitz.open(str(filepath))
        text_parts = []
        for page in doc:
            page_text = page.get_text()
            if page_text.strip():
                text_parts.append(page_text)
        doc.close()
        return "\n\n".join(text_parts) if text_parts else None
    except:
        return None


def extract_text(filepath):
    if is_mhtml(filepath):
        return extract_mhtml_text(filepath), "mhtml"
    else:
        return extract_pdf_text(filepath), "pdf"


# ─── CHUNKING ────────────────────────────────────────────────────────────────

def chunk_text(text, source_name, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    char_size = chunk_size * 4
    char_overlap = overlap * 4
    chunks = []

    paragraphs = text.split("\n\n")
    current_chunk = ""
    chunk_index = 0

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        if len(current_chunk + "\n\n" + para) > char_size and len(current_chunk) > 0:
            chunks.append({
                "id": f"{source_name}::chunk_{chunk_index}",
                "source": source_name,
                "index": chunk_index,
                "text": current_chunk.strip(),
            })
            words = current_chunk.split()
            overlap_words = words[-max(1, char_overlap // 5):]
            current_chunk = " ".join(overlap_words) + "\n\n" + para
            chunk_index += 1
        else:
            current_chunk = (current_chunk + "\n\n" + para) if current_chunk else para

    if current_chunk.strip():
        chunks.append({
            "id": f"{source_name}::chunk_{chunk_index}",
            "source": source_name,
            "index": chunk_index,
            "text": current_chunk.strip(),
        })

    return chunks


# ─── VOYAGE EMBEDDINGS ───────────────────────────────────────────────────────

def embed_batch(texts, api_key, max_retries=5):
    """Embed a batch of texts using Voyage AI API with retry logic."""
    url = "https://api.voyageai.com/v1/embeddings"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = json.dumps({
        "model": VOYAGE_MODEL,
        "input": texts,
    }).encode("utf-8")

    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=60) as resp:
                result = json.loads(resp.read().decode("utf-8"))
            return [item["embedding"] for item in result["data"]]
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = min(2 ** (attempt + 1), 30)  # Exponential backoff, max 30s
                print(f" ⏳ rate limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                raise
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                raise

    return [[0.0] * 1024] * len(texts)


def embed_all_chunks(chunks, api_key):
    """Embed all chunks in batches."""
    all_embeddings = []
    total_batches = (len(chunks) + EMBED_BATCH_SIZE - 1) // EMBED_BATCH_SIZE

    for i in range(0, len(chunks), EMBED_BATCH_SIZE):
        batch = chunks[i:i + EMBED_BATCH_SIZE]
        texts = [c["text"] for c in batch]
        batch_num = i // EMBED_BATCH_SIZE + 1

        sys.stdout.write(f"  Embedding batch {batch_num}/{total_batches} ({len(batch)} chunks)...")

        try:
            embeddings = embed_batch(texts, api_key)
            all_embeddings.extend(embeddings)
            print(f" ✅")
        except Exception as e:
            print(f" ❌ {str(e)[:60]}")
            # Add empty embeddings as fallback
            all_embeddings.extend([[0.0] * 1024] * len(batch))

        # Rate limit: delay between batches
        if i + EMBED_BATCH_SIZE < len(chunks):
            time.sleep(2)

    return all_embeddings


# ─── SUPABASE ────────────────────────────────────────────────────────────────

def upsert_chunks(chunks, embeddings, supabase_url, supabase_key):
    """Upsert chunks into Supabase in batches."""
    client = create_client(supabase_url, supabase_key)

    batch_size = 100  # Supabase upsert limit
    total_batches = (len(chunks) + batch_size - 1) // batch_size

    for i in range(0, len(chunks), batch_size):
        batch_chunks = chunks[i:i + batch_size]
        batch_embeddings = embeddings[i:i + batch_size]
        batch_num = i // batch_size + 1

        rows = []
        for chunk, embedding in zip(batch_chunks, batch_embeddings):
            rows.append({
                "id": chunk["id"],
                "source": chunk["source"],
                "chunk_index": chunk["index"],
                "text": chunk["text"],
                "embedding": embedding,
            })

        sys.stdout.write(f"  Upserting batch {batch_num}/{total_batches} ({len(rows)} rows)...")

        try:
            client.table("chunks").upsert(rows).execute()
            print(f" ✅")
        except Exception as e:
            print(f" ❌ {str(e)[:80]}")

        time.sleep(0.2)


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    print("📚 Dr PowerScale — PDF Indexer (Voyage AI + Supabase)\n")

    env = load_env()
    voyage_key = env.get("VOYAGE_API_KEY")
    supabase_url = env.get("SUPABASE_URL")
    supabase_key = env.get("SUPABASE_ANON_KEY")

    if not all([voyage_key, supabase_url, supabase_key]):
        print("❌ Missing env vars in .env.local:")
        print(f"   VOYAGE_API_KEY: {'✅' if voyage_key else '❌'}")
        print(f"   SUPABASE_URL: {'✅' if supabase_url else '❌'}")
        print(f"   SUPABASE_ANON_KEY: {'✅' if supabase_key else '❌'}")
        sys.exit(1)

    if not PDF_DIR.exists():
        print(f"❌ PDF directory not found: {PDF_DIR}")
        sys.exit(1)

    files = sorted(PDF_DIR.glob("*.pdf"))

    if not files:
        print("📭 No files found in docs/raw-pdfs/")
        sys.exit(0)

    pdf_count = sum(1 for f in files if not is_mhtml(f))
    mhtml_count = sum(1 for f in files if is_mhtml(f))
    print(f"Found {len(files)} file(s): {pdf_count} real PDFs, {mhtml_count} MHTML snapshots\n")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Extract and chunk
    print("⏳ Step 1: Extracting text and chunking...\n")
    all_chunks = []
    success_count = 0
    fail_count = 0

    for filepath in files:
        source_name = filepath.stem
        sys.stdout.write(f"  {filepath.name}...")

        text, fmt = extract_text(filepath)

        if not text or len(text.strip()) < 50:
            print(" ⚠️  No text")
            fail_count += 1
            continue

        chunks = chunk_text(text, source_name)
        all_chunks.extend(chunks)

        md_content = "\n\n---\n\n".join(
            f"## {c['id']}\n\n{c['text']}" for c in chunks
        )
        (PROCESSED_DIR / f"{source_name}.md").write_text(md_content, encoding="utf-8")

        print(f" ✅ {len(chunks)} chunks ({fmt})")
        success_count += 1

    print(f"\n📊 Extracted: {success_count} OK, {fail_count} failed, {len(all_chunks)} total chunks\n")

    # Step 2: Clear existing data and generate embeddings
    print("⏳ Step 2: Clearing old data from Supabase...\n")
    try:
        client = create_client(supabase_url, supabase_key)
        # Delete all existing chunks
        client.table("chunks").delete().neq("id", "").execute()
        print("  ✅ Cleared\n")
    except Exception as e:
        print(f"  ⚠️  {str(e)[:60]} (continuing anyway)\n")

    print("⏳ Step 3: Generating Voyage embeddings...\n")
    embeddings = embed_all_chunks(all_chunks, voyage_key)
    print(f"\n📊 Embedded: {len(embeddings)} vectors\n")

    # Step 4: Upsert to Supabase
    print("⏳ Step 4: Upserting to Supabase...\n")
    upsert_chunks(all_chunks, embeddings, supabase_url, supabase_key)

    print(f"\n✅ Done!")
    print(f"   {len(all_chunks)} chunks embedded and stored in Supabase")
    print(f"   Model: {VOYAGE_MODEL} (1024 dimensions)")
    print(f"\n📌 Next: Update Vercel API route + deploy")


if __name__ == "__main__":
    main()
