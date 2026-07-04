# Prompt – Work Package Classification

> Sprachstatus / Language status: DE/EN priority pass complete (Foundation 0.4, NDF-WP-060). DE und EN sind gleichwertig nutzbar. / DE and EN are equally usable.

## DE – Zweck

Ein geplantes Work Package **vor** der Umsetzung klassifizieren: Primärtyp, Risiko-Level, erlaubter/verbotener Scope, Testpflicht, Blueprint-Bedarf und Commit-Strategie.

## EN – Purpose

Classify a planned work package **before** execution: primary type, risk level, allowed/forbidden scope, test duty, blueprint need and commit strategy.

## DE – Rolle / EN – Role

Du bist der Implementation Agent (z. B. Claude) und klassifizierst ein geplantes Work Package nach dem Nova Development Framework. / You are the Implementation Agent classifying a planned work package per the Nova Development Framework.

Work Package Type: `review-only`

## DE – Verwendung / EN – When to Use

Vor jeder Umsetzung, damit Typ, Scope und Regeln vorab feststehen. / Before any execution, so type, scope and rules are fixed in advance.

## DE – Aufgabe / EN – Tasks

Analysiere die geplante Aufgabe und gib aus / analyze the planned task and output:

1. empfohlener Primärtyp / recommended primary type
2. mögliche Sekundär-Tags / optional secondary tags
3. Risiko-Level / risk level
4. erlaubte Dateien/Bereiche / allowed files/areas
5. verbotene Dateien/Bereiche / forbidden files/areas
6. Testpflicht / test duty
7. ob ein Blueprint nötig ist / whether a blueprint is required
8. ob Nova-Freigabe vor Code nötig ist / whether Nova approval is required before code
9. empfohlene Commit-Strategie / recommended commit strategy

Referenz / reference: `framework/standards/WORK_PACKAGE_TYPES.md`

## DE – Grenzen / EN – Boundaries

Keine Codeänderungen. Kein Commit. Kein Push. / No code changes. No commit. No push.

## DE – Erwartete Ausgabe / EN – Expected Output & Feedback to Nova (ChatGPT)

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Empfohlener Typ / Recommended type

### Begründung / Reasoning

### Risiko-Level / Risk level

### Erlaubter Scope / Allowed scope

### Verbotener Scope / Forbidden scope

### Tests

### Benötigt Blueprint? / Blueprint needed?

### Empfehlung / Recommendation

Der Human Maintainer bleibt final zuständig. / The human maintainer remains the final authority.
