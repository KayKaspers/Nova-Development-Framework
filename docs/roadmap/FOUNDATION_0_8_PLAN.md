# Foundation 0.8 Plan

## DE – Zweck

Dieser Plan sammelt die Kandidaten für Foundation 0.8 (Ergebnis von NDF-WP-107). **Status-Update: Scope locked** (NDF-WP-108, 2026-07-08) — verbindliche Einstufung: [FOUNDATION_0_8_SCOPE_LOCK.md](FOUNDATION_0_8_SCOPE_LOCK.md). Release-blocking sind nur 108, 109 (Context Economy Concept — **erledigt**, [NDF_CONTEXT_ECONOMY.md](../agent-workflows/NDF_CONTEXT_ECONOMY.md)), 110 (Skill Security Policy — **erledigt: [ADR-0032](../adr/ADR-0032-skill-security-policy.md) Accepted + Policy-Dokument**), 111 (Skills MVP Design — **erledigt: [MVP Design](../agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md)**, kein aktives Skill Pack), 113 (Context Pack Template & Prompt Modes — **nächster Schritt**), 114, 115. **WP-112 (Skills MVP Implementation) bleibt optional (Option A)** — nur per Human-Maintainer-Scope-Change hochstufbar. Foundation 0.8 ist gelockt, **nicht released** und **nicht v1.0**. Es wird in diesem WP **kein Skill Pack erstellt**.

## EN – Purpose

This plan collects the candidates for Foundation 0.8 (result of NDF-WP-107). It is **not a scope lock** — the scope only becomes binding with NDF-WP-108. Foundation 0.8 is **not scope-locked**, **not released**, and **not v1.0**. **No skill pack is created** in this work package.

## DE – Arbeitstitel

**Foundation 0.8 – Agent Enablement & Context Economy** (Agenten-Befähigung und Kontext-Ökonomie). Nur Arbeitstitel — der Scope Lock (WP-108) bestätigt oder ändert ihn. Foundation 0.8 ist **nicht v1.0** und kein v1.0 Release Candidate.

## EN – Working Title

**Foundation 0.8 – Agent Enablement & Context Economy.** Working title only — the scope lock (WP-108) confirms or changes it. Foundation 0.8 is **not v1.0** and no v1.0 release candidate.

## DE – Ausgangslage

Foundation 0.7 ist als `v0.7.0-foundation` veröffentlicht (2026-07-08), vollständig abgeschlossen (WP-106), keine offenen 0.7-blocking Follow-ups. Übernommener Future Candidate aus 0.7: **NDF Agent Enablement & Context Economy**, inkl. eines kleinen public-neutralen Claude Skills Pack. Kompatibilitäts-Governance ist über [ADR-0031](../adr/ADR-0031-v1x-compatibility-policy.md) geregelt; die volle v1.x-Zusage aktiviert erst mit v1.0. Nächste freie ADR-Nummer: ADR-0032.

## EN – Background

Foundation 0.7 is published as `v0.7.0-foundation` (2026-07-08), fully complete (WP-106), no open 0.7-blocking follow-ups. The future candidate carried over from 0.7: **NDF Agent Enablement & Context Economy**, including a small public-neutral Claude Skills Pack. Compatibility governance is settled via ADR-0031; the full v1.x promise activates only at v1.0. Next free ADR number: ADR-0032.

## DE – Ziele

1. **NDF Context Economy** als offizielles Workflow-Prinzip planen (bewusster Token-/Kontextverbrauch).
2. **Context Packs** und **Compact Context Summary** als NDF-Standard standardisieren.
3. Ein kleines, public-neutrales **Claude Skills Pack** als MVP planen (nur Design in dieser Phase).
4. Eine **Skill Security Policy** vorbereiten (Human-Gates, keine Git-/Release-Schreibaktionen, keine Netzwerkzugriffe, keine Secrets).
5. Eine **Skill Review Checklist** vorbereiten.
6. **Skill-vs-Prompt-vs-Workflow-Entscheidungskriterien** planen.
7. **Release Safety** und **Human-Maintainer-Gates** für Skills festlegen.
8. Keine automatische Git-/Release-Aktion durch Skills — fail closed.

