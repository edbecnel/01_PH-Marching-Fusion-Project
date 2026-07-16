# Source Markdown to PDF mapping

This document lists how repository Markdown sources flow through the manual build pipeline into release PDFs under `dist/manual/{version}/`.

**Authoritative manifests:** [`manifest.yaml`](manifest.yaml), [`trainers-manifest.yaml`](trainers-manifest.yaml), and [`students-manifest.yaml`](students-manifest.yaml). Update those files first when adding or moving documentation; then refresh this mapping if the build order changes.

## Build pipeline

```text
docs/**/*.md  (source)
      │
      ▼  preprocess.py  (strip breadcrumbs, rewrite links, inject chapter anchors)
.build/manual/{version}/{volume_id}/*.md  (interim, gitignored)
      │
      ▼  pandoc + LaTeX
dist/manual/{version}/*.pdf  (release)
```

| Stage | Location | Purpose |
|-------|----------|---------|
| Source | `docs/**/*.md` | Canonical documentation edited in GitHub / Obsidian |
| Interim | `.build/manual/{version}/{volume_id}/` | Preprocessed Markdown cache for one Pandoc invocation per volume |
| Release | `dist/manual/{version}/` | Published PDFs (tracked in git) |

Replace `{version}` with the CLI label (for example `2026.07`). The interim directory is removed and rebuilt on each volume build.

### Interim file naming

| Interim file | Origin |
|--------------|--------|
| `00-cover.md` | Generated cover page (not from a source file) |
| `{NN}-{basename}.md` | Preprocessed copy of a manifest-listed source (`NN` is manifest order, 01–99) |
| `{NN}-appendix-technique-header.md` | Generated section divider when a volume embeds Reference technique chapters after User Guides content (`user_guides`, `students` volumes) |

Preprocessing changes (see [`scripts/build_manual/preprocess.py`](../scripts/build_manual/preprocess.py)):

- Remove breadcrumb navigation line
- Rewrite cross-volume `.md` links to sibling `.pdf` links
- Inject Pandoc chapter anchors on the first `#` heading
- For trainers `Concept_Library.md`, extract only the listed `##` sections (see volume 00 below)

## Release PDF index

| PDF | Manifest | Volume id |
|-----|----------|-----------|
| [`00-Trainers-Manual.pdf`](../dist/manual/2026.07/00-Trainers-Manual.pdf) | `trainers-manifest.yaml` | `trainers` |
| [`01-Specifications.pdf`](../dist/manual/2026.07/01-Specifications.pdf) | `manifest.yaml` | `specifications` |
| [`02-Reference.pdf`](../dist/manual/2026.07/02-Reference.pdf) | `manifest.yaml` | `reference` |
| [`03-User-Guides.pdf`](../dist/manual/2026.07/03-User-Guides.pdf) | `manifest.yaml` | `user_guides` |
| [`04-Research.pdf`](../dist/manual/2026.07/04-Research.pdf) | `manifest.yaml` | `research` |
| [`05-Architecture.pdf`](../dist/manual/2026.07/05-Architecture.pdf) | `manifest.yaml` | `architecture` |
| [`06-Governance.pdf`](../dist/manual/2026.07/06-Governance.pdf) | `manifest.yaml` | `governance` |
| [`07-AI-Development.pdf`](../dist/manual/2026.07/07-AI-Development.pdf) | `manifest.yaml` | `ai_development` |
| [`08-Templates-and-Placeholders.pdf`](../dist/manual/2026.07/08-Templates-and-Placeholders.pdf) | `manifest.yaml` | `templates_placeholders` |
| [`09-Student-Practice-Guide.pdf`](../dist/manual/2026.07/09-Student-Practice-Guide.pdf) | `students-manifest.yaml` | `students` |

---

## 01-Specifications.pdf

