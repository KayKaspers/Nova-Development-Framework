# NDF Prompt Library Overview

## Zweck

Die Prompt Library stellt wiederverwendbare, geprüfte und strukturierte Prompts bereit.

Rollenhinweis: Nova = ChatGPT-basierte Planungs-/Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`); ausführende Prompts richten sich an den Implementation Agent (z. B. Claude).

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
