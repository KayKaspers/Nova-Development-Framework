# Foundation 0.7 Release Criteria

## DE – Status

**Scope locked (NDF-WP-098, 2026-07-08).** Foundation 0.7 ist gelockt, nicht released, nicht v1.0. Die Blocking-Kriterien sind verbindlich gemäß [FOUNDATION_0_7_SCOPE_LOCK.md](../roadmap/FOUNDATION_0_7_SCOPE_LOCK.md); abgehakt wird erst gegen tatsächliche Ergebnisse — keine falschen Haken.

## EN – Status

**Scope locked (NDF-WP-098, 2026-07-08).** Foundation 0.7 is locked, not released, not v1.0. The blocking criteria are binding per the scope lock; boxes are only checked against actual results — no false checkmarks.

## DE – Ziel

```text
Foundation v1.0 Path Consolidation & Compatibility Governance Release
(voraussichtlich Pre-Release v0.7.0-foundation — noch nicht released)
```

## EN – Goal

Foundation pre-release, presumably `v0.7.0-foundation` — not released. Consolidate the v1.0 path and decide compatibility governance without claiming v1.0.

## DE – Release-blocking Kriterien (verbindlich seit WP-098)

- [x] Foundation 0.6 released und abgeschlossen (`v0.6.0-foundation`, 2026-07-07; WP-096).
- [x] Foundation 0.7 Scope locked (NDF-WP-098, 2026-07-08: [`FOUNDATION_0_7_SCOPE_LOCK.md`](../roadmap/FOUNDATION_0_7_SCOPE_LOCK.md)).
- [x] **Checklist DE/EN entschieden** (NDF-WP-099, 2026-07-08: **Option B — optional mit finaler Begründung**, [`FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md`](../roadmap/FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md); nicht release-blocking, kein Auto-Carry, kein Folge-WP).
- [x] **v1.x Compatibility Policy entschieden** (NDF-WP-100, 2026-07-08: **ADR-0031 angenommen** — [`ADR-0031-v1x-compatibility-policy.md`](../adr/ADR-0031-v1x-compatibility-policy.md); Governance-Rahmen, aktive volle v1.x-Zusage erst mit v1.0; v1.0-Kriterium `met with notes`, kein v1.0-Claim).
- [ ] **Project Adapter Convention Stability bestätigt** (NDF-WP-101): Konventionen über 0.4→0.6 stabil/additiv dokumentiert.
- [ ] Release Readiness Review durchgeführt (NDF-WP-104).
- [ ] Release Notes, Go/No-Go-Checkliste und Tagging-Guide vorbereitet (NDF-WP-105).
- [ ] Finaler Tag + GitHub Pre-Release (nur Human Maintainer).

## EN – Release-Blocking Criteria (binding since WP-098)

0.6 released (done, checked at scope lock); scope locked; **checklist DE/EN decided** (prioritized / kept-optional-with-rationale / dropped — no fourth silent deferral); **v1.x compatibility policy drafted** (as a draft, possibly ADR-0031 — no v1.0 claim); **adapter convention stability confirmed** (stable/additive across 0.4→0.6); readiness review; release prep artifacts; final tag + GitHub pre-release by the human maintainer only.

## DE – Optionale Kandidaten

- [ ] External Validation Evidence Depth Pass (NDF-WP-102) — optional mit Upgrade-Ventil (nur per Human-Maintainer-Scope-Change hochstufbar, Bedingungen im Scope Lock); adressiert PSV-001, bleibt sonst non-blocking.
- [ ] Academy Entry Decision (NDF-WP-103).
- [ ] Kleine Doku-/i18n-Konsolidierung.

## EN – Optional Candidates

WP-102 evidence depth pass (upgradable to blocking), WP-103 academy entry decision, small documentation / i18n consolidation — none blocks unless WP-098 says so.

## DE – Deferred / Nicht-Ziele

Vollständige Doku-Website; vollständige i18n-Abdeckung; ADR-Massenmigration; v1.0 Release Candidate; großer Rewrite; neue App-Features. Kosmetisch/manuell (kein WP): optionaler v0.6-Release-Body-Polish.

## EN – Deferred / Non-Goals

Full documentation website; full i18n; ADR mass migration; v1.0 release candidate; large rewrite; new application features. Cosmetic/manual (no work package): optional v0.6 release body polish.

## DE – Public Quality Gate

Der Public Quality Gate v0.2 bleibt Pflichtinvariante: strict + self-test grün, new-file neutrality check aktiv, lokal und in CI. Wirksamkeit zuletzt in WP-089 mit Evidence-Level strong bestätigt.

## EN – Public Quality Gate

The public quality gate v0.2 stays a mandatory invariant: strict + self-test green, new-file neutrality check active, locally and in CI. Effectiveness last confirmed in WP-089 at evidence level strong.

## DE – Public Neutrality

Keine privaten Projekt-/Personennamen, keine Reviewer-Identitäten, keine Kontaktwege, keine echten Domains, keine Secret-Werte (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden). Gilt für alle neuen 0.7-Dokumente.

## EN – Public Neutrality

No private project/person names, reviewer identities, contacts, domains, or secret values (naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed). Applies to all new 0.7 documents.

## DE – v1.0-Abgrenzung

Foundation 0.7 **konsolidiert den v1.0-Pfad**, behauptet aber keine v1.0-Reife. Auch wenn WP-100/101 offene v1.0-Kriterien schließen oder entwerfen: Kein 0.7-Dokument darf v1.0 als erreicht darstellen. Ein v1.0-Release entscheidet ausschließlich ein späterer eigener v1.0-Zyklus (Scope Lock → Readiness → Prep → Maintainer-Freigabe).

## EN – v1.0 Boundary

Foundation 0.7 **consolidates the v1.0 path** but claims no v1.0 maturity. Even where WP-100/101 close or draft open v1.0 criteria, no 0.7 document may present v1.0 as reached. A v1.0 release is decided solely by a later dedicated v1.0 cycle.

## DE – Offene Entscheidungen für WP-098

1. Finale blocking/optional/deferred-Einstufung.
2. Wird WP-102 (Evidence Depth) blocking — und mit welchem Ventil?
3. WP-099-Entscheidungskorridor (priorisieren / optional-mit-Begründung / streichen) verbindlich machen.
4. Entwirft WP-100 die v1.x-Policy als ADR-0031 oder als reines Policy-Dokument?
5. Änderungsregeln nach Scope Lock.

## EN – Open Decisions for WP-098

(1) Final classification; (2) whether WP-102 becomes blocking and with what valve; (3) making the WP-099 decision corridor binding; (4) whether WP-100 drafts the v1.x policy as ADR-0031 or a plain policy document; (5) change rules after scope lock.

## DE – Go/No-Go

Finale Entscheidung nach Checkliste durch den Human Maintainer (Checkliste entsteht erst in NDF-WP-105):

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```

## EN – Go/No-Go

Final decision by the human maintainer after the checklist (created only in NDF-WP-105); fields above.
