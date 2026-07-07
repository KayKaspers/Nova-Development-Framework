# Foundation 0.6 Plan

## DE – Zweck

Dieser Plan definiert den Umfang für Foundation 0.6 (Ergebnis von NDF-WP-084). **Status-Update: Released** als `v0.6.0-foundation` (Foundation Pre-Release, 2026-07-07 — kein v1.0); Scope locked seit NDF-WP-085 — verbindliche Einstufung: [FOUNDATION_0_6_SCOPE_LOCK.md](FOUNDATION_0_6_SCOPE_LOCK.md). Release-blocking sind nur 085, 086 (ADR-Entscheidung — **erledigt: Minimal ADR Policy adopted**, [`docs/adr/ADR_POLICY.md`](../adr/ADR_POLICY.md)), 088 (öffentliche Validierung — **erledigt: PASS WITH NOTES**, Ventil nicht benötigt, WP-087 skipped), 089 (Gate Maintenance — **erledigt: Evidence-Level strong, WP-090 not needed**), 094 (**erledigt: GO WITH NOTES**), 095 (**erledigt: Release Prep**). Foundation 0.6 ist als `v0.6.0-foundation` veröffentlicht — weiterhin **nicht v1.0**.

## EN – Purpose

This plan defines the scope for Foundation 0.6 (result of NDF-WP-084). **Status update: Released** as `v0.6.0-foundation` (foundation pre-release, 2026-07-07 — not v1.0); scope locked since NDF-WP-085 — binding classification: [FOUNDATION_0_6_SCOPE_LOCK.md](FOUNDATION_0_6_SCOPE_LOCK.md). All release-blocking work packages are done.

## DE – Leitidee

**Foundation 0.6 – Adoption Confidence & Governance Hardening** (Adoptionsvertrauen & Governance-Härtung). Foundation 0.5 hat die offenen Punkte sichtbar und messbar gemacht — 0.6 arbeitet sie **kontrolliert ab oder entscheidet sie bewusst**: die aufgeschobene ADR-Policy wird entschieden (nicht wieder verschoben), die externe Validierung wird auf das öffentliche Fixture gehoben, der Quality Gate wird gewartet und nachweisbar gemacht, und die v1.x-Kompatibilitätsfrage bekommt einen ersten Policy-Entwurf.

## EN – Theme

**Foundation 0.6 – Adoption Confidence & Governance Hardening.** Foundation 0.5 made the open items visible and measurable — 0.6 works them off **in a controlled way or decides them consciously**: the deferred ADR policy gets decided (not carried over again), external validation is lifted to the public fixture, the quality gate is maintained and made provable, and the v1.x compatibility question gets a first policy draft.

## DE – Ausgangspunkt nach Foundation 0.5

`v0.5.0-foundation` ist veröffentlicht (2026-07-07), Foundation 0.5 ist vollständig abgeschlossen, keine offenen Follow-ups. Aus WP-083 übernommene 0.6-Kandidaten:

1. ADR-Policy-Entscheidung: priorisieren oder ausdrücklich streichen (**verbindliche Sonderregel aus dem 0.5 Scope Lock — kein drittes stilles Verschieben**)
2. Öffentlicher SampleProject-Runbook-Validierungslauf (v1.0-tracked; WP-073-Unterlagen sofort nutzbar)
3. Optionale Checklist-/i18n-Arbeit
4. Quality Gate Maintenance Review inkl. CI-Denylist-Wirksamkeitsnachweis
5. Academy Entry Pass
6. v1.x-Kompatibilitätszusage / Compatibility Policy Draft (v1.0-tracked)

## EN – Starting Point after Foundation 0.5

`v0.5.0-foundation` is published (2026-07-07), Foundation 0.5 is fully complete, no open follow-ups. The 0.6 candidates carried over from WP-083 are listed above — including the binding ADR special rule (prioritize or drop explicitly, no third silent carry-over).

## DE – Ziele

1. **Governance-Härtung:** Die ADR-Policy wird entschieden — dokumentierte Entscheidung statt Dauerläufer. Ergebnis darf auch ein ehrliches Streichen sein.
2. **Adoptionsvertrauen:** Ein Runbook-basierter unabhängiger Lauf gegen das **öffentliche** SampleProject-Fixture hebt External Validation im v1.0-Draft von `partially met` Richtung `met`.
3. **Nachweisbare Qualität:** Gate-Wartung inkl. Nachweis, dass die CI-Denylist mit gesetztem Secret tatsächlich greift.
4. **v1.0-Unsicherheit reduzieren:** Erster v1.x-Kompatibilitäts-Policy-Entwurf schließt die im v1.0-Draft benannte bewusste Lücke — als Entwurf, nicht als Versprechen.
5. Optional: Checklist-DE/EN- und Academy-Einstiegslücken verkleinern, ehrlich in der Matrix geführt.

## EN – Goals

(1) Governance hardening: the ADR policy gets decided — a documented decision instead of a perpetual carry-over (an honest drop is a valid outcome). (2) Adoption confidence: a runbook-based independent run against the **public** SampleProject fixture lifts external validation in the v1.0 draft from `partially met` toward `met`. (3) Provable quality: gate maintenance including proof that the CI denylist works with the secret set. (4) Reduce v1.0 uncertainty: a first v1.x compatibility policy draft closes the deliberate gap named in the v1.0 draft — as a draft, not a promise. (5) Optionally shrink the checklist DE/EN and academy entry gaps.

## DE – Nicht-Ziele

