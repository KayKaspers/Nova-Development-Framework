# Project Brain – WP-107 Foundation 0.8 Planning Notes

## Summary

Foundation-0.8-Planung erstellt: Arbeitstitel **Agent Enablement & Context Economy**, Kandidaten-Work-Packages (107–115 + optional 116–118), Release-Criteria-Draft, MVP-Skill-Set nur als Design, Brain-Notes. **Kein Scope Lock, kein Release, kein v1.0, kein Skill Pack erstellt.** Empfehlung: **GO WITH NOTES** (Scope Lock in WP-108 muss die blocking/optional-Trennung treffen).

## Inputs reviewed

Foundation-0.7-Abschlussdokumente (README, CHANGELOG, 0.7-Release-Notes/Criteria/Plan/Queue, NEXT_PHASE_0_7, WP-106-Brain-Notiz); ADR-0031; V1_0_PATH_SUMMARY; V1_0_READINESS_CRITERIA_DRAFT. Gate strict/self-test.

## Foundation 0.7 closure status

Released/published als `v0.7.0-foundation` (2026-07-08), WP-106 abgeschlossen, keine offenen 0.7-blocking Follow-ups. Known Limitations bleiben sichtbar; Agent Enablement/Context Economy war dort ausschließlich Future Candidate. Kein v1.0-Claim, keine aktive volle v1.x-Zusage — bestätigt.

## Foundation 0.8 working title

**Foundation 0.8 – Agent Enablement & Context Economy.** Kontrollierte, docs-getriebene NDF-Erweiterung; kein großer Feature-Release.

## Proposed goals

Context Economy als Prinzip; Context Packs + Compact Context Summary standardisieren; kleines public-neutrales Claude Skills Pack MVP (nur Design); Skill Security Policy (fail closed, Human-Gates); Skill Review Checklist; Skill-vs-Prompt-vs-Workflow-Kriterien; Release Safety; keine autonome Git-/Release-Aktion durch Skills.

## Candidate WPs

Blocking-Kandidaten: 108 Scope Lock, 109 Context Economy Concept, 110 Skill Security Policy, 111 Skills MVP Design, 112 Skills MVP Implementation, 113 Context Pack Template & Prompt Modes, 114 Readiness, 115 Release Prep. Optional: 116 Skill-to-Cursor-Export-Assessment, 117 Workflow-Builder-Evaluation, 118 Docs-Polish-Skill-Evaluation. Finale Trennung erst in WP-108.

## Proposed MVP skill set

Nur geplant, nicht erstellt: `ndf-token-economy`, `ndf-feedback-to-nova`, `ndf-work-package-runner`, `ndf-public-neutrality-guard`, `ndf-release-safety`, `ndf-adr-governance`. Optional später: `ndf-evidence-review`, `ndf-skill-builder`, `ndf-workflow-builder`, `ndf-docs-polish`, `ndf-cursor-rules-export`. Pflichtregeln: docs-only zuerst, keine Scripts ohne Scope-Lock, keine Netz/Secrets/privaten Infos, keine Git-Schreibaktionen, Human-Gates, Rückmeldung an Nova + Compact Context Summary.

## What was not done

Kein Scope Lock; keine Skills/`.claude/skills`/Cursor-Rules/Workflows/Scripts erstellt; keine Drittanbieter-Skills importiert; kein Commit/Push/Tag/Release; keine CI-/Script-Änderung; kein v1.0-Claim; keine aktive volle v1.x-Zusage; Foundation 0.8 nirgends als scope-locked oder released dargestellt.

## Risks

Scope Creep (Kandidatenliste verleitet zur Überladung) → WP-108 muss den blocking Kern klein halten. Skills-Security-Risiko (Skills mit Schreib-/Netzrechten) → Security Policy (WP-110) fail closed, docs-only zuerst. Missverständnis „Skill Pack existiert" → überall als geplant/kandidierend markiert. Ein-Personen-Engpass unverändert.

## Recommendation

**GO WITH NOTES** — Planung sauber; WP-108 Scope Lock muss entscheiden, was wirklich blocking wird (insb. WP-112 Implementierung und docs-only-vs-scripts).

## Compact Context Summary

Foundation 0.8 **Planning** (WP-107) erstellt: Arbeitstitel „Agent Enablement & Context Economy". 0.7 released (`v0.7.0-foundation`, 2026-07-08, WP-106). Kandidaten-WPs 108–115 (+optional 116–118); Release-Criteria-Draft; MVP-Skill-Set nur als Design (`ndf-token-economy`, `-feedback-to-nova`, `-work-package-runner`, `-public-neutrality-guard`, `-release-safety`, `-adr-governance`). Nicht scope-locked, nicht released, kein v1.0, kein Skill Pack erstellt. Security: docs-only zuerst, keine Git-/Release-/Netz-/Secret-Zugriffe, Human-Gates. Nächster Schritt: WP-108 Scope Lock. Nächste freie ADR-Nummer 0032 (Skill Security Policy ADR-0032-Kandidat).
