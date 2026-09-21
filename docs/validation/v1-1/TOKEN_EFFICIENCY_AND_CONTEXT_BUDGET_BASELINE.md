# Token Efficiency & Context Budget Baseline — Validation

> Work Package: `NDF-WP-152` — Token Efficiency & Context Budget Baseline
> Type: docs-only / additive implementation (no new skill, no subsystem)

## WP

`NDF-WP-152 – Token Efficiency & Context Budget Baseline`, Skill-assisted Standard/Extended Mode, model Opus 4.8 (Fable 5 fallback path). Additive implementation of the WP-151 recommendation.

## Ziel

NDF soll längere reale Claude-Arbeitssitzungen ermöglichen: normale Work Packages laden weniger Kontext, wiederholen stabile Regeln seltener, nutzen Skills selektiver, und Session-Fortsetzungen laufen über kurze Handoffs — ohne Sicherheits-, Review-, Neutralitäts- oder Release-Gate zu schwächen.

## Ergebnis

**GO WITH NOTES – token efficiency and context budget baseline implemented.** Additiv und docs-only; keine neuen Skills; keine Skill-Entfernung/-Umbenennung; keine inkompatible Prompt-Mode-Änderung; keine Toolpflicht; kein MCP/API/OAuth/Netzwerk als NDF-Core; kein v1.1 Scope Lock/Release Prep. ADR-0031/0032 unverändert.

## Bezug zu WP-151

WP-151 (`ed2195a`) empfahl **GO additiv-schlank + project-local Pilot** und lehnte die Skills `ndf-token-budget-reviewer` / `ndf-session-handoff-runner` ab (Guidance/Template statt Skill). WP-152 setzt genau das um: Guidance-Guide + Templates + Budgets + additive Profile, **kein** neuer Skill, **kein** großes Subsystem. Nicht übernommen: eigenständiger Token-Skill, neue Governance-Ebene, Requirements-Engineering-System, Repo-Packaging/MCP/Memory-Automation als Core.

## Neue / aktualisierte Dokumente

- **Neu:** [`docs/guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md`](../../guides/TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md) (18 Abschnitte)
- **Aktualisiert (additiv):** [`docs/agent-workflows/NDF_PROMPT_MODES.md`](../../agent-workflows/NDF_PROMPT_MODES.md) — additive Profile-Sektion (Full/Standard/Short unverändert)
- **Aktualisiert (minimal):** README, CHANGELOG `[Unreleased]`, V1_1_PLAN, Context Pack, Next Phase

## Neue Templates

- [`CURRENT_STATE_TEMPLATE.md`](../../templates/CURRENT_STATE_TEMPLATE.md)
- [`SESSION_HANDOFF_TEMPLATE.md`](../../templates/SESSION_HANDOFF_TEMPLATE.md)
- [`LEAN_WP_PROMPT_TEMPLATE.md`](../../templates/LEAN_WP_PROMPT_TEMPLATE.md)
- [`REVIEW_ONLY_PROMPT_TEMPLATE.md`](../../templates/REVIEW_ONLY_PROMPT_TEMPLATE.md)
- [`FIX_PROMPT_TEMPLATE.md`](../../templates/FIX_PROMPT_TEMPLATE.md)

Alle Templates sind kurz, referenzieren stabile NDF-Regeln, enthalten die vier Kurzregeln (keep short / no history duplication / reference rules / escalate budget) und keine privaten Daten.

## Context Budgets

B0 Micro / B1 Lean (bevorzugter Normalfall) / B2 Standard / B3 Extended / B4 Exceptional; je Budget WP-Arten, Quellenanzahl, Kontextklassen, Skill-Anzahl, Governance-Anteil, Rückmeldeformat, Reviewtiefe, Eskalationsregel definiert. B4 ist kein Standard; regelmäßiger B4-Bedarf ⇒ WP splitten/neu scopen. Keine schein-präzisen Tokenzahlen.

## Prompt Profiles

Lean (B1, bevorzugter Normalfall) · Handoff (B0–B1, kein Implementierungsmodus) · Review-only (B1–B2, keine neue Umsetzung) · Fix (B0–B1, kein Scope-Ausbau). Additiv zu Full/Standard/Short; deren Semantik unverändert. Full bleibt Pflicht für Release/ADR/Security/v1.x-Kompatibilität/komplexe Reviews.

## Short Report

Kompaktes B0/B1-Rückmeldeformat (Result / Changed files / Evidence / Risks / Open questions / Next step / Compact Context Summary). B0/B1 erzeugen nicht automatisch 15–17 Abschnitte; Full-Rückmeldung bleibt für B3/B4 erlaubt; Reviewqualität darf nicht sinken.

