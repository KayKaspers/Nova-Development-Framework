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

**Foundation 0.9 ist released / published** als `v0.9.0-foundation` (2026-07-10; annotated Tag → `e735041`, GitHub Pre-Release; WP-133 Reconciliation abgeschlossen). Keine offenen 0.9-blocking Follow-ups. **NDF-WP-125 – Skills MVP Implementation Blueprint** ist erledigt (GO WITH NOTES; 4-Skill-MVP empfohlen; [Blueprint](../docs/validation/foundation-0-9/SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md)). **Nächster empfohlener Schritt: NDF-WP-129 – Docs-only Skills MVP Implementation**, aber **nur bedingt** und **nicht aktiviert**: erfordert einen ausdrücklichen Human-Maintainer-Scope-Change, engen docs-only Scope (die vier MVP-Skills) und ADR-0032-Konformität. WP-130/131/132 optional. Nächste freie ADR-Nummer: 0033. Kein v1.0, keine aktive volle v1.x-Zusage, keine aktiven Skills.
