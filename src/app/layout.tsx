import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Dr PowerScale — AI Storage Assistant",
  description:
    "AI-powered assistant for Dell PowerScale and Isilon NAS storage. Get answers about OneFS, SmartConnect, SyncIQ, deduplication, snapshots, and more.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
