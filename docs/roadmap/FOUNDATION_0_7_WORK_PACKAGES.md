# Foundation 0.7 – Work Package Queue

> Status: **Scope locked** (NDF-WP-098, 2026-07-08). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_7_SCOPE_LOCK.md](FOUNDATION_0_7_SCOPE_LOCK.md). / Scope locked; binding classification in the "Scope Lock" column.

## Vorgeschlagene Queue / Proposed Queue

| ID | Titel | Typ | Ziel | Abhängigkeiten | Scope Lock | Herkunft / Origin |
|---|---|---|---|---|---|---|
| NDF-WP-097 | Foundation 0.7 Planning | docs-only / planning | Plan, WP-Kandidaten, Criteria-Draft, Brain-Notes | 0.6 released (WP-096) | **erledigt** (Planung, 2026-07-07) | — |
| NDF-WP-098 | Foundation 0.7 Scope Lock | docs-only / planning-gate | Umfang einfrieren, WP-102-Ventil-Frage, WP-099-Korridor, Änderungsregeln | WP-097 | **release-blocking** (Gate — abgeschlossen mit dem Scope-Lock-Dokument, NDF-WP-098) | 0.5/0.6-Muster |
| NDF-WP-099 | Checklist DE/EN Decision | docs-only / decision | **Entscheiden:** priorisieren (release-blocking) / optional-mit-Begründung / streichen — kein viertes stilles Verschieben | WP-098 | **release-blocking** — entschieden in WP-099: **Option B — optional mit finaler Begründung** ([`FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md`](FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md); kein Auto-Carry mehr, kein Folge-WP nötig) | WP-061/075/091, mehrfach offen |
| NDF-WP-100 | v1.x Compatibility Policy Decision / ADR-0031 Preparation | docs-only / adr-policy | v1.x-Kompatibilitätszusage entwerfen (was verspricht v1.x: Struktur? Prompts? Konventionen?) — Draft, ggf. als ADR-0031 | WP-098 | **release-blocking** (Kern: Compatibility Governance) — entschieden in WP-100: **ADR-0031 angenommen** ([`ADR-0031-v1x-compatibility-policy.md`](../adr/ADR-0031-v1x-compatibility-policy.md)); Governance-Rahmen, volle v1.x-Zusage erst mit v1.0; kein v1.0-Claim | WP-079/093, offenes v1.0-Kriterium |
| NDF-WP-101 | Project Adapter Convention Stability Review | review-only / docs-only | Bestätigen, dass Adapter-Konventionen (Manifest, Output-Pfade, Health-Score) über 0.4→0.6 stabil/additiv sind; v1.0-Kriterium Richtung `met` | WP-098 | **release-blocking** (Kern: v1.0 Path Consolidation) — durchgeführt in WP-101: **Stable with notes** ([`PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md`](../validation/project-adapter/PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md)); Kriterium `met with notes` | v1.0-Draft `partially met` |
| NDF-WP-102 | External Validation Evidence Depth Pass | review-only | Detaillierterer öffentlicher Lauf mit ausgefülltem Feedback-Template; adressiert PSV-001 → Richtung volles PASS / `met` | WP-098 | **optional mit Upgrade-Ventil** — nur per Human-Maintainer-Scope-Change hochstufbar (Bedingungen im Scope Lock); sonst optional, PSV-001 v1.0-tracked | WP-088-Note PSV-001 |
| NDF-WP-103 | Academy Entry Decision | docs-only / i18n | **Entscheiden:** Academy-Einstieg priorisieren oder bewusst deferred; nicht still liegen lassen | WP-098 | optional (Entscheidungs-WP: priorisieren oder bewusst deferred) | WP-062/077/092, mehrfach offen |
| NDF-WP-104 | Foundation 0.7 Release Readiness Review | review-only | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.7-Kriterien | blocking WPs done | **release-blocking** — durchgeführt in WP-104: **GO WITH NOTES** ([`FOUNDATION_0_7_RELEASE_READINESS_REVIEW.md`](../release/FOUNDATION_0_7_RELEASE_READINESS_REVIEW.md); keine Blocker, Notes non-blocking) | Release-Muster |
| NDF-WP-105 | Foundation 0.7 Release Prep | docs-only / release-prep | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide (voraussichtlich `v0.7.0-foundation`) | WP-104 | **release-blocking** — erledigt in WP-105 (Release Notes/Go-No-Go/Tagging-Guide erstellt); Release am 2026-07-08 veröffentlicht | Release-Muster |
| NDF-WP-106 | Foundation 0.7 Post-Release Status Cleanup | docs-only / post-release-cleanup | Tag + GitHub Release read-only verifizieren, Status auf released/published heben | WP-105 + manueller Release | **erledigt** in WP-106 (2026-07-08: `v0.7.0-foundation` veröffentlicht und verifiziert; Statusdokumente released/published) | Release-Muster |

## Optionaler Scope (verbindlich / binding)

- NDF-WP-102 External Validation Evidence Depth Pass (falls WP-098 es nicht auf blocking hochstuft)
- NDF-WP-103 Academy Entry Decision
- Doku-/i18n-Konsolidierung (klein) / small documentation / i18n consolidation

## Deferred / Nicht-Ziele (verbindlich / binding)

- Vollständige Doku-Website / full documentation website
- Vollständige i18n-Abdeckung / full i18n completion
- ADR-Massenmigration / ADR mass migration
- v1.0 Release Candidate (nur späterer eigener v1.0-Zyklus)
- Großer Framework-Rewrite; neue Applikations-Features

## Manual / cosmetic (kein WP / no work package)

- Optionaler v0.6-GitHub-Release-Body-Polish: Der Body enthält die Pflichtaussage „This is not a v1.0 release.", ist aber minimal. Der Human Maintainer kann ihn optional per Release-Edit aus den Release Notes erweitern — **keine GitHub-Schreibaktion in NDF-WPs**, non-blocking.

## Future Candidate (nach Foundation 0.7 / after Foundation 0.7)

- **NDF Agent Enablement & Context Economy**, inkl. eines kleinen public-neutralen Claude Skills Pack — nur möglicher nächster Evolutionsschritt **nach** Foundation 0.7. **Kein Foundation-0.7-Scope, kein Release-Kriterium, kein blocking WP; wird in diesem Zyklus nicht erstellt.** Über Aufnahme entscheidet ein späterer eigener Planungszyklus. / Only a possible next evolution step after Foundation 0.7 — not scope, not a release criterion, not a blocking work package.

## Regeln / Rules

- Die Einstufung ist mit NDF-WP-098 **verbindlich gelockt**. Änderungen (inkl. WP-102-Upgrade-Ventil und WP-099-Korridor) nur gemäß den Regeln in [FOUNDATION_0_7_SCOPE_LOCK.md](FOUNDATION_0_7_SCOPE_LOCK.md).
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock.
- Blocking Kern (verbindlich): Gates (098/104/105) + je ein Deliverable pro Titel-Hälfte (Compatibility Governance → 100, v1.0 Path Consolidation → 101) + die überfällige Checklist-Entscheidung (099).
- **WP-099 und WP-103 sind Entscheidungs-WPs** — sie dürfen mit „streichen"/„bewusst deferred mit Begründung" enden, aber nicht mit stillem Weiterschieben.
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim.
