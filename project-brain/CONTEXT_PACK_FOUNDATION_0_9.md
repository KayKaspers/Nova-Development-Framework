# Context Pack – Foundation 0.9

> Kompakter Phasen-Snapshot nach dem [Context Pack Template](CONTEXT_PACK_TEMPLATE.md) (NDF-WP-121). Nur geprüfte, öffentliche Repo-Inhalte. Ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate und kein Human-Maintainer-Review.

## Status

`scope-locked` · **nicht released** · **nicht v1.0** · validation-first · Snapshot: 2026-07-08.

## Scope

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Zuerst Adoption/Validation der 0.8-Artefakte, dann optionale Enablement-Entscheidungen.

## Current Phase

Foundation 0.9.

## Current Phase Status

**Released / published — reconciliation documented** als `v0.9.0-foundation` (2026-07-10, NDF-WP-133). Nicht v1.0, kein v1.0 Release Candidate, keine aktive volle v1.x-Zusage. Kein aktives Skill Pack.

## Last Completed Work Package

`NDF-WP-125 – Skills MVP Implementation Blueprint` — GO WITH NOTES; 4-Skill-MVP empfohlen (`ndf-work-package-runner`, `ndf-compact-context-summary-runner`, `ndf-public-neutrality-guard`, `ndf-context-pack-maintainer`); WP-129 bedingt mit engem docs-only Scope empfohlen; **keine Implementierung**, kein aktives Skill Pack. Blueprint: `docs/validation/foundation-0-9/SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md`.

## Next Work Package

`NDF-WP-129 – Docs-only Skills MVP Implementation` — **optional, nicht aktiviert**; nur bei ausdrücklichem Human-Maintainer-Scope-Change, engem docs-only Scope (die vier MVP-Skills), ADR-0032-konform.

## Release-Blocking Work Packages

- NDF-WP-121 Scope Lock — done
- NDF-WP-122 Context Economy Adoption Review — done (GO WITH NOTES)
- NDF-WP-123 Prompt Modes and Context Pack Validation — done (GO WITH NOTES)
- NDF-WP-124 Optional Skills MVP Implementation Decision — done (Option B: Blueprint-first, implementation-not-activated)
- NDF-WP-126 Adoption Evidence and v1.0 Path Review — done (GO WITH NOTES)
- NDF-WP-127 Release Readiness Review — done (GO WITH NOTES)
- NDF-WP-128 Release Prep — done
- NDF-WP-133 Post-Release Reconciliation Cleanup — done (released / published — reconciliation documented)

## Optional Work Packages

- NDF-WP-125 Skills MVP Implementation Blueprint — **erledigt: GO WITH NOTES** (4-Skill-MVP empfohlen; keine Implementierung, kein aktives Skill Pack)
- NDF-WP-129 Docs-only Skills MVP Implementation — optional, **not activated** (nach WP-125 bedingt mit engem docs-only Scope empfohlen)
- NDF-WP-130 Skill-to-Cursor Rules Export Assessment — optional (Assessment)
- NDF-WP-131 Workflow Builder Evaluation — optional (Evaluation)
- NDF-WP-132 Docs Polish Skill Evaluation — optional (Evaluation)
- NDF-WP-133 Post-Release Status Cleanup — post-release candidate

## Deferred / Non-Goals

Aktives Skill Pack per Default; `.claude/skills` per Default; Skills-Implementierung ohne Human-Maintainer-Scope-Change; Scripts in Skills; netzwerkfähige Skills; Git-/Release-/Tag-Aktionen durch Skills; Cursor-Rules-/Workflow-Implementierung; Drittanbieter-Skill-Import; v1.0 RC; Aktivierung der vollen v1.x-Zusage.

## Accepted ADRs Relevant to This Phase

- `ADR-0031 – v1.x Compatibility Policy (Accepted)` — volle Zusage erst mit v1.0.
- `ADR-0032 – Skill Security Policy (Accepted)` — fail-closed Governance für NDF-Skills.
- Nächste freie ADR-Nummer: **ADR-0033**.

## Current Safety Boundaries

Fail closed; keine aktiven Skills ohne ausdrücklichen Scope; keine Scripts/Netz/Secrets/privaten Daten; keine autonomen Commit-/Push-/Tag-/Release-Aktionen; kein Drittanbieter-Skill-Import; Public Quality Gate + Public Neutrality Pflicht; Human Maintainer finale Kontrolle.

## Known Notes / Limitations

Validation-first; Skills-Implementierung optional/nicht aktiviert (WP-129); WP-124 nur Entscheidung; 0.8-Optional-WPs (112/116/117/118) neu bewertbar, nicht überschrieben; 0.9 noch nicht release-geprüft (WP-127 offen).

## Relevant Source Files

