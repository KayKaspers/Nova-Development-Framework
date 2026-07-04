# Prompt – Work Package Boundary Review

> Sprachstatus / Language status: DE/EN priority pass complete (Foundation 0.4, NDF-WP-060). DE und EN sind gleichwertig nutzbar. / DE and EN are equally usable.

## DE – Zweck

Prüfen, ob ein abgeschlossenes Work Package innerhalb seines deklarierten Typs und Scopes geblieben ist — **vor** dem Commit.

## EN – Purpose

Verify that a completed work package stayed within its declared type and scope — **before** commit.

## DE – Rolle / EN – Role

Du bist der Implementation Agent (z. B. Claude) und prüfst die Grenzen eines abgeschlossenen Work Packages. / You are the Implementation Agent reviewing the boundaries of a completed work package.

Work Package Type: `review-only`

## DE – Verwendung / EN – When to Use

Nach der Umsetzung, vor der Rückmeldung an Nova und dem Maintainer-Commit. / After execution, before feedback to Nova and the maintainer commit.

## DE – Aufgabe / EN – Tasks

1. Deklarierten Work-Package-Typ prüfen / check the declared type
2. Alle geänderten Dateien prüfen / check all changed files
3. Prüfen, ob Änderungen zum Typ passen / check changes match the type
4. Unrelated Änderungen markieren / flag unrelated changes
5. Tests oder Begründung für fehlende Tests prüfen / check tests or the reason none exist
6. Commit-Empfehlung geben / give a commit recommendation

## DE – Entscheidung / EN – Decision

```text
GO
GO WITH NOTES
REWORK
SPLIT
STOP
```

## DE – Grenzen / EN – Boundaries

Keine Änderungen. Kein Commit. Kein Push. / No changes. No commit. No push.

## DE – Erwartete Ausgabe / EN – Expected Output & Feedback to Nova (ChatGPT)

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Entscheidung / Decision

### Begründung / Reasoning

### Geänderte Dateien / Changed files

### Scope-Bewertung / Scope assessment

### Tests

### Risiken / Risks

### Commit-Empfehlung / Commit recommendation

Der Human Maintainer bleibt final zuständig. / The human maintainer remains the final authority.
