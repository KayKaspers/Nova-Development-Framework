# Nova Development Framework v1.0.0

## DE – Status

**Final Release vorbereitet — pending Human Maintainer release.** Diese Notes bereiten den finalen `v1.0.0`-Release vor; er ist **noch nicht veröffentlicht**. Bis zur manuellen Veröffentlichung durch den Human Maintainer gilt v1.0 **nicht** als released. Tag und GitHub-Release sind ausschließlich manuelle Human-Maintainer-Schritte (siehe [Tagging-Guide](V1_0_FINAL_TAGGING_AND_GITHUB_RELEASE_GUIDE.md)); kein Tag/Release durch einen AI-Agenten. Die volle v1.x-Kompatibilitätszusage wird **erst mit dem manuellen finalen Release wirksam** (ADR-0031) — sie wird hier nur vorbereitet, nicht aktiviert.

## EN – Status

**Final release prepared — pending human-maintainer release.** These notes prepare the final `v1.0.0` release; it is **not yet published**. Until the Human Maintainer publishes it manually, v1.0 is **not** released. Tag and GitHub release are human-maintainer-only manual steps (see the tagging guide); no tag/release by an AI agent. The full v1.x compatibility promise takes effect **only with the manual final release** (ADR-0031) — it is prepared here, not activated.

## DE – Was v1.0 umfasst

- Work-Package-Prozess (Planning → Scope Lock → Readiness → Prep → manueller Tag → Cleanup)
- Prompt Modes (Full / Standard / Short) und der Skills-first Operating Mode
- Context Packs und die Compact Context Summary
- **38 docs-only Skills** (`.claude/skills/`), fail-closed, ADR-0032-konform
- Public Neutrality (Public Quality Gate v0.2)
- ADR Governance und Release Governance
- Human-Maintainer-only-Regel (nur der Mensch committet/taggt/released)
- **v1.x Compatibility Policy** (ADR-0031) — mit finalem v1.0 aktiv
- Skill Security Policy (ADR-0032, fail-closed, docs-only)

## EN – What v1.0 Includes

The work-package process; prompt modes and the skills-first operating mode; context packs and the Compact Context Summary; **38 docs-only skills** (fail-closed, ADR-0032-compliant); public neutrality (gate v0.2); ADR and release governance; the human-maintainer-only rule; the **v1.x compatibility policy** (ADR-0031, active with final v1.0); the skill security policy (ADR-0032).

## DE – Was sich gegenüber dem RC geändert hat

- **WP-145:** 22 weitere docs-only Advisory-Skills (Skill-Pack 8 → 30).
- **WP-146:** 8 zusätzliche docs-only Advisory-Skills (Skill-Pack 30 → **38**).
- **WP-147:** v1.0 Final Readiness Review — GO WITH NOTES, keine Blocker/Gaps; **G-13-Weg C bestätigt**.
- Der veröffentlichte RC `v1.0.0-rc.1` (→ `4beab84`) bleibt unverändert; v1.0 baut darauf auf.

## EN – What Changed Since the RC

WP-145 added 22 further docs-only advisory skills (8 → 30); WP-146 added 8 more (30 → **38**); WP-147 confirmed final readiness (GO WITH NOTES, no blockers/gaps, G-13 path C). The published RC `v1.0.0-rc.1` (→ `4beab84`) stays unchanged; v1.0 builds on it.

## DE – Known Final Notes

- **G-13 (External Validation Evidence Depth)** wird über **Weg C** behandelt: **Weg A** (tieferer öffentlicher schrittbelegter Neutral-Lauf) bleibt **best-effort / future improvement**; **Weg B** (dokumentierte akzeptierte Grenze / Known Limitation) gilt für v1.0 final — **kein Blocker**, Ein-Personen-Engpass transparent, keine erfundene externe Evidenz. Siehe [Final Readiness Review](../validation/v1-0/V1_0_FINAL_READINESS_REVIEW.md).
- **Kein externes RC-Feedback erfasst** — als Known Limitation dokumentiert (kein Blocker).
- **RDS-001 / ADS-001:** die Real-use-Historie der in WP-145/WP-146 ergänzten Skills sammelt sich im Betrieb.
- **Project-Enablement-Skills und weitere Governance-Skills** bleiben post-v1.0/v1.1-Kandidaten.
- **Zweiter Fixture-Typ (Projekt mit Code)** bleibt dokumentierte Grenze/Non-Goal.

