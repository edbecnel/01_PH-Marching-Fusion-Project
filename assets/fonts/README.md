# Bundled fonts for PDF manual builds

Typography matches GitHub Markdown rendering: **Noto Sans** (body) and **Noto Sans Mono** (code).

| Family | Files | License |
|--------|-------|---------|
| Noto Sans | `NotoSans/*.ttf` | [SIL Open Font License 1.1](https://scripts.sil.org/OFL) |
| Noto Sans Mono | `NotoSansMono/*.ttf` | [SIL Open Font License 1.1](https://scripts.sil.org/OFL) |

Source: [notofonts/noto-fonts](https://github.com/notofonts/noto-fonts) (hinted TTF subsets).

Configured in `scripts/build_manual/templates/header.tex` via `fontspec`.
