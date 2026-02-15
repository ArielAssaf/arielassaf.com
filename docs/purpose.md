# Purpose & Functionality

- Personal blog for Ariel Assaf sharing essays and thought pieces on AI, technology, and related topics.
- Built with Hugo (PaperMod theme) to publish markdown posts under `content/posts`.
- Content flows from Markdown files through Hugo builds into static assets deployed via GitHub Pages to `https://arielassaf.com`.
- GitHub remains the canonical source of truth for posts; Substack is treated as a mirrored distribution channel.
- Substack mirror packages are generated from published Hugo posts by `scripts/substack_mirror.py` and can be produced locally or via GitHub Actions artifacts.
- Comments are enabled site-wide using the PaperMod integrations configured in `hugo.toml`.
