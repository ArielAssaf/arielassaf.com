# Runbook

- `hugo server -D` - Start the local development server with drafts enabled; expected: site available at http://localhost:1313.
- `hugo --minify --baseURL "https://arielassaf.com/"` - Build the production site into `./public` with minified assets; expected: fresh static bundle ready to deploy.
- `hugo --minify && touch public/.nojekyll && cp static/CNAME public/` - Reproduce the GitHub Pages build locally; expected: bundle includes `.nojekyll` and `CNAME` for custom domain.
- `git submodule update --init --recursive` - Ensure the PaperMod theme submodule is present; expected: `themes/PaperMod` populated before running Hugo.
- `git push origin main` - Trigger GitHub Pages workflow after changes land on `main`; expected: Actions workflow redeploys the site to `https://arielassaf.com`.
