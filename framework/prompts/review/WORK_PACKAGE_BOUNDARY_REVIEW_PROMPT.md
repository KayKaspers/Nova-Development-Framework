# Claude Prompt – Work Package Boundary Review

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Verify that a completed work package stayed within its declared type and scope before commit: changed files, unrelated changes, tests. Decision: GO / GO WITH NOTES / REWORK / SPLIT / STOP. Review-only — no changes, no commit, no push. Finish with the structured feedback to Nova (ChatGPT).

## Rolle

Du bist Claude und prüfst, ob ein abgeschlossenes Work Package innerhalb seiner Grenzen geblieben ist.

## Work Package Type

review-only

## Ziel

Prüfe Scope, Dateiliste, Tests und Risiken vor Commit.

## Aufgabe

1. Prüfe den deklarierten Work-Package-Typ.
2. Prüfe alle geänderten Dateien.
3. Prüfe, ob Änderungen zum Typ passen.
4. Markiere unrelated Änderungen.
5. Prüfe Tests oder Begründung für fehlende Tests.
6. Gib eine Commit-Empfehlung.

## Entscheidung

Nutze eine dieser Entscheidungen:

```text
GO
GO WITH NOTES
REWORK
SPLIT
STOP
```

## Grenzen

Keine Änderungen. Kein Commit. Kein Push.

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Entscheidung

### Begründung

### Geänderte Dateien

### Scope-Bewertung

### Tests

### Risiken

### Commit-Empfehlung
