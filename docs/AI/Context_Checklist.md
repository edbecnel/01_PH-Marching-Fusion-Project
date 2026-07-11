# Context Checklist

[Home](../../README.md) › [Project Index](../../PROJECT_INDEX.md) › [AI Engineering Handbook](README.md) › Context Checklist

> **Status:** Maintained
> **Owner:** Philippine Marching Percussion Fusion Project
> **Applies To:** AI-assisted project work
> **Last Reviewed:** 2026-07-11
> **Review Frequency:** On Change

## Purpose

This document defines the information that should be provided to AI assistants when performing project work.

The goal is to provide enough context for useful output without overwhelming the assistant with unrelated files.

## Core Checklist

Before asking AI to perform project work, identify:

- relevant requirements and specifications
- applicable ADRs
- relevant architecture documents
- musical, educational, or arranging constraints
- only the files required for the task
- clear success criteria
- known constraints
- expected output format
- whether the work is planning, editing, composition, documentation, review, or troubleshooting

## Repository Entry Points

When starting a new AI session, useful entry points include:

- `PROJECT_INDEX.md`
- `PROJECT_CHARTER.md`
- `ARCHITECTURE_DECISIONS.md`
- `docs/Specifications/Core_Blueprint.md`
- `docs/Reference/Concept_Library.md`
- `docs/Architecture/`
- `docs/Specifications/`
- `docs/User_Guides/`
- `docs/AI/`
- `scores/` — when working on notation or warm-ups
- `references/` — when working on groove vocabulary or inspiration

## Avoid Overloading Context

Do not provide the entire repository unless the task genuinely requires it.

Prefer targeted context:

- the affected file
- related specification or concept-library entry
- related architecture document
- relevant score or audio deliverable
- relevant ADRs

## For Documentation Tasks

Provide:

- target document path
- purpose of the document
- audience (educator, arranger, performer, contributor)
- related documents
- preferred tone
- whether to create, update, split, merge, or review

## For Musical and Arranging Tasks

Provide:

- target instrument section or score path
- groove vocabulary or cultural constraints
- notation standards in effect (or note if still planned)
- MuseScore or playback constraints
- layering intent (Philippine groove, DCI overlay, HBCU contrast)
- acceptance criteria for musical identity and teachability

## For Architecture Tasks

Provide:

- project goals
- constraints
- current documentation architecture
- alternatives considered
- known risks
- affected domains or deliverable areas

## Related Documents

- [Prompting_Guide.md](./Prompting_Guide.md)
- [AI_Decision_Matrix.md](./AI_Decision_Matrix.md)
- [Verification.md](./Verification.md)
- [Core Blueprint](../Specifications/Core_Blueprint.md)

## Parent

- [AI Engineering Handbook](README.md)
