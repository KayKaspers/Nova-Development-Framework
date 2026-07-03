# NDF Practical Workflow v0.1

## Ziel

Dieser Workflow beschreibt, wie Softwareprojekte mit dem Nova Development Framework praktisch umgesetzt werden.

Der Fokus liegt auf einfacher Bedienung, klarer Verantwortung und hoher Qualität.

## Standard-Werkzeuge

- ChatGPT / Nova: Planung, Architektur, Review, Prompts
- Claude: Umsetzung konkreter Arbeitspakete
- VS Code: Dateien ansehen und bearbeiten
- GitHub Desktop: Commit, Push, Pull
- GitHub: Repository, Historie, Releases

Cursor ist optional und nicht Teil des Einsteiger-Standards.

## Grundablauf

```text
Nova plant
↓
Claude setzt ein kleines Arbeitspaket um
↓
Maintainer prüft in VS Code
↓
GitHub Desktop zeigt Änderungen
↓
Maintainer committet
↓
Maintainer pusht
↓
Claude liefert Rückmeldung an Nova
↓
Nova reviewt und erstellt nächsten Schritt
```

## Regel 1 – Kleine Arbeitspakete

Claude bekommt niemals große Sammelaufgaben.

Ein Arbeitspaket soll idealerweise in 30 bis 90 Minuten prüfbar sein.

## Regel 2 – Menschliche Veröffentlichung

KI darf Dateien erstellen oder ändern, aber nicht eigenständig veröffentlichen.

Commits und Pushes bleiben menschlich kontrolliert.

## Regel 3 – Rückmeldung an Nova

Jeder Claude-Arbeitsschritt endet mit einer strukturierten Rückmeldung an Nova.

## Regel 4 – Dokumentation gehört zur Aufgabe

Wenn eine Funktion geändert wird, muss passende Dokumentation geprüft oder ergänzt werden.

## Regel 5 – Keine unklaren Repository-Zustände

Wenn ein Tool keine Ausgabe liefert oder ein Befehl unklar ist, wird gestoppt.
