# Next Phase – Foundation 0.6

## Status

**Scope locked** (NDF-WP-085, 2026-07-07) — verbindlich: `docs/roadmap/FOUNDATION_0_6_SCOPE_LOCK.md`. Release-blocking: 085 (done) · **086 ADR Decision** · **088 Public Validation Run** (8-Bedingungen-Ventil über WP-094) · **089 Gate Maintenance** (inkl. CI-Denylist-Bewertung; WP-090 merged) · 094 · 095. Optional: 087 (falls nötig), 091–093. **Nächster Schritt: NDF-WP-086 – ADR Policy Decision** (annehmen oder ehrlich streichen — „später" unzulässig). Kein Release, kein v1.0.

## Current baseline

Foundation 0.5 released as `v0.5.0-foundation` (2026-07-07, GitHub Pre-Release); vollständig abgeschlossen, keine offenen 0.5-Follow-ups.

## Theme

**Adoption Confidence & Governance Hardening** — die in 0.5 sichtbar gemachten offenen Punkte kontrolliert abarbeiten oder bewusst entscheiden.

## Candidate priorities

1. **WP-086 ADR Policy Decision** (Blocking-Empfehlung — 0.5-Sonderregel: entscheiden oder ehrlich streichen, kein drittes stilles Verschieben)
2. **WP-088 Public SampleProject Runbook Validation Run** (Blocking-Empfehlung mit Ventil-Prüfung durch WP-085 — hebt v1.0-External-Validation Richtung `met`; WP-087 Preparation nur falls nötig)
3. **WP-089 Quality Gate Maintenance Review** (Blocking-Empfehlung, leichtgewichtig; WP-090 CI-Denylist-Proof entfällt, wenn 089 ihn mit erbringt)
4. WP-093 v1.x Compatibility Policy Draft (optional, v1.0-tracked — schließt die bewusste Lücke aus dem v1.0-Draft)
5. WP-091 Checklist DE/EN, WP-092 Academy Entry (optional)

## Next recommended WP

**NDF-WP-085 – Foundation 0.6 Scope Lock** — verbindliche Einstufung, Ventil-Frage für WP-088, Änderungsregeln. Kein inhaltliches WP vorher.

## Non-goals

Kein v1.0/Release Candidate; kein Rewrite; keine Website/Export-Pipeline/CLI; keine volle i18n-Abdeckung; keine ADR-Massenmigration (nur Entscheidung); keine realen privaten Projekte.

## Notes for Nova

- WP-085 muss zwei Dinge klären: (a) exakte Ventil-Formulierung für WP-088 (Empfehlung: 8-Bedingungen-Muster aus dem 0.5 Scope Lock übernehmen), (b) ob WP-090 als eigenes WP nötig ist oder in WP-089 aufgeht.
- Die WP-086-Entscheidung darf „streichen" lauten, aber nicht „später" — das ist die verbindliche 0.5-Regel.
- Details: `docs/roadmap/FOUNDATION_0_6_PLAN.md`, `docs/roadmap/FOUNDATION_0_6_WORK_PACKAGES.md`, `docs/release/FOUNDATION_0_6_RELEASE_CRITERIA.md`
