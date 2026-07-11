# Framework Self-Hosting

[Home](../../README.md) › [Project Index](../../PROJECT_INDEX.md) › [Governance](README.md) › Framework Self-Hosting

> **Status:** Maintained
> **Owner:** Engineering Documentation Framework
> **Applies To:** Engineering Documentation Framework repository only
> **Last Reviewed:** 2026-07-10
> **Review Frequency:** Per Release
> **Authoritative:** Yes

> **Note:** This is an EDF upstream reference copy. This project validates using the external EDF Framework Advisor. See [Project Governance](Project_Governance.md).

## Applicability

This document applies only to the Engineering Documentation Framework repository.

Projects adopting EDF may use the same validation approach, but they are not required to satisfy EDF-specific template, generator, analyzer, self-hosting, or release rules.

## Purpose

Self-hosting requires EDF to apply its own documentation architecture, governance, navigation, analyzer, and non-destructive tooling standards to the EDF repository.

## Requirements

EDF must validate:

- canonical repository structure
- required root documents
- AI handbook completeness
- Governance-domain completeness
- hierarchical Markdown navigation
- relative Markdown links
- orphan documents
- metadata and lifecycle validity
- ownership and review metadata
- overdue reviews
- analyzer read-only behavior
- PowerShell and Bash analyzer behavior
- accepted exceptions
- release readiness

## Validation Commands

### Bash

From the repository root, run:

```bash
./scripts/run_self_hosting_validation.sh
```

This is the normal macOS and Linux workflow. The wrapper automatically:

1. runs the Framework Advisor Stage 1 regression verification
2. validates Bash 3.2 compatibility and shell-script requirements
3. runs the Framework Advisor against the EDF repository
4. captures the complete output in a timestamped text report

If the wrapper is not executable, invoke it explicitly:

```bash
bash ./scripts/run_self_hosting_validation.sh
```

The `chmod` and `git update-index --chmod` commands are one-time repository setup actions, not part of every validation run.

### PowerShell

```powershell
.\scripts\run_self_hosting_validation.ps1
```

Each runner writes a timestamped report under:

```text
reports/self-hosting/
```

## Report Handling

The generated report is a project record and should be reviewed and committed to Git when it documents an implementation milestone or release-validation result.

## Pass Criteria

A stable EDF release requires:

- no unresolved critical findings
- no broken internal links
- no unexplained orphan canonical documents
- no invalid canonical lifecycle states
- no missing ownership on governed canonical documents
- no hidden accepted exceptions
- successful analyzer execution
- human review of the generated report

A numeric score is not a substitute for reviewing findings.

## Accepted Exceptions

Every accepted exception must identify:

- affected rule
- rationale
- owner
- approval
- review date
- resolution plan or permanent-exception status

## Release Gate

M5 release preparation must reference the latest reviewed self-hosting report.

EDF must not claim self-hosting compliance until the local report has been generated and reviewed by the maintainer.

## Parent

- [Governance](README.md)

## Related Documents

- [EDF Governance](EDF_Governance.md)
- [Governance Analyzer Compliance](Analyzer_Compliance.md)
- [Governance Checklist](Governance_Checklist.md)
- [Engineering Documentation Framework](https://github.com/edbecnel/Engineering-Documentation-Framework) — upstream self-hosting validation
- [Project Governance](Project_Governance.md)
- [AI Repository Workflow](../AI/Repository_Workflow.md)
