# Docs Structure Policy

## Zweck

`docs/` enthält erklärende Framework-Dokumentation.

## Zielstruktur

```text
docs/
├── academy/
├── architecture/
├── blueprint/
├── constitution/
├── domain/
├── export/
├── governance/
├── project-starter/
├── project-system/
├── release/
├── repository/
├── reviews/
├── toolkit/
└── website/
```

## Regeln

### Keine losen Dokumente

Neue Dokumente sollen einem Themenordner zugeordnet werden.

### Keine Templates in docs

Templates gehören nach:

```text
framework/templates/
```

### Keine Prompts in docs

Prompts gehören nach:

```text
framework/prompts/
```

### Keine Project-Brain-Notizen in docs

Project-Brain-Notizen gehören nach:

```text
project-brain/
```

## Ausnahme

Übersichtsseiten dürfen in `docs/` liegen, wenn sie Navigation vereinfachen.
