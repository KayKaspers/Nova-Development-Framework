# ADR-0026: First Real Reference Project Integration

## Status

Accepted

## Kontext

Foundation 0.1 hat das Nova Development Framework als strukturelles Fundament etabliert. Foundation 0.2 soll beweisen, dass NDF auf echte Projekte anwendbar ist.

## Entscheidung

Referenzprojekt B (CI/Docker-Referenz) wird als erstes echtes Projekt für NDF integriert.

## Begründung

Referenzprojekt B besitzt bereits reale technische Eigenschaften:

- Docker-first
- CI
- Preflight 2.0
- FFmpeg Build-Gate
- Tests mit Mocking
- reale Dokumentations- und Build-Risiken

## Konsequenzen

- NDF wird praktisch validiert.
- Referenzprojekt B erhält eine Project System Baseline.
- Lessons Learned fließen zurück ins NDF.
- Foundation 0.2 bekommt ein reales Referenzprojekt.
