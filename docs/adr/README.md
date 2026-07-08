# Architecture Decision Records – Dokumentations- und Themen-ADRs

Dieser Ordner enthält dokumentationsnahe und thematische ADRs des Nova Development Frameworks, insbesondere ab Foundation 0.2 (ADR-0027 ff.). / This directory contains the public ADR policy and thematic decision records of NDF.

**Einstieg / start here:** [`ADR_POLICY.md`](ADR_POLICY.md) (verbindliche Minimal-Policy seit NDF-WP-086) · [`ADR_TEMPLATE.md`](ADR_TEMPLATE.md)

## Angenommene thematische ADRs (Auswahl) / Accepted thematic ADRs (selection)

- [`ADR-0031-v1x-compatibility-policy.md`](ADR-0031-v1x-compatibility-policy.md) — v1.x Compatibility Policy (Accepted, NDF-WP-100): Governance-Rahmen für v1.x-Kompatibilität; volle Zusage aktiviert erst mit v1.0. Kein v1.0-Claim.
- [`ADR-0032-skill-security-policy.md`](ADR-0032-skill-security-policy.md) — Skill Security Policy (Accepted, NDF-WP-110): Fail-Closed-Governance für NDF-Skills; keine autonomen Git-/Release-/Netzwerk-/Secret-Aktionen, Human-Maintainer-Gates verbindlich. Operatives Regelwerk: [`../agent-workflows/NDF_SKILL_SECURITY_POLICY.md`](../agent-workflows/NDF_SKILL_SECURITY_POLICY.md). Kein aktives Skill Pack.

## Abgrenzung

- `adr/` – Foundation-/Framework-Kernentscheidungen (0.1-Ära, eingefroren)
- `docs/adr/` – spätere dokumentationsnahe und thematische ADRs (dieser Ordner)

Neue ADRs entstehen hier. Die nächste freie Nummer ergibt sich aus der höchsten vorhandenen ADR-Nummer über beide Ordner hinweg (aktuell: **ADR-0033** wäre die nächste, nachdem ADR-0032 in NDF-WP-110 angenommen wurde).

## Bekannte Nummerierungs-Überschneidung

Die frühen Dateien ADR-0001 bis ADR-0005 in diesem Ordner stammen aus der ersten Aufbauphase und überschneiden sich nummerisch mit den Kern-ADRs unter `adr/`, behandeln aber teils andere Themen. **Entscheidung (NDF-WP-086, `ADR_POLICY.md`):** Sie bleiben dokumentierter Altbestand ohne Massenmigration; künftige Nummern kollidieren nicht mehr, weil neue ADRs die nächste freie Nummer über beide Ordner hinweg nutzen (aktuell ADR-0033).
