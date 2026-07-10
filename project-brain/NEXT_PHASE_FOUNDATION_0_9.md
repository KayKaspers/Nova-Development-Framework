# Next Phase – Foundation 0.9

## Current status

**Released / published — reconciliation documented** als `v0.9.0-foundation` (2026-07-10, NDF-WP-133). Foundation 0.9 ist veröffentlicht, **nicht v1.0**, kein v1.0 RC, keine aktive volle v1.x-Zusage, kein aktives Skill Pack, validation-first. Release-blocking (alle done): 121 · 122 (GO WITH NOTES) · 123 (GO WITH NOTES) · 124 (Option B) · 126 (GO WITH NOTES) · 127 (GO WITH NOTES) · 128 (Release Prep) · 133 (Post-Release Reconciliation Cleanup, released/published). **Reconciliation:** Tag-Cut bei WP-126 (`e735041`); WP-127/128 nach dem Tag committet (`b268503`), Tag nicht verschoben, kein History-Rewrite, kein Korrektur-Release. **WP-125 optional/conditional (nächster empfohlener Blueprint); WP-129 optional/nicht aktiviert; WP-130/131/132 optionale Assessments.**

## Working title

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Zuerst Adoption/Validation der 0.8-Artefakte, dann optionale Enablement-Entscheidungen — kein großer Feature-Sprung.

## Foundation 0.8 baseline

Foundation 0.8 released als `v0.8.0-foundation` (2026-07-08, WP-119); vollständig abgeschlossen, keine offenen Follow-ups. Lieferte Context Economy, Skill Security Policy (ADR-0032), Skills-MVP-**Design** (kein aktives Pack), Prompt Modes, Context Pack Template. Optional/nicht aktiviert: WP-112/116/117/118. Nächste freie ADR-Nummer: 0033.

## Proposed goals

0.8-Artefakte praktisch validieren; Context Packs + Prompt Modes prüfen; Adoption Evidence für Context Economy sammeln; Skills-MVP-Design gegen optionale Umsetzung prüfen; Entscheidungskorridor für WP-112/docs-only Skills-Implementierung; optionale Cursor-Export-/Workflow-Builder-Assessments; v1.0-Pfad mit Evidence stärken; Scope klein halten.

## Candidate WPs

121 Scope Lock · 122 Context Economy Adoption Review · 123 Prompt Modes & Context Pack Validation · 124 Optional Skills MVP Implementation Decision · 125 Skills MVP Implementation Blueprint · 126 Adoption Evidence & v1.0 Path Review · 127 Readiness · 128 Release Prep.

## Optional candidates

129 docs-only Skills MVP Implementation (nur wenn WP-124 befürwortet + WP-121 scoped) · 130 Skill-to-Cursor-Export-Assessment · 131 Workflow-Builder-Evaluation · 132 Docs-Polish-Skill-Evaluation · 133 Post-Release Status Cleanup.

## Known constraints

Public Quality Gate v0.2 Pflicht; ADR-0032 bindend (fail closed, docs-only zuerst, keine Scripts/Netz/Secrets/privaten Daten/autonomen Git-Release-Aktionen; Human-Maintainer-Kontrolle). **Optional Enablement = zuerst Bewertung/Entscheidung, Implementierung nie automatisch.** Kein aktives Skill Pack; keine Chain-of-Thought; kein v1.0-Claim; keine aktive volle v1.x-Zusage; keine Drittanbieter-Skill-Inhalte. Nächste freie ADR-Nummer: 0033.

## Next WP

**Foundation 0.9 ist released / published** als `v0.9.0-foundation` (2026-07-10; annotated Tag → `e735041`, GitHub Pre-Release; WP-133 Reconciliation abgeschlossen). Keine offenen 0.9-blocking Follow-ups. **NDF-WP-125** (Blueprint), **NDF-WP-129** (Docs-only Skills MVP Implementation) und **NDF-WP-134** (Skills-first Operating Mode & Prompt Compression Validation) sind erledigt (alle GO WITH NOTES): vier docs-only MVP-Skills liegen unter `.claude/skills/`; der [Skills-first Operating Mode](../docs/validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md) ist dokumentiert (Standard Prompt Mode als Default, Full für kritische Fälle), Prompt-Kompression validiert, **DSK-001 Partially closed**. **NDF-WP-135** (External Skills Landscape), **NDF-WP-136** (Extended Skills Pack Blueprint), **NDF-WP-137** (Docs-only Extended Core Skills MVP Implementation) und **NDF-WP-138** (Skill Prompt Compression Real-use Validation) sind erledigt (alle GO WITH NOTES). Das Skill-Pack umfasst **acht** docs-only Skills; WP-138 hat den realen Prompt-Kompressionsnutzen validiert (~40–65 % je Prompt-Typ), **DSK-001 Closed with notes**, **ECS-001 Partially closed**, Skills-first Standard-Default bestätigt. **NDF-WP-139** (v1.0 Gap Review & Scope Lock) und **NDF-WP-140** (External Validation Evidence Review) sind erledigt (beide GO WITH NOTES). WP-139: Scope Lock als Kandidat empfohlen (18 Bereiche, keine Blocker). WP-140: G-13 (External Validation Evidence Depth) auf **Partially closed / tracked for RC** bewertet (zwei unabhängige Läufe PASS WITH NOTES, begrenzte Schrittbeleg-Tiefe); **RC can proceed with notes**, v1.0 final braucht tiefere Evidenz oder eine dokumentierte akzeptierte Grenze. **NDF-WP-141** (v1.0 Release Criteria Finalization) ist erledigt (GO WITH NOTES): RC-Kriterien (RC-01…13) und Final-Kriterien (F-01…07) getrennt, Allowed RC Notes + Final Blockers definiert, G-13-Schwelle festgelegt (RC mit Notes; v1.0 final Weg A tieferer Lauf oder Weg B akzeptierte Grenze); [Release Criteria](../docs/release/V1_0_RELEASE_CRITERIA.md). **Nächster empfohlener Schritt: NDF-WP-142 – v1.0 RC Readiness Review** (Full/Skill-assisted Full Prompt Mode, Opus 4.8; ehrlicher Check gegen die RC-Kriterien); danach WP-143 (v1.0 RC Release Prep) → manueller RC-Release (Human Maintainer) → v1.0 Final-Pfad. Optionale Governance-/Project-Enablement-Skills bleiben Kandidaten, nicht blockierend. WP-130/131/132 bleiben optional/nicht aktiviert. Nächste freie ADR-Nummer: 0033. Kein v1.0, keine aktive volle v1.x-Zusage.
