# Neutral Example Project (SampleProject) — Adapter Validation Fixture

## DE – Zweck

Dieses Verzeichnis enthält **SampleProject**: ein fiktives, neutrales Beispielprojekt, das als Testfall (Fixture) für die praktische Validierung des NDF Project Adapters v0.2 dient (NDF-WP-047).

Wichtig:

- SampleProject ist **kein echtes Produkt** und keine lauffähige Software — nur dokumentierte Beispielartefakte.
- Es enthält **keine echten privaten Daten**: keine realen Projekt-, Personen-, Organisations- oder Kundennamen, keine echten Domains, keine echten Secrets.
- Es simuliert bewusst ein **gewachsenes, unaufgeräumtes Bestandsprojekt** mit Lücken, damit der Project Adapter etwas zu finden hat.

Abgrenzung: `examples/minimal-ndf-project/` zeigt ein Projekt, das NDF **bereits nutzt** (Post-Adoption). Dieses Fixture zeigt den Zustand **davor** (Pre-Adoption).

## EN – Purpose

This directory contains **SampleProject**: a fictitious, neutral example project serving as the fixture for the practical validation of the NDF Project Adapter v0.2 (NDF-WP-047).

Important:

- SampleProject is **not a real product** and not runnable software — documented example artifacts only.
- It contains **no real private data**: no real project, person, organization or customer names, no real domains, no real secrets.
- It deliberately simulates a **grown, untidy existing project** with gaps, so the project adapter has something to find.

Distinction: `examples/minimal-ndf-project/` shows a project **already using** NDF (post-adoption). This fixture shows the state **before** (pre-adoption).

## DE – Nutzung in WP-047 / EN – Usage in WP-047

WP-047 spielt den Adapter vollständig durch (Phasen 0–10 aus `docs/project-starter/PROJECT_ADAPTER_V0_2.md`):

1. Intake mit `PROJECT_BRIEF.md` als Maintainer-Input ausfüllen.
2. Read-only Review über alle Fixture-Dateien (inkl. `sample-docs/` und `MOCK_REPOSITORY_TREE.md`).
3. Baseline-Artefakte erzeugen und gegen `expected-adapter-output/README.md` bewerten.
4. Lücken des Adapters selbst als Findings an Nova (ChatGPT) zurückmelden.

## Relevante Dateien / Relevant files

| Datei | Rolle im Fixture |
|---|---|
| `PROJECT_BRIEF.md` | fiktive Projektbeschreibung (Intake-Input) |
| `CURRENT_STATE.md` | Ist-Zustand mit Lücken und Schulden |
| `REQUIREMENTS.md` | Anforderungen inkl. Security und DE/EN |
| `ARCHITECTURE_OVERVIEW.md` | grobe Architektur mit offenen Fragen |
| `SECURITY_NOTES.md` | Sicherheitsstand inkl. harmlosem Destructive-Action-Planungsfall |
| `ROADMAP.md` / `RISKS.md` | unklare Prioritäten und Risiken |
| `MOCK_REPOSITORY_TREE.md` | fiktive Repo-Struktur des Projekts |
| `sample-docs/` | bewusst unvollständige Projekt-Doku (Fundmaterial für den Adapter) |
| `expected-adapter-output/README.md` | erwartete Adapter-Ergebnisse für WP-047 |
