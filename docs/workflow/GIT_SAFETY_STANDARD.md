# Git-Safety-Standard / Git Safety Standard

## DE

### Grundsatz

Repository-Verlauf ist wertvoll. Änderungen am Verlauf dürfen nicht automatisiert und unkontrolliert erfolgen.

### Der Implementation Agent darf nicht automatisch

- committen oder pushen
- force-pushen
- resetten oder rebasen
- `git clean` ausführen
- Branches oder Tags löschen
- Commits veröffentlichen

Force-Pushes sind generell nur nach expliziter Freigabe durch den Human Maintainer erlaubt.

### Menschliche Kontrolle

Der Human Maintainer führt Commits und Pushes aus (z. B. über GitHub Desktop). Commits sind klein und scoped: ein Work Package, eine nachvollziehbare Commit-Message.

### Keine Secrets

Keine Secrets committen (`.env`, Keys, Tokens, Credentials). Vor jedem Commit werden die Änderungen darauf geprüft.

### Statusdisziplin

`git status` wird vor und nach Änderungen geprüft — kein Commit aus einem unklaren Repository-Zustand heraus.

### Stop-Regel

Wenn Tool-Ausgaben fehlen oder unklar sind:

> Stoppen. Nicht raten. Nova (ChatGPT) fragen.

### Erlaubte Prüfungen

Der Implementation Agent oder Nova dürfen vorschlagen: `git status`, `git diff`, Tests, Dateiprüfungen. Die Veröffentlichung bleibt menschlich.

## EN

### Principle

Repository history is valuable. History changes must never happen automatically and uncontrolled.

### The Implementation Agent must never automatically

- commit or push
- force-push
- reset or rebase
- run `git clean`
- delete branches or tags
- publish commits

Force pushes in general require explicit approval by the human maintainer.

### Human control

The human maintainer performs commits and pushes (e.g. via GitHub Desktop). Commits are small and scoped: one work package, one traceable commit message.

### No secrets

Never commit secrets (`.env`, keys, tokens, credentials). Changes are checked for secrets before every commit.

### Status discipline

`git status` is checked before and after changes — never commit from an unclear repository state.

### Stop rule

If tool output is missing or unclear:

> Stop. Don't guess. Ask Nova (ChatGPT).

### Allowed checks

The Implementation Agent or Nova may propose: `git status`, `git diff`, tests, file checks. Publication stays human.