- Kein v1.0-Release, kein v1.0 Release Candidate, keine v1.0-Reife-Behauptung — 0.6 **reduziert v1.0-Unsicherheit**, mehr nicht.
- Kein großer Rewrite; keine neuen Großkonzepte ohne Scope-Review.
- Keine vollständige Doku-Website, keine Export-Pipeline, keine CLI.
- Keine vollständige i18n-Abdeckung; Übersetzung bleibt priorisiert.
- Keine ADR-Massenmigration (nur die Policy-Entscheidung; Migration frühestens danach als eigenes Vorhaben).
- Keine Integration realer privater Projekte; Neutralität bleibt Invariante.

## EN – Non-Goals

No v1.0 release, release candidate, or maturity claim — 0.6 **reduces v1.0 uncertainty**, nothing more. No big rewrite; no new large concepts without a scope review; no full documentation website, export pipeline, or CLI; no full i18n coverage; no bulk ADR migration (only the policy decision); no integration of real private projects.

## DE – Kandidaten für den Scope Lock

Vorschlag — verbindlich erst mit NDF-WP-085; Details und vorläufige Einstufung: [FOUNDATION_0_6_WORK_PACKAGES.md](FOUNDATION_0_6_WORK_PACKAGES.md)

| Priorität (Vorschlag) | Thema |
|---|---|
| P1 | Scope Lock (WP-085) |
| P1 | ADR Policy Decision (WP-086 — Sonderregel: entscheiden, nicht verschieben) |
| P1 | Public SampleProject Runbook Validation: Preparation falls nötig (WP-087) + Run (WP-088) |
| P1 | Quality Gate Maintenance Review (WP-089), ggf. inkl. CI Denylist Effectiveness Proof (WP-090) |
| P2 | v1.x Compatibility Policy Draft (WP-093) |
| P2 | Checklist DE/EN Priority Pass (WP-091), Academy Entry Pass (WP-092) |
| Release | Release Readiness (WP-094) + Release Prep (WP-095) |

## EN – Scope Lock Candidates

Proposal — binding only with NDF-WP-085; details and preliminary classification in the work package candidates document (table above).

## DE – v1.0-Bezug

Foundation 0.6 soll v1.0-Unsicherheit reduzieren — **ohne v1.0 zu behaupten**: WP-088 kann External Validation auf volles `met` heben; WP-086 schließt das offene v1.0-Kriterium „ADR-Policy entschieden oder dokumentiert gestrichen"; WP-093 liefert den Entwurf für die im v1.0-Draft als bewusste Lücke geführte v1.x-Kompatibilitätszusage; WP-089/090 stützen die Gate-Invarianten. Ob und wann v1.0 kommt, entscheidet ausschließlich ein späterer eigener v1.0-Zyklus.

## EN – v1.0 Relevance

Foundation 0.6 should reduce v1.0 uncertainty — **without claiming v1.0**: WP-088 can lift external validation to a full `met`; WP-086 closes the open v1.0 criterion "ADR policy decided or documented as dropped"; WP-093 drafts the v1.x compatibility promise named as a deliberate gap in the v1.0 draft; WP-089/090 support the gate invariants. Whether and when v1.0 happens is decided solely by a later dedicated v1.0 cycle.

## DE – Risiken

1. **ADR-Entscheidung wird erneut aufgeschoben** — Gegenmittel: WP-086 ist als Blocking-Kandidat empfohlen und die 0.5-Sonderregel lässt kein stilles Verschieben zu; das Ergebnis darf „streichen" sein, aber nicht „später".
2. **Öffentlicher Validierungslauf erneut personenabhängig** — Gegenmittel: WP-073-Unterlagen sind sofort nutzbar; WP-085 sollte prüfen, ob ein Ventil analog 0.5 nötig ist (Empfehlung: ja, mit denselben strengen Bedingungen).
3. **Kandidatenliste verleitet zu Scope Creep** (12 WPs) — Gegenmittel: WP-085 hält den blocking Kern klein; Optionales bleibt optional.
4. **v1.x-Policy-Entwurf könnte als Zusage gelesen werden** — Gegenmittel: Draft-Markierung wie beim v1.0-Kriterien-Draft, keine Termine.
5. **Ein-Personen-Engpass** — unverändert; kleine WPs halten Reviews machbar.

## EN – Risks

(1) The ADR decision gets deferred again — WP-086 is a recommended blocking candidate and the 0.5 special rule forbids silent carry-over ("drop" is valid, "later" is not). (2) The public validation run is again person-dependent — the WP-073 materials are immediately usable; WP-085 should consider a valve analogous to 0.5. (3) The candidate list invites scope creep — WP-085 keeps the blocking core small. (4) The v1.x policy draft could be read as a promise — draft markers, no dates. (5) Single-person bottleneck — unchanged.

## DE – Empfohlene Reihenfolge

```text
084 (Planning — dieses Dokument)
→ 085 (Scope Lock)
→ 086 (ADR Decision) ‖ 087/088 (Public Validation) ‖ 089/090 (Gate Maintenance + Proof)
→ 091 / 092 / 093 (optional bzw. nach Einstufung durch WP-085)
→ 094 → 095 (Release-Strecke)
```

## EN – Recommended Order

Planning → scope lock → ADR decision ‖ public validation ‖ gate maintenance/proof → optional work per WP-085 classification → release track.

## DE – Nächster Schritt

**NDF-WP-085 – Foundation 0.6 Scope Lock:** verbindliche Einstufung (release-blocking / optional / deferred), Ventil-Frage für WP-088, Änderungsregeln. Kein inhaltliches WP startet vorher.

## EN – Next Step

**NDF-WP-085 – Foundation 0.6 scope lock:** binding classification, the valve question for WP-088, change rules. No content work package starts before it.
