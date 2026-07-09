# Foundation 0.9 Scope Lock

## DE – Zweck

Dieses Dokument friert den Umfang von Foundation 0.9 verbindlich ein (NDF-WP-121). Es macht aus dem Kandidatenplan (NDF-WP-120) die verbindliche Einstufung: release-blocking, optional/conditional, deferred — inklusive der WP-124-/WP-125-/WP-129-Entscheidungen, der Einordnung der Foundation-0.8-Optional-WPs und der Change-Control-Regeln.

## EN – Purpose

This document bindingly freezes the Foundation 0.9 scope (NDF-WP-121), turning the candidate plan (NDF-WP-120) into the binding classification — including the WP-124/WP-125/WP-129 decisions, the classification of the Foundation 0.8 optional WPs, and the change control rules.

## DE – Scope-Lock-Status

**Scope locked** (NDF-WP-121, 2026-07-08). Foundation 0.9 ist gelockt, **nicht released**, **nicht v1.0** und **kein v1.0 Release Candidate**. In diesem WP wird **kein Skill Pack, keine `.claude/skills`, keine `SKILL.md`, keine Cursor Rules, kein Workflow und kein Script** erstellt. Foundation 0.9 bleibt **validation-first**.

## EN – Scope Lock Status

**Scope locked** (NDF-WP-121, 2026-07-08). Foundation 0.9 is locked, **not released**, **not v1.0**, and **no v1.0 release candidate**. This work package creates **no skill pack, no `.claude/skills`, no `SKILL.md`, no Cursor rules, no workflow, and no script**. Foundation 0.9 stays **validation-first**.

## DE – Arbeitstitel

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Gesperrter Kernfokus: **Adoption Review + Prompt/Context Validation + Optional Skills Decision + v1.0 Evidence Review** — zuerst validieren, erst dann optionales Enablement entscheiden.

## EN – Working Title

**Foundation 0.9 – Adoption, Validation & Optional Enablement.** Locked core focus: **adoption review + prompt/context validation + optional skills decision + v1.0 evidence review** — validate first, decide optional enablement only afterwards.

## DE – Release-blocking Scope

Nur diese WPs blockieren den Release:

| WP | Titel | Begründung |
|---|---|---|
| NDF-WP-121 | Foundation 0.9 Scope Lock | Gate — abgeschlossen mit diesem Dokument |
| NDF-WP-122 | Context Economy Adoption Review | Kern: prüfen, ob Context Economy in echten WPs hilft — **nächster Schritt** |
| NDF-WP-123 | Prompt Modes and Context Pack Validation | Kern: Prompt Modes + Context Pack Template validieren |
| NDF-WP-124 | Optional Skills MVP Implementation Decision | Kern: **Entscheidung** (keine Implementierung), verhindert stille Skill-Aktivierung |
| NDF-WP-126 | Adoption Evidence and v1.0 Path Review | Kern: Adoption-/Validation-Evidence, v1.0-Draft ehrlich fortschreiben |
| NDF-WP-127 | Foundation 0.9 Release Readiness Review | Gate |
| NDF-WP-128 | Foundation 0.9 Release Prep | Gate |

## EN – Release-Blocking Scope

Only WP-121 (this gate), WP-122 (context economy adoption review), WP-123 (prompt modes and context pack validation), WP-124 (optional skills MVP implementation decision — decision only), WP-126 (adoption evidence and v1.0 path review), WP-127 (readiness review), and WP-128 (release prep) block the release.

## DE – Optionale / bedingte Work Packages

Should-have/conditional, blockiert nie; Unerledigtes wird ehrlich geführt:

- **NDF-WP-125 – Skills MVP Implementation Blueprint** (conditional: nur wenn WP-124 eine spätere Implementierung empfiehlt; höchstens Blueprint, keine Implementierung)
- **NDF-WP-129 – Docs-only Skills MVP Implementation** (optional, **nicht durch WP-121 aktiviert**; nur per ausdrücklichem Human-Maintainer-Scope-Change nach WP-124/WP-125)
- NDF-WP-130 – Skill-to-Cursor Rules Export Assessment (nur Assessment)
- NDF-WP-131 – Workflow Builder Evaluation (nur Evaluation)
- NDF-WP-132 – Docs Polish Skill Evaluation (nur Evaluation)
- NDF-WP-133 – Foundation 0.9 Post-Release Status Cleanup (nur Post-Release-Kandidat nach manuellem Release)

## EN – Optional / Conditional Work Packages

WP-125 (skills MVP implementation blueprint — conditional on WP-124), WP-129 (docs-only skills MVP implementation — optional, **not activated by WP-121**, only via explicit human-maintainer scope change after WP-124/WP-125), WP-130/131/132 (assessments/evaluations only), WP-133 (post-release candidate only). None blocks.