## EN – Goals

(1) Plan **NDF Context Economy** as an official workflow principle; (2) standardize **Context Packs** and **Compact Context Summary** as an NDF standard; (3) plan a small public-neutral **Claude Skills Pack** MVP (design only in this phase); (4) prepare a **Skill Security Policy** (human gates, no git/release writes, no network, no secrets); (5) prepare a **Skill Review Checklist**; (6) plan **skill-vs-prompt-vs-workflow** decision criteria; (7) define **Release Safety** and **human-maintainer gates** for skills; (8) no autonomous git/release action by skills — fail closed.

## DE – Nicht-Ziele

- Keine v1.0-Release-Vorbereitung, kein v1.0 Release Candidate, keine v1.0-Reife-Behauptung.
- Keine Skill-Script-Ausführung; keine Netzwerkzugriffe durch Skills.
- Keine Drittanbieter-Skills importieren; keine externen Skill-Inhalte oder Branding-/Autorenhinweise übernehmen.
- Keine große Automatisierungsplattform; keine autonome Git-/Release-Automation.
- Keine Cursor-Rules und keine Workflows in dieser Planning-Phase.
- Keine privaten Projektadapter; Neutralität bleibt Invariante.
- **In WP-107 wird kein Skill Pack und keine `.claude/skills`-Datei erstellt.**

## EN – Non-Goals

No v1.0 release prep, release candidate, or maturity claim; no skill-script execution or network access by skills; no import of third-party skills or external skill content / branding / author notices; no large automation platform or autonomous git/release automation; no Cursor rules or workflows in this planning phase; no private project adapters. **WP-107 creates no skill pack and no `.claude/skills` file.**

## DE – Vorgeschlagener Scope

Foundation 0.8 soll **kein großer Feature-Release** werden, sondern eine kontrollierte, dokumentationsgetriebene NDF-Erweiterung: Context Economy als Prinzip, ein kleines Skills-MVP mit strikter Security Policy und Human-Gates, sowie klare Entscheidungsregeln für Skill vs. Prompt vs. Workflow. Bewährtes Muster wie 0.4–0.7: kleiner blocking Kern, optionale Kandidaten ehrlich als optional geführt, deferred Themen sichtbar. Die verbindliche blocking/optional/deferred-Trennung entsteht erst in WP-108.

## EN – Proposed Scope

Foundation 0.8 should be **not a large feature release** but a controlled, documentation-driven NDF extension: context economy as a principle, a small skills MVP with a strict security policy and human gates, and clear decision rules for skill vs. prompt vs. workflow. Same pattern as 0.4–0.7: small blocking core, optional candidates kept honestly optional, deferred topics visible. The binding blocking/optional/deferred split happens only in WP-108.

## DE – Vorgeschlagene Work Packages

Vollständige Kandidatenliste: [FOUNDATION_0_8_WORK_PACKAGES.md](FOUNDATION_0_8_WORK_PACKAGES.md). Kern-Kandidaten: WP-108 (Scope Lock), WP-109 (Context Economy Concept), WP-110 (Skill Security Policy), WP-111 (Skills Pack MVP Design), WP-112 (Skills Pack MVP Implementation), WP-113 (Context Pack Template & Prompt Modes), WP-114/115 (Readiness/Prep). Optional: WP-116 (Skill-to-Cursor-Export-Assessment), WP-117 (Workflow-Builder-Evaluation), WP-118 (Docs-Polish-Skill-Evaluation).

## EN – Proposed Work Packages

Full candidate list in the work package candidates document. Core candidates: WP-108 (scope lock), WP-109 (context economy concept), WP-110 (skill security policy), WP-111 (skills pack MVP design), WP-112 (skills pack MVP implementation), WP-113 (context pack template & prompt modes), WP-114/115 (readiness/prep). Optional: WP-116/117/118.

