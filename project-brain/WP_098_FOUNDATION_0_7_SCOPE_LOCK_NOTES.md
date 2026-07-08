# Project Brain – WP-098 Foundation 0.7 Scope Lock Notes

## Summary

Foundation-0.7-Scope verbindlich eingefroren (Arbeitstitel v1.0 Path Consolidation & Compatibility Governance). Nova-Empfehlung kritisch geprüft und unverändert übernommen — deckt sich mit der WP-097-Empfehlung; kleiner blocking Kern nach 0.4/0.5/0.6-Muster. Kein Release, kein v1.0.

## Inputs reviewed

0.7-Planung (Plan, Queue, Criteria, NEXT_PHASE, WP-097-Note) — nur planning, keine verfrühten Haken, alle Kandidaten übernommen. 0.6-Follow-ups (Release Notes/Criteria/Readiness/Cleanup) — 0.6 bleibt korrekt published, keine `tag pending`-Reste. v1.0-Draft/Path/ADR-Policy — v1.x-Kompatibilitätszusage weiter klar `not met`, ADR-0031 als nächste Nummer bestätigt, noch nicht erstellt.

## Final scope

- **Release-blocking:** 098 (Gate, done), 099 (Checklist Decision), 100 (v1.x Policy / ADR-0031), 101 (Convention Stability), 104 (Readiness), 105 (Release Prep).
- **Optional:** 102 (Evidence Depth, mit Upgrade-Ventil), 103 (Academy Entry Decision), Doku-/i18n-Konsolidierung.
- **Deferred/Nicht-Ziel:** Website, volle i18n, v1.0-RC, Rewrite, App-Features, ADR-Massenmigration, volle externe Zertifizierung.
- **Manuell/kosmetisch (kein WP):** v0.6-Release-Body-Polish (keine GitHub-Schreibaktion).

## WP-099 decision corridor

Verbindlich: **A) priorisieren** (release-blocking; Folge-WP für die Arbeit möglich) / **B) optional mit expliziter finaler Begründung** / **C) streichen mit Begründung**. Stilles Verschieben, viertes Weiterschleppen, unklares „später" ausdrücklich verboten. Die seit 0.4 offene Frage wird in 0.7 entschieden.

## WP-100 ADR-0031 decision path

WP-100 entscheidet ADR-0031 vs. reines Policy-Dokument mit ADR-Verweis; **ADR-0031 ist der bevorzugte Pfad** (dauerhafte Governance-Wirkung), begründete Abweichung erlaubt. Keine v1.0-Kompatibilitätszusage überhöhen — Draft, kein Versprechen. ADR-0031-Datei wird erst in WP-100 erstellt.

## WP-102 optional status and upgrade valve

Bleibt optional/non-blocking (WP-088 hat External Validation bereits auf `met with notes` gehoben; PSV-001 v1.0-tracked). Upgrade nur per ausdrücklichem Human-Maintainer-Scope-Change und nur bei (a) früh verfügbarem detailliertem Independent Validator und (b) ohne Gefährdung des Kern-Scopes.

## Change control

Kein neues blocking WP ohne Scope-Change-Vermerk; keine stille Erweiterung; kein Feature Creep; kein v1.0-Claim; keine Release Prep vor WP-104; kein Agent-Tagging; kein stilles WP-099-Verschieben. Redaktionelle Fixes = keine Scope-Änderung.

## Risks

WP-091-Viertverschiebung (→ WP-099-Entscheidungspflicht), v1.x-Policy als v1.0-Zusage lesbar (→ Draft-Markierung + Überhöhungsverbot), Evidence-Depth personenabhängig (→ optional mit Ventil), Scope Creep (→ kleiner Kern + Change Control). Ein-Personen-Engpass unverändert.

## Next step

**NDF-WP-099 – Checklist DE/EN Decision** (parallel: WP-100, WP-101).
