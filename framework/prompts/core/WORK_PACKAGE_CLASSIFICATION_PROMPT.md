# Claude Prompt – Work Package Classification

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Classify a planned work package before execution: recommend the primary type, risk level, allowed and forbidden scope, test duty, blueprint need and commit strategy. Work package type: `review-only` — no code changes, no commit, no push. Finish with the structured feedback to Nova (ChatGPT).

## Rolle

Du bist Claude und klassifizierst ein geplantes Work Package nach dem Nova Development Framework.

## Work Package Type

review-only

## Ziel

Bestimme den passenden Work-Package-Typ, bevor Umsetzung beginnt.

## Aufgabe

Analysiere die geplante Aufgabe und gib aus:

1. empfohlener Primärtyp
2. mögliche Sekundär-Tags
3. Risiko-Level
4. erlaubte Dateien/Bereiche
5. verbotene Dateien/Bereiche
6. Testpflicht
7. ob ein Blueprint nötig ist
8. ob Nova-Freigabe vor Code nötig ist
9. empfohlene Commit-Strategie

## Grenzen

Keine Codeänderungen. Kein Commit. Kein Push.

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Empfohlener Typ

### Begründung

### Risiko-Level

### Erlaubter Scope

### Verbotener Scope

### Tests

### Benötigt Blueprint?

### Empfehlung
