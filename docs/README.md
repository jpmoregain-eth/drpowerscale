# Dr PowerScale — Documentation & PDF Indexing Guide

## Project Overview

Dr PowerScale is an AI chat assistant for Dell PowerScale / Isilon NAS storage.
It uses **Groq** (Llama 3.3 70B) for responses and **RAG** (Retrieval Augmented Generation) for grounding answers in official documentation.

---

## Where to Put PDFs

Place all PowerScale / Isilon documentation PDFs in:

```
docs/raw-pdfs/
```

### File Naming Convention

Use descriptive names that identify the document:

```
docs/raw-pdfs/
├── onefs-9.8-admin-guide.pdf
├── onefs-9.8-cli-reference.pdf
├── powerscale-f900-spec-sheet.pdf
├── smartconnect-deployment-guide.pdf
├── synciq-admin-guide.pdf
├── snapshot-isi-admin-guide.pdf
├── powerscale-networking-guide.pdf
├── onefs-upgrade-guide-9.7-to-9.8.pdf
└── ...
```

### Recommended Documents to Include

Priority 1 (Core — get these first):
- OneFS CLI Reference Guide (latest version)
- OneFS Administration Guide (latest version)
- PowerScale Networking Guide
- SyncIQ Administration Guide
- SnapshotIQ Administration Guide

Priority 2 (Important):
- SmartConnect Deployment Guide
- SmartPools Administration Guide
- SmartDedupe Administration Guide
- Security Configuration Guide
- OneFS Upgrade Guide

Priority 3 (Nice to have):
- Hardware guides for specific node models
- Performance tuning guides
- NDMP configuration guides
- HDFS/S3 protocol guides
- Compliance and audit guides

---

## How the Indexing Works

### Architecture

```
PDFs (docs/raw-pdfs/)
  ↓  [Step 1: Extract text]
Markdown chunks (docs/processed/)
  ↓  [Step 2: Generate embeddings]
Embeddings JSON (docs/embeddings.json)
  ↓  [Build time: next build]
Static asset served by Next.js
  ↓  [Runtime: /api/chat]
Cosine similarity search → top chunks → injected into prompt
```

### The Process

#### Step 1: Add PDFs

Copy your PDF files into `docs/raw-pdfs/`.

#### Step 2: Run the Indexing Script

```bash
npm run index-docs
```

This script will:
1. Read all PDFs from `docs/raw-pdfs/`
2. Extract text content from each PDF
3. Split text into chunks (~500 tokens each, with overlap)
4. Generate embeddings for each chunk (using an embedding model)
5. Save chunks + embeddings to `docs/embeddings.json`
6. Save human-readable chunks to `docs/processed/` as markdown files

#### Step 3: Build the App

```bash
npm run build
```

The build process reads `docs/embeddings.json` and makes it available to the API route.

#### Step 4: Deploy

```bash
git add . && git commit -m "Add PowerScale docs" && git push
```

Vercel auto-deploys. The new documentation is immediately available in the chat.

---

## Updating Documentation

When new OneFS versions are released or docs change:

1. Replace/add PDFs in `docs/raw-pdfs/`
2. Run `npm run index-docs` to regenerate the index
3. Commit and push

**Note:** Re-indexing is required whenever PDFs change. The embeddings are not automatically updated.

---

## Technical Details

### Embedding Model

The indexing script uses [embedding model TBD] to generate 384-dimensional vectors for each text chunk. These are stored as JSON arrays alongside the text.

### Chunk Size

Each chunk is approximately 500 tokens (~2000 characters) with 50-token overlap to maintain context across chunk boundaries.

### Retrieval

At runtime, when a user asks a question:
1. The question is embedded using the same model
2. Cosine similarity is computed against all document chunks
3. The top 5 most relevant chunks are retrieved
4. These chunks are injected into the system prompt as `[CONTEXT]`
5. The LLM generates a response grounded in the actual documentation

### File Structure

```
docs/
├── raw-pdfs/          ← PUT PDFs HERE
│   └── *.pdf
├── processed/         ← Auto-generated markdown chunks
│   └── *.md
├── embeddings.json    ← Auto-generated embeddings index
└── README.md          ← This file

scripts/
└── index-docs.mjs     ← Indexing script (run with: npm run index-docs)
```

---

## Environment Variables

Create a `.env.local` file with:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from: https://console.groq.com/

---

## FAQ

**Q: Can I use this for other Dell storage products?**
A: Not yet. The system prompt and knowledge are scoped to PowerScale/Isilon only. Future versions may add PowerMax, PowerStore, etc.

**Q: How accurate are the answers?**
A: The AI uses official Dell documentation when available (via RAG). For topics not covered in the indexed docs, it falls back to general knowledge. Always verify critical procedures against official Dell support.

**Q: What if the AI gives wrong information?**
A: Report it! The system prompt and indexed docs can be updated. For production use, always verify answers against official Dell documentation.
