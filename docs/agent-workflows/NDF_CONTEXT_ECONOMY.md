# NDF Context Economy

## DE – Zweck

Dieses Dokument definiert **Context Economy** als offizielles, public-neutrales NDF-Arbeitsprinzip (NDF-WP-109). Ziel: Kontext- und Tokenverbrauch in NDF-Agentenabläufen reduzieren, **ohne** Sicherheits-, Qualitäts- oder Review-Kontext zu verlieren. Es definiert nur das **Konzept und die Regeln** — konkrete Templates und Prompt-Mode-Vorlagen entstehen erst in NDF-WP-113, Skills erst in WP-111/112.

## EN – Purpose

This document defines **Context Economy** as an official, public-neutral NDF working principle (NDF-WP-109). Goal: reduce context and token usage in NDF agent workflows **without** losing security, quality, or review context. It defines only the **concept and rules** — concrete templates and prompt-mode drafts come only in NDF-WP-113, skills only in WP-111/112.

## DE – Definition

Context Economy ist der bewusste, sparsame Umgang mit Kontext in NDF-Abläufen: Es wird nur der Kontext geladen und weitergegeben, der für die Aufgabe, ihre Sicherheit und ihren Review nötig ist — kompakt, gezielt und wiederverwendbar. Context Economy ist **kein** Sparen an Sorgfalt, sondern Sparen an unnötigem Ballast.

## EN – Definition

Context Economy is the deliberate, frugal handling of context in NDF workflows: only the context needed for the task, its safety, and its review is loaded and handed over — compact, targeted, and reusable. Context Economy is **not** saving on diligence but saving on unnecessary ballast.

## DE – Grundprinzipien

Context Economy bedeutet **nicht** weniger Sorgfalt, weniger Security, weniger Review, weniger Quality Gate oder weniger Dokumentation. Context Economy bedeutet:

- weniger unnötiger Kontext
- mehr gezielte Quellen statt Volltext
- mehr wiederverwendbare Status-Snapshots
- klarere Prompt-Größen
- weniger Wiederholung
- bessere Übergaben zwischen Nova (ChatGPT), Implementation Agent und Human Maintainer

## EN – Core Principles

Context Economy does **not** mean less diligence, security, review, quality gate, or documentation. It means: less unnecessary context; more targeted sources instead of full text; more reusable status snapshots; clearer prompt sizes; less repetition; better handovers between Nova (ChatGPT), the Implementation Agent, and the Human Maintainer.

## DE – Kontext-Schichten

Fünf Schichten trennen dauerhaften von flüchtigem Kontext. Pro Schicht: Zweck, typische Quellen, was einzuschließen ist, was nicht, Token-Spar-Effekt und Sicherheits-Leitplanke.

**Ebene 1 – Dauerhafte Regeln (Durable Rules).** Zweck: unveränderliche NDF-Invarianten. Quellen: Rollenmodell, Work-Package-Typen, Public Quality Gate, ADR-Policy, ADR-0031. Einschließen: geltende Regeln/Invarianten. Nicht einschließen: phasenspezifische Details. Spar-Effekt: einmal referenzieren statt wiederholen. Leitplanke: Security-/Neutralitätsregeln nie kürzen.

**Ebene 2 – Phasenkontext (Phase Context).** Zweck: aktueller Foundation-Stand. Quellen: aktueller Scope Lock, Plan, WP-Queue, NEXT_PHASE. Einschließen: blocking/optional/deferred, nächster WP. Nicht einschließen: abgeschlossene Detailhistorie. Spar-Effekt: ein Phasen-Snapshot statt vieler Einzeldokumente. Leitplanke: kein Release-/v1.0-Fehlstatus.

**Ebene 3 – Work-Package-Kontext (Work Package Context).** Zweck: der konkrete Auftrag. Quellen: das WP-Prompt, direkt betroffene Dateien. Einschließen: Ziel, Scope, harte Grenzen. Nicht einschließen: fremde WPs. Spar-Effekt: nur die WP-relevanten Quellen. Leitplanke: harte Grenzen des WP bleiben vollständig.

