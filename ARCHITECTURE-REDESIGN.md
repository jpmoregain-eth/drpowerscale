# Dr PowerScale — Architecture Redesign Plan
**Date:** 2026-03-30
**Status:** Paused — resume tomorrow

---

## Current State

### What's Working ✅
- **Frontend:** Next.js chatbot UI on Vercel → https://drpowerscale.vercel.app
- **LLM:** Groq (Llama 3.3 70B) via API
- **System Prompt:** Comprehensive PowerScale/Isilon scope + product reference
- **PDFs Collected:** 62 files in `docs/raw-pdfs/` (real PDFs + MHTML snapshots)
- **Chunks Extracted:** 3,490 chunks across 62 sources
- **Indexer:** Python script using PyMuPDF (`scripts/index-docs.py`)

### What's Broken ❌
- **RAG is NOT wired up** — API route has `// TODO: RAG context injection point`
- **Embeddings are placeholder** — random vectors, not real semantic embeddings
- **Chatbot answers from LLM knowledge only** — can't reference specific PDF content
- **35MB embeddings.json** — too large for Vercel serverless, never actually used

---

## The Problem

```
Current flow:
  User asks → Groq LLM → Answer (from training data only)
  
  PDFs exist but are never consulted.
```

---

## Proposed Architecture: Supabase + pgvector + OpenAI

```
┌─────────────────────────────────────────────────────┐
│                   LOCAL (Legion 5)                    │
│                                                       │
│  PDFs → PyMuPDF → chunks → OpenAI embed → INSERT     │
│  Run once, or when adding new docs                    │
│                                                       │
│  Script: scripts/index-docs.py (upgrade to embed)     │
└──────────────────────┬──────────────────────────────┘
                       │
              ┌────────▼────────┐
              │   Supabase DB   │
              │   (pgvector)    │
              │                 │
              │ Table: chunks   │
              │  - id           │
              │  - source       │
              │  - text         │
              │  - embedding    │ ← 1536-dim vector (OpenAI)
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │  Vercel (API)   │
              │                 │
              │ 1. User asks Q  │
              │ 2. OpenAI embed │ ← embed the query
              │    the query    │
              │ 3. Supabase     │ ← vector similarity search
              │    vector search│
              │ 4. Top 5 chunks │
              │ 5. Inject into  │
              │    system prompt│
              │ 6. Groq answers │
              │    from context │
              └─────────────────┘
```

### Why This Approach
- **Real semantic search** — finds relevant docs even with different wording
- **Data lives in Supabase** — not in Git, not in Vercel
- **Adding docs = INSERT** — no redeploy needed
- **Free tier** — Supabase 500MB, OpenAI ~$0.01/month for chatbot queries
- **Industry standard** — pgvector is the go-to for this use case

---

## What's Needed to Resume

### Accounts to Create
1. **Supabase** — https://supabase.com (free tier)
   - Create project
   - Get: Project URL + anon key
   - Enable pgvector extension

2. **OpenAI** — https://platform.openai.com
   - Create API key
   - For: Query embeddings (text-embedding-3-small, 1536 dims)
   - Cost: ~$0.01/month for chatbot volume

### Share with GoldmanSax
- Supabase URL + anon key
- OpenAI API key
- (Will add to Vercel environment variables)

---

## Implementation Steps (Tomorrow)

### Step 1: Supabase Setup
```sql
-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Create chunks table
CREATE TABLE chunks (
  id TEXT PRIMARY KEY,
  source TEXT NOT NULL,
  chunk_index INT NOT NULL,
  text TEXT NOT NULL,
  embedding vector(1536)
);

-- Create index for fast similarity search
CREATE INDEX ON chunks USING ivfflat (embedding vector_cosine_ops);
```

### Step 2: Update Local Indexer
- Upgrade `scripts/index-docs.py`
- Add OpenAI embedding generation (text-embedding-3-small)
- Add Supabase INSERT logic
- Run once to populate DB

### Step 3: Update Vercel API Route
- Add `@supabase/supabase-js` dependency
- Add OpenAI dependency (for query embedding)
- Implement `retrieveContext()` function:
  1. Embed user's question via OpenAI
  2. Query Supabase for top 5 similar chunks
  3. Return formatted context
- Inject context into system prompt as `[CONTEXT]`
- Add env vars: `SUPABASE_URL`, `SUPABASE_ANON_KEY`, `OPENAI_API_KEY`

### Step 4: Remove Old Embeddings
- Delete `docs/embeddings.json` (35MB placeholder file)
- Keep `docs/raw-pdfs/` and `docs/processed/` for reference
- Update `.gitignore`

### Step 5: Test & Deploy
- Test locally first
- Push to GitHub → Vercel auto-deploys
- Test on https://drpowerscale.vercel.app

---

## File Structure (Target)

```
drpowerscale/
├── docs/
│   ├── raw-pdfs/              ← 62 PDFs (keep for reference)
│   └── processed/             ← Human-readable markdown chunks
├── scripts/
│   └── index-docs.py          ← PDF → chunks → OpenAI embed → Supabase
├── src/
│   └── app/
│       └── api/
│           └── chat/
│               └── route.ts   ← RAG retrieval + LLM call
├── package.json
└── README.md
```

---

## Open Questions
- Should we keep the 35MB `embeddings.json` in Git? (Probably delete it)
- Should we also embed with a local model as backup? (Overkill for now)
- Hybrid search (vector + keyword) later? (Phase 2)

---

## Notes
- PyMuPDF is the best PDF extractor (handles Dell DRM-protected docs)
- MHTML files from Dell InfoHub are useless (JS-rendered content)
- DrDellEMC knowledge base has additional docs we can copy later
- Groq API key is already in Vercel env vars
