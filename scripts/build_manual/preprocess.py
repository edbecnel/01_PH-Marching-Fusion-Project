#!/usr/bin/env python3
"""Preprocess project Markdown for Pandoc PDF manual builds."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

BREADCRUMB_RE = re.compile(r"^\[Home\].*›.*\n", re.MULTILINE)
ANGLE_LINK_RE = re.compile(r"\[([^\]]+)\]\(<([^>]+)>\)")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def normalize_angle_bracket_links(text: str) -> str:
    return ANGLE_LINK_RE.sub(r"[\1](\2)", text)


def strip_breadcrumbs(text: str) -> str:
    return BREADCRUMB_RE.sub("", text, count=1)


def file_anchor(rel_path: str) -> str:
    """Stable in-PDF anchor from a source file path (e.g. docs/Reference/Legato_Stroke.md)."""
    stem = Path(rel_path).stem.lower().replace("_", "-")
    return re.sub(r"[^a-z0-9-]+", "-", stem).strip("-")


def slugify_heading(text: str) -> str:
    """Approximate Pandoc auto-identifiers for heading fragments."""
    text = re.sub(r"^\d+\.\s*", "", text.strip())
    text = text.lower()
    text = text.replace("—", "-").replace("–", "-")
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def inject_chapter_anchor(text: str, rel_path: str) -> str:
    """Add Pandoc header ID on first # heading for intra-PDF jumps."""
    anchor = file_anchor(rel_path)
    lines = text.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if line.startswith("# ") and not line.startswith("## "):
            if "{#" in line:
                return text
            stripped = line.rstrip("\n")
            lines[i] = f"{stripped} {{#{anchor}}}\n"
            return "".join(lines)
    return text


def extract_markdown_sections(text: str, section_titles: list[str]) -> str:
    """Extract ## sections whose heading text matches any title in section_titles."""
    if not section_titles:
        return text

    lines = text.splitlines(keepends=True)
    title_set = set(section_titles)
    chunks: list[str] = []
    current: list[str] = []
    in_section = False

    for line in lines:
        if line.startswith("## ") and not line.startswith("### "):
            heading = line[3:].strip()
            if in_section and current:
                chunks.append("".join(current))
            if heading in title_set:
                in_section = True
                current = [line]
            else:
                in_section = False
                current = []
        elif in_section:
            current.append(line)

    if in_section and current:
        chunks.append("".join(current))

    if not chunks:
        return text

    header = "# Concept Library (excerpt)\n\n"
    header += "Selected sections for the Trainers Manual.\n\n"
    return header + "\n".join(c.strip() for c in chunks)


def resolve_link_target(href: str, source_file: Path, repo_root: Path) -> str | None:
    """Resolve a markdown link to a repo-relative path string."""
    href = href.strip()
    if not href or href.startswith(("http://", "https://", "mailto:")):
        return None
    if href.startswith("#"):
        return None

    path_part, _, _frag = href.partition("#")
    if not path_part:
        return None

    if not path_part.endswith(".md"):
        return None

    target = (source_file.parent / path_part).resolve()
    repo_root = repo_root.resolve()
    if target.is_file():
        try:
            return str(target.relative_to(repo_root)).replace("\\", "/")
        except ValueError:
            pass

    # Fallback: strip leading .. segments and resolve under repo root
    # (handles ../../../scores/... style links from docs/User_Guides/)
    parts = path_part.replace("\\", "/").split("/")
    while parts and parts[0] == "..":
        parts.pop(0)
    suffix = "/".join(parts)
    candidate = repo_root / suffix
    if candidate.is_file():
        return suffix

    return None


def lookup_registry(path: str, registry: dict[str, Any]) -> dict[str, Any] | None:
    entries = registry.get("entries", {})
    if path in entries:
        return entries[path]
    # Match by filename for root-relative links from nested docs
    name = Path(path).name
    for key, val in entries.items():
        if key == name or key.endswith("/" + name):
            return val
    return None


# When a source file appears in multiple volumes, prefer these targets for cross-PDF links.
VOLUME_LINK_PRIORITY: dict[str, int] = {
    "specifications": 10,
    "reference": 20,
    "user_guides": 30,
    "students": 35,
    "research": 40,
    "architecture": 50,
    "governance": 60,
    "ai_development": 70,
    "templates_placeholders": 80,
    "trainers": 90,
}


def pick_cross_volume_entry(
    volumes: dict[str, dict[str, str]], current_volume_id: str
) -> dict[str, str] | None:
    candidates = [
        (VOLUME_LINK_PRIORITY.get(vid, 50), entry)
        for vid, entry in volumes.items()
        if vid != current_volume_id
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0])
    return candidates[0][1]


def rewrite_manual_links(
    text: str,
    source_file: Path,
    repo_root: Path,
    current_volume_id: str,
    link_map: dict[str, dict[str, dict[str, str]]],
    link_registry: dict[str, Any],
) -> str:
    """Rewrite .md links for PDF: in-volume anchors, sibling PDFs, or repository notes."""

    def replace_match(match: re.Match[str]) -> str:
        label = match.group(1)
        href = match.group(2).strip()
        if href.startswith(("http://", "https://", "mailto:")):
            return match.group(0)

        frag = ""
        path_part = href
        if "#" in href:
            path_part, _, frag = href.partition("#")

        if href.startswith("#") or (not path_part and frag):
            slug = slugify_heading(frag or href.lstrip("#"))
            return f"[{label}](#{slug})" if slug else match.group(0)

        if not path_part:
            return match.group(0)

        target_rel = resolve_link_target(href, source_file, repo_root)
        if target_rel is None:
            return match.group(0)

        volumes = link_map.get(target_rel)
        if volumes:
            if current_volume_id in volumes:
                anchor = file_anchor(target_rel)
                if frag:
                    heading_slug = slugify_heading(frag)
                    return f"[{label}](#{heading_slug})"
                return f"[{label}](#{anchor})"

            entry = pick_cross_volume_entry(volumes, current_volume_id)
            if entry:
                pdf_name = entry["pdf"]
                vol_title = entry.get("title", pdf_name)
                if frag:
                    return f"[{label} ({vol_title})]({pdf_name})"
                return f"[{label} ({vol_title})]({pdf_name})"

        reg = lookup_registry(target_rel, link_registry)
        if reg and reg.get("type") == "repository":
            note = reg.get("note", "see project repository")
            return f"{label} *({note})*"
        if reg and reg.get("type") == "pdf":
            pdf_name = reg["pdf"]
            vol_title = reg.get("title", pdf_name)
            return f"[{label} ({vol_title})]({pdf_name})"

        # Exists on disk but not exported to any PDF volume
        return f"{label} *(not included in PDF manual; see project repository)*"

    text = normalize_angle_bracket_links(text)
    return MARKDOWN_LINK_RE.sub(replace_match, text)


def preprocess_file(
    source: Path,
    dest: Path,
    repo_root: Path,
    volume_id: str,
    link_map: dict[str, dict[str, dict[str, str]]],
    link_registry: dict[str, Any],
    rel_path: str,
    extract_section_titles: list[str] | None = None,
) -> None:
    text = source.read_text(encoding="utf-8")
    text = strip_breadcrumbs(text)
    if extract_section_titles:
        text = extract_markdown_sections(text, extract_section_titles)
    else:
        text = inject_chapter_anchor(text, rel_path)
    text = rewrite_manual_links(
        text, source, repo_root, volume_id, link_map, link_registry
    )
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
