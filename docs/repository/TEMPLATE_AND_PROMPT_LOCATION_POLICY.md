# Template and Prompt Location Policy

## Zweck

Prompts und Templates müssen eindeutig auffindbar sein.

## Zentrale Template-Quelle

```text
framework/templates/
```

Alle wiederverwendbaren Templates gehören langfristig hierher.

## Zentrale Prompt-Quelle

```text
framework/prompts/
```

Alle wiederverwendbaren Prompts gehören langfristig hierher.

## Projektbezogene Prompts

In echten Projekten dürfen projektspezifische Prompts liegen unter:

```text
prompts/claude/
```

Im NDF selbst bleiben universelle Prompts unter `framework/prompts/`.

## Alte oder doppelte Bereiche

Falls Root-Ordner wie `templates/` oder `standards/` parallel existieren, sollen sie geprüft und bei Bedarf migriert werden.

## Regel

Ein Template oder Prompt soll genau eine kanonische Quelle haben.
