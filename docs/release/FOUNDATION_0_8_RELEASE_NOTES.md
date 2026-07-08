# Foundation 0.8 Release Notes

## DE – Status

**Release-prepared / tag pending.** Foundation 0.8 ist vorbereitet, aber **nicht released**, bis der Human Maintainer den manuellen Release (Tag + GitHub Pre-Release) abschließt. Geplanter Tag: `v0.8.0-foundation`. Nicht v1.0, kein v1.0 Release Candidate.

## EN – Status

**Release-prepared / tag pending.** Foundation 0.8 is prepared but **not released** until the Human Maintainer completes the manual release (tag + GitHub pre-release). Planned tag: `v0.8.0-foundation`. Not v1.0, no v1.0 release candidate.

## DE – Release-Typ

Foundation **Pre-Release** (`v0.8.0-foundation`), Titel „Nova Development Framework v0.8.0 Foundation".

## EN – Release Type

Foundation **pre-release** (`v0.8.0-foundation`), title "Nova Development Framework v0.8.0 Foundation".

## DE – Zusammenfassung

Foundation 0.8 – **Agent Enablement & Context Economy** operationalisiert die in 0.7 gefestigte NDF-Governance für wiederkehrende Agenten-/Claude-Abläufe: bewusster Kontext-/Tokenverbrauch, sichere Skill-Governance und konkrete Vorlagen — ohne Sicherheit, Review oder Neutralität zu reduzieren. Es ist eine kontrollierte, dokumentationsgetriebene Erweiterung, kein großer Feature-Release und **kein v1.0-Schritt**.

## EN – Summary

Foundation 0.8 – **Agent Enablement & Context Economy** operationalizes the NDF governance consolidated in 0.7 for recurring agent/Claude workflows: deliberate context/token usage, safe skill governance, and concrete templates — without reducing safety, review, or neutrality. It is a controlled, documentation-driven extension, not a large feature release, and **not a v1.0 step**.

## DE – Was neu ist

- **NDF Context Economy** als offizielles Arbeitsprinzip (fünf Kontext-Schichten, verbindliche Compact Context Summary) — WP-109.
- **NDF Skill Security Policy** als **ADR-0032** (Accepted) + operatives Regelwerk: fail closed, keine autonomen Git-/Release-/Netz-/Secret-Aktionen — WP-110.
- **NDF Claude Skills Pack MVP Design** (sechs Skills, nur Design, kein aktives Pack) — WP-111.
- **NDF Prompt Modes** (Full/Standard/Short) + **Context Pack Template** + erstes Foundation-0.8 Context Pack — WP-113.
- **Release Readiness Review**: GO WITH NOTES, keine Blocker — WP-114.

## EN – What Is New

NDF Context Economy as an official working principle (five context layers, binding Compact Context Summary — WP-109); NDF Skill Security Policy as ADR-0032 (Accepted) + operative rule set: fail closed, no autonomous git/release/network/secret actions (WP-110); NDF Claude Skills Pack MVP design (six skills, design only, no active pack — WP-111); NDF Prompt Modes (Full/Standard/Short) + Context Pack Template + first Foundation 0.8 Context Pack (WP-113); release readiness review: GO WITH NOTES, no blockers (WP-114).

## DE – Release-blocking Work Packages

WP-108 Scope Lock · WP-109 Context Economy Concept · WP-110 Skill Security Policy / ADR-0032 · WP-111 Skills Pack MVP Design · WP-113 Context Pack Template & Prompt Modes · WP-114 Release Readiness Review (GO WITH NOTES) · WP-115 Release Prep (dieses WP).

## EN – Release-Blocking Work Packages

WP-108/109/110/111/113/114/115 — all complete or prepared; the final tag + GitHub pre-release remain a manual human-maintainer step.

## DE – Optionale Work Packages

