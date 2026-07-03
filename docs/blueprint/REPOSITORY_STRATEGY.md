# NDF Repository Strategy

## Kurzfristig

Ein Repository:

```text
nova-development-framework
```

Vorteile:

- einfacher Start
- keine Mehrfachverwaltung
- schnelle Iteration
- alles an einem Ort

## Langfristig

Vier Repositories:

```text
ndf-core
ndf-academy
ndf-toolkit
ndf-examples
```

## ndf-core

Enthält:

- Constitution
- Standards
- Governance
- ADRs
- Project Brain
- Quality Gates

## ndf-academy

Enthält:

- Handbuch
- Lernpfade
- Übungen
- Lösungen
- Glossar
- PDF/Word/Web Export

## ndf-toolkit

Enthält:

- Generator
- CLI
- Templates
- Scripts
- Prompt Library
- Export Tools

## ndf-examples

Enthält:

- Beispielprojekte
- Referenzimplementierungen
- Referenzprojekt-B-Adapter (CI/Docker)
- Referenzprojekt-A-Adapter (Destructive Operations)
- Adapter für zukünftige Referenzprojekte

## Entscheidung

Aufteilung noch nicht sofort. Erst Foundation im Mono-Repo stabilisieren.
