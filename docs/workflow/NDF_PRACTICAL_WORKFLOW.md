# Praktischer NDF-Workflow / NDF Practical Workflow

## DE

### Zweck

Dieser Workflow beschreibt, wie Softwareprojekte mit dem Nova Development Framework praktisch umgesetzt werden. Der Fokus liegt auf einfacher Bedienung, klarer Verantwortung und hoher Qualität.

### Rollen

- **Nova (ChatGPT)** — die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle ([NOVA_CHATGPT_ROLE.md](NOVA_CHATGPT_ROLE.md))
- **Implementation Agent** (z. B. Claude) — setzt genau ein Work Package um
- **Human Maintainer** — prüft, committet, pusht, gibt Releases frei

Werkzeuge: VS Code (Dateien ansehen/bearbeiten), GitHub Desktop (Commit/Push/Pull ohne Terminal), GitHub (Repository, Historie, Releases). Cursor ist optional und nicht Teil des Einsteiger-Standards.

### Standardablauf

```text
Nova (ChatGPT) plant
↓
Implementation Agent setzt ein kleines Work Package um
↓
Maintainer prüft in VS Code
↓
GitHub Desktop zeigt Änderungen
↓
Maintainer committet und pusht
↓
Implementation Agent liefert Rückmeldung an Nova
↓
Nova reviewt und erstellt nächsten Schritt
```

Typische Work-Package-Schritte: Klassifizieren → Planen → Umsetzen → Rückmeldung → Review → Commit ([WORK_PACKAGE_LIFECYCLE.md](../../framework/standards/WORK_PACKAGE_LIFECYCLE.md)).

### Regel 1 – Kleine Work Packages

Der Implementation Agent bekommt niemals große Sammelaufgaben. Ein Work Package soll idealerweise in 30 bis 90 Minuten prüfbar sein.

### Regel 2 – Menschliche Veröffentlichung

KI darf Dateien erstellen oder ändern, aber nicht eigenständig veröffentlichen. Commits und Pushes bleiben menschlich kontrolliert.

### Regel 3 – Rückmeldung an Nova

Jeder Arbeitsschritt des Implementation Agent endet mit einer strukturierten Rückmeldung an Nova (die ChatGPT-basierte Review-Rolle).

### Regel 4 – Dokumentation gehört zur Aufgabe

Wenn eine Funktion geändert wird, muss passende Dokumentation geprüft oder ergänzt werden.

### Regel 5 – Keine unklaren Repository-Zustände

Wenn ein Tool keine Ausgabe liefert oder ein Befehl unklar ist, wird gestoppt.

## EN

### Purpose

This workflow describes how software projects are executed in practice with the Nova Development Framework. The focus is on simple handling, clear responsibility, and high quality.

### Roles

- **Nova (ChatGPT)** — the ChatGPT-based planning, architecture and review role ([NOVA_CHATGPT_ROLE.md](NOVA_CHATGPT_ROLE.md))
- **Implementation Agent** (e.g. Claude) — executes exactly one work package
- **Human Maintainer** — reviews, commits, pushes, approves releases

Tools: VS Code (view/edit files), GitHub Desktop (commit/push/pull without a terminal), GitHub (repository, history, releases). Cursor is optional and not part of the beginner standard.

### Standard flow

```text
Nova (ChatGPT) plans
↓
Implementation Agent executes one small work package
↓
Maintainer reviews in VS Code
↓
GitHub Desktop shows the changes
↓
Maintainer commits and pushes
↓
Implementation Agent delivers the feedback to Nova
↓
Nova reviews and prepares the next step
```

Typical work package steps: Classify → Plan → Execute → Report → Review → Commit ([WORK_PACKAGE_LIFECYCLE.md](../../framework/standards/WORK_PACKAGE_LIFECYCLE.md)).

### Rule 1 – Small work packages

The Implementation Agent never receives large bundled tasks. A work package should ideally be reviewable in 30 to 90 minutes.

### Rule 2 – Human publication

AI may create or change files, but never publishes on its own. Commits and pushes stay under human control.

### Rule 3 – Feedback to Nova

Every Implementation Agent step ends with a structured feedback to Nova (the ChatGPT-based review role).

### Rule 4 – Documentation is part of the task

When functionality changes, matching documentation must be checked or extended.

### Rule 5 – No unclear repository states

If a tool produces no output or a command is unclear: stop, don't guess.
