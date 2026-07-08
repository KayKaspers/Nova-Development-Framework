# Project Brain – WP-097 Foundation 0.7 Planning Notes

## Summary

Foundation 0.7 als Planungskandidat angelegt: Plan, Work-Package-Kandidaten (097–105), Criteria-Draft, NEXT_PHASE-Note. Arbeitstitel **v1.0 Path Consolidation & Compatibility Governance**. Kein Scope Lock (folgt in WP-098), kein Release, kein v1.0.

## Inputs reviewed

0.6-Abschluss sauber (released, keine falschen „tag pending"-Stellen); v1.0-Draft/Path-Summary (WP-086/088/089-Updates korrekt eingearbeitet); ADR-Policy (ADR-0031 als nächste Nummer bestätigt). Kein Statusfehler in 0.6-Dokumenten gefunden.

## Candidate matrix (Kurzform)

| Kandidat | v1.0-Relevanz | Risiko bei erneutem Verschieben | Vorschlag |
|---|---|---|---|
| Checklist DE/EN (WP-099) | tracked | hoch — viertes Mal offen | **release-blocking Entscheidungs-WP** (priorisieren/optional-mit-Begründung/streichen) |
| v1.x Compatibility Policy (WP-100) | **blocking-Kriterium `not met`** | hoch — letzte klare v1.0-Lücke | **release-blocking** (ADR-0031-Kandidat) |
| Convention Stability (WP-101) | `partially met` → `met` möglich | mittel | **release-blocking** (Kern-Konsolidierung) |
| Evidence Depth (WP-102) | `met with notes` → volles `met` | niedrig (PSV-001 non-blocking) | optional, hochstufbar durch WP-098 |
| Academy Entry (WP-103) | tracked, non-blocking | mittel | optional Entscheidungs-WP |
| Gate operational note QGM-003 | — | niedrig | Monitoring, kein WP |
| Doku/i18n-Konsolidierung | — | niedrig | optional/deferred |
| v0.6-Release-Body-Polish | — | keine | manuell/kosmetisch |

## Recommended core focus

Je ein Kern-Deliverable pro Titel-Hälfte: **Compatibility Governance → WP-100** (schließt das letzte klar `not met` v1.0-Kriterium), **v1.0 Path Consolidation → WP-101** (hebt Konventions-Stabilität Richtung `met`). Dazu die überfällige **WP-099**-Entscheidung. Bewährtes 0.4/0.5/0.6-Muster: kleiner blocking Kern.

## Suggested WP queue

097 (done) → 098 Scope Lock → 099 Checklist Decision ‖ 100 v1.x Policy ‖ 101 Stability Review → 102/103 optional → 104 Readiness → 105 Release Prep.

## Suggested release-blocking candidates

098, 099, 100, 101, 104, 105. **Final entscheidet WP-098.**

## Suggested optional candidates

102 (hochstufbar), 103, Doku/i18n-Konsolidierung.

## Risks

WP-091-Viertverschiebung (→ WP-099 als Entscheidungspflicht), v1.x-Policy als v1.0-Zusage lesbar (→ Draft-Markierung), Evidence-Depth personenabhängig (→ Ventil-Frage an WP-098), Scope Creep (→ kleiner Kern).

## What was not done

Kein Scope Lock, keine Einstufung final, keine Ventil-Formulierung, keine WP-Umsetzung, keine v1.0-/0.7-Release-Behauptung, keine Änderung an 0.6-Release-Dokumenten, keine GitHub-Schreibaktion (v0.6-Body-Polish nur als Kandidat notiert).

## Next step

**NDF-WP-098 – Foundation 0.7 Scope Lock.**
