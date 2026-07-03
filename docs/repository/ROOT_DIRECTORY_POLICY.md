# Root Directory Policy

## Zweck

Der Root des Repositories soll übersichtlich bleiben.

Diese Policy wird seit WP-032 automatisch durch den Public Quality Gate geprüft (siehe `PUBLIC_QUALITY_GATE.md`).

## Erlaubte Root-Dateien

- README.md
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- LICENSE
- CHANGELOG.md
- .gitignore
- .gitattributes

Roadmaps liegen unter `docs/roadmap/`, nicht im Root.

## Nicht mehr im Root erlaubt

Import-Paket-Artefakte gehören direkt nach `docs/import-history/` und werden im Root vom Quality Gate als Fehler gemeldet:

- Import-Anleitungen (`NDF_*IMPORT_ANLEITUNG.md`)
- Pack-READMEs (`README_WP_*.md`, `README_*PACK.md`)
- Paket-Changelogs (`CHANGELOG_WP_*.md`, `CHANGELOG_*_INTEGRATION.md`, …)

## Nicht erlaubt

- unbenannte Notizen
- doppelte README-Dateien
- generierte Exporte ohne Zielordner
- Screenshots im Root
- ZIP-Dateien im Repository

## Regel

Wenn eine Datei nicht innerhalb von 10 Sekunden erklärbar ist, gehört sie nicht in den Root.
