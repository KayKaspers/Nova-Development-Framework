# Foundation 0.9 Release Criteria (Draft)

## DE – Status

**Scope locked (NDF-WP-121, 2026-07-08).** Foundation 0.9 ist gelockt, **nicht released**, **nicht v1.0**. Verbindliche Einstufung: [FOUNDATION_0_9_SCOPE_LOCK.md](../roadmap/FOUNDATION_0_9_SCOPE_LOCK.md). Boxen werden nur gegen tatsächliche Ergebnisse abgehakt — keine falschen Haken.

## EN – Status

**Scope locked (NDF-WP-121, 2026-07-08).** Foundation 0.9 is locked, **not released**, **not v1.0**. Binding classification: the scope lock. Boxes are checked only against actual results — no false checkmarks.

## DE – Arbeitstitel

```text
Foundation 0.9 – Adoption, Validation & Optional Enablement
(voraussichtlich Pre-Release v0.9.0-foundation — scope-locked, nicht released, nicht v1.0)
```

## EN – Working Title

Foundation pre-release, presumably `v0.9.0-foundation` — planned only, not scope-locked, not released. Validate adoption and decide optional enablement without claiming v1.0.

## DE – Release-blocking Kriterien (verbindlich seit WP-121)

- [x] Foundation 0.8 released und abgeschlossen (`v0.8.0-foundation`, 2026-07-08; WP-119).
- [x] Foundation 0.9 Planning erstellt (NDF-WP-120).
- [x] Foundation 0.9 Scope Lock abgeschlossen (NDF-WP-121, 2026-07-08: [`FOUNDATION_0_9_SCOPE_LOCK.md`](../roadmap/FOUNDATION_0_9_SCOPE_LOCK.md); validation-first, WP-124 blocking-Entscheidung, WP-125 optional/conditional, WP-129 optional/nicht aktiviert).
- [ ] Context Economy Adoption Review abgeschlossen (NDF-WP-122).
- [ ] Prompt Modes and Context Pack Validation abgeschlossen (NDF-WP-123).
- [ ] Optional Skills MVP Implementation Decision abgeschlossen (NDF-WP-124) — nur Entscheidung.
- [ ] Adoption Evidence and v1.0 Path Review abgeschlossen (NDF-WP-126).
- [ ] Kein aktives Skill Pack ohne ausdrücklichen Scope + ADR-0032-Konformität.
- [ ] Keine autonome Git-/Release-/Tag-Aktion durch Skills.
- [ ] Public Quality Gate strict grün.
- [ ] Public Quality Gate self-test grün.
- [ ] Public Neutrality sauber.
- [ ] Release Readiness Review abgeschlossen (NDF-WP-127).
- [ ] Release Prep abgeschlossen (NDF-WP-128).
- [ ] Finaler Tag + GitHub Pre-Release (nur Human Maintainer).

## EN – Release-Blocking Criteria (binding since WP-121)

0.8 released (done); 0.9 planning done; scope lock done (validation-first; WP-124 blocking decision, WP-125 optional/conditional, WP-129 optional/not activated); context economy adoption review; prompt modes and context pack validation; optional skills MVP implementation decision (decision only); adoption evidence and v1.0 path review; no active skill pack without explicit scope + ADR-0032 compliance; no autonomous git/release/tag action by skills; public quality gate strict + self-test green; public neutrality clean; readiness review; release prep; final tag + GitHub pre-release by the human maintainer only.

## DE – Optionale / bedingte Kandidaten

- [ ] Skills MVP Implementation Blueprint (NDF-WP-125) — **optional / conditional**, nur wenn WP-124 eine spätere Implementierung empfiehlt.
- [ ] Docs-only Skills MVP Implementation (NDF-WP-129) — **optional, nicht aktiviert**; nur per Human-Maintainer-Scope-Change, strikt ADR-0032-konform.
- [ ] Skill-to-Cursor Rules Export Assessment (NDF-WP-130) / Workflow Builder Evaluation (NDF-WP-131) / Docs Polish Skill Evaluation (NDF-WP-132) — optionale Assessments.
- [ ] Foundation 0.9 Post-Release Status Cleanup (NDF-WP-133) — Post-Release-Kandidat.

## EN – Optional / Conditional Candidates

WP-125 blueprint (optional/conditional on WP-124), WP-129 docs-only implementation (optional, not activated — only via human-maintainer scope change, ADR-0032-compliant), WP-130/131/132 assessments/evaluations, WP-133 post-release candidate — none blocks.

## DE – Sicherheits- und Neutralitätsinvarianten

Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflicht. ADR-0032 (Skill Security Policy) bleibt bindend: fail closed, docs-only zuerst, keine Scripts/Netz/Secrets/privaten Daten/autonomen Git-Release-Aktionen. Keine privaten Namen/Reviewer/Kontakte/Domains; der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden, der Wert nie.

## EN – Security and Neutrality Invariants

Public quality gate v0.2 stays mandatory. ADR-0032 stays binding: fail closed, docs-only first, no scripts/network/secrets/private data/autonomous git-release actions. No private names/reviewer/contacts/domains; naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed, its value never.

## DE – v1.0-Abgrenzung

Foundation 0.9 **stärkt den v1.0-Pfad mit Adoption-/Validation-Evidence**, behauptet aber keine v1.0-Reife und aktiviert keine volle v1.x-Kompatibilitätszusage. Kein 0.9-Dokument darf v1.0 als erreicht darstellen. Ein v1.0-Release entscheidet ausschließlich ein späterer eigener v1.0-Zyklus.

## EN – v1.0 Boundary

Foundation 0.9 **strengthens the v1.0 path with adoption/validation evidence** but claims no v1.0 maturity and activates no full v1.x promise. No 0.9 document may present v1.0 as reached. A v1.0 release is decided solely by a later dedicated v1.0 cycle.

## DE – Offene Entscheidungen für WP-121

1. Finale blocking/optional/deferred-Einstufung.
2. Befürwortet WP-124 die docs-only Skills-Implementierung — und werden WP-125/WP-129 blocking oder optional?
3. Werden die 0.8-Optional-WPs (112/116/117/118) durch 0.9-Kandidaten ersetzt oder parallel geführt?
4. Umfang der Adoption-/Validation-Evidence.
5. Änderungsregeln nach Scope Lock.

## EN – Open Decisions for WP-121

(1) Final classification; (2) whether WP-124 endorses the docs-only skills implementation and whether WP-125/WP-129 are blocking or optional; (3) whether the 0.8 optional WPs are replaced or run in parallel; (4) the scope of adoption/validation evidence; (5) change rules after scope lock.

## DE – Go/No-Go

Finale Entscheidung nach Checkliste durch den Human Maintainer (Checkliste entsteht erst in NDF-WP-128).

## EN – Go/No-Go

Final decision by the human maintainer after the checklist (created only in NDF-WP-128).