## DE – Deferred / Non-Goals

- Aktives Claude Skills Pack per Default
- `.claude/skills`-Erstellung per Default
- Skills-Implementierung ohne ausdrücklichen Human-Maintainer-Scope-Change
- Scripts in Skills; netzwerkfähige Skills
- Git-Schreibaktionen / Release-/Tag-Aktionen durch Skills
- Cursor-Rules-Implementierung; Workflow-Implementierung
- Drittanbieter-Skill-Import; private projektspezifische Skills
- v1.0 Release Candidate; Aktivierung der vollen v1.x-Kompatibilitätszusage

## EN – Deferred / Non-Goals

Active Claude skills pack by default; `.claude/skills` creation by default; skills implementation without an explicit human-maintainer scope change; scripts inside skills; network-enabled skills; git write actions / release/tag actions from skills; Cursor rules implementation; workflow implementation; third-party skill import; private project-specific skills; v1.0 release candidate; full v1.x compatibility activation.

## DE – Entscheidung zu WP-124

**WP-124 (Optional Skills MVP Implementation Decision) ist release-blocking.** Begründung: die Entscheidung ist wertvoll und ist **keine Implementierung**; sie klärt, ob WP-125/WP-129 später sinnvoll sind, und verhindert eine stille Aktivierung von Skills. WP-124 liefert eine begründete Empfehlung (priorisieren / optional / verwerfen), keine `.claude/skills`.

## EN – Decision on WP-124

**WP-124 is release-blocking.** The decision is valuable and is **not an implementation**; it clarifies whether WP-125/WP-129 are worthwhile later and prevents a silent activation of skills. WP-124 yields a reasoned recommendation, no `.claude/skills`.

## DE – Entscheidung zu WP-125

**WP-125 (Skills MVP Implementation Blueprint) ist optional / conditional.** Ein Blueprint kann sinnvoll sein, **wenn** WP-124 eine spätere Implementierung empfiehlt; er ist nicht zwingend für den 0.9-Release. **Kein Blueprint vor der WP-124-Entscheidung; kein Implementation Scope in WP-125** — es bleibt ein Design/Blueprint gemäß ADR-0032.

## EN – Decision on WP-125

**WP-125 is optional / conditional.** A blueprint may be worthwhile **if** WP-124 recommends a later implementation; it is not mandatory for the 0.9 release. **No blueprint before the WP-124 decision; no implementation scope in WP-125** — it stays a design/blueprint per ADR-0032.

## DE – Entscheidung zu WP-129

**WP-129 (Docs-only Skills MVP Implementation) ist optional, nicht release-blocking und wird durch WP-121 nicht aktiviert.** Implementierung ist höheres Risiko als Adoption/Validation; ADR-0032 verlangt fail closed. Reihenfolge: **erst Entscheidung (WP-124), dann ggf. Blueprint (WP-125), dann ggf. separate ausdrückliche Aktivierung (WP-129)**. Keine stille `.claude/skills`-Erstellung; jede Umsetzung strikt docs-only und ADR-0032-konform.

## EN – Decision on WP-129

**WP-129 is optional, not release-blocking, and not activated by WP-121.** Implementation carries higher risk than adoption/validation; ADR-0032 requires fail closed. Order: **decision first (WP-124), then possibly a blueprint (WP-125), then possibly a separate explicit activation (WP-129)**. No silent `.claude/skills` creation; any implementation strictly docs-only and ADR-0032-compliant.

## DE – Einordnung der Foundation-0.8-Optional-WPs

**WP-112, WP-116, WP-117 und WP-118 bleiben Foundation-0.8-Optional-Kandidaten und wurden nicht aktiviert.** Foundation 0.9 kann ihre Themen über **neue** 0.9-Kandidaten-WPs neu bewerten. Die alten WP-Nummern werden **nicht wiederverwendet, überschrieben oder still reaktiviert.** Themen-Zuordnung: WP-112 → WP-124/WP-125/WP-129; WP-116 → WP-130; WP-117 → WP-131; WP-118 → WP-132.

## EN – Classification of Foundation 0.8 Optional WPs

WP-112, WP-116, WP-117, and WP-118 remain Foundation 0.8 optional candidates and were not activated. Foundation 0.9 may re-evaluate their themes through **new** 0.9 candidate WPs. The old WP numbers are **not reused, overwritten, or silently reopened.** Theme mapping: WP-112 → WP-124/125/129; WP-116 → WP-130; WP-117 → WP-131; WP-118 → WP-132.

## DE – Sicherheitsgrenzen

Verbindlich für alle Foundation-0.9-WPs (gemäß ADR-0032): keine aktiven Skills ohne ausdrücklichen Scope; keine Scripts; keine Netzwerkzugriffe; keine Secrets; keine privaten Projektdaten; keine autonomen Commit-/Push-/Tag-/Release-Aktionen; kein Drittanbieter-Skill-Import; Public Quality Gate + Public Neutrality Pflicht; jede spätere Skill-Umsetzung strikt docs-only und ADR-0032-konform.

