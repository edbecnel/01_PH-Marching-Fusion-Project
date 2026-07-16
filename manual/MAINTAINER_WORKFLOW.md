# PDF maintainer workflow

How to fix documentation errors, rebuild release PDFs, and interpret build warnings.

## Quick reference

| Task | Command (from repository root) |
|------|--------------------------------|
| Validate manifests | `python3 scripts/build_manual/build_manual.py --validate` |
| Rebuild all PDFs | `python3 scripts/build_manual/build_manual.py --version 2026.07` |
| Rebuild one volume | `python3 scripts/build_manual/build_manual.py --version 2026.07 --volume reference` |
| Rebuild Trainers Manual | `python3 scripts/build_manual/build_manual.py --version 2026.07 --trainers` |
| Rebuild Student Guide | `python3 scripts/build_manual/build_manual.py --version 2026.07 --students` |

Shorthand: `./scripts/build_manual/build.sh 2026.07`

Output: `dist/manual/2026.07/*.pdf`

Setup and release checklist: [`scripts/build_manual/README.md`](../scripts/build_manual/README.md)

---

## When you spot an error in a PDF

### 1. Identify the PDF and section

Note the PDF filename (for example `02-Reference.pdf`) and the section heading from the table of contents or page body.

### 2. Trace back to the source Markdown

**CLI lookup:**

```bash
python3 scripts/build_manual/lookup_source.py --pdf 02-Reference.pdf --section "Concept Library"
python3 scripts/build_manual/lookup_source.py --source docs/Reference/Concept_Library.md
```

**Mapping tables:** open [`SOURCE_TO_PDF_MAPPING.md`](SOURCE_TO_PDF_MAPPING.md) and find the volume table for that PDF. Use the **Source Markdown** column — that is the file you edit.

Regenerate the mapping after manifest changes: `python3 scripts/build_manual/generate_source_mapping.py`

**Authoritative manifests** (if the mapping doc is stale):

- [`manifest.yaml`](manifest.yaml) — volumes `01`–`08`
- [`trainers-manifest.yaml`](trainers-manifest.yaml) — `00-Trainers-Manual.pdf`
- [`students-manifest.yaml`](students-manifest.yaml) — `09-Student-Practice-Guide.pdf`

### 3. Edit source files only

| Edit | Do not edit |
|------|-------------|
| `docs/**/*.md` | `dist/manual/**/*.pdf` |
| Manifest YAML when adding/moving docs | `.build/` interim cache |

The build pipeline:

```text
docs/**/*.md  →  .build/manual/{version}/{volume_id}/*.md  →  dist/manual/{version}/*.pdf
```

To inspect preprocessing output after a build:

```text
.build/manual/2026.07/{volume_id}/{NN}-{basename}.md
```

Example: Concept Library in Reference → `.build/manual/2026.07/reference/02-Concept_Library.md`

### 4. Rebuild affected volume(s)

Rebuild every PDF that embeds the file you changed. See **Multi-volume sources** in [`SOURCE_TO_PDF_MAPPING.md`](SOURCE_TO_PDF_MAPPING.md).

Common case — `docs/Reference/Concept_Library.md`:

```bash
python3 scripts/build_manual/build_manual.py --version 2026.07 --volume reference
python3 scripts/build_manual/build_manual.py --version 2026.07 --trainers
```

(`00-Trainers-Manual.pdf` embeds only two sections from Concept Library; other edits affect Reference only.)

### 5. Spot-check and commit

1. Open the rebuilt PDF in `dist/manual/2026.07/`.
2. Confirm the fix and cross-links (especially in `00-Trainers-Manual.pdf` and `09-Student-Practice-Guide.pdf`).
3. Commit updated PDFs under `dist/manual/{version}/` with your source changes.

---

## Build warnings — what to do

A successful build ends with `Done. 10 PDF(s) in dist/manual/2026.07`. Warnings below do **not** stop the build. Treat them by severity.

### Safe to ignore (cosmetic)

