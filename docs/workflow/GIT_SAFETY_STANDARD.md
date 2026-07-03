# Git Safety Standard

## Grundsatz

Repository-Verlauf ist wertvoll. Änderungen am Verlauf dürfen nicht automatisiert und unkontrolliert erfolgen.

## KI darf nicht automatisch

- pushen
- force pushen
- resetten
- rebasen
- clean ausführen
- Branches löschen
- Tags löschen
- Commits veröffentlichen

## Menschliche Kontrolle

Der Maintainer führt Commits und Pushes über GitHub Desktop aus.

## Stop-Regel

Wenn Tool-Ausgaben fehlen oder unklar sind:

> Stoppen. Nicht raten. Nova fragen.

## Erlaubte Prüfungen

Claude oder Nova dürfen vorschlagen:

- git status
- git diff
- Tests
- Dateiprüfung

Aber Veröffentlichung bleibt menschlich.
