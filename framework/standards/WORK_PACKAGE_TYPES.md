# NDF Standard – Work Package Types

## Pflicht

Jedes Work Package muss einen Typ haben.

## Typen

| Typ | Zweck | Code erlaubt? |
|---|---|---|
| Review-only | prüfen und berichten | nein |
| Docs-only | Dokumentation | nein |
| Code-fix | fokussierte Codeänderung | ja |
| Test-only | Tests | nur Testcode |
| Security-baseline | Security-Review | nein |
| Health-score-update | Score nach validiertem Stand | nein |
| CI-diagnostic | CI/Build-Fehler analysieren | ggf. |
| Destructive-blueprint | gefährliche Aktion planen | nein |
| Destructive-implementation | genehmigte destructive action bauen | ja |

## Regel

Unterschiedliche Typen nicht ohne Freigabe in einem Commit mischen.
