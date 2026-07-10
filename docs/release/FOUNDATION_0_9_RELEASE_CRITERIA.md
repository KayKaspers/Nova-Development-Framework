# Foundation 0.9 Release Criteria (Draft)

## DE – Status

**Released / published — reconciliation documented (NDF-WP-133, 2026-07-10).** Foundation 0.9 ist als `v0.9.0-foundation` Foundation Pre-Release veröffentlicht (annotated Tag → Commit `e735041`/WP-126; GitHub Pre-Release published 2026-07-10). Der Tag-Cut lag bei WP-126; WP-127/WP-128 wurden **nach** dem Tag committet (`b268503`) und sind hier als nachträgliche Readiness-/Prep-Governance-Artefakte dokumentiert. Der Tag wurde **nicht verschoben**, kein History-Rewrite, kein Korrektur-Release. Foundation 0.9 ist **nicht v1.0**, **kein v1.0 RC**; die volle v1.x-Zusage ist nicht aktiv. Boxen werden nur gegen tatsächliche Ergebnisse abgehakt.

## EN – Status

**Released / published — reconciliation documented (NDF-WP-133, 2026-07-10).** Foundation 0.9 is published as the `v0.9.0-foundation` foundation pre-release (annotated tag → commit `e735041`/WP-126; GitHub pre-release published 2026-07-10). The tag cut was at WP-126; WP-127/WP-128 were committed after the tag (`b268503`) and are documented here as post-tag readiness/prep governance artifacts. The tag was **not moved**, no history rewrite, no correction release. Foundation 0.9 is **not v1.0**, **no v1.0 RC**; the full v1.x promise is not active.

## DE – Arbeitstitel

```text
Foundation 0.9 – Adoption, Validation & Optional Enablement
(Pre-Release v0.9.0-foundation — veröffentlicht am 2026-07-10, nicht v1.0)
```

## EN – Working Title

Foundation pre-release, presumably `v0.9.0-foundation` — planned only, not scope-locked, not released. Validate adoption and decide optional enablement without claiming v1.0.

## DE – Release-blocking Kriterien (verbindlich seit WP-121)

- [x] Foundation 0.8 released und abgeschlossen (`v0.8.0-foundation`, 2026-07-08; WP-119).
- [x] Foundation 0.9 Planning erstellt (NDF-WP-120).
- [x] Foundation 0.9 Scope Lock abgeschlossen (NDF-WP-121, 2026-07-08: [`FOUNDATION_0_9_SCOPE_LOCK.md`](../roadmap/FOUNDATION_0_9_SCOPE_LOCK.md); validation-first, WP-124 blocking-Entscheidung, WP-125 optional/conditional, WP-129 optional/nicht aktiviert).
- [x] Context Economy Adoption Review abgeschlossen (NDF-WP-122, 2026-07-08: **GO WITH NOTES** — [`CONTEXT_ECONOMY_ADOPTION_REVIEW.md`](../validation/context-economy/CONTEXT_ECONOMY_ADOPTION_REVIEW.md); Adoption belegt, 16-Punkte-Matrix, Detailvalidierung folgt in WP-123).
- [x] Prompt Modes and Context Pack Validation abgeschlossen (NDF-WP-123, 2026-07-08: **GO WITH NOTES** — [`PROMPT_MODES_CONTEXT_PACK_VALIDATION.md`](../validation/context-economy/PROMPT_MODES_CONTEXT_PACK_VALIDATION.md); 28-Punkte-Matrix, Short Prompt sicher begrenzt, keine Blocker).
- [x] Optional Skills MVP Implementation Decision abgeschlossen (NDF-WP-124, 2026-07-08: **Option B — Blueprint-first, implementation-not-activated** — [`NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md`](../agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md); 24-Punkte-Matrix, WP-125 empfohlen/optional, WP-129 nicht aktiviert).
- [x] Adoption Evidence and v1.0 Path Review abgeschlossen (NDF-WP-126, 2026-07-08: **GO WITH NOTES** — [`ADOPTION_EVIDENCE_AND_V1_0_PATH_REVIEW.md`](../validation/foundation-0-9/ADOPTION_EVIDENCE_AND_V1_0_PATH_REVIEW.md); WP-122/123/124-Evidence zusammengeführt, v1.0-Pfad gestärkt aber nicht geschlossen, volle v1.x-Zusage nicht aktiv).
- [ ] Kein aktives Skill Pack ohne ausdrücklichen Scope + ADR-0032-Konformität.
- [ ] Keine autonome Git-/Release-/Tag-Aktion durch Skills.
- [ ] Public Quality Gate strict grün.
- [ ] Public Quality Gate self-test grün.
- [ ] Public Neutrality sauber.
- [x] Release Readiness Review abgeschlossen (NDF-WP-127, 2026-07-08: **GO WITH NOTES** — [`FOUNDATION_0_9_READINESS_REVIEW.md`](FOUNDATION_0_9_READINESS_REVIEW.md); 18-Punkte-Criteria-Check, keine Blocker, Notes non-blocking).
- [x] Release Prep abgeschlossen (NDF-WP-128, 2026-07-10: [`FOUNDATION_0_9_RELEASE_NOTES.md`](FOUNDATION_0_9_RELEASE_NOTES.md), [`FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md`](FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md), [`FOUNDATION_0_9_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`](FOUNDATION_0_9_TAGGING_AND_GITHUB_RELEASE_GUIDE.md)).
- [x] Finaler annotated Tag + GitHub Pre-Release (Human Maintainer, 2026-07-10): Tag `v0.9.0-foundation` → Commit `e735041`; GitHub Pre-Release „Nova Development Framework v0.9.0 Foundation" (prerelease, Target `main`, published 2026-07-10).
- [x] Post-Release-Reconciliation-Cleanup (NDF-WP-133, 2026-07-10): Tag + GitHub Release read-only verifiziert, Statusdokumente auf released/published gehoben, Tag-Cut-Abweichung (WP-126) transparent dokumentiert; kein Tag-Move, kein History-Rewrite, kein Korrektur-Release.
- [ ] Finaler Tag + GitHub Pre-Release (nur Human Maintainer).

**Foundation 0.9 ist released / published als `v0.9.0-foundation` (2026-07-10). Nicht v1.0, kein v1.0 RC; volle v1.x-Zusage nicht aktiv; kein aktives Skill Pack. Die zwei bekannten Notes (Short-Prompt-Ersteinsatz offen, externe Validierungs-Evidenz-Tiefe v1.0-tracked) bleiben non-blocking und sichtbar.** / Foundation 0.9 is released/published as `v0.9.0-foundation` (2026-07-10); not v1.0, no v1.0 RC; full v1.x promise not active; no active skill pack; the two known notes stay non-blocking and visible.

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
