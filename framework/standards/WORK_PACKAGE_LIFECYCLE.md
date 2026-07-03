# NDF Standard – Work Package Lifecycle

> Sprachstatus / Language status: EN mit deutscher Einleitung. / English with German introduction.

DE: Dieser Standard beschreibt den Lebenszyklus jedes Work Package — von der Aufnahme über Klassifizierung, Prompt, Umsetzung durch den Implementation Agent und Rückmeldung an Nova (ChatGPT-Review-Rolle, siehe [NOVA_CHATGPT_ROLE.md](../../docs/workflow/NOVA_CHATGPT_ROLE.md)) bis zu Review, Maintainer-Commit, CI-Prüfung und Follow-up.

## Lifecycle

```text
Intake -> Classification -> Blueprint/Prompt -> Execution -> Rückmeldung -> Nova Review -> Maintainer Commit -> CI/Validation -> Follow-up
```

## 1. Intake

Capture the need: bug, feature, risk, security finding, documentation gap, release need or CI failure.

## 2. Classification

Assign one primary Work Package type.

Examples:

- Security review -> `security-baseline`
- Security fix -> `security-code-fix`
- Health score change -> `health-score-update`
- Delete feature planning -> `destructive-blueprint`
- Delete feature implementation -> `destructive-implementation`

## 3. Blueprint / Prompt

Nova writes the Claude prompt with type, scope, allowed files, forbidden files, tests and Rückmeldung.

## 4. Execution

Claude executes only within the scope and does not commit or push.

## 5. Rückmeldung

Claude reports summary, changed files, tests, risks and recommendation.

## 6. Nova Review

Nova decides: GO, GO WITH NOTES, REWORK, SPLIT or STOP.

## 7. Maintainer Commit

The human maintainer controls staging, commit, push and release.

## 8. CI / Validation

After push, CI is checked and failures are classified.

## 9. Follow-up

If project posture changes, update Health Score, Project Brain, risks or create next WP.
