# Architectural Overview

## Core Stack
- Static site generator: Hugo (`hugo.toml`)
- Theme: PaperMod (`themes/PaperMod` submodule)
- Content source: Markdown files in `content/posts`
- Hosting/deploy: GitHub Pages via `.github/workflows/hugo.yml`

## Publishing Model
- Canonical source of truth is this GitHub repository (`main` branch).
- Canonical public URLs are served from `https://arielassaf.com`.
- Substack is a mirror channel, not the canonical origin.

## Substack Mirror Flow
- Generator script: `scripts/substack_mirror.py`
- Input: published posts from `hugo list all` (`draft: false`, section `posts`)
- Output: `.mirror/substack/outbox/*.md` and `.mirror/substack/outbox/manifest.json`
- Generated markdown includes:
  - canonical post URL on `arielassaf.com`
  - canonical source link back to GitHub (`blob/main/...`)
- CI workflow: `.github/workflows/substack-mirror.yml`
  - Runs on `main` pushes that touch posts
  - Uploads `substack-mirror-<sha>` artifact with ready-to-paste files
