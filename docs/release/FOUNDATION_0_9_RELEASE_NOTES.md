# Foundation 0.9 Release Notes

## DE – Status

**Release-prepared / pending manual release.** Foundation 0.9 ist vorbereitet, aber **nicht released**, bis der Human Maintainer den manuellen Release (annotated Tag + GitHub Pre-Release) abschließt. Geplanter Tag: `v0.9.0-foundation`. Nicht v1.0, kein v1.0 Release Candidate; die volle v1.x-Kompatibilitätszusage ist nicht aktiv.

## EN – Status

**Release-prepared / pending manual release.** Foundation 0.9 is prepared but **not released** until the Human Maintainer completes the manual release (annotated tag + GitHub pre-release). Planned tag: `v0.9.0-foundation`. Not v1.0, no v1.0 release candidate; the full v1.x compatibility promise is not active.

## DE – Release-Typ

Foundation **Pre-Release** (`v0.9.0-foundation`), Titel „Nova Development Framework v0.9.0 Foundation", GitHub Pre-Release, annotated Tag.

## EN – Release Type

Foundation **pre-release** (`v0.9.0-foundation`), title "Nova Development Framework v0.9.0 Foundation", GitHub pre-release, annotated tag.

## DE – Zusammenfassung

Foundation 0.9 – **Adoption, Validation & Optional Enablement** validiert die in Foundation 0.8 eingeführten Agent-Enablement-Artefakte in der Praxis: Context Economy ist nachweislich adoptiert, Prompt Modes und Context Packs sind im Detail validiert, der Skills-Pfad ist mit einer dokumentierten Governance-Entscheidung (Blueprint-first) geregelt, und die gesammelte Evidence ist in den v1.0-Pfad eingeordnet — ohne v1.0 zu behaupten. Validation-first, bewusst klein, **kein v1.0-Schritt**.

## EN – Summary

Foundation 0.9 – **Adoption, Validation & Optional Enablement** validates the agent-enablement artifacts introduced in Foundation 0.8 in practice: context economy is demonstrably adopted, prompt modes and context packs are validated in detail, the skills path is governed by a documented decision (blueprint-first), and the collected evidence is placed on the v1.0 path — without claiming v1.0. Validation-first, deliberately small, **not a v1.0 step**.

## DE – Wichtigste Inhalte

- **Context Economy Adoption Review** (WP-122, GO WITH NOTES): 16-Punkte-Matrix belegt, dass Compact Context Summary, Context Packs und Prompt Modes praktisch adoptiert sind.
- **Prompt Modes and Context Pack Validation** (WP-123, GO WITH NOTES): 28-Punkte-Matrix; Full/Standard/Short klar begrenzt, Short mit expliziter Verbotsliste und ohne Gate-/Human-Review-Bypass; Context Pack Template vollständig.
- **Optional Skills MVP Implementation Decision** (WP-124): **Option B — Blueprint-first, implementation-not-activated** (24-Punkte-Matrix gegen ADR-0032); WP-125 empfohlen aber optional, WP-129 nicht aktiviert.
- **Adoption Evidence and v1.0 Path Review** (WP-126, GO WITH NOTES): Evidence zusammengeführt; v1.0-Pfad gestärkt (Arbeitsweise/Effizienz), aber nicht geschlossen.
- **Release Readiness Review** (WP-127, GO WITH NOTES): 18-Punkte-Criteria-Check, keine Blocker.

## EN – Highlights

Context Economy adoption review (WP-122, GO WITH NOTES, 16-point matrix); prompt modes and context pack validation (WP-123, GO WITH NOTES, 28-point matrix — Short with explicit forbidden cases, no gate/human-review bypass); optional skills MVP implementation decision (WP-124: **Option B — blueprint-first, implementation-not-activated**, 24-point matrix against ADR-0032); adoption evidence and v1.0 path review (WP-126, GO WITH NOTES — v1.0 path strengthened, not completed); release readiness review (WP-127, GO WITH NOTES, 18-point criteria check, no blockers).

## DE – Release-blocking Work Packages

WP-121 Scope Lock · WP-122 Context Economy Adoption Review · WP-123 Prompt Modes and Context Pack Validation · WP-124 Optional Skills MVP Implementation Decision · WP-126 Adoption Evidence and v1.0 Path Review · WP-127 Release Readiness Review (GO WITH NOTES) · WP-128 Release Prep (dieses WP). WP-133 Post-Release Cleanup folgt erst nach dem manuellen Release.

## EN – Release-Blocking Work Packages

WP-121/122/123/124/126/127/128 — all complete or prepared; the final annotated tag + GitHub pre-release remain a manual Human Maintainer step. WP-133 post-release cleanup follows only after the manual release.

## DE – Optionale / bedingte Work Packages

Nicht aktiviert: **WP-125** (Skills MVP Implementation Blueprint — von WP-124 empfohlen, Start nur auf ausdrücklichen Human-Maintainer-Wunsch), **WP-129** (Docs-only Skills MVP Implementation — nur per separatem Human-Maintainer-Scope-Change), **WP-130** (Skill-to-Cursor-Export-Assessment), **WP-131** (Workflow-Builder-Evaluation), **WP-132** (Docs-Polish-Skill-Evaluation).

## EN – Optional / Conditional Work Packages

Not activated: WP-125 (blueprint — recommended by WP-124, start only on explicit Human Maintainer request), WP-129 (docs-only implementation — only via separate Human Maintainer scope change), WP-130/131/132 (assessments/evaluations).

## DE – Bekannte Notes / Known Notes

