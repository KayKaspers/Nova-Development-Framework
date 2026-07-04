# Project Adapter Output Structure

Diese Dateien erzeugt der Project Adapter im Zielprojekt (vollständige Variante). Bestehende Projektdateien werden nicht verändert — NDF-Artefakte kommen additiv dazu. Pfad-Regeln: `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md`.

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.md        # kanonisch Markdown (optional eingebetteter YAML/JSON-Block)
project-system/CAPABILITY_MATRIX.md
project-system/COMPLIANCE_CHECK.md
project-system/HEALTH_SCORE.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
docs/ndf/README.md
docs/ndf/ADOPTION_NOTES.md
```

## Minimale Variante / Minimal variant

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
```

## Output-Pfad-Konvention / Output path convention

| Zweck / Purpose | Pfad / Path |
|---|---|
| neutrale Fixture-/Validierungsläufe / neutral fixture/validation runs | `examples/<fixture-name>/adapter-validation-output/` |
| erwartete Outputs (getrennt von tatsächlichen) / expected outputs (separate from actual) | `examples/<fixture-name>/expected-adapter-output/` |
| zentrale Validierungsnachweise / central validation evidence | `docs/validation/project-adapter/` |
| echte/produktionsnahe Übernahme / real adoption (nur nach Maintainer-Entscheidung) | `project-system/`, `project-brain/`, `docs/project-adoption/` |

## Hinweise / Notes

- **Validierungsoutput** trägt in jeder Datei einen klaren „keine produktive Doku"-Hinweis und bleibt von **erwarteten** Outputs getrennt. / Validation output is clearly marked and stays separate from expected output.
- Adapter-Output überschreibt **nie still** produktive Projektdokumente. / Adapter output never silently overwrites productive docs.
- Manifest: kanonisch `PROJECT_MANIFEST.md` (Markdown), YAML/JSON nur eingebettet/abgeleitet. / Manifest canonical as markdown.
- Specs: `docs/project-system/` · Vorlagen: `framework/project-starter/templates/`, `framework/templates/project-adapter/`
- Bei öffentlichen Projekten: keine privaten Namen/Domains/Secrets in diese Artefakte (Public Quality Gate v0.2, new-file neutrality check). / No private terms in public projects.
