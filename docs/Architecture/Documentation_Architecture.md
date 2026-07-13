[Home](../../README.md) › [Project Index](../../PROJECT_INDEX.md) › [Architecture](README.md) › Documentation Architecture

# Documentation Architecture

## Purpose

The Philippine Marching Percussion Fusion Project is intended to become more than a collection of scores. It is a documented educational, arranging, cultural, and performance system.

This document defines where information belongs so the project can grow without scattering knowledge across unrelated files.

## Architectural Model

The repository uses the Engineering Documentation Framework as its baseline and extends it for a special-purpose music-education project.

```text
.
├── Root navigation and governance
├── docs/                    # Human-readable project documentation
├── scores/                  # MuseScore and printable score deliverables
├── audio/                   # Practice and presentation audio
├── references/              # Curated source material and links
├── assets/                  # Project branding and shared visual assets
├── scripts/                 # Project utilities and validation
├── reports/                 # Generated reports
├── tasks/                   # Active work tracking
└── archive/                 # Superseded material
```

## Root Document Responsibilities

### `README.md`

Concise public landing page. It explains the project and directs readers to `PROJECT_INDEX.md`.

### `PROJECT_INDEX.md`

Authoritative navigation hub for all project documentation and deliverables.

### `PROJECT_CHARTER.md`

Defines purpose, scope, stakeholders, constraints, and success criteria.

### `docs/Specifications/Philippine_Marching_Percussion_Identity_Framework.md`

The project's musical constitution. Defines identity, cultural foundations, and the Identity Preservation Checklist.

### `ENGINEERING_DOCUMENTATION_FRAMEWORK.md`

Records how EDF applies to this special-purpose project.

### `ARCHITECTURE_DECISIONS.md`

Indexes project ADRs.

### `CHANGELOG.md`

Records significant structural and documentation changes.

## Documentation Domains

### `docs/Architecture/`

Project structure, documentation architecture, cross-cutting design, and ADRs.

### `docs/Specifications/`

Authoritative statements of project intent, required behavior, design constraints, notation rules, and musical requirements.

Primary documents:

- [Philippine Marching Percussion Identity Framework](../Specifications/Philippine_Marching_Percussion_Identity_Framework.md) — musical constitution
- [Core Blueprint](../Specifications/Core_Blueprint.md) — operational blueprint
- [Design Principles](../Specifications/Design_Principles.md)
- [Notation Standards](../Specifications/Notation_Standards.md)

### `docs/Reference/`

Definitions, terminology, concept explanations, and stable reference material.

### `docs/User_Guides/`

Practical instructions for arrangers, educators, performers, and other end users.

Primary documents:

- [Instructor Introduction](../User_Guides/Instructor_Introduction.md) — first read for music educators and pilot collaborators
- [MONHS 2026 Pilot Brief](../User_Guides/MONHS_2026_Pilot_Brief.md) — Misamis Oriental National High School (MONHS) pilot
- [Educational Handbook](../User_Guides/Educational_Handbook.md) — teaching methodology
- [Arranging Guide](../User_Guides/Arranging_Guide.md) — arranging guidance

### `docs/Development/`

Project-building workflow, experiments, internal working methods, and the project journal.

### `docs/Governance/`

Project-specific governance guidance when it becomes necessary.

### `docs/Templates/`

Reusable document and teaching-material templates.

### `docs/Research/`

Research notes, source evaluations, cultural studies, and analysis derived from external materials.

## Deliverable Areas

### `scores/`

MuseScore files, PDFs, and score-related documentation.

### `audio/`

Full mixes, sectional practice tracks, and approved exports.

### `references/`

Curated recordings, links, media notes, and inspiration sources. Large copyrighted media should not be committed unless redistribution is permitted.

### `assets/`

Canonical project branding and shared visual assets (for example the primary logo). See [Assets README](../../assets/README.md).

## Information Lifecycle

```text
Research or observation
        ↓
Development note or project journal
        ↓
Concept Library or specification
        ↓
Arranging or educational guidance
        ↓
Score and audio deliverable
        ↓
Field testing
        ↓
Revision or archival
```

## Placement Rules

- Vision and required outcomes belong in Specifications.
- Stable definitions belong in Reference.
- Practical how-to guidance belongs in User Guides.
- Experiments and provisional observations belong in Development.
- Structural decisions belong in Architecture.
- External-source analysis belongs in Research.
- Finished music belongs in `scores/`.
- Finished practice audio belongs in `audio/`.
- Canonical branding and shared visual assets belong in `assets/`.
- Superseded material belongs in `archive/`.

## Navigation Rules

Every user-facing Markdown document should link upward through the documentation hierarchy. Domain README files provide local navigation, while `PROJECT_INDEX.md` remains the master index.

## Migration Rule

Information should have one canonical home. During migration, old paths must be explicitly listed for removal after the replacement files have been verified.
