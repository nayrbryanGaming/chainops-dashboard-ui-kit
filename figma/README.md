# Figma Workflow Guide

This kit ships with **design tokens** and **HTML/CSS screens** you can recreate or import into Figma.

## Option A — Recreate from tokens (recommended)

1. Open Figma → create new file: `ChainOps Dashboard UI Kit`
2. Import colors from `design-tokens/tokens.json`
3. Create Figma Variables:
   - `color/bg/base` → `#070b14`
   - `color/accent/cyan` → `#22d3ee`
   - `color/accent/purple` → `#a78bfa`
4. Set typography:
   - **DM Sans** (UI)
   - **JetBrains Mono** (code / hashes)
5. Use `preview/*.html` as visual reference while rebuilding frames

## Option B — HTML to Figma plugins

Use plugins like **html.to.design** with local files:
1. Serve preview folder locally (`npx serve preview`)
2. Import key screens into Figma for editable layers

## Suggested Figma page structure

- 🎨 Cover
- 🧩 Components
- 🔐 Auth
- 📊 Dashboard
- ⛓️ Web3
- 🤖 AI Ops
- ⚙️ Settings
- 💰 Marketing

## Premium bundle tip

Export your Figma file as `.fig` and bundle with this kit at **$69–$79** on Gumroad.
