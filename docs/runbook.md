# Runbook

- `hugo server -D` - Start the local development server with drafts enabled; expected: site available at http://localhost:1313.
- For posts with audio, keep the MP3 in `static/audio/` and set its `/audio/<file>.mp3` path in the post's `narration` frontmatter field; expected: a native player below the post title and metadata.
- `hugo --minify --baseURL "https://arielassaf.com/"` - Build the production site into `./public` with minified assets; expected: fresh static bundle ready to deploy.
- `hugo --minify && touch public/.nojekyll && cp static/CNAME public/` - Reproduce the GitHub Pages build locally; expected: bundle includes `.nojekyll` and `CNAME` for custom domain.
- `python scripts/substack_mirror.py` - Generate Substack-ready markdown files for all published posts into `.mirror/substack/outbox`; expected: one file per post plus `manifest.json`.
- `python scripts/substack_mirror.py --git-range "<old_sha>..<new_sha>"` - Generate Substack-ready markdown only for changed published posts; expected: outbox contains just mirrored changes for that revision range.
- `git submodule update --init --recursive` - Ensure the PaperMod theme submodule is present; expected: `themes/PaperMod` populated before running Hugo.
- `git push origin main` - Trigger GitHub Pages workflow after changes land on `main`; expected: Actions workflow redeploys the site to `https://arielassaf.com`.
- `git push origin main` also triggers `Build Substack Mirror Package`, which uploads a `substack-mirror-<sha>` artifact containing files ready to paste into Substack.