Nicht aktiviert: **WP-112** (Skills MVP Implementation, nur per Human-Maintainer-Scope-Change hochstufbar), **WP-116** (Skill-to-Cursor-Export-Assessment), **WP-117** (Workflow-Builder-Evaluation), **WP-118** (Docs-Polish-Skill-Evaluation).

## EN – Optional Work Packages

Not activated: WP-112 (skills MVP implementation, upgradable only via human-maintainer scope change), WP-116/117/118 (assessments/evaluations).

## DE – Wichtige Sicherheitsgrenzen

Gemäß **ADR-0032** (fail closed): Skills docs-only zuerst; keine Scripts im MVP; keine Netzwerkzugriffe; keine Secrets; keine privaten Projektdaten; keine autonomen Commit-/Push-/Tag-/Release-Aktionen; kein Drittanbieter-Skill-Import; Public Quality Gate + Public Neutrality Pflicht; Human Maintainer bleibt finaler Owner.

## EN – Important Security Boundaries

Per ADR-0032 (fail closed): skills docs-only first; no scripts in the MVP; no network access; no secrets; no private project data; no autonomous commit/push/tag/release actions; no third-party skill import; public quality gate + public neutrality mandatory; the human maintainer stays final owner.

## DE – Skill-Pack-Status

**Kein aktives Claude Skills Pack.** Das Skills-MVP existiert ausschließlich als **Design** (WP-111). Es wurden keine `.claude/skills`, keine `SKILL.md` und keine neuen Skill-Scripts erstellt. Eine tatsächliche Implementierung (WP-112) erfordert einen ausdrücklichen Human-Maintainer-Scope-Change und bleibt strikt docs-only.

## EN – Skill Pack Status

**No active Claude Skills Pack.** The skills MVP exists only as **design** (WP-111). No `.claude/skills`, `SKILL.md`, or new skill scripts were created. An actual implementation (WP-112) requires an explicit human-maintainer scope change and stays strictly docs-only.

## DE – Context Economy

Die Prompt Modes machen die Kontext-/Token-Sparsamkeit praktisch nutzbar: **Full** für governance-/release-kritische Arbeit, **Standard** für normale WPs, **Short** nur für standardisierte Folgearbeit mit aktuellem Context Pack. Short Prompt ist für ADR/Security/Scope Lock/Release/destructive/Git-Write-Tag-Release/unklare Anforderungen ausdrücklich verboten.

## EN – Context Economy

The prompt modes make context/token economy usable: Full for governance/release-critical work, Standard for normal WPs, Short only for standardized follow-up work with a current Context Pack. Short Prompt is explicitly forbidden for ADR/security/scope lock/release/destructive/git-write-tag-release/unclear requirements.

## DE – ADRs

**ADR-0031** (v1.x Compatibility Policy) und **ADR-0032** (Skill Security Policy) sind Accepted. Nächste freie ADR-Nummer: **ADR-0033**. Keine ADR-Massenmigration.

## EN – ADRs

ADR-0031 (v1.x compatibility policy) and ADR-0032 (skill security policy) are Accepted. Next free ADR number: ADR-0033. No ADR mass migration.

## DE – Bekannte Notes / Limitations

- Foundation 0.8 ist bis zum manuellen Release durch den Human Maintainer **nicht released**.
- Foundation 0.8 ist **nicht v1.0** und kein v1.0 Release Candidate.
- Die volle v1.x-Kompatibilitätszusage ist **nicht aktiv** (erst mit einem künftigen v1.0-Release).
- **WP-112 bleibt optional und nicht aktiviert.**
- Es existiert **kein aktives Claude Skills Pack**; das MVP ist nur Design.
- Eine tatsächliche Skill-Implementierung erfordert einen ausdrücklichen Human-Maintainer-Scope-Change.
- Der Public Quality Gate bleibt Pflichtinvariante.
- Der Human Maintainer kontrolliert Commit, Push, Tag und Release.

## EN – Known Notes / Limitations

