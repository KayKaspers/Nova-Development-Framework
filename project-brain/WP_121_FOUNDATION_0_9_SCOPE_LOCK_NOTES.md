# Project Brain – WP-121 Foundation 0.9 Scope Lock Notes

## Summary

Foundation-0.9-Scope verbindlich gelockt: gesperrter Kernfokus **Adoption Review + Prompt/Context Validation + Optional Skills Decision + v1.0 Evidence Review** (validation-first). Release-blocking: 121/122/123/124/126/127/128. **WP-124 ist release-blocking (nur Entscheidung); WP-125 optional/conditional; WP-129 optional/nicht aktiviert.** Kein Skill Pack/Script/`.claude/skills`. Kein Release, kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

FOUNDATION_0_9_PLAN/WORK_PACKAGES/RELEASE_CRITERIA, NEXT_PHASE_0_9, WP-120-Brain-Notiz; Foundation-0.8 Post-Release Status + Context Pack; Agent-Workflows (Context Economy, Prompt Modes, Skill Security Policy, Skills MVP Design); ADR-0031/0032/README; README, CHANGELOG, V1_0_PATH_SUMMARY. Gate strict/self-test grün, Working Tree sauber (WP-120 `05198ee`), 0.8-Release per gh verifiziert.

## Scope decision

Validation-first: zuerst prüfen (Adoption/Validation), dann optionale Enablement-Entscheidungen; tatsächliche Skill-Implementierung bewusst nachgelagert und nicht durch den Scope Lock aktiviert.

## Release-blocking WPs

121 Scope Lock (Gate, done) · 122 Context Economy Adoption Review (nächster Schritt) · 123 Prompt Modes and Context Pack Validation · 124 Optional Skills MVP Implementation Decision (nur Entscheidung) · 126 Adoption Evidence and v1.0 Path Review · 127 Readiness · 128 Release Prep.

## Optional / conditional WPs

125 Skills MVP Implementation Blueprint (conditional auf WP-124) · 129 Docs-only Skills MVP Implementation (optional, nicht aktiviert) · 130 Skill-to-Cursor-Export-Assessment · 131 Workflow-Builder-Evaluation · 132 Docs-Polish-Skill-Evaluation · 133 Post-Release Status Cleanup (Post-Release-Kandidat).

## Deferred / Non-Goals

Aktives Skill Pack per Default; `.claude/skills` per Default; Skills-Implementierung ohne Human-Maintainer-Scope-Change; Scripts in Skills; netzwerkfähige Skills; Git-Schreib-/Release-/Tag-Aktionen durch Skills; Cursor-Rules-Implementierung; Workflow-Implementierung; Drittanbieter-Skill-Import; private projektspezifische Skills; v1.0 RC; Aktivierung der vollen v1.x-Zusage.

## Decision on WP-124

**Release-blocking.** Die Entscheidung ist wertvoll und keine Implementierung; sie klärt, ob WP-125/WP-129 später sinnvoll sind, und verhindert stille Skill-Aktivierung. Liefert begründete Empfehlung (priorisieren/optional/verwerfen), keine `.claude/skills`.

## Decision on WP-125

**Optional / conditional.** Blueprint nur, wenn WP-124 eine spätere Implementierung empfiehlt; nicht zwingend für den 0.9-Release; kein Blueprint vor der WP-124-Entscheidung; kein Implementation Scope — Design/Blueprint gemäß ADR-0032.

## Decision on WP-129

**Optional, nicht release-blocking, nicht durch WP-121 aktiviert.** Höheres Risiko als Adoption/Validation; ADR-0032 fail closed. Reihenfolge: Entscheidung (124) → ggf. Blueprint (125) → ggf. separate ausdrückliche Aktivierung (129). Keine stille `.claude/skills`-Erstellung; strikt docs-only + ADR-0032.

## Foundation 0.8 optional WP classification

WP-112/116/117/118 bleiben 0.8-Optional-Kandidaten, nicht aktiviert; Themen über neue 0.9-Kandidaten neu bewertbar; alte Nummern nicht wiederverwendet/überschrieben/still reaktiviert. Zuordnung: 112 → 124/125/129; 116 → 130; 117 → 131; 118 → 132.

## Security boundaries

Gemäß ADR-0032: keine aktiven Skills ohne ausdrücklichen Scope; keine Scripts/Netz/Secrets/privaten Daten; keine autonomen Commit-/Push-/Tag-/Release-Aktionen; kein Drittanbieter-Skill-Import; Public Quality Gate + Public Neutrality Pflicht; jede spätere Skill-Umsetzung strikt docs-only + ADR-0032. Human Maintainer finaler Owner.

## Change control

Kein neues release-blocking WP ohne expliziten Scope-Change; keine Skills-Implementierung ohne ausdrückliche Human-Maintainer-Entscheidung; keine `.claude/skills` ohne explizite Aktivierung eines Implementierungs-WP; keine Scripts ohne spätere ADR-/Scope-Entscheidung; keine Netz/Git-Writes/Release-Tag; kein Drittanbieter-Skill-Import; optionale WPs bleiben optional bis Human-Maintainer-Upgrade; kein v1.0; keine Release Prep vor WP-127; redaktionelle Korrekturen sind keine Scope-Änderung.

## Impact on v1.0 path

Foundation 0.9 stärkt den v1.0-Pfad mit Adoption-/Validation-Evidence (WP-126), behauptet aber keine v1.0-Reife und aktiviert keine volle v1.x-Zusage. V1_0_PATH_SUMMARY DE+EN aktualisiert (0.9 scope-locked, validation-first, kein v1.0). Kein v1.0-Claim.

## What was not done

Keine Skills/`.claude/skills`/`SKILL.md`/Cursor-Rules/Workflows/Scripts erstellt; keine WP-125/129/130/131/132-Aktivierung; keine 0.8-Optional-WP-Reaktivierung; kein Commit/Push/Tag/Release; keine CI-/Script-Änderung; kein v1.0-Claim; Foundation 0.9 nirgends als released dargestellt.

## Risks

Scope Creep (Skills-Implementierung) → blocking Kern klein, WP-124 nur Entscheidung, WP-129 nicht aktiviert. Missverständnis „Skills werden umgesetzt" → überall als „zuerst Entscheidung, nie automatisch" markiert; klare WP-124→125→129-Reihenfolge. Doppelung mit 0.8-Optional-WPs → explizit als Neu-Bewertung (nicht Überschreiben) dokumentiert.

## Recommendation

**GO WITH NOTES** — Scope sauber und validation-first gelockt; bewusste Notes: WP-124 nur Entscheidung, WP-125 conditional, WP-129 optional/nicht aktiviert; Adoption Evidence folgt in WP-122/123/126.

## Compact Context Summary

Foundation 0.9 **scope-locked** (WP-121, 2026-07-08): validation-first, Kern Adoption Review + Prompt/Context Validation + Optional Skills Decision + v1.0 Evidence Review. Release-blocking 121/122/123/124/126/127/128; **WP-124 release-blocking (nur Entscheidung), WP-125 optional/conditional, WP-129 optional/nicht aktiviert**, WP-130/131/132 optionale Assessments, WP-133 Post-Release-Kandidat. 0.8-Optional-WPs (112/116/117/118) neu bewertbar, nicht überschrieben. ADR-0032 bindend (keine Skills/Scripts/Netz/autonomen Git-Release-Aktionen ohne ausdrücklichen Scope). 0.8 released. Nächster Schritt WP-122. Nächste freie ADR-Nummer 0033. Kein Release, kein v1.0, kein aktives Skill Pack.
