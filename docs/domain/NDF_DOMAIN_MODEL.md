# NDF Domain Model

Version: 0.1  
Status: Foundation Architecture

## Zweck

Das Domain Model definiert die zentralen Begriffe des Nova Development Frameworks. Es sorgt dafür, dass alle Teile des Frameworks dieselbe Sprache verwenden.

## Grundsatz

Ein Framework ohne gemeinsames Vokabular wird inkonsistent. Das NDF definiert deshalb seine Kernobjekte bewusst und verbindlich.

## Kernobjekte

```text
Project
Module
Artifact
Standard
Rule
Decision
Work Package
Prompt
Template
Quality Gate
Review
Milestone
Release
Lesson Learned
Knowledge Node
Project Brain
Project Adapter
Capability
Compliance Check
Health Score
```

## Project

Ein Project ist ein konkretes Software-, Dokumentations- oder Infrastrukturvorhaben, das nach NDF-Standards geplant, umgesetzt und gepflegt wird.

Beispiele:

- CastCore
- SpeakCore
- AirCore
- SC-OrgaSuite
- NDF selbst

Ein Project besitzt:

- Project Brain
- Roadmap
- Standards
- Work Packages
- Releases
- Lessons Learned

## Module

Ein Module ist ein logisch abgegrenzter Bestandteil eines Projekts oder Frameworks.

Beispiele:

- Backend
- Frontend
- Worker
- Documentation
- Prompt Library
- Academy
- Toolkit

Ein Module besitzt:

- Zweck
- Verantwortlichkeit
- Schnittstellen
- Qualitätskriterien

## Artifact

Ein Artifact ist ein dauerhaftes Ergebnis.

Beispiele:

- README
- Architekturdiagramm
- ADR
- Dockerfile
- Prompt
- Release Notes
- Handbuchkapitel

Artifacts sind versioniert oder zumindest nachvollziehbar dokumentiert.

## Standard

Ein Standard beschreibt, wie etwas grundsätzlich gemacht wird.

Beispiele:

- Git Standard
- Documentation Standard
- Security Standard
- Prompt Standard
- Release Standard

Standards erzeugen Regeln und Quality Gates.

## Rule

Eine Rule ist eine konkrete verbindliche Regel.

Beispiel:

> KI darf keine unverifizierten Pushes ausführen.

Rules sind prüfbarer als Standards.

## Decision

Eine Decision ist eine dokumentierte Entscheidung, meist als ADR.

Eine Decision beantwortet:

- Warum wurde entschieden?
- Welche Alternativen gab es?
- Was sind Konsequenzen?

## Work Package

Ein Work Package ist eine kleine umsetzbare Aufgabe.

Eigenschaften:

- klares Ziel
- definierter Kontext
- Grenzen
- Qualitätsregeln
- erwartete Rückmeldung

## Prompt

Ein Prompt ist eine strukturierte Arbeitsanweisung an ein KI-System.

Prompts im NDF enthalten mindestens:

- Ziel
- Kontext
- Aufgabe
- Grenzen
- Qualitätsregeln
- Rückmeldung an Nova

## Template

Ein Template ist eine wiederverwendbare Vorlage.

Beispiele:

- README Template
- ADR Template
- Work Package Template
- Claude Prompt Template

## Quality Gate

Ein Quality Gate ist ein Prüfschritt, der erfüllt sein muss, bevor ein Arbeitsschritt oder Release weitergeht.

Beispiele:

- keine Secrets
- Dokumentation aktualisiert
- Tests ausgeführt
- GitHub Desktop Changes geprüft

## Review

Ein Review ist eine strukturierte Prüfung.

Reviews können sein:

- Code Review
- Architecture Review
- Documentation Review
- Security Review
- Release Review

## Milestone

Ein Milestone ist ein geplanter größerer Fortschritt.

Beispiele:

- Foundation 0.1
- Prompt Library v0.1
- Academy Band 1
- Generator v0.1

## Release

Ein Release ist eine veröffentlichte Version mit Changelog, Qualitätsprüfung und nachvollziehbarem Stand.

## Lesson Learned

Eine Lesson Learned ist eine Erfahrung aus einem Projekt, die künftige Arbeit verbessert.

Beispiel:

> Cursor ist optional, weil GitHub Desktop einsteigerfreundlicher ist.

## Knowledge Node

Ein Knowledge Node ist ein einzelnes Wissenselement im NDF Knowledge Graph.

Beispiele:

- eine Regel
- ein Standard
- eine Entscheidung
- ein Prompt
- eine Lesson Learned

## Project Brain

Der Project Brain ist das Langzeitgedächtnis eines Projekts.

Er enthält:

- Status
- Entscheidungen
- Roadmap
- Risiken
- Lessons Learned
- offene Fragen

## Project Adapter

Ein Project Adapter verbindet ein konkretes Projekt mit dem NDF.

Er beschreibt:

- Projektstatus
- projektspezifische Regeln
- relevante Standards
- relevante Prompts
- Quality Gates
- erste Arbeitspakete

## Capability

Eine Capability ist eine Fähigkeit eines Projekts oder Frameworks.

Beispiele:

- Docker Support
- CI/CD
- FFmpeg Processing
- Multi Language
- Preflight
- Admin Dashboard

## Compliance Check

Ein Compliance Check prüft, ob ein Projekt NDF-Regeln erfüllt.

## Health Score

Der Health Score bewertet den Zustand eines Projekts über mehrere Qualitätsdimensionen.
