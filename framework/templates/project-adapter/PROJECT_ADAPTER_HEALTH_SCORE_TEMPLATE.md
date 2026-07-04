# Initial Health Score (Template)

Initiale Gesundheitsbewertung nach der Adapter-Analyse. Kategorien und Regeln gemäß `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` (Foundation 0.4). Jede Bewertung braucht Evidenz — keine geratenen Werte. Skala: 0–10 pro Kategorie.

| Kategorie / Category | Score (0–10) | Evidenz / Evidence | Größtes Risiko / Top risk |
|---|---|---|---|
| Documentation | | | |
| Security | | | |
| Operations | | | |
| Testing / CI | | | |
| Release Readiness | | | |
| Maintainability | | | |
| Governance / Workflow | | | |
| i18n / Language Readiness | | | |

## Gesamteinschätzung / Overall

<!-- Durchschnitt oder gewichtete Einschätzung + 2-3 Sätze / average or weighted view + 2-3 sentences -->

## Empfohlenes NDF-Level / Recommended NDF level

<!-- 1–5 nach docs/project-starter/NDF_LEVEL_GUIDE.md -->

## Regeln / Rules

- Der initiale Score ist eine Baseline, kein Urteil über den Projektwert — er macht Fortschritt messbar. / The initial score is a baseline, not a verdict.
- Keine Scheingenauigkeit; fehlende Evidenz wird **nicht** positiv bewertet — `unknown` ist besser als erfundene Reife. / No false precision; missing evidence is not scored positively.
- Jeder Score wird begründet (Spalte Evidenz). / Every score is justified.
- Kategorien ohne Bewertungsgrundlage als `n/a` markieren — aber nur mit Begründung, nicht mit 0 bestrafen. / Mark unassessable categories `n/a` with a reason.
- Score-Änderungen später nur über `health-score-update`-Work-Packages mit Evidenz (vorher/nachher/Delta). / Later changes only via health-score-update work packages.
