#!/usr/bin/env python3
"""Generate Substack-ready mirror files from published Hugo posts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.parse import urlsplit


@dataclass
class Post:
    path: str
    title: str
    date: str
    permalink: str


def run(args: list[str]) -> str:
    proc = subprocess.run(args, check=True, capture_output=True, text=True)
    return proc.stdout


def normalize_path(value: str) -> str:
    return value.replace("\\", "/")


def parse_hugo_posts() -> list[Post]:
    output = run(["hugo", "list", "all"])
    rows = csv.DictReader(output.splitlines())
    posts: list[Post] = []
    for row in rows:
        if row.get("kind") != "page":
            continue
        if row.get("section") != "posts":
            continue
        if row.get("draft", "").strip().lower() == "true":
            continue
        source_path = normalize_path(row.get("path", ""))
        if not source_path.endswith(".md"):
            continue
        posts.append(
            Post(
                path=source_path,
                title=row.get("title", "").strip(),
                date=row.get("date", "").strip(),
                permalink=row.get("permalink", "").strip(),
            )
        )
    return posts


def changed_paths(git_range: str) -> set[str]:
    output = run(["git", "diff", "--name-only", git_range, "--", "content/posts"])
    return {
        normalize_path(line.strip())
        for line in output.splitlines()
        if line.strip().endswith(".md")
    }


def strip_frontmatter(markdown: str) -> str:
    markdown = markdown.lstrip("\ufeff")
    match = re.match(r"\A---\s*\r?\n.*?\r?\n---\s*\r?\n", markdown, flags=re.DOTALL)
    body = markdown[match.end() :] if match else markdown
    return body.lstrip("\r\n")


def _convert_inline_markdown(text: str) -> str:
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    text = re.sub(r"_(.*?)_", r"<em>\1</em>", text)
    return text


def to_substack_html(markdown: str) -> str:
    text = markdown
    # Remove editorial notes meant for drafting only.
    text = re.sub(r"^\[SUGGESTION:.*?\]\s*$", "", text, flags=re.MULTILINE)
    lines = text.splitlines()
    blocks: list[str] = []
    paragraph_lines: list[str] = []

    def flush_paragraph() -> None:
        if not paragraph_lines:
            return
        paragraph = " ".join(line.strip() for line in paragraph_lines if line.strip())
        if paragraph:
            blocks.append(f"<p>{_convert_inline_markdown(paragraph)}</p>")
        paragraph_lines.clear()

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            continue
        if re.fullmatch(r"-{3,}", stripped):
            flush_paragraph()
            continue
        heading_match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading_match:
            flush_paragraph()
            level = len(heading_match.group(1))
            heading_text = _convert_inline_markdown(heading_match.group(2).strip())
            blocks.append(f"<h{level}>{heading_text}</h{level}>")
            continue
        paragraph_lines.append(stripped)

    flush_paragraph()
    return "\n\n".join(blocks).strip()


def slug_from_permalink(permalink: str) -> str:
    path = urlsplit(permalink).path.strip("/")
    if not path:
        return "home"
    return path.replace("/", "__")


def git_remote_http_url() -> str:
    origin = run(["git", "remote", "get-url", "origin"]).strip()
    if origin.endswith(".git"):
        origin = origin[:-4]
    if origin.startswith("git@github.com:"):
        origin = "https://github.com/" + origin.split(":", 1)[1]
    return origin


def build_payload(post: Post, source_body: str, canonical_repo_url: str) -> str:
    source_link = f"{canonical_repo_url}/blob/main/{post.path}"
    html_body = to_substack_html(source_body)
    return (
        f"<p>Canonical URL: <a href=\"{post.permalink}\">{post.permalink}</a></p>\n"
        f"<p>Canonical source (GitHub): <a href=\"{source_link}\">{source_link}</a></p>\n\n"
        f"{html_body}\n"
    )


def wrap_html_document(title: str, body_html: str) -> str:
    return (
        "<!doctype html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "  <meta charset=\"utf-8\" />\n"
        f"  <title>{title}</title>\n"
        "  <style>\n"
        "    body { max-width: 760px; margin: 40px auto; font-family: Georgia, 'Times New Roman', serif; line-height: 1.65; font-size: 22px; color: #111; padding: 0 20px; }\n"
        "    h1, h2, h3, h4, h5, h6 { line-height: 1.25; margin-top: 1.5em; margin-bottom: 0.5em; }\n"
        "    p { margin: 0 0 1em; }\n"
        "    a { color: #0b57d0; }\n"
        "  </style>\n"
        "</head>\n"
        "<body>\n"
        f"{body_html}\n"
        "</body>\n"
        "</html>\n"
    )


def ensure_clean_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for child in path.iterdir():
        if child.is_file():
            child.unlink()


def hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def write_manifest(path: Path, posts: Iterable[dict[str, str]]) -> None:
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "posts": list(posts),
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate Substack-ready markdown mirror files from published Hugo posts."
    )
    parser.add_argument(
        "--output-dir",
        default=".mirror/substack/outbox",
        help="Directory where generated markdown files are written.",
    )
    parser.add_argument(
        "--git-range",
        default="",
        help="Optional git revision range (example: abc123..def456). Only changed posts are exported.",
    )
    parser.add_argument(
        "--canonical-repo-url",
        default="",
        help="Optional canonical repository URL. Defaults to git origin.",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    ensure_clean_dir(output_dir)

    canonical_repo_url = args.canonical_repo_url.strip() or git_remote_http_url()
    posts = parse_hugo_posts()
    if args.git_range.strip():
        changed = changed_paths(args.git_range.strip())
        posts = [post for post in posts if post.path in changed]

    manifest_posts: list[dict[str, str]] = []
    for post in posts:
        source = Path(post.path)
        if not source.exists():
            continue
        raw = source.read_text(encoding="utf-8-sig")
        body = strip_frontmatter(raw)
        slug = slug_from_permalink(post.permalink)
        payload = build_payload(post, body, canonical_repo_url)
        output_file = output_dir / f"{slug}.md"
        output_file.write_text(
            payload,
            encoding="utf-8",
        )
        output_html_file = output_dir / f"{slug}.html"
        output_html_file.write_text(
            wrap_html_document(post.title, payload),
            encoding="utf-8",
        )
        manifest_posts.append(
            {
                "title": post.title,
                "source_path": post.path,
                "permalink": post.permalink,
                "published_at": post.date,
                "sha256": hash_text(body),
                "output_file": normalize_path(str(output_file)),
                "output_html_file": normalize_path(str(output_html_file)),
            }
        )

    write_manifest(output_dir / "manifest.json", manifest_posts)
    print(f"Generated {len(manifest_posts)} Substack mirror file(s) in {output_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
