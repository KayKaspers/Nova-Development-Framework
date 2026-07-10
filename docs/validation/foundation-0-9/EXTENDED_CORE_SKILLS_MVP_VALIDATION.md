# Extended Core Skills MVP Validation

## DE – Zweck

Validierung der docs-only Extended-Core-Skills-Implementierung (NDF-WP-137, Skill-assisted Full Prompt Mode) gegen den [Extended Skills Pack Blueprint](EXTENDED_SKILLS_PACK_BLUEPRINT.md) (WP-136), die [Skill Security Policy](../../agent-workflows/NDF_SKILL_SECURITY_POLICY.md) und [ADR-0032](../../adr/ADR-0032-skill-security-policy.md). Geprüft wird, dass **genau vier** neue Core-Skills docs-only, fail-closed und ADR-0032-konform angelegt wurden — ohne die optionalen +2, ohne Scripts/Netz/Secrets/private Daten/Git-Release-Aktionen und ohne funktionalen Umbau der bestehenden MVP-Skills.

## EN – Purpose

Validation of the docs-only extended-core-skills implementation (NDF-WP-137) against the Extended Skills Pack Blueprint (WP-136), the Skill Security Policy, and ADR-0032. It verifies that **exactly four** new core skills were created docs-only, fail-closed, and ADR-0032-compliant — without the optional +2, without scripts/network/secrets/private data/git-release actions, and without functionally rebuilding the existing MVP skills.

## DE – Ergebnis

**GO WITH NOTES.** Vier neue docs-only Core-Skills als `SKILL.md` angelegt; Skill-Index aktualisiert; keine optionalen +2; keine Extended-Release-/ADR-Skills; bestehende MVP-Skills unverändert; ADR-0032 unverändert bindend; Public Quality Gate v0.2 grün; kein v1.0.

## EN – Result

**GO WITH NOTES.** Four new docs-only core skills created as `SKILL.md`; skill index updated; no optional +2; no extended release/ADR skills; existing MVP skills unchanged; ADR-0032 unchanged and binding; Public Quality Gate v0.2 green; not v1.0.

## DE – Angelegte / geänderte Artefakte

- `.claude/skills/ndf-skill-quality-reviewer/SKILL.md` (NEU)
- `.claude/skills/ndf-existing-project-analysis-runner/SKILL.md` (NEU)
- `.claude/skills/ndf-docs-polish-runner/SKILL.md` (NEU)
- `.claude/skills/ndf-changelog-writer/SKILL.md` (NEU)
- `.claude/skills/README.md` (dokumentarisch um die vier neuen Skills ergänzt)

Der Skill-Pack umfasst nun **acht** docs-only Skills (vier Core-MVP aus WP-129 + vier Extended-Core aus WP-137).

## EN – Created / Changed Artifacts

The four new `SKILL.md` files plus the documentary README update. The pack now holds **eight** docs-only skills (four core MVP from WP-129 + four extended core from WP-137).

## DE – Validierungs-Matrix / EN – Validation Matrix

| # | Kriterium / Criterion | Status | Nachweis / Evidence |
|---|---|---|---|
| 1 | Genau vier neue Skills | **Met** | vier neue `SKILL.md` unter `.claude/skills/` |
| 2 | Keine optionalen +2 Skills | **Met** | kein `ndf-release-safety` / `ndf-adr-governance-review` angelegt |
| 3 | Keine Extended-Release-/ADR-Skills | **Met** | wie #2 |
| 4 | Alle Skill-Dateien Markdown-only | **Met** | ausschließlich `.md` |
| 5 | Keine Scripts / ausführbaren Dateien | **Met** | keine `.py`/`.sh`/`.js`/ausführbaren Dateien |
| 6 | Kein Netzwerk | **Met** | keine Netzwerklogik in Skills |
| 7 | Keine Secrets | **Met** | nur Secret-**Name**, kein Wert |
| 8 | Keine privaten Daten | **Met** | Neutralitäts-Scan sauber |
| 9 | Keine privaten Projektnamen | **Met** | keine realen Projektnamen |
| 10 | Keine echten privaten Domains | **Met** | keine Domains/URLs |
| 11 | Keine Git-/Release-/Tag-Aktionen | **Met** | Git nur als Self-Check-Hinweis |
| 12 | ADR-0032 unverändert | **Met** | Policy-Datei unberührt |
| 13 | Public Neutrality eingehalten | **Met** | Gate `--strict` + `--self-test` grün |
| 14 | Bestehende Skills nicht funktional umgebaut | **Met** | nur README dokumentarisch ergänzt |
| 15 | Skills ersetzen keine Gates | **Met** | Guard/Reviewer verweisen auf realen Gate |
| 16 | Skills ersetzen keine Human Review | **Met** | Human-Maintainer-only-Grenzen je `SKILL.md` |
| 17 | 13-Pflichtfelder je `SKILL.md` | **Met** | Title…Interaction in jeder Datei |
| 18 | Foundation 0.9 bleibt nicht v1.0 | **Met** | Statusdokumente/Kontroll-Greps sauber |

