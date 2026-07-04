# Foundation 0.4 Release Criteria

> Planungskriterien aus WP-057 — bewusst **nicht** abgehakt (außer objektiv bereits Erfülltem). Abschluss erfolgt in der Foundation-0.4 Release Readiness (geplant: NDF-WP-067). / Planning criteria; deliberately unchecked until the 0.4 release readiness review.

## Release-Typ / Release type

```text
Foundation Adoption Hardening Release (Pre-Release v0.4.0-foundation)
```

## Release-blocking Pflichtkriterien / Release-blocking criteria

Gemäß Scope Lock (`docs/roadmap/FOUNDATION_0_4_SCOPE_LOCK.md`): nur diese Kriterien blockieren den Release.

- [x] Foundation 0.3 released (Tag `v0.3.0-foundation`, 2026-07-04).
- [x] Foundation 0.4 Scope locked (NDF-WP-058, 2026-07-04).
- [x] Adapter Conventions Polish umgesetzt (NDF-WP-059: `PROJECT_ADAPTER_CONVENTIONS.md`, Manifest-/Output-/Health-Score-Konvention, Templates/Checkliste, Präfix + First-Safe-WP-Template).
- [ ] Prompt Library DE/EN Priority Pass umgesetzt (NDF-WP-060) oder über WP-067 dokumentiert herabgestuft.
- [ ] Public Quality Gate v0.2 weiterhin grün (strict + self-test), new-file neutrality check aktiv.
- [ ] Release Readiness Review durchgeführt (NDF-WP-067, GO/GO WITH NOTES).
- [ ] Release Notes 0.4 vorbereitet (NDF-WP-068).
- [ ] Go/No-Go-Checkliste 0.4 vorbereitet und durchgegangen (NDF-WP-068).

## Optionale Kriterien / Optional criteria (should-have, nicht release-blockierend)

Unfertige optionale Punkte blockieren den Release nicht, müssen aber in Release Notes und Translation-Status-Matrix ehrlich dokumentiert sein.

- [ ] Checklist Library DE/EN Priority Pass (NDF-WP-061).
- [ ] Academy Band 1 Entry Pass (NDF-WP-062).
- [ ] ADR Policy & Structure Consolidation Plan (NDF-WP-063).
- [ ] Public Quality Gate Maintenance Review (NDF-WP-066).
## Deferred (blockieren den Release nicht) / Deferred (do not block the release)

- [ ] Independent Adapter Validation Run (NDF-WP-064 — deferred candidate, nur wenn Unbeteiligte verfügbar).
- [ ] Docs Export / Website Readiness Concept (NDF-WP-065 — deferred candidate, nur bei Restkapazität).

## Invarianten (müssen durchgehend gelten) / Invariants

- [ ] Public Quality Gate strict + self-test grün.
- [ ] Keine privaten Projekt-/Personenbezüge in getrackten oder neuen Dateien (new-file neutrality check).
- [ ] Keine privaten Suchmuster in Prüf-/Release-Dokumentation.
- [ ] Foundation 0.1, 0.2 und 0.3 bleiben frozen; Tags werden nicht verschoben.
- [ ] Keine v1.0-Behauptung.

## Go/No-Go

Finale Entscheidung nach Checkliste durch den Human Maintainer:

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```
