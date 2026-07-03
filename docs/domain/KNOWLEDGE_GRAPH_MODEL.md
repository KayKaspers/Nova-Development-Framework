# NDF Knowledge Graph Model

## Zweck

Der Knowledge Graph verbindet Wissen, Regeln, Entscheidungen, Prompts und Projekte.

## Node Types

- Project
- Standard
- Rule
- ADR
- Prompt
- Template
- Lesson Learned
- Quality Gate
- Capability
- Artifact

## Edge Types

- uses
- requires
- improves
- replaces
- documents
- validates
- generates
- depends_on
- applies_to

## Beispiel

```text
Referenzprojekt B
  uses Docker Standard
Docker Standard
  requires Docker Quality Gate
Docker Quality Gate
  validates Docker Compose Files
Lesson Learned FFmpeg Tests
  improves Testing Standard
Testing Standard
  applies_to Referenzprojekt B
```

## Nutzen

Der Knowledge Graph ermöglicht später:

- bessere Suche
- automatische Empfehlungen
- Projekt-Health-Checks
- Compliance-Bewertung
- Generierung passender Work Packages
