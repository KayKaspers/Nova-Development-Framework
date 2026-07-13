# Capability Matrix Specification

## Zweck

Die Capability Matrix beschreibt, welche Fähigkeiten ein Projekt besitzt.

## Statuswerte

- not_planned
- planned
- in_progress
- implemented
- verified
- deprecated

## Beispiel

| Capability | Status | Notes |
|---|---|---|
| Docker | verified | Build-Gate vorhanden |
| CI/CD | implemented | GitHub Actions aktiv |
| Preflight | implemented | Preflight 2.0 |
| Multi Language | planned | DE/EN vorgesehen |
| Health Score | not_planned | später |

## Nutzen

Die Matrix ermöglicht:

- Projektvergleich
- Roadmap-Planung
- Health Score
- passende Prompt-Auswahl
- passende Templates

## Optionales mehrdimensionales Statusmodell (additiv)

Das oben beschriebene **Einzelstatusmodell bleibt weiterhin zulässig** und ist der Standard. Ergänzend kann ein Projekt bei Bedarf ein **optionales mehrdimensionales Statusmodell** verwenden, wenn eine Capability gleichzeitig unabhängige Zustände besitzt. Siehe auch die [Decision and Status Modeling Guidance](../governance/NDF_DECISION_AND_STATUS_MODELING_GUIDANCE.md).

Beispielhafte, voneinander getrennte Dimensionen:

```text
Roadmap Status
Implementation Status
Support Status
Evidence or Validation Status   (optional)
```

Beispielzeile:

| Capability | Roadmap Status | Implementation Status | Support Status | Evidence Status |
|---|---|---|---|---|
| Beispiel-Capability | planned | not-implemented | not-supported | not-assessed |

Trennungsregeln:

- Roadmap inclusion does not imply implementation.
- Implementation does not imply supported status.
- Vendor or protocol mention does not imply support.
- **Support requires defined evidence.**

### Wann Einzelstatus, wann mehrdimensional

- **Einzelstatus beibehalten**, wenn keine unabhängigen Statusdimensionen benötigt werden, keine Missverständnisse entstehen und kein separater Support-/Evidenzstatus erforderlich ist.
- **Mehrdimensional verwenden**, wenn Roadmap, Implementierung und Support unabhängig fortschreiten, Reife/Evidenz separat bewertet wird oder ein Einzelstatus falsche Schlussfolgerungen erzeugen würde.

### Keine universelle Pflicht

Multi-dimensional status modeling is optional guidance, not a mandatory requirement for every NDF project or every project matrix. Bestehende Einzelstatus-Matrizen bleiben gültig; kein Projekt wird zu mehreren Statusdimensionen gezwungen; es werden keine projektspezifischen Werte als verpflichtende NDF-Werte übernommen; Support wird nicht allein aus Roadmap- oder Implementierungsstatus abgeleitet.