**Ebene 4 – Evidenzkontext (Evidence Context).** Zweck: Nachweise für Entscheidungen. Quellen: Gate-Ausgabe, gezielte Greps, Git-Status/-Log (read-only). Einschließen: die für den Nachweis nötigen Ergebnisse. Nicht einschließen: Rohlogs in voller Länge. Spar-Effekt: kompakte Ergebnisse statt Volldumps. Leitplanke: erforderliche Evidenz nie wegkürzen.

**Ebene 5 – Ergebniszusammenfassung (Output Summary).** Zweck: Übergabe. Quellen: das WP-Ergebnis. Einschließen: Rückmeldung an Nova + Compact Context Summary. Nicht einschließen: private Denkprotokolle. Spar-Effekt: ein wiederverwendbarer Snapshot. Leitplanke: keine privaten Daten, keine Chain-of-Thought.

## EN – Context Layers

Five layers separate durable from transient context. Each layer states purpose, typical sources, what to include, what not to include, token-saving effect, and a safety guardrail.

- **Layer 1 – Durable Rules:** invariant NDF rules (role model, work-package types, public quality gate, ADR policy, ADR-0031); include applicable rules, exclude phase details; reference once instead of repeating; never trim security/neutrality rules.
- **Layer 2 – Phase Context:** current foundation state (scope lock, plan, WP queue, NEXT_PHASE); include blocking/optional/deferred and next WP, exclude completed detail history; one phase snapshot instead of many documents; no false release/v1.0 status.
- **Layer 3 – Work Package Context:** the concrete assignment (the WP prompt, directly affected files); include goal, scope, hard limits, exclude other WPs; only WP-relevant sources; keep the WP's hard limits complete.
- **Layer 4 – Evidence Context:** proof for decisions (gate output, targeted greps, read-only git status/log); include the results needed as evidence, exclude full-length raw logs; compact results instead of full dumps; never trim required evidence.
- **Layer 5 – Output Summary:** handover (the WP result); include Report to Nova + Compact Context Summary, exclude private thinking logs; one reusable snapshot; no private data, no chain-of-thought.

## DE – Compact Context Summary

Die **Compact Context Summary** ist der offizielle NDF-Handover-Baustein am Ende eines Work Packages. Sie:

- umfasst 5–10 Zeilen,
- fasst den letzten WP-Status zusammen,
- nennt Entscheidung / Ergebnis,
- nennt die nächste Aktion,
- nennt bekannte Notes / Risiken,
- enthält **keine** privaten Daten,
- enthält **keine** Chain-of-Thought,
- ist Teil der Rückmeldung an Nova (ChatGPT),
- ist später in Context Packs übernehmbar.

Neutrales Mini-Beispiel:

```text
WP-XXX completed with GO WITH NOTES. The reviewed scope is stable with notes and remains not v1.0. No release action was performed. Known notes remain non-blocking. Next WP: WP-YYY.
```

## EN – Compact Context Summary

The **Compact Context Summary** is the official NDF handover building block at the end of a work package: 5–10 lines; summarizes the last WP status; names decision/result; names the next action; names known notes/risks; contains **no** private data; contains **no** chain-of-thought; is part of the Report to Nova (ChatGPT); is reusable in Context Packs later. Neutral mini-example as above.

## DE – Context Packs

**Konzeptionell (Templates erst in WP-113).** Ein Context Pack ist ein kompakter, wiederverwendbarer Phasen-Snapshot als Einstieg für ein Folge-WP. Ein Context Pack **soll enthalten**: aktueller Phasenstatus; letztes abgeschlossenes WP; nächstes WP; release-blocking WPs; optionale/deferred WPs; für die Phase relevante angenommene ADRs; bekannte Notes/Limitations; aktuelle Sicherheitsgrenzen; relevante Quelldateien; kompakte Kontext-Historie. Ein Context Pack **soll nicht enthalten**: private Projektdaten; Secrets; Roh-Chatlogs; Chain-of-Thought; riesige kopierte Dokumente; externe Skill-Inhalte; ungeprüften Drittanbieter-Text.

Mögliche Dateinamen **nur als Konzept** (in diesem WP nicht erstellt): `project-brain/CONTEXT_PACK_FOUNDATION_0_8.md`, `project-brain/CONTEXT_PACK_TEMPLATE.md`.

## EN – Context Packs

