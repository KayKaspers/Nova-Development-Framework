# NDF-WP-152 – Token Efficiency & Context Budget Baseline (Notes)

## Ziel

Additive, docs-only Umsetzung der WP-151-Empfehlung: normale WPs sollen weniger Kontext laden, stabile Regeln seltener wiederholen, Skills selektiver nutzen und Session-Fortsetzungen über kurze Handoffs erlauben — ohne Sicherheits-/Review-/Neutralitäts-/Release-Gate zu schwächen. Kein neuer Skill, kein Subsystem.

## Ergebnis

**GO WITH NOTES – token efficiency and context budget baseline implemented.** Startgate bestanden: WP-151 committed (`ed2195a`), Working Tree sauber, `v1.0.0` annotated → `9dcadc1`, ADR-0031/0032 unverändert, 38 Skills.

## Status

Implemented, pending Nova review. Uncommitted für Human-Maintainer-Commit übergeben.

## Artefakte

Neu: `docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md`; Templates `CURRENT_STATE_TEMPLATE.md`, `SESSION_HANDOFF_TEMPLATE.md`, `LEAN_WP_PROMPT_TEMPLATE.md`, `REVIEW_ONLY_PROMPT_TEMPLATE.md`, `FIX_PROMPT_TEMPLATE.md` (unter `docs/templates/`); `docs/validation/v1-1/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md`; diese Notes. Additiv: `docs/agent-workflows/NDF_PROMPT_MODES.md` (Profile-Sektion). Minimal: README, CHANGELOG, V1_1_PLAN, Context Pack, Next Phase.

## Roadmap-Auswirkung

WP-152-Einschub umgesetzt. Neue aufsteigende Reihenfolge: WP-152 Token Efficiency & Context Budget Baseline → WP-153 External Validation Improvement → WP-154 Project Enablement Validation → WP-155 Public Documentation Polish → WP-156 v1.1 Readiness Review → WP-157 v1.1 Release Prep. Keine weitere Roadmap-Ausweitung. v1.1 bleibt planning only.

## Context Budgets

B0 Micro / B1 Lean (bevorzugter Normalfall) / B2 Standard / B3 Extended / B4 Exceptional (kein Standard; regelmäßiger B4-Bedarf ⇒ splitten). Keine schein-präzisen Tokenzahlen.

## Prompt Profiles

Lean / Handoff / Review-only / Fix — additiv zu Full/Standard/Short (unverändert). Lean bevorzugter Normalfall, aber fail-closed; Full Pflicht für Release/ADR/Security/v1.x/komplexe Reviews.

## Templates

Fünf kurze Templates, alle mit den vier Kurzregeln (keep short / no history duplication / reference rules / escalate budget), ohne private Daten.

## Skill-Entscheidung

Keine neuen Skills; 38 unverändert. Nutzungsregel: nicht alle default aktivieren; je Budget B0 0–1 … B4 nur mit Begründung; vier häufige Kandidaten benannt, nicht erzwungen. `ndf-token-budget-reviewer`/`ndf-session-handoff-runner` bleiben abgelehnt (Guidance/Template statt Skill).

## Pilot-Empfehlung

Operations-oriented consumer project (neutral) als erster project-local Pilot; testet CURRENT_STATE, SESSION_HANDOFF, Lean/Review-only/Fix, B0–B2, Short Report, Evidence Pack. Erfolgskriterien qualitativ (keine Tokenziele ohne Messdaten). NDF-Core-Härtung erst nach Pilot + Human-Maintainer-Entscheidung.

## Risiken

Lean-Übernutzung ohne Fail-Closed-Disziplin; Wirksamkeit noch ungemessen (Pilot liefert Evidenz); Skill-Merge/Adapter separat (WP-151); Roadmap-Konsistenz beim Renumbering.

## Nächster empfohlener Schritt

Human-Maintainer-Commit (`docs(context): add token efficiency baseline`), dann project-local Pilot im Operations-Archetyp; danach Bewertung einer NDF-Core-Härtung.

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-152 hat die aus WP-151 empfohlene Token-Efficiency-Baseline additiv und docs-only umgesetzt: Baseline-Guide, Context Budgets B0–B4, additive Prompt-Profile Lean/Handoff/Review-only/Fix, fünf Templates, Short Report, Evidence Pack, Skill Selection Rule, Fail-Closed-Regeln, neutraler project-local Pilot. Keine neuen/entfernten/umbenannten Skills, keine Scripts/Automation, kein MCP/API/OAuth/Netz, keine Git-/Release-Aktion. ADR-0031/0032 unverändert; v1.x-Kompatibilität gewahrt; v1.1 bleibt planning only. Roadmap auf WP-152…157 reconciled.