**Interim directory:** `.build/manual/{version}/specifications/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/Specifications/README.md` | `01-README.md` | |
| 2 | `docs/Specifications/Philippine_Marching_Percussion_Identity_Framework.md` | `02-Philippine_Marching_Percussion_Identity_Framework.md` | |
| 3 | `docs/Specifications/Core_Blueprint.md` | `03-Core_Blueprint.md` | |
| 4 | `docs/Specifications/Design_Principles.md` | `04-Design_Principles.md` | |
| 5 | `docs/Specifications/Notation_Standards.md` | `05-Notation_Standards.md` | |

---

## 02-Reference.pdf

**Interim directory:** `.build/manual/{version}/reference/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/Reference/README.md` | `01-README.md` | |
| 2 | `docs/Reference/Concept_Library.md` | `02-Concept_Library.md` | Full document |
| 3 | `docs/Reference/Philippine_Percussion_Sound_Model.md` | `03-Philippine_Percussion_Sound_Model.md` | |
| 4 | `docs/Reference/Syncopated_Push_and_Pull.md` | `04-Syncopated_Push_and_Pull.md` | |
| 5 | `docs/Reference/Legato_Stroke.md` | `05-Legato_Stroke.md` | |
| 6 | `docs/Reference/Accent_Taps.md` | `06-Accent_Taps.md` | |
| 7 | `docs/Reference/Eight_Eight_Sixteen.md` | `07-Eight_Eight_Sixteen.md` | |
| 8 | `docs/Reference/Grid_Exercises.md` | `08-Grid_Exercises.md` | |

---

## 03-User-Guides.pdf

**Interim directory:** `.build/manual/{version}/user_guides/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/User_Guides/README.md` | `01-README.md` | |
| 2 | `docs/User_Guides/Instructor_Introduction.md` | `02-Instructor_Introduction.md` | |
| 3 | `docs/User_Guides/MONHS_2026_Pilot_Brief.md` | `03-MONHS_2026_Pilot_Brief.md` | |
| 4 | `docs/User_Guides/Arranging_Guide.md` | `04-Arranging_Guide.md` | |
| 5 | `docs/User_Guides/Educational_Handbook.md` | `05-Educational_Handbook.md` | |
| 6 | `docs/User_Guides/Student_Practice_Guide.md` | `06-Student_Practice_Guide.md` | |
| — | *(generated)* | `07-appendix-technique-header.md` | Divider before embedded Reference chapters |
| 7 | `docs/Reference/Legato_Stroke.md` | `07-Legato_Stroke.md` | Also in `02-Reference.pdf` |
| 8 | `docs/Reference/Accent_Taps.md` | `08-Accent_Taps.md` | Also in `02-Reference.pdf` |
| 9 | `docs/Reference/Eight_Eight_Sixteen.md` | `09-Eight_Eight_Sixteen.md` | Also in `02-Reference.pdf` |
| 10 | `docs/Reference/Grid_Exercises.md` | `10-Grid_Exercises.md` | Also in `02-Reference.pdf` |

---

## 04-Research.pdf

**Interim directory:** `.build/manual/{version}/research/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/Research/README.md` | `01-README.md` | |
| 2 | `docs/Research/Indigenous_Philippine_Percussion.md` | `02-Indigenous_Philippine_Percussion.md` | |
| 3 | `docs/Research/Kaamulan_Festival.md` | `03-Kaamulan_Festival.md` | |
| 4 | `docs/Research/Philippine_Marching_Heritage.md` | `04-Philippine_Marching_Heritage.md` | |

---

## 05-Architecture.pdf

**Interim directory:** `.build/manual/{version}/architecture/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/Architecture/README.md` | `01-README.md` | |
| 2 | `docs/Architecture/Documentation_Architecture.md` | `02-Documentation_Architecture.md` | |
| 3 | `docs/Architecture/ADRs/README.md` | `03-README.md` | |

---

## 06-Governance.pdf

