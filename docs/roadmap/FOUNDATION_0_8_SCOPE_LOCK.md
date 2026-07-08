# Foundation 0.8 Scope Lock

## DE – Zweck

Dieses Dokument friert den Umfang von Foundation 0.8 verbindlich ein (NDF-WP-108). Es macht aus dem Kandidatenplan (NDF-WP-107) die verbindliche Einstufung: release-blocking, optional, deferred — inklusive der WP-112-Entscheidung (Skills-MVP-Implementierung), der ADR-0032-Frage (Skill Security Policy) und der Change-Control-Regeln.

## EN – Purpose

This document bindingly freezes the Foundation 0.8 scope (NDF-WP-108), turning the candidate plan (NDF-WP-107) into the binding classification — including the WP-112 decision (skills MVP implementation), the ADR-0032 question (skill security policy), and the change control rules.

## DE – Scope-Lock-Status

**Scope locked** (NDF-WP-108, 2026-07-08). Foundation 0.8 ist gelockt, **nicht released**, **nicht v1.0** und **kein v1.0 Release Candidate**. In diesem WP wird **kein Skill Pack, keine `.claude/skills`, keine Cursor Rules, kein Workflow und kein Script erstellt**.

## EN – Scope Lock Status

**Scope locked** (NDF-WP-108, 2026-07-08). Foundation 0.8 is locked, **not released**, **not v1.0**, and **no v1.0 release candidate**. This work package creates **no skill pack, no `.claude/skills`, no Cursor rules, no workflow, and no script**.

## DE – Arbeitstitel

**Foundation 0.8 – Agent Enablement & Context Economy.** Gesperrter Kernfokus: **Context Economy + Skill Security + Skills MVP Design** — bewusst klein und sicher. Foundation 0.8 operationalisiert die in 0.7 gefestigte Governance, behauptet aber keine v1.0-Reife.

## EN – Working Title

**Foundation 0.8 – Agent Enablement & Context Economy.** Locked core focus: **context economy + skill security + skills MVP design** — deliberately small and safe. Foundation 0.8 operationalizes the governance consolidated in 0.7 but claims no v1.0 maturity.

## DE – Release-blocking Scope

Nur diese WPs blockieren den Release:

| WP | Titel | Begründung |
|---|---|---|
| NDF-WP-108 | Foundation 0.8 Scope Lock | Gate — abgeschlossen mit diesem Dokument |
| NDF-WP-109 | NDF Context Economy Concept | Kern: Context Economy als NDF-Prinzip |
| NDF-WP-110 | NDF Skill Security Policy / ADR-0032 | Kern: dauerhafte Governance-Grenzen für Skills (ADR-0032 in diesem WP) |
| NDF-WP-111 | NDF Claude Skills Pack MVP Design | Kern: Design des MVP-Skill-Sets (nur Design, keine Implementierung) |
| NDF-WP-113 | NDF Context Pack Template and Prompt Modes | Kern: Context-Pack-Template + Prompt-Modi standardisieren |
| NDF-WP-114 | Foundation 0.8 Release Readiness Review | Gate |
| NDF-WP-115 | Foundation 0.8 Release Prep | Gate |

## EN – Release-Blocking Scope

Only WP-108 (this gate), WP-109 (context economy concept), WP-110 (skill security policy / ADR-0032), WP-111 (skills pack MVP design), WP-113 (context pack template and prompt modes), WP-114 (readiness review), and WP-115 (release prep) block the release.

## DE – Optionale Work Packages

Should-have, blockiert nie; Unerledigtes wird ehrlich in Release Notes und Matrix geführt:

- **NDF-WP-112 – NDF Claude Skills Pack MVP Implementation** (mit Upgrade-Regel, siehe unten)
- NDF-WP-116 – Skill-to-Cursor Rules Export Assessment (nur Assessment)
- NDF-WP-117 – Workflow Builder Evaluation (nur Evaluation)
- NDF-WP-118 – Docs Polish Skill Evaluation (nur Evaluation)

## EN – Optional Work Packages

WP-112 (skills MVP implementation, with upgrade rule below), WP-116 (skill-to-Cursor export assessment), WP-117 (workflow builder evaluation), WP-118 (docs polish skill evaluation). None blocks; unfinished items documented honestly.

## DE – Deferred / Non-Goals

