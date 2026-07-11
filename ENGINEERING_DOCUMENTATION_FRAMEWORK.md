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

## Project-Specific Extensions

This project adds:

- `docs/Research/`
- `scores/`
- `audio/`
- `references/`

These extensions support the special-purpose music-education nature of the project while retaining EDF navigation, governance, traceability, and information-architecture practices.

## Canonical Entry Points

- [Project README](README.md)
- [Project Index](PROJECT_INDEX.md)
- [Project Charter](PROJECT_CHARTER.md)
- [Documentation Architecture](docs/Architecture/Documentation_Architecture.md)
