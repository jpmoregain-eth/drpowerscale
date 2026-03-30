# Dr PowerScale

AI-powered chat assistant for Dell PowerScale and Isilon NAS storage.

## Features

- 🤖 AI chat powered by Groq (Llama 3.3 70B)
- 📚 RAG-grounded answers from official Dell documentation
- 🔒 Scoped to PowerScale/Isilon NAS only
- ⚡ Streaming responses
- 📱 Responsive design

## Quick Start

```bash
# Install dependencies
npm install

# Set up environment
cp .env.example .env.local
# Edit .env.local and add your GROQ_API_KEY

# Run dev server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Adding Documentation

1. Place PowerScale/Isilon PDFs in `docs/raw-pdfs/`
2. Run `npm run index-docs`
3. Build and deploy

See [docs/README.md](docs/README.md) for full details.

## Deploy

```bash
npm run build
# Push to GitHub — Vercel auto-deploys
```

## Tech Stack

- Next.js 15
- React 19
- Tailwind CSS v4
- Groq SDK (Llama 3.3 70B Versatile)
- TypeScript

## Scope

This assistant only handles Dell PowerScale and Isilon NAS storage queries. It does not discuss other Dell products (PowerMax, PowerStore, etc.), SAN technologies, or non-storage topics.

---

*Based on the [Virtual MPS](https://github.com/jpmoregain-eth/mpsg) architecture.*
