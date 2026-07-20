# v1.1 Plan — Validation, Enablement & Operational Maturity

## DE – Titel

v1.1 Planning / Post-v1.0 Roadmap (NDF-WP-150, Skill-assisted Full Prompt Mode). Erster Post-v1.0-Zyklus nach dem finalen `v1.0.0`-Release.

## DE – Status

**Planung — nicht released.** v1.0.0 bleibt final veröffentlicht; die volle v1.x-Kompatibilitätszusage (ADR-0031) ist ab `v1.0.0` aktiv. Dieses Dokument plant v1.1; es bereitet **keinen** v1.1-Release vor und veröffentlicht nichts. Verbindliche Einstufung erst mit einem späteren v1.1 Scope Lock. Keine Breaking Changes, keine neuen Skills, keine Releases durch dieses WP.

## EN – Status

**Planning — not released.** v1.0.0 stays final; the full v1.x compatibility promise (ADR-0031) is active from `v1.0.0`. This document plans v1.1; it prepares **no** v1.1 release and publishes nothing. Binding classification only with a later v1.1 scope lock. No breaking changes, no new skills, no releases by this WP.

## DE – Ziel

Den Zustand nach v1.0.0 als Ausgangspunkt festhalten, die aktive v1.x-Kompatibilitätsverpflichtung berücksichtigen, die Known Final Notes aus [WP-149](../validation/v1-0/V1_0_FINAL_POST_RELEASE_REVIEW.md) in Roadmap-Items überführen, den v1.1-Scope und die Breaking-/Non-Breaking-Grenzen definieren und die nächsten WPs priorisieren.

## EN – Goal

Capture the post-v1.0.0 baseline, honor the active v1.x compatibility promise, map the WP-149 known final notes into roadmap items, define the v1.1 scope and breaking/non-breaking boundaries, and prioritize the next WPs.

## DE – Ausgangslage nach v1.0

- **v1.0.0 final released** (annotated Tag `v1.0.0` → finaler Commit `9dcadc1`, WP-148/149; kein AI-Git-/Release-Vorgang).
- **v1.x-Zusage aktiv ab v1.0.0** gemäß ADR-0031 (nicht rückwirkend für Foundation `v0.x` oder RC `v1.0.0-rc.1`).
- **ADR-0031 aktiv im v1.x-Kontext; ADR-0032 unverändert bindend** (docs-only, fail-closed, keine Scripts/Netz/Secrets/autonomen Git-Release-Aktionen).
- **38 docs-only Skills** unter `.claude/skills/`.
- **Public Quality Gate v0.2 grün** auf dem finalen Commit.
- **Keine offenen v1.0-Blocker.**
- **Neu (post-v1.0, Human Maintainer):** ein **erster realer Projekt-Feedback-Intake** wurde außerhalb dieses WP hinzugefügt (project-local Intake-Review). Das beginnt, die „kein externes RC-Feedback"-Grenze abzubauen, und speist die Project-Enablement- und Feedback-Triage-Planung. **Neutralitätshinweis:** projektspezifische Namen/Details bleiben project-local und werden hier nicht übernommen.

## EN – Post-v1.0 Baseline

v1.0.0 final released (annotated tag → `9dcadc1`); the v1.x promise is active from v1.0.0 (ADR-0031, not retroactive); ADR-0031 active, ADR-0032 unchanged and binding; 38 docs-only skills; gate green on the final commit; no open v1.0 blockers. New (post-v1.0, by the Human Maintainer): a first real project feedback intake was added outside this WP (a project-local intake review) — it begins to address the "no external RC feedback" boundary and feeds project-enablement/feedback-triage planning. Neutrality note: project-specific names/details stay project-local and are not carried here.

## DE – v1.1-Scope

**v1.1 = Validation, Enablement & Operational Maturity.** Schwerpunkt: die im v1.0 als future improvement / accepted limitation geführten Punkte operationell abbauen — ohne Breaking Changes.

**Ziele:**
- Skills Real-use Review (RDS-001/ADS-001, 38-Skill-Real-use-Historie).
- External Validation Improvement (G-13-Weg A: tieferer öffentlicher schrittbelegter Neutral-Lauf).
- Project Enablement Validation (Adapter/Enablement; erster Projekt-Feedback-Intake einbeziehen).
- Public Documentation Polish (README/Guides/i18n-Matrix).
- v1.x compatibility maintenance (Breaking-/Deprecation-Regeln gemäß ADR-0031 pflegen).
- Post-v1.0 risk reduction (Ein-Personen-Engpass transparent halten).

