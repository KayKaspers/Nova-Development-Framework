# Context Pack – Foundation 0.8

> Kompakter Phasen-Snapshot nach dem [Context Pack Template](CONTEXT_PACK_TEMPLATE.md) (NDF-WP-113). Nur geprüfte, öffentliche Repo-Inhalte. Ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate und kein Human-Maintainer-Review.

## Status

`scope-locked` · **nicht released** · **nicht v1.0** · Snapshot: 2026-07-08.

## Scope

**Foundation 0.8 – Agent Enablement & Context Economy.** Kontrollierte, docs-getriebene NDF-Erweiterung: Context Economy, Skill Security, Skills MVP Design, Context Packs & Prompt Modes.

## Current Phase

Foundation 0.8.

## Current Phase Status

Scope-locked (NDF-WP-108), **release-prepared / tag pending** (NDF-WP-115). Nicht released, nicht v1.0, kein v1.0 Release Candidate. Kein aktives Skill Pack.

## Last Completed Work Package

`NDF-WP-115 – Foundation 0.8 Release Prep` — Release Notes + Go/No-Go-Checkliste + Tagging-Guide erstellt; **release-prepared / tag pending**. Kein aktives Skill Pack.

## Next Work Package

Manueller Human-Maintainer-Release (Go/No-Go → Tag `v0.8.0-foundation` → GitHub Pre-Release), danach Post-Release-Status-Cleanup-Kandidat `NDF-WP-119`.

## Release-Blocking Work Packages

- NDF-WP-108 Scope Lock — done
- NDF-WP-109 Context Economy Concept — done
- NDF-WP-110 Skill Security Policy / ADR-0032 — done
- NDF-WP-111 Skills Pack MVP Design — done
- NDF-WP-113 Context Pack Template and Prompt Modes — done
- NDF-WP-114 Release Readiness Review — done (GO WITH NOTES)
- NDF-WP-115 Release Prep — done (release-prepared / tag pending)

## Optional Work Packages

- NDF-WP-112 Skills MVP Implementation — optional, **not activated**
- NDF-WP-116 Skill-to-Cursor Rules Export Assessment — optional
- NDF-WP-117 Workflow Builder Evaluation — optional
- NDF-WP-118 Docs Polish Skill Evaluation — optional

## Deferred / Non-Goals

Vollständige Automatisierungsplattform; autonome Multi-Agent-Workflows; Scripts in Skills; netzwerkfähige Skills; Git-Schreib-/Release-/Tag-Aktionen durch Skills; Cursor-Rules-Export-Implementierung; Workflow-Implementierung; Drittanbieter-Skill-Import; private projektspezifische Skills; v1.0 RC; Aktivierung der vollen v1.x-Zusage.

## Accepted ADRs Relevant to This Phase

- `ADR-0031 – v1.x Compatibility Policy (Accepted)` — Governance-Rahmen; volle Zusage erst mit v1.0.
- `ADR-0032 – Skill Security Policy (Accepted)` — fail-closed Governance für NDF-Skills.
- Nächste freie ADR-Nummer: **ADR-0033**.

## Current Safety Boundaries

Fail closed; docs-only zuerst; keine Scripts; keine Netzwerkzugriffe; keine Secrets; keine privaten Projektdaten; keine autonomen Commit-/Push-/Tag-/Release-Aktionen; kein Drittanbieter-Skill-Import; Public Quality Gate + Public Neutrality Pflicht; Human Maintainer finale Kontrolle.

## Known Notes / Limitations

Skills bleiben Design (kein aktives Pack); WP-112 optional, nicht aktiviert; Prompt Modes/Context Packs ersetzen keine Gate-/Human-Maintainer-Prüfung; Foundation 0.8 noch nicht release-geprüft (WP-114 offen).

## Relevant Source Files

- `docs/roadmap/FOUNDATION_0_8_SCOPE_LOCK.md`, `FOUNDATION_0_8_PLAN.md`, `FOUNDATION_0_8_WORK_PACKAGES.md`
- `docs/release/FOUNDATION_0_8_RELEASE_CRITERIA.md`
- `docs/agent-workflows/NDF_CONTEXT_ECONOMY.md`, `NDF_SKILL_SECURITY_POLICY.md`, `NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md`, `NDF_PROMPT_MODES.md`
- `docs/adr/ADR-0032-skill-security-policy.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_8.md`

## Compact Context History

- WP-109: Context Economy als NDF-Prinzip definiert (5 Kontext-Schichten, Compact Context Summary verbindlich, Context Packs/Prompt Modes konzeptionell). Kein Skill Pack.
- WP-110: Skill Security Policy als ADR-0032 (Accepted) + operatives Regelwerk; fail closed; keine autonomen Git-/Release-/Netz-/Secret-Aktionen. Nächste ADR-Nummer 0033.
- WP-111: Skills Pack MVP Design (6 Skills + Review Matrix), nur Design, kein aktives Pack; WP-112 optional.
- WP-113: Prompt Modes (Full/Standard/Short) + Context Pack Template + dieses Context Pack. Kein Skill Pack.
- WP-114: Release Readiness Review — GO WITH NOTES, keine Blocker, 20-Punkte-Matrix, Dateisystemprüfung bestätigt kein aktives Skill Pack / keine `.claude/skills`.
- WP-115: Release Prep — Release Notes + Go/No-Go + Tagging-Guide erstellt; release-prepared / tag pending. Nächster Schritt: manueller Human-Maintainer-Release, dann Post-Release-Cleanup-Kandidat WP-119.

## Next Prompt Recommendation

Manueller Human-Maintainer-Release (Go/No-Go → Tag → GitHub Pre-Release); danach **Full Prompt Mode** für das Post-Release-Cleanup-WP (Kandidat NDF-WP-119).

## What Must Not Be Claimed

Keine Foundation-0.8-Release-Behauptung vor Tagging; kein v1.0; keine aktive volle v1.x-Kompatibilitätszusage; kein aktives Claude Skills Pack; keine WP-112-Aktivierung.

## What Must Not Be Included

Keine privaten Daten; keine Secrets; keine Roh-Chatlogs; keine Chain-of-Thought; keine externen Skill-Inhalte; keine riesigen Kopien.

## Update Rules

Nach jedem abgeschlossenen WP aktualisieren; nur geprüfte, öffentliche Repo-Inhalte; Compact Context Summary als Inputquelle erlaubt; ersetzt keine Prüfung der aktuellen Dateien, keinen Public Quality Gate, kein Human-Maintainer-Review.
