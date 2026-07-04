# Foundation 0.3 Release Criteria

> Planungskriterien aus WP-044 — bewusst **nicht** abgehakt. Abschluss erfolgt in der Foundation-0.3 Release Readiness (geplant: NDF-WP-054). / Planning criteria; deliberately unchecked until the 0.3 release readiness review.

## Release-Typ / Release type

```text
Foundation Adoption Release (Pre-Release v0.3.0-foundation)
```

## Release-blocking Pflichtkriterien / Release-blocking criteria

Gemäß Scope Lock (`docs/roadmap/FOUNDATION_0_3_SCOPE_LOCK.md`): nur diese Kriterien blockieren den Release.

- [x] Foundation 0.2 released (Tag `v0.2.0-foundation`, 2026-07-03).
- [x] Foundation 0.3 Scope locked (NDF-WP-045, 2026-07-03).
- [x] Neutrales Beispielprojekt vorhanden als Adapter-Fixture (NDF-WP-046: `examples/neutral-example-project/`).
- [x] Project Adapter praktisch validiert: alle Phasen 0–10 am neutralen Beispielprojekt durchgespielt, Findings zurückgeführt (NDF-WP-047: **PASS WITH NOTES**, `docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md`).
- [x] Public Quality Gate v0.2 geprüft und grün (NDF-WP-052: new-file neutrality check aktiv, strict + self-test passed, E2E-Nachweis mit synthetischem Begriff).
- [ ] Release Readiness Review durchgeführt (NDF-WP-054, GO/GO WITH NOTES).
- [ ] Release Notes 0.3 vorbereitet (NDF-WP-055).
- [ ] Go/No-Go-Checkliste 0.3 vorbereitet und durchgegangen (NDF-WP-055).

## Optionale Kriterien / Optional criteria (should-have, nicht release-blockierend)

Unfertige optionale Punkte blockieren den Release nicht, müssen aber in Release Notes und Translation-Status-Matrix ehrlich dokumentiert sein.

- [ ] Zentrale Prompts DE/EN verbessert (Full Pass, NDF-WP-048).
- [ ] Zentrale Checklisten DE/EN verbessert (Full Pass, NDF-WP-049).
- [ ] Academy-Einstieg DE/EN verbessert (NDF-WP-050).
- [ ] ADR-Policy geklärt und dokumentiert (NDF-WP-051).
- [ ] Docs-Export-/Website-Konzept (NDF-WP-053 — deferred candidate, nur bei Restkapazität).

## Invarianten (müssen durchgehend gelten) / Invariants

- [ ] Public Quality Gate strict + self-test grün.
- [ ] Keine privaten Projekt-/Personenbezüge in getrackten Dateien (inkl. neuer Dateien vor dem Commit prüfen).
- [ ] Keine privaten Suchmuster in Prüf-/Release-Dokumentation.
- [ ] Foundation 0.1 und 0.2 bleiben frozen; Tags werden nicht verschoben.
- [ ] Keine v1.0-Behauptung.

## Go/No-Go

Finale Entscheidung nach Checkliste durch den Human Maintainer:

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```
