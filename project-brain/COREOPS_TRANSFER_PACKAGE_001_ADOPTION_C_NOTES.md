# CoreOps Transfer Package 001 – Adoption C (Notes)

## Kandidaten

`NDF-FC-COREOPS-005` (Accepted Product Direction without technical fixation), `NDF-FC-COREOPS-006` (Multi-dimensional status models), `NDF-FC-COREOPS-007` (Framework tailoring before adoption). Adoption C (`NDF-ADOPT-COREOPS-001C`, docs-only / governance-guidance). Alle drei als **optionale, projektneutrale Guidance** übernommen.

## Accepted-Product-Direction-Muster (005)

Neue Guidance trennt Decision Class / Lifecycle Status / Binding Level; eine akzeptierte Produkt-/Governance-Richtung akzeptiert **keine** Architektur/Technologie/Implementierung/Release; technische Umsetzung braucht eigene spätere Architektur-/ADR-/WP-Entscheidung + Human-Maintainer-Freigabe.

## Optionales mehrdimensionales Statusmodell (006)

Additiv in `docs/project-system/CAPABILITY_MATRIX_SPEC.md`: Roadmap/Implementation/Support/optional Evidence getrennt; Einzelstatus bleibt zulässig/Default; Support benötigt Evidenz; **keine universelle NDF-Core-Pflicht**, keine CoreOps-Werte als globale Pflicht, keine Ableitung von Support aus Roadmap/Implementierung.

## Framework-Tailoring-Guidance (007)

Neue Guidance: Applicability Review, mandatory-vs-optional, projektneutrale Konflikthierarchie (Recht → Human-Maintainer → Security/Safety-Invarianten → akzeptierte ADRs/Scope-Locks → normative NDF-Regeln → projektspezifische Governance → getailorte Framework-Guidance → Advisory), Tailoring-Ergebniswerte, Framework-Overload-Grenzen, optionale Profile, keine Compliance-/Zertifizierungsbehauptung durch Terminologie, Human-Maintainer-Gate. Abgegrenzt vom NDF-zu-Projekt-Project-Adapter.

## Keine universelle neue Core-Pflicht

Alle drei Muster sind optional; einfache Projekte werden nicht belastet; bestehende Matrix-/Decision-Modelle bleiben gültig.

## Pfadkorrektur

Capability Matrix Spec am tatsächlichen Pfad `docs/project-system/CAPABILITY_MATRIX_SPEC.md` additiv erweitert; **keine** Datei unter `framework/standards/CAPABILITY_MATRIX_SPEC.md` erstellt; nichts verschoben/umbenannt. Vorheriger `blocked-path-mismatch` resolved.

## Status

- NDF-Version noch nicht zugeordnet.
- Nova Review pending.
- Human-Maintainer-Commit pending.
- CoreOps-Rückverlinkung noch ausstehend (separates Traceability-WP).

## Alle sieben Kandidaten fachlich behandelt

001/003/004 → Adoption A (`1ebffa6`); 002 → Adoption B (`e894c6f`); 005/006/007 → Adoption C. Adoption A/B unverändert.

## Kompatibilität / Governance

Additiv, guidance-orientiert, rückwärtskompatibel; keine technische Ableitung aus Produktentscheidung; keine vollständige Framework-Pflicht; keine ADR-Hierarchie überschrieben; keine Compliance-/Zertifizierungsaussage; keine neue NDF-Version; ADR-0031/0032 unberührt. Breaking-Change-Potenzial: low.

## Nächster NDF-Schritt nach Review

Nach Nova-Review + Human-Maintainer-Entscheidung/-Commit: separates **CoreOps-Traceability-WP** zur Rückverlinkung aller tatsächlich adoptierten Kandidaten. Kein weiteres Adoption-WP in diesem Lauf begonnen.