- Foundation 0.9 ist **nicht v1.0**.
- Foundation 0.9 ist **kein v1.0 Release Candidate**.
- Die **volle v1.x-Kompatibilitätszusage ist nicht aktiv** (erst mit einem künftigen v1.0-Release).
- **ADR-0031** (v1.x Compatibility Policy) bleibt accepted und unverändert.
- **ADR-0032** (Skill Security Policy) bleibt accepted und unverändert; nächste freie ADR-Nummer: ADR-0033.
- Es gibt **kein aktives Claude Skills Pack**; keine `.claude/skills`, keine `SKILL.md`, keine Skill-Scripts.
- **WP-125 bleibt optional/conditional**; **WP-129 bleibt optional und nicht aktiviert**; WP-130/131/132 bleiben optional.
- Der **Short Prompt Mode hat in 0.9 noch keinen praktischen Ersteinsatz** (Definition validiert, Beobachtungspunkt).
- Die **externe Validierungs-Evidenz-Tiefe bleibt v1.0-tracked** (evidence-quality note).
- **WP-133** ist erst nach dem manuellen Release relevant.
- **Commit/Push/Tag/Release bleiben Human-Maintainer-only.**

## EN – Known Notes

Not v1.0; no v1.0 release candidate; full v1.x compatibility promise not active (only at a future v1.0 release); ADR-0031 and ADR-0032 stay accepted and unchanged (next free ADR number: ADR-0033); no active Claude Skills Pack — no `.claude/skills`, no `SKILL.md`, no skill scripts; WP-125 stays optional/conditional, WP-129 optional and not activated, WP-130/131/132 optional; Short Prompt Mode has no practical first use in 0.9 yet (definition validated, observation point); external validation evidence depth stays v1.0-tracked; WP-133 becomes relevant only after the manual release; commit/push/tag/release stay Human-Maintainer-only.

## DE – Nicht-Ziele

Kein v1.0 und kein v1.0 Release Candidate; keine aktive volle v1.x-Kompatibilitätszusage; kein aktives Skill Pack; keine Skill-Implementierung; keine Skill-Scripts; keine netzwerkfähigen Skills; keine autonomen Git-/Release-Aktionen; keine Cursor-Rules-/Workflow-Implementierung; kein Drittanbieter-Skill-Import; kein History-Rewrite.

## EN – Non-Goals

No v1.0 and no v1.0 release candidate; no active full v1.x compatibility promise; no active skill pack; no skill implementation; no skill scripts; no network-enabled skills; no autonomous git/release actions; no Cursor rules/workflow implementation; no third-party skill import; no history rewrite.

## DE – Upgrade von Foundation 0.8

Foundation 0.8 bleibt veröffentlicht (Tag `v0.8.0-foundation`). Foundation 0.9 ist additiv: keine Migrationsschritte, keine ersetzten Artefakte. Wer 0.8 nutzt, erhält zusätzlich die Adoption-/Validation-Reviews, die dokumentierte Skills-Governance-Entscheidung und die aktualisierte v1.0-Pfad-Evidence.

## EN – Upgrade from Foundation 0.8

Foundation 0.8 stays published. Foundation 0.9 is additive: no migration steps, no replaced artifacts — users of 0.8 additionally get the adoption/validation reviews, the documented skills governance decision, and the updated v1.0-path evidence.

## DE – Human-Maintainer-Release-Schritte

1. WP-128-Diff prüfen und committen.
2. Finale Go/No-Go-Checkliste durchgehen ([FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md](FOUNDATION_0_9_GO_NO_GO_CHECKLIST.md)).
3. Annotated Tag `v0.9.0-foundation` erstellen und pushen ([Tagging-Guide](FOUNDATION_0_9_TAGGING_AND_GITHUB_RELEASE_GUIDE.md)).
4. GitHub Pre-Release „Nova Development Framework v0.9.0 Foundation" erstellen.
5. Danach WP-133 Post-Release Cleanup starten.

## EN – Human Maintainer Release Steps

(1) Review and commit the WP-128 diff; (2) run the final go/no-go checklist; (3) create and push the annotated tag `v0.9.0-foundation` (tagging guide); (4) create the GitHub pre-release "Nova Development Framework v0.9.0 Foundation"; (5) then start WP-133 post-release cleanup.

---

## GitHub Release Body (Vorschlag / suggested)

```text
Nova Development Framework v0.9.0 Foundation is an adoption, validation and optional
enablement pre-release.

Highlights:
- Context Economy adoption reviewed and confirmed in practice (WP-122)
- Prompt Modes and Context Packs validated in detail; Short Prompt Mode strictly
  bounded with explicit forbidden cases (WP-123)
- Skills MVP implementation decided: Option B — blueprint-first, implementation
  not activated; ADR-0032 stays binding (WP-124)
- Adoption/validation evidence consolidated on the v1.0 path — strengthened,
  not completed (WP-126)
- Release readiness review completed with no blockers (WP-127, GO WITH NOTES)

Known notes:
- No active Claude Skills Pack is created; the skills MVP exists as design only.
- WP-125 (blueprint) stays optional/conditional; WP-129 (implementation) stays
  optional and not activated.
- The Short Prompt Mode has no practical first use yet.
- External validation evidence depth remains v1.0-tracked.
- The full v1.x compatibility promise is not active before a future v1.0 release.

This is not a v1.0 release. Full DE/EN release notes:
docs/release/FOUNDATION_0_9_RELEASE_NOTES.md

---

DE: Adoption-, Validierungs- und Optional-Enablement-Pre-Release. Kein v1.0; die volle
v1.x-Kompatibilitätszusage ist vor einem künftigen v1.0-Release nicht aktiv. Kein aktives
Skill Pack. Vollständige zweisprachige Release Notes im Repository unter
docs/release/FOUNDATION_0_9_RELEASE_NOTES.md.
```
