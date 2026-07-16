# PDF Manual Releases

Offline-readable PDF exports of project documentation. **Distribute all PDFs in a release folder together** so cross-volume links work.

## Latest release: 2026.07

| PDF | Description |
|-----|-------------|
| [00-Trainers-Manual.pdf](2026.07/00-Trainers-Manual.pdf) | Field teaching handbook (start here for instructors) |
| [01-Specifications.pdf](2026.07/01-Specifications.pdf) | Identity framework, blueprint, design principles |
| [02-Reference.pdf](2026.07/02-Reference.pdf) | Concept library, technique, sound model |
| [03-User-Guides.pdf](2026.07/03-User-Guides.pdf) | Instructor, pilot, arranging, education |
| [04-Research.pdf](2026.07/04-Research.pdf) | Indigenous percussion, Kaamulan, heritage |
| [05-Architecture.pdf](2026.07/05-Architecture.pdf) | Documentation architecture, ADRs |
| [06-Governance.pdf](2026.07/06-Governance.pdf) | EDF governance |
| [07-AI-Development.pdf](2026.07/07-AI-Development.pdf) | AI workflow and project journal |
| [08-Templates-and-Placeholders.pdf](2026.07/08-Templates-and-Placeholders.pdf) | Templates and EDF placeholders |
| [09-Student-Practice-Guide.pdf](2026.07/09-Student-Practice-Guide.pdf) | Student orientation and technique reference |

Build metadata: [manifest.json](2026.07/manifest.json)

## Rebuilding for a new release

Maintainers regenerate PDFs with [scripts/build_manual](../../scripts/build_manual/README.md), then commit the updated `dist/manual/{version}/` folder.

For tracing PDF errors back to source Markdown and handling build warnings, see [PDF maintainer workflow](../../manual/MAINTAINER_WORKFLOW.md).

```bash
./scripts/build_manual/build.sh 2026.07
```