**Conceptual (templates only in WP-113).** A Context Pack is a compact, reusable phase snapshot serving as an entry point for a follow-up WP. It **should contain**: current phase status; last completed WP; next WP; release-blocking WPs; optional/deferred WPs; accepted ADRs relevant to the phase; known notes/limitations; current safety boundaries; relevant source files; compact context history. It **should not contain**: private project data; secrets; raw chat logs; chain-of-thought; huge copied documents; external skill contents; unreviewed third-party text. Candidate file names are named as concept only and are **not created** in this WP.

## DE – Prompt Modes

**Konzeptionell (Templates erst in WP-113).** Drei Größen mit klaren Auswahlkriterien:

- **Full Prompt** — für Scope Lock, ADR, Release Prep, Release Readiness, Security Policy und gefährliche / irreversible / governance-relevante Entscheidungen. Voller Kontext, volle Grenzen.
- **Standard Prompt** — für normale Work Packages, Doku-Reviews, kleine Statusupdates, vorhersehbare Aufgaben.
- **Short Prompt** — für gut standardisierte Folgearbeiten nach vorhandenem Context Pack, kleine Update-WPs und wiederkehrende Checks.

**Grenze:** Ein Short Prompt darf **nie** genutzt werden für Security Policy, ADR, Scope Lock, Release, destructive changes, Git-Write-/Release-/Tag-Aktionen oder unklare Anforderungen — dort ist Full (bzw. mindestens Standard) Pflicht.

## EN – Prompt Modes

**Conceptual (templates only in WP-113).** Three sizes with clear selection criteria: **Full Prompt** for scope lock, ADR, release prep, release readiness, security policy, and dangerous/irreversible/governance-relevant decisions; **Standard Prompt** for normal work packages, doc reviews, small status updates, predictable tasks; **Short Prompt** for well-standardized follow-up work after an existing Context Pack, small update WPs, and recurring checks. **Boundary:** a Short Prompt must **never** be used for security policy, ADR, scope lock, release, destructive changes, git write/release/tag actions, or unclear requirements — those require Full (or at least Standard).

## DE – Rollenmodell

Context Economy verbessert die Übergaben im bestehenden Rollenmodell: **Nova (ChatGPT)** – die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle – plant kompakt und liefert klare WP-Prompts; der **Implementation Agent** arbeitet gegen gezielten Kontext und liefert Rückmeldung an Nova + Compact Context Summary; der **Human Maintainer** behält die finale Kontrolle (GO / GO WITH NOTES / REWORK / STOP, Commit, Push, Tag, Release).

## EN – Role Model

Context Economy improves handovers in the existing role model: **Nova (ChatGPT)** – the ChatGPT-based planning, architecture and review role – plans compactly and delivers clear WP prompts; the **Implementation Agent** works against targeted context and delivers Report to Nova + Compact Context Summary; the **Human Maintainer** keeps final control (GO / GO WITH NOTES / REWORK / STOP, commit, push, tag, release).

## DE – Sicherheits- und Neutralitätsgrenzen

- Public Quality Gate bleibt Pflicht.
- Public Neutrality bleibt Pflicht.
- Keine Secrets.
- Keine privaten Projektdaten.
- Keine Roh-Chat-Historie.
- Keine Chain-of-Thought.
- Kein Drittanbieter-Skill-Import.
- Keine autonome Commit-/Push-/Tag-/Release-Aktion.
- Der Human Maintainer behält die finale Kontrolle.
- Short Prompts dürfen keine Sicherheitsprüfungen umgehen.
- Token-Sparen darf niemals erforderliche Evidenz entfernen.

## EN – Security and Neutrality Boundaries

Public quality gate remains mandatory; public neutrality remains mandatory; no secrets; no private project data; no raw chat history; no chain-of-thought; no third-party skill import; no autonomous commit/push/tag/release; the human maintainer retains final control; short prompts must not bypass safety checks; token saving must never remove required evidence.

## DE – Was nicht reduziert werden darf

Niemals reduziert werden: die geltenden Sicherheits-/Neutralitätsregeln, die Public-Quality-Gate-Prüfungen, die harten Grenzen eines WP, die erforderliche Evidenz für eine Entscheidung und die Human-Maintainer-Gates. Wenn Context Economy und Sicherheit in Konflikt geraten, gewinnt Sicherheit.

## EN – What Must Not Be Reduced

