# Project Brain – WP-111 NDF Claude Skills Pack MVP Design Notes

## Summary

MVP-Design des NDF Claude Skills Pack erstellt: `docs/agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md` (DE/EN) mit sechs Skills, je vollständiger Spezifikation, integrierter Review Matrix, gemeinsamen Regeln, WP-112-Grenze und Nicht-Zielen. **Nur Design — kein aktives Skill Pack, keine `.claude/skills`/`SKILL.md`/Scripts.** Kein Release, kein v1.0. Empfehlung: **GO WITH NOTES**.

## Inputs reviewed

0.8 Scope Lock/Plan/Queue/Criteria, Context Economy (WP-109), Skill Security Policy + ADR-0032 (WP-110), ADR/README, NEXT_PHASE_0_8, WP-109/110-Brain-Notizen, README, CHANGELOG. Gate strict/self-test grün, Working Tree sauber (WP-110 `e47ba06`).

## MVP Design

Grundsätze: klein/fokussiert (genau 6 Skills), docs-only zuerst, fail closed, additiv, human-first. Sicherheitsbasis vollständig aus ADR-0032 übernommen. Pflichtstatus „Design only / kein aktives Skill Pack / keine `.claude/skills` / keine Scripts / keine autonomen Git-Release-Aktionen" enthalten.

## MVP Skill Set

Genau sechs: `ndf-token-economy`, `ndf-feedback-to-nova`, `ndf-work-package-runner`, `ndf-public-neutrality-guard`, `ndf-release-safety`, `ndf-adr-governance`. Keine weiteren, keine optionalen hochgezogen. Future/optional nur benannt: `ndf-evidence-review`, `ndf-skill-builder`, `ndf-workflow-builder`, `ndf-docs-polish`, `ndf-cursor-rules-export`.

## Skill specifications

Je Skill dokumentiert: Name, Zweck, Wann nutzen/nicht nutzen, erlaubte/verbotene Inputs, erlaubte/verbotene Outputs, Pflichtprüfungen, Pflicht-Handover, Security Notes, Bezug zu anderen NDF-Docs. Zusätzlich integrierte Review Matrix (Skill/Zweck/Trigger/erlaubte+verbotene Outputs/Security-Checks/Handover/MVP-Status) — alle sechs auf „MVP-Status: Design". Kein separates Matrix-Dokument nötig (kompakt).

## Shared skill rules

Alle Skills: docs-only; keine Scripts/Netzwerk/Secrets/privaten Daten/Drittanbieter-Inhalte; keine Git-Schreib-/Release-/Tag-/destruktiven Aktionen; Gate + Neutralität + Human-Gates respektieren; Rückmeldung an Nova + Compact Context Summary unterstützen.

## Security boundaries

Vollständig aus ADR-0032 abgeleitet (fail closed). `ndf-public-neutrality-guard` kennt/dokumentiert keine Secret-Werte (Secret-Name nur als Name); `ndf-release-safety` löst nie Tag/Release aus; `ndf-adr-governance` finalisiert nichts ohne Human-Maintainer-Review; `ndf-token-economy` reduziert nie erforderliche Evidenz/Sicherheit.

## Relationship to ADR-0032

Jeder Skill hält die Skill Security Policy ein; die Grenzen jedes Skills spiegeln die Policy direkt. Kein Skill ermöglicht autonome Aktionen.

## Relationship to Context Economy

`ndf-token-economy` und `ndf-feedback-to-nova` operationalisieren Compact Context Summary + Kontextverdichtung ohne Sicherheits-/Evidenz-Verlust. Prompt Modes und Context-Pack-Templates bleiben WP-113.

## WP-112 boundary

WP-112 bleibt optional; WP-111 aktiviert es nicht. Implementierung nur per ausdrücklichem Human-Maintainer-Scope-Change; docs-only, sofern nicht spätere ADR-/Scope-Entscheidung mehr erlaubt; keine Scripts/Netz/Git-Writes/Release-Tag/Secrets/privaten Daten. Keine stille Aktivierung.

## Foundation 0.8 updates

WP-111 in Queue/Criteria/Plan als erledigt; **WP-113 (Context Pack Template & Prompt Modes) als nächster release-blocking Schritt**; WP-112 optional. README (DE/EN): Link auf MVP Design (als „geplantes Skills-MVP (Design)"). CHANGELOG: WP-111-Zeile. NEXT_PHASE_0_8 aktualisiert.

## What was not done

Keine aktiven Skills; keine `.claude/skills`/`SKILL.md`/Skill-Dateien; keine Cursor-Rules/Workflows/Scripts/Netzwerk-Tools; kein Drittanbieter-Skill-Import; keine WP-112-Aktivierung; kein Commit/Push/Tag/Release; kein v1.0-Claim; Foundation 0.8 nirgends als released dargestellt.

## Risks

Gering: Risiko „Skills wirken aktiv" → Pflichtstatus + Review-Matrix-Spalte „MVP-Status: Design" + durchgehende „nur Design"-Formulierung. Risiko stiller WP-112-Aktivierung → eigener Abschnitt „Beziehung zu WP-112" mit expliziter Nicht-Aktivierung. WP-113 muss Prompt Modes/Templates liefern, ohne den MVP-Scope zu überdehnen.

## Recommendation

**GO WITH NOTES** — Design sauber, sicher und neutral; bewusste Note: kein aktives Skill Pack, WP-112 bleibt optional, WP-113 liefert Templates/Prompt Modes.

## Compact Context Summary

Foundation 0.8 (scope-locked, Agent Enablement & Context Economy). **WP-111 done:** `docs/agent-workflows/NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md` (DE/EN) designt 6 MVP-Skills (`ndf-token-economy`, `-feedback-to-nova`, `-work-package-runner`, `-public-neutrality-guard`, `-release-safety`, `-adr-governance`) mit Spezifikationen + Review Matrix + gemeinsamen Regeln + WP-112-Grenze. Nur Design, kein aktives Skill Pack, keine `.claude/skills`/Scripts. ADR-0032-konform (fail closed). Release-blocking done: 108/109/110/111. Nächster Schritt WP-113 (Context Pack Template & Prompt Modes). WP-112 optional, nicht aktiviert. Nächste freie ADR-Nummer 0033. Kein Release, kein v1.0.
