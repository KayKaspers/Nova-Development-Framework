# Expected Adapter Output – SampleProject (für NDF-WP-047)

## DE – Zweck

Dieses Dokument definiert, welche Artefakte der Project-Adapter-Durchlauf in NDF-WP-047 erzeugen bzw. bewerten soll. Die Outputs werden **erst in WP-047 erstellt** — hier steht nur die Erwartung.

## EN – Purpose

This document defines which artifacts the project adapter run in NDF-WP-047 is expected to produce or assess. The outputs are **created in WP-047 only** — this file states the expectation.

## Erwartete Artefakte / Expected artifacts

| Artefakt | Quelle im Fixture | Erwartung |
|---|---|---|
| Review Report | alle Fixture-Dateien | erkennt: Doku-Widersprüche (Port), Destructive-Kandidaten (Notiz-Löschung, `reset-db.sh`), Secret-Handling-Lücke, rote CI, geteilten Admin |
| Project Profile | PROJECT_BRIEF, CURRENT_STATE | beschreibt Realität, nicht Wunschzustand |
| Project Manifest | PROJECT_BRIEF | neutrale Platzhalter (`SampleProject`, `<project-owner>`) |
| Project Brain | CURRENT_STATE, ROADMAP | Stand, Entscheidungen, nächste Schritte |
| Capability Matrix | MOCK_REPOSITORY_TREE, ARCHITECTURE_OVERVIEW | Docker ✓, CI vorhanden-aber-rot, Tests unklar, Docs lückenhaft |
| Compliance Check | RISKS, SECURITY_NOTES | `fail`-Punkte werden zu Work-Package-Quellen, kein Blocker |
| Health Score (initial) | alle | evidenzbasiert; niedrige Werte bei Security/Doku/Release Readiness erwartet; `n/a` wo keine Grundlage |
| Initial Work Package Queue | Review-Ergebnisse | 3–6 kleine typisierte WPs mit eigenem Präfix (nicht `SP-WP` blind kopieren — Template-Regel beachten) |
| First Safe Work Package | Queue | review-only oder docs-only (erwartbar: Doku-/Port-Klärung), **nicht** die Löschfunktion |

## Erwartete Klassifizierungen / Expected classifications

- Notiz-Löschung und `reset-db.sh`: erfasst als Kandidaten für `destructive-blueprint` — **keine Implementierung**.
- Secret-Handling: Kandidat für `security-baseline` → später `security-code-fix` (fail-closed).
- NDF-Level: ehrliche Einstufung im unteren Bereich mit Begründung (`docs/project-starter/NDF_LEVEL_GUIDE.md`).

## Bewertungsregeln für WP-047 / Assessment rules

1. Jede Phase des Adapters (0–10 gemäß `docs/project-starter/PROJECT_ADAPTER_V0_2.md`) wird durchlaufen oder ihr Auslassen begründet.
2. Abweichungen zwischen erwarteten und tatsächlichen Outputs sind **Findings** — sie bewerten den Adapter, nicht das Fixture.
3. Findings, die den Adoptionsbeweis betreffen, folgen der Scope-Lock-Regel (release-blocking Folge-WPs); alles andere wird dokumentiert.
4. Neutralität gilt auch für alle erzeugten Outputs (new-file neutrality check vor dem Commit).
