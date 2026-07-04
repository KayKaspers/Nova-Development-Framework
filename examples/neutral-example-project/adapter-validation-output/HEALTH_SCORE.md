# Health Score – SampleProject (initial, Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.

Skala 0–10 je Kategorie (gemäß `framework/templates/project-adapter/PROJECT_ADAPTER_HEALTH_SCORE_TEMPLATE.md`). Änderungen später nur über `health-score-update`-WPs mit Evidenz. Unbekanntes wird nicht positiv bewertet, bewusst fehlende Fixture-Details nicht doppelt bestraft (als Risiko vermerkt).

| Kategorie | Score | Evidenz | Größtes Risiko |
|---|---|---|---|
| Documentation | 3 | Doku existiert, aber unvollständig + widersprüchlich (SP-F-001/002) | Onboarding unmöglich |
| Security | 2 | Auth vorhanden; keine Rollen, kein Audit, Secrets ungeklärt (SP-F-008–010) | Leak / unbefugtes Löschen |
| CI/CD | 2 | Workflow existiert, rot + ignoriert (SP-F-003) | Regressionen unbemerkt |
| Release Readiness | 1 | kein Prozess, kein Backup, kein Rollback (SP-F-013) | Datenverlust bei Update |
| Architecture | 4 | einfach und funktionsfähig; undokumentiert, offene Fragen | Wissensverlust |
| Testing | 2 | Alt-Tests vorhanden, Abdeckung unknown | falsches Vertrauen |
| Maintainability | 3 | läuft, aber Tech-Debt: doppelte Konfig, tote Branches (SP-F-014) | steigende Änderungskosten |
| Project Brain | 0 → 1 | vor Adapter keiner; initial erstellt, ungelebt | Pflege schläft ein |
| Workflow Adoption | 0 → 1 | vor Adapter keiner; Queue initial | Rückfall in Zuruf-Arbeit |
| Operations/Backup* | 1 | Backup „TODO", Ein-Personen-Wissen (SP-F-013/016) | Ausfall des Maintainers |
| i18n* | 2 | gemischt, unentschieden, aber ehrlich benannt (SP-F-015) | inkonsistente Doku |

\* Zusatzkategorien dieser Validierung — im Adapter-Template nicht enthalten (siehe Improvement Backlog).

## Gesamteinschätzung

**≈ 2/10.** SampleProject funktioniert im Alltag, ist aber undokumentiert, ungesichert und unstrukturiert — typisches gewachsenes Level-0-Projekt. Die Baseline hebt Governance-Kategorien von 0 auf 1; echte Verbesserung kommt aus der Work Package Queue.

## Empfohlenes NDF-Level

**Level 0 (Ist)** → Level 1 nach Commit der Baseline-Artefakte; Level 2 erreichbar nach SP-WP-001–004.
