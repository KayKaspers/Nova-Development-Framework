# Foundation 0.6 – Work Package Candidates (Draft)

> Status: **Kandidatenplan aus NDF-WP-084 — kein Scope Lock.** Die Spalte „Empfehlung" ist vorläufig; verbindlich wird die Einstufung erst mit NDF-WP-085. / Candidate plan from NDF-WP-084 — not a scope lock; classification becomes binding only with NDF-WP-085.

| ID | Titel | Typ | Ziel | Abhängigkeiten | Empfehlung (vorläufig) / Recommendation (preliminary) | Herkunft / Origin |
|---|---|---|---|---|---|---|
| NDF-WP-084 | Foundation 0.6 Planning | docs-only / planning | Plan, WP-Kandidaten, Criteria-Draft, Brain-Notes | 0.5 released (WP-083) | **erledigt mit diesem Dokument** | — |
| NDF-WP-085 | Foundation 0.6 Scope Lock | docs-only / planning-gate | Umfang einfrieren, Ventil-Frage für WP-088, Änderungsregeln | WP-084 | **recommended release-blocking candidate** (Gate) | 0.5-Muster |
| NDF-WP-086 | ADR Policy Decision | docs-only / adr-policy | ADR-Policy **entscheiden**: Nummernraum, Ablageort, Altbestand — oder ehrlich streichen; nur Entscheidung/Plan, keine Migration | WP-085 | **recommended release-blocking candidate** — 0.5-Sonderregel: kein drittes stilles Verschieben | WP-063/076, zweimal verschoben |
| NDF-WP-087 | Public SampleProject Runbook Validation Preparation | docs-only | Nur falls nötig: WP-073-Unterlagen für den öffentlichen Fixture-Lauf nachschärfen (Erwartung: minimal, Unterlagen sind nutzbar) | WP-085 | recommended optional candidate (if needed) | WP-073 |
| NDF-WP-088 | Public SampleProject Runbook Validation Run | review-only | Runbook-basierter unabhängiger Lauf gegen das **öffentliche** Fixture; hebt v1.0-External-Validation Richtung `met` | WP-085 (+087 falls nötig) | **recommended release-blocking candidate** — WP-085 sollte ein Ventil analog 0.5 prüfen (personenabhängig) | WP-074-Note IAV-002, v1.0-tracked |
| NDF-WP-089 | Quality Gate Maintenance Review | review-only + docs-only | Gate-Nachlauf: weiterhin grün, Doku/Checkliste aktuell, kleine Härtung nur bei Bedarf | WP-085 | **recommended release-blocking candidate** (leichtgewichtig; erstmals seit v0.2 fällig) | WP-066/078 |
| NDF-WP-090 | CI Denylist Effectiveness Proof | review-only | Nachweis, dass die CI-Denylist mit gesetztem Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` tatsächlich greift (z. B. CI-Log-Verifikation) | WP-085 | recommended optional candidate — **entfällt, wenn WP-089 den Nachweis mit erbringt** | WP-078-Prüfpunkt |
| NDF-WP-091 | Checklist DE/EN Priority Pass | docs-only / i18n | Übrige Checklisten DE/EN-Kern | WP-085 | recommended optional candidate | WP-061/075, zweimal offen |
| NDF-WP-092 | Academy Entry Pass | docs-only / i18n | Einstiegskapitel DE/EN, von README verlinkt | WP-085 | recommended optional candidate | WP-062/077 |
| NDF-WP-093 | v1.x Compatibility Policy Draft | docs-only / concept | Entwurf der v1.x-Kompatibilitätszusage (was verspricht v1.x: Struktur? Prompts? Konventionen?) — Draft, kein Versprechen | WP-085 | recommended optional candidate (v1.0-tracked; schließt die bewusste Lücke aus dem v1.0-Draft) | WP-079 offene Frage |
| NDF-WP-094 | Foundation 0.6 Release Readiness Review | review-only | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.6-Kriterien | blocking WPs done | **recommended release-blocking candidate** | Release-Muster |
| NDF-WP-095 | Foundation 0.6 Release Prep | docs-only / release-prep | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide (voraussichtlich `v0.6.0-foundation`) | WP-094 | **recommended release-blocking candidate** | Release-Muster |

## Recommended deferred candidates

- Vollständige Doku-Website / full documentation website (Konzept bleibt WP-080-Nachfolger)
- Vollständige i18n-Abdeckung / full i18n completion
- ADR-Massenmigration / ADR mass migration (erst nach der WP-086-Entscheidung, eigenes Vorhaben)
- v1.0 Release Candidate (ausschließlich späterer eigener v1.0-Zyklus)

## Regeln / Rules

- **Kandidatenplan** — finale Einstufung (release-blocking / optional / deferred) trifft ausschließlich NDF-WP-085.
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock.
- Empfohlener kleiner blocking Kern: Gates (085/094/095) + je ein Deliverable pro Leitideen-Hälfte (Governance → 086, Adoption Confidence → 088) + leichter Gate-Nachlauf (089).
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim.
