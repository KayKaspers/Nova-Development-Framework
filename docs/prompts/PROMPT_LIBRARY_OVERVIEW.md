# NDF Prompt Library Overview

## Zweck

Die Prompt Library stellt wiederverwendbare, geprüfte und strukturierte Prompts bereit.

Rollenhinweis: Nova = ChatGPT-basierte Planungs-/Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`); ausführende Prompts richten sich an den Implementation Agent (z. B. Claude).

Sprachstatus / Language status: Kern-Prompts (Adapter, Core, Review, priorisierte Security) tragen seit WP-039 DE/EN-Zweck- und Grenzen-Blöcke; Details siehe `docs/i18n/TRANSLATION_STATUS.md`. / Core prompts carry DE/EN purpose and boundary blocks since WP-039.

DE/EN Priority Pass (Foundation 0.4, NDF-WP-060): Zuerst nutzen — die fünf Adoptions-Erstkontakt-Prompts (Project Adapter Intake/Baseline/Create, Work Package Classification, Boundary Review) sind vollständig DE/EN. Danach die priorisierten Security-/Gate-Prompts (DE/EN-Kern). Restarbeiten transparent: `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md`; NDF ist kein v1.0. / Use first: the five fully bilingual adoption first-contact prompts, then the prioritized security/gate prompts.

## Kategorien

```text
framework/prompts/
├── core/
├── roles/
├── architecture/
├── development/
├── documentation/
├── testing/
├── devops/
├── security/
├── review/
├── project-adapter/
└── blocks/
```

## Prompt-Grundstruktur

Jeder NDF-Prompt enthält:

1. Rolle
2. Ziel
3. Kontext
4. Aufgabe
5. Grenzen
6. Qualitätsregeln
7. Erwartete Ausgabe
8. Rückmeldung an Nova

## Grundregel

Ein Prompt darf nie unklar lassen, was getan werden soll und was nicht getan werden darf.
