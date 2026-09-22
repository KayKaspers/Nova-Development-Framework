# NDF Project Adapter v0.2

> Sprachstatus / Language status: bilingual DE/EN (NDF-WP-157). Vorherige Fassung war DE-only. / Previously DE-only; now bilingual.
>
> Konventionen / Conventions: Seit Foundation 0.4 gelten verbindliche Manifest-, Output-Pfad- und Health-Score-Konventionen — siehe [PROJECT_ADAPTER_CONVENTIONS.md](PROJECT_ADAPTER_CONVENTIONS.md). Kurz: `PROJECT_MANIFEST.md` ist kanonisch (Markdown), Validierungsoutput liegt unter `examples/<fixture>/adapter-validation-output/` getrennt von erwartetem Output, und der Health Score nutzt die 0.4-Kategorien mit `unknown`/`n/a`-Regeln. / Binding manifest, output-path, and health-score conventions have applied since Foundation 0.4 — see [PROJECT_ADAPTER_CONVENTIONS.md](PROJECT_ADAPTER_CONVENTIONS.md). In short: `PROJECT_MANIFEST.md` is canonical (Markdown), validation output lives under `examples/<fixture>/adapter-validation-output/` separate from expected output, and the Health Score uses the 0.4 categories with `unknown`/`n/a` rules.

## DE – 1. Zweck

Der Project Adapter überführt ein bestehendes Softwareprojekt strukturiert in das Nova Development Framework — ohne Neustart, ohne riskante Umbauten, ohne dass das Projekt instabil wird.

Ergebnis ist ein vollständiges NDF Project System im Zielprojekt: Profil, Manifest, Project Brain, Capability Matrix, Compliance Check, Health Score und eine typisierte Work Package Queue.

## EN – 1. Purpose

The Project Adapter carries an existing software project into the Nova Development Framework in a structured way — no restart, no risky rework, no instability introduced into the project.

The result is a complete NDF Project System in the target project: Profile, Manifest, Project Brain, Capability Matrix, Compliance Check, Health Score, and a typed Work Package Queue.

## DE – 2. Wann nutzt man den Adapter?

- Ein bestehendes Projekt soll künftig nach NDF weiterentwickelt werden.
- Ein Projekt braucht eine ehrliche Standortbestimmung (Doku, CI, Security, Release-Reife).
- Ein Team will KI-gestützte Umsetzung mit menschlicher Kontrolle einführen.

Nicht nötig: für neue Projekte — dafür gibt es den Project Starter (`docs/project-starter/NEW_PROJECT_FLOW.md`).

## EN – 2. When to Use the Adapter

- An existing project is to be developed under NDF going forward.
- A project needs an honest status assessment (docs, CI, security, release readiness).
- A team wants AI-assisted implementation with human control.

Not needed for new projects — that's what the Project Starter is for (`docs/project-starter/NEW_PROJECT_FLOW.md`).

## DE – 3. Voraussetzungen

- Lese-Zugriff auf das Zielprojekt-Repository (lokal oder remote).
- Ein menschlicher Maintainer, der Entscheidungen trifft und Commits freigibt.
- Grundverständnis der NDF-Rollen und Work-Package-Typen (`framework/standards/WORK_PACKAGE_TYPES.md`).

## EN – 3. Prerequisites

- Read access to the target project's repository (local or remote).
- A human maintainer who makes decisions and approves commits.
- Basic understanding of NDF roles and work-package types (`framework/standards/WORK_PACKAGE_TYPES.md`).

## DE – 4. Rollenmodell

```text
Nova (Planung) -> Implementation Agent (Ausführung) -> Human Maintainer (Review & Freigabe)
```

- **Nova** plant die Adapter-Phasen als Work Packages und reviewt die Ergebnisse.
- **Der Implementation Agent** (z. B. Claude) analysiert read-only und erstellt die NDF-Artefakte.
- **Der menschliche Maintainer** prüft jede Phase, entscheidet GO / REWORK / SPLIT / STOP und führt Commits aus.

**PREPARED vs. AUTHORIZED:** Was der Implementation Agent read-only liefert (Intake-Entwurf, Analyse, Artefaktvorschlag) ist **PREPARED** — vorbereitend, beratend, nie für sich genommen ausreichend, um eine Phase freizugeben. Erst was der Human Maintainer bestätigt oder liefert — insbesondere Ziele, Sicherheits-Ausschlüsse und Public/Private-Status im Intake (Phase 0) — ist **AUTHORIZED** und erlaubt den Übergang zur nächsten Phase. Diese Trennung ist eine bestehende, strukturelle Eigenschaft des Rollenmodells, kein neues Gate.

## EN – 4. Role Model

```text
Nova (planning) -> Implementation Agent (execution) -> Human Maintainer (review & approval)
```

- **Nova** plans the adapter phases as work packages and reviews the results.
- **The Implementation Agent** (e.g. Claude) analyses read-only and produces the NDF artifacts.
- **The human maintainer** reviews each phase, decides GO / REWORK / SPLIT / STOP, and performs commits.

