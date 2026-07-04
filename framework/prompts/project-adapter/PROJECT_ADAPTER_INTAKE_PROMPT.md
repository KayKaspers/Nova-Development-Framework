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

> Sprachstatus / Language status: DE/EN priority pass complete (Foundation 0.4, NDF-WP-060). DE und EN sind gleichwertig nutzbar. / DE and EN are equally usable.

## DE – Zweck

Ein bestehendes Projekt streng read-only analysieren und einen NDF-Adapter-Vorschlag erstellen: Review Report, empfohlenes NDF-Level, erste sichere Work Packages.

## EN – Purpose

Analyze an existing project strictly read-only and produce an NDF adapter proposal: review report, recommended NDF level, first safe work packages.

## DE – Rolle / EN – Role

Du bist der Implementation Agent (z. B. Claude) und analysierst ein bestehendes Projekt für die NDF-Adaption. / You are the Implementation Agent (e.g. Claude) analyzing an existing project for NDF adoption.

Work Package Type: `review-only`

## DE – Verwendung / EN – When to Use

Als **Phase 0/1** des Project Adapters, bevor Baseline-Artefakte erzeugt werden. / As **phase 0/1** of the project adapter, before baseline artifacts are created.

## DE – Eingaben / EN – Inputs

- Ausgefülltes Intake-Template (`framework/templates/project-adapter/PROJECT_ADAPTER_INTAKE_TEMPLATE.md`) / filled intake template
- Lesezugriff auf das Zielprojekt-Repository / read access to the target project repository

## DE – Aufgaben / EN – Tasks

1. Repository-Struktur, Stack, Doku-Stand, CI-Stand, Security-Merkmale und Release-Stand erfassen. / Capture structure, stack, docs, CI, security and release state.
2. Destruktive Funktionen (Löschen, Bulk-Operationen, irreversible Aktionen) identifizieren und markieren. / Identify and mark destructive functions.
3. Review Report nach `framework/templates/project-adapter/PROJECT_ADAPTER_REVIEW_REPORT_TEMPLATE.md` erstellen. / Produce the review report.
4. NDF-Level empfehlen (`docs/project-starter/NDF_LEVEL_GUIDE.md`). / Recommend the NDF level.
5. 3–6 erste Work Packages vorschlagen — klein, typisiert, erstes WP sicher (review-only oder docs-only). / Propose 3–6 first work packages; the first must be safe.

## DE – Grenzen / EN – Boundaries

- Keine Codeänderungen, keine Konfig- oder CI-Änderungen. / No code, config or CI changes.
- Keine Secrets lesen, ausgeben oder kopieren (`.env`, Keys, Tokens, Credentials); Fundstellen nur als Risiko nennen, ohne Inhalt. / Never read, output or copy secrets; report locations as risk only.
- Kein Commit, kein Push — nur Analyse und Vorschlag. / No commit, no push — analysis and proposal only.
- Keine privaten Namen in öffentlich sichtbare Artefakte übernehmen (Public/Private-Status aus dem Intake beachten). / No private names in public artifacts.
- Adapter-Konventionen beachten: `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md`. / Follow the adapter conventions.

## DE – Erwartete Ausgabe / EN – Expected Output

Ein Review Report plus die strukturierte Rückmeldung an Nova (siehe unten). / A review report plus the structured feedback to Nova (below).

## DE – Rückmeldung an Nova (ChatGPT) / EN – Feedback to Nova (ChatGPT)

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

Struktur nach `framework/templates/RUECKMELDUNG_AN_NOVA_STANDARD.md`, mindestens / at minimum:

1. Zusammenfassung der Analyse / analysis summary
2. Review Report (oder Verweis darauf) / review report or reference
3. Empfohlenes NDF-Level mit Begründung / recommended NDF level with reasoning
4. Vorgeschlagene Work Packages mit Typen / proposed work packages with types
5. Risiken / offene Punkte / risks and open points
6. Empfehlung: GO / REWORK / SPLIT / STOP / recommendation

Der Human Maintainer bleibt final zuständig. / The human maintainer remains the final authority.
