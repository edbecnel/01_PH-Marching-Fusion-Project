# PDF link resolution

Markdown sources use **repository `.md` links** for GitHub and Obsidian. PDF builds rewrite those links at compile time.

## Three outcomes in PDF output

| Source link target | PDF behavior |
|--------------------|--------------|
| **Same volume, embedded chapter** | In-PDF jump (`#chapter-anchor` or `#heading-anchor`) |
| **Another PDF volume** | Clickable sibling PDF link, e.g. `[Identity Framework (Specifications)](01-Specifications.pdf)` |
| **Not in any PDF** (scores, audio, root charter) | Plain text with repository note from [`link_registry.yaml`](link_registry.yaml) |

## Manifests

| File | Role |
|------|------|
| [`manifest.yaml`](manifest.yaml) | Which `.md` files are embedded in each volume PDF |
| [`trainers-manifest.yaml`](trainers-manifest.yaml) | Trainers Manual curation |
| [`students-manifest.yaml`](students-manifest.yaml) | Student Practice Guide curation |
| [`link_registry.yaml`](link_registry.yaml) | Paths outside `docs/` or not exported to PDF |

A source file may appear in **more than one volume** (e.g. Legato Stroke in `03-User-Guides.pdf` and `02-Reference.pdf`). Link rewriting uses the **current volume** for in-PDF jumps.

## User Guides self-contained technique

`03-User-Guides.pdf` embeds these Reference chapters after the User Guides documents:

- Legato Stroke
- Accent-Taps
- 8-8-16 Exercise
- Grid Exercises

Educational Handbook “Related Documents” links to those chapters resolve **inside the same PDF**.

## Student Practice Guide

`09-Student-Practice-Guide.pdf` embeds:

- [Student Practice Guide](../docs/User_Guides/Student_Practice_Guide.md) — orientation and canonical assignment names
- The same four technique Reference chapters (Legato Stroke, Accent-Taps, 8-8-16, Grid Exercises)

Section titles match `02-Reference.pdf` and instructor manuals so trainers can assign **Legato Stroke → Key Mechanics** without a separate student numbering scheme.

## Adding a new link target

1. **New `docs/` file** — add to the correct volume in `manifest.yaml` (and `trainers-manifest.yaml` if needed).
2. **Repository deliverable** (scores, audio) — add an entry to `link_registry.yaml` with `type: repository`.
3. **Re-run** `python3 scripts/build_manual/build_manual.py --validate` then rebuild.

Do not change source Markdown to `.pdf` links; the build pipeline handles PDF output.
