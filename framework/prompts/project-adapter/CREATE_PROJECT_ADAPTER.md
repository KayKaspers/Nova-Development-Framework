---
id: ndf-adapter-create-project-adapter-001
title: Create Project Adapter
version: 0.1
category: project-adapter
role: Claude Architect
supported_models: [Claude, ChatGPT]
risk_level: low
requires_human_review: true
---

# NDF Prompt – Create Project Adapter

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Legacy v0.1 short form: describe an existing project and propose an NDF adapter (goal, current state, standards, quality gates, first work packages). No code changes, no commit, no push. For the full v0.2 flow use PROJECT_ADAPTER_INTAKE_PROMPT.md and PROJECT_SYSTEM_BASELINE_PROMPT.md.

## Ziel

Erstelle einen NDF Project Adapter für ein bestehendes Projekt.

## Aufgabe

1. Beschreibe Projektziel.
2. Beschreibe aktuellen Stand.
3. Liste relevante Standards.
4. Definiere projektspezifische Quality Gates.
5. Definiere Claude-Regeln.
6. Schlage erste Work Packages vor.

Adapter-Konventionen (Foundation 0.4): `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md`.

## Grenzen

- Keine Codeänderungen.
- Kein Commit.
- Kein Push.

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

Nutze den Standardblock Rückmeldung an Nova.
