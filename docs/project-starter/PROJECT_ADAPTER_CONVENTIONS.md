# Project Adapter Conventions

> Gilt seit Foundation 0.4 (NDF-WP-059). Schärft die Konventionen aus der praktischen Adapter-Validierung (NDF-WP-047, PASS WITH NOTES). / In effect since Foundation 0.4; sharpens the conventions from the practical adapter validation.

## DE – Zweck

Diese Datei legt verbindliche Konventionen für Project-Adapter-Läufe fest, damit externe Nutzer den Adapter konsistent anwenden. Sie adressiert die drei should-have-Findings aus NDF-WP-047: Manifest-Format, Health-Score-Kategorien und Output-Pfade.

## EN – Purpose

This file sets binding conventions for project adapter runs so external users apply the adapter consistently. It addresses the three should-have findings from NDF-WP-047: manifest format, health-score categories, and output paths.

## DE – Geltungsbereich

Für alle Adapter-Läufe — neutrale Validierungs-/Demo-Läufe wie auch produktionsnahe Projektübernahmen. Ergänzt den Guide `PROJECT_ADAPTER_V0_2.md`; ersetzt ihn nicht.

## EN – Scope

For all adapter runs — neutral validation/demo runs and production-like project adoptions alike. Complements the guide `PROJECT_ADAPTER_V0_2.md`; does not replace it.

## DE – Manifest-Konvention

- **`PROJECT_MANIFEST.md` ist das kanonische, öffentlich reviewbare Standardformat.** Markdown bleibt der Review-Artefakt-Container.
- Ein YAML- oder JSON-Block **innerhalb** der Markdown-Datei ist erlaubt (eingebettet oder abgeleitet), ist aber **nicht** die alleinige Wahrheit.
- Keine maschinelle Manifest-Pflicht in Foundation 0.4 (kein Build hängt am Manifest).
- Unbekannte Felder werden ausdrücklich als `unknown`, `not evidenced`, `n/a` oder `open decision` markiert — nie geraten.

## EN – Manifest Convention

- **`PROJECT_MANIFEST.md` is the canonical, publicly reviewable standard format.** Markdown stays the review-artifact container.
- A YAML or JSON block **inside** the markdown file is allowed (embedded or derived) but is **not** the sole source of truth.
- No machine-readable manifest requirement in Foundation 0.4.
- Unknown fields are explicitly marked `unknown`, `not evidenced`, `n/a`, or `open decision` — never guessed.

## DE – Output-Pfad-Konvention

| Zweck | Pfad |
|---|---|
| neutrale Fixture-/Validierungsläufe | `examples/<fixture-name>/adapter-validation-output/` |
| zentrale Validierungsnachweise | `docs/validation/project-adapter/` |
| echte/produktionsnahe Projektübernahme | `project-system/`, `project-brain/`, `docs/project-adoption/` (oder bestehende Projektstruktur) — **nur nach Human-Maintainer-Entscheidung** |

Regeln:

- Adapter-Output darf **produktive Projektdokumente nie still überschreiben**.
- Validierungsoutput muss klar als solcher markiert sein (Kopfzeilen-Hinweis).
- **Erwartete Outputs** (`expected-adapter-output/`) und **tatsächliche Outputs** (`adapter-validation-output/`) bleiben getrennt.

## EN – Output Path Convention

| Purpose | Path |
|---|---|
| neutral fixture/validation runs | `examples/<fixture-name>/adapter-validation-output/` |
| central validation evidence | `docs/validation/project-adapter/` |
| real/production-like adoption | `project-system/`, `project-brain/`, `docs/project-adoption/` (or existing project structure) — **only after human-maintainer decision** |

Rules: adapter output never silently overwrites productive project docs; validation output is clearly marked as such; expected outputs and actual outputs stay separated.

## DE – Health-Score-Konvention

Foundation-0.4-Mindestkategorien:

```text
Documentation
Security
Operations
Testing / CI
Release Readiness
Maintainability
Governance / Workflow
i18n / Language Readiness
```

Regeln:

- Keine Scheingenauigkeit; fehlende Evidenz wird nicht positiv bewertet.
- `unknown` ist besser als erfundene Reife.
- Jeder Score wird begründet.
- Kategorien dürfen `n/a` sein — aber nur mit Begründung.
- Der Health Score ist ein Startpunkt (Baseline), kein Urteil über den Projektwert. Änderungen später nur über `health-score-update`-Work-Packages mit Evidenz.

## EN – Health Score Convention

Foundation 0.4 minimum categories: Documentation, Security, Operations, Testing / CI, Release Readiness, Maintainability, Governance / Workflow, i18n / Language Readiness. No false precision; missing evidence is not scored positively; `unknown` beats invented maturity; every score is justified; `n/a` only with a reason; the score is a baseline, not a verdict — later changes only via `health-score-update` work packages with evidence.

## DE – Validierungs- und Demo-Läufe

Nutzen ausschließlich `examples/<fixture-name>/adapter-validation-output/`, tragen einen klaren „Validierungsoutput, keine produktive Doku"-Hinweis in jeder Datei und verweisen auf den zentralen Nachweis unter `docs/validation/project-adapter/`.

## EN – Validation and Demo Runs

Use `examples/<fixture-name>/adapter-validation-output/` only, carry a clear "validation output, not production documentation" note in every file, and link the central evidence under `docs/validation/project-adapter/`.

## DE – Produktionsnahe Adapter-Läufe

Erzeugen die NDF-Artefakte additiv im Zielprojekt (siehe Output-Pfad-Konvention). Vor dem Lauf legt der Human Maintainer den Zielpfad fest. Bestehende Dokumente werden referenziert, nicht überschrieben.

## EN – Production-like Adapter Runs

Produce the NDF artifacts additively in the target project (see output path convention). Before the run, the human maintainer fixes the target path. Existing documents are referenced, not overwritten.

## DE – Umgang mit unbekannten Informationen

Was aus den Eingaben nicht belegbar ist, wird als `unknown` / `not evidenced` / `n/a` / `open decision` markiert. Der Adapter erfindet keine Fakten und bewertet Unbekanntes nicht positiv.

## EN – Handling Unknown Information

Anything not evidenced from the inputs is marked `unknown` / `not evidenced` / `n/a` / `open decision`. The adapter invents no facts and does not score unknowns positively.

## DE – Neutralität und private Begriffe

Alle erzeugten Adapter-Outputs unterliegen dem Public Quality Gate v0.2 inklusive new-file neutrality check. Keine privaten Projekt-/Personennamen, keine echten Domains/Secrets, keine privaten Suchmuster — auch nicht in Beispielen. Neutrale Platzhalter wie `SampleProject`, `example-owner`, `example.local`, `EXAMPLE_SECRET_PLACEHOLDER`.

## EN – Neutrality and Private Terms

All generated adapter outputs are subject to the public quality gate v0.2 including the new-file neutrality check. No private project/person names, no real domains/secrets, no private search patterns — not even in examples. Use neutral placeholders like `SampleProject`, `example-owner`, `example.local`, `EXAMPLE_SECRET_PLACEHOLDER`.

## DE – Nicht-Ziele

Keine maschinelle Manifest-Pflicht, keine Adapter-Automatisierung, kein neues Adapter-Feature, keine v1.0-Behauptung. WP-059 schärft nur Konventionen und Dokumentation.

## EN – Non-Goals

No machine-readable manifest requirement, no adapter automation, no new adapter feature, no v1.0 claim. WP-059 only sharpens conventions and documentation.
