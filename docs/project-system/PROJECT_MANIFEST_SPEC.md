# Project Manifest Specification

## Zweck

Das Project Manifest ist die Identitätskarte eines Projekts.

Es ist maschinenlesbar und menschenlesbar.

## Empfohlenes Format

```yaml
name: SampleProject
slug: sample-project
owner: Kay
architecture_lead: Nova
implementation_assistant: Claude
repository: ""
status: active
ndf_level: 1
primary_language: ""
secondary_languages: []
deployment:
  - docker
quality_targets:
  documentation: required
  tests: required
  security: required
  ci: required
```

## Pflichtfelder

- name
- slug
- owner
- status
- ndf_level
- repository

## Statuswerte

- idea
- active
- paused
- maintenance
- archived

## NDF-Level

- 0: nicht angebunden
- 1: Basisanbindung
- 2: Standards aktiv
- 3: Quality Gates aktiv
- 4: Health Score aktiv
- 5: vollständig NDF-konform
