-- Supabase SQL for Dr PowerScale keyword search
-- Run this in Supabase SQL Editor

-- Create chunks table (keyword search version)
CREATE TABLE IF NOT EXISTS chunks (
  id TEXT PRIMARY KEY,
  source TEXT NOT NULL,
  chunk_index INT NOT NULL,
  text TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Create index for keyword search
CREATE INDEX idx_chunks_text ON chunks USING gin(to_tsvector('english', text));
CREATE INDEX idx_chunks_source ON chunks(source);

-- Enable Row Level Security (optional but recommended)
ALTER TABLE chunks ENABLE ROW LEVEL SECURITY;

-- Allow anonymous read access (for the chatbot)
CREATE POLICY "Allow anonymous read" ON chunks
  FOR SELECT USING (true);