## EN – v1.1 Scope

**v1.1 = Validation, Enablement & Operational Maturity.** Focus: operationally reduce the v1.0 future-improvement/accepted-limitation items without breaking changes — skills real-use review, external validation improvement (G-13 path A), project enablement validation (incorporating the first project feedback intake), public documentation polish, v1.x compatibility maintenance, and post-v1.0 risk reduction.

## DE – Nicht-Ziele

- Breaking Changes an bestehenden Skills, Prompt Modes, Adapter-Konventionen oder öffentlichen Einstiegspunkten.
- Neue inkompatible Prompt-Strukturen.
- Nicht-ADR-konforme Skill-Automation.
- Netzwerk-/API-/MCP-/Script-Skills ohne neue ausdrückliche ADR.
- Private Projektlogik/-namen/-domains im Public NDF.
- v1.1-Release durch dieses WP; autonome Git-/Release-Aktionen.

## EN – Non-Goals

Breaking changes to existing skills/prompt-modes/adapter-conventions/public entry points; new incompatible prompt structures; non-ADR-compliant skill automation; network/API/MCP/script skills without a new explicit ADR; private project logic/names/domains in public NDF; a v1.1 release by this WP; autonomous git/release actions.

## DE – Known Final Notes → Roadmap-Mapping

Status: planned · candidate · accepted limitation · non-goal · future improvement.

| Note ID | Note | Post-v1.0 Status | Empfohlener WP | Priorität | v1.x-Kompatibilitätsrisiko | Begründung |
|---|---|---|---|---|---|---|
| RDS-001 | Real-use-Historie der 22 WP-145-Skills | future improvement | **WP-151** | **P0** | gering (additiv) | frischste Betriebs-Evidenz zuerst auswerten |
| ADS-001 | Real-use-Historie der 8 WP-146-Skills | future improvement | **WP-151** | **P0** | gering | mit RDS-001 gemeinsam auswerten |
| — | 38-Skill-Real-use-Historie gesamt | future improvement | **WP-151** | P1 | gering | Nutzen/Trigger-Qualität/Sprawl beobachten |
| G-13 (Weg A) | External Validation Evidence Depth | future improvement | **WP-152** | **P1** | gering (additive Evidenz) | größter v1.0-Vorbehalt; für v1.1 stärken |
| — | „kein externes RC-Feedback" | accepted limitation → **teilweise adressiert** | **WP-152/WP-153** | P1 | gering | erster Projekt-Feedback-Intake (project-local) speist Enablement/Feedback-Triage |
| — | Project Enablement / weitere Skills | candidate / future improvement | **WP-153** | P1 | gering | Adapter/Enablement praktisch validieren |
| — | Public Documentation Polish | planned | **WP-154** | P2 | gering | Doku-Feinschliff, keine Substanzänderung |
| — | zweiter Fixture-Typ (Projekt mit Code) | non-goal (v1.0) → candidate (v1.1) | **WP-152** (optional) | P3 | gering | optional in External Validation; sonst weiter Non-Goal |
| — | Ein-Personen-Engpass | accepted limitation (strukturell) | — (in jedem WP transparent) | P2 (tracked) | keine | strukturell nicht vor v1.1 lösbar; ehrlich benannt |
| — | v1.x-Kompatibilität aktiv | planned (maintenance) | **WP-155/156** | P1 | — | Breaking-/Deprecation-Regeln pflegen (ADR-0031) |

## EN – Known Final Notes → Roadmap Mapping

The table maps each note to a post-v1.0 status, a recommended WP, a priority (P0–P3), a v1.x-compatibility risk, and a rationale: RDS-001/ADS-001 and the 38-skill real-use history → WP-151 (skills real-use review); G-13 path A → WP-152 (external validation improvement); the "no external RC feedback" limitation is now partially addressed by the first project feedback intake → WP-152/153; project enablement/further skills → WP-153; public docs polish → WP-154; a second fixture type moves from non-goal to a v1.1 candidate (optional in WP-152); the single-maintainer bottleneck stays an accepted structural limitation (tracked); v1.x compatibility maintenance → WP-155/156.

