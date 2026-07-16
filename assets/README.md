[Home](../README.md) › [Project Index](../PROJECT_INDEX.md) › Assets

# Assets

> **Status:** Maintained
> **Owner:** Philippine Marching Percussion Fusion Project
> **Applies To:** Project branding and shared visual assets
> **Last Reviewed:** 2026-07-13
> **Review Frequency:** On change
> **Authoritative:** Yes

## Purpose

This directory holds canonical project branding and shared visual assets. It is a deliberate project extension outside `docs/`, alongside `scores/`, `audio/`, and `references/`.

## Contents

| File | Use |
|---|---|
| [ph-marching-fusion-logo.png](ph-marching-fusion-logo.png) | Primary project logo |
| [fonts/](fonts/) | Noto Sans + Noto Sans Mono (PDF manual typography) |

## Usage

Reference the primary logo from documentation and README files with a relative path:

```markdown
![Philippine Marching Percussion Fusion Project](assets/ph-marching-fusion-logo.png)
```

The root [README](../README.md) displays this logo as the public landing-page identity.

## Placement Rules

- Store **canonical** logo and brand image masters here.
- Do not place logos in `docs/User_Guides/` or other documentation domains.
- Exported copies embedded in score PDFs or handouts should trace back to files in this directory.
- Add new variants (for example SVG or icon-only marks) to this directory with clear filenames and update this README.

## Related Documents

- [Documentation Architecture](../docs/Architecture/Documentation_Architecture.md)
- [EDF Adoption Guide](../ENGINEERING_DOCUMENTATION_FRAMEWORK.md)
- [Project Governance](../docs/Governance/Project_Governance.md)
