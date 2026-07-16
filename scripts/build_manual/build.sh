#!/usr/bin/env bash
# Build all PDF manuals. Requires: pandoc, tectonic, Python 3 + PyYAML.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
export PATH="/opt/homebrew/bin:${PATH:-}"

PYTHON="${PYTHON:-python3}"
if ! "$PYTHON" -c "import yaml" 2>/dev/null; then
  if [ -x "$ROOT/.venv/bin/python" ]; then
    PYTHON="$ROOT/.venv/bin/python"
  elif [ -x /opt/anaconda3/bin/python3 ]; then
    PYTHON=/opt/anaconda3/bin/python3
  fi
fi

VERSION="${1:-unreleased}"
exec "$PYTHON" scripts/build_manual/build_manual.py --version "$VERSION" "${@:2}"