## DE – v1.x Compatibility Boundaries (für v1.1)

| Kategorie | Beispiele |
|---|---|
| **Non-breaking (erlaubt in v1.1)** | additive neue docs-only Skills (ADR-0032-konform); additive Doku/Validierungsdokumente; additive Roadmap-/Context-Pack-Updates; Klarstellungen/Politur ohne Semantikänderung; zusätzliche optionale Prompt-Profile |
| **Needs ADR** | jede Erweiterung des Skill-Security-Scopes (Scripts/Netz/Secrets/Automation); jede Lockerung von ADR-0031/0032; neue Fähigkeitsklassen; Änderung der Denylist-Governance |
| **Breaking (nicht ohne v-Bump/Deprecation)** | Entfernen/Umbenennen bestehender Skills, auf die WPs verweisen; inkompatible Änderung etablierter Prompt-Mode-Semantik; nicht-additive Änderung der Adapter-Konventionen; Entfernen öffentlicher Einstiegspunkte |
| **Human-Maintainer-only** | alle Commit/Push/Tag/Release; jede ADR-Annahme; jeder v1.1-Release; jeder Scope-Change; GO/GO WITH NOTES/REWORK/STOP |

**Grundsatz:** v1.1 bleibt in der v1.x-Kompatibilität; Erweiterungen sind additiv; Breaking Changes erfordern eine ausdrückliche Deprecation-/ADR-Entscheidung des Human Maintainers gemäß ADR-0031.

## EN – v1.x Compatibility Boundaries (for v1.1)

The table separates non-breaking (additive docs-only skills/docs/roadmap updates, clarifications, optional prompt profiles), needs-ADR (any skill-security-scope extension, any ADR-0031/0032 relaxation, new capability classes, denylist-governance changes), breaking (removing/renaming depended-on skills, incompatible prompt-mode semantics, non-additive adapter-convention changes, removing public entry points), and human-maintainer-only (all commit/push/tag/release, ADR acceptance, v1.1 release, scope changes, decisions). Principle: v1.1 stays within v1.x compatibility; extensions are additive; breaking changes need an explicit human-maintainer deprecation/ADR decision per ADR-0031.

## DE – Work Packages (Post-v1.0-Reihenfolge)

**Reconciliation-Hinweis:** WP-149 hatte eine vorläufige Reihenfolge (WP-152/153/151/154) genannt; dieser Plan übernimmt die **saubere aufsteigende Nummerierung** WP-151…156 und ersetzt die vorläufige Zuordnung.

