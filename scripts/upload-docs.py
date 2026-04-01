#!/usr/bin/env python3
"""Upload PowerScale docs to Supabase for keyword search"""

import os
import sys
from pathlib import Path
from datetime import datetime

try:
    from supabase import create_client
except ImportError:
    print("pip install supabase")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
PROCESSED_DIR = PROJECT_DIR / "docs" / "processed"
ENV_FILE = PROJECT_DIR / ".env.local"

def load_env():
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            if '=' in line and not line.startswith('#'):
                key, _, value = line.partition('=')
                env[key.strip()] = value.strip()
    return env

def split_text(text, chunk_size=1000, overlap=100):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

def main():
    print("🚀 Uploading PowerScale docs to Supabase")
    
    # Get files
    files = list(PROCESSED_DIR.glob("*.md"))
    print(f"Found {len(files)} markdown files")
    
    # Connect to Supabase
    env = load_env()
    url = env.get('SUPABASE_URL') or env.get('NEXT_PUBLIC_SUPABASE_URL')
    key = env.get('SUPABASE_ANON_KEY') or env.get('NEXT_PUBLIC_SUPABASE_ANON_KEY')
    supabase = create_client(url, key)
    
    # Clear existing
    print("Clearing existing chunks...")
    supabase.table('chunks').delete().neq('id', '').execute()
    
    # Upload each file
    total_chunks = 0
    for md_file in files:
        source = md_file.stem
        text = md_file.read_text(encoding='utf-8')
        
        # Split into chunks
        chunks_list = split_text(text, chunk_size=1500, overlap=150)
        
        # Prepare for upload
        records = []
        for i, chunk_content in enumerate(chunks_list):
            records.append({
                'id': f"{source}_{i:04d}",
                'source': source,
                'chunk_index': i,
                'text': chunk_content[:2000]  # Limit size
            })
        
        # Upload in batches
        for i in range(0, len(records), 50):
            batch = records[i:i+50]
            supabase.table('chunks').insert(batch).execute()
        
        total_chunks += len(chunks_list)
        print(f"  {source}: {len(chunks_list)} chunks")
    
    print(f"\n✅ Done! Uploaded {total_chunks} chunks from {len(files)} files")

if __name__ == "__main__":
    main()
