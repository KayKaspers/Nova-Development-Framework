# Foundation 0.9 Plan

## DE – Zweck

Dieser Plan sammelt die Kandidaten für Foundation 0.9 (Ergebnis von NDF-WP-120). **Status-Update: released / published — reconciliation documented** (NDF-WP-133, 2026-07-10; `v0.9.0-foundation`, [Post-Release Reconciliation Notes](../../project-brain/WP_133_FOUNDATION_0_9_POST_RELEASE_RECONCILIATION_CLEANUP_NOTES.md)) — verbindliche Einstufung: [FOUNDATION_0_9_SCOPE_LOCK.md](FOUNDATION_0_9_SCOPE_LOCK.md). Release-blocking waren nur 121, 122 (Context Economy Adoption Review — **erledigt: GO WITH NOTES**, [Adoption Review](../validation/context-economy/CONTEXT_ECONOMY_ADOPTION_REVIEW.md)), 123 (Prompt Modes & Context Pack Validation — **erledigt: GO WITH NOTES**, [Validation](../validation/context-economy/PROMPT_MODES_CONTEXT_PACK_VALIDATION.md)), 124 (Optional Skills MVP Implementation Decision — **erledigt: Option B, Blueprint-first/implementation-not-activated**, [Decision](../agent-workflows/NDF_SKILLS_MVP_IMPLEMENTATION_DECISION.md)), 126 (Adoption Evidence & v1.0 Path Review — **erledigt: GO WITH NOTES**, [Review](../validation/foundation-0-9/ADOPTION_EVIDENCE_AND_V1_0_PATH_REVIEW.md)), 127 (Release Readiness Review — **erledigt: GO WITH NOTES**, [Readiness Review](../release/FOUNDATION_0_9_READINESS_REVIEW.md)), 128 (Release Prep — **erledigt**, [Release Notes](../release/FOUNDATION_0_9_RELEASE_NOTES.md) + Go/No-Go + Tagging-Guide). **Reconciliation-Hinweis:** Tag-Cut lag bei WP-126 (Commit `e735041`); WP-127/WP-128 wurden **nach** dem Tag committet (`b268503`), der Tag wurde nicht verschoben (kein History-Rewrite, kein Korrektur-Release). **WP-125 optional/conditional — erledigt (Blueprint, GO WITH NOTES, [Blueprint](../validation/foundation-0-9/SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md)); WP-129 — erledigt (Docs-only Skills MVP implementiert, GO WITH NOTES, [Validation](../validation/foundation-0-9/DOCS_ONLY_SKILLS_MVP_VALIDATION.md); vier docs-only MVP-Skills, keine Extended Skills, ADR-0032-konform); WP-134 — erledigt (Skills-first Operating Mode & Prompt Compression Validation, GO WITH NOTES, [Operating Mode](../validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md); DSK-001 Partially closed); WP-135 — erledigt (External Skills Landscape & Prioritization, GO WITH NOTES, [Landscape](../validation/foundation-0-9/EXTERNAL_SKILLS_LANDSCAPE_AND_PRIORITIZATION.md); Skill-Roadmap 136→v1.0, keine Übernahme fremder Skills); WP-136 — erledigt (Extended Skills Pack Blueprint, GO WITH NOTES, [Blueprint](../validation/foundation-0-9/EXTENDED_SKILLS_PACK_BLUEPRINT.md); 4-Kern-Extended-Pack empfohlen, keine Implementierung); WP-137 — erledigt (Docs-only Extended Core Skills MVP Implementation, GO WITH NOTES, [Validation](../validation/foundation-0-9/EXTENDED_CORE_SKILLS_MVP_VALIDATION.md); vier Extended-Core-Skills implementiert, Skill-Pack nun acht Skills, keine optionalen +2); WP-138 — erledigt (Skill Prompt Compression Real-use Validation, GO WITH NOTES, [Validation](../validation/foundation-0-9/SKILL_PROMPT_COMPRESSION_REAL_USE_VALIDATION.md); reale Prompt-Reduktion ~40–65 %, DSK-001 Closed with notes, ECS-001 Partially closed; empfiehlt v1.0 Gap Review); WP-139 — erledigt (v1.0 Gap Review & Scope Lock, GO WITH NOTES – v1.0 scope lock candidate, [Gap Review](../validation/v1-0/V1_0_GAP_REVIEW_AND_SCOPE_LOCK.md); 9 Met / 8 Met with notes / 1 tracked Gap / keine Blocker; nächste WPs 140→143 Richtung v1.0 RC, keine v1.0-Aktivierung); WP-140 — erledigt (External Validation Evidence Review, GO WITH NOTES, [Evidence Review](../validation/v1-0/EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md); G-13 Partially closed / tracked for RC, RC can proceed with notes, v1.0 final braucht tiefere Evidenz oder dokumentierte Grenze); WP-141 — erledigt (v1.0 Release Criteria Finalization, GO WITH NOTES, [Release Criteria](../release/V1_0_RELEASE_CRITERIA.md); RC-Kriterien RC-01…13 und Final-Kriterien F-01…07 getrennt, G-13-Schwelle festgelegt, keine v1.0-Aktivierung/RC); WP-142 — erledigt (v1.0 RC Readiness Review, GO WITH NOTES – ready for v1.0 RC Release Prep, [RC Readiness](../validation/v1-0/V1_0_RC_READINESS_REVIEW.md); 9 Met / 4 Met with notes / 0 Gaps / 0 Blocker, Allowed RC Notes accepted, keine RC-blockierenden Final Blocker); WP-143 — erledigt (v1.0 RC Release Prep, GO WITH NOTES – v1.0 RC prepared, pending Human Maintainer release, [RC Release Notes](../release/V1_0_RC_1_RELEASE_NOTES.md); `v1.0.0-rc.1` als Doku vorbereitet, kein Tag/Release durch Claude, nicht final v1.0); WP-144 — erledigt (v1.0 RC Post-Release Review, GO WITH NOTES – RC published and post-release triage started, [Post-Release Review](../validation/v1-0/V1_0_RC_POST_RELEASE_REVIEW.md); Human Maintainer hat annotated Tag `v1.0.0-rc.1` → `4beab84` veröffentlicht, RC-01/RC-10 read-only bestätigt, G-13 Final-Weg C empfohlen, kein RC-Feedback bisher); WP-145 — erledigt (Remaining Docs-only Skills Pack Implementation, GO WITH NOTES – remaining docs-only skills implemented, [Validation](../validation/v1-0/REMAINING_DOCS_ONLY_SKILLS_PACK_VALIDATION.md); 22 neue Advisory-Skills, Skill-Pack nun 30 Skills, RC unverändert, Final Readiness → WP-146); WP-130/131/132 optionale Assessments.** Foundation 0.9 ist **veröffentlicht, aber nicht v1.0**, kein v1.0 RC, keine aktive volle v1.x-Zusage; validation-first. Kein aktives Skill Pack.

