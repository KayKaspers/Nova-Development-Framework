# Foundation 0.8 Release Readiness Review

## DE – Zweck

Review-Gate (NDF-WP-114, Full Prompt Mode) vor der Release-Vorbereitung von voraussichtlich `v0.8.0-foundation`: Prüfung aller release-blocking Kriterien, der Skill-Sicherheitsgrenzen, der Context-Economy-Artefakte, des Quality Gates und der öffentlichen Einstiegspunkte. Ergebnis: **GO WITH NOTES**. Foundation 0.8 ist **nicht released**, **nicht v1.0** und **kein v1.0 Release Candidate**. Es existiert **kein aktives Skill Pack**.

## EN – Purpose

Review gate (NDF-WP-114, Full Prompt Mode) before the release preparation of presumably `v0.8.0-foundation`: verification of all release-blocking criteria, the skill security boundaries, the context economy artifacts, the quality gate, and the public entry points. Result: **GO WITH NOTES**. Foundation 0.8 is **not released**, **not v1.0**, and **no v1.0 release candidate**. **No active skill pack** exists.

## DE – Status

Foundation 0.8 ist scope-locked (NDF-WP-108) und mit diesem Review bereit für **NDF-WP-115 – Release Prep**. Noch nicht released; Tag `v0.8.0-foundation` noch nicht gesetzt.

## EN – Status

Foundation 0.8 is scope-locked (NDF-WP-108) and, with this review, ready for **NDF-WP-115 – Release Prep**. Not yet released; tag `v0.8.0-foundation` not yet set.

## DE – Review-Ergebnis

**GO WITH NOTES.** Alle inhaltlichen release-blocking WPs (108/109/110/111/113) sind erledigt und nachgewiesen; keine Blocker. Die Notes sind ausschließlich non-blocking und bewusst (Foundation 0.8 unreleased/nicht v1.0, WP-112 optional, kein aktives Skill Pack).

## EN – Review Result

**GO WITH NOTES.** All content release-blocking WPs (108/109/110/111/113) are complete and evidenced; no blockers. The notes are exclusively non-blocking and deliberate (Foundation 0.8 unreleased/not v1.0, WP-112 optional, no active skill pack).

## DE – Geprüfter Scope

Scope Lock (NDF-WP-108) eingehalten: Agent Enablement & Context Economy, blocking Kern 108/109/110/111/113/114/115, optional 112 (mit Upgrade-Regel)/116/117/118, deferred Automatisierungsplattform/Scripts-in-Skills/netzwerkfähige Skills/Git-Release-Aktionen durch Skills/Cursor-Export/Workflows/Drittanbieter-Import/v1.0-RC. Kein Scope Creep; die WP-112-Upgrade-Regel wurde nicht gezogen; kein Skill Pack, keine `.claude/skills`, keine neuen Skill-Scripts erzeugt.

## EN – Reviewed Scope

Scope lock honored: blocking core 108/109/110/111/113/114/115, optional 112 (with upgrade rule)/116/117/118, deferred items intact. No scope creep; the WP-112 upgrade rule was not pulled; no skill pack, `.claude/skills`, or new skill scripts were created.

## DE – Readiness Matrix / EN – Readiness Matrix

