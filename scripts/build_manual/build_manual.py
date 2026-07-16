#!/usr/bin/env python3
"""Build multi-volume PDF manuals from project Markdown documentation."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

from preprocess import preprocess_file

REPO_ROOT = Path(__file__).resolve().parents[2]
MANUAL_DIR = REPO_ROOT / "manual"
TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

ALL_VOLUMES = [
    ("00-Trainers-Manual.pdf", "Trainers Manual", "Field teaching handbook for instructors and pilot collaborators"),
    ("01-Specifications.pdf", "Specifications", "Identity framework, blueprint, design principles, notation standards"),
    ("02-Reference.pdf", "Reference", "Concept library, technique, grids, sound model"),
    ("03-User-Guides.pdf", "User Guides", "Instructor, pilot, arranging, and educational guidance"),
    ("04-Research.pdf", "Research", "Indigenous percussion, Kaamulan, marching heritage"),
    ("05-Architecture.pdf", "Architecture", "Documentation architecture and ADRs"),
    ("06-Governance.pdf", "Governance", "EDF governance, metadata, change management"),
    ("07-AI-Development.pdf", "AI and Development", "AI-assisted workflow and project development notes"),
    ("08-Templates-and-Placeholders.pdf", "Templates and EDF Placeholders", "Templates and inactive EDF domain placeholders"),
]


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_docs_md(repo_root: Path) -> set[str]:
    return {
        str(p.relative_to(repo_root)).replace("\\", "/")
        for p in (repo_root / "docs").rglob("*.md")
    }


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


def build_link_map_from_manifests(
    main: dict[str, Any], trainers: dict[str, Any]
) -> dict[str, dict[str, str]]:
    link_map: dict[str, dict[str, str]] = {}
    for manifest in (main, trainers):
        for vol in manifest.get("volumes", []):
            for path, _ in parse_manifest_files(vol):
                link_map[path] = {
                    "volume_id": vol["id"],
                    "pdf": vol["pdf"],
                    "title": vol["title"],
                }
    return link_map


def validate_manifest(repo_root: Path, main: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    docs_files = collect_docs_md(repo_root)
    manifest_files: set[str] = set()
    for vol in main.get("volumes", []):
        for path, _ in parse_manifest_files(vol):
            manifest_files.add(path)
            if not (repo_root / path).is_file():
                errors.append(f"Missing file: {path}")
    missing = docs_files - manifest_files
    extra = manifest_files - docs_files
    for m in sorted(missing):
        errors.append(f"docs/ file not in manifest.yaml: {m}")
    for e in sorted(extra):
        if not (repo_root / e).is_file():
            errors.append(f"manifest.yaml lists missing file: {e}")
    return errors


def git_commit(repo_root: Path) -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def find_pdf_engine() -> list[str]:
    for engine in ("tectonic", "pdflatex", "xelatex", "lualatex"):
        if shutil.which(engine):
            return ["--pdf-engine", engine]
    return []


def render_cover(
    volume_title: str,
    version: str,
    description: str,
    logo_rel: str = "assets/ph-marching-fusion-logo.png",
) -> str:
    lines = [
        "---",
        f'title: "Philippine Marching Percussion Fusion"',
        f'subtitle: "{volume_title}"',
        "---",
        "",
    ]
    logo_path = REPO_ROOT / logo_rel
    if logo_path.is_file():
        lines.append(f"![]({logo_rel})")
        lines.append("")
    lines.append(f"**Release:** {version}")
    lines.append("")
    lines.append(f"*{description}*")
    lines.append("")
    lines.append("## Manual volumes in this release")
    lines.append("")
    lines.append("| PDF | Description |")
    lines.append("|-----|-------------|")
    for pdf, _title, desc in ALL_VOLUMES:
        lines.append(f"| {pdf} | {desc} |")
    lines.append("")
    return "\n".join(lines)


def build_volume(
    vol: dict[str, Any],
    version: str,
    output_dir: Path,
    build_dir: Path,
    link_map: dict[str, dict[str, str]],
    repo_root: Path,
) -> Path:
    vol_id = vol["id"]
    pdf_name = vol["pdf"]
    title = vol["title"]
    description = vol.get("description", title)
    out_pdf = output_dir / pdf_name

    vol_build = build_dir / vol_id
    if vol_build.exists():
        shutil.rmtree(vol_build)
    vol_build.mkdir(parents=True)

    processed: list[Path] = []
    cover_path = vol_build / "00-cover.md"
    cover_path.write_text(
        render_cover(title, version, description), encoding="utf-8"
    )
    processed.append(cover_path)

    for i, (rel_path, sections) in enumerate(parse_manifest_files(vol), start=1):
        src = repo_root / rel_path
        dest = vol_build / f"{i:02d}-{Path(rel_path).name}"
        preprocess_file(
            src,
            dest,
            repo_root,
            vol_id,
            link_map,
            extract_section_titles=sections,
        )
        processed.append(dest)

    pandoc_args = [
        "pandoc",
        *[str(p) for p in processed],
        "-o",
        str(out_pdf),
        "--from=markdown",
        "--toc",
        "--toc-depth=3",
        "--number-sections",
        "-V",
        "geometry:margin=1in",
        "-V",
        "fontsize=11pt",
        "-V",
        "linkcolor:blue",
        "-V",
        "urlcolor:blue",
        "--resource-path",
        f"{repo_root}:{repo_root / 'docs'}:{repo_root / 'assets'}",
        "--metadata",
        f"title=Philippine Marching Percussion Fusion — {title}",
    ]

    engine_args = find_pdf_engine()
    if not engine_args:
        print(
            "ERROR: No PDF engine found. Install tectonic: brew install tectonic",
            file=sys.stderr,
        )
        sys.exit(1)
    pandoc_args.extend(engine_args)

    header = TEMPLATE_DIR / "header.tex"
    if header.is_file():
        pandoc_args.extend(["-H", str(header)])

    print(f"Building {pdf_name} ...")
    subprocess.run(pandoc_args, cwd=repo_root, check=True)
    return out_pdf


def main() -> None:
    parser = argparse.ArgumentParser(description="Build PDF manuals from docs/")
    parser.add_argument("--version", default="unreleased", help="Release version label")
    parser.add_argument(
        "--volume", help="Build single volume id (e.g. reference, trainers)"
    )
    parser.add_argument("--trainers", action="store_true", help="Build trainers manual only")
    parser.add_argument(
        "--validate", action="store_true", help="Validate manifest only"
    )
    args = parser.parse_args()

    main_manifest = load_yaml(MANUAL_DIR / "manifest.yaml")
    trainers_manifest = load_yaml(MANUAL_DIR / "trainers-manifest.yaml")

    if args.validate:
        errors = validate_manifest(REPO_ROOT, main_manifest)
        if errors:
            print("Validation failed:", file=sys.stderr)
            for e in errors:
                print(f"  - {e}", file=sys.stderr)
            sys.exit(1)
        print("manifest.yaml: OK (all docs/**/*.md accounted for)")
        for vol in trainers_manifest["volumes"]:
            for path, _ in parse_manifest_files(vol):
                if not (REPO_ROOT / path).is_file():
                    print(f"trainers-manifest: missing {path}", file=sys.stderr)
                    sys.exit(1)
        print("trainers-manifest.yaml: OK")
        return

    if not shutil.which("pandoc"):
        print("ERROR: pandoc not found", file=sys.stderr)
        sys.exit(1)

    version = args.version
    output_dir = REPO_ROOT / "dist" / "manual" / version
    build_dir = REPO_ROOT / ".build" / "manual" / version
    output_dir.mkdir(parents=True, exist_ok=True)

    link_map = build_link_map_from_manifests(main_manifest, trainers_manifest)

    built: list[str] = []

    domain_volumes = sorted(
        main_manifest["volumes"], key=lambda v: v.get("order", 99)
    )
    trainers_volumes = trainers_manifest["volumes"]

    if args.trainers:
        to_build = trainers_volumes
    elif args.volume:
        to_build = [
            v
            for v in domain_volumes + trainers_volumes
            if v["id"] == args.volume
        ]
        if not to_build:
            print(f"Unknown volume id: {args.volume}", file=sys.stderr)
            sys.exit(1)
    else:
        to_build = domain_volumes + trainers_volumes

    for vol in to_build:
        pdf = build_volume(vol, version, output_dir, build_dir, link_map, REPO_ROOT)
        built.append(pdf.name)

    record = {
        "version": version,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_commit(REPO_ROOT),
        "pdfs": built,
        "link_map_keys": len(link_map),
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(record, indent=2), encoding="utf-8"
    )
    print(f"\nDone. {len(built)} PDF(s) in {output_dir}")


if __name__ == "__main__":
    main()
