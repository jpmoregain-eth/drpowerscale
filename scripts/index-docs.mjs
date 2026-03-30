#!/usr/bin/env node

/**
 * Dr PowerScale — PDF Indexing Script
 *
 * Converts PDFs in docs/raw-pdfs/ to searchable chunks with embeddings.
 *
 * Usage:
 *   npm run index-docs
 *
 * Prerequisites:
 *   npm install pdf-parse
 *
 * Output:
 *   - docs/processed/*.md   (human-readable chunks)
 *   - docs/embeddings.json   (machine-readable index for RAG)
 */

import { readFileSync, writeFileSync, readdirSync, mkdirSync, existsSync } from "fs";
import { join, basename, extname } from "path";

// ─── CONFIG ──────────────────────────────────────────────────────────────────

const PDF_DIR = join(import.meta.dirname, "..", "docs", "raw-pdfs");
const PROCESSED_DIR = join(import.meta.dirname, "..", "docs", "processed");
const EMBEDDINGS_FILE = join(import.meta.dirname, "..", "docs", "embeddings.json");

const CHUNK_SIZE = 500;       // Target tokens per chunk (~2000 chars)
const CHUNK_OVERLAP = 50;     // Overlap tokens between chunks
const EMBEDDING_DIM = 384;    // Embedding dimensions

// ─── HELPERS ─────────────────────────────────────────────────────────────────

function chunkText(text, sourceName, chunkSize = CHUNK_SIZE, overlap = CHUNK_OVERLAP) {
  // Simple character-based chunking (approximation: 1 token ≈ 4 chars)
  const charSize = chunkSize * 4;
  const charOverlap = overlap * 4;
  const chunks = [];

  // Split by paragraphs first for better boundaries
  const paragraphs = text.split(/\n\s*\n/);
  let currentChunk = "";
  let chunkIndex = 0;

  for (const para of paragraphs) {
    if ((currentChunk + "\n\n" + para).length > charSize && currentChunk.length > 0) {
      chunks.push({
        id: `${sourceName}::chunk_${chunkIndex}`,
        source: sourceName,
        index: chunkIndex,
        text: currentChunk.trim(),
      });

      // Keep overlap from end of current chunk
      const words = currentChunk.split(/\s+/);
      const overlapWords = words.slice(-Math.floor(charOverlap / 5));
      currentChunk = overlapWords.join(" ") + "\n\n" + para;
      chunkIndex++;
    } else {
      currentChunk = currentChunk ? currentChunk + "\n\n" + para : para;
    }
  }

  // Don't forget last chunk
  if (currentChunk.trim()) {
    chunks.push({
      id: `${sourceName}::chunk_${chunkIndex}`,
      source: sourceName,
      index: chunkIndex,
      text: currentChunk.trim(),
    });
  }

  return chunks;
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("📚 Dr PowerScale — PDF Indexer\n");

  // Check for PDFs
  if (!existsSync(PDF_DIR)) {
    console.log(`❌ PDF directory not found: ${PDF_DIR}`);
    console.log("   Create it and add your PowerScale/Isilon PDFs there.");
    process.exit(1);
  }

  const pdfFiles = readdirSync(PDF_DIR).filter((f) => extname(f).toLowerCase() === ".pdf");

  if (pdfFiles.length === 0) {
    console.log("📭 No PDFs found in docs/raw-pdfs/");
    console.log("   Add your PowerScale/Isilon documentation PDFs there.");
    process.exit(0);
  }

  console.log(`Found ${pdfFiles.length} PDF(s):\n`);
  pdfFiles.forEach((f) => console.log(`   📄 ${f}`));
  console.log("");

  // Ensure output dirs exist
  mkdirSync(PROCESSED_DIR, { recursive: true });

  // Dynamic import for pdf-parse (ESM compatibility)
  let pdfParse;
  try {
    const pdfModule = await import("pdf-parse");
    pdfParse = pdfModule.default;
  } catch {
    console.log("❌ pdf-parse not installed. Run: npm install pdf-parse");
    process.exit(1);
  }

  const allChunks = [];

  for (const pdfFile of pdfFiles) {
    const pdfPath = join(PDF_DIR, pdfFile);
    const sourceName = basename(pdfFile, ".pdf");

    console.log(`⏳ Processing: ${pdfFile}...`);

    try {
      const buffer = readFileSync(pdfPath);
      const data = await pdfParse(buffer);
      const text = data.text;

      if (!text || text.trim().length === 0) {
        console.log(`   ⚠️  No text extracted (scanned PDF?). Skipping.`);
        continue;
      }

      const chunks = chunkText(text, sourceName);
      allChunks.push(...chunks);

      // Save human-readable markdown
      const mdContent = chunks
        .map((c) => `## ${c.id}\n\n${c.text}`)
        .join("\n\n---\n\n");
      writeFileSync(join(PROCESSED_DIR, `${sourceName}.md`), mdContent);

      console.log(`   ✅ ${chunks.length} chunks extracted`);
    } catch (err) {
      console.log(`   ❌ Error: ${err.message}`);
    }
  }

  console.log(`\n📊 Total: ${allChunks.length} chunks from ${pdfFiles.length} PDF(s)`);

  // Generate placeholder embeddings (random for now — replace with real model)
  // TODO: Replace with actual embedding model (e.g., @xenova/transformers or OpenAI embeddings)
  console.log("⏳ Generating embeddings (placeholder — replace with real model)...");

  const seededRandom = (seed) => {
    const x = Math.sin(seed) * 10000;
    return x - Math.floor(x);
  };

  for (const chunk of allChunks) {
    // Generate deterministic pseudo-embeddings based on text hash
    // REPLACE THIS with real embeddings for production use
    const hash = chunk.text.split("").reduce((acc, c) => acc + c.charCodeAt(0), 0);
    chunk.embedding = Array.from({ length: EMBEDDING_DIM }, (_, i) =>
      seededRandom(hash + i) * 2 - 1
    );
  }

  // Save embeddings index
  const index = {
    version: 1,
    chunkSize: CHUNK_SIZE,
    chunkOverlap: CHUNK_OVERLAP,
    embeddingDim: EMBEDDING_DIM,
    generatedAt: new Date().toISOString(),
    totalChunks: allChunks.length,
    chunks: allChunks.map((c) => ({
      id: c.id,
      source: c.source,
      index: c.index,
      text: c.text,
      embedding: c.embedding,
    })),
  };

  writeFileSync(EMBEDDINGS_FILE, JSON.stringify(index, null, 2));

  const fileSizeMB = (JSON.stringify(index).length / 1024 / 1024).toFixed(2);
  console.log(`\n✅ Index saved: ${EMBEDDINGS_FILE} (${fileSizeMB} MB)`);
  console.log("\n📌 Next steps:");
  console.log("   1. Replace placeholder embeddings with real model (see TODO in script)");
  console.log("   2. npm run build");
  console.log("   3. git add . && git commit && git push");
}

main().catch(console.error);
