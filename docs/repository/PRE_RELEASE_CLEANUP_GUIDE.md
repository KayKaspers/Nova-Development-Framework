# Pre-Release Cleanup Guide

## Zweck

Vor dem Foundation-0.1-Release soll das Repository öffentlich sauber wirken.

Der aktuelle Aufbau war korrekt für die Arbeitsphase, aber vor einem Release müssen temporäre Import- und Paketdateien aus dem Root entfernt oder verschoben werden.

## Ziele

- professionelle Root-README
- Root-Verzeichnis übersichtlich halten
- Import-Anleitungen archivieren
- Paket-Changelogs archivieren
- Release-Tag vorbereiten
- Repository öffentlich präsentierbar machen

## Was bleibt im Root?

Empfohlen:

```text
README.md
CHANGELOG.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
LICENSE
.gitattributes
.github/
academy/
adr/
branding/
build/
docs/
examples/
framework/
project-brain/
scripts/
standards/
templates/
```

## Was soll aus dem Root verschwinden?

### Import-Anleitungen

Alle Dateien nach diesem Muster:

```text
NDF_*_IMPORT_ANLEITUNG.md
```

Ziel:

```text
docs/import-history/
```

### Paket-Changelogs

Alle Dateien nach diesem Muster:

```text
CHANGELOG_*.md
```

Ziel:

```text
docs/release/history/
```

### Alte Übersichtsdokumente

Zum Beispiel:

```text
NDF_*_Uebersicht.docx
NDF_*_Uebersicht.pdf
```

Ziel:

```text
docs/import-history/legacy-overviews/
```

## Was wird nicht automatisch bereinigt?

- `templates/`
- `standards/`
- `github-desktop-guide/`

Diese Ordner sollten später geprüft werden, aber nicht direkt vor dem Release blind gelöscht oder verschoben werden.

## Empfohlener Ablauf

1. Cleanup-Paket importieren.
2. Cleanup-Skript mit Dry Run prüfen.
3. Cleanup-Skript mit `-Apply` ausführen.
4. Änderungen in GitHub Desktop prüfen.
5. Commit erstellen.
6. Push origin.
7. Nova final prüfen lassen.
8. GitHub Release `v0.1.0-foundation` erstellen.