**PREPARED vs. AUTHORIZED:** whatever the Implementation Agent delivers read-only (an intake draft, an analysis, a proposed artifact set) is **PREPARED** — preparatory, advisory, never by itself sufficient to advance a phase. Only what the Human Maintainer confirms or supplies — in particular goals, safety exclusions, and public/private status in the Intake (Phase 0) — is **AUTHORIZED** and permits moving to the next phase. This split is an existing, structural property of the role model, not a new gate.

## DE – 5. Adapter-Phasen

| Phase | Name | Typ | Ergebnis |
|---|---|---|---|
| 0 | Intake | review-only | ausgefülltes Intake-Template |
| 1 | Repository Read-only Review | review-only | Review Report |
| 2 | Project Profile | docs-only | `project-system/PROJECT_PROFILE.md` |
| 3 | Project Manifest | docs-only | `project-system/PROJECT_MANIFEST.md` (kanonisch Markdown; eingebettetes YAML/JSON erlaubt — siehe Conventions) |
| 4 | Project Brain | docs-only | `project-brain/PROJECT_BRAIN.md` |
| 5 | Capability Matrix | docs-only | `project-system/CAPABILITY_MATRIX.md` |
| 6 | Compliance Check | review-only | `project-system/COMPLIANCE_CHECK.md` |
| 7 | Health Score | health-score-update | `project-system/HEALTH_SCORE.md` |
| 8 | Work Package Queue | docs-only | `project-system/WORK_PACKAGE_QUEUE.md` |
| 9 | First Safe Work Package | je nach Typ | erstes kleines, sicheres WP |
| 10 | Review and Commit | — | Maintainer-Review, Commit, Push |

Phasen 2–8 können in einem `project-adapter`-Work-Package gebündelt werden (vollständige Variante, siehe `framework/prompts/project-adapter/PROJECT_SYSTEM_BASELINE_PROMPT.md`) oder einzeln laufen. Diese gebündelte Ausführung liefert zusätzlich `docs/ndf/README.md` und `docs/ndf/ADOPTION_NOTES.md` (siehe §11) — keinem einzelnen Phasen-Ergebnis oben zugeordnet, sondern Teil der gebündelten Baseline.

## EN – 5. Adapter Phases

| Phase | Name | Type | Result |
|---|---|---|---|
| 0 | Intake | review-only | completed intake template |
| 1 | Repository Read-only Review | review-only | review report |
| 2 | Project Profile | docs-only | `project-system/PROJECT_PROFILE.md` |
| 3 | Project Manifest | docs-only | `project-system/PROJECT_MANIFEST.md` (canonical Markdown; embedded YAML/JSON allowed — see Conventions) |
| 4 | Project Brain | docs-only | `project-brain/PROJECT_BRAIN.md` |
| 5 | Capability Matrix | docs-only | `project-system/CAPABILITY_MATRIX.md` |
| 6 | Compliance Check | review-only | `project-system/COMPLIANCE_CHECK.md` |
| 7 | Health Score | health-score-update | `project-system/HEALTH_SCORE.md` |
| 8 | Work Package Queue | docs-only | `project-system/WORK_PACKAGE_QUEUE.md` |
| 9 | First Safe Work Package | depends on type | first small, safe WP |
| 10 | Review and Commit | — | maintainer review, commit, push |

Phases 2–8 can be bundled into one `project-adapter` work package (full variant, see `framework/prompts/project-adapter/PROJECT_SYSTEM_BASELINE_PROMPT.md`) or run individually. This bundled execution additionally produces `docs/ndf/README.md` and `docs/ndf/ADOPTION_NOTES.md` (see §11) — not attributed to any single phase result above, but part of the bundled baseline.

## DE – 6. Benötigte NDF-Artefakte

- Templates: `framework/templates/project-adapter/`
- Checkliste: `framework/checklists/PROJECT_ADAPTER_CHECKLIST.md`
- Prompts: `framework/prompts/project-adapter/`
- Spezifikationen: `docs/project-system/`
- Entscheidungshilfe: `docs/toolkit/PROJECT_ADAPTER_HELPER.md`
- Vorbereitende Analyse (optional, read-only): `.claude/skills/ndf-existing-project-analysis-runner/SKILL.md` — deckt die read-only-ableitbaren Intake-Felder ab (Project Type, Tech Stack, Known Risks, teilweise Project Name/Deployment Model/Repository URL), nicht die drei Human-Maintainer-Felder (Maintainer Goals, Public/Private Status, Safety Notes).

## EN – 6. Required NDF Artifacts

- Templates: `framework/templates/project-adapter/`
- Checklist: `framework/checklists/PROJECT_ADAPTER_CHECKLIST.md`
- Prompts: `framework/prompts/project-adapter/`
- Specifications: `docs/project-system/`
- Decision helper: `docs/toolkit/PROJECT_ADAPTER_HELPER.md`
- Preparatory analysis (optional, read-only): `.claude/skills/ndf-existing-project-analysis-runner/SKILL.md` — covers the read-only-derivable intake fields (Project Type, Tech Stack, Known Risks, partially Project Name/Deployment Model/Repository URL), not the three Human-Maintainer fields (Maintainer Goals, Public/Private Status, Safety Notes).

