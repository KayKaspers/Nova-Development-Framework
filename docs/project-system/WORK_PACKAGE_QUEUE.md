# Work Package Queue

## Zweck

Die Work Package Queue enthält die nächsten sinnvollen Arbeitspakete eines Projekts.

## Prioritäten

- P0: kritisch
- P1: hoch
- P2: normal
- P3: niedrig

## Status

- draft
- ready
- in_progress
- review
- done
- blocked

## Beispiel

```yaml
- id: castcore-wp-001
  title: Stabilize docs-status generation
  priority: P1
  status: ready
  prompt: prompts/claude/castcore/docs-status-stability.md
```

## Regel

Ein Work Package muss klein genug sein, dass Kay es prüfen kann.
