# Prompt Metadata Standard

Jeder Prompt erhält Metadaten.

## Pflichtfelder

```yaml
id:
title:
version:
category:
role:
supported_models:
input_required:
output_expected:
risk_level:
requires_human_review:
```

## Beispiel

```yaml
id: ndf-dev-small-fix-001
title: Small Fix Work Package
version: 0.1
category: development
role: Claude Developer
supported_models:
  - Claude
  - ChatGPT
risk_level: low
requires_human_review: true
```

## Risikostufen

- low
- medium
- high

High-Risk-Prompts dürfen niemals ohne menschliche Prüfung umgesetzt werden.
