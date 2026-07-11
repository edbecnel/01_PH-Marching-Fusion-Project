# AI Philosophy

[Home](../../README.md) › [Project Index](../../PROJECT_INDEX.md) › [AI Engineering Handbook](README.md) › AI Philosophy


## Purpose

This document defines the core philosophy for using AI tools within the Philippine Marching Percussion Fusion Project and other projects that adopt the Engineering Documentation Framework.

AI is treated as a project assistant, not an autonomous owner of musical quality, cultural authenticity, educational sequencing, or final creative decisions.

## Primary Principle

Use the least expensive AI that can comfortably solve the task.

This does not mean always using the cheapest model. It means choosing the tool that provides the best overall engineering value after considering:

- task complexity
- required reasoning depth
- context size
- privacy requirements
- model capability
- developer time
- risk of rework
- cost of mistakes

Saving a small amount of API cost is not useful if it causes hours of additional project time or leads to poor creative or educational decisions.

## Human Ownership

Human developers and project owners remain responsible for all final outcomes.

AI may assist with:

- brainstorming
- architecture analysis
- requirements refinement
- code generation
- documentation drafting
- testing suggestions
- debugging support
- review assistance

Humans remain responsible for:

- final engineering judgment
- security decisions
- production approval
- correctness verification
- maintainability
- testing
- release decisions

## Documentation as AI Context

AI performance improves when the project has well-structured documentation.

The repository should be treated as the source of truth. AI assistants should be pointed to authoritative documents such as:

- `PROJECT_INDEX.md`
- `PROJECT_CHARTER.md`
- `ARCHITECTURE_DECISIONS.md`
- relevant specifications
- relevant architecture documents
- relevant user guides and educational documents
- `docs/AI/Repository_Workflow.md`

AI should not be given the entire repository blindly when a smaller, better-curated context is sufficient.

## Same Standards as Human Work

AI-generated work must meet the same standards as human-written work.

AI-generated code and documentation should be:

- reviewed
- tested
- verified
- kept consistent with project architecture
- committed through the normal Git workflow
- documented when it affects architecture, behavior, or operations

## Decisions Still Require Documentation

Significant architecture decisions influenced by AI still require formal documentation.

Use ADRs for decisions that affect:

- project structure and documentation architecture
- notation or production tooling choices
- educational methodology direction
- long-term maintainability

## Related Documents

- [AI_Roles.md](./AI_Roles.md)
- [AI_Decision_Matrix.md](./AI_Decision_Matrix.md)
- [Governance.md](./Governance.md)

## Parent

- [AI Engineering Handbook](README.md)
