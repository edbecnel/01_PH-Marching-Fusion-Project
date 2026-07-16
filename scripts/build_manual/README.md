# PDF Manual Build

Build multi-volume PDF manuals and the **Trainers Manual** from project Markdown.

**Maintainers:** see [PDF maintainer workflow](../../manual/MAINTAINER_WORKFLOW.md) for trace-back from PDF errors to source `.md` files and how to interpret build warnings.

## Requirements

- [Pandoc](https://pandoc.org/) 3.x — `brew install pandoc`
- [Tectonic](https://tectonic-typesetting.github.io/) — `brew install tectonic` (Unicode LaTeX engine; lighter than full MacTeX), or `xelatex` / `lualatex` from MacTeX
- Python 3 with PyYAML
- Bundled fonts in [`assets/fonts/`](../../assets/fonts/) (Noto Sans + Noto Sans Mono; included in the repo)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/build_manual/requirements.txt
```

If your Python already includes PyYAML (e.g. Anaconda), you can skip the venv.

## Quick start

From the repository root:

```bash
python3 scripts/build_manual/build_manual.py --validate
python3 scripts/build_manual/build_manual.py --version 2026.07
```

Output: `dist/manual/2026.07/*.pdf` (10 PDFs)

## Commands

| Command | Purpose |
|---------|---------|
| `--validate` | Ensure every `docs/**/*.md` file is listed in `manual/manifest.yaml` |
| `--version 2026.07` | Label for output folder and cover pages |
| `--volume reference` | Build one domain volume by id |
| `--trainers` | Build only `00-Trainers-Manual.pdf` |
| `--students` | Build only `09-Student-Practice-Guide.pdf` |
| `lookup_source.py` | Trace PDF section or source path to manifests (see below) |
| `generate_source_mapping.py` | Regenerate `manual/SOURCE_TO_PDF_MAPPING.md` from YAML |

## Trace PDF content to source Markdown

```bash
# PDF + section heading -> source file
python3 scripts/build_manual/lookup_source.py --pdf 02-Reference.pdf --section "Concept Library"

# Source file -> which PDFs embed it
python3 scripts/build_manual/lookup_source.py --source docs/Reference/Concept_Library.md
```

Full workflow: [PDF maintainer workflow](../../manual/MAINTAINER_WORKFLOW.md). Mapping tables: [SOURCE_TO_PDF_MAPPING.md](../../manual/SOURCE_TO_PDF_MAPPING.md).

Regenerate mapping after manifest edits:

```bash
python3 scripts/build_manual/generate_source_mapping.py
```

## Release PDFs

| File | Contents |
|------|----------|
| `00-Trainers-Manual.pdf` | Curated field handbook (see `manual/trainers-manifest.yaml`) |
| `01-Specifications.pdf` | Identity framework, blueprint, design, notation |
| `02-Reference.pdf` | Concept library, technique, sound model |
| `03-User-Guides.pdf` | Instructor, pilot, arranging, education |
| `04-Research.pdf` | Indigenous percussion, Kaamulan, heritage |
| `05-Architecture.pdf` | Documentation architecture, ADRs |
| `06-Governance.pdf` | EDF governance |
| `07-AI-Development.pdf` | AI workflow + project journal |
| `08-Templates-and-Placeholders.pdf` | Templates, API/DB/Deployment stubs |
| `09-Student-Practice-Guide.pdf` | Student orientation + technique reference (see `manual/students-manifest.yaml`) |

## Cross-volume links

Links in Markdown that point to a file in another volume are rewritten to **clickable sibling PDF links** (e.g. `02-Reference.pdf`). Distribute all PDFs in the **same folder** or zip archive.

Links to **the same volume** become in-PDF jumps (`#chapter-anchor`). Links to **scores, audio, or root docs** not in any PDF become plain-text repository notes.

See [PDF link resolution](../../manual/PDF_LINKS.md) for the full rules, [`manual/SOURCE_TO_PDF_MAPPING.md`](../../manual/SOURCE_TO_PDF_MAPPING.md) for source → interim → PDF tables, and [`manual/link_registry.yaml`](../../manual/link_registry.yaml) for non-PDF paths.

Each PDF includes:

- Cover page with logo and volume index
- **Table of contents** (3 levels)
- Numbered sections
- **GitHub-like typography** — Noto Sans body text, Noto Sans Mono code (see [`header.tex`](templates/header.tex))

## Adding new documentation

1. Add the `.md` file under `docs/`.
2. Add its path to the appropriate volume in [`manual/manifest.yaml`](../../manual/manifest.yaml).
3. If it belongs in the Trainers Manual, also update [`manual/trainers-manifest.yaml`](../../manual/trainers-manifest.yaml).
4. If it belongs in the Student Practice Guide, also update [`manual/students-manifest.yaml`](../../manual/students-manifest.yaml).
5. Run `--validate` before building.

## Release checklist

1. Finish documentation changes for the release.
2. `python3 scripts/build_manual/build_manual.py --validate`
3. `python3 scripts/build_manual/build_manual.py --version YYYY.MM`
4. Spot-check TOC and cross-links in `00-Trainers-Manual.pdf` and `09-Student-Practice-Guide.pdf`.
5. Zip: `cd dist/manual/YYYY.MM && zip -r ../../../PH-Marching-Fusion-Manual-YYYY.MM.zip *.pdf`
6. Note the manual build in [`CHANGELOG.md`](../../CHANGELOG.md).
7. Commit the updated `dist/manual/{version}/` folder so GitHub users can download PDFs directly.

Published PDFs are **tracked in git** under [`dist/manual/`](../../dist/manual/README.md). Only `.build/` (preprocess cache) stays gitignored.
