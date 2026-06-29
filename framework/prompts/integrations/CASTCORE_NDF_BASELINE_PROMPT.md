---
id: ndf-integration-castcore-baseline-001
title: CastCore NDF Project System Baseline
version: 0.1
category: integrations
role: Claude Project Architect
supported_models: [Claude, ChatGPT]
risk_level: medium
requires_human_review: true
---

# NDF Prompt – CastCore Project System Baseline

## Ziel

Erstelle eine NDF Project System Baseline für CastCore.

## Aufgabe

1. Analysiere den aktuellen CastCore-Projektstand.
2. Erstelle Project Manifest.
3. Erstelle Project Profile.
4. Erstelle Capability Matrix.
5. Erstelle Compliance Check.
6. Erstelle Health Score.
7. Erstelle Work Package Queue.
8. Erstelle Risiken und Lessons Learned.

## Bekannte CastCore-Fakten

- Preflight 2.0 ist implementiert.
- CI war grün.
- FFmpeg Docker Build-Gate ist vorhanden.
- Tests sollen ffmpeg-frei/gemockt bleiben.
- `docs-status.json` kann durch Datumswerte instabil werden.
- Docker Build-Gates prüfen ffmpeg/ffprobe.

## Grenzen

- Keine Codeänderungen.
- Kein Commit.
- Kein Push.
- Keine CI-Änderungen.
- Keine großen Refactorings.

## Rückmeldung an Nova

1. Zusammenfassung
2. Erzeugte Artefakte
3. CastCore NDF-Level
4. Risiken
5. Empfohlene erste Work Packages
6. Offene Fragen
