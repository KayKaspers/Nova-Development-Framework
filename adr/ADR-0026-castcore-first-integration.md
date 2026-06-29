# ADR-0026: CastCore as First Real NDF Integration

## Status

Accepted

## Kontext

Foundation 0.1 hat das Nova Development Framework als strukturelles Fundament etabliert. Foundation 0.2 soll beweisen, dass NDF auf echte Projekte anwendbar ist.

## Entscheidung

CastCore wird als erstes echtes Referenzprojekt für NDF integriert.

## Begründung

CastCore besitzt bereits reale technische Eigenschaften:

- Docker-first
- CI
- Preflight 2.0
- FFmpeg Build-Gate
- Tests mit Mocking
- reale Dokumentations- und Build-Risiken

## Konsequenzen

- NDF wird praktisch validiert.
- CastCore erhält eine Project System Baseline.
- Lessons Learned fließen zurück ins NDF.
- Foundation 0.2 bekommt ein reales Referenzprojekt.
