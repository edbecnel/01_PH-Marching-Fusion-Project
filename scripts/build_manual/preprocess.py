#!/usr/bin/env python3
"""Preprocess project Markdown for Pandoc PDF manual builds."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

BREADCRUMB_RE = re.compile(r"^\[Home\].*›.*\n", re.MULTILINE)
ANGLE_LINK_RE = re.compile(
    r"\[([^\]]+)\]\(<([^>]+)>\)"
)
MARKDOWN_LINK_RE = re.compile(
    r"\[([^\]]+)\]\(([^)]+)\)"
)
CHAPTER_BREAK = "\n\n\\newpage\n\n"


def normalize_angle_bracket_links(text: str) -> str:
    return ANGLE_LINK_RE.sub(r"[\1](\2)", text)


def strip_breadcrumbs(text: str) -> str:
    return BREADCRUMB_RE.sub("", text, count=1)


def extract_markdown_sections(text: str, section_titles: list[str]) -> str:
    """Extract ## sections whose heading text matches any title in section_titles."""
    if not section_titles:
        return text

    lines = text.splitlines(keepends=True)
    title_set = set(section_titles)
    chunks: list[str] = []
    current: list[str] = []
    in_section = False
    current_title = ""

    for line in lines:
        if line.startswith("## ") and not line.startswith("### "):
            heading = line[3:].strip()
            if in_section and current:
                chunks.append("".join(current))
            if heading in title_set:
                in_section = True
                current_title = heading
                current = [line]
            else:
                in_section = False
                current = []
                current_title = ""
        elif in_section:
            current.append(line)

    if in_section and current:
        chunks.append("".join(current))

    if not chunks:
        return text

    header = "# Concept Library (excerpt)\n\n"
    header += "Selected sections for the Trainers Manual.\n\n"
    return header + "\n".join(c.strip() for c in chunks)


def resolve_link_target(href: str, source_file: Path, repo_root: Path) -> Path | None:
    """Resolve a markdown link to a repo-relative .md path."""
    href = href.strip()
    if not href or href.startswith(("http://", "https://", "mailto:")):
        return None
    if href.startswith("#"):
        return source_file.resolve()

    path_part, _, _frag = href.partition("#")
    if not path_part:
        return source_file.resolve()

    if path_part.endswith(".md"):
        target = (source_file.parent / path_part).resolve()
        if target.is_file():
            try:
                return target.relative_to(repo_root.resolve())
            except ValueError:
                return None
    return None


def rewrite_cross_volume_links(
    text: str,
    source_file: Path,
    repo_root: Path,
    current_volume_id: str,
    link_map: dict[str, dict[str, str]],
) -> str:
    """Rewrite links to other volumes as sibling PDF links."""

    def replace_match(match: re.Match[str]) -> str:
        label = match.group(1)
        href = match.group(2).strip()
        if href.startswith(("http://", "https://", "mailto:")):
            return match.group(0)

        frag = ""
        path_part = href
        if "#" in href:
            path_part, _, frag = href.partition("#")

        if path_part.startswith("#") or not path_part:
            return match.group(0)

        target_rel = resolve_link_target(href, source_file, repo_root)
        if target_rel is None:
            return match.group(0)

        key = str(target_rel).replace("\\", "/")
        entry = link_map.get(key)
        if entry is None:
            return match.group(0)

        if entry["volume_id"] == current_volume_id:
            if frag:
                return f"[{label}](#{frag})"
            return match.group(0)

        pdf_name = entry["pdf"]
        vol_title = entry.get("title", pdf_name)
        if frag:
            display = f"{label} ({vol_title})"
        else:
            display = label
        return f"[{display}]({pdf_name})"

    text = normalize_angle_bracket_links(text)
    return MARKDOWN_LINK_RE.sub(replace_match, text)


def preprocess_file(
    source: Path,
    dest: Path,
    repo_root: Path,
    volume_id: str,
    link_map: dict[str, dict[str, str]],
    extract_section_titles: list[str] | None = None,
) -> None:
    text = source.read_text(encoding="utf-8")
    text = strip_breadcrumbs(text)
    if extract_section_titles:
        text = extract_markdown_sections(text, extract_section_titles)
    text = rewrite_cross_volume_links(text, source, repo_root, volume_id, link_map)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
