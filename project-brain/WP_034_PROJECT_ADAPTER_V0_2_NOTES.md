# Project Brain – WP-034 Project Adapter v0.2 Notes

## Warum existiert WP-034?

NDF war nach der Neutralisierung öffentlich sauber, aber für Außenstehende fehlte der praktische Einstieg: Wie bringe ich ein *bestehendes* Projekt nach NDF? Der v0.1-Adapter (ein einzelnes Template + ein Prompt) war zu dünn. WP-034 macht den Adapter zu einem vollständigen, kopierbaren Prozess.

## Was wurde ergänzt?

- Guide mit 11 Phasen (0–10): `docs/project-starter/PROJECT_ADAPTER_V0_2.md`
- Checkliste: `framework/checklists/PROJECT_ADAPTER_CHECKLIST.md`
- 6 Templates unter `framework/templates/project-adapter/` (Intake, Review Report, Output-Struktur, WP-Queue, Health Score, Compliance Check)
- 2 Prompts unter `framework/prompts/project-adapter/` (Intake read-only, Project System Baseline)
- Helper überarbeitet: `docs/toolkit/PROJECT_ADAPTER_HELPER.md` (Entscheidungshilfe statt Ablaufkopie)

## Kernentscheidungen

- Phasen 0–1 sind strikt read-only; Baseline erst nach Nova-/Maintainer-Freigabe.
- Beispiel-IDs `SP-WP-xxx` sind explizit als Beispiel markiert; echte Projekte wählen ein eigenes neutrales Präfix.
- NDF-Artefakte sind im Zielprojekt additiv — keine Umbauten an Bestand.
- Alter v0.1-Adapter (`framework/templates/NDF_PROJECT_ADAPTER_TEMPLATE.md`, `framework/prompts/project-adapter/CREATE_PROJECT_ADAPTER.md`) bleibt als Altbestand erhalten.

## Offene Grenzen

- Ordner-Dopplung `project-adapter/` / `project-adapters/` — in WP-035 aufgelöst: v0.1-Prompt nach `project-adapter/` migriert.
- Der Adapter ist noch nicht an einem externen (nicht-Referenz-)Projekt erprobt.

## Nächste empfohlene WPs

1. Adapter-Praxistest an einem neutralen Beispielprojekt (z. B. examples/minimal-ndf-project erweitern)
2. Prompt-Index (`framework/prompts/PROMPT_INDEX.md`) um die neuen Adapter-Prompts ergänzen
3. ADR Consolidation (aus WP-033 offen)