Foundation 0.8 is not released until the manual release by the human maintainer; not v1.0 and no v1.0 release candidate; the full v1.x compatibility promise is not active (only at a future v1.0 release); WP-112 remains optional and not activated; no active Claude Skills Pack exists (MVP is design only); an actual skill implementation requires an explicit human-maintainer scope change; the public quality gate remains mandatory; the human maintainer controls commit, push, tag, and release.

## DE – Nicht-Ziele

Kein v1.0 und kein v1.0 Release Candidate; keine aktive volle v1.x-Kompatibilitätszusage; kein aktives Skill Pack; keine Skill-Scripts; keine netzwerkfähigen Skills; keine autonomen Git-/Release-Aktionen; keine Automatisierungsplattform; keine Cursor-Rules/Workflows; kein Drittanbieter-Skill-Import; kein History-Rewrite.

## EN – Non-Goals

No v1.0 and no v1.0 release candidate; no active full v1.x compatibility promise; no active skill pack; no skill scripts; no network-enabled skills; no autonomous git/release actions; no automation platform; no Cursor rules/workflows; no third-party skill import; no history rewrite.

## DE – Upgrade- / Nutzungsnotizen

Foundation 0.7 bleibt veröffentlicht (Tag `v0.7.0-foundation`). Foundation 0.8 ist additiv: keine Migrationsschritte, keine ersetzten Artefakte. Wer 0.7 nutzt, erhält zusätzlich Context Economy, die Skill Security Policy (ADR-0032), das Skills-MVP-Design und die Prompt Modes / Context Packs.

## EN – Upgrade / Usage Notes

Foundation 0.7 stays published (tag `v0.7.0-foundation`). Foundation 0.8 is additive: no migration steps, no replaced artifacts — users of 0.7 additionally get context economy, the skill security policy (ADR-0032), the skills MVP design, and the prompt modes / context packs.

## DE – Nächste Schritte nach Veröffentlichung

1. Manuell (Human Maintainer): Go/No-Go-Checkliste, Tag `v0.8.0-foundation`, GitHub Pre-Release.
2. Danach ein Post-Release-Status-Cleanup-WP (Kandidat `NDF-WP-119`): Foundation 0.8 auf released/published heben, Tag/Release read-only verifizieren.
3. Optional (nur per Human-Maintainer-Scope-Change): WP-112 Skills MVP Implementation.

## EN – Next Steps After Publication

(1) Manually: go/no-go checklist, tag `v0.8.0-foundation`, GitHub pre-release; (2) then a post-release status cleanup WP (candidate `NDF-WP-119`): lift Foundation 0.8 to released/published, verify tag/release read-only; (3) optionally (only via human-maintainer scope change): WP-112 skills MVP implementation.

---

## GitHub Release Body (Vorschlag / suggested)

```text
Nova Development Framework v0.8.0 Foundation is an agent enablement and context economy
pre-release.

Highlights:
- NDF Context Economy defined (five context layers, binding Compact Context Summary)
- NDF Skill Security Policy accepted as ADR-0032 (fail closed; no autonomous
  commit/push/tag/release, no network, no secrets, no scripts in the MVP)
- NDF Claude Skills Pack MVP designed (six skills, design only)
- NDF Prompt Modes (Full/Standard/Short) and Context Pack template added
- Release readiness review completed with no blockers (GO WITH NOTES)

Known notes:
- No active Claude Skills Pack is created; the MVP exists as design only.
- WP-112 (skills MVP implementation) remains optional and not activated.
- The full v1.x compatibility promise is not active before a future v1.0 release.

This is not a v1.0 release. Full DE/EN release notes:
docs/release/FOUNDATION_0_8_RELEASE_NOTES.md

---

DE: Agent-Enablement- und Context-Economy-Pre-Release. Kein v1.0; die volle
v1.x-Kompatibilitätszusage ist vor einem künftigen v1.0-Release nicht aktiv. Kein aktives
Skill Pack. Vollständige zweisprachige Release Notes im Repository unter
docs/release/FOUNDATION_0_8_RELEASE_NOTES.md.
```
