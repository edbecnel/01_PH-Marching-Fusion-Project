#!/usr/bin/env python3
"""Load manual manifests and resolve source Markdown to PDF volumes."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterator

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]

REPO_ROOT = Path(__file__).resolve().parents[2]
MANUAL_DIR = REPO_ROOT / "manual"

MANIFEST_FILES = (
    ("manifest.yaml", "main"),
    ("trainers-manifest.yaml", "trainers"),
    ("students-manifest.yaml", "students"),
)


def load_yaml(path: Path) -> dict[str, Any]:
    if yaml is None:
        raise RuntimeError("PyYAML required: pip install pyyaml")
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def parse_manifest_files(vol: dict[str, Any]) -> list[tuple[str, list[str] | None]]:
    result: list[tuple[str, list[str] | None]] = []
    for entry in vol.get("files", []):
        if isinstance(entry, str):
            result.append((entry, None))
        elif isinstance(entry, dict):
            path = entry.get("path")
            if not path:
                continue
            sections = None
            extract = entry.get("extract")
            if isinstance(extract, dict):
                sections = extract.get("sections")
            result.append((path, sections))
    return result


def slugify_heading(text: str) -> str:
    text = re.sub(r"^\d+\.\s*", "", text.strip())
    text = text.lower()
    text = text.replace("—", "-").replace("–", "-")
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", "-", text).strip("-")


def read_first_heading(source_path: Path) -> str | None:
    if not source_path.is_file():
        return None
    for line in source_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            return line[2:].strip().split("{#", 1)[0].strip()
    return None


def iter_volume_file_entries(
    vol: dict[str, Any],
    version: str = "2026.07",
) -> list[dict[str, Any]]:
    """Return ordered build entries for one volume (mirrors build_manual.py)."""
    vol_id = vol["id"]
    pdf_name = vol["pdf"]
    file_list = parse_manifest_files(vol)
    entries: list[dict[str, Any]] = []
    prev_prefix: str | None = None

    entries.append(
        {
            "order": 0,
            "source": None,
            "interim": f".build/manual/{version}/{vol_id}/00-cover.md",
            "pdf": pdf_name,
            "vol_id": vol_id,
            "notes": "Generated cover page",
        }
    )

    for i, (rel_path, sections) in enumerate(file_list, start=1):
        prefix = "/".join(rel_path.split("/")[:2])
        if (
            prev_prefix == "docs/User_Guides"
            and prefix == "docs/Reference"
            and vol_id in ("user_guides", "students")
        ):
            sep_num = len(entries)
            entries.append(
                {
                    "order": sep_num,
                    "source": None,
                    "interim": (
                        f".build/manual/{version}/{vol_id}/"
                        f"{sep_num:02d}-appendix-technique-header.md"
                    ),
                    "pdf": pdf_name,
                    "vol_id": vol_id,
                    "notes": "Generated divider before embedded Reference chapters",
                }
            )

        notes: list[str] = []
        if sections:
            section_list = ", ".join(f"`{s}`" for s in sections)
            notes.append(f"Section extract only: {section_list}")

        entries.append(
            {
                "order": i,
                "source": rel_path,
                "interim": (
                    f".build/manual/{version}/{vol_id}/"
                    f"{i:02d}-{Path(rel_path).name}"
                ),
                "pdf": pdf_name,
                "vol_id": vol_id,
                "notes": "; ".join(notes) if notes else "",
            }
        )
        prev_prefix = prefix

    return entries


def load_all_volumes() -> list[dict[str, Any]]:
    volumes: list[dict[str, Any]] = []
    for filename, _kind in MANIFEST_FILES:
        path = MANUAL_DIR / filename
        if not path.is_file():
            continue
        manifest = load_yaml(path)
        volumes.extend(manifest.get("volumes", []))
    return volumes


def build_source_index(version: str = "2026.07") -> dict[str, list[dict[str, Any]]]:
    """Map each source .md path to every volume entry that embeds it."""
    index: dict[str, list[dict[str, Any]]] = {}
    for vol in load_all_volumes():
        for entry in iter_volume_file_entries(vol, version):
            source = entry.get("source")
            if not source:
                continue
            index.setdefault(source, []).append(entry)
    return index


def lookup_by_pdf_section(
    pdf: str,
    section: str,
    version: str = "2026.07",
) -> list[dict[str, Any]]:
    """Find source files whose first # heading matches section (fuzzy)."""
    if not pdf.endswith(".pdf"):
        pdf = f"{pdf}.pdf" if not pdf.endswith(".pdf") else pdf

    section_slug = slugify_heading(section)
    matches: list[dict[str, Any]] = []

    for vol in load_all_volumes():
        vol_pdf = vol.get("pdf", "")
        if vol_pdf != pdf and not vol_pdf.endswith(pdf) and not pdf.endswith(vol_pdf):
            continue
        for entry in iter_volume_file_entries(vol, version):
            source = entry.get("source")
            if not source:
                continue
            heading = read_first_heading(REPO_ROOT / source)
            if not heading:
                continue
            heading_slug = slugify_heading(heading)
            if (
                section.lower() in heading.lower()
                or section_slug == heading_slug
                or section_slug in heading_slug
                or heading_slug in section_slug
            ):
                matches.append(
                    {
                        **entry,
                        "heading": heading,
                        "vol_title": vol.get("title", ""),
                    }
                )
    return matches


def lookup_by_source(source: str, version: str = "2026.07") -> list[dict[str, Any]]:
    source = source.replace("\\", "/").lstrip("./")
    index = build_source_index(version)
    return index.get(source, [])