| # | Kriterium / Criterion | Status | Nachweis / Evidence |
|---|---|---|---|
| 1 | Scope Lock completed | **Met** | `FOUNDATION_0_8_SCOPE_LOCK.md` (WP-108) |
| 2 | Context Economy Concept completed | **Met** | `docs/agent-workflows/NDF_CONTEXT_ECONOMY.md` (WP-109) |
| 3 | Skill Security Policy / ADR-0032 completed | **Met** | `ADR-0032-skill-security-policy.md` (Accepted) + `NDF_SKILL_SECURITY_POLICY.md` (WP-110) |
| 4 | Claude Skills Pack MVP Design completed | **Met** | `NDF_CLAUDE_SKILLS_PACK_MVP_DESIGN.md` (WP-111, Design only) |
| 5 | Context Pack Template and Prompt Modes completed | **Met** | `NDF_PROMPT_MODES.md`, `CONTEXT_PACK_TEMPLATE.md`, `CONTEXT_PACK_FOUNDATION_0_8.md` (WP-113) |
| 6 | WP-112 remains optional and not activated | **Met** | Scope Lock + Queue: optional, Upgrade-Regel nicht gezogen |
| 7 | No active Claude Skills Pack exists | **Met** | Dateisystemprüfung: kein aktives Pack |
| 8 | No `.claude/skills` or `SKILL.md` files exist | **Met** | kein `.claude`-Verzeichnis, keine `SKILL.md` getrackt |
| 9 | No scripts or executable skill tooling added | **Met** | keine neuen Scripts in `docs/agent-workflows/`; Altbestand-Scripts unverändert |
| 10 | No network-enabled skills exist | **Met** | ADR-0032 verbietet Netzwerkzugriffe; keine Skills existent |
| 11 | No autonomous Git / tag / release capability exists | **Met** | ADR-0032 + Policy: fail closed, Human-Maintainer-only |
| 12 | Public Quality Gate strict passed | **Met** | `--strict`: passed (0/0) |
| 13 | Public Quality Gate self-test passed | **Met** | `--self-test`: passed |
| 14 | Public Neutrality clean | **Met** | Kontroll-Greps sauber |
| 15 | README / CHANGELOG status consistent | **Met** | 0.8 scope-locked, nicht released |
| 16 | Foundation 0.8 not marked as released | **Met** | keine „0.8 released"-Treffer |
| 17 | No v1.0 claim | **Met** | v1.0 nur als Abgrenzung/Pfad/Nicht-Ziel |
| 18 | No active full v1.x compatibility promise | **Met** | ADR-0031: aktiv erst mit v1.0 |
| 19 | Context Pack current enough for WP-115 | **Met with notes** | `CONTEXT_PACK_FOUNDATION_0_8.md` aktuell bis WP-113; wird in WP-114/115 fortgeschrieben |
| 20 | Release Prep can start after WP-114 if no blockers remain | **Met** | keine Blocker; WP-115 kann starten |

## DE – Release-blocking Work Packages

108 Scope Lock ✅ · 109 Context Economy Concept ✅ · 110 Skill Security Policy / ADR-0032 ✅ · 111 Skills Pack MVP Design ✅ · 113 Context Pack Template & Prompt Modes ✅ · 114 Readiness Review ✅ (dieses Dokument) · **115 Release Prep ⬜ offen**.

## EN – Release-Blocking Work Packages

108/109/110/111/113 done; 114 done (this document); **115 Release Prep open**.

## DE – Optionale Work Packages

Keines blockiert: **WP-112** (Skills MVP Implementation) optional, **nicht aktiviert** (Upgrade-Regel nicht gezogen); **WP-116** (Skill-to-Cursor-Export-Assessment), **WP-117** (Workflow-Builder-Evaluation), **WP-118** (Docs-Polish-Skill-Evaluation) optional, nicht aktiviert.

## EN – Optional Work Packages

None blocks: WP-112 optional, not activated (upgrade rule not pulled); WP-116/117/118 optional, not activated.

## DE – Sicherheits- und Neutralitätsprüfung

Public Quality Gate `--strict` und `--self-test` grün; new-file neutrality check aktiv. Keine privaten Projekt-/Personennamen, Reviewer-Identitäten, Kontaktwege, echten Domains oder Secret-Werte in getrackten Dateien. „chain-of-thought"/„raw chat" kommen ausschließlich als Verbot vor. Der Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden, der Wert nie.

## EN – Security and Neutrality Review

Public quality gate strict + self-test green; new-file neutrality check active. No private names, reviewer identities, contacts, domains, or secret values in tracked files. "chain-of-thought"/"raw chat" appear only as prohibitions. Naming `NDF_PUBLIC_NEUTRALITY_DENYLIST` is allowed, its value never.

## DE – Skill-Pack-Prüfung

Dateisystemprüfung bestätigt: **kein `.claude`-Verzeichnis, keine `.claude/skills`, keine `SKILL.md`, keine neuen Skill-Scripts.** Das Skills-MVP existiert ausschließlich als Design (WP-111). Eine tatsächliche Skill-Implementierung erfordert einen ausdrücklichen Human-Maintainer-Scope-Change (WP-112, optional). Die vorhandenen Repo-Scripts (`scripts/check_public_quality.py`, `scripts/check-repository-safety.sh`, Cleanup-Scripts) sind legitimer Altbestand — kein Skill-Verstoß.

## EN – Skill Pack Review

Filesystem check confirms: **no `.claude` directory, no `.claude/skills`, no `SKILL.md`, no new skill scripts.** The skills MVP exists only as design (WP-111). An actual skill implementation requires an explicit human-maintainer scope change (WP-112, optional). The existing repo scripts are legitimate pre-existing tooling — no skill violation.

