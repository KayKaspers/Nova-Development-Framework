# Academy Lesson – Work Package Types

## Ziel

Lerne, warum professionelle KI-gestützte Entwicklung kleine, klar typisierte Arbeitspakete braucht.

## Problem

Ohne klare Typen passiert schnell Folgendes:

- ein Review wird zum Code-Fix
- ein Code-Fix verändert nebenbei Dokumentation, CI und Docker
- ein Security-Review hebt den Health Score an, obwohl nichts verbessert wurde
- eine Delete-Funktion wird ohne Blueprint gebaut

## Lösung

NDF nutzt Work-Package-Typen.

## Beispiel aus CastCore

`CC-WP-006 Security Baseline Review` hatte den Typ `security-baseline`.

Danach wurde `CC-WP-007 Fail-closed Secret Validation` als `security-code-fix` umgesetzt.

Der Health Score wurde anschließend separat als `health-score-update` angepasst.

## Beispiel aus SpeakCore

Eine Backup-Delete-Funktion darf nicht direkt implementiert werden.

Erst:

```text
destructive-blueprint
```

Dann nach Review:

```text
destructive-implementation
```

## Merksatz

```text
Erst Typ, dann Prompt, dann Umsetzung.
```
