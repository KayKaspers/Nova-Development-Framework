# Context Pack – Foundation 0.9

> Kompakter Phasen-Snapshot nach dem [Context Pack Template](CONTEXT_PACK_TEMPLATE.md) (NDF-WP-121). Nur geprüfte, öffentliche Repo-Inhalte. Ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate und kein Human-Maintainer-Review.

## Status

`scope-locked` · **nicht released** · **nicht v1.0** · validation-first · Snapshot: 2026-07-08.

## Scope

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Zuerst Adoption/Validation der 0.8-Artefakte, dann optionale Enablement-Entscheidungen.

## Current Phase

Foundation 0.9.

## Current Phase Status

**NDF ist v1.0.0 released — reconciled** (2026-07-10, NDF-WP-149; annotated Tag `v1.0.0` → finaler Commit `9dcadc1`, Final release, kein AI-Git-/Release-Vorgang). Die **volle v1.x-Kompatibilitätszusage ist ab `v1.0.0` aktiv** gemäß ADR-0031 (nicht rückwirkend für Foundation `v0.x`/RC `v1.0.0-rc.1`); RC-Tag historisch unverändert (→ `4beab84`). Vorgeschichte: Foundation 0.9 `v0.9.0-foundation` (WP-133) → v1.0-Pfad WP-139…148 → RC `v1.0.0-rc.1` (WP-143/144) → final `v1.0.0` (WP-148/149). Ein **docs-only Skills-Pack** liegt unter `.claude/skills/` — seit WP-129 vier Core-MVP-Skills, seit WP-137 vier Extended-Core-Skills, seit WP-145 22 Advisory-Skills, seit WP-146 acht weitere Advisory-Skills (**38 gesamt**) — additiv, ADR-0032-konform, ohne Scripts/Automation/Netz/Secrets; keine autonom ausführenden Skills. Seit WP-134 gilt der **Skills-first Operating Mode**: Standard Prompt Mode als Default, Full nur für kritische Fälle (Security/Release/ADR/v1.0/neue Skills); DSK-001 Partially closed.

## Last Completed Work Package

