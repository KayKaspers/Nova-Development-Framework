# Foundation 0.6 Release Criteria

## DE – Status

**Scope locked (NDF-WP-085, 2026-07-07).** Foundation 0.6 ist gelockt, nicht released, nicht v1.0. Die Blocking-Kriterien sind verbindlich gemäß [FOUNDATION_0_6_SCOPE_LOCK.md](../roadmap/FOUNDATION_0_6_SCOPE_LOCK.md); abgehakt wird erst gegen tatsächliche Ergebnisse — keine falschen Haken.

## EN – Status

**Scope locked (NDF-WP-085, 2026-07-07).** Foundation 0.6 is locked, not released, not v1.0. The blocking criteria are binding per the scope lock; boxes are only checked against actual results — no false checkmarks.

## DE – Release-Ziel

```text
Foundation Adoption Confidence & Governance Hardening Release
(voraussichtlich Pre-Release v0.6.0-foundation — noch nicht released)
```

## EN – Release Target

Foundation pre-release, presumably `v0.6.0-foundation` — not released. Tagging guide and release prep follow later (WP-095), not in this draft.

## DE – Kriterien / EN – Criteria

Grundsatz: Kriterien müssen prüfbar sein (Nachweis benennbar); ehrliche Statuswerte wie im v1.0-Draft. Die folgenden Listen sind seit NDF-WP-085 **verbindlich**.

## DE – Release-blocking Kriterien (verbindlich seit WP-085)

- [x] Foundation 0.5 released und abgeschlossen (`v0.5.0-foundation`, 2026-07-07; WP-083).
- [x] Foundation 0.6 Scope locked (NDF-WP-085, 2026-07-07: [`FOUNDATION_0_6_SCOPE_LOCK.md`](../roadmap/FOUNDATION_0_6_SCOPE_LOCK.md)).
- [x] **ADR-Policy explizit entschieden** (NDF-WP-086, 2026-07-07: **Minimal ADR Policy adopted** — [`docs/adr/ADR_POLICY.md`](../adr/ADR_POLICY.md); Massenmigration bleibt deferred).
- [x] **Public SampleProject Runbook Validation ehrlich bewertet** (NDF-WP-088, 2026-07-07: **PASS WITH NOTES** — unabhängig positiv bestätigt, keine Blocker/High-Findings; Schrittbelege nicht vollständig, [`independent-runs/2026-07-07-public-sampleproject-runbook-validation/`](../validation/project-adapter/independent-runs/2026-07-07-public-sampleproject-runbook-validation/README.md); Ventil **nicht benötigt**; WP-087 **skipped/not needed** — Lauf direkt mit den WP-073-Unterlagen).
- [x] **Quality Gate Maintenance geprüft** (NDF-WP-089, 2026-07-07: Gate grün, CI-Denylist-Wirksamkeit **Evidence-Level strong** — [`PUBLIC_QUALITY_GATE_MAINTENANCE_REVIEW.md`](../quality/PUBLIC_QUALITY_GATE_MAINTENANCE_REVIEW.md); **WP-090 not needed** — der Nachweis wurde ausreichend in WP-089 erbracht).
- [x] Release Readiness Review durchgeführt (NDF-WP-094, 2026-07-07: **GO WITH NOTES**, keine Blocker — [`FOUNDATION_0_6_RELEASE_READINESS_REVIEW.md`](FOUNDATION_0_6_RELEASE_READINESS_REVIEW.md)).
- [x] Release Notes vorbereitet (NDF-WP-095: [`FOUNDATION_0_6_RELEASE_NOTES.md`](FOUNDATION_0_6_RELEASE_NOTES.md), inkl. PSV-001, QGM-003 und aller Known Limitations aus WP-094).
- [x] Go/No-Go-Checkliste vorbereitet (NDF-WP-095: [`FOUNDATION_0_6_GO_NO_GO_CHECKLIST.md`](FOUNDATION_0_6_GO_NO_GO_CHECKLIST.md), 22 Punkte) — Durchgang durch den Human Maintainer offen.
- [x] Tagging-/GitHub-Release-Guide vorbereitet (NDF-WP-095: [`FOUNDATION_0_6_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`](FOUNDATION_0_6_TAGGING_AND_GITHUB_RELEASE_GUIDE.md)).
- [ ] Finaler Tag `v0.6.0-foundation` + GitHub Pre-Release (nur Human Maintainer, offen).
- [ ] Keine privaten Projekt-/Personen-/Secret-Leaks; kein v1.0-Claim (Invarianten unten, durchgehend).

## EN – Release-blocking Criteria (binding since WP-085)

0.5 released and complete (done); scope locked (done, NDF-WP-085); **ADR policy explicitly decided** (minimal policy adopted **or** honest documented drop — no further carry-over); **public SampleProject runbook validation honestly assessed** (performed and evaluated, or transparently downgraded per the strict 8-condition valve via WP-094); **gate maintenance reviewed** including the CI denylist effectiveness assessment; readiness review done; release prep artifacts prepared; final tag + GitHub pre-release by the human maintainer only; no private project/person/secret leakage and no v1.0 claim throughout.

## DE – Nicht-Blocker (verbindlich optional)

- [ ] Validation Preparation Nachschärfung (NDF-WP-087 — nur falls nötig).
- [ ] CI Denylist Effectiveness Proof als eigenes WP (NDF-WP-090 — entfällt, wenn WP-089 den Nachweis mit erbringt).
- [ ] Checklist Library DE/EN Priority Pass (NDF-WP-091).
- [ ] Academy Band 1 Entry Pass (NDF-WP-092).
- [ ] v1.x Compatibility Policy Draft (NDF-WP-093 — v1.0-tracked, aber kein 0.6-Blocker-Vorschlag).
- Deferred: Doku-Website, volle i18n-Abdeckung, ADR-Massenmigration, v1.0 Release Candidate.

## EN – Non-Blockers (binding optional)

WP-087 (if needed — skipped if WP-088 starts with the WP-073 materials), WP-090 (merged into WP-089 unless WP-089 explicitly finds a separate proof artifact necessary), WP-091 checklist DE/EN, WP-092 academy entry, WP-093 v1.x compatibility policy draft (v1.0-tracked, not a 0.6 blocker); deferred: documentation website, full i18n, ADR mass migration, v1.0 release candidate, large rewrite.

## DE – Invarianten (müssen durchgehend gelten)

- [ ] Public Quality Gate strict + self-test grün (new-file neutrality check aktiv).
- [ ] Keine privaten Projekt-/Personennamen, keine Reviewer-Identitäten, keine Kontaktwege, keine echten Domains in getrackten oder neuen Dateien.
- [ ] Keine Secret-Werte (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden).
- [ ] **Kein v1.0-Claim** — auch nicht implizit über den v1.x-Policy-Draft.
- [ ] Foundation 0.1–0.5 bleiben frozen; Tags werden nie verschoben.
- [ ] Der Human Maintainer behält die Release-Kontrolle; der Implementation Agent taggt und released nicht.

## EN – Invariants

Gate green throughout; no private names/identities/contacts/domains; no secret values; **no v1.0 claim** (not even implicitly via the v1.x policy draft); Foundation 0.1–0.5 stay frozen, tags never moved; the human maintainer keeps release control — the Implementation Agent never tags or releases.

## DE – Go/No-Go

Finale Entscheidung nach Checkliste durch den Human Maintainer (Checkliste entsteht erst in NDF-WP-095):

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```

## EN – Go/No-Go

Final decision by the human maintainer after the checklist (created only in NDF-WP-095); fields above.
