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
- id: sample-project-wp-001
  title: Stabilize docs-status generation
  priority: P1
  status: ready
  prompt: prompts/claude/sample-project/docs-status-stability.md
```

## Regel

Ein Work Package muss klein genug sein, dass der Maintainer es prüfen kann.