`NDF-WP-150 – v1.1 Planning / Post-v1.0 Roadmap` — GO WITH NOTES – v1.1 planning started; v1.1 = **Validation, Enablement & Operational Maturity** (nur geplant, nicht released); Ausgangslage nach v1.0.0 dokumentiert (v1.x-Zusage aktiv, ADR-0031/0032 unverändert, 38 Skills, keine offenen v1.0-Blocker); Known Final Notes in Roadmap-Items überführt (RDS-001/ADS-001/38-Skill-Real-use → WP-151; G-13-Weg A → WP-152; „kein RC-Feedback" teilweise adressiert durch ersten Projekt-Feedback-Intake → WP-152/153); v1.x-Kompatibilitätsgrenzen dokumentiert; erster realer Projekt-Feedback-Intake (Human Maintainer, project-local) neutral einbezogen; keine Breaking Changes/neue Skills/Releases. Doc: `docs/roadmap/V1_1_PLAN.md`.

## Next Work Package

**NDF-WP-151 – Skills Real-use Review** (RDS-001/ADS-001 + 38-Skill-Real-use auswerten: Nutzen/Trigger-Qualität/Overlap/Sprawl; Skill-assisted Standard/Full Prompt Mode, Opus 4.8). v1.1-Roadmap: WP-151 → WP-152 (External Validation Improvement, G-13-Weg A) → WP-153 (Project Enablement Validation) → WP-154 (Public Documentation Polish) → WP-155 (v1.1 Readiness Review) → WP-156 (v1.1 Release Prep). WP-130/131/132 bleiben optional/nicht aktiviert.

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
- WP-136: NDF Extended Skills Pack Blueprint — **GO WITH NOTES**; Extended Core Skills Pack empfohlen (4 Kern + bis 2 optional, max. 6); konzeptionelle 13-Feld-Skill-Designs, Overlap-Analyse, WP-137-Implementierungsplan; Reconciliation: WP-137 = Docs-only Extended Core Skills MVP Implementation. Keine Implementierung; `.claude/skills` unverändert; ADR-0032 unverändert.
- WP-137: Docs-only Extended Core Skills MVP Implementation — **GO WITH NOTES**; genau vier docs-only Extended-Core-Skills unter `.claude/skills/` implementiert (skill-quality-reviewer, existing-project-analysis-runner, docs-polish-runner, changelog-writer) + README-Update; keine optionalen +2; bestehende MVP-Skills unverändert; Skill-Pack nun **acht** Skills; ADR-0032 unverändert.
- WP-138: Skill Prompt Compression Real-use Validation — **GO WITH NOTES**; acht-teiliges Skill-Pack real-use-validiert; DSK-001 Closed with notes, ECS-001 Partially closed; Skills-first Standard-Default bestätigt; keine neuen/geänderten Skills; ADR-0032 unverändert.
- WP-139: v1.0 Gap Review & Scope Lock — **GO WITH NOTES – v1.0 scope lock candidate**; 18 Bereiche (9 Met, 8 Met with notes, 1 tracked Gap G-13, keine Blocker); Scope Lock als Kandidat empfohlen; achtteiliges Skill-Pack reicht für v1.0-Core; ADR-0031/0032 stabil; keine v1.0-Aktivierung/RC.
- WP-140: External Validation Evidence Review — **GO WITH NOTES**; G-13 **Partially closed / tracked for RC**; Evidence-Matrix (9 Quellen: 2 strong, 5 moderate, 1 limited); zwei unabhängige Läufe (WP-074/WP-088, PASS WITH NOTES); RC can proceed with notes; keine erfundene Evidenz; ADR-0031/0032 unverändert.
- WP-141: v1.0 Release Criteria Finalization — **GO WITH NOTES**; RC-Kriterien RC-01…13 und Final-Kriterien F-01…07 getrennt; Allowed RC Notes + Final Blockers definiert; G-13-Schwelle (RC mit Notes; v1.0 final Weg A/B); achtteiliges Skill-Pack reicht für v1.0-Core; keine v1.0-Aktivierung/RC.
- WP-142: v1.0 RC Readiness Review — **GO WITH NOTES – ready for v1.0 RC Release Prep**; RC-Kriterien RC-01…13 (9 Met, 4 Met with notes, 0 Gaps, 0 Blocker); Allowed RC Notes accepted; keine RC-blockierenden Final Blocker; Skill-Pack RC-tauglich; keine v1.0-Aktivierung/RC.
- WP-143: v1.0 RC Release Prep — **GO WITH NOTES – v1.0 RC prepared, pending Human Maintainer release**; `v1.0.0-rc.1` als Doku vorbereitet (RC Release Notes/Go-No-Go/Tagging-Guide); kein Tag/Release durch Claude; Known RC Notes sichtbar; RC-01/RC-10 auf RC-Commit erneut zu bestätigen.
- WP-144: v1.0 RC Post-Release Review — **GO WITH NOTES – RC published and post-release triage started**; Human Maintainer hat annotated Tag `v1.0.0-rc.1` (→ `4beab84`) veröffentlicht; RC-01/RC-10 read-only bestätigt; G-13 requires final action → Final-Weg C empfohlen; noch kein externes RC-Feedback; kein v1.0 final.
- WP-145: Remaining Docs-only Skills Pack Implementation — **GO WITH NOTES**; 22 neue docs-only Advisory-Skills; Skill-Pack 30 Skills; bestehende 8 unverändert; RC unverändert; kein v1.0 final. Final Readiness → WP-146.
- WP-146: Additional Docs-only Skills Pack Implementation — **GO WITH NOTES**; 8 neue docs-only Advisory-Skills; Skill-Pack **38 Skills**; bestehende 30 unverändert; RC unverändert; kein v1.0 final. Final Readiness → WP-147.
- WP-147: v1.0 Final Readiness Review — **GO WITH NOTES – ready for v1.0 Final Release Prep**; F-01…F-07 (6 Met with notes, F-03 N/A bis final, 0 Gaps, 0 Blocker); G-13-Weg C bestätigt; 38-Skill-Pack final-tauglich mit Notes; keine v1.0-Final-Aktivierung; RC unverändert.
- WP-148: v1.0 Final Release Prep — **GO WITH NOTES – v1.0 final prepared, pending Human Maintainer release**; `v1.0.0` als Doku vorbereitet (Final Release Notes/Go-No-Go/Tagging-Guide, kopierbarer Release Body); G-13-Weg C final; kein Tag/Release durch Claude; v1.x-Zusage prepared/pending; RC unverändert.
- WP-149: v1.0 Final Post-Release Review / Reconciliation — **GO WITH NOTES – v1.0 final released and reconciled**; annotated Tag `v1.0.0` (→ `9dcadc1`) als Final release durch Human Maintainer; volle v1.x-Zusage ab `v1.0.0` aktiv (ADR-0031); G-13 via Weg C reconciled; RC-Tag unverändert. **NDF ist v1.0.0 released.**
- WP-150: v1.1 Planning / Post-v1.0 Roadmap — **GO WITH NOTES – v1.1 planning started** ([v1.1 Plan](../docs/roadmap/V1_1_PLAN.md)); v1.1 = Validation, Enablement & Operational Maturity (nur geplant); Known Final Notes → Roadmap-Items (RDS-001/ADS-001 → WP-151; G-13-Weg A → WP-152; „kein RC-Feedback" teilweise adressiert durch ersten Projekt-Feedback-Intake → WP-152/153); v1.x-Kompatibilitätsgrenzen (non-breaking/needs-ADR/breaking/human-maintainer-only) dokumentiert; WP-Reihenfolge WP-151…156 (ersetzt vorläufige WP-149-Nummerierung); erster realer Projekt-Feedback-Intake neutral einbezogen; keine Breaking Changes/neue Skills/Releases; ADR-0031/0032 unverändert.

## Next Prompt Recommendation

**Skill-assisted Standard oder Full Prompt Mode** für **NDF-WP-151 – Skills Real-use Review** (RDS-001/ADS-001 + 38-Skill-Real-use: Nutzen/Trigger-Qualität/Overlap/Sprawl; empfohlenes Modell Claude Opus 4.8). v1.1-Roadmap: WP-151 → WP-152 → WP-153 → WP-154 → WP-155 → WP-156. WP-130/131/132 bleiben optional/nicht aktiviert.

## What Must Not Be Claimed

Keine Foundation-0.9-Release-Behauptung; kein v1.0; keine aktive volle v1.x-Kompatibilitätszusage; kein aktives Claude Skills Pack; keine WP-129-Aktivierung.

## What Must Not Be Included

Keine privaten Daten; keine Secrets; keine Roh-Chatlogs; keine Chain-of-Thought; keine externen Skill-Inhalte; keine riesigen Kopien.

## Update Rules

Nach jedem abgeschlossenen WP aktualisieren; nur geprüfte, öffentliche Repo-Inhalte; Compact Context Summary als Inputquelle erlaubt; ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate, kein Human-Maintainer-Review.