## EN – Known Final Notes

G-13 is handled via path C: path A (a deeper public step-evidenced neutral run) stays best-effort/future improvement; path B (a documented accepted boundary / known limitation) applies for v1.0 final — not a blocker, the single-maintainer bottleneck transparent, no invented external evidence. No external RC feedback was captured (documented known limitation, not a blocker). RDS-001/ADS-001 — the real-use history of the WP-145/146 skills accrues in operation. Project-enablement and further governance skills stay post-v1.0/v1.1 candidates. A second fixture type stays a documented limit/non-goal.

## DE – v1.x-Zusage

Die volle v1.x-Kompatibilitätszusage (ADR-0031) wird **erst mit dem manuellen finalen Release** durch den Human Maintainer wirksam. **Keine Aktivierung durch Claude.** Bis dahin ist sie „prepared / pending Human Maintainer final release".

## EN – v1.x Promise

The full v1.x compatibility promise (ADR-0031) takes effect **only with the manual final release** by the Human Maintainer. **No activation by Claude.** Until then it is "prepared / pending human-maintainer final release".

## DE – Human-Maintainer-only-Hinweis

Nur der Human Maintainer committet, pusht, taggt und veröffentlicht. Kein AI-Agent führt Tag-, Release- oder GitHub-Schreibaktionen aus (ADR-0032). Freigabe gemäß [Final Go/No-Go-Checkliste](V1_0_FINAL_GO_NO_GO_CHECKLIST.md); manuelle Schritte im [Tagging-Guide](V1_0_FINAL_TAGGING_AND_GITHUB_RELEASE_GUIDE.md).

## EN – Human-Maintainer-only Note

Only the Human Maintainer commits, pushes, tags, and publishes. No AI agent performs tag/release/GitHub write actions (ADR-0032). Approval per the final go/no-go checklist; manual steps in the tagging guide.

---

## DE – GitHub Release Body (kopierbar) / EN – GitHub Release Body (copy-paste)

```markdown
# Nova Development Framework v1.0.0

Final release of the Nova Development Framework — a documentation-first framework for planning, executing, and reviewing work packages with a Nova (ChatGPT) planning/architecture/review role, an implementation agent, and a Human Maintainer who alone commits, tags, and releases.

**What v1.0 includes:** the work-package process; Full/Standard/Short prompt modes and the skills-first operating mode; context packs and the Compact Context Summary; 38 docs-only, fail-closed skills; public neutrality (Public Quality Gate v0.2); ADR and release governance; the human-maintainer-only rule.

**v1.x compatibility policy (ADR-0031):** active with this final release — see the policy for compatibility categories and breaking/deprecation rules.

**Security (ADR-0032, skill security policy):** all skills are docs-only and fail-closed — no scripts, no network, no secrets, no private data, no autonomous git/release actions.

**Known final notes:** external-validation evidence depth is handled via a documented accepted boundary (a deeper public step-evidenced run stays a future improvement); no external RC feedback was captured (a documented limitation); the real-use history of the newer skills accrues in operation; project-enablement and further governance skills are post-v1.0/v1.1 candidates; a second fixture type stays a documented limit.

Not a pre-release. Built on `v1.0.0-rc.1`.
```

**Hinweis:** Der Release Body enthält keine privaten Daten, keine echten privaten Domains, keine Reviewer-Identitäten und keine falschen Claims. Er ist erst mit dem manuellen finalen Release durch den Human Maintainer gültig.
