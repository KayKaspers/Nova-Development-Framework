# NDF Toolkit Architecture

## Architekturidee

```text
User Input
   ↓
Project Manifest
   ↓
Project Profile
   ↓
Template Selection
   ↓
Prompt Selection
   ↓
Quality Gates
   ↓
Generated Work Packages
   ↓
Human Review
```

## Hauptmodule

### Project Starter

Erstellt Grundstruktur für neue Projekte.

### Prompt Selector

Wählt passende Prompts aus der Prompt Library.

### Template Selector

Wählt passende Templates aus der Template Library.

### Quality Check Helper

Hilft bei manuellen oder später automatisierten Quality Gates.

### Release Helper

Bereitet Release Notes, Checklist und Changelog vor.

### Project Adapter Helper

Bindet bestehende Projekte an NDF an.

## Designregel

Jedes Toolkit-Modul muss ohne Automatisierung nutzbar sein, bevor es automatisiert wird.
