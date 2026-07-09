# Project Brain – WP-120 Foundation 0.9 Planning Notes

## Summary

Foundation-0.9-Planung erstellt: Arbeitstitel **Adoption, Validation & Optional Enablement**, Kandidaten-Work-Packages (120–128 + optional 129–133), Release-Criteria-Draft, Brain-Notes. **Kein Scope Lock, kein Release, kein v1.0, keine Skills/`.claude/skills`/Cursor-Rules/Workflows/Scripts erstellt.** Empfehlung: **GO WITH NOTES** (Scope Lock in WP-121 muss die blocking/optional-Trennung treffen).

## Inputs reviewed

Foundation-0.8-Abschlussdokumente (README, CHANGELOG, Post-Release Status, Release Notes/Criteria, Plan/Queue, NEXT_PHASE_0_8, Context Pack, WP-119-Brain-Notiz); Agent-Workflows (Context Economy, Prompt Modes, Skill Security Policy, Skills MVP Design); ADR-0031/0032 + ADR-README; V1_0_PATH_SUMMARY. Gate strict/self-test grün, Working Tree sauber (WP-119 `1ad8a90`), 0.8-Release per gh verifiziert.

## Foundation 0.8 closure status

Released/published als `v0.8.0-foundation` (2026-07-08), WP-119 abgeschlossen, keine offenen 0.8-blocking Follow-ups. WP-112/116/117/118 optional/nicht aktiviert; kein aktives Skill Pack (MVP nur Design). Kein v1.0-Claim, keine aktive volle v1.x-Zusage — bestätigt.

## Foundation 0.9 working title

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Zuerst Adoption/Validation, dann optionale Enablement-Entscheidungen; kein großer Feature-Sprung.

## Proposed goals

0.8-Artefakte validieren; Context Packs + Prompt Modes prüfen; Adoption Evidence sammeln; Skills-MVP-Design gegen optionale Umsetzung prüfen; Entscheidungskorridor WP-112/docs-only Skills-Implementierung; optionale Cursor-Export-/Workflow-Builder-Assessments; v1.0-Pfad mit Evidence stärken; Scope klein halten.

## Candidate WPs

Blocking-Kandidaten: 121 Scope Lock, 122 Context Economy Adoption Review, 123 Prompt Modes & Context Pack Validation, 124 Optional Skills MVP Implementation Decision, 125 Skills MVP Implementation Blueprint, 126 Adoption Evidence & v1.0 Path Review, 127 Readiness, 128 Release Prep. Optional: 129 docs-only Skills MVP Implementation, 130 Skill-to-Cursor-Export-Assessment, 131 Workflow-Builder-Evaluation, 132 Docs-Polish-Skill-Evaluation, 133 Post-Release Cleanup. Finale Trennung erst in WP-121.

## Optional enablement candidates

**Optional Enablement = zuerst Bewertung/Entscheidung; Implementierung nie automatisch.** WP-124 entscheidet über docs-only Skills-Implementierung (WP-129); WP-125 entwirft ggf. Blueprint gemäß ADR-0032 (keine Scripts/Netz/Secrets/privaten Daten/autonomen Git-Release-Aktionen). WP-130 (Cursor-Export) und WP-131 (Workflow-Builder) bleiben nur Assessment/Evaluation. Die 0.8-Optional-WPs (112/116/117/118) werden neu bewertet, nicht überschrieben.

## v1.0 path relationship

Foundation 0.9 stärkt den v1.0-Pfad mit Adoption-/Validation-Evidence (WP-126), behauptet aber keine v1.0-Reife und aktiviert keine volle v1.x-Zusage. V1_0_PATH_SUMMARY DE+EN aktualisiert (0.9 Planungskandidat, Adoption/Validation-Fokus). Kein v1.0-Claim.

## What was not done

Kein Scope Lock; keine Skills/`.claude/skills`/`SKILL.md`/Cursor-Rules/Workflows/Scripts erstellt; keine Drittanbieter-Skills importiert; keine WP-129/130/131/132-Aktivierung; kein Commit/Push/Tag/Release; keine CI-/Script-Änderung; kein v1.0-Claim; Foundation 0.9 nirgends als scope-locked oder released dargestellt.

## Risks

Scope Creep (Kandidatenliste, insb. Skills-Implementierung) → WP-121 muss den blocking Kern klein halten und Optional-Enablement-Grenze wahren. Missverständnis „Skills werden umgesetzt" → überall als „zuerst Bewertung/Entscheidung, nie automatisch" markiert. Doppelung mit 0.8-Optional-WPs → explizit als Neu-Bewertung (nicht Überschreiben) dokumentiert. Ein-Personen-Engpass unverändert.

## Recommendation

**GO WITH NOTES** — Planung sauber und neutral; WP-121 Scope Lock muss entscheiden, was wirklich blocking wird (insb. WP-124/125/129 und die Adoption-Evidence-Tiefe).

## Compact Context Summary

Foundation 0.9 **Planning** (WP-120) erstellt: Arbeitstitel „Adoption, Validation & Optional Enablement". 0.8 released (`v0.8.0-foundation`, 2026-07-08, WP-119). Kandidaten-WPs 121–128 (+optional 129–133); Release-Criteria-Draft. Fokus: Adoption/Validation der 0.8-Artefakte zuerst, dann optionale Enablement-Entscheidungen (Skills-Implementierung/Cursor-Export/Workflow-Builder) — Implementierung nie automatisch, ADR-0032 bindend. Nicht scope-locked, nicht released, kein v1.0, keine Skills erstellt. Nächster Schritt: WP-121 Scope Lock. Nächste freie ADR-Nummer 0033. Kein aktives Skill Pack.
