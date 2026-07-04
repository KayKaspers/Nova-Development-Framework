# Adapter Validation Output – SampleProject (NDF-WP-047)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.

## DE – Was ist dieser Output?

Dieses Verzeichnis enthält das Ergebnis eines vollständigen Project-Adapter-v0.2-Durchlaufs (Phasen 0–10 aus `docs/project-starter/PROJECT_ADAPTER_V0_2.md`) am fiktiven SampleProject-Fixture. Es zeigt einem externen Nutzer, **wie NDF-Artefakte für ein bestehendes Projekt aussehen**, wenn der Adapter angewendet wird.

## EN – What is this output?

This directory contains the result of a complete Project Adapter v0.2 run (phases 0–10 per `docs/project-starter/PROJECT_ADAPTER_V0_2.md`) on the fictitious SampleProject fixture. It shows an external user **what NDF artifacts look like for an existing project** when the adapter is applied.

## Abgedeckte Phasen / Covered phases

| Phase | Artefakt |
|---|---|
| 0 Intake | Input: `../PROJECT_BRIEF.md` (Fixture) |
| 1 Read-only Review | `FINDINGS.md` |
| 2 Project Profile | `PROJECT_PROFILE.md` |
| 3 Project Manifest | `PROJECT_MANIFEST.md` |
| 4 Project Brain | `PROJECT_BRAIN.md` |
| 5 Capability Matrix | `CAPABILITY_MATRIX.md` |
| 6 Compliance Check | `COMPLIANCE_CHECK.md` |
| 7 Health Score | `HEALTH_SCORE.md` |
| 8 Work Package Queue | `INITIAL_WORK_PACKAGE_QUEUE.md` |
| 9 First Safe WP | `FIRST_SAFE_WORK_PACKAGE.md` |
| 10 Review | `ADAPTER_VALIDATION_REVIEW_REPORT.md` (bewertet den Adapter selbst) |

## Leseempfehlung / How to read

1. Zuerst `ADAPTER_VALIDATION_REVIEW_REPORT.md` — das Gesamtergebnis der Validierung.
2. Dann `FINDINGS.md` und `HEALTH_SCORE.md` — was der Adapter im Fixture gefunden hat.
3. Dann `INITIAL_WORK_PACKAGE_QUEUE.md` + `FIRST_SAFE_WORK_PACKAGE.md` — wie es für ein echtes Projekt weiterginge.

## Nicht enthalten / Not included

- keine Implementierung von SampleProject-Work-Packages (auch nicht des First Safe WP)
- keine Destructive-Action-Implementierung (nur Blueprint-Kandidat in der Queue)
- kein echter Code, keine Secrets, keine echten Domains
- Der zentrale Foundation-0.3-Nachweis liegt in `docs/validation/project-adapter/SAMPLEPROJECT_ADAPTER_VALIDATION.md`.
