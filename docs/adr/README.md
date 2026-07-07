# Architecture Decision Records – Dokumentations- und Themen-ADRs

Dieser Ordner enthält dokumentationsnahe und thematische ADRs des Nova Development Frameworks, insbesondere ab Foundation 0.2 (ADR-0027 ff.). / This directory contains the public ADR policy and thematic decision records of NDF.

**Einstieg / start here:** [`ADR_POLICY.md`](ADR_POLICY.md) (verbindliche Minimal-Policy seit NDF-WP-086) · [`ADR_TEMPLATE.md`](ADR_TEMPLATE.md)

## Abgrenzung

- `adr/` – Foundation-/Framework-Kernentscheidungen (0.1-Ära, eingefroren)
- `docs/adr/` – spätere dokumentationsnahe und thematische ADRs (dieser Ordner)

Neue ADRs entstehen hier. Die nächste freie Nummer ergibt sich aus der höchsten vorhandenen ADR-Nummer über beide Ordner hinweg (aktuell: ADR-0031 wäre die nächste).

## Bekannte Nummerierungs-Überschneidung

Die frühen Dateien ADR-0001 bis ADR-0005 in diesem Ordner stammen aus der ersten Aufbauphase und überschneiden sich nummerisch mit den Kern-ADRs unter `adr/`, behandeln aber teils andere Themen. **Entscheidung (NDF-WP-086, `ADR_POLICY.md`):** Sie bleiben dokumentierter Altbestand ohne Massenmigration; künftige Nummern kollidieren nicht mehr, weil neue ADRs die nächste freie Nummer über beide Ordner hinweg nutzen (aktuell ADR-0031).
