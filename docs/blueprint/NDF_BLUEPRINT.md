# Nova Development Framework Blueprint

Version: 0.1  
Status: Strategic Draft  
Purpose: Langfristige Architektur des NDF

## 1. Warum dieser Blueprint existiert

Das NDF ist mehr als ein Handbuch oder eine Sammlung von Vorlagen. Es soll ein vollständiges Entwicklungsframework werden, das Projekte von der ersten Idee bis zum stabilen Release begleitet.

Der Blueprint verhindert, dass das Framework zufällig wächst. Er definiert die tragende Architektur.

## 2. Das Säulenmodell

Das NDF besteht aus sechs Säulen.

```text
NDF
├── Foundation
├── Academy
├── Toolkit
├── AI Collaboration
├── Delivery
└── Best Practices
```

## 3. Säule 1 – Foundation

Foundation ist das Regelwerk.

Enthält:

- Constitution
- Governance
- ADR-System
- Standards
- Project Brain
- Quality Gates
- Release-Politik
- Sicherheitsregeln

Ziel: Alle Projekte haben dieselbe stabile Grundlage.

## 4. Säule 2 – Academy

Academy ist das Lehrwerk.

Enthält:

- Einsteigerkurse
- Handbuch
- Übungen
- Lösungen
- Glossar
- Beispiele
- DE/EN-Lernpfade

Ziel: Nutzer verstehen nicht nur, was zu tun ist, sondern warum.

## 5. Säule 3 – Toolkit

Toolkit ist die praktische Werkzeugkiste.

Enthält:

- Templates
- Prompt Library
- Checklisten
- Generatoren
- Skripte
- Projektstarter
- Export-Werkzeuge

Ziel: Wiederverwendbare Bausteine statt wiederholter Handarbeit.

## 6. Säule 4 – AI Collaboration

AI Collaboration beschreibt die Zusammenarbeit mit KI.

Enthält:

- Nova-Rolle
- Claude-Rolle
- optional Cursor
- Prompt-Standards
- Rückmeldung an Nova
- Sicherheitsgrenzen
- Review-Abläufe

Ziel: KI produktiv nutzen, ohne Kontrolle zu verlieren.

## 7. Säule 5 – Delivery

Delivery beschreibt den Weg von Idee zu Release.

Enthält:

- Projektstart
- Architekturphase
- Umsetzung
- Tests
- Dokumentation
- Release
- Wartung

Ziel: Projekte nicht nur bauen, sondern professionell veröffentlichen.

## 8. Säule 6 – Best Practices

Best Practices speichern Erfahrung.

Enthält:

- Lessons Learned aus CastCore
- Lessons Learned aus SpeakCore
- Lessons Learned aus AirCore
- Lessons Learned aus SC-OrgaSuite
- wiederverwendbare Entscheidungen
- typische Fehler

Ziel: Jedes Projekt macht das NDF besser.

## 9. Repository-Strategie

Langfristig wird das NDF in vier Repositories aufgeteilt.

```text
ndf-core
ndf-academy
ndf-toolkit
ndf-examples
```

Kurzfristig bleibt alles in einem Repository, bis Struktur und Inhalte stabil sind.

## 10. Wann wird aufgeteilt?

Eine Aufteilung erfolgt erst, wenn mindestens zwei Bedingungen erfüllt sind:

- Repository wird unübersichtlich
- Academy wächst stark
- Generator/Toolkit bekommt eigene technische Abhängigkeiten
- externe Nutzer sollen nur einzelne Teile verwenden
- Releases brauchen getrennte Versionierung

## 11. Zielbild

Das NDF soll irgendwann Folgendes ermöglichen:

1. Neues Projekt starten.
2. Fragenkatalog beantworten.
3. NDF erzeugt Grundstruktur.
4. README, Roadmap, Project Brain und Prompts entstehen automatisch.
5. Projekt startet mit Docker, CI, Standards und Dokumentation.

## 12. Grundsatz

Das NDF ist kein statisches Dokument.

Es ist ein lernendes Entwicklungsframework.
