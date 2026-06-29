# NDF Repository Structure Cleanup Plan

## Status

Draft / Foundation 0.1 Preparation

## Warum dieser Plan nötig ist

Das NDF ist inzwischen kein kleines Dokumentationsprojekt mehr. Es enthält:

- Foundation
- Academy
- Toolkit
- Prompt Library
- Template Library
- Project System
- Export Concept
- Website Concept
- ADRs
- Project Brain
- Reviews

Durch das schnelle Wachstum können Überschneidungen entstehen. Der Cleanup Plan verhindert, dass das Repository unübersichtlich wird.

## Grundsatz

> Erst planen, dann verschieben.

Dieser Plan definiert die Zielstruktur. Dateien werden erst nach Review und Freigabe verschoben.

## Aktuelle beobachtete Risiken

### Risiko 1 – Doppelte Template-Bereiche

Es gibt teils alte `templates/`-Bereiche und neue `framework/templates/`-Bereiche.

### Risiko 2 – Standards verteilt

Standards können in `standards/`, `framework/standards/` und `docs/` auftauchen.

### Risiko 3 – Changelog-Dateien verstreut

Mehrere Changelog-Dateien liegen wahrscheinlich auf Root-Ebene.

### Risiko 4 – Paket-READMEs

Einige Import- oder Paket-README-Dateien sind nach dem Import nicht dauerhaft nötig.

### Risiko 5 – Docs ohne klare Navigation

`docs/` wächst stark und braucht eine verbindliche Unterstruktur.

## Zielstruktur

```text
Nova-Development-Framework/
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
├── LICENSE.md
├── ROADMAP.md
│
├── academy/
│   └── band-1-foundation/
│
├── adr/
│
├── assets/
│   ├── images/
│   ├── diagrams/
│   ├── branding/
│   └── screenshots/
│
├── branding/
│
├── build/
│   ├── book-manifests/
│   ├── mkdocs/
│   ├── pandoc/
│   └── styles/
│
├── docs/
│   ├── academy/
│   ├── architecture/
│   ├── blueprint/
│   ├── constitution/
│   ├── domain/
│   ├── export/
│   ├── governance/
│   ├── project-starter/
│   ├── project-system/
│   ├── release/
│   ├── repository/
│   ├── reviews/
│   ├── toolkit/
│   └── website/
│
├── examples/
│   └── minimal-ndf-project/
│
├── framework/
│   ├── prompts/
│   ├── templates/
│   ├── standards/
│   ├── project-system/
│   ├── project-starter/
│   └── toolkit/
│
├── project-brain/
│
├── scripts/
│
└── exports/
    ├── pdf/
    ├── word/
    ├── web/
    └── epub/
```

## Verzeichnisregeln

### Root

Root enthält nur zentrale Projektdateien:

- README.md
- CONTRIBUTING.md
- SECURITY.md
- CODE_OF_CONDUCT.md
- CHANGELOG.md
- LICENSE.md
- ROADMAP.md

Keine Sprint-README-Dateien dauerhaft im Root.

### academy/

Enthält Lernmaterial und Handbuchstruktur.

### adr/

Enthält ausschließlich Architecture Decision Records.

### docs/

Enthält erklärende Dokumentation zum Framework.

### framework/

Enthält nutzbare Framework-Bausteine:

- Prompts
- Templates
- Standards
- Toolkit-Definitionen
- Project-System-Vorlagen

### project-brain/

Enthält Langzeitwissen des NDF-Projekts.

### examples/

Enthält Beispielprojekte.

### build/

Enthält Export- und Website-Build-Konfiguration.

### exports/

Enthält generierte Artefakte. Diese sind abgeleitet, nicht Source of Truth.

## Cleanup-Strategie

### Phase 1 – Bestandsaufnahme

- Root-Dateien prüfen
- doppelte Changelogs identifizieren
- doppelte Template-Strukturen identifizieren
- Standards-Standorte prüfen

### Phase 2 – Zielstruktur bestätigen

- Zielstruktur mit Nova prüfen
- Sonderfälle dokumentieren
- ADR ergänzen, falls nötig

### Phase 3 – kontrolliertes Verschieben

- keine Massenverschiebung ohne Review
- kleine Commits
- pro Commit nur eine Strukturänderung
- GitHub Desktop Changes prüfen

### Phase 4 – README und Navigation aktualisieren

Nach dem Verschieben:

- README Repository Structure aktualisieren
- Website Navigation Draft prüfen
- Project Brain aktualisieren

## Empfehlung Nova

Vor Foundation 0.1 sollten wir mindestens:

1. Root bereinigen.
2. Changelog-Strategie festlegen.
3. `framework/templates/` als zentrale Template-Quelle festlegen.
4. `framework/prompts/` als zentrale Prompt-Quelle festlegen.
5. `docs/` nach Themenbereichen stabilisieren.

## Wichtig

Dieser Plan ist bewusst konservativ.  
Wir verschieben nur, was eindeutig ist.
