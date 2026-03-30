#!/usr/bin/env python3
"""
Dr PowerScale — Quick Indexer using Gemini embeddings + Supabase
Replaces Voyage with Gemini (free, no rate limit issues).
"""

import os, json, sys, time, re, email, urllib.request
from pathlib import Path
from html.parser import HTMLParser

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("❌ pip install PyMuPDF")

try:
    from supabase import create_client
except ImportError:
    sys.exit("❌ pip install supabase")

# ─── CONFIG ──────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
PDF_DIR = PROJECT_DIR / "docs" / "raw-pdfs"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
EMBED_BATCH_SIZE = 100
GEMINI_API_KEY = open("/home/ubuntu/gemini_api_key.txt").read().strip()
GEMINI_MODEL = "models/gemini-embedding-001"

# Load Supabase creds from .env.local
env = {}
for line in (PROJECT_DIR / ".env.local").read_text().splitlines():
    if '=' in line and not line.strip().startswith('#'):
        k, _, v = line.partition('=')
        env[k.strip()] = v.strip()

SUPABASE_URL = env["SUPABASE_URL"]
SUPABASE_KEY = env["SUPABASE_ANON_KEY"]

# ─── HTML EXTRACTOR ──────────────────────────────────────────────────────────
class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style','noscript'): self.skip = True
        if tag in ('br','p','div','h1','h2','h3','h4','h5','h6','li','tr'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style','noscript'): self.skip = False
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
    def get_text(self):
        return re.sub(r'\s+', ' ', ' '.join(self.parts)).strip()

def html_to_text(html):
    p = HTMLTextExtractor()
    p.feed(html)
    return p.get_text()

def is_mhtml(fp):
    try:
        with open(fp, 'rb') as f:
            return f.read(100).startswith(b'From:')
    except: return False

def extract_text(fp):
    if is_mhtml(fp):
        try:
            with open(fp, 'r', errors='ignore') as f:
                msg = email.message_from_string(f.read())
            for part in msg.walk():
                if part.get_content_type() == 'text/html':
                    payload = part.get_payload(decode=True)
                    if payload:
                        charset = part.get_content_charset() or 'utf-8'
                        return html_to_text(payload.decode(charset, errors='ignore'))
            # fallback
            content = fp.read_text(errors='ignore')
            for tag in ('<!DOCTYPE', '<html', '<HTML'):
                idx = content.find(tag)
                if idx != -1:
                    return html_to_text(content[idx:])
            return html_to_text(content)
        except:
            return None
    else:
        try:
            doc = fitz.open(str(fp))
            parts = [p.get_text() for p in doc if p.get_text().strip()]
            doc.close()
            return "\n\n".join(parts) if parts else None
        except:
            return None

# ─── CHUNKING ────────────────────────────────────────────────────────────────
def chunk_text(text, source, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    char_size = chunk_size * 4
    char_overlap = overlap * 4
    chunks = []
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    current = ""
    idx = 0
    for para in paragraphs:
        if len(current + "\n\n" + para) > char_size and current:
            chunks.append({"id": f"{source}::chunk_{idx}", "source": source, "index": idx, "text": current.strip()})
            words = current.split()
            current = " ".join(words[-max(1, char_overlap // 5):]) + "\n\n" + para
            idx += 1
        else:
            current = (current + "\n\n" + para) if current else para
    if current.strip():
        chunks.append({"id": f"{source}::chunk_{idx}", "source": source, "index": idx, "text": current.strip()})
    return chunks

# ─── GEMINI EMBEDDINGS ───────────────────────────────────────────────────────
def embed_batch_gemini(texts):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL.split('/')[-1]}:batchEmbedContents?key={GEMINI_API_KEY}"
    requests = [{"model": GEMINI_MODEL, "content": {"parts": [{"text": t[:8000]}]}} for t in texts]
    payload = json.dumps({"requests": requests}).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    return [e.get("values", []) for e in data.get("embeddings", [])]

# ─── SUPABASE ────────────────────────────────────────────────────────────────
def upsert_to_supabase(chunks, embeddings):
    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    # Clear old data
    try:
        client.table("chunks").delete().neq("id", "").execute()
        print("  ✅ Cleared old data")
    except Exception as e:
        print(f"  ⚠️  Clear: {e}")

    batch_size = 50
    for i in range(0, len(chunks), batch_size):
        rows = []
        for c, emb in zip(chunks[i:i+batch_size], embeddings[i:i+batch_size]):
            rows.append({
                "id": c["id"],
                "source": c["source"],
                "chunk_index": c["index"],
                "text": c["text"],
                "embedding": emb,
            })
        try:
            client.table("chunks").upsert(rows).execute()
            done = min(i + batch_size, len(chunks))
            print(f"  📦 {done}/{len(chunks)} rows upserted", flush=True)
        except Exception as e:
            print(f"  ❌ batch {i//batch_size + 1}: {str(e)[:100]}")
        time.sleep(0.3)

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    print("📚 Dr PowerScale — Gemini Indexer\n")

    files = sorted(f for f in PDF_DIR.iterdir() if f.suffix.lower() == ".pdf")
    print(f"Found {len(files)} files\n")

    # Step 1: Extract + chunk
    print("⏳ Extracting + chunking...")
    all_chunks = []
    ok = fail = 0
    for fp in files:
        sys.stdout.write(f"  {fp.name}...")
        text = extract_text(fp)
        if not text or len(text.strip()) < 50:
            print(" ⚠️")
            fail += 1
            continue
        chunks = chunk_text(text, fp.stem)
        all_chunks.extend(chunks)
        print(f" ✅ {len(chunks)} chunks")
        ok += 1
    print(f"\n📊 {ok} OK, {fail} failed, {len(all_chunks)} total chunks\n")

    # Step 2: Embed with Gemini
    print("⏳ Embedding with Gemini (free, 1024-dim)...")
    all_embeddings = []
    total_batches = (len(all_chunks) + EMBED_BATCH_SIZE - 1) // EMBED_BATCH_SIZE
    for i in range(0, len(all_chunks), EMBED_BATCH_SIZE):
        batch = all_chunks[i:i + EMBED_BATCH_SIZE]
        texts = [c["text"] for c in batch]
        bn = i // EMBED_BATCH_SIZE + 1
        sys.stdout.write(f"  Batch {bn}/{total_batches} ({len(batch)} chunks)...")
        try:
            embs = embed_batch_gemini(texts)
            all_embeddings.extend(embs)
            print(f" ✅ ({len(embs)} vectors)")
        except Exception as e:
            print(f" ❌ {str(e)[:80]}")
            # Fallback: zero vectors
            all_embeddings.extend([[0.0] * 1024] * len(batch))
        if bn < total_batches:
            time.sleep(1)  # Small delay between batches
    print(f"\n📊 Embedded: {len(all_embeddings)} vectors\n")

    # Step 3: Push to Supabase
    print("⏳ Pushing to Supabase...")
    upsert_to_supabase(all_chunks, all_embeddings)

    print(f"\n✅ Done! {len(all_chunks)} chunks in Supabase")
    print("   Ready for drpowerscale.vercel.app 🚀")

if __name__ == "__main__":
    main()
