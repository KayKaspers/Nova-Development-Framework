---
id: ndf-adapter-create-project-adapter-001
title: Create Project Adapter
version: 0.1
category: project-adapter
role: Implementation Agent (e.g. Claude)
supported_models: [Claude, ChatGPT]
risk_level: low
requires_human_review: true
---

# NDF Prompt – Create Project Adapter (Legacy v0.1)

> Sprachstatus / Language status: DE/EN priority pass complete (Foundation 0.4, NDF-WP-060). Legacy-Kurzform; der vollständige v0.2-Flow ist PROJECT_ADAPTER_INTAKE_PROMPT.md + PROJECT_SYSTEM_BASELINE_PROMPT.md.

## DE – Zweck

Legacy-v0.1-Kurzform: ein bestehendes Projekt beschreiben und einen NDF-Adapter vorschlagen (Ziel, aktueller Stand, Standards, Quality Gates, erste Work Packages).

## EN – Purpose

Legacy v0.1 short form: describe an existing project and propose an NDF adapter (goal, current state, standards, quality gates, first work packages).

## DE – Verwendung / EN – When to Use

Nur für einen schnellen Überblick. Für echte Übernahmen den v0.2-Flow nutzen. / For a quick overview only. Use the v0.2 flow for real adoptions.

## DE – Aufgabe / EN – Tasks

1. Projektziel beschreiben / describe the project goal
2. Aktuellen Stand beschreiben / describe the current state
3. Relevante Standards listen / list relevant standards
4. Projektspezifische Quality Gates definieren / define project-specific quality gates
5. Regeln für den Implementation Agent definieren / define implementation-agent rules
6. Erste Work Packages vorschlagen / propose first work packages

Adapter-Konventionen (Foundation 0.4): `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md`.

## DE – Grenzen / EN – Boundaries

- Keine Codeänderungen. / No code changes.
- Kein Commit, kein Push. / No commit, no push.
- Keine privaten Namen/Domains/Secrets. / No private names/domains/secrets.

## DE – Rückmeldung an Nova (ChatGPT) / EN – Feedback to Nova (ChatGPT)

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role. Nutze den Standardblock `framework/templates/RUECKMELDUNG_AN_NOVA_STANDARD.md`. Der Human Maintainer bleibt final zuständig.
