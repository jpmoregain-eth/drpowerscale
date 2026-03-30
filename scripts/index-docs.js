#!/usr/bin/env node

/**
 * Dr PowerScale — PDF Indexing Script
 *
 * Converts PDFs in docs/raw-pdfs/ to searchable chunks with embeddings.
 * Uses pdftotext (poppler-utils) for reliable PDF text extraction.
 *
 * Usage:
 *   node scripts/index-docs.js
 *
 * Output:
 *   - docs/processed/*.md   (human-readable chunks)
 *   - docs/embeddings.json   (machine-readable index for RAG)
 */

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

// ─── CONFIG ──────────────────────────────────────────────────────────────────

const PDF_DIR = path.join(__dirname, "..", "docs", "raw-pdfs");
const PROCESSED_DIR = path.join(__dirname, "..", "docs", "processed");
const EMBEDDINGS_FILE = path.join(__dirname, "..", "docs", "embeddings.json");

const CHUNK_SIZE = 500;       // Target tokens per chunk (~2000 chars)
const CHUNK_OVERLAP = 50;     // Overlap tokens between chunks
const EMBEDDING_DIM = 384;    // Embedding dimensions

// ─── HELPERS ─────────────────────────────────────────────────────────────────

function extractPdfText(pdfPath) {
  try {
    const text = execSync(`pdftotext -layout "${pdfPath}" -`, {
      encoding: "utf-8",
      maxBuffer: 50 * 1024 * 1024,
      timeout: 30000,
    });
    return text;
  } catch (err) {
    return null;
  }
}

function chunkText(text, sourceName, chunkSize = CHUNK_SIZE, overlap = CHUNK_OVERLAP) {
  const charSize = chunkSize * 4;
  const charOverlap = overlap * 4;
  const chunks = [];

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

      const words = currentChunk.split(/\s+/);
      const overlapWords = words.slice(-Math.floor(charOverlap / 5));
      currentChunk = overlapWords.join(" ") + "\n\n" + para;
      chunkIndex++;
    } else {
      currentChunk = currentChunk ? currentChunk + "\n\n" + para : para;
    }
  }

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

function seededRandom(seed) {
  const x = Math.sin(seed) * 10000;
  return x - Math.floor(x);
}

// ─── MAIN ────────────────────────────────────────────────────────────────────

async function main() {
  console.log("📚 Dr PowerScale — PDF Indexer (pdftotext)\n");

  if (!fs.existsSync(PDF_DIR)) {
    console.log(`❌ PDF directory not found: ${PDF_DIR}`);
    process.exit(1);
  }

  const pdfFiles = fs.readdirSync(PDF_DIR).filter((f) => path.extname(f).toLowerCase() === ".pdf");

  if (pdfFiles.length === 0) {
    console.log("📭 No PDFs found in docs/raw-pdfs/");
    process.exit(0);
  }

  console.log(`Found ${pdfFiles.length} PDF(s):\n`);
  pdfFiles.forEach((f) => {
    const size = (fs.statSync(path.join(PDF_DIR, f)).size / 1024).toFixed(0);
    console.log(`   📄 ${f} (${size} KB)`);
  });
  console.log("");

  fs.mkdirSync(PROCESSED_DIR, { recursive: true });

  const allChunks = [];
  let successCount = 0;
  let failCount = 0;

  for (const pdfFile of pdfFiles) {
    const pdfPath = path.join(PDF_DIR, pdfFile);
    const sourceName = path.basename(pdfFile, ".pdf");

    process.stdout.write(`⏳ ${pdfFile}...`);

    const text = extractPdfText(pdfPath);

    if (!text || text.trim().length === 0) {
      console.log(` ⚠️  No text extracted`);
      failCount++;
      continue;
    }

    const chunks = chunkText(text, sourceName);
    allChunks.push(...chunks);

    const mdContent = chunks
      .map((c) => `## ${c.id}\n\n${c.text}`)
      .join("\n\n---\n\n");
    fs.writeFileSync(path.join(PROCESSED_DIR, `${sourceName}.md`), mdContent);

    console.log(` ✅ ${chunks.length} chunks`);
    successCount++;
  }

  console.log(`\n📊 Results: ${successCount} OK, ${failCount} failed`);
  console.log(`   ${allChunks.length} total chunks`);

  // Generate placeholder embeddings
  console.log("⏳ Generating placeholder embeddings...");

  for (const chunk of allChunks) {
    const hash = chunk.text.split("").reduce((acc, c) => acc + c.charCodeAt(0), 0);
    chunk.embedding = Array.from({ length: EMBEDDING_DIM }, (_, i) =>
      seededRandom(hash + i) * 2 - 1
    );
  }

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

  fs.writeFileSync(EMBEDDINGS_FILE, JSON.stringify(index));

  const fileSizeMB = (fs.statSync(EMBEDDINGS_FILE).size / 1024 / 1024).toFixed(2);
  console.log(`\n✅ Index saved: ${EMBEDDINGS_FILE} (${fileSizeMB} MB)`);
  console.log(`   ${allChunks.length} chunks from ${successCount}/${pdfFiles.length} PDFs`);
  console.log("\n📌 Next: npm run build && git add . && git commit && git push");
}

main().catch(console.error);
