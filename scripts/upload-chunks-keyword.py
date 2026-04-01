#!/usr/bin/env python3
"""
Dr PowerScale — Keyword Search Uploader (Phase 1)

Uploads PDF chunks to Supabase for keyword search.
No embeddings yet — just text storage.

Usage:
    python3 scripts/upload-chunks-keyword.py
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

try:
    from supabase import create_client
except ImportError:
    print("❌ supabase not installed. Run: pip install --break-system-packages supabase")
    sys.exit(1)

# ─── CONFIG ──────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
PROCESSED_DIR = PROJECT_DIR / "docs" / "processed"
ENV_FILE = PROJECT_DIR / ".env.local"

# ─── LOAD ENV ────────────────────────────────────────────────────────────────

def load_env():
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if '=' in line and not line.strip().startswith('#'):
                key, _, value = line.partition('=')
                env[key.strip()] = value.strip()
    return env

# ─── SUPABASE CLIENT ─────────────────────────────────────────────────────────

def get_supabase():
    env = load_env()
    url = env.get('SUPABASE_URL') or env.get('NEXT_PUBLIC_SUPABASE_URL')
    key = env.get('SUPABASE_ANON_KEY') or env.get('NEXT_PUBLIC_SUPABASE_ANON_KEY')
    
    if not url or not key:
        print("❌ Missing Supabase credentials in .env.local")
        print("   Need: SUPABASE_URL and SUPABASE_ANON_KEY")
        sys.exit(1)
    
    return create_client(url, key)

# ─── UPLOAD CHUNKS ───────────────────────────────────────────────────────────

def upload_chunks():
    print("🚀 Dr PowerScale Keyword Search Uploader")
    print("=" * 50)
    
    # Check for processed chunks
    if not PROCESSED_DIR.exists():
        print(f"❌ Processed directory not found: {PROCESSED_DIR}")
        print("   Run the indexer first to extract chunks from PDFs")
        sys.exit(1)
    
    # Load chunks from processed files
    chunks = []
    for json_file in sorted(PROCESSED_DIR.glob("*.json")):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                source = json_file.stem
                for i, chunk_text in enumerate(data.get('chunks', [])):
                    chunks.append({
                        'id': f"{source}_{i:04d}",
                        'source': source,
                        'chunk_index': i,
                        'text': chunk_text
                    })
        except Exception as e:
            print(f"⚠️  Skipping {json_file.name}: {e}")
            continue
    
    if not chunks:
        print("❌ No chunks found to upload")
        sys.exit(1)
    
    print(f"📚 Found {len(chunks)} chunks from {len(list(PROCESSED_DIR.glob('*.json')))} sources")
    
    # Connect to Supabase
    print("🔗 Connecting to Supabase...")
    supabase = get_supabase()
    
    # Clear existing chunks (optional — comment out if you want to keep existing)
    print("🧹 Clearing existing chunks...")
    try:
        supabase.table('chunks').delete().neq('id', '').execute()
        print("   ✅ Existing chunks cleared")
    except Exception as e:
        print(f"   ⚠️  Could not clear existing chunks: {e}")
    
    # Upload in batches
    batch_size = 100
    total_uploaded = 0
    
    print(f"⬆️  Uploading {len(chunks)} chunks to Supabase...")
    
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        try:
            result = supabase.table('chunks').insert(batch).execute()
            total_uploaded += len(batch)
            print(f"   Progress: {total_uploaded}/{len(chunks)} chunks uploaded")
        except Exception as e:
            print(f"   ❌ Error uploading batch {i//batch_size + 1}: {e}")
            continue
    
    print("=" * 50)
    print(f"✅ Done! Uploaded {total_uploaded} chunks to Supabase")
    print(f"🌐 Table: chunks")
    print(f"🔍 Ready for keyword search!")

# ─── MAIN ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    upload_chunks()
