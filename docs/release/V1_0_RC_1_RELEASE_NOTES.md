# Nova Development Framework v1.0.0-rc.1 Release Candidate

## DE – Status

**Release Candidate — nicht final v1.0.** `v1.0.0-rc.1` ist ein **Kandidat** zur Validierung des v1.0-Pfads. **Keine volle v1.x-Kompatibilitätszusage ist aktiv** (ADR-0031; die volle Zusage tritt erst mit finalem `v1.0.0` in Kraft). Dieser RC ist **vorbereitet, aber nicht veröffentlicht**: Tag und GitHub-Release sind ausschließlich manuelle Human-Maintainer-Schritte (siehe Tagging-Guide). Kein Tag, kein Release durch einen AI-Agenten.

## EN – Status

**Release candidate — not final v1.0.** `v1.0.0-rc.1` is a candidate for validating the v1.0 path. **No full v1.x compatibility promise is active** (ADR-0031; the full promise takes effect only with final `v1.0.0`). This RC is **prepared but not published**: tag and GitHub release are human-maintainer-only manual steps (see the tagging guide). No tag, no release by an AI agent.

## DE – Was dieser RC validiert

- Work-Package-Prozess (Planning → Scope Lock → Readiness → Prep → manueller Tag → Cleanup)
- Prompt Modes (Full / Standard / Short) und der Skills-first Operating Mode
- Context Packs und die Compact Context Summary
- Public Neutrality (Public Quality Gate v0.2)
- ADR Governance und Release Governance
- Human-Maintainer-only-Regel (nur der Mensch committet/taggt/released)
- v1.x Compatibility Policy **vorbereitet, aber noch nicht final aktiv** (ADR-0031)
- Skill Security Policy (ADR-0032, fail-closed, docs-only)

## EN – What This RC Validates

The work-package process; prompt modes and the skills-first operating mode; context packs and the Compact Context Summary; public neutrality (gate v0.2); ADR and release governance; the human-maintainer-only rule; the v1.x compatibility policy (prepared but not yet finally active, ADR-0031); the skill security policy (ADR-0032, fail-closed, docs-only).

## DE – Wichtigste enthaltene Ergebnisse

- **Foundation 0.9** (`v0.9.0-foundation`, released/published — reconciliation documented): Adoption, Validation & Optional Enablement.
- **Skills-first-Strang WP-125…WP-138:** docs-only Skill-Pack mit **acht** Skills (vier Core-MVP + vier Extended-Core), Skills-first Operating Mode, real-use-validierte Prompt-Kompression.
- **WP-139** v1.0 Gap Review & Scope Lock (Scope-Lock-Kandidat; 9 Met, 8 Met with notes, 1 tracked Gap, keine Blocker).
- **WP-140** External Validation Evidence Review (G-13 Partially closed / tracked for RC; RC can proceed with notes).
- **WP-141** v1.0 Release Criteria Finalization (RC-Kriterien RC-01…13 vs. Final-Kriterien F-01…07).
- **WP-142** v1.0 RC Readiness Review (GO WITH NOTES – ready for v1.0 RC Release Prep).

## EN – Key Included Results

Foundation 0.9 (`v0.9.0-foundation`); the skills-first strand WP-125…WP-138 (an eight-skill docs-only pack, the skills-first operating mode, real-use-validated prompt compression); WP-139 (v1.0 gap review & scope lock), WP-140 (external validation evidence review), WP-141 (release criteria finalization), WP-142 (RC readiness review).

## DE – Known RC Notes

- **G-13 External Validation Evidence Depth** bleibt `tracked` (begrenzte Schrittbeleg-Tiefe; ein Lauf privat-kontextuell). Kein RC-Blocker.
- **ECS-001** Extended-Core-Skill-Real-use-Historie `partially closed`.
- **RC ist nicht final** — keine v1.0-Reife wird behauptet.
- **Volle v1.x-Kompatibilitätszusage erst mit finalem v1.0** (ADR-0031).
- **Project-Enablement-Skills** optional/post-v1.0.
- **Optionale Governance-Skills** (`ndf-release-safety`, `ndf-adr-governance-review`) optional.
- **Zweiter Fixture-Typ (Projekt mit Code)** bleibt dokumentierte Grenze.
- **RC-01 (Gate grün)** und **RC-10 (Changelog/RC-Notes)** sind auf dem tatsächlichen RC-Commit erneut zu bestätigen.

## EN – Known RC Notes

G-13 stays tracked (limited per-step depth; one private-context run), not an RC blocker; ECS-001 partially closed; the RC is not final (no v1.0 maturity claimed); the full v1.x promise only at final v1.0; project-enablement skills optional/post-v1.0; optional governance skills optional; a second fixture type stays a documented limit; RC-01 (gate green) and RC-10 (changelog/RC notes) must be re-confirmed on the actual RC commit.

## DE – Upgrade-/Usage-Hinweis

Dieser RC eignet sich zum **Testen und Review des v1.0-Pfads** (Arbeitsweise, Governance, Skills, Adapter-Konventionen). Er ist **nicht** als finale v1.0-Kompatibilitätszusage zu behandeln — Konventionen können sich bis zum finalen v1.0 noch ändern (governed über ADR-0031). Rückmeldungen zum RC fließen in die v1.0-Final-Entscheidung ein (RC als Validierungsvehikel).

## EN – Upgrade / Usage Note

This RC is suitable for testing and reviewing the v1.0 path (way of working, governance, skills, adapter conventions). It must **not** be treated as a final v1.0 compatibility promise — conventions may still change until final v1.0 (governed via ADR-0031). RC feedback feeds the v1.0 final decision (the RC as a validation vehicle).

## DE – Human-Maintainer-only-Hinweis

Nur der Human Maintainer committet, pusht, taggt und veröffentlicht. Kein AI-Agent führt Tag-, Release- oder GitHub-Schreibaktionen aus (ADR-0032). Die manuellen Schritte stehen im [Tagging- und GitHub-Release-Guide](V1_0_RC_1_TAGGING_AND_GITHUB_RELEASE_GUIDE.md); die Freigabe erfolgt gemäß [Go/No-Go-Checkliste](V1_0_RC_1_GO_NO_GO_CHECKLIST.md).

## EN – Human-Maintainer-only Note

Only the Human Maintainer commits, pushes, tags, and publishes. No AI agent performs tag/release/GitHub write actions (ADR-0032). Manual steps are in the tagging guide; approval follows the go/no-go checklist.