## EN – Purpose

This plan collects the candidates for Foundation 0.9 (result of NDF-WP-120). It is **not a scope lock** — the scope only becomes binding with NDF-WP-121. Foundation 0.9 is **not scope-locked**, **not released**, and **not v1.0**. **No skills, `.claude/skills`, Cursor rules, workflows, or scripts** are created in this WP.

## DE – Arbeitstitel

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Nur Arbeitstitel — der Scope Lock (WP-121) bestätigt oder ändert ihn. Foundation 0.9 ist **nicht v1.0** und kein v1.0 Release Candidate.

## EN – Working Title

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Working title only — the scope lock (WP-121) confirms or changes it. Foundation 0.9 is **not v1.0** and no v1.0 release candidate.

## DE – Ausgangslage

Foundation 0.8 ist als `v0.8.0-foundation` veröffentlicht (2026-07-08), vollständig abgeschlossen (WP-119), keine offenen 0.8-blocking Follow-ups. Foundation 0.8 brachte Context Economy, die Skill Security Policy (ADR-0032), das Claude-Skills-Pack-MVP-**Design** (kein aktives Pack), die Prompt Modes (Full/Standard/Short) und das Context Pack Template. Optional/nicht aktiviert: WP-112 (Skills MVP Implementation), WP-116 (Skill-to-Cursor-Export-Assessment), WP-117 (Workflow-Builder-Evaluation), WP-118 (Docs-Polish-Skill-Evaluation). Nächste freie ADR-Nummer: **ADR-0033**.

## EN – Background

Foundation 0.8 is published as `v0.8.0-foundation` (2026-07-08), fully complete (WP-119), no open 0.8-blocking follow-ups. It delivered context economy, the skill security policy (ADR-0032), the Claude skills pack MVP **design** (no active pack), the prompt modes (Full/Standard/Short), and the context pack template. Optional/not activated: WP-112/116/117/118. Next free ADR number: ADR-0033.

## DE – Ziele