Never reduced: the applicable security/neutrality rules, the public quality gate checks, a WP's hard limits, the evidence required for a decision, and the human-maintainer gates. Where context economy and safety conflict, safety wins.

## DE – Anwendung in Work Packages

Pro WP: passenden Prompt Mode wählen (Full/Standard/Short nach den Kriterien oben); nur die nötigen Kontext-Schichten laden; Evidenz kompakt dokumentieren; mit Rückmeldung an Nova + Compact Context Summary abschließen. So bleibt jeder WP-Lauf nachvollziehbar und sicher, aber schlank.

## EN – Usage in Work Packages

Per WP: choose the right prompt mode (Full/Standard/Short per the criteria above); load only the needed context layers; document evidence compactly; close with Report to Nova + Compact Context Summary. Every WP run stays traceable and safe, yet lean.

## DE – Beziehung zu Claude Skills

Skills sind **späteres** Enablement — **dieses WP erstellt keine Skills.** Skills sollen wiederkehrende Standardregeln aus Prompts auslagern (z. B. Rückmeldung-an-Nova-Struktur, Neutralitätsprüfung), dürfen aber **keine** autonomen Schreib-/Release-Aktionen ermöglichen und müssen die **Skill Security Policy aus WP-110** respektieren. Das Skills-MVP-Design folgt in **WP-111**, die Implementierung bleibt **WP-112 (optional)**. Referenziertes MVP-Skill-Set (nur geplant, **nicht aktiv**): `ndf-token-economy`, `ndf-feedback-to-nova`, `ndf-work-package-runner`, `ndf-public-neutrality-guard`, `ndf-release-safety`, `ndf-adr-governance`.

## EN – Relationship to Claude Skills

Skills are **later** enablement — **this WP creates no skills.** Skills should externalize recurring standard rules from prompts (e.g., the Report-to-Nova structure, the neutrality check) but must **not** enable autonomous write/release actions and must respect the **skill security policy from WP-110**. The skills MVP design follows in **WP-111**; implementation stays **WP-112 (optional)**. The referenced MVP skill set is planned only and **not active**: `ndf-token-economy`, `ndf-feedback-to-nova`, `ndf-work-package-runner`, `ndf-public-neutrality-guard`, `ndf-release-safety`, `ndf-adr-governance`.

## DE – Beziehung zu Foundation 0.8

Context Economy ist das erste inhaltliche Deliverable von Foundation 0.8 (Agent Enablement & Context Economy). Es liefert das Prinzip, auf dem WP-113 (Context Pack Template & Prompt Modes) und die Skills (WP-111/112) aufbauen. Foundation 0.8 ist scope-locked, **nicht released**, **nicht v1.0**.

## EN – Relationship to Foundation 0.8

Context Economy is the first content deliverable of Foundation 0.8 (Agent Enablement & Context Economy). It provides the principle that WP-113 (context pack template & prompt modes) and the skills (WP-111/112) build on. Foundation 0.8 is scope-locked, **not released**, **not v1.0**.

## DE – Nicht-Ziele

Kein Skill Pack, keine `.claude/skills`, keine Cursor Rules, keine Workflows, keine Scripts in diesem WP; keine finalen Context-Pack-Templates oder Prompt-Mode-Vorlagen (WP-113); keine Chain-of-Thought-Anforderung; kein Import externer Skill-Inhalte; kein v1.0-Claim; keine aktive volle v1.x-Kompatibilitätszusage; kein Release.

## EN – Non-Goals

No skill pack, `.claude/skills`, Cursor rules, workflows, or scripts in this WP; no final context-pack templates or prompt-mode drafts (WP-113); no chain-of-thought requirement; no import of external skill content; no v1.0 claim; no active full v1.x compatibility promise; no release.

## DE – Nächste Schritte

**NDF-WP-110 – NDF Skill Security Policy / ADR-0032.** Danach WP-111 (Skills MVP Design) und WP-113 (Context Pack Template & Prompt Modes), die dieses Konzept in konkrete Vorlagen überführen.

## EN – Next Steps

**NDF-WP-110 – NDF Skill Security Policy / ADR-0032.** Then WP-111 (skills MVP design) and WP-113 (context pack template & prompt modes), which turn this concept into concrete templates.
