# PDF Manual Build

Build multi-volume PDF manuals and the **Trainers Manual** from project Markdown.

## Requirements

- [Pandoc](https://pandoc.org/) 3.x — `brew install pandoc`
- [Tectonic](https://tectonic-typesetting.github.io/) — `brew install tectonic` (PDF engine; lighter than full MacTeX)
- Python 3 with PyYAML

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

Output: `dist/manual/2026.07/*.pdf` (9 PDFs)

## Commands

| Command | Purpose |
|---------|---------|
| `--validate` | Ensure every `docs/**/*.md` file is listed in `manual/manifest.yaml` |
| `--version 2026.07` | Label for output folder and cover pages |
| `--volume reference` | Build one domain volume by id |
| `--trainers` | Build only `00-Trainers-Manual.pdf` |

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

## Cross-volume links

Links in Markdown that point to a file in another volume are rewritten to **clickable sibling PDF links** (e.g. `02-Reference.pdf`). Distribute all PDFs in the **same folder** or zip archive.

Each PDF includes:

- Cover page with logo and volume index
- **Table of contents** (3 levels)
- Numbered sections

## Adding new documentation

1. Add the `.md` file under `docs/`.
2. Add its path to the appropriate volume in [`manual/manifest.yaml`](../../manual/manifest.yaml).
3. If it belongs in the Trainers Manual, also update [`manual/trainers-manifest.yaml`](../../manual/trainers-manifest.yaml).
4. Run `--validate` before building.

## Release checklist

1. Finish documentation changes for the release.
2. `python3 scripts/build_manual/build_manual.py --validate`
3. `python3 scripts/build_manual/build_manual.py --version YYYY.MM`
4. Spot-check TOC and cross-links in `00-Trainers-Manual.pdf`.
5. Zip: `cd dist/manual/YYYY.MM && zip -r ../../../PH-Marching-Fusion-Manual-YYYY.MM.zip *.pdf`
6. Note the manual build in [`CHANGELOG.md`](../../CHANGELOG.md).
7. Commit the updated `dist/manual/{version}/` folder so GitHub users can download PDFs directly.

Published PDFs are **tracked in git** under [`dist/manual/`](../../dist/manual/README.md). Only `.build/` (preprocess cache) stays gitignored.