## DE – Sicherheits- und Neutralitätsregeln

Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflichtinvariante. Skills sind zuerst **docs-only**; keine Scripts im MVP, außer ein späterer Scope Lock erlaubt es ausdrücklich; keine Netzwerkzugriffe, keine Secrets, keine privaten Projektinformationen, keine Git-Schreibaktionen, keine Releases. Jeder Skill respektiert Human-Maintainer-Gates und unterstützt — wenn er WP-Arbeit betrifft — Rückmeldung an Nova (ChatGPT) und Compact Context Summary. Keine privaten Namen/Suchmuster/Domains/Kontakte; der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden, der Wert nie.

## EN – Security and Neutrality Rules

Public quality gate v0.2 stays a mandatory invariant. Skills are **docs-only first**; no scripts in the MVP unless a later scope lock explicitly allows it; no network access, no secrets, no private project information, no git writes, no releases. Every skill respects human-maintainer gates and — where it touches work-package work — supports Report to Nova (ChatGPT) and a Compact Context Summary. No private names/patterns/domains/contacts; naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed, its value never.

## DE – Beziehung zu Foundation 0.7

Foundation 0.8 ist additiv und baut direkt auf 0.7 auf: die in 0.7 gefestigte Rollen-/WP-/Gate-Governance (Stable Candidate in ADR-0031) wird operationalisiert — Context Economy und Skills machen die bestehenden Prinzipien effizienter nutzbar, ohne sie zu ändern. Foundation 0.7 bleibt released; keine 0.7-Artefakte werden ersetzt.

## EN – Relationship to Foundation 0.7

Foundation 0.8 is additive and builds directly on 0.7: the role/WP/gate governance consolidated in 0.7 (Stable Candidate in ADR-0031) is operationalized — context economy and skills make the existing principles more efficient to use without changing them. Foundation 0.7 stays released; no 0.7 artifacts are replaced.

## DE – Beziehung zum v1.0-Pfad

Foundation 0.8 ist **kein v1.0-Schritt** und keine v1.0-Vorbereitung. Es adressiert kein offenes v1.0-Kriterium direkt, sondern verbessert die Arbeitsweise (Effizienz, Skill-Governance). Der v1.0-Pfad bleibt unverändert definiert (nicht terminiert); kein 0.8-Dokument darf v1.0 als erreicht oder eine volle v1.x-Zusage als aktiv darstellen.

## EN – Relationship to the v1.0 Path

Foundation 0.8 is **not a v1.0 step** and not v1.0 preparation. It addresses no open v1.0 criterion directly but improves the way of working (efficiency, skill governance). The v1.0 path stays defined (not scheduled); no 0.8 document may present v1.0 as reached or a full v1.x promise as active.

## DE – Offene Entscheidungen für Scope Lock

WP-108 muss klären: (a) finale blocking/optional/deferred-Einstufung; (b) ob die Skills-MVP-Implementierung (WP-112) blocking wird oder als optional/Folge-Release geführt wird; (c) ob das MVP strikt docs-only bleibt oder ausgewählte Scripts unter Security Policy erlaubt werden; (d) welcher konkrete Skill-Umfang ins MVP kommt; (e) Änderungsregeln nach Scope Lock.

## EN – Open Decisions for Scope Lock

WP-108 must settle: (a) final blocking/optional/deferred classification; (b) whether the skills MVP implementation (WP-112) becomes blocking or is kept optional / a follow-up release; (c) whether the MVP stays strictly docs-only or allows selected scripts under the security policy; (d) the concrete skill set for the MVP; (e) change rules after scope lock.

## DE – Nächster Schritt

**NDF-WP-113 – NDF Context Pack Template and Prompt Modes.** WP-109/110/111 erledigt (Context Economy, Skill Security Policy / [ADR-0032](../adr/ADR-0032-skill-security-policy.md), [Skills MVP Design](../agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md)); danach optional WP-112, dann WP-114/115. Nächste freie ADR-Nummer: 0033.

## EN – Next Step

**NDF-WP-108 – Foundation 0.8 scope lock.** No content work package (context economy, skills, security policy) starts before the scope lock is complete.
