# Developer Guide

## Local Workflow
- Create or edit posts in `content/posts/*.md`.
- Mark posts live with frontmatter `draft: false`.
- For interactive simulations, place HTML files in `static/simulations/*.html` and embed with:
  - `{{< simulation src="/simulations/<file>.html" title="..." height="620" >}}`
- Validate build:
  - `hugo --minify --baseURL "https://arielassaf.com/"`
- Generate Substack mirror package:
  - `python scripts/substack_mirror.py`

## Mirroring to Substack
- Open generated files in `.mirror/substack/outbox`.
- Paste content into Substack post editor.
- Keep the generated canonical lines at the top so the original source remains explicit.

## CI Automation
- `git push origin main` triggers:
  - GitHub Pages deploy (`.github/workflows/hugo.yml`)
  - Substack mirror package build (`.github/workflows/substack-mirror.yml`)
- Download the `substack-mirror-<sha>` artifact from Actions to get changed mirror files.

## Edit Guardrails
- Keep changes surgical; avoid refactoring unrelated files.
- If publishing flow changes, update:
  - `docs/runbook.md`
  - `docs/purpose.md`
  - `.agent/ARCHITECTURAL_OVERVIEW.md`
  - `.agent/DEVELOPER_GUIDE.md`
