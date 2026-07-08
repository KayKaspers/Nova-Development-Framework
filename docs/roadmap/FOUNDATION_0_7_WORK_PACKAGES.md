# Foundation 0.7 – Work Package Candidates (Draft)

> Status: **Kandidatenplan aus NDF-WP-097 — kein Scope Lock.** Die Spalte „Empfehlung" ist vorläufig; verbindlich wird die Einstufung erst mit NDF-WP-098. / Candidate plan from NDF-WP-097 — not a scope lock; classification becomes binding only with NDF-WP-098.

## Vorgeschlagene Queue / Proposed Queue

| ID | Titel | Typ | Ziel | Abhängigkeiten | Empfehlung (vorläufig) | Herkunft / Origin |
|---|---|---|---|---|---|---|
| NDF-WP-097 | Foundation 0.7 Planning | docs-only / planning | Plan, WP-Kandidaten, Criteria-Draft, Brain-Notes | 0.6 released (WP-096) | **erledigt mit diesem Dokument** | — |
| NDF-WP-098 | Foundation 0.7 Scope Lock | docs-only / planning-gate | Umfang einfrieren, WP-102-Ventil-Frage, WP-099-Korridor, Änderungsregeln | WP-097 | **recommended release-blocking candidate** (Gate) | 0.5/0.6-Muster |
| NDF-WP-099 | Checklist DE/EN Decision | docs-only / decision | **Entscheiden:** priorisieren (release-blocking) / optional-mit-Begründung / streichen — kein viertes stilles Verschieben | WP-098 | **recommended release-blocking candidate** (Entscheidungspflicht) | WP-061/075/091, mehrfach offen |
| NDF-WP-100 | v1.x Compatibility Policy Decision / ADR-0031 Preparation | docs-only / adr-policy | v1.x-Kompatibilitätszusage entwerfen (was verspricht v1.x: Struktur? Prompts? Konventionen?) — Draft, ggf. als ADR-0031 | WP-098 | **recommended release-blocking candidate** (Kern: Compatibility Governance) | WP-079/093, offenes v1.0-Kriterium |
| NDF-WP-101 | Project Adapter Convention Stability Review | review-only / docs-only | Bestätigen, dass Adapter-Konventionen (Manifest, Output-Pfade, Health-Score) über 0.4→0.6 stabil/additiv sind; v1.0-Kriterium Richtung `met` | WP-098 | **recommended release-blocking candidate** (Kern: v1.0 Path Consolidation) | v1.0-Draft `partially met` |
| NDF-WP-102 | External Validation Evidence Depth Pass | review-only | Detaillierterer öffentlicher Lauf mit ausgefülltem Feedback-Template; adressiert PSV-001 → Richtung volles PASS / `met` | WP-098 | **optional candidate** — von WP-098 auf blocking hochstufbar; ggf. mit Ventil (personenabhängig) | WP-088-Note PSV-001 |
| NDF-WP-103 | Academy Entry Decision | docs-only / i18n | **Entscheiden:** Academy-Einstieg priorisieren oder bewusst deferred; nicht still liegen lassen | WP-098 | **optional candidate** | WP-062/077/092, mehrfach offen |
| NDF-WP-104 | Foundation 0.7 Release Readiness Review | review-only | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.7-Kriterien | blocking WPs done | **recommended release-blocking candidate** | Release-Muster |
| NDF-WP-105 | Foundation 0.7 Release Prep | docs-only / release-prep | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide (voraussichtlich `v0.7.0-foundation`) | WP-104 | **recommended release-blocking candidate** | Release-Muster |

## Recommended optional candidates

- NDF-WP-102 External Validation Evidence Depth Pass (falls WP-098 es nicht auf blocking hochstuft)
- NDF-WP-103 Academy Entry Decision
- Doku-/i18n-Konsolidierung (klein) / small documentation / i18n consolidation

## Recommended deferred / non-goal candidates

- Vollständige Doku-Website / full documentation website
- Vollständige i18n-Abdeckung / full i18n completion
- ADR-Massenmigration / ADR mass migration
- v1.0 Release Candidate (nur späterer eigener v1.0-Zyklus)
- Großer Framework-Rewrite; neue Applikations-Features

## Manual / cosmetic (kein WP / no work package)

- Optionaler v0.6-GitHub-Release-Body-Polish: Der Body enthält die Pflichtaussage „This is not a v1.0 release.", ist aber minimal. Der Human Maintainer kann ihn optional per Release-Edit aus den Release Notes erweitern — **keine GitHub-Schreibaktion in NDF-WPs**, non-blocking.

## Regeln / Rules

- **Kandidatenplan** — finale Einstufung (release-blocking / optional / deferred) trifft ausschließlich NDF-WP-098.
- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock.
- Empfohlener kleiner blocking Kern: Gates (098/104/105) + je ein Deliverable pro Titel-Hälfte (Compatibility Governance → 100, v1.0 Path Consolidation → 101) + die überfällige Checklist-Entscheidung (099).
- **WP-099 und WP-103 sind Entscheidungs-WPs** — sie dürfen mit „streichen"/„bewusst deferred mit Begründung" enden, aber nicht mit stillem Weiterschieben.
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv; kein v1.0-Claim.
