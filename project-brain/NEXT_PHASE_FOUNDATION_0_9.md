# Next Phase – Foundation 0.9

## Current status

**Scope locked** (NDF-WP-121, 2026-07-08). Foundation 0.9 ist gelockt, **nicht released**, **nicht v1.0**, validation-first. Keine Skills erstellt. Verbindliche Einstufung: `docs/roadmap/FOUNDATION_0_9_SCOPE_LOCK.md`. Release-blocking: 121 (done) · 122 (Context Economy Adoption Review — **done: GO WITH NOTES**) · 123 (Prompt Modes & Context Pack Validation — **done: GO WITH NOTES**) · 124 (Optional Skills MVP Implementation Decision — **done: Option B**) · 126 (Adoption Evidence & v1.0 Path Review — **done: GO WITH NOTES**) · 127 (Release Readiness Review — **done: GO WITH NOTES**) · 128 (Release Prep — **done: release-prepared / pending manual release**, `docs/release/FOUNDATION_0_9_RELEASE_NOTES.md` + Go/No-Go + Tagging-Guide). Alle release-blocking WPs erledigt; offen nur der manuelle Tag/Release, danach WP-133. **WP-125 optional/conditional; WP-129 optional/nicht aktiviert; WP-130/131/132 optionale Assessments; WP-133 Post-Release-Kandidat.**

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

**Manuelles Go/No-Go + annotated Tag `v0.9.0-foundation` + GitHub Pre-Release durch den Human Maintainer** (WP-128 Release Prep abgeschlossen, release-prepared / pending manual release). Danach **NDF-WP-133 – Foundation 0.9 Post-Release Status Cleanup**. WP-125 optional (nur auf Human-Maintainer-Wunsch); WP-129 optional, nicht aktiviert; WP-130/131/132 optional. Nächste freie ADR-Nummer: 0033. Kein v1.0, keine aktive volle v1.x-Zusage, keine aktiven Skills.
