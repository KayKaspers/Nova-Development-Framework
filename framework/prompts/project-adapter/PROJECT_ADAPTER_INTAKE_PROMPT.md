---
id: project-adapter-intake-001
title: Project Adapter Intake and Read-only Review
version: 0.2
category: project-adapter
role: Implementation Agent (e.g. Claude)
supported_models: [Claude, ChatGPT]
risk_level: low
requires_human_review: true
---

# Prompt – Project Adapter Intake & Read-only Review

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Analyze an existing project strictly read-only and produce an NDF adapter proposal: review report, recommended NDF level, first safe work packages. No code or config changes, never read or output secrets, no commit, no push — analysis and proposal only.

## Rolle

Du bist der Implementation Agent und analysierst ein bestehendes Projekt für die NDF-Adaption.

## Work Package Type

review-only

## Ziel

Analysiere das Zielprojekt ausschließlich lesend und erstelle einen NDF-Adapter-Vorschlag.

## Eingaben

- Ausgefülltes Intake-Template (`framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md`)
- Lesezugriff auf das Zielprojekt-Repository

## Aufgaben

1. Repository-Struktur, Stack, Doku-Stand, CI-Stand, Security-Merkmale und Release-Stand erfassen.
2. Destruktive Funktionen (Löschen, Bulk-Operationen, irreversible Aktionen) identifizieren und markieren.
3. Review Report nach `framework/templates/project-adapter/PROJECT_ADAPTER_REVIEW_REPORT_TEMPLATE.md` erstellen.
4. NDF-Level empfehlen (`docs/project-starter/NDF_LEVEL_GUIDE.md`).
5. 3–6 erste Work Packages vorschlagen — klein, typisiert, erstes WP sicher (review-only oder docs-only).

## Strikte Grenzen

- Keine Codeänderungen, keine Konfig- oder CI-Änderungen.
- Keine Secrets lesen, ausgeben oder kopieren (`.env`, Keys, Tokens, Credentials). Fundstellen nur als Risiko nennen, ohne Inhalt.
- Kein Commit, kein Push.
- Nur Analyse und Vorschlag — keine Umsetzung.
- Keine privaten Namen in öffentlich sichtbare Artefakte übernehmen (Public/Private-Status aus dem Intake beachten).

## Rückmeldung an Nova (zwingend)

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

Adapter-Konventionen beachten / follow the adapter conventions: `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` (Manifest, Output-Pfade, Health Score).

Struktur nach `framework/templates/RUECKMELDUNG_AN_NOVA_STANDARD.md`, mindestens:

1. Zusammenfassung der Analyse
2. Review Report (oder Verweis darauf)
3. Empfohlenes NDF-Level mit Begründung
4. Vorgeschlagene Work Packages mit Typen
5. Risiken / offene Punkte
6. Empfehlung: GO / REWORK / SPLIT / STOP
