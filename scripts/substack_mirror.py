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
    match = re.match(r"\A---\s*\r?\n.*?\r?\n---\s*\r?\n", markdown, flags=re.DOTALL)
    body = markdown[match.end() :] if match else markdown
    return body.lstrip("\r\n")


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
    return (
        f"# {post.title}\n\n"
        f"> Canonical URL: {post.permalink}\n"
        f"> Canonical source (GitHub): {source_link}\n\n"
        f"---\n\n"
        f"{source_body.rstrip()}\n"
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
        raw = source.read_text(encoding="utf-8")
        body = strip_frontmatter(raw)
        slug = slug_from_permalink(post.permalink)
        output_file = output_dir / f"{slug}.md"
        output_file.write_text(
            build_payload(post, body, canonical_repo_url),
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
            }
        )

    write_manifest(output_dir / "manifest.json", manifest_posts)
    print(f"Generated {len(manifest_posts)} Substack mirror file(s) in {output_dir}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