## DE – Context-Economy-Prüfung

WP-109 (Context Economy Concept) und WP-113 (Prompt Modes + Context Pack Template + Foundation-0.8 Context Pack) sind konsistent: die fünf Kontext-Schichten, die verbindliche Compact Context Summary und die Full/Standard/Short Prompt Modes sind dokumentiert; Short Prompt ist für kritische Arbeit (ADR/Security/Scope Lock/Release/destructive/Git-Write-Tag-Release/unklare Anforderungen) ausdrücklich verboten. Token-Sparen entfernt keine Sicherheit/Evidenz.

## EN – Context Economy Review

WP-109 and WP-113 are consistent: the five context layers, the binding Compact Context Summary, and the Full/Standard/Short prompt modes are documented; Short Prompt is explicitly forbidden for critical work. Token saving removes no safety/evidence.

## DE – ADR-Prüfung

ADR-0031 (v1.x Compatibility Policy) und ADR-0032 (Skill Security Policy) sind **Accepted**; keine alten ADRs umnummeriert, keine Massenmigration. Nächste freie ADR-Nummer: **ADR-0033** (konsistent in `docs/adr/README.md`).

## EN – ADR Review

ADR-0031 and ADR-0032 are Accepted; no old ADRs renumbered, no mass migration. Next free ADR number: ADR-0033 (consistent in the ADR index).

## DE – v1.0-Abgrenzung

Foundation 0.8 ist **kein v1.0-Schritt**: es operationalisiert die Arbeitsweise (Context Economy, Skill-Governance), adressiert aber kein offenes v1.0-Kriterium direkt. Kein 0.8-Dokument stellt v1.0 als erreicht oder eine volle v1.x-Zusage als aktiv dar (ADR-0031: aktiv erst mit v1.0).

## EN – v1.0 Boundary

Foundation 0.8 is **not a v1.0 step**: it operationalizes the way of working but addresses no open v1.0 criterion directly. No 0.8 document presents v1.0 as reached or a full v1.x promise as active (ADR-0031: active only at v1.0).

## DE – Bekannte Notes / Limitations

- Foundation 0.8 ist noch nicht released.
- Foundation 0.8 ist nicht v1.0.
- Die volle v1.x-Kompatibilitätszusage ist nicht aktiv (erst mit v1.0).
- WP-112 bleibt optional und nicht aktiviert.
- Es existiert kein aktives Claude Skills Pack.
- Das Skills-MVP existiert nur als Design.
- Eine tatsächliche Skill-Implementierung erfordert einen ausdrücklichen Human-Maintainer-Scope-Change.
- Public Quality Gate bleibt Pflichtinvariante.
- Der Human Maintainer kontrolliert Commit, Push, Tag und Release.

## EN – Known Notes / Limitations

Foundation 0.8 is not released yet; not v1.0; the full v1.x compatibility promise is not active; WP-112 remains optional and not activated; no active Claude Skills Pack exists; the skills MVP exists only as design; an actual skill implementation would require an explicit human-maintainer scope change; the public quality gate remains mandatory; the human maintainer controls commit, push, tag, and release.

## DE – Blocker

**Keine.** Alle release-blocking Kriterien außer WP-114 (dieses Dokument) und WP-115 sind erfüllt und nachgewiesen.

## EN – Blockers

**None.** All release-blocking criteria except WP-114 (this document) and WP-115 are met and evidenced.

## DE – Empfehlung

**GO WITH NOTES.** Foundation 0.8 ist bereit für die Release-Vorbereitung (NDF-WP-115). Die Notes sind ausschließlich non-blocking. WP-115 muss Release Notes, Go/No-Go-Checkliste und Tagging-Guide erstellen.

## EN – Recommendation

**GO WITH NOTES.** Foundation 0.8 is ready for release preparation (NDF-WP-115). The notes are exclusively non-blocking. WP-115 must create release notes, a go/no-go checklist, and a tagging guide.

## DE – Nächster Schritt

**NDF-WP-115 – Foundation 0.8 Release Prep** (Release Notes inkl. der Known Notes, Kriterien-Abschluss, Go/No-Go-Checkliste, Tagging-Guide für voraussichtlich `v0.8.0-foundation`).

## EN – Next Step

**NDF-WP-115 – Foundation 0.8 Release Prep** (release notes incl. the known notes, criteria completion, go/no-go checklist, tagging guide for presumably `v0.8.0-foundation`).