- `docs/roadmap/FOUNDATION_0_9_SCOPE_LOCK.md`, `FOUNDATION_0_9_PLAN.md`, `FOUNDATION_0_9_WORK_PACKAGES.md`
- `docs/release/FOUNDATION_0_9_RELEASE_CRITERIA.md`
- `docs/agent-workflows/NDF_CONTEXT_ECONOMY.md`, `NDF_PROMPT_MODES.md`, `NDF_SKILL_SECURITY_POLICY.md`, `NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md`
- `docs/adr/ADR-0031-...`, `ADR-0032-skill-security-policy.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`

## Compact Context History

- WP-120: Foundation 0.9 Planning — Arbeitstitel „Adoption, Validation & Optional Enablement"; Kandidaten-WPs 120–128 (+optional 129–133). Kein Scope Lock, keine Skills.
- WP-121: Scope Lock — validation-first; blocking 121/122/123/124/126/127/128; WP-124 blocking-Entscheidung, WP-125 optional/conditional, WP-129 optional/nicht aktiviert; 0.8-Optional-WPs neu bewertbar.
- WP-122: Context Economy Adoption Review — GO WITH NOTES; Adoption belegt (16-Punkte-Matrix), Compact Context Summary/Context Packs/Prompt Modes praktisch genutzt; kein aktives Skill Pack.
- WP-123: Prompt Modes and Context Pack Validation — GO WITH NOTES; 28-Punkte-Matrix; Short Prompt sicher begrenzt, Template vollständig; Note PMV-003: erster realer Short-Prompt-Einsatz bleibt Beobachtungspunkt.
- WP-124: Optional Skills MVP Implementation Decision — **Option B: Blueprint-first, implementation-not-activated** (24-Punkte-Matrix); WP-125 empfohlen/nicht aktiviert, WP-129 nicht aktiviert; ADR-0032 bindend.
- WP-126: Adoption Evidence and v1.0 Path Review — GO WITH NOTES; WP-122/123/124-Evidence zusammengeführt (28-Punkte-Matrix); v1.0-Pfad gestärkt (Arbeitsweise/Effizienz), aber kein offenes v1.0-Kriterium direkt adressiert; externe-Validierungs-Evidenz-Tiefe bleibt v1.0-tracked; volle v1.x-Zusage nicht aktiv.
- WP-127: Release Readiness Review — **GO WITH NOTES**; 18-Punkte-Criteria-Check (16 Met, 2 Met with notes), alle blocking WPs vor WP-127 erfüllt, keine Blocker; Known Notes für WP-128-Release-Notes fixiert.
- WP-128: Release Prep — Release Notes + Go/No-Go + Tagging-Guide erstellt; alle Known Notes übernommen.
- WP-133: Post-Release Reconciliation Cleanup — Tag `v0.9.0-foundation` (annotated, → `e735041`/WP-126) + GitHub Pre-Release (published 2026-07-10) read-only verifiziert; Status auf **released / published — reconciliation documented** gehoben. Tag-Cut lag bei WP-126; WP-127/128 nach dem Tag committet (`b268503`), kein Tag-Move / History-Rewrite / Korrektur-Release. Nächster Schritt WP-125 (Blueprint).
- WP-125: Skills MVP Implementation Blueprint — **GO WITH NOTES**; zehn Kandidaten bewertet, 4-Skill-MVP empfohlen (WP-Runner, Compact-Context-Summary-Runner, Public-Neutrality-Guard, Context-Pack-Maintainer), Extended-Set + Nicht-Empfohlene definiert; Token-Economy hoch–sehr hoch, Skill/PK/Prompt-Matrix, Security-Model, 13-Punkte-Validierungsplan; WP-129 bedingt mit engem docs-only Scope empfohlen; **keine Implementierung**, kein aktives Skill Pack, keine `.claude/skills`/`SKILL.md`/Scripts.

## Next Prompt Recommendation

**Full Prompt Mode** für WP-129 (Docs-only Skills MVP Implementation — Skills-/Security-/Governance-Bezug; empfohlenes Modell Claude Opus 4.8) — **nur** bei ausdrücklichem Human-Maintainer-Scope-Change und engem docs-only Scope (die vier MVP-Skills); sonst bleibt WP-129 nicht aktiviert.

## What Must Not Be Claimed

Keine Foundation-0.9-Release-Behauptung; kein v1.0; keine aktive volle v1.x-Kompatibilitätszusage; kein aktives Claude Skills Pack; keine WP-129-Aktivierung.

## What Must Not Be Included

Keine privaten Daten; keine Secrets; keine Roh-Chatlogs; keine Chain-of-Thought; keine externen Skill-Inhalte; keine riesigen Kopien.

## Update Rules

Nach jedem abgeschlossenen WP aktualisieren; nur geprüfte, öffentliche Repo-Inhalte; Compact Context Summary als Inputquelle erlaubt; ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate, kein Human-Maintainer-Review.