## EN – Security Boundaries

Binding for all Foundation 0.9 work packages (per ADR-0032): no active skills without an explicit scope; no scripts; no network access; no secrets; no private project data; no autonomous commit/push/tag/release actions; no third-party skill import; public quality gate + public neutrality mandatory; any later skill implementation strictly docs-only and ADR-0032-compliant.

## DE – Human-Maintainer-Gates

Der Human Maintainer bleibt finaler Owner: GO / GO WITH NOTES / REWORK / STOP, Commit, Push, Tag, Release. Skills und Agenten treffen keine irreversiblen Entscheidungen und lösen keine Git-/Release-Aktionen aus. Nova (ChatGPT) plant und reviewt; der Implementation Agent implementiert nur beauftragte WPs.

## EN – Human Maintainer Gates

The human maintainer stays final owner: decides GO / GO WITH NOTES / REWORK / STOP, commits, pushes, tags, and releases. Skills and agents make no irreversible decisions and trigger no git/release actions. Nova (ChatGPT) plans and reviews; the Implementation Agent implements only commissioned work packages.

## DE – Change Control

Nach NDF-WP-121 gilt:

- Kein neues release-blocking WP ohne ausdrücklichen Scope-Change-Vermerk (kleines Nova-(ChatGPT)-Review + Human-Maintainer-Freigabe).
- **Keine Skills-Implementierung ohne ausdrückliche Human-Maintainer-Entscheidung.**
- **Keine `.claude/skills` ohne explizite Aktivierung eines Implementierungs-WP.**
- Keine Scripts ohne spätere ausdrückliche ADR-/Scope-Entscheidung.
- Keine Netzwerkzugriffe; keine Git-Schreibaktionen; keine Release-/Tag-Aktionen.
- Kein Import von Drittanbieter-Skills.
- Optionale WPs bleiben optional, bis der Human Maintainer sie ausdrücklich hochstuft.
- Foundation 0.9 bleibt **kein v1.0**; keine stille Scope-Erweiterung; keine Release Prep vor WP-127.
- Redaktionelle Korrekturen (Tippfehler, Links, Statusklarstellungen) sind keine Scope-Änderung.

## EN – Change Control

After NDF-WP-121: no new release-blocking work package without an explicit scope-change note; no skills implementation without an explicit human-maintainer decision; no `.claude/skills` without explicit activation of an implementation WP; no scripts without a later explicit ADR/scope decision; no network access, git writes, or release/tag actions; no third-party skill import; optional WPs stay optional until the human maintainer explicitly upgrades them; Foundation 0.9 stays not v1.0; no silent scope expansion; no release prep before WP-127; editorial fixes are not scope changes.

## DE – Beziehung zu Foundation 0.8

Foundation 0.9 ist additiv und baut auf 0.8 auf: es validiert und operationalisiert die dort geschaffenen Artefakte (Context Economy, Prompt Modes, Context Packs, Skill Security Policy, Skills MVP Design), ohne sie zu ändern. Foundation 0.8 bleibt released; die 0.8-Optional-WPs werden neu bewertet, nicht überschrieben.

## EN – Relationship to Foundation 0.8

Foundation 0.9 is additive and builds on 0.8: it validates and operationalizes the artifacts created there without changing them. Foundation 0.8 stays released; the 0.8 optional WPs are re-evaluated, not overwritten.

## DE – Beziehung zum v1.0-Pfad

Foundation 0.9 **stärkt den v1.0-Pfad mit Adoption-/Validation-Evidence** (WP-126), behauptet aber keine v1.0-Reife und aktiviert keine volle v1.x-Zusage. Kein 0.9-Dokument darf v1.0 als erreicht darstellen. Ein v1.0-Release entscheidet ausschließlich ein späterer eigener v1.0-Zyklus.

## EN – Relationship to the v1.0 Path

Foundation 0.9 **strengthens the v1.0 path with adoption/validation evidence** (WP-126) but claims no v1.0 maturity and activates no full v1.x promise. No 0.9 document may present v1.0 as reached. A v1.0 release is decided solely by a later dedicated v1.0 cycle.

## DE – Nächster Schritt

**NDF-WP-122 – Context Economy Adoption Review.** Kein anderes inhaltliches WP startet vor WP-122; WP-123 (Validation) und WP-124 (Skills-Entscheidung) folgen im gesperrten Kern.

## EN – Next Step

**NDF-WP-122 – Context Economy Adoption Review.** No other content work package starts before WP-122; WP-123 (validation) and WP-124 (skills decision) follow in the locked core.
