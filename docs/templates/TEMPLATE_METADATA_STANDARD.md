# Template Metadata Standard

## Pflicht-Metadaten

Templates können optional einen Metadatenblock erhalten.

```yaml
id:
title:
version:
category:
artifact_type:
recommended_for:
requires_review:
owner:
```

## Beispiel

```yaml
id: ndf-template-project-readme-001
title: Project README Template
version: 0.1
category: project
artifact_type: README
recommended_for:
  - new-project
  - open-source
requires_review: true
owner: Nova
```

## Nutzen

Metadaten ermöglichen später:

- Template-Suche
- Generatoren
- Qualitätsprüfung
- automatische Projektinitialisierung
