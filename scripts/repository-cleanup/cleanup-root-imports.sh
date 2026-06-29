#!/usr/bin/env bash
set -euo pipefail

APPLY="${1:-}"

IMPORT_DIR="docs/import-history"
LEGACY_DIR="docs/import-history/legacy-overviews"
HISTORY_DIR="docs/release/history"

mkdir -p "$IMPORT_DIR" "$LEGACY_DIR" "$HISTORY_DIR"

echo "Planned moves:"
echo

shopt -s nullglob

for file in NDF*IMPORT_ANLEITUNG.md; do
  echo "MOVE $file -> $IMPORT_DIR/$file"
  if [[ "$APPLY" == "--apply" ]]; then
    mv "$file" "$IMPORT_DIR/$file"
  fi
done

for file in CHANGELOG_*.md; do
  echo "MOVE $file -> $HISTORY_DIR/$file"
  if [[ "$APPLY" == "--apply" ]]; then
    mv "$file" "$HISTORY_DIR/$file"
  fi
done

for file in NDF*_Uebersicht.docx NDF*_Uebersicht.pdf; do
  echo "MOVE $file -> $LEGACY_DIR/$file"
  if [[ "$APPLY" == "--apply" ]]; then
    mv "$file" "$LEGACY_DIR/$file"
  fi
done

if [[ "$APPLY" != "--apply" ]]; then
  echo
  echo "Dry run only. Run with --apply to move files:"
  echo "./scripts/repository-cleanup/cleanup-root-imports.sh --apply"
fi
