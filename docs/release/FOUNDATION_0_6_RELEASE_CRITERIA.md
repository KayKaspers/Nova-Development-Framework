# Foundation 0.6 Release Criteria

## DE – Status

**Draft aus NDF-WP-084 — not scope-locked.** Foundation 0.6 ist in Planung, nicht released, nicht v1.0. Alle Blocking-Kriterien sind Vorschläge, bis der Scope Lock (NDF-WP-085) sie verbindlich macht. Abgehakt wird erst gegen tatsächliche Ergebnisse — keine falschen Haken.

## EN – Status

**Draft from NDF-WP-084 — not scope-locked.** Foundation 0.6 is in planning, not released, not v1.0. All blocking criteria are proposals until the scope lock (NDF-WP-085) makes them binding. Boxes are only checked against actual results — no false checkmarks.

## DE – Release-Ziel

```text
Foundation Adoption Confidence & Governance Hardening Release
(voraussichtlich Pre-Release v0.6.0-foundation — noch nicht released)
```

## EN – Release Target

Foundation pre-release, presumably `v0.6.0-foundation` — not released. Tagging guide and release prep follow later (WP-095), not in this draft.

## DE – Draft-Kriterien / EN – Draft Criteria

Grundsatz: Kriterien müssen prüfbar sein (Nachweis benennbar); ehrliche Statuswerte wie im v1.0-Draft. Die folgenden zwei Listen sind **Vorschläge** für WP-085.

## DE – Vorgeschlagene Blocking-Kriterien

- [ ] Foundation 0.5 released und abgeschlossen (bereits erfüllt — wird beim Scope Lock abgehakt).
- [ ] Foundation 0.6 Scope locked (NDF-WP-085).
- [ ] **ADR-Policy explizit entschieden** (NDF-WP-086): dokumentierte Entscheidung — priorisierte Policy **oder** ehrliches Streichen mit Begründung; kein weiteres Verschieben.
- [ ] **Public SampleProject Runbook Validation ehrlich bewertet** (NDF-WP-088): durchgeführt und ausgewertet — oder gemäß einem von WP-085 definierten Ventil transparent herabgestuft.
- [ ] **Quality Gate Maintenance geprüft** (NDF-WP-089): Gate weiterhin grün, Doku aktuell, CI-Denylist-Wirksamkeit nachgewiesen oder als eigener Punkt (WP-090) erledigt.
- [ ] Release Readiness Review durchgeführt (NDF-WP-094).
- [ ] Release Notes, Go/No-Go-Checkliste und Tagging-Guide vorbereitet (NDF-WP-095).
- [ ] Finaler Tag + GitHub Pre-Release (nur Human Maintainer).

## EN – Proposed Blocking Criteria

0.5 released (done, checked at scope lock); scope locked; **ADR policy explicitly decided** (prioritized policy **or** honest documented drop — no further carry-over); **public SampleProject runbook validation honestly assessed** (performed and evaluated, or transparently downgraded per a WP-085-defined valve); **gate maintenance reviewed** including CI denylist effectiveness; readiness review; release prep artifacts; final tag + GitHub pre-release by the human maintainer only.

## DE – Vorgeschlagene Nicht-Blocker

- [ ] Validation Preparation Nachschärfung (NDF-WP-087 — nur falls nötig).
- [ ] CI Denylist Effectiveness Proof als eigenes WP (NDF-WP-090 — entfällt, wenn WP-089 den Nachweis mit erbringt).
- [ ] Checklist Library DE/EN Priority Pass (NDF-WP-091).
- [ ] Academy Band 1 Entry Pass (NDF-WP-092).
- [ ] v1.x Compatibility Policy Draft (NDF-WP-093 — v1.0-tracked, aber kein 0.6-Blocker-Vorschlag).
- Deferred: Doku-Website, volle i18n-Abdeckung, ADR-Massenmigration, v1.0 Release Candidate.

## EN – Proposed Non-Blockers

WP-087 (if needed), WP-090 (dropped if covered by WP-089), WP-091 checklist DE/EN, WP-092 academy entry, WP-093 v1.x compatibility policy draft (v1.0-tracked, not proposed as a 0.6 blocker); deferred: documentation website, full i18n, ADR mass migration, v1.0 release candidate.

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
