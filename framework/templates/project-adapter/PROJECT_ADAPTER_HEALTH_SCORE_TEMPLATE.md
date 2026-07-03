# Initial Health Score (Template)

Initiale Gesundheitsbewertung nach der Adapter-Analyse. Jede Bewertung braucht Evidenz — keine geratenen Werte. Skala: 0–10 pro Kategorie.

| Kategorie | Score (0–10) | Evidenz | Größtes Risiko |
|---|---|---|---|
| Documentation | | | |
| Security | | | |
| CI/CD | | | |
| Release Readiness | | | |
| Architecture | | | |
| Testing | | | |
| Maintainability | | | |
| Project Brain | | | |
| Workflow Adoption | | | |

## Gesamteinschätzung

<!-- Durchschnitt oder gewichtete Einschätzung + 2-3 Sätze -->

## Empfohlenes NDF-Level

<!-- 1–5 nach docs/project-starter/NDF_LEVEL_GUIDE.md -->

## Regeln

- Der initiale Score ist eine Baseline, kein Urteil — er macht Fortschritt messbar.
- Score-Änderungen später nur über `health-score-update`-Work-Packages mit Evidenz (vorher/nachher/Delta).
- Kategorien ohne Bewertungsgrundlage als `n/a` markieren, nicht mit 0 bestrafen.
