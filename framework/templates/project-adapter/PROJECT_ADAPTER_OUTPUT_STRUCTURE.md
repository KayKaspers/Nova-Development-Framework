# Project Adapter Output Structure

Diese Dateien erzeugt der Project Adapter im Zielprojekt (vollständige Variante). Bestehende Projektdateien werden nicht verändert — NDF-Artefakte kommen additiv dazu.

```text
project-system/PROJECT_PROFILE.md        # Was ist das Projekt, wohin soll es?
project-system/PROJECT_MANIFEST.yaml     # Maschinenlesbare Eckdaten (Owner, Stack, Level)
project-system/CAPABILITY_MATRIX.md      # Was kann das Projekt heute (Docker, CI, Tests, ...)?
project-system/COMPLIANCE_CHECK.md       # Abgleich gegen NDF-Standards
project-system/HEALTH_SCORE.md           # Initiale Gesundheitsbewertung mit Evidenz
project-system/WORK_PACKAGE_QUEUE.md     # Erste typisierte Work Packages
project-brain/PROJECT_BRAIN.md           # Arbeitsgedächtnis: Stand, Entscheidungen, nächste Schritte
docs/ndf/README.md                       # Kurzerklärung: dieses Projekt nutzt NDF
docs/ndf/ADOPTION_NOTES.md               # Was wurde beim Adaptieren entschieden und warum
```

## Minimale Variante

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.yaml
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
```

## Hinweise

- Specs für die einzelnen Dateien: `docs/project-system/`
- Vorlagen für Erstbefüllung: `framework/project-starter/templates/`
- Bei öffentlichen Projekten: keine privaten Namen oder internen Details in diese Artefakte schreiben.