## Evidence Pack

Kompaktes Review-Format (Relevant files / diffs / Checks run / Acceptance criteria / Known risks / Open questions) statt Rohlogs; prüfbare Evidenz bleibt erhalten.

## Skill Selection Rule

38 Skills als Bibliothek; nicht alle default aktivieren; nur die für die Aufgabe nötigen. Auswahl je Budget: B0 0–1, B1 1–3, B2 2–5, B3 4–8, B4 nur mit Begründung. Vier häufige Kandidaten benannt (work-package-runner, compact-context-summary-runner, public-neutrality-guard, changelog-writer), aber nicht blind erzwungen. Auswirkung auf die 38 Skills: **keine** — reine Nutzungsregel.

## Optional project-local tools

Repomix, Repo-Map-Tools, lokale semantische Code-Suche, Layered-Memory, Token-Optimizer — optional project-local, **nicht** NDF-Core; keine Pflicht, keine Auto-Installation, kein MCP/API/OAuth/Netzwerk als Core; Privacy/Neutrality prüfen; keine Secrets/privaten Daten in Tool-Kontext; project-local dokumentieren.

## Project-local Pilot

Archetyp: operations-oriented consumer project (neutral). Getestet: CURRENT_STATE, SESSION_HANDOFF, Lean/Review-only/Fix, B0/B1/B2, Short Report, Evidence Pack. Erfolgskriterien: mehrere zusammenhängende Schritte ohne Vollkontext, weniger Boilerplate/Dateien, klare Wiederaufnahme, keine schlechtere Reviewqualität, keine verlorenen Governance-Grenzen. Nicht enthalten: private Projektdaten, schein-präzise Tokenziele, NDF-Core-Verankerung (spätere Human-Maintainer-Entscheidung).

## Fail-Closed Rules

Lean/B0/B1 verboten für: Release-Gate, ADR-Änderung, Security Policy, v1.x-Kompatibilitätsrisiko, Breaking-Change, Migration, Datenschutz/Berechtigung, widersprüchliche Quellen, unklaren Scope, fehlende autoritative Dokumente, Public-Neutrality-Unsicherheit. Regel: fehlenden Kontext sichtbar machen, nicht raten; bei Unsicherheit Budget erhöhen / STOP / Human-Maintainer-Gate. Erweitert die bestehenden Short-Prompt-Verbote.

## ADR-0031 Bewertung

Unverändert. Alle Änderungen fallen in die Non-breaking-Kategorie der V1_1_PLAN-Grenzen (additive Doku/Guidance/Templates/optionale Profile). Keine Entfernung/Umbenennung/inkompatible Semantikänderung.

## ADR-0032 Bewertung

Unverändert. Keine Scripts, keine Automation, kein Netz/Secrets; project-local Tools ausdrücklich nicht als NDF-Core; fail-closed erhalten.

## Public Neutrality

Gewahrt. Consumer nur als neutraler Archetyp; keine privaten Projektnamen/Domains/Reviewer-Identitäten; Secret-Name genannt, Wert nie. Public Quality Gate `--strict` + `--self-test` grün.

## v1.x Compatibility

Nicht verletzt. Rein additiv; bestehende Modi/Skills/Einstiegspunkte unverändert; keine neue NDF-Version.

## Non-Goals eingehalten

Keine neuen Skills; keine Skill-Entfernung/-Umbenennung; keine inkompatible Prompt-Mode-Änderung; kein v1.1 Scope Lock; kein Release Prep; kein Requirements-Engineering-System; keine externen Tools als Core; kein MCP/API/OAuth/Netzwerk; keine Scripts; keine Git-/Release-/Tag-Aktion.

## Risiken / offene Punkte

- Lean-Übernutzung ohne Fail-Closed-Disziplin → Regeln müssen gelebt werden (im Guide zentral verankert).
- Wirksamkeit noch nicht gemessen → project-local Pilot liefert reale Vorher/Nachher-Evidenz.
- Skill-Merge/Adapter-Konsolidierung (WP-151) bleibt separatem kompatiblen WP vorbehalten.
- Roadmap-Renumbering (WP-152-Einschub) muss konsistent bleiben.

## Entscheidung

**GO WITH NOTES – token efficiency and context budget baseline implemented.** Nächster empfohlener Schritt: Human-Maintainer-Commit, dann project-local Pilot im Operations-Archetyp vor jeder NDF-Core-Härtung.
