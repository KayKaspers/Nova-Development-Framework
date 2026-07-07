# Foundation 0.6 – Work Package Queue

> Status: **Scope locked** (NDF-WP-085, 2026-07-07). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_6_SCOPE_LOCK.md](FOUNDATION_0_6_SCOPE_LOCK.md). / Scope locked; binding classification in the "Scope Lock" column.

| ID | Titel | Typ | Ziel | Abhängigkeiten | Scope Lock | Herkunft / Origin |
|---|---|---|---|---|---|---|
| NDF-WP-084 | Foundation 0.6 Planning | docs-only / planning | Plan, WP-Kandidaten, Criteria-Draft, Brain-Notes | 0.5 released (WP-083) | **erledigt** (Planung, 2026-07-07) | — |
| NDF-WP-085 | Foundation 0.6 Scope Lock | docs-only / planning-gate | Umfang einfrieren, Ventil-Frage für WP-088, Änderungsregeln | WP-084 | **release-blocking** (Gate — abgeschlossen mit dem Scope-Lock-Dokument, NDF-WP-085) | 0.5-Muster |
| NDF-WP-086 | ADR Policy Decision | docs-only / adr-policy | ADR-Policy **entscheiden**: Nummernraum, Ablageort, Altbestand — oder ehrlich streichen; nur Entscheidung/Plan, keine Migration | WP-085 | **release-blocking** — entschieden in WP-086: **Minimal ADR Policy adopted** ([`docs/adr/ADR_POLICY.md`](../adr/ADR_POLICY.md) + Template + Index-Update; Massenmigration bleibt deferred) | WP-063/076, zweimal verschoben |
| NDF-WP-087 | Public SampleProject Runbook Validation Preparation | docs-only | Nur falls nötig: WP-073-Unterlagen für den öffentlichen Fixture-Lauf nachschärfen (Erwartung: minimal, Unterlagen sind nutzbar) | WP-085 | optional — **skipped/not needed** (WP-088 wurde direkt mit den WP-073-Unterlagen bestätigt) | WP-073 |
| NDF-WP-088 | Public SampleProject Runbook Validation Run | review-only | Runbook-basierter unabhängiger Lauf gegen das **öffentliche** Fixture; hebt v1.0-External-Validation Richtung `met` | WP-085 (+087 falls nötig) | **release-blocking** — durchgeführt in WP-088: unabhängig positiv bestätigt, **PASS WITH NOTES** ([independent-runs/2026-07-07](../validation/project-adapter/independent-runs/2026-07-07-public-sampleproject-runbook-validation/README.md)); Ventil nicht benötigt | WP-074-Note IAV-002, v1.0-tracked |
| NDF-WP-089 | Quality Gate Maintenance Review | review-only + docs-only | Gate-Nachlauf: weiterhin grün, Doku/Checkliste aktuell, kleine Härtung nur bei Bedarf | WP-085 | **release-blocking** (leichtgewichtig; inkl. CI-Denylist-Wirksamkeitsbewertung) | WP-066/078 |
| NDF-WP-090 | CI Denylist Effectiveness Proof | review-only | Nachweis, dass die CI-Denylist mit gesetztem Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` tatsächlich greift (z. B. CI-Log-Verifikation) | WP-085 | **merged/conditional** — Teil von WP-089; nur eigenständig, wenn WP-089 ein separates Nachweis-Artefakt für nötig erklärt | WP-078-Prüfpunkt |
| NDF-WP-091 | Checklist DE/EN Priority Pass | docs-only / i18n | Übrige Checklisten DE/EN-Kern | WP-085 | optional (should-have) | WP-061/075, zweimal offen |
| NDF-WP-092 | Academy Entry Pass | docs-only / i18n | Einstiegskapitel DE/EN, von README verlinkt | WP-085 | optional (should-have) | WP-062/077 |
| NDF-WP-093 | v1.x Compatibility Policy Draft | docs-only / concept | Entwurf der v1.x-Kompatibilitätszusage (was verspricht v1.x: Struktur? Prompts? Konventionen?) — Draft, kein Versprechen | WP-085 | optional (should-have; v1.0-tracked — schließt die bewusste Lücke aus dem v1.0-Draft) | WP-079 offene Frage |
| NDF-WP-094 | Foundation 0.6 Release Readiness Review | review-only | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.6-Kriterien | blocking WPs done | **release-blocking** | Release-Muster |
| NDF-WP-095 | Foundation 0.6 Release Prep | docs-only / release-prep | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide (voraussichtlich `v0.6.0-foundation`) | WP-094 | **release-blocking** | Release-Muster |

## Deferred (verbindlich / binding)

- Vollständige Doku-Website / full documentation website (Konzept bleibt WP-080-Nachfolger)
- Vollständige i18n-Abdeckung / full i18n completion
- ADR-Massenmigration / ADR mass migration (erst nach der WP-086-Entscheidung, eigenes Vorhaben)
- v1.0 Release Candidate (ausschließlich späterer eigener v1.0-Zyklus)
- Großer Framework-Rewrite / large framework rewrite
- Neue Applikations-Features / new application features

## Regeln / Rules

- Die Einstufung ist mit NDF-WP-085 **verbindlich gelockt**. Änderungen (inkl. WP-088-Ventil) nur gemäß den Regeln in [FOUNDATION_0_6_SCOPE_LOCK.md](FOUNDATION_0_6_SCOPE_LOCK.md).
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock.
- Blocking Kern (verbindlich): Gates (085/094/095) + je ein Deliverable pro Leitideen-Hälfte (Governance → 086, Adoption Confidence → 088) + leichter Gate-Nachlauf (089).
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim.
