# Context Pack – Foundation 0.9

> Kompakter Phasen-Snapshot nach dem [Context Pack Template](CONTEXT_PACK_TEMPLATE.md) (NDF-WP-121). Nur geprüfte, öffentliche Repo-Inhalte. Ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate und kein Human-Maintainer-Review.

## Status

`scope-locked` · **nicht released** · **nicht v1.0** · validation-first · Snapshot: 2026-07-08.

## Scope

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Zuerst Adoption/Validation der 0.8-Artefakte, dann optionale Enablement-Entscheidungen.

## Current Phase

Foundation 0.9.

## Current Phase Status

**Released / published — reconciliation documented** als `v0.9.0-foundation` (2026-07-10, NDF-WP-133). Nicht v1.0, kein v1.0 Release Candidate, keine aktive volle v1.x-Zusage. Ein **docs-only Skills MVP** (vier Markdown-Skills unter `.claude/skills/`) ist seit WP-129 vorhanden — additiv, ADR-0032-konform, ohne Scripts/Automation; keine autonom ausführenden Skills. Seit WP-134 gilt der **Skills-first Operating Mode**: Standard Prompt Mode als Default, Full nur für kritische Fälle (Security/Release/ADR/v1.0/neue Skills); DSK-001 Partially closed.

## Last Completed Work Package

`NDF-WP-135 – External Skills Landscape & Project Skill Prioritization` — GO WITH NOTES; externe Skill-Quellen als Kategoriemodell bewertet (keine Übernahme, kein Netzwerk), sieben Skill-Families priorisiert, NDF-Core/Project-Enablement getrennt, Allow/Watch/Reject + Skill-Roadmap (136→v1.0); Project-local-Skills nur als neutrale Archetypen (keine privaten Namen); keine neuen/Extended Skills. Doc: `docs/validation/foundation-0-9/EXTERNAL_SKILLS_LANDSCAPE_AND_PRIORITIZATION.md`.

## Next Work Package

**NDF-WP-136 – NDF Extended Skills Pack Blueprint** (Core/Governance/Docs, P0/P1-Allowlist; Kandidat, docs-only, nicht aktiviert; Skill-assisted Full Prompt Mode, Opus 4.8). Skill-first-Roadmap: WP-136 → 137 → 138 → 139 (Real-use-Validierung, schließt DSK-001) → v1.0 Gap Review & Scope Lock. WP-130/131/132 bleiben optional/nicht aktiviert.

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

- NDF-WP-125 Skills MVP Implementation Blueprint — **erledigt: GO WITH NOTES** (4-Skill-MVP empfohlen)
- NDF-WP-129 Docs-only Skills MVP Implementation — **erledigt: GO WITH NOTES** (vier docs-only MVP-Skills implementiert, ADR-0032-konform, keine Extended Skills)
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
- WP-129: Docs-only Skills MVP Implementation — **GO WITH NOTES**; genau vier docs-only MVP-Skills unter `.claude/skills/` implementiert + `README.md`-Index + [Validation](../docs/validation/foundation-0-9/DOCS_ONLY_SKILLS_MVP_VALIDATION.md) (18-Punkte-Matrix); keine Extended Skills, keine Scripts, kein Netz, keine Secrets (nur Name), keine Git-/Release-Aktionen; ADR-0032 unverändert bindend; Scope-Change (`.claude/skills`/`SKILL.md` nun erlaubt) ausschließlich für diese vier Skills. Known Note DSK-001: Prompt-Ersparnis noch nicht empirisch gemessen.
- WP-134: Skills-first Operating Mode & Prompt Compression Validation — **GO WITH NOTES**; Skills-first Operating Mode dokumentiert ([Operating Mode](../docs/validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md), [Compression Validation](../docs/validation/foundation-0-9/SKILLS_PROMPT_COMPRESSION_VALIDATION.md)); drei Vorher/Nachher-Prompt-Typen verglichen (normal hoch ~40–60 %, release mittel ~25–40 %, governance ~30–45 %); Standard Prompt Mode neuer Default, Full für kritische Fälle; **DSK-001 Partially closed** (strukturelle Baseline; Real-use-Messung offen → WP-139); keine neuen/Extended Skills; Governance stabil; ADR-0032 unverändert. Skill-first-Roadmap-Kandidaten WP-135–139 dokumentiert (nicht aktiviert).
- WP-135: External Skills Landscape & Project Skill Prioritization — **GO WITH NOTES**; vier externe Quellen als Kategoriemodell bewertet (kein Netzwerk, keine 1:1-Übernahme, Lizenzprüfung vor Adaption nötig); sieben Skill-Families priorisiert; Kandidaten P0–P3 (P0: skill-quality-reviewer, existing-project-analysis-runner, docs-polish-runner, changelog-writer); Allow/Watch/Reject (Rejectlist: Git-/Release-/Netz-/Secret-/Payment-/Social-/Offensive-Security-/Multi-Agent-Automation, unklare Lizenz, private Projektlogik); Public-NDF vs Project-local getrennt (Archetypen, keine privaten Namen); Roadmap WP-136→v1.0. Keine neuen/Extended Skills; ADR-0032 unverändert.

## Next Prompt Recommendation

**Skill-assisted Full Prompt Mode** für **NDF-WP-136 – NDF Extended Skills Pack Blueprint** (Core/Governance/Docs, P0/P1-Allowlist; docs-only Blueprint, keine Implementierung; empfohlenes Modell Claude Opus 4.8). WP-137 (Project Enablement) danach/parallel. WP-130/131/132 bleiben optional/nicht aktiviert.

## What Must Not Be Claimed

Keine Foundation-0.9-Release-Behauptung; kein v1.0; keine aktive volle v1.x-Kompatibilitätszusage; kein aktives Claude Skills Pack; keine WP-129-Aktivierung.

## What Must Not Be Included

Keine privaten Daten; keine Secrets; keine Roh-Chatlogs; keine Chain-of-Thought; keine externen Skill-Inhalte; keine riesigen Kopien.

## Update Rules

Nach jedem abgeschlossenen WP aktualisieren; nur geprüfte, öffentliche Repo-Inhalte; Compact Context Summary als Inputquelle erlaubt; ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate, kein Human-Maintainer-Review.
