# Project Brain – WP-039 Prompt & Checklist DE/EN Alignment Notes

## Was wurde gemacht?

- **12 Kern-Prompts** mit Sprachstatus-Zeile, kompaktem `## EN – Purpose`-Block (Zweck, Grenzen, Entscheidung, Feedback-Ziel) und bilingualer Nova-(ChatGPT)-Erklärung im Rückmeldungs-Abschnitt:
  - Project Adapter: Intake, System Baseline, Create (v0.1 legacy, mit Verweis auf v0.2-Flow)
  - Core/Review: Work Package Classification, Work Package Boundary Review
  - Security (priorisiert): Baseline Review, Finding Triage, Focused Code Fix, Fail-closed Config, Release Gate, Destructive Blueprint Review, Destructive Implementation Gate
- **7 Checklisten** mit bilingualem Zweck-Block (`## DE – Zweck` / `## EN – Purpose`): WP-Type, Project Adapter, Destructive Blueprint, Destructive Implementation Review, Owner-only Flow, Audit Privacy, Security Prompt.
- **Prompt-Index:** Classification-, Boundary-Review- und die 7 Security-Kern-Prompts ergänzt, „DE/EN core"-Markierung, Hinweis auf die Security Prompt Library.
- **Prompt-Library-Overview:** Sprachstatus-Absatz ergänzt.

## Kernentscheidungen

- Kein Big-Bang: EN-Zweck-Blöcke statt Vollübersetzung — ein EN-Nutzer versteht Zweck, Grenzen, Entscheidungswerte und Rückmeldeziel; die detaillierten Aufgabenschritte bleiben DE.
- Wichtige Abgrenzung überall wiederholt: Security Review ≠ Security Fix ≠ Health Score Update; kein Commit/Push durch den Implementation Agent; keine Secrets.
- Checklisten-Punktlisten (überwiegend EN-Fachbegriffe) bewusst nicht gedoppelt — nur der Zweck ist bilingual.

## Offene Folgearbeiten

1. Prompt library full DE/EN alignment (übrige ~14 Security-/Fach-Prompts, Blocks, Rollen-Prompts)
2. Checklist library full DE/EN alignment (übrige Checklisten in `framework/checklists/` und `security/`)
3. Security prompt full DE/EN pass (Aufgabenschritte der Security-Prompts)

## Nächste empfohlene WPs

1. Adapter-Praxistest (aus WP-034 offen)
2. ADR Consolidation (aus WP-033 offen)
3. `GITHUB_DESKTOP_WORKFLOW.md` EN-Spiegelung (klein, aus WP-038 offen)
