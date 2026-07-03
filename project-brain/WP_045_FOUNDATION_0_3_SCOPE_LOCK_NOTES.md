# Project Brain – WP-045 Foundation 0.3 Scope Lock Notes

## Entscheidung

Der Foundation-0.3-Scope ist eingefroren (`docs/roadmap/FOUNDATION_0_3_SCOPE_LOCK.md`, 2026-07-03). Leitidee bestätigt: **Adoption Release** — der einzige Release-Kernbeweis ist die praktische Übernehmbarkeit am neutralen Beispielprojekt.

## Release-blocking (6 WPs)

045 Scope Lock (mit diesem WP abgeschlossen) · 046 Neutral Example Project v0.2 · 047 Adapter Practical Validation · 052 Public Quality Gate v0.2 · 054 Readiness Review · 055 Release Prep

## Optional (should-have, nicht blockierend)

048 Prompt-Full-Pass · 049 Checklist-Full-Pass · 050 Academy-Entry-Pass · 051 ADR Consolidation Plan — unfertig ⇒ bekannte Einschränkung in Release Notes + Translation-Matrix, dann nach 0.3.

## Out of Scope / Herabstufung

Kein v1.0, keine volle Academy-Übersetzung, keine Website, keine CLI, keine Export-Pipeline, kein History-Rewrite, keine privaten Beispiele, keine ADR-Massenmigration ohne Policy, keine neuen Großkonzepte ohne Scope-Review. **WP-053 von „optional" auf „deferred candidate" herabgestuft** (strenger als der WP-044-Draft): startet nur bei Restkapazität nach allen blocking WPs, sonst 0.4.

## Änderungsregeln

Neue blocking WPs nur mit Nova-(ChatGPT)-Review + Maintainer-Freigabe + Scope-Lock-Update; optionale WPs nie stillschweigend zu blocking; Herabstufung blocking→optional nur über WP-054 mit Begründung; jede Änderung wird hier im Project Brain protokolliert. WP-047-Findings sind nur blocking, wenn sie den Adoptionsbeweis selbst betreffen.

## Risiken

1. WP-047 könnte größere Adapter-Lücken aufdecken → dann greift die Findings-Regel (kleine blocking Folge-WPs nur für den Adoptionsbeweis).
2. Versuchung, i18n-Pässe doch zu blocking zu machen → Änderungsregeln verhindern stilles Aufweichen.

## Nächstes empfohlenes WP

NDF-WP-046 – Neutral Example Project v0.2 (parallel möglich: NDF-WP-052).
