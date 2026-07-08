# Foundation 0.8 Release Criteria (Draft)

## DE – Status

**Planning-Draft (NDF-WP-107).** Foundation 0.8 ist **nicht scope-locked**, **nicht released**, **nicht v1.0**. Die folgenden Kriterien sind **Kandidaten** für die spätere Scope-Lock-Entscheidung (WP-108) — sie werden erst gegen tatsächliche Ergebnisse abgehakt, keine falschen Haken. Nur WP-107 (Planning) ist erledigt.

## EN – Status

**Planning draft (NDF-WP-107).** Foundation 0.8 is **not scope-locked**, **not released**, **not v1.0**. The criteria below are **candidates** for the later scope-lock decision (WP-108) — checked only against actual results, no false checkmarks. Only WP-107 (planning) is done.

## DE – Arbeitstitel

```text
Foundation 0.8 – Agent Enablement & Context Economy
(voraussichtlich Pre-Release v0.8.0-foundation — nur geplant, nicht scope-locked, nicht released)
```

## EN – Working Title

Foundation pre-release, presumably `v0.8.0-foundation` — planned only, not scope-locked, not released. Operationalize agent enablement and context economy without claiming v1.0.

## DE – Kandidaten-Kriterien (verbindlich erst mit WP-108)

- [x] Foundation 0.7 released und abgeschlossen (`v0.7.0-foundation`, 2026-07-08; WP-106).
- [x] Foundation 0.8 Planning erstellt (NDF-WP-107).
- [ ] Foundation 0.8 Scope Lock abgeschlossen (NDF-WP-108).
- [ ] NDF Context Economy Concept angenommen (NDF-WP-109).
- [ ] NDF Skill Security Policy angenommen (NDF-WP-110).
- [ ] Skills-MVP-Scope definiert (NDF-WP-111).
- [ ] Skill Pack bleibt public-neutral (keine privaten Projektdaten, keine externen Skill-Inhalte).
- [ ] Keine autonome Git-/Release-/Tag-Aktion durch Skills.
- [ ] Public Quality Gate strict grün.
- [ ] Public Quality Gate self-test grün.
- [ ] Release Readiness Review abgeschlossen (NDF-WP-114).
- [ ] Release Prep abgeschlossen (NDF-WP-115).
- [ ] Finaler Tag + GitHub Pre-Release (nur Human Maintainer).

## EN – Candidate Criteria (binding only with WP-108)

0.7 released (done); 0.8 planning done; scope lock; context economy concept accepted; skill security policy accepted; skills MVP scope defined; skill pack stays public-neutral; no autonomous git/release/tag action by skills; public quality gate strict + self-test green; readiness review; release prep; final tag + GitHub pre-release by the human maintainer only.

## DE – Sicherheits- und Neutralitätsinvarianten

Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflicht. Keine privaten Projekt-/Personennamen, Reviewer-Identitäten, Kontaktwege, echten Domains oder Secret-Werte (der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden). Keine Drittanbieter-Skill-Inhalte oder externen Branding-/Autorenhinweise. Skills docs-only zuerst; keine Netzwerkzugriffe; keine Git-Schreibaktionen; Human-Maintainer-Gates verbindlich.

## EN – Security and Neutrality Invariants

Public quality gate v0.2 stays mandatory. No private names, reviewer identities, contacts, domains, or secret values (naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed). No third-party skill content or external branding/author notices. Skills docs-only first; no network access; no git writes; human-maintainer gates binding.

## DE – v1.0-Abgrenzung

Foundation 0.8 ist **kein v1.0-Schritt** und keine v1.0-Vorbereitung; es adressiert kein offenes v1.0-Kriterium direkt. Kein 0.8-Dokument darf v1.0 als erreicht oder eine volle v1.x-Kompatibilitätszusage als aktiv darstellen. Ein v1.0-Release entscheidet ausschließlich ein späterer eigener v1.0-Zyklus.

## EN – v1.0 Boundary

Foundation 0.8 is **not a v1.0 step** and not v1.0 preparation; it addresses no open v1.0 criterion directly. No 0.8 document may present v1.0 as reached or a full v1.x promise as active. A v1.0 release is decided solely by a later dedicated v1.0 cycle.

## DE – Offene Entscheidungen für WP-108

1. Finale blocking/optional/deferred-Einstufung.
2. Wird die Skills-MVP-Implementierung (WP-112) blocking oder optional/Folge-Release?
3. Bleibt das MVP strikt docs-only oder werden ausgewählte Scripts unter Security Policy erlaubt?
4. Konkreter Skill-Umfang des MVP.
5. Änderungsregeln nach Scope Lock.

## EN – Open Decisions for WP-108

(1) Final classification; (2) whether the skills MVP implementation (WP-112) is blocking or optional/follow-up; (3) whether the MVP stays strictly docs-only or allows selected scripts under the security policy; (4) the concrete MVP skill set; (5) change rules after scope lock.

## DE – Go/No-Go

Finale Entscheidung nach Checkliste durch den Human Maintainer (Checkliste entsteht erst in NDF-WP-115).

## EN – Go/No-Go

Final decision by the human maintainer after the checklist (created only in NDF-WP-115).
