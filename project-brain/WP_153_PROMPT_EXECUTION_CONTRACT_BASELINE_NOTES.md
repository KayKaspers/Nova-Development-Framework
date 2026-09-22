# NDF-WP-153 – Prompt Execution Contract Baseline (Notes)

> Status: **pending Nova/Human review** — Annahme erst durch Nova-Review + Human-Maintainer-Commit. Validation: [PROMPT_EXECUTION_CONTRACT_BASELINE.md](../docs/validation/v1-1/PROMPT_EXECUTION_CONTRACT_BASELINE.md)

## WP / Baseline

`NDF-WP-153 – Prompt Execution Contract Baseline` (docs-only, Full / Governance implementation, inkl. Final Rework). Start-Revision `c4c1c34` auf `main`; `v1.0.0` bleibt letzter Release; v1.1 nur geplant.

## Ziel

Framework-weiter Ausführungsvertrag für Agent-Prompts und Human-Maintainer-Befehlsfolgen — ohne Runtime oder Tooling.

## Dateien

- Neu: `framework/prompts/blocks/BLOCK_EXECUTION_CONTRACT.md`, `docs/validation/v1-1/PROMPT_EXECUTION_CONTRACT_BASELINE.md`, diese Notes.
- Geändert: `WORK_PACKAGE_LIFECYCLE.md`, `NDF_PROMPT_MODES.md`, Templates LEAN_WP / REVIEW_ONLY / FIX / SESSION_HANDOFF, `standards/git-standard.md`, `NDF_SKILL_SECURITY_POLICY.md`, `TOKEN_EFFICIENCY_AND_CONTEXT_BUDGET_BASELINE.md`, `V1_1_PLAN.md`, `CHANGELOG.md`, `CONTEXT_PACK_FOUNDATION_0_9.md`, `NEXT_PHASE_FOUNDATION_0_9.md`, `PROMPT_INDEX.md`, `README.md`.

## Human-Maintainer-Entscheidungen (Kern)

Vier Session-Werte (Begründung außer bei `SAME_SESSION_ALLOWED`); neue Prompts ohne Deklaration = Defekt, Legacy-Prompts nicht blockierend (`NEW_SESSION_RECOMMENDED` + `SESSION_DECLARATION_MISSING_LEGACY`); vollständiger Ersatz statt Delta, enge Option-Selection-Ausnahme; Prompt-Format vor generischem Skill-Output; vollständige CLI-Befehlsfolgen; ADR-0032-Consumer-Scope → separate ADR; Roadmap WP-153/154 eingefügt, WP-155…159 folgen.

## Kompatibilität

Additiv + Klarstellung; verhaltensseitig non-breaking (Legacy-Fallback); kein Breaking Change; ADR-0032-Consumer-Scope bewusst vertagt.

## Validierung (kurz)

`git diff --check` sauber; Public Quality Gate self-test + strict grün (lokal ohne Denylist → CI maßgeblich); relative Links aufgelöst; keine SKILL.md-/ADR-Änderung; Index leer; kein Git Write durch Claude.

## Offene Punkte

Ältere Foundation-0.9-Context-Pack-Felder (P1-State-Härtung); ADR-0032-Consumer-Scope (separate ADR, Kandidat ADR-0033). Geklärt (Final Authority Reconciliation): Nova gibt Review-Verdikte ab, der Human Maintainer bleibt finaler Owner von Annahme, Scope, ADR und Git/Release (`NOVA_REVIEW != HUMAN_ACCEPTANCE`; Block, Lifecycle §6, Skill Security Policy und v1.1-Plan abgeglichen); „Legacy" = vor dem Human-Maintainer-Commit, der WP-153 annimmt (kein Hash eingebettet).

## Nächster WP (nur nach Annahme)

**WP-154 – Skills Pack P0 Hardening** — erst nach Nova-/Human-Maintainer-Annahme und Human-Maintainer-Commit von WP-153, mit eigenem vollständigem Ausführungsprompt.

## Verbotene vorzeitige Aktionen

WP-154 vor Annahme starten; SKILL.md- oder ADR-Änderungen; ADR-0033 ohne Autorisierung; private Consumer-Skill-Nutzung als autorisiert erklären; Staging/Commit/Push/Fetch/Tag/Release durch einen Agenten; v1.1 Scope Lock oder Release Prep.

## Compact Context Summary

WP-153 (docs-only) verankert den NDF-Ausführungsvertrag in `BLOCK_EXECUTION_CONTRACT.md`: Session-Deklaration (vier Werte, Legacy-Fallback), vollständige Ausführungsanweisungen (complete ≠ verbose), vollständiger Ersatz statt Delta mit enger Option-Selection-Ausnahme, Prompt-vor-Skill-Ausgabevorrang, CLI-Abdeckung; Anker in Lifecycle, Prompt Modes, Templates, Git-Standard, Skill Security Policy und Guide; Prompt Index und README nachgezogen; Roadmap WP-153…159. Start `c4c1c34`; pending Nova/Human review; keine SKILL.md-/ADR-Änderung; v1.1 planning only. Nächster WP nach Annahme: WP-154.
