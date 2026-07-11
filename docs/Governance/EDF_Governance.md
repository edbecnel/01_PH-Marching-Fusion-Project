# EDF Governance

[Home](../../README.md) › [Project Index](../../PROJECT_INDEX.md) › [Governance](README.md) › EDF Governance

> **Status:** Maintained
> **Owner:** Engineering Documentation Framework
> **Applies To:** Engineering Documentation Framework repository only
> **Last Reviewed:** 2026-07-10
> **Review Frequency:** Annual

> **Note:** This is an EDF upstream reference copy. For day-to-day governance of this project, see [Project Governance](Project_Governance.md).

## Applicability

This document applies only to development, maintenance, validation, and release of
the Engineering Documentation Framework itself.

Projects that adopt EDF are not required to maintain EDF templates, generators,
analyzers, framework governance documents, self-hosting checks, or EDF release
artifacts unless they independently choose to implement comparable tooling.

Adopting projects remain subject to the baseline governance documents in this domain.

## Purpose

This document extends the baseline Governance subsystem with requirements that are
specific to EDF as a reusable framework.

## Template Governance

Changes to canonical documentation standards must be evaluated for corresponding
template changes.

Template changes must:

- preserve non-destructive generation behavior
- avoid overwriting project-owned files
- include required navigation
- reflect current metadata and governance standards
- remain suitable for both new and existing projects

## Generator Governance

EDF generators must:

- create only missing files
- never overwrite existing project-owned files
- never delete, rename, move, or merge project-owned files automatically
- create complete navigation when generating documents
- clearly report created and skipped files
- remain consistent with the canonical templates and architecture

Changes to generator behavior require review against the non-destructive generation
principles.

## Framework Advisor Governance

The Framework Advisor must:

- remain read-only unless a future explicitly approved mode says otherwise
- explain findings and recommendations
- distinguish baseline project checks from EDF-specific checks
- avoid inventing project facts, owners, approvals, or exceptions
- use transparent scoring rules
- report accepted exceptions separately from unresolved noncompliance

EDF-specific checks may include:

- template completeness
- generator-template alignment
- analyzer-governance alignment
- framework self-hosting compliance
- required framework documents
- release-readiness validation

## Governance-System Governance

Changes to Governance itself must:

- preserve the distinction between baseline governance and EDF-specific governance
- update affected templates, generators, analyzer rules, and navigation
- be recorded in architecture decisions when they alter governance direction
- be reflected in the changelog when release-significant

## Self-Hosting Governance

Before a stable EDF release, the EDF repository should be evaluated against its own:

- canonical structure
- navigation requirements
- metadata standards
- lifecycle rules
- ownership and review rules
- link-validation requirements
- analyzer requirements
- template requirements

Accepted exceptions must be documented and must not be hidden by scoring.

## Versioning Governance

Framework releases should identify:

- the framework version
- significant governance changes
- template changes
- generator changes
- analyzer changes
- migration considerations
- compatibility expectations

Breaking changes to canonical structure, metadata meaning, or required behavior should
be clearly identified.

## Release Governance

An EDF release should not be considered complete until:

- required documentation is current
- navigation links are validated
- framework-specific analyzer checks are reviewed
- self-hosting results are acceptable
- architecture decisions are recorded
- the changelog is updated
- a human maintainer approves the release

## Maintenance Responsibility

The EDF maintainer is responsible for ensuring that framework components remain
internally consistent.

This includes alignment among:

- architecture
- governance
- templates
- generators
- Framework Advisor behavior
- adoption guidance
- release documentation

## Parent

- [Governance](README.md)

## Related Documents

- [Governance Overview](Governance_Overview.md)
- [Governance Analyzer Compliance](Analyzer_Compliance.md)
- [Governance Checklist](Governance_Checklist.md)
- [Documentation Change Management](Change_Management.md)
- [AI Repository Workflow](../AI/Repository_Workflow.md)
- [Documentation Architecture](../Architecture/Documentation_Architecture.md)
