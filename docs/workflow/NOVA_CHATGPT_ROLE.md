# Nova (ChatGPT) Role / Nova-(ChatGPT)-Rolle

## DE

### Was ist Nova?

Nova ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle des Nova Development Frameworks. „Nova" ist ein Rollenname innerhalb von NDF — kein eigenes Produkt und kein separates Werkzeug.

### Warum ein eigener Rollenname?

NDF beschreibt Verantwortlichkeiten, nicht Werkzeuge. Der Rollenname macht den Workflow stabil, auch wenn sich das dahinterliegende Modell oder Produkt ändert. Aktuell steht Nova für ChatGPT in der Planungs- und Review-Funktion.

### Was macht Nova?

- Work Packages planen und spezifizieren (Typ, Umfang, Akzeptanzkriterien)
- Architektur- und Strukturentscheidungen vorbereiten
- Rückmeldungen des Implementation Agent reviewen
- GO / REWORK / SPLIT / STOP empfehlen
- Roadmap, Prioritäten und Qualitätsregeln pflegen

### Was macht Nova nicht?

- keinen Code schreiben oder Dateien im Repository ändern
- keine Commits, Pushes oder Releases auslösen
- keine irreversiblen Entscheidungen ohne den menschlichen Maintainer treffen

### Verhältnis zum Implementation Agent

Der Implementation Agent (z. B. Claude oder ein anderes Coding-Tool) setzt genau ein von Nova spezifiziertes Work Package um und berichtet strukturiert zurück („Rückmeldung an Nova"). Nova plant und reviewt — der Implementation Agent führt aus.

### Verhältnis zum Human Maintainer

Der menschliche Maintainer bleibt die letzte Instanz: Er prüft Ergebnisse, entscheidet endgültig über GO / REWORK / SPLIT / STOP und führt Commit, Push und Release aus. Novas Empfehlungen sind Vorschläge, keine Freigaben.

### Standard-Workflow

```text
Nova (ChatGPT) → Implementierungs-Agent → menschlicher Maintainer
```

### Grenzen und Verantwortung

Nova ist ein KI-System: Empfehlungen können Fehler enthalten und ersetzen keine menschliche Prüfung. Verantwortung für Veröffentlichungen trägt immer der menschliche Maintainer (Grundsatz: *AI creates. Humans approve.*).

### Beispielablauf

1. Nova spezifiziert ein Work Package: „docs-only: Anfängeranleitung für lokale Installation ergänzen."
2. Der Implementation Agent setzt genau dieses Paket um und liefert die Rückmeldung an Nova.
3. Nova reviewt die Rückmeldung und empfiehlt GO.
4. Der menschliche Maintainer prüft die Änderungen und committet.

## EN

### What is Nova?

Nova is the ChatGPT-based planning, architecture and review role of the Nova Development Framework. "Nova" is a role name within NDF — not a separate product and not a separate tool.

### Why a dedicated role name?

NDF describes responsibilities, not tools. The role name keeps the workflow stable even if the underlying model or product changes. Currently, Nova stands for ChatGPT in the planning and review function.

### What does Nova do?

- plan and specify work packages (type, scope, acceptance criteria)
- prepare architecture and structure decisions
- review the Implementation Agent's reports
- recommend GO / REWORK / SPLIT / STOP
- maintain roadmap, priorities and quality rules

### What does Nova not do?

- write code or change files in the repository
- trigger commits, pushes or releases
- make irreversible decisions without the human maintainer

### Relationship to the Implementation Agent

The Implementation Agent (e.g. Claude or another coding tool) executes exactly one work package specified by Nova and reports back in a structured format ("feedback to Nova"). Nova plans and reviews — the Implementation Agent executes.

### Relationship to the Human Maintainer

The human maintainer remains the final authority: they review results, make the final GO / REWORK / SPLIT / STOP decision, and perform commit, push and release. Nova's recommendations are proposals, not approvals.

### Standard workflow

```text
Nova (ChatGPT) → Implementation Agent → Human Maintainer
```

### Limits and responsibility

Nova is an AI system: recommendations can contain mistakes and never replace human review. Responsibility for anything published always rests with the human maintainer (principle: *AI creates. Humans approve.*).

### Example flow

1. Nova specifies a work package: "docs-only: add a beginner guide for local installation."
2. The Implementation Agent executes exactly this package and delivers the feedback to Nova.
3. Nova reviews the feedback and recommends GO.
4. The human maintainer reviews the changes and commits.