## DE – Known Notes

- **ECS-001:** Der Token-Economy-Nutzen der Extended-Core-Skills ist qualitativ erwartet (advisory Strukturierung), aber die reale Vorher/Nachher-Messung bleibt der Real-use-Validierung (WP-138) vorbehalten — konsistent mit DSK-001 (Partially closed).
- **ECS-002:** `ndf-existing-project-analysis-runner` ist der neutralitätssensibelste neue Skill; seine Grenze „keine privaten Projektinhalte im Public NDF" ist explizit verankert.
- **ECS-003:** `ndf-changelog-writer` und (nicht implementiert) `ndf-release-safety` bleiben strikt ohne Release-/Tag-/Versionsauslösung.

## EN – Known Notes

ECS-001 — token-economy benefit is qualitatively expected; real before/after measurement stays with the real-use validation (WP-138), consistent with DSK-001. ECS-002 — the existing-project-analysis runner is the most neutrality-sensitive new skill; its "no private project content in public NDF" boundary is explicit. ECS-003 — the changelog writer (and the not-implemented release-safety) stay strictly without release/tag/version triggering.

## DE – Sicherheits- / ADR-0032-Bewertung

Alle vier neuen Skills sind docs-only und fail-closed; verboten und nicht enthalten: Scripts, Netzwerk, Secrets, private Daten, autonome Git-/Release-/Tag-Aktionen, Tool-Orchestrierung. Jede `SKILL.md` trägt die 13 Pflichtfelder inkl. erlaubter/verbotener Aktionen, Fail-closed-Verhalten, Public-Neutrality- und ADR-0032-Grenzen sowie Human-Maintainer-only-Grenzen. ADR-0032 bleibt unverändert; die bestehenden MVP-Skills wurden nicht funktional umgebaut (nur der README-Index wurde ergänzt).

## EN – Security / ADR-0032 Assessment

All four new skills are docs-only and fail-closed; scripts, network, secrets, private data, autonomous git/release/tag actions, and tool orchestration are forbidden and absent. Each `SKILL.md` carries the 13 required fields. ADR-0032 stays unchanged; the existing MVP skills were not functionally rebuilt (only the README index was extended).

## DE – Nächster Schritt

**NDF-WP-138 – Skill Prompt Compression Real-use Validation** (schließt DSK-001/ECS-001 mit realer Vorher/Nachher-Messung). Danach optional ein **Project Enablement Skills Blueprint**, dann **v1.0 Gap Review & Scope Lock**. Die optionalen +2 Core-Skills (`ndf-release-safety`, `ndf-adr-governance-review`) bleiben Kandidaten für ein späteres, ausdrücklich gescoptes WP. Nächste freie ADR-Nummer: 0033.

## EN – Next Step

**NDF-WP-138 – Skill Prompt Compression Real-use Validation** (closes DSK-001/ECS-001 with a real before/after measurement). Then optionally a **Project Enablement Skills Blueprint**, then **v1.0 gap review & scope lock**. The optional +2 core skills stay candidates for a later, explicitly scoped WP. Next free ADR number: 0033.