1. Foundation-0.8-Artefakte in der praktischen Nutzung validieren.
2. Context Packs und Prompt Modes auf Verständlichkeit und Sicherheit prüfen.
3. Adoption Evidence für Context Economy sammeln und dokumentieren.
4. Skill Security Policy und Skills MVP Design gegen eine optionale Umsetzung prüfen.
5. Einen Entscheidungskorridor für WP-112 / eine docs-only Skills-MVP-Implementierung vorbereiten.
6. Optionale Assessments für Cursor-Rules-Export und Workflow-Builder planen.
7. Den v1.0-Pfad mit Evidence-/Validation-Notes stärken — ohne v1.0 zu behaupten.
8. Scope klein halten und Feature Creep vermeiden.

## EN – Goals

(1) Validate the Foundation 0.8 artifacts in practical use; (2) check context packs and prompt modes for clarity and safety; (3) collect and document adoption evidence for context economy; (4) test the skill security policy and skills MVP design against an optional implementation; (5) prepare a decision corridor for WP-112 / a docs-only skills MVP implementation; (6) plan optional assessments for Cursor-rules export and a workflow builder; (7) strengthen the v1.0 path with evidence/validation notes — without claiming v1.0; (8) keep scope small and avoid feature creep.

## DE – Nicht-Ziele

- Keine v1.0-Release-Vorbereitung, kein v1.0 Release Candidate, keine aktive volle v1.x-Kompatibilitätszusage.
- Keine Skill-Implementierung in WP-120; keine `.claude/skills` in WP-120.
- Keine Cursor Rules; keine Workflows; keine Scripts.
- Keine Git-/Release-Automation; keine Drittanbieter-Skill-Imports.
- Keine privaten Projektadapter; Neutralität bleibt Invariante.

## EN – Non-Goals

No v1.0 release prep, release candidate, or active full v1.x compatibility promise; no skill implementation or `.claude/skills` in WP-120; no Cursor rules, workflows, or scripts; no git/release automation or third-party skill imports; no private project adapters.

## DE – Vorgeschlagener Scope

Foundation 0.9 soll **kein großer Feature-Sprung** werden, sondern zuerst **Adoption und Validation**: prüfen, ob die 0.8-Artefakte in echten WPs helfen, bevor optionales Enablement (docs-only Skills-Implementierung, Cursor-Export-Assessment, Workflow-Builder-Evaluation) überhaupt entschieden wird. Bewährtes Muster wie 0.4–0.8: kleiner blocking Kern, optionale Kandidaten ehrlich als optional geführt, deferred Themen sichtbar. Die verbindliche blocking/optional/deferred-Trennung entsteht erst in WP-121.

## EN – Proposed Scope

Foundation 0.9 should be **not a large feature jump** but first **adoption and validation**: check whether the 0.8 artifacts help in real WPs before any optional enablement (docs-only skills implementation, Cursor-export assessment, workflow-builder evaluation) is even decided. Same pattern as 0.4–0.8. The binding blocking/optional/deferred split happens only in WP-121.

## DE – Vorgeschlagene Work Packages

Vollständige Kandidatenliste: [FOUNDATION_0_9_WORK_PACKAGES.md](FOUNDATION_0_9_WORK_PACKAGES.md). Kern-Kandidaten: WP-121 (Scope Lock), WP-122 (Context Economy Adoption Review), WP-123 (Prompt Modes & Context Pack Validation), WP-124 (Optional Skills MVP Implementation Decision), WP-125 (Skills MVP Implementation Blueprint), WP-126 (Adoption Evidence & v1.0 Path Review), WP-127/128 (Readiness/Prep). Optional: WP-129 (docs-only Skills MVP Implementation), WP-130 (Skill-to-Cursor-Export-Assessment), WP-131 (Workflow-Builder-Evaluation), WP-132 (Docs-Polish-Skill-Evaluation), WP-133 (Post-Release Status Cleanup).

## EN – Proposed Work Packages

Full candidate list in the work package candidates document. Core: WP-121/122/123/124/125/126/127/128. Optional: WP-129/130/131/132/133.

## DE – Adoption und Validation

Der erste Teil des Arbeitstitels: WP-122 prüft, ob Context Economy in echten WPs hilft (Adoption Review); WP-123 validiert Prompt Modes + Context Pack Template auf Verständlichkeit und Sicherheit; WP-126 sammelt belastbare Adoption-/Validation-Evidence für den v1.0-Pfad. Ziel ist ehrliche Evidenz, keine Behauptung.

## EN – Adoption and Validation

The first half of the title: WP-122 checks whether context economy helps in real WPs; WP-123 validates prompt modes + context pack template for clarity and safety; WP-126 collects robust adoption/validation evidence for the v1.0 path. The goal is honest evidence, not a claim.

## DE – Optional Enablement

