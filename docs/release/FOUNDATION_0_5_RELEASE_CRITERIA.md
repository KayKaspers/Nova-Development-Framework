# Foundation 0.5 Release Criteria

## DE – Status

**Scope locked (NDF-WP-072, 2026-07-06).** Foundation 0.5 ist gelockt, nicht released. Die release-blocking Kriterien sind verbindlich gemäß [FOUNDATION_0_5_SCOPE_LOCK.md](../roadmap/FOUNDATION_0_5_SCOPE_LOCK.md); abgehakt wird erst gegen tatsächliche Ergebnisse.

## EN – Status

**Scope locked (NDF-WP-072, 2026-07-06).** Foundation 0.5 is locked, not released. The release-blocking criteria are binding per the scope lock; boxes are only checked against actual results.

## DE – Release-Ziel

```text
Foundation External Validation & 1.0 Path Hardening Release (Pre-Release v0.5.0-foundation)
```

## EN – Release Goal

Foundation pre-release `v0.5.0-foundation` — external validation & 1.0 path hardening. Not v1.0.

## DE – Release-blocking Kriterien (verbindlich seit WP-072)

- [x] Foundation 0.4 released und Follow-ups geschlossen (`v0.4.0-foundation`, 2026-07-04; WP-070).
- [x] Foundation 0.5 Scope locked (NDF-WP-072, 2026-07-06: `FOUNDATION_0_5_SCOPE_LOCK.md`).
- [x] Independent Adapter Validation Preparation abgeschlossen (NDF-WP-073: Preparation-Dokument, Runbook, Validator Brief, Feedback- und Outreach-Template unter `docs/validation/project-adapter/`; Ergebnisort `independent-runs/` definiert).
- [ ] Independent Adapter Validation Run durchgeführt und Findings dokumentiert (NDF-WP-074) — **oder** Downgrade-Ventil über WP-081 gezogen gemäß den 8 Bedingungen im Scope Lock (inkl. dokumentiertem Anfrage-Versuch, Known-Limitation-Eintrag und Maintainer-Bestätigung).
- [x] v1.0 Readiness Criteria Draft erstellt (NDF-WP-079: [`V1_0_READINESS_CRITERIA_DRAFT.md`](V1_0_READINESS_CRITERIA_DRAFT.md) + [`V1_0_PATH_SUMMARY.md`](../roadmap/V1_0_PATH_SUMMARY.md)) — als Entwurf markiert, ohne v1.0-Claim. Erfüllt den 0.5-Beitrag zu „1.0 Path Hardening"; bedeutet **nicht** v1.0-Readiness — v1.0 braucht später einen eigenen Zyklus.
- [ ] Public Quality Gate weiterhin grün (strict + self-test), new-file neutrality check aktiv.
- [ ] Release Readiness Review durchgeführt (NDF-WP-081).
- [ ] Release Notes, Go/No-Go-Checkliste und Tagging-Guide vorbereitet (NDF-WP-082).
- [ ] Finaler Tag `v0.5.0-foundation` + GitHub Pre-Release (nur Human Maintainer).

## EN – Release-blocking Criteria (binding since WP-072)

0.4 released + follow-ups closed (done); scope locked (done, NDF-WP-072); validation preparation done; validation run done and findings documented — or the downgrade valve pulled via WP-081 per the 8 scope lock conditions (incl. documented outreach attempt, known-limitation entry, maintainer confirmation); v1.0 criteria draft created (marked as draft, no v1.0 claim); public quality gate green; readiness review done; release prep artifacts prepared; final tag + GitHub pre-release by the human maintainer only.

## DE – Optionale Kriterien (should-have, nicht release-blockierend)

Unfertige optionale Punkte blockieren den Release nicht, müssen aber in Release Notes und Translation-Status-Matrix ehrlich dokumentiert sein.

- [ ] Checklist Library DE/EN Priority Pass (NDF-WP-075).
- [ ] ADR Policy & Structure Consolidation Plan (NDF-WP-076).
- [ ] Academy Band 1 Entry Pass (NDF-WP-077).
- [ ] Public Quality Gate Maintenance Review (NDF-WP-078).

## EN – Optional Criteria

WP-075/076/077/078 — should-have; unfinished items documented honestly in release notes and the translation status matrix, never blocking.

## DE – Deferred Kriterien (blockieren den Release nicht)

- [ ] Docs Export / Website Readiness Concept (NDF-WP-080 — deferred candidate, nur bei Restkapazität).

## EN – Deferred Criteria

WP-080 (deferred candidate, spare capacity only) — does not block the release.

## DE – Invarianten (müssen durchgehend gelten)

- [ ] Public Quality Gate strict + self-test grün.
- [ ] Keine privaten Projekt-/Personenbezüge in getrackten oder neuen Dateien (new-file neutrality check).
- [ ] Keine privaten Suchmuster und keine Secret-Werte in Prüf-/Release-Dokumentation (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden).
- [ ] Foundation 0.1–0.4 bleiben frozen; Tags werden nicht verschoben.
- [ ] Keine v1.0-Behauptung — auch nicht implizit über den Criteria Draft.
- [ ] Der Human Maintainer bleibt final zuständig; Release-Readiness und Release-Prep bleiben eigene Gates.

## EN – Invariants

Gate green throughout; no private references or search patterns in tracked or new files; no secret values documented (naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed); Foundation 0.1–0.4 stay frozen, tags are never moved; no v1.0 claim — not even implicitly via the criteria draft; the human maintainer stays finally responsible, readiness and release prep remain separate gates.

## DE – Go/No-Go Felder

Finale Entscheidung nach Checkliste durch den Human Maintainer (Checkliste entsteht in NDF-WP-082):

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```

## EN – Go/No-Go Fields

Final decision by the human maintainer after the checklist (created in NDF-WP-082); fields above.

## DE – Nicht-Ziele

Kein v1.0-Release; keine Website/Export-Pipeline/CLI (höchstens Konzept); kein DE/EN-Massenprojekt; keine ADR-Massenmigration; kein History-Rewrite; keine privaten Projektbeispiele; keine Release-Automation.

## EN – Non-Goals

No v1.0 release; no website, export pipeline, or CLI (concept at most); no blanket DE/EN project; no bulk ADR migration; no history rewrite; no private project examples; no release automation.
