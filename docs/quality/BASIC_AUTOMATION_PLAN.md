# Basic Automation Plan

## Zweck

Foundation 0.2 soll erste einfache Qualitätsprüfungen vorbereiten oder einführen.

Die Checks sollen helfen, ohne das Projekt unnötig kompliziert zu machen.

## Ziele

- Markdown-Probleme früh erkennen
- tote Links erkennen
- Repository-Struktur prüfen
- Release-Dateien nachvollziehbar halten
- neue Fehler durch schnelle Paketimporte vermeiden

## Grundsatz

```text
Automation supports quality. It does not replace human review.
```

## Check 1 – Markdown Lint

### Ziel

Markdown-Dateien auf einfache Strukturprobleme prüfen.

### Mögliche Prüfungen

- Überschriftenstruktur
- trailing spaces
- fehlende Leerzeilen
- Codeblöcke
- doppelte H1

### Risiko

Zu strenge Regeln können den Arbeitsfluss stören.

### Empfehlung

Zunächst nur Warning-Level.

## Check 2 – Link Check

### Ziel

Interne Links und externe Links prüfen.

### Mögliche Tools

- markdown-link-check
- lychee
- MkDocs strict mode

### Risiko

Externe Links können zeitweise fehlschlagen.

### Empfehlung

Zuerst interne Links priorisieren.

## Check 3 – Repository Structure Check

### Ziel

Prüfen, ob kritische Dateien und Ordner existieren.

### Beispiele

- README.md
- CHANGELOG.md
- docs/
- framework/prompts/
- framework/templates/
- project-brain/
- adr/

### Empfehlung

Ein einfaches Python- oder PowerShell-Skript reicht zunächst.

## Check 4 – Release Readiness Check

### Ziel

Vor Releases prüfen, ob die Release-Artefakte vorhanden sind.

### Beispiele

- Release Notes
- Checklist
- Version Manifest
- ADR
- Project Brain Notes

## Foundation 0.2 Mindestziel

Mindestens:

- Basic Automation Plan
- lokale Check-Anleitung
- optional erster GitHub Actions Draft

## Nicht-Ziel

Keine harte CI-Blockade, solange die Regeln noch nicht stabil sind.