**Interim directory:** `.build/manual/{version}/governance/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/Governance/README.md` | `01-README.md` | |
| 2 | `docs/Governance/Governance_Overview.md` | `02-Governance_Overview.md` | |
| 3 | `docs/Governance/Project_Governance.md` | `03-Project_Governance.md` | |
| 4 | `docs/Governance/EDF_Governance.md` | `04-EDF_Governance.md` | |
| 5 | `docs/Governance/Document_Metadata_Standard.md` | `05-Document_Metadata_Standard.md` | |
| 6 | `docs/Governance/Document_Lifecycle.md` | `06-Document_Lifecycle.md` | |
| 7 | `docs/Governance/Change_Management.md` | `07-Change_Management.md` | |
| 8 | `docs/Governance/Ownership_and_Review.md` | `08-Ownership_and_Review.md` | |
| 9 | `docs/Governance/Governance_Checklist.md` | `09-Governance_Checklist.md` | |
| 10 | `docs/Governance/Analyzer_Compliance.md` | `10-Analyzer_Compliance.md` | |
| 11 | `docs/Governance/Framework_Self_Hosting.md` | `11-Framework_Self_Hosting.md` | |

---

## 07-AI-Development.pdf

**Interim directory:** `.build/manual/{version}/ai_development/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/AI/README.md` | `01-README.md` | |
| 2 | `docs/AI/AI_Philosophy.md` | `02-AI_Philosophy.md` | |
| 3 | `docs/AI/Repository_Workflow.md` | `03-Repository_Workflow.md` | |
| 4 | `docs/AI/AI_Roles.md` | `04-AI_Roles.md` | |
| 5 | `docs/AI/AI_Decision_Matrix.md` | `05-AI_Decision_Matrix.md` | |
| 6 | `docs/AI/Context_Checklist.md` | `06-Context_Checklist.md` | |
| 7 | `docs/AI/Prompting_Guide.md` | `07-Prompting_Guide.md` | |
| 8 | `docs/AI/Verification.md` | `08-Verification.md` | |
| 9 | `docs/AI/Security.md` | `09-Security.md` | |
| 10 | `docs/AI/Governance.md` | `10-Governance.md` | |
| 11 | `docs/AI/Cost_Optimization.md` | `11-Cost_Optimization.md` | |
| 12 | `docs/Development/README.md` | `12-README.md` | |
| 13 | `docs/Development/Project_Journal.md` | `13-Project_Journal.md` | |

---

## 08-Templates-and-Placeholders.pdf

**Interim directory:** `.build/manual/{version}/templates_placeholders/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/Templates/README.md` | `01-README.md` | |
| 2 | `docs/API/README.md` | `02-README.md` | |
| 3 | `docs/Database/README.md` | `03-README.md` | |
| 4 | `docs/Deployment/README.md` | `04-README.md` | |

---

## 00-Trainers-Manual.pdf

**Interim directory:** `.build/manual/{version}/trainers/`

| Order | Source Markdown                                                            | Interim Markdown                                          | Notes                                                                                   |
| ----: | -------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------- |
|     — | *(generated)*                                                              | `00-cover.md`                                             | Cover page                                                                              |
|     1 | `docs/User_Guides/Instructor_Introduction.md`                              | `01-Instructor_Introduction.md`                           |                                                                                         |
|     2 | `docs/User_Guides/MONHS_2026_Pilot_Brief.md`                               | `02-MONHS_2026_Pilot_Brief.md`                            |                                                                                         |
|     3 | `docs/User_Guides/Educational_Handbook.md`                                 | `03-Educational_Handbook.md`                              |                                                                                         |
|     4 | `docs/Specifications/Design_Principles.md`                                 | `04-Design_Principles.md`                                 | Also in `01-Specifications.pdf`                                                         |
|     5 | `docs/Specifications/Philippine_Marching_Percussion_Identity_Framework.md` | `05-Philippine_Marching_Percussion_Identity_Framework.md` | Also in `01-Specifications.pdf`                                                         |
|     6 | `docs/Reference/Legato_Stroke.md`                                          | `06-Legato_Stroke.md`                                     | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `09-Student-Practice-Guide.pdf`       |
|     7 | `docs/Reference/Accent_Taps.md`                                            | `07-Accent_Taps.md`                                       | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `09-Student-Practice-Guide.pdf`       |
|     8 | `docs/Reference/Eight_Eight_Sixteen.md`                                    | `08-Eight_Eight_Sixteen.md`                               | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `09-Student-Practice-Guide.pdf`       |
|     9 | `docs/Reference/Grid_Exercises.md`                                         | `09-Grid_Exercises.md`                                    | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `09-Student-Practice-Guide.pdf`       |
|    10 | `docs/Reference/Concept_Library.md`                                        | `10-Concept_Library.md`                                   | **Section extract only:** `6. Call and Response`, `9. Community Performance Traditions` |
|    11 | `docs/Research/Indigenous_Philippine_Percussion.md`                        | `11-Indigenous_Philippine_Percussion.md`                  | Also in `04-Research.pdf`                                                               |
|    12 | `docs/Research/Kaamulan_Festival.md`                                       | `12-Kaamulan_Festival.md`                                 | Also in `04-Research.pdf`                                                               |