- Vollständige Automatisierungsplattform
- Autonome Multi-Agent-Workflows
- Scripts innerhalb von Skills
- Skills mit Netzwerkzugriff
- Git-Schreibaktionen durch Skills
- Release-/Tag-Aktionen durch Skills
- Cursor-Rules-Export-Implementierung
- Workflow-Implementierung
- Import von Drittanbieter-Skills
- Private, projektspezifische Skills
- v1.0 Release Candidate
- Aktivierung der vollen v1.x-Kompatibilitätszusage

## EN – Deferred / Non-Goals

Full automation platform; autonomous multi-agent workflows; scripts inside skills; network-enabled skills; git write actions from skills; release/tag actions from skills; Cursor rules export implementation; workflow implementation; third-party skill import; private project-specific skills; v1.0 release candidate; full v1.x compatibility activation.

## DE – Entscheidung zu WP-112

**Option A gewählt: WP-112 (Skills MVP Implementation) bleibt optional, nicht release-blocking.** Foundation 0.8 lockt die Design-, Security- und Context-Economy-Grundlage; die tatsächliche Skills-MVP-Implementierung bleibt optional oder Folge-Release (ggf. Foundation 0.9).

**Begründung:** reduziert Scope Creep; Security Policy (WP-110) und MVP Design (WP-111) kommen zuerst; keine `.claude/skills` vor der Sicherheitsentscheidung; Skills können nach Readiness optional oder später umgesetzt werden.

**Upgrade-Regel:** WP-112 darf **nur** per ausdrücklichem Human-Maintainer-Scope-Change-Vermerk auf release-blocking hochgestuft werden, und nur wenn (a) WP-110 (Security Policy) und WP-111 (MVP Design) abgeschlossen sind und (b) die Implementierung strikt docs-only bleibt (keine Scripts, keine Netzwerkzugriffe, keine Git-Schreib-/Release-/Tag-Aktionen, keine Secrets, keine privaten Projektdaten, verbindliche Human-Maintainer-Gates). Ohne diesen Vermerk bleibt WP-112 optional.

## EN – Decision on WP-112

**Option A chosen: WP-112 (skills MVP implementation) stays optional, not release-blocking.** Foundation 0.8 locks the design, security, and context economy foundation; the actual skills MVP implementation remains optional or a follow-up (possibly Foundation 0.9). **Rationale:** reduces scope creep; security policy (WP-110) and MVP design (WP-111) come first; no `.claude/skills` before the security decision. **Upgrade rule:** WP-112 may be upgraded to release-blocking **only** via an explicit human-maintainer scope-change note, and only if WP-110 and WP-111 are complete and the implementation stays strictly docs-only (no scripts, network, git writes, release/tag actions, secrets, or private data; mandatory human-maintainer gates).

## DE – Entscheidung zu ADR-0032

**ADR-0032 ist der bevorzugte Pfad für die Skill Security Policy** — Skill-Security-Regeln betreffen dauerhaft Agenten-Grenzen, Tool-/Script-Erlaubnis, Schreibaktionen, Secrets, Public Neutrality, Human-Maintainer-Gates und Release Safety; das ist eine dauerhafte Governance-Entscheidung im Sinne der ADR-Policy. **ADR-0032 wird erst in WP-110 erstellt**, nicht in diesem WP. Die nächste freie ADR-Nummer bleibt **ADR-0032**, bis WP-110 sie belegt.

## EN – Decision on ADR-0032

**ADR-0032 is the preferred path for the skill security policy** — skill security rules permanently affect agent boundaries, tool/script permission, write actions, secrets, public neutrality, human-maintainer gates, and release safety; this is a lasting governance decision under the ADR policy. **ADR-0032 is created only in WP-110**, not here. The next free ADR number stays **ADR-0032** until WP-110 uses it.

## DE – Sicherheitsgrenzen

Verbindlich für alle Foundation-0.8-WPs:

- Skills zuerst **docs-only**; keine Scripts im MVP, außer ein späterer ausdrücklicher Scope-Change erlaubt es.
- Keine Netzwerkzugriffe durch Skills.
- Keine Git-Schreibaktionen, keine Release-/Tag-Aktionen durch Skills.
- Keine Secrets; der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden, der Wert nie.
- Keine privaten Projektdaten; keine Drittanbieter-Skill-Inhalte oder externen Branding-/Autorenhinweise.
- Public Quality Gate v0.2 (strict + self-test, new-file neutrality check) bleibt Pflichtinvariante.
- Jeder WP-bezogene Skill unterstützt Rückmeldung an Nova (ChatGPT) und Compact Context Summary.

## EN – Security Boundaries