**Optional Enablement heißt: zuerst Bewertung oder Entscheidung. Implementierung ist nie automatisch.** WP-124 entscheidet, ob eine docs-only Skills-MVP-Implementierung (WP-129) sinnvoll ist; WP-125 entwirft — falls gescopt — einen Implementation Blueprint. Jede spätere Implementierung muss ADR-0032 einhalten (keine Scripts, keine Netzwerkzugriffe, keine Secrets, keine privaten Projektdaten, keine autonomen Git-/Release-/Tag-Aktionen, Human-Maintainer-Kontrolle). Cursor-Rules-Export (WP-130) und Workflow-Builder (WP-131) bleiben **nur Assessment/Evaluation**, bis ein späterer Scope Lock anders entscheidet — in WP-120 werden keine Cursor Rules und keine Workflows erzeugt.

## EN – Optional Enablement

**Optional enablement means evaluation or decision first. Implementation is never automatic.** WP-124 decides whether a docs-only skills MVP implementation (WP-129) is worthwhile; WP-125 drafts an implementation blueprint if scoped. Any later implementation must obey ADR-0032 (no scripts, network, secrets, private project data, or autonomous git/release/tag actions; human-maintainer control). Cursor-rules export (WP-130) and workflow builder (WP-131) stay **assessment/evaluation only** until a later scope lock decides otherwise — no Cursor rules or workflows are created in WP-120.

## DE – Sicherheits- und Neutralitätsregeln

Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflichtinvariante. ADR-0032 (Skill Security Policy) bleibt bindend für alle Skill-bezogenen WPs. Keine privaten Namen/Suchmuster/Domains/Kontakte; der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden, der Wert nie. Kein aktives Skill Pack; keine Chain-of-Thought.

## EN – Security and Neutrality Rules

Public quality gate v0.2 stays a mandatory invariant. ADR-0032 stays binding for all skill-related WPs. No private names/patterns/domains/contacts; naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed, its value never. No active skill pack; no chain-of-thought.

## DE – Beziehung zu Foundation 0.8

Foundation 0.9 ist additiv und baut auf 0.8 auf: es validiert und operationalisiert die dort geschaffenen Artefakte (Context Economy, Prompt Modes, Context Packs, Skill Security Policy, Skills MVP Design), ohne sie zu ändern. Foundation 0.8 bleibt released; die 0.8-Optional-WPs (112/116/117/118) können durch 0.9-Kandidaten neu bewertet werden, werden aber nicht überschrieben.

## EN – Relationship to Foundation 0.8

Foundation 0.9 is additive and builds on 0.8: it validates and operationalizes the artifacts created there without changing them. Foundation 0.8 stays released; the 0.8 optional WPs (112/116/117/118) may be re-evaluated by 0.9 candidates but are not overwritten.

## DE – Beziehung zum v1.0-Pfad

Foundation 0.9 **stärkt den v1.0-Pfad mit Adoption-/Validation-Evidence**, behauptet aber keine v1.0-Reife und aktiviert keine volle v1.x-Zusage. Kein 0.9-Dokument darf v1.0 als erreicht darstellen. Ein v1.0-Release entscheidet ausschließlich ein späterer eigener v1.0-Zyklus.

## EN – Relationship to the v1.0 Path

Foundation 0.9 **strengthens the v1.0 path with adoption/validation evidence** but claims no v1.0 maturity and activates no full v1.x promise. No 0.9 document may present v1.0 as reached. A v1.0 release is decided solely by a later dedicated v1.0 cycle.

## DE – Offene Entscheidungen für Scope Lock

WP-121 muss klären: (a) finale blocking/optional/deferred-Einstufung; (b) ob WP-124 die docs-only Skills-Implementierung befürwortet und ob WP-125/WP-129 blocking oder optional werden; (c) ob die 0.8-Optional-WPs (112/116/117/118) durch 0.9-Kandidaten ersetzt oder parallel geführt werden; (d) Umfang der Adoption-/Validation-Evidence; (e) Änderungsregeln nach Scope Lock.

## EN – Open Decisions for Scope Lock

WP-121 must settle: (a) final blocking/optional/deferred classification; (b) whether WP-124 endorses the docs-only skills implementation and whether WP-125/WP-129 become blocking or optional; (c) whether the 0.8 optional WPs (112/116/117/118) are replaced by 0.9 candidates or run in parallel; (d) the scope of adoption/validation evidence; (e) change rules after scope lock.

## DE – Nächster Schritt

**NDF-WP-122 – Context Economy Adoption Review.** Scope Lock (WP-121) abgeschlossen; WP-123 (Validation) und WP-124 (Skills-Entscheidung) folgen im gesperrten Kern.

## EN – Next Step

**NDF-WP-121 – Foundation 0.9 scope lock.** No content work package starts before the scope lock is complete.
