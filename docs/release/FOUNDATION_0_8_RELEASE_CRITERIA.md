# Foundation 0.8 Release Criteria (Draft)

## DE – Status

**Released / published als `v0.8.0-foundation` Foundation Pre-Release am 2026-07-08 (NDF-WP-119).** Foundation 0.8 ist released, aber **nicht v1.0**; die volle v1.x-Kompatibilitätszusage ist nicht aktiv. Read-only-Verifikation: [FOUNDATION_0_8_POST_RELEASE_STATUS.md](FOUNDATION_0_8_POST_RELEASE_STATUS.md). Boxen werden nur gegen tatsächliche Ergebnisse abgehakt — keine falschen Haken.

## EN – Status

**Released / published as the `v0.8.0-foundation` foundation pre-release on 2026-07-08 (NDF-WP-119).** Foundation 0.8 is released, but **not v1.0**; the full v1.x compatibility promise is not active. Read-only verification: the post-release status document. Boxes are checked only against actual results — no false checkmarks.

## DE – Arbeitstitel

```text
Foundation 0.8 – Agent Enablement & Context Economy
(Pre-Release v0.8.0-foundation — veröffentlicht am 2026-07-08, nicht v1.0)
```

## EN – Working Title

Foundation pre-release `v0.8.0-foundation` — published on 2026-07-08, not v1.0. Operationalized agent enablement and context economy without claiming v1.0.

## DE – Release-blocking Kriterien (verbindlich seit WP-108)

- [x] Foundation 0.7 released und abgeschlossen (`v0.7.0-foundation`, 2026-07-08; WP-106).
- [x] Foundation 0.8 Planning erstellt (NDF-WP-107).
- [x] Foundation 0.8 Scope Lock abgeschlossen (NDF-WP-108, 2026-07-08: [`FOUNDATION_0_8_SCOPE_LOCK.md`](../roadmap/FOUNDATION_0_8_SCOPE_LOCK.md); WP-112 optional (Option A), ADR-0032 in WP-110).
- [x] NDF Context Economy Concept angenommen (NDF-WP-109, 2026-07-08: [`NDF_CONTEXT_ECONOMY.md`](../agent-workflows/NDF_CONTEXT_ECONOMY.md); 5 Kontext-Schichten, Compact Context Summary verbindlich, Context Packs + Prompt Modes konzeptionell — Templates in WP-113).
- [x] NDF Skill Security Policy angenommen / **ADR-0032 erstellt** (NDF-WP-110, 2026-07-08: [ADR-0032](../adr/ADR-0032-skill-security-policy.md) Accepted + [`NDF_SKILL_SECURITY_POLICY.md`](../agent-workflows/NDF_SKILL_SECURITY_POLICY.md); fail closed, keine autonomen Git-/Release-/Netz-/Secret-Aktionen; nächste freie ADR-Nummer 0033).
- [x] Skills-MVP-Design definiert (NDF-WP-111, 2026-07-08: [`NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md`](../agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md); 6 Skills + Review Matrix, nur Design, kein aktives Skill Pack).
- [x] NDF Context Pack Template + Prompt-Modi standardisiert (NDF-WP-113, 2026-07-08: [`NDF_PROMPT_MODES.md`](../agent-workflows/NDF_PROMPT_MODES.md), [`CONTEXT_PACK_TEMPLATE.md`](../../project-brain/CONTEXT_PACK_TEMPLATE.md), [`CONTEXT_PACK_FOUNDATION_0_8.md`](../../project-brain/CONTEXT_PACK_FOUNDATION_0_8.md); Short Prompt nie für kritische Arbeit).
- [ ] Skill Pack bleibt public-neutral (keine privaten Projektdaten, keine externen Skill-Inhalte).
- [ ] Keine autonome Git-/Release-/Tag-Aktion durch Skills.
- [ ] Public Quality Gate strict grün.
- [ ] Public Quality Gate self-test grün.
- [x] Release Readiness Review abgeschlossen (NDF-WP-114, 2026-07-08: **GO WITH NOTES** — [`FOUNDATION_0_8_READINESS_REVIEW.md`](FOUNDATION_0_8_READINESS_REVIEW.md); keine Blocker, kein aktives Skill Pack, 20-Punkte-Readiness-Matrix).
- [x] Release Prep abgeschlossen (NDF-WP-115, 2026-07-08: [`FOUNDATION_0_8_RELEASE_NOTES.md`](FOUNDATION_0_8_RELEASE_NOTES.md), [`FOUNDATION_0_8_GO_NO_GO_CHECKLIST.md`](FOUNDATION_0_8_GO_NO_GO_CHECKLIST.md), [`FOUNDATION_0_8_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`](FOUNDATION_0_8_TAGGING_AND_GITHUB_RELEASE_GUIDE.md); **release-prepared / tag pending**).
- [x] Finaler Tag + GitHub Pre-Release (Human Maintainer, 2026-07-08): Tag `v0.8.0-foundation` (annotated, → Commit `a39f50b`), GitHub Pre-Release „Nova Development Framework v0.8.0 Foundation" (prerelease, Target `main`); read-only verifiziert in NDF-WP-119.
- [x] Post-Release-Status-Cleanup (NDF-WP-119, 2026-07-08): Statusdokumente auf released/published gehoben, Tag + GitHub Release read-only verifiziert; keine offenen 0.8-blocking Follow-ups.

**Foundation 0.8 ist released / published als `v0.8.0-foundation` (2026-07-08). Nicht v1.0; die volle v1.x-Kompatibilitätszusage ist nicht aktiv; kein aktives Skill Pack.** / Foundation 0.8 is released/published as `v0.8.0-foundation`; not v1.0; the full v1.x compatibility promise is not active; no active skill pack.

## EN – Release-Blocking Criteria (binding since WP-108)

0.7 released (done); 0.8 planning done; scope lock done (WP-112 optional per Option A, ADR-0032 in WP-110); context economy concept accepted; skill security policy accepted / ADR-0032 created; skills MVP design defined (design only); context pack template + prompt modes standardized; skill pack stays public-neutral; no autonomous git/release/tag action by skills; public quality gate strict + self-test green; readiness review; release prep; final tag + GitHub pre-release by the human maintainer only.

## DE – Optionale Kandidaten

- [ ] NDF Claude Skills Pack MVP Implementation (NDF-WP-112) — **optional (Option A)**; nur per Human-Maintainer-Scope-Change hochstufbar (Regel im Scope Lock).
- [ ] Skill-to-Cursor Rules Export Assessment (NDF-WP-116).
- [ ] Workflow Builder Evaluation (NDF-WP-117).
- [ ] Docs Polish Skill Evaluation (NDF-WP-118).

## EN – Optional Candidates

WP-112 skills MVP implementation (optional, Option A — upgradable only via human-maintainer scope change), WP-116/117/118 assessments/evaluations — none blocks.

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