## DE – 7. Sicherheitsregeln

1. Phase 0–1 sind strikt read-only: keine Codeänderungen, keine Konfigänderungen.
2. Keine Secrets lesen, kopieren oder in Artefakte übernehmen (`.env`, Keys, Tokens, Credentials).
3. Destruktive Funktionen des Zielprojekts (Löschen, Bulk-Operationen, irreversible Aktionen) werden nur **erfasst**, nie verändert — Änderungen daran laufen später über `destructive-blueprint` → `destructive-implementation`.
4. Jede Phase endet mit einer Rückmeldung an Nova; ohne Freigabe keine nächste Phase.
5. Kein Commit und kein Push durch den Implementation Agent, sofern nicht ausdrücklich freigegeben.
6. Private Namen, interne URLs und personenbezogene Daten gehören nicht in öffentlich sichtbare NDF-Artefakte.

## EN – 7. Safety Rules

1. Phases 0–1 are strictly read-only: no code changes, no configuration changes.
2. Never read, copy, or carry secrets into artifacts (`.env`, keys, tokens, credentials).
3. Destructive functions of the target project (deletion, bulk operations, irreversible actions) are only **captured**, never changed — changes to them run later via `destructive-blueprint` → `destructive-implementation`.
4. Every phase ends with a report to Nova; no next phase without approval.
5. No commit and no push by the Implementation Agent unless explicitly authorized.
6. Private names, internal URLs, and personal data do not belong in publicly visible NDF artifacts.

## DE – 8. Umgang mit bestehenden Projekten

- Bestehende Strukturen werden respektiert: NDF-Artefakte kommen **zusätzlich** ins Projekt, vorhandene Dateien werden nicht umgebaut.
- Bestehende Doku wird referenziert, nicht dupliziert.
- Ein Projekt mit starker Technik, aber schwacher Doku beginnt mit Doku-/Status-WPs, nicht mit Features.
- Ein Projekt mit riskanten Funktionen beginnt mit Security-/Destructive-Reviews.

## EN – 8. Handling Existing Projects

- Existing structures are respected: NDF artifacts are **additive** to the project; existing files are not reworked.
- Existing docs are referenced, not duplicated.
- A project with strong tech but weak docs starts with docs/status WPs, not features.
- A project with risky functions starts with security/destructive reviews.

## DE – 9. Minimale Variante

Für kleine Projekte oder einen schnellen Start:

```text
Phase 0 -> Phase 1 -> Phase 2 (Profile) -> Phase 3 (Manifest) -> Phase 8 (kleine Queue) -> Phase 10
```

Capability Matrix, Compliance Check und Health Score können später als eigene Work Packages folgen. Phase 4 (Project Brain) läuft in dieser Variante nicht mit — siehe `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md` für die exakte Minimal-Output-Liste.

## EN – 9. Minimal Variant

For small projects or a quick start:

```text
Phase 0 -> Phase 1 -> Phase 2 (Profile) -> Phase 3 (Manifest) -> Phase 8 (small queue) -> Phase 10
```

Capability Matrix, Compliance Check, and Health Score can follow later as their own work packages. Phase 4 (Project Brain) does not run in this variant — see `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md` for the exact minimal output list.

## DE – 10. Vollständige Variante

Alle Phasen 0–10 in Reihenfolge. Empfohlen für Projekte, die produktiv genutzt werden, mehrere Module haben oder sicherheitsrelevante Funktionen enthalten.

## EN – 10. Full Variant

All phases 0–10 in order. Recommended for projects that are used in production, have multiple modules, or contain security-relevant functions.

## DE – 11. Ergebnisstruktur

Siehe `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`:

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.md
project-system/CAPABILITY_MATRIX.md
project-system/COMPLIANCE_CHECK.md
project-system/HEALTH_SCORE.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
docs/ndf/README.md          # Teil der gebündelten Phase-2–8-Ausführung, siehe §5
docs/ndf/ADOPTION_NOTES.md  # Teil der gebündelten Phase-2–8-Ausführung, siehe §5
```

## EN – 11. Output Structure

See `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`:

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.md
project-system/CAPABILITY_MATRIX.md
project-system/COMPLIANCE_CHECK.md
project-system/HEALTH_SCORE.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
docs/ndf/README.md          # part of the bundled Phase 2–8 execution, see §5
docs/ndf/ADOPTION_NOTES.md  # part of the bundled Phase 2–8 execution, see §5
```

## DE – 12. Nächster Schritt nach Adapter-Ausführung

Das erste Work Package aus der Queue umsetzen — klein, sicher, typisiert (z. B. Documentation Stability Review oder Security Baseline Review). Danach etabliert sich der normale NDF-Zyklus: Classify → Plan → Execute → Rückmeldung → Review → Commit.

## EN – 12. Next Step After Running the Adapter

Implement the first work package from the queue — small, safe, typed (e.g. a Documentation Stability Review or a Security Baseline Review). After that, the normal NDF cycle establishes itself: Classify → Plan → Execute → Report → Review → Commit.
