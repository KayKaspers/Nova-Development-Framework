# ADR-0001: Human-Governed Git Operations

## Status
Accepted

## Entscheidung

KI-Agenten dürfen keine unkontrollierten Git-Operationen durchführen, die Repository-Verlauf oder entfernte Repositories verändern.

## Gilt besonders für

- git commit
- git push
- git reset
- git clean
- git rebase
- git merge
- git tag delete
- force push

## Begründung

Repository-Operationen sind sicherheits- und verlaufsrelevant. Wenn ein KI-Agent keine eindeutigen Terminalausgaben oder Exit-Codes prüfen kann, darf er nicht fortfahren.

## Regel

**AI creates. Humans approve. Humans publish.**
