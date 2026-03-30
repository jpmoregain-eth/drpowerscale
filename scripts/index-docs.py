#!/usr/bin/env python3
"""
Dr PowerScale — PDF Indexing Script (PyMuPDF + MHTML)

Converts PDFs and MHTML files in docs/raw-pdfs/ to searchable chunks.

Usage:
    python3 scripts/index-docs.py

Output:
    - docs/processed/*.md   (human-readable chunks)
    - docs/embeddings.json   (machine-readable index for RAG)
"""

import os
import json
import sys
import math
import re
import email
from pathlib import Path
from datetime import datetime
from html.parser import HTMLParser

try:
    import fitz  # PyMuPDF
except ImportError:
    print("❌ PyMuPDF not installed. Run: pip install --break-system-packages PyMuPDF")
    sys.exit(1)

# ─── CONFIG ──────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
PDF_DIR = PROJECT_DIR / "docs" / "raw-pdfs"
PROCESSED_DIR = PROJECT_DIR / "docs" / "processed"
EMBEDDINGS_FILE = PROJECT_DIR / "docs" / "embeddings.json"

CHUNK_SIZE = 500       # Target tokens per chunk (~2000 chars)
CHUNK_OVERLAP = 50     # Overlap tokens between chunks
EMBEDDING_DIM = 384    # Embedding dimensions

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
    """Extract readable text from HTML."""
    extractor = HTMLTextExtractor()
    extractor.feed(html_content)
    text = extractor.get_text()
    # Clean up whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()


# ─── EXTRACTION FUNCTIONS ────────────────────────────────────────────────────

def is_mhtml(filepath):
    """Check if file is MHTML (web page snapshot) not a real PDF."""
    try:
        with open(filepath, 'rb') as f:
            header = f.read(100)
        return header.startswith(b'From: <Saved') or header.startswith(b'From:')
    except:
        return False


def extract_mhtml_text(filepath):
    """Extract text from MHTML web page snapshot."""
    try:
        with open(filepath, 'r', errors='ignore') as f:
            msg = email.message_from_string(f.read())
        
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == 'text/html':
                payload = part.get_payload(decode=True)
                if payload:
                    charset = part.get_content_charset() or 'utf-8'
                    html = payload.decode(charset, errors='ignore')
                    return html_to_text(html)
        
        # Fallback: try as raw HTML
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read()
        # Find HTML content after headers
        html_start = content.find('<!DOCTYPE')
        if html_start == -1:
            html_start = content.find('<html')
        if html_start == -1:
            html_start = content.find('<HTML')
        if html_start != -1:
            return html_to_text(content[html_start:])
        
        return html_to_text(content)
    except Exception as e:
        return None


def extract_pdf_text(filepath):
    """Extract text from PDF using PyMuPDF."""
    try:
        doc = fitz.open(str(filepath))
        text_parts = []
        for page in doc:
            page_text = page.get_text()
            if page_text.strip():
                text_parts.append(page_text)
        doc.close()
        return "\n\n".join(text_parts) if text_parts else None
    except Exception as e:
        return None


def extract_text(filepath):
    """Auto-detect format and extract text."""
    if is_mhtml(filepath):
        return extract_mhtml_text(filepath), "mhtml"
    else:
        return extract_pdf_text(filepath), "pdf"


# ─── CHUNKING ────────────────────────────────────────────────────────────────

def chunk_text(text, source_name, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    """Split text into overlapping chunks."""
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


def seeded_random(seed):
    """Deterministic pseudo-random for placeholder embeddings."""
    x = math.sin(seed) * 10000
    return x - math.floor(x)


# ─── MAIN ────────────────────────────────────────────────────────────────────

def main():
    print("📚 Dr PowerScale — PDF/MHTML Indexer\n")

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
    for f in files:
        size_kb = f.stat().st_size / 1024
        fmt = "MHTML" if is_mhtml(f) else "PDF"
        print(f"   📄 {f.name} ({size_kb:.0f} KB, {fmt})")
    print()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    all_chunks = []
    success_count = 0
    fail_count = 0

    for filepath in files:
        source_name = filepath.stem
        sys.stdout.write(f"⏳ {filepath.name}...")

        text, fmt = extract_text(filepath)

        if not text or len(text.strip()) < 50:
            print(" ⚠️  No text extracted")
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

    print(f"\n📊 Results: {success_count} OK, {fail_count} failed")
    print(f"   {len(all_chunks)} total chunks")

    # Generate placeholder embeddings
    print("⏳ Generating placeholder embeddings...")

    for chunk in all_chunks:
        text_hash = sum(ord(c) for c in chunk["text"])
        chunk["embedding"] = [
            seeded_random(text_hash + i) * 2 - 1
            for i in range(EMBEDDING_DIM)
        ]

    index = {
        "version": 1,
        "chunkSize": CHUNK_SIZE,
        "chunkOverlap": CHUNK_OVERLAP,
        "embeddingDim": EMBEDDING_DIM,
        "generatedAt": datetime.now().isoformat(),
        "totalChunks": len(all_chunks),
        "chunks": [
            {
                "id": c["id"],
                "source": c["source"],
                "index": c["index"],
                "text": c["text"],
                "embedding": c["embedding"],
            }
            for c in all_chunks
        ],
    }

    EMBEDDINGS_FILE.write_text(json.dumps(index), encoding="utf-8")

    file_size_mb = EMBEDDINGS_FILE.stat().st_size / 1024 / 1024
    print(f"\n✅ Index saved: {file_size_mb:.2f} MB")
    print(f"   {len(all_chunks)} chunks from {success_count}/{len(files)} files")
    print("\n📌 Next: git add -A && git commit && git push")


if __name__ == "__main__":
    main()
