#!/usr/bin/env bash
set -e

echo "NDF Repository Safety Check"
echo "---------------------------"

if [ ! -d .git ]; then
  echo "ERROR: Kein Git-Repository gefunden."
  exit 1
fi

git status --short

echo "Check abgeschlossen. Bitte Änderungen manuell prüfen."
