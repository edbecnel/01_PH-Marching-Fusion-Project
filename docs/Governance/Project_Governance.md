# Project Governance

[Home](../../README.md) › [Project Index](../../PROJECT_INDEX.md) › [Governance](README.md) › Project Governance

> **Status:** Maintained
> **Owner:** Philippine Marching Percussion Fusion Project
> **Applies To:** This repository only
> **Last Reviewed:** 2026-07-11
> **Review Frequency:** Quarterly
> **Authoritative:** Yes

## Purpose

This document defines governance requirements specific to the Philippine Marching Percussion Fusion Project.

It supplements the baseline governance documents adopted from the [Engineering Documentation Framework](https://github.com/edbecnel/Engineering-Documentation-Framework). Baseline rules for metadata, lifecycle, ownership, review, and change management remain in force unless this document states a project-specific exception.

## Domain Profile

This project implements a **music-education domain profile** on top of EDF Core. It is an educational and musical initiative, not a conventional software repository.

The project preserves EDF navigation, traceability, and governance practices while extending the documentation model for:

- musical scores and notation
- practice and presentation audio
- curated reference material
- project branding and shared visual assets
- music-education research
- arranging and pedagogy documentation

See [Documentation Architecture](../Architecture/Documentation_Architecture.md) and [EDF Adoption Guide](../../ENGINEERING_DOCUMENTATION_FRAMEWORK.md).

## Authoritative Sources

| Source | Role |
|---|---|
| GitHub (`main` branch) | Canonical source of truth for all project content |
| `PROJECT_INDEX.md` | Primary navigation hub for humans and AI assistants |
| `docs/Specifications/` | Authoritative musical, educational, and design intent |
| `scores/` and `audio/` | Finished musical deliverables |
| `references/` | Curated inspiration and source material |
| `assets/` | Canonical branding and shared visual assets |

## Document Ownership

The project owner is accountable for:

- accuracy of specifications, guides, and educational content
- cultural authenticity of musical and pedagogical decisions
- navigation integrity across `docs/`, deliverable areas, and root indexes
- review of AI-assisted documentation and score-related changes

Baseline governance documents in this domain were adopted from EDF. When EDF upstream guidance and project needs conflict, this document and [Documentation Architecture](../Architecture/Documentation_Architecture.md) take precedence for this repository.

## EDF Domains Not Used

The following EDF Core domains are retained as structural placeholders only. They are **not active** for this project:

| Domain | Reason |
|---|---|
| `docs/API/` | No application programming interface |
| `docs/Database/` | No database or persistence layer |
| `docs/Deployment/` | No software deployment pipeline |

Do not place project documentation in these domains unless the project's nature changes.

## Accepted Deliverable Areas

The Framework Advisor may report Markdown under `scores/`, `audio/`, `references/`, `reports/`, and `assets/` as outside canonical `docs/` locations. This is expected and accepted.

These paths are deliberate project extensions documented in [Documentation Architecture](../Architecture/Documentation_Architecture.md). They must remain linked from `PROJECT_INDEX.md` and include hierarchical navigation breadcrumbs.

## AI-Assisted Work

AI-assisted changes to this repository follow [AI Repository Workflow](../AI/Repository_Workflow.md).

Key requirements:

- work directly in the local Git working tree
- deliver complete files at normal repository paths
- update navigation when documents change
- preserve Philippine musical identity in all creative and educational content
- treat the human project owner as the final authority

## Validation

This project does not host EDF Framework Advisor scripts. Validation is performed read-only from a local clone of the Engineering Documentation Framework repository:

```bash
/path/to/Engineering-Documentation-Framework/scripts/analyze_project_structure.sh \
  "/path/to/01_PH-Marching-Fusion-Project"
```

Analyzer recommendations about `scores/`, `audio/`, `references/`, `reports/`, and `assets/` may be accepted as documented exceptions above. Recommendations about missing `docs/AI/` or governance completeness should be resolved.

## Framework Reference Documents

The following documents are retained as **reference copies** of EDF upstream guidance. They apply to EDF repository maintenance, not to day-to-day work in this project:

- [EDF Governance](EDF_Governance.md)
- [Framework Self-Hosting](Framework_Self_Hosting.md)

## Review Expectations

| Document class | Review frequency |
|---|---|
| Specifications and Core Blueprint | On change |
| AI Repository Workflow | On change |
| Educational and arranging guides | Quarterly or on change |
| Scores and audio deliverables | On revision |
| Governance and adoption docs | Quarterly |

## Parent

- [Governance](README.md)

## Related Documents

- [Governance Overview](Governance_Overview.md)
- [Document Metadata Standard](Document_Metadata_Standard.md)
- [Documentation Change Management](Change_Management.md)
- [AI Repository Workflow](../AI/Repository_Workflow.md)
- [EDF Adoption Guide](../../ENGINEERING_DOCUMENTATION_FRAMEWORK.md)
