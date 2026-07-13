[Home](README.md) › [Project Index](PROJECT_INDEX.md) › EDF Adoption

# Engineering Documentation Framework Adoption

## Purpose

This project adopts the Engineering Documentation Framework (EDF) as its documentation architecture and governance baseline.

The project is not a conventional software-development repository. EDF is therefore applied as a structured documentation system, with project-specific extensions for music education, arranging, performance, research, scores, and audio.

## Adoption Principles

1. GitHub is the canonical source of truth.
2. `PROJECT_INDEX.md` is the primary documentation navigation hub.
3. Documentation belongs under the closest applicable EDF domain.
4. Musical deliverables remain outside `docs/`.
5. Project-specific domains may be added without altering EDF Core.
6. Existing information should be migrated rather than duplicated.
7. Superseded material should be archived or explicitly removed with a recorded migration.
8. Markdown documents should include hierarchical navigation.
9. Generation and bootstrap tools must not overwrite existing files silently.
10. Changes should be validated and accompanied by a report when practical.

## Domain Profile

This repository is a **music-education domain profile** implementation of EDF. It preserves EDF Core navigation and governance while adding deliverable areas appropriate to marching-percussion education.

Authoritative project-specific rules are in [Project Governance](docs/Governance/Project_Governance.md).

## Project-Specific Extensions

This project adds:

- `docs/Research/`
- `scores/`
- `audio/`
- `references/`

These extensions support the special-purpose music-education nature of the project while retaining EDF navigation, governance, traceability, and information-architecture practices.

## EDF Domains Not Used

The following EDF Core domains are structural placeholders only:

- `docs/API/`
- `docs/Database/`
- `docs/Deployment/`

They are not active documentation domains for this project. See each domain's README for details.

## Accepted Analyzer Exceptions

When validating against the EDF Framework Advisor, the following findings are accepted for this project:

| Finding | Reason |
|---|---|
| Markdown in `scores/` | Intentional musical deliverable area |
| Markdown in `audio/` | Intentional practice and presentation audio area |
| Markdown in `references/` | Intentional curated source-material area |
| Markdown in `reports/` | Intentional generated-report area |

These paths are linked from `PROJECT_INDEX.md` and documented in [Documentation Architecture](docs/Architecture/Documentation_Architecture.md).

## AI-Assisted Workflow

AI-assisted work on this repository follows the IDE-native workflow defined in [AI Repository Workflow](docs/AI/Repository_Workflow.md).

Key practices:

- read and modify files in the local Git working tree
- deliver complete files at normal repository paths
- review changes with `git status` and `git diff` before committing
- update navigation when documentation changes

The legacy `.update/` ZIP handover workflow was used only for the initial EDF migration and is no longer the standard operating model.

## Validation

Run the EDF Framework Advisor read-only from a local clone of the [Engineering Documentation Framework](https://github.com/edbecnel/Engineering-Documentation-Framework) repository:

```bash
/path/to/Engineering-Documentation-Framework/scripts/analyze_project_structure.sh \
  "/path/to/01_PH-Marching-Fusion-Project"
```

This project does not maintain its own copy of EDF validation scripts.

## Canonical Entry Points

- [Project README](README.md)
- [Project Index](PROJECT_INDEX.md)
- [Project Charter](PROJECT_CHARTER.md)
- [Philippine Marching Percussion Identity Framework](docs/Specifications/Philippine_Marching_Percussion_Identity_Framework.md)
- [Instructor Introduction](docs/User_Guides/Instructor_Introduction.md) — for educators and pilot collaborators
- [Documentation Architecture](docs/Architecture/Documentation_Architecture.md)
- [AI Engineering Handbook](docs/AI/README.md)
- [Project Governance](docs/Governance/Project_Governance.md)
