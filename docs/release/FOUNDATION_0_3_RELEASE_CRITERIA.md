# Foundation 0.3 Release Criteria

> Planungskriterien aus WP-044 — bewusst **nicht** abgehakt. Abschluss erfolgt in der Foundation-0.3 Release Readiness (geplant: NDF-WP-054). / Planning criteria; deliberately unchecked until the 0.3 release readiness review.

## Release-Typ / Release type

```text
Foundation Adoption Release (Pre-Release v0.3.0-foundation)
```

## Pflichtkriterien / Required criteria

- [x] Foundation 0.2 released (Tag `v0.2.0-foundation`, 2026-07-03).
- [ ] Foundation 0.3 Scope locked (NDF-WP-045).
- [ ] Project Adapter praktisch validiert: alle Phasen 0–10 am neutralen Beispielprojekt durchgespielt, Findings zurückgeführt (NDF-WP-047).
- [ ] Neutrales Beispielprojekt vorhanden/aktualisiert als Adapter-Zielprojekt (NDF-WP-046).
- [ ] Public Quality Gate v0.2 geprüft und grün (NDF-WP-052).
- [ ] Zentrale Prompts DE/EN verbessert (Full Pass, NDF-WP-048) oder Rest bewusst dokumentiert.
- [ ] Zentrale Checklisten DE/EN verbessert (Full Pass, NDF-WP-049) oder Rest bewusst dokumentiert.
- [ ] Academy-Einstieg DE/EN verbessert (NDF-WP-050).
- [ ] ADR-Policy geklärt und dokumentiert (NDF-WP-051).
- [ ] Release Readiness Review durchgeführt (NDF-WP-054).
- [ ] Release Notes 0.3 vorbereitet (NDF-WP-055).
- [ ] Go/No-Go-Checkliste 0.3 vorbereitet und durchgegangen (NDF-WP-055).

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