#### `Underfull \hbox` / `Overfull \hbox`

LaTeX line-breaking feedback. The PDF is still generated. Ignore unless you see visible layout problems (awkward gaps, text running into margins).

**If layout looks wrong:** reword the paragraph, shorten a table cell, or split a long inline list in the source Markdown.

#### `accessing absolute path .../T/media-.../assets/ph-marching-fusion-logo.png`

Pandoc copies the cover logo into a temporary directory during the build. Harmless on local macOS builds. Only relevant if you need bit-identical reproducible builds across machines.

**Action:** none required for normal maintenance.

#### `warnings were issued by the TeX engine`

Summary line after the above. Build still succeeded.

**Action:** none unless missing characters or broken links appear in the PDF.

---

### Fix when visible in the PDF

#### `Missing character` / `could not represent character` (e.g. `→`, `≈`)

**Cause:** Bundled Noto Sans TTF subsets in [`assets/fonts/`](../assets/fonts/) do not include every Unicode symbol used in the docs. Affected sources today include:

| Character | Example source |
|-----------|----------------|
| `→` (U+2192) | [`docs/Reference/Philippine_Percussion_Sound_Model.md`](../docs/Reference/Philippine_Percussion_Sound_Model.md), [`docs/Reference/Grid_Exercises.md`](../docs/Reference/Grid_Exercises.md), [`docs/Governance/Document_Lifecycle.md`](../docs/Governance/Document_Lifecycle.md) |
| `≈` (U+2248) | [`docs/Reference/Syncopated_Push_and_Pull.md`](../docs/Reference/Syncopated_Push_and_Pull.md) |

**What you see:** blank box, missing glyph, or wrong character in the PDF.

**Fix options (pick one):**

1. **Source substitution (fastest):** Replace symbols with ASCII in the source `.md` file:
   - `→` → `->`
   - `≈` → `~` or `approx.`
2. **Font upgrade (project-wide):** Replace subset fonts with full Noto Sans files that include Mathematical Operators, then rebuild all volumes. Update [`assets/fonts/README.md`](../assets/fonts/README.md) accordingly.

After any source fix, rebuild the volumes that embed the changed file.

---

### Fix when cross-links break inside a PDF

#### `[WARNING] Duplicate identifier 'readme'` (and similar)

**Cause:** Multiple `README.md` files in one volume receive the same Pandoc heading anchor (derived from the filename stem `readme`). Same issue can occur for other repeated basenames (for example `verification`, `kaamulan-festival`).

**What you see:** Build succeeds; in-PDF links to a specific README or chapter may jump to the wrong section.

**Fix (maintainer / build pipeline):**

- Long-term: improve anchor injection in [`scripts/build_manual/preprocess.py`](../scripts/build_manual/preprocess.py) to use path-based IDs (for example `#architecture-readme` vs `#ai-readme`) instead of stem-only slugs.
- Short-term: when writing links inside a multi-README volume, prefer explicit heading anchors or link to the sibling PDF volume instead of a generic `#readme`.

Volumes commonly affected: `05-Architecture`, `07-AI-Development`, `08-Templates-and-Placeholders`.

---

## Warning severity summary

| Warning type | Blocks build? | Action |
|--------------|---------------|--------|
| Underfull / Overfull hbox | No | Ignore unless layout looks wrong |
| Absolute path (logo temp file) | No | Ignore |
| Missing character (`→`, `≈`, …) | No | **Fix source or fonts** — glyphs missing in PDF |
| Duplicate identifier | No | **Fix anchors** if intra-PDF links are wrong |
| `ERROR:` / non-zero exit | Yes | Read stderr; fix missing pandoc/tectonic, manifest, or source paths |

---

## Related documents

- [Source → PDF mapping](SOURCE_TO_PDF_MAPPING.md)
- [PDF link resolution](PDF_LINKS.md)
- [PDF manual build](../scripts/build_manual/README.md)
- [PDF manual releases](../dist/manual/README.md)
