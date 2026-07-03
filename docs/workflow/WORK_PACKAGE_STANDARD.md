# NDF Work-Package-Standard / NDF Work Package Standard

## DE

### Definition

Ein Work Package ist eine klar begrenzte Aufgabe mit Ziel, Kontext, Grenzen, Qualitätsregeln und Rückmeldung.

### Work Package Type

Jedes Work Package hat genau einen primären Typ (z. B. `review-only`, `docs-only`, `code-fix`). Der Typ bestimmt erlaubte Änderungen, Testerwartung und Review-Tiefe. Standard: [WORK_PACKAGE_TYPES.md](../../framework/standards/WORK_PACKAGE_TYPES.md)

### Ein gutes Work Package enthält

- Ziel
- Kontext
- konkrete Aufgabe
- Scope: betroffene Bereiche, erlaubte Dateien (allowed files), verbotene Bereiche (forbidden files)
- Grenzen
- Tests bzw. begründete Test-Ausnahme
- Dokumentationspflicht
- Rückmeldung an Nova (die ChatGPT-basierte Review-Rolle, siehe [NOVA_CHATGPT_ROLE.md](NOVA_CHATGPT_ROLE.md))

### Schlechtes vs. gutes Work Package

Schlecht:

```text
Mach das Projekt besser.
```

Gut:

```text
Untersuche die Docker-Compose-Dokumentation und ergänze eine Anfängeranleitung für die lokale Installation. Typ: docs-only. Keine Codeänderungen. Am Ende Rückmeldung an Nova.
```

### Review-Entscheidung

Nach der Rückmeldung entscheidet Nova bzw. der Maintainer: **GO / GO WITH NOTES / REWORK / SPLIT / STOP**.

### Commit-Regel

Der Implementation Agent committet und pusht nicht. Der Human Maintainer prüft die Änderungen und veröffentlicht mit einer scoped Commit-Message.

### Maximale Größe

Ein Work Package sollte so klein sein, dass der Maintainer die Änderungen nachvollziehen kann.

## EN

### Definition

A work package is a clearly bounded task with goal, context, limits, quality rules, and feedback.

### Work Package Type

Every work package has exactly one primary type (e.g. `review-only`, `docs-only`, `code-fix`). The type decides allowed changes, test expectations, and review depth. Standard: [WORK_PACKAGE_TYPES.md](../../framework/standards/WORK_PACKAGE_TYPES.md)

### A good work package contains

- goal
- context
- concrete task
- scope: affected areas, allowed files, forbidden files
- limits
- tests or a justified test exemption
- documentation duty
- feedback to Nova (the ChatGPT-based review role, see [NOVA_CHATGPT_ROLE.md](NOVA_CHATGPT_ROLE.md))

### Bad vs. good work package

Bad:

```text
Make the project better.
```

Good:

```text
Review the Docker Compose documentation and add a beginner guide for local installation. Type: docs-only. No code changes. Finish with feedback to Nova.
```

### Review decision

After the feedback, Nova and the maintainer decide: **GO / GO WITH NOTES / REWORK / SPLIT / STOP**.

### Commit rule

The Implementation Agent does not commit or push. The human maintainer reviews the changes and publishes them with a scoped commit message.

### Maximum size

A work package should be small enough that the maintainer can fully understand the changes.