Binding for all Foundation 0.8 work packages: skills docs-only first (no scripts in the MVP unless a later explicit scope change allows it); no network access; no git writes, no release/tag actions; no secrets (naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed, its value never); no private project data; no third-party skill content or external branding/author notices; public quality gate v0.2 stays a mandatory invariant; every work-package-related skill supports Report to Nova (ChatGPT) and a Compact Context Summary.

## DE – Human-Maintainer-Gates

Der Human Maintainer bleibt finaler Owner: Er entscheidet GO / GO WITH NOTES / REWORK / STOP, committet, pusht, taggt und veröffentlicht. Skills und Agenten treffen keine irreversiblen Entscheidungen und lösen keine Git-/Release-Aktionen aus. Nova (ChatGPT) plant und reviewt; der Implementation Agent implementiert nur beauftragte WPs.

## EN – Human Maintainer Gates

The human maintainer stays final owner: decides GO / GO WITH NOTES / REWORK / STOP, commits, pushes, tags, and releases. Skills and agents make no irreversible decisions and trigger no git/release actions. Nova (ChatGPT) plans and reviews; the Implementation Agent implements only commissioned work packages.

## DE – Change Control

Nach NDF-WP-108 gilt:

- **Kein neues release-blocking WP** ohne ausdrücklichen Scope-Change-Vermerk (kleines Nova-(ChatGPT)-Review + Human-Maintainer-Freigabe).
- **Keine Skills-Implementierung ohne vorher abgeschlossene Security Policy (WP-110).**
- **Keine Scripts** ohne ausdrückliche spätere Entscheidung.
- Keine Netzwerkzugriffe; keine Git-Schreibaktionen; keine Release-/Tag-Aktionen.
- **Kein Import von Drittanbieter-Skills.**
- Optionale WPs bleiben optional, bis der Human Maintainer sie ausdrücklich hochstuft (inkl. WP-112-Upgrade-Regel).
- Keine stille Scope-Erweiterung, kein Feature Creep, kein v1.0-Claim, keine Release Prep vor WP-114.
- Redaktionelle Korrekturen (Tippfehler, Links, Statusklarstellungen) sind keine Scope-Änderung.

## EN – Change Control

After NDF-WP-108: no new release-blocking work package without an explicit scope-change note; no skills implementation before the security policy (WP-110) is complete; no scripts without an explicit later decision; no network access, git writes, or release/tag actions; no third-party skill import; optional work packages stay optional until the human maintainer explicitly upgrades them (incl. the WP-112 upgrade rule); no silent scope expansion, feature creep, v1.0 claim, or release prep before WP-114; editorial fixes are not scope changes.

## DE – Beziehung zu Foundation 0.7

Foundation 0.8 ist additiv und baut auf 0.7 auf: die dort gefestigte Rollen-/WP-/Gate-Governance (Stable Candidate in ADR-0031) wird operationalisiert, nicht verändert. Foundation 0.7 bleibt released; keine 0.7-Artefakte werden ersetzt.

## EN – Relationship to Foundation 0.7

Foundation 0.8 is additive and builds on 0.7: the role/WP/gate governance consolidated there (Stable Candidate in ADR-0031) is operationalized, not changed. Foundation 0.7 stays released; no 0.7 artifacts are replaced.

## DE – Beziehung zum v1.0-Pfad

Foundation 0.8 ist **kein v1.0-Schritt** und keine v1.0-Vorbereitung; es adressiert kein offenes v1.0-Kriterium direkt, sondern verbessert die Arbeitsweise. Kein 0.8-Dokument darf v1.0 als erreicht oder eine volle v1.x-Zusage als aktiv darstellen. Ein v1.0-Release entscheidet ausschließlich ein späterer eigener v1.0-Zyklus.

## EN – Relationship to the v1.0 Path

Foundation 0.8 is **not a v1.0 step** and not v1.0 preparation; it addresses no open v1.0 criterion directly but improves the way of working. No 0.8 document may present v1.0 as reached or a full v1.x promise as active. A v1.0 release is decided solely by a later dedicated v1.0 cycle.

## DE – Nächster Schritt

**NDF-WP-109 – NDF Context Economy Concept.** Kein anderes inhaltliches WP startet vor WP-109; WP-110 (Skill Security Policy / ADR-0032) und WP-111 (MVP Design) folgen im gesperrten Kern.

## EN – Next Step

**NDF-WP-109 – NDF Context Economy Concept.** No other content work package starts before WP-109; WP-110 (skill security policy / ADR-0032) and WP-111 (MVP design) follow in the locked core.
