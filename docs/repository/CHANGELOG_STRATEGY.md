# Changelog Strategy

## Problem

Während der Foundation-Phase entstanden mehrere Changelog-Dateien für einzelne Pakete.

Das war für den Aufbau hilfreich, ist aber langfristig unübersichtlich.

## Ziel

Ein zentrales `CHANGELOG.md` im Root ist die Hauptquelle.

## Modul-Changelogs

Modul-Changelogs dürfen existieren, wenn ein Modul eigenständig versioniert wird.

Beispiele:

- Prompt Library
- Template Library
- Toolkit
- Academy

## Empfehlung für Foundation 0.1

Kurzfristig:

- Root `CHANGELOG.md` als Hauptchangelog pflegen.
- Paket-Changelogs später in `docs/release/history/` oder Modulordner verschieben.

Langfristig:

```text
CHANGELOG.md
docs/release/history/
framework/prompts/CHANGELOG.md
framework/templates/CHANGELOG.md
academy/CHANGELOG.md
```

## Regel

Jeder Release braucht einen Eintrag im Hauptchangelog.
