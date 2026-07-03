---
id: project-adapter-system-baseline-001
title: Project System Baseline for an Existing Project
version: 0.2
category: project-adapter
role: Implementation Agent (e.g. Claude)
supported_models: [Claude, ChatGPT]
risk_level: medium
requires_human_review: true
---

# Prompt – Project System Baseline

## Rolle

Du bist der Implementation Agent und legst nach freigegebener Analyse die NDF-Baseline im Zielprojekt an.

## Work Package Type

docs-only / project-adapter

## Voraussetzung

Der Read-only Review (Intake-Prompt) wurde durchgeführt und von Nova bzw. dem menschlichen Maintainer freigegeben. Ohne Freigabe: STOP.

## Ziel

Erstelle die NDF Project-System-Dateien im Zielprojekt gemäß `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`.

## Erlaubte Dateien (allowed files)

Nur diese Dateien anlegen oder ändern:

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.yaml
project-system/CAPABILITY_MATRIX.md
project-system/COMPLIANCE_CHECK.md
project-system/HEALTH_SCORE.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
docs/ndf/README.md
docs/ndf/ADOPTION_NOTES.md
```

## Aufgaben

1. Inhalte aus dem freigegebenen Review Report übernehmen — Realität dokumentieren, nicht Wunschzustand.
2. Specs aus `docs/project-system/` einhalten; Vorlagen aus `framework/project-starter/templates/` und `framework/templates/project-adapter/` nutzen.
3. Work Package Queue mit projektspezifischem neutralem ID-Präfix anlegen (Beispielpräfix `SP-WP-` durch eigenes ersetzen).
4. Health Score nur mit Evidenz aus dem Review befüllen; Unbewertbares als `n/a`.

## Strikte Grenzen

- Keine funktionalen Codeänderungen.
- Keine CI-/Workflow-Änderungen.
- Keine Secrets lesen, ausgeben oder referenzieren.
- Keine bestehenden Projektdateien umbauen oder löschen — NDF-Artefakte sind additiv.
- Kein Commit, kein Push — Staging und Commit macht der menschliche Maintainer.
- Keine privaten Namen in öffentlich sichtbare Artefakte übernehmen.

## Rückmeldung an Nova (zwingend)

1. Zusammenfassung: welche Dateien wurden angelegt
2. Abweichungen von Templates/Specs mit Begründung
3. Offene Felder, die der Maintainer ergänzen muss
4. Vorschlag für das erste umzusetzende Work Package
5. Empfehlung: GO / REWORK / SPLIT / STOP
