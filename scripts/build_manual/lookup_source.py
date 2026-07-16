#!/usr/bin/env python3
"""Reverse lookup: PDF volume + section -> source Markdown path."""

from __future__ import annotations

import argparse
import sys

from manifest_index import (
    REPO_ROOT,
    build_source_index,
    lookup_by_pdf_section,
    lookup_by_source,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Trace PDF manual content back to source Markdown files."
    )
    parser.add_argument(
        "--version",
        default="2026.07",
        help="Release version label for interim paths (default: 2026.07)",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--pdf",
        help="PDF filename (e.g. 02-Reference.pdf) for section lookup",
    )
    group.add_argument(
        "--source",
        help="Source path (e.g. docs/Reference/Concept_Library.md) for PDF lookup",
    )
    parser.add_argument(
        "--section",
        help="Section title or heading fragment (required with --pdf)",
    )
    args = parser.parse_args()

    if args.pdf and not args.section:
        parser.error("--section is required when using --pdf")

    if args.source:
        entries = lookup_by_source(args.source, args.version)
        if not entries:
            print(f"No PDF volumes embed: {args.source}", file=sys.stderr)
            sys.exit(1)
        print(f"Source: {args.source}")
        print(f"Embedded in {len(entries)} volume(s):\n")
        for e in entries:
            note = f"  ({e['notes']})" if e.get("notes") else ""
            print(f"  {e['pdf']}{note}")
            print(f"    interim: {e['interim']}")
        return

    matches = lookup_by_pdf_section(args.pdf, args.section, args.version)
    if not matches:
        print(
            f"No source found for section '{args.section}' in {args.pdf}",
            file=sys.stderr,
        )
        print(
            "\nTip: use exact or partial heading text from the PDF table of contents.",
            file=sys.stderr,
        )
        print(
            "See manual/SOURCE_TO_PDF_MAPPING.md for full volume tables.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"PDF: {args.pdf}")
    print(f"Section query: {args.section}")
    print(f"Matches: {len(matches)}\n")
    for m in matches:
        note = f"  notes: {m['notes']}" if m.get("notes") else ""
        print(f"  source:  {m['source']}")
        print(f"  heading: {m.get('heading', '(unknown)')}")
        print(f"  interim: {m['interim']}{note}")
        print()


if __name__ == "__main__":
    main()
