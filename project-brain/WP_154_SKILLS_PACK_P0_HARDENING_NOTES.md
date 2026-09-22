# NDF-WP-154 – Skills Pack P0 Hardening (Notes)

> Status: **Nova-Review bestanden** — die Human-Maintainer-Annahme wird mit dem Commit wirksam, der diesen Stand trägt (kein Commit-Hash vorweggenommen). Validation: [SKILLS_PACK_P0_HARDENING.md](../docs/validation/v1-1/SKILLS_PACK_P0_HARDENING.md)

## WP / Baseline

`NDF-WP-154 – Skills Pack P0 Hardening` (docs-only / kompatibilitätssensitive Skill-Umsetzung; Full, B2-Ziel / B3-Maximum). Start-Revision `70446a3` auf `main` (WP-153 angenommen, committed, gepusht); `v1.0.0` bleibt letzter Release; v1.1 nur geplant.

## Ziel

P0-Härtung von genau sechs Skills vor der normalen v1.1-Arbeit — ohne neue, entfernte oder umbenannte Skills, ohne Provider-Mechanik, ohne ADR-Änderung.

## Dateien

- Geändert (Skills, je `SKILL.md`): `ndf-work-package-runner`, `ndf-compact-context-summary-runner`, `ndf-changelog-writer`, `ndf-release-safety`, `ndf-release-notes-runner`, `ndf-v1-readiness-review`.
- Geändert (Pack/State): `.claude/skills/README.md`, `CHANGELOG.md`, `README.md`, `docs/roadmap/V1_1_PLAN.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`, `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`.
- Neu: `docs/validation/v1-1/SKILLS_PACK_P0_HARDENING.md`, diese Notes.

## Sechs Skills (Kern)

WP-Runner = primärer docs-only Ausführungs-Router (Execution Header inkl. Legacy-Fallback, `COMPLETE`/`COMPLETE REPLACEMENT`, Delta-STOP, Profile + Budgets ohne Absenkung, Fail-Closed-Eskalation statt „unklar → Full", Preflight, sichtbarer Rahmen, 0–3 Support-Skills, Prompt-vor-Skill-Ausgabevorrang, keine Runtime); Summary-Runner ohne feste Zwei-Block-Form (Formatvorrang, Handoff-Essentials ohne Dopplung); Changelog-Writer ohne falsche „v1.x-Zusage nicht aktiv"-Invariante, nur mit CHANGELOG im Scope; Release-Safety und Release-Notes versionsneutral (pre-release/final, major/minor/patch, v1.x aktiv seit `v1.0.0`, Migration Notes, Human-Maintainer-Befehlsfolgen gemäß Execution Contract); v1-Readiness historisch/Spezialist → `ndf-release-safety` (nicht umbenannt, nicht deprecated).

## Kompatibilität

Klarstellung + verhaltensseitig non-breaking + additiv; kein Breaking Change; keine Skill-Namen entfernt/umbenannt; Full/Standard/Short und WP-152-Profile unverändert; im Frontmatter nur `description`-Text geändert.

## Integrity Lock

Sechs `SKILL.md` geändert → gespeicherte Hashes/Lock-Einträge dafür sind veraltet; Consumer mit Integrity Locks re-verifizieren vor normativer Nutzung (Refresh mit Review + Human-Maintainer-Freigabe). NDF selbst führt keinen governed Skill-Lock → kein `INTEGRITY_LOCK_SCOPE_DECISION_REQUIRED`. Pre-Change-SHA-256 im Validation-Doc.

## Validierung (kurz)

`git diff --check` sauber; Index leer; genau sechs SKILL.md geändert; Frontmatter-Keys und alle Abschnitte erhalten; Stale-Phrase-Scan sauber; Public Quality Gate self-test + strict grün (lokal ohne Denylist → CI maßgeblich); relative Links aufgelöst; keine ADR-/Block-Änderung; kein Git Write durch Claude.

## Offene Punkte

ADR-0032-Consumer-Scope (separate ADR, Kandidat ADR-0033) — unverändert offen; Trigger-Review der übrigen 32 Skills (P1/P2); Provider-Mapping der semantischen Kategorien (später); `ndf-public-release-body-reviewer` als Konsolidierungskandidat (später); formale v1-Readiness-Deprecation (P3, ADR-0031-Prozess); Foundation-0.9-Context-Pack-Drift (P1).

## Lifecycle

Nova-Implementierungsreview abgeschlossen (sechs Skills bestätigt); anschließend nur noch eine begrenzte State-Closure-Nacharbeit an Lifecycle-/Current-State-Wording — ohne SKILL.md-Änderung. Die Human-Maintainer-Annahme wird mit dem Commit wirksam, der diesen Stand trägt; erst danach ist WP-154 auch git-seitig abgeschlossen.

## Nächster WP (nicht gestartet)

**WP-155 – External Validation Improvement** — nächster geplanter WP. Nicht gestartet und keine autorisierte Ausführung, solange kein eigener vollständiger WP-155-Ausführungsprompt mit Execution Header vorliegt; Start erst nach dem Human-Maintainer-Commit dieses Stands.

## Verbotene vorzeitige Aktionen

WP-155 ohne eigenen vollständigen Ausführungsprompt oder vor dem Human-Maintainer-Commit starten; weitere SKILL.md- oder ADR-Änderungen; ADR-0033 ohne Autorisierung; private Consumer-Skill-Nutzung als autorisiert erklären; Provider-Mechanik; Staging/Commit/Push/Fetch/Tag/Release durch einen Agenten; v1.1 Scope Lock oder Release Prep.

## Compact Context Summary

WP-154 (docs-only) härtet genau sechs Skills: WP-Runner als primärer Ausführungs-Router (Execution Header, Profile/Budgets, Fail-Closed-Eskalation, 0–3 Support-Skills, Prompt-vor-Skill-Vorrang, keine Runtime), Summary-Runner mit Formatvorrang und Handoff-Essentials, versionsneutrale Changelog-/Release-Safety-/Release-Notes-Skills (v1.x aktiv seit `v1.0.0`), v1-Readiness historisch → `ndf-release-safety`; Skills-README mit Pack-Modell, Ausgabevorrang und Integrity-Lock-Hinweis. Start `70446a3`; Nova-Review bestanden, Human-Maintainer-Annahme wirksam mit dem Commit, der diesen Stand trägt; kein Breaking Change; keine ADR-Änderung; Integrity-Records der sechs Skills veraltet (Consumer re-verifizieren nach dem Commit). Nächster geplanter WP: WP-155 – External Validation Improvement (nicht gestartet, eigener vollständiger Ausführungsprompt erforderlich).
