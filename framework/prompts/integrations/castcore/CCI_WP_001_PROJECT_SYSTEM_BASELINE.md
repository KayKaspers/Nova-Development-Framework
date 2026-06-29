---
id: castcore-cci-wp-001-project-system-baseline
title: CastCore Project System Baseline
version: 0.1
category: integrations/castcore
role: Claude Project Architect
supported_models: [Claude, ChatGPT]
risk_level: medium
requires_human_review: true
---

# Claude Prompt – CastCore Project System Baseline

## Rolle

Du bist Claude und arbeitest im Nova Development Framework.

## Ziel

Erstelle im CastCore-Repository eine NDF Project System Baseline.

## Aufgabe

Lege folgende Dateien an:

```text
project-system/project-manifest.yaml
project-system/PROJECT_PROFILE.md
project-system/CAPABILITY_MATRIX.md
project-system/COMPLIANCE_CHECK.md
project-system/HEALTH_SCORE.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
project-brain/RISKS.md
project-brain/LESSONS_LEARNED.md
docs/ndf/WORKFLOW.md
docs/ndf/QUALITY_GATES.md
```

## Bekannte CastCore-Fakten

- Preflight 2.0 ist implementiert.
- CI war zuletzt grün.
- FFmpeg Docker Build-Gate ist vorhanden.
- Tests sollen ffmpeg-frei/gemockt bleiben.
- `docs-status.json` kann durch Datumswerte instabil werden.
- Docker Build-Gates prüfen ffmpeg/ffprobe.

## Grenzen

- Keine Codeänderungen.
- Keine CI-Änderungen.
- Kein Commit.
- Kein Push.
- Keine Dateien löschen.
- Keine großen Umstrukturierungen.

## Akzeptanzkriterien

- Alle NDF-Artefakte sind erstellt.
- Inhalte spiegeln den realen CastCore-Stand wider.
- Risiken sind klar dokumentiert.
- Work Package Queue enthält kleine nächste Schritte.
- Rückmeldung an Nova ist vorhanden.

## Rückmeldung an Nova

Bitte am Ende:

1. Zusammenfassung
2. Erzeugte Dateien
3. Wichtigste Entscheidungen
4. Risiken
5. Empfohlene nächste Work Packages
6. Offene Fragen
