# Website Navigation – MkDocs Draft

```yaml
site_name: Nova Development Framework
site_description: Plan. Build. Review. Improve.

theme:
  name: material
  language: de
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.highlight
    - content.code.copy

nav:
  - Home: README.md
  - Getting Started:
      - Overview: getting-started/index.md
      - Beginner Workflow: getting-started/beginner-workflow.md
      - GitHub Desktop: getting-started/github-desktop.md
      - VS Code: getting-started/vs-code.md
  - Foundation:
      - Constitution: docs/constitution/NDF_CONSTITUTION.md
      - Blueprint: docs/blueprint/NDF_BLUEPRINT.md
      - Domain Model: docs/domain/NDF_DOMAIN_MODEL.md
  - Academy:
      - Band 1: academy/band-1-foundation/README.md
  - Toolkit:
      - Overview: docs/toolkit/NDF_TOOLKIT_OVERVIEW.md
  - Prompt Library:
      - Overview: docs/prompts/PROMPT_LIBRARY_OVERVIEW.md
  - Template Library:
      - Overview: docs/templates/TEMPLATE_LIBRARY_OVERVIEW.md
  - Project System:
      - Overview: docs/project-system/NDF_PROJECT_SYSTEM.md
```

## Hinweis

Diese Datei ist ein Navigationsentwurf, noch keine finale MkDocs-Konfiguration.