---

## 09-Student-Practice-Guide.pdf

**Interim directory:** `.build/manual/{version}/students/`

| Order | Source Markdown | Interim Markdown | Notes |
|------:|-----------------|------------------|-------|
| — | *(generated)* | `00-cover.md` | Cover page |
| 1 | `docs/User_Guides/Student_Practice_Guide.md` | `01-Student_Practice_Guide.md` | Also in `03-User-Guides.pdf` |
| — | *(generated)* | `02-appendix-technique-header.md` | Divider before embedded Reference chapters |
| 2 | `docs/Reference/Legato_Stroke.md` | `02-Legato_Stroke.md` | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf` |
| 3 | `docs/Reference/Accent_Taps.md` | `03-Accent_Taps.md` | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf` |
| 4 | `docs/Reference/Eight_Eight_Sixteen.md` | `04-Eight_Eight_Sixteen.md` | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf` |
| 5 | `docs/Reference/Grid_Exercises.md` | `05-Grid_Exercises.md` | Also in `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf` |

---

## Source files appearing in multiple PDFs

| Source Markdown | PDF volumes |
|-----------------|-------------|
| `docs/Specifications/Design_Principles.md` | `01-Specifications.pdf`, `00-Trainers-Manual.pdf` |
| `docs/Specifications/Philippine_Marching_Percussion_Identity_Framework.md` | `01-Specifications.pdf`, `00-Trainers-Manual.pdf` |
| `docs/Reference/Legato_Stroke.md` | `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf`, `09-Student-Practice-Guide.pdf` |
| `docs/Reference/Accent_Taps.md` | `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf`, `09-Student-Practice-Guide.pdf` |
| `docs/Reference/Eight_Eight_Sixteen.md` | `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf`, `09-Student-Practice-Guide.pdf` |
| `docs/Reference/Grid_Exercises.md` | `02-Reference.pdf`, `03-User-Guides.pdf`, `00-Trainers-Manual.pdf`, `09-Student-Practice-Guide.pdf` |
| `docs/Reference/Concept_Library.md` | `02-Reference.pdf` (full), `00-Trainers-Manual.pdf` (two sections only) |
| `docs/User_Guides/Student_Practice_Guide.md` | `03-User-Guides.pdf`, `09-Student-Practice-Guide.pdf` |
| `docs/Research/Indigenous_Philippine_Percussion.md` | `04-Research.pdf`, `00-Trainers-Manual.pdf` |
| `docs/Research/Kaamulan_Festival.md` | `04-Research.pdf`, `00-Trainers-Manual.pdf` |

All other `docs/**/*.md` files map to exactly one domain volume PDF (`01`–`08`).

## Sources not exported to PDF

These paths are intentionally outside the manual manifests (repository-only or domain deliverables):

- Root charter and index files (`README.md`, `PROJECT_INDEX.md`, etc.)
- `scores/`, `audio/`, `reports/`, `scripts/`, `manual/` (except as build inputs)
- See [`link_registry.yaml`](link_registry.yaml) for plain-text link notes in PDF output

## Related documents

- [PDF link resolution](PDF_LINKS.md) — how `.md` links become in-PDF jumps or sibling PDF links
- [PDF manual build](../scripts/build_manual/README.md) — requirements, commands, release checklist
- [PDF manual releases](../dist/manual/README.md) — published version folders