| WP | Ziel | Scope | Nicht-Ziele | Erwartete Artefakte | Prompt Mode | Modell | v1.x-Risiko | Erwartete Entscheidung |
|---|---|---|---|---|---|---|---|---|
| **WP-151 – Skills Real-use and Context Efficiency Review** *(präzisiert aus „Skills Real-use Review")* | RDS-001/ADS-001 + 38-Skill-Real-use auswerten **und** das reale Token-/Kontextproblem analysieren (Kontextklassen, Context Budgets, Lean-Prompt-Architektur, Session-Handoff, WP-152-Entscheidungsvorlage) | Nutzen/Trigger-Qualität/Overlap/Sprawl; Context-Efficiency-Modelle; Empfehlungen | neue Skills, Skill-Umbau, Token-System-Implementierung | Review-Doc + Notes ([Review](../validation/v1-1/SKILLS_REAL_USE_AND_CONTEXT_EFFICIENCY_REVIEW.md)) | Skill-assisted Extended Review | Fable 5 / Opus 4.8 | gering | GO WITH NOTES |
| **WP-152 – External Validation Improvement** | G-13-Weg A angehen | tieferer öffentlicher schrittbelegter Neutral-Lauf; ggf. zweiter Fixture-Typ; Feedback-Intake einordnen | erfundene Evidenz, private Daten | Validation-Doc + Notes | Skill-assisted Full | Opus 4.8 | gering (additiv) | GO WITH NOTES |
| **WP-153 – Project Enablement Validation** | Adapter/Enablement praktisch validieren | Adapter-Qualität/Neutralität; ersten Projekt-Feedback-Intake neutral einbeziehen | private Projektlogik im Public NDF, Auto-Migration | Validation-Doc + Notes | Skill-assisted Full | Opus 4.8 | gering | GO WITH NOTES |
| **WP-154 – Public Documentation Polish** | Doku-Feinschliff | README/Guides/i18n-Matrix; Klarheit/Konsistenz | Substanz-/Governance-Änderung | Doku-Updates + Notes | Skill-assisted Standard | Opus 4.8 | gering | GO WITH NOTES |
| **WP-155 – v1.1 Readiness Review** | v1.1-Reife prüfen | Check gegen v1.1-Scope + v1.x-Kompatibilität | Release-Erstellung | Readiness-Doc + Notes | Skill-assisted Full | Opus 4.8 | mittel | GO WITH NOTES / REWORK |
| **WP-156 – v1.1 Release Prep** | v1.1-Release vorbereiten (nur Doku) | Release Notes/Go-No-Go/Tagging-Guide (Tag `v1.1.0`) | Tag/Release durch AI | Release-Prep-Docs + Notes | Skill-assisted Full | Opus 4.8 | mittel | GO WITH NOTES – pending Human Maintainer |

**Begründung der Reihenfolge:** zuerst Betriebs-Evidenz der Skills (151, frischste Notes, geringstes Risiko), dann der größte v1.0-Vorbehalt External Validation (152), dann Enablement mit realem Feedback (153), dann Doku-Polish (154), dann Readiness (155) und Release Prep (156). Optional/parallel und nicht blockierend: WP-130/131/132 (0.9-Optional-Assessments).

## EN – Work Packages (post-v1.0 order)

Reconciliation note: WP-149 gave a tentative order (152/153/151/154); this plan adopts the clean ascending numbering WP-151…156 and supersedes it. The table sequences WP-151 (skills real-use review) → WP-152 (external validation improvement, G-13 path A) → WP-153 (project enablement validation) → WP-154 (public documentation polish) → WP-155 (v1.1 readiness review) → WP-156 (v1.1 release prep, docs only), with goal, scope, non-goals, expected artifacts, prompt mode, model, v1.x risk, and expected decision. Rationale: operational skill evidence first (freshest notes, lowest risk), then the biggest v1.0 caveat (external validation), then enablement with real feedback, then docs polish, then readiness and release prep.

## DE – Risks / Open Notes

- **Skill-Sprawl (38 Skills):** in WP-151 auf Nutzen/Trigger-Qualität prüfen; ggf. Konsolidierung (nur additiv/mit WP-Scope).
- **G-13-Weg A** braucht einen realen öffentlichen Lauf — Ein-Personen-Engpass bleibt begrenzend (WP-152).
- **Projekt-Feedback-Neutralität:** projektspezifische Details bleiben project-local; Public NDF neutral halten (WP-153).
- **v1.x-Kompatibilität:** Breaking Changes vermeiden; Deprecation nur per ADR/Human-Maintainer.
- **Kein Zeitplan;** dieser Plan ist kein Scope Lock.

## EN – Risks / Open Notes

Skill-sprawl (38 skills) to be reviewed in WP-151 (possible additive consolidation with a WP scope); G-13 path A needs a real public run (single-maintainer bottleneck limiting, WP-152); project-feedback neutrality (project-specific details stay project-local, WP-153); avoid breaking changes (deprecation only via ADR/human-maintainer); no schedule; this plan is not a scope lock.

## DE – Decision

**GO WITH NOTES – v1.1 planning started.** v1.0.0 bleibt final veröffentlicht; v1.x-Zusage aktiv; v1.1 = Validation, Enablement & Operational Maturity, nur geplant (nicht released); Known Final Notes in WP-151…156 überführt; keine Breaking Changes, keine neuen Skills, keine Releases. ADR-0031/0032 unverändert. **Nächster empfohlener WP: WP-151 – Skills Real-use and Context Efficiency Review** *(Titel nach der Planung präzisiert: zusätzlich Context-Efficiency-Analyse und WP-152-Entscheidungsvorlage).*

## EN – Decision

**GO WITH NOTES – v1.1 planning started.** v1.0.0 stays final; the v1.x promise is active; v1.1 = Validation, Enablement & Operational Maturity, planned only (not released); known final notes mapped into WP-151…156; no breaking changes, new skills, or releases. ADR-0031/0032 unchanged. Next recommended WP: WP-151 – Skills Real-use and Context Efficiency Review (title precisified post-planning).
