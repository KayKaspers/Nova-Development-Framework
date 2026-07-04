# Project Brain – WP-058 Foundation 0.4 Scope Lock Notes

## Entscheidung

Der Foundation-0.4-Scope ist eingefroren (`docs/roadmap/FOUNDATION_0_4_SCOPE_LOCK.md`, 2026-07-04). Leitidee bestätigt: **Adoption Hardening & Public Usability** — der Titel hat zwei Hälften, der blocking Kern gibt jeder Hälfte genau ein Deliverable.

## Release-blocking (5 WPs)

058 Scope Lock (mit diesem WP abgeschlossen) · 059 Adapter Conventions Polish (Adoption Hardening, an WP-047-Findings gebunden) · 060 Prompt DE/EN Priority Pass (Public Usability, eng gefasst) · 067 Readiness · 068 Prep.

## Kritische Bewertung (Aufgabe 1/3)

Der WP-057-Draft-Kern wurde bestätigt, nicht erweitert (kein Scope Creep). WP-060 blieb bewusst blocking, weil „Public Usability" die halbe Titel-Idee ist und die Prompt-Bibliothek das meistgenutzte öffentliche Artefakt ist — aber **eng gefasst** als „Priority Pass" (meistgenutzte Prompts, nicht die gesamte Bibliothek) und mit **Downgrade-Ventil**: WP-067 kann WP-060 mit Begründung auf optional herabstufen, wenn der Reststand ehrlich dokumentiert wird. So hängt der Release nicht an i18n-Vollständigkeit. WP-066 (Gate Maintenance) blieb optional; WP-064/065 deferred.

## Optional (should-have)

061 Checklist DE/EN · 062 Academy Entry · 063 ADR Policy Plan · 066 Gate Maintenance — unfertig ⇒ Known Limitation in Release Notes + Matrix, dann nach 0.5.

## Deferred

064 Independent Adapter Run (nur wenn Unbeteiligte verfügbar) · 065 Docs Export/Website (aus 0.3 übernommen). Blockieren nie.

## Out of Scope

Kein v1.0, keine Voll-Übersetzung, keine Voll-Academy, keine Website, keine Export-Pipeline, keine CLI, kein History-Rewrite, keine privaten Beispiele, keine ADR-Massenmigration ohne Policy, keine neuen Großkonzepte, keine neuen produktiven Beispiel-Apps, keine Release-Automation.

## Änderungsregeln

Neue blocking WPs nur mit Nova-(ChatGPT)-Review + Maintainer-Freigabe + Scope-Lock-Update; optionale nie stillschweigend zu blocking; Herabstufung nur über WP-067; alles im Project Brain protokolliert.

## Risiken

1. WP-060-Umfang könnte knapp werden → Downgrade-Ventil greift.
2. Versuchung, i18n-Optionale doch zu blocking zu machen → Änderungsregeln verhindern stilles Aufweichen.

## Nächstes empfohlenes WP

NDF-WP-059 – Adapter Conventions Polish (parallel möglich: NDF-WP-060).
