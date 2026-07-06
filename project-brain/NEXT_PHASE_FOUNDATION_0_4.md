# Project Brain – Next Phase Foundation 0.4

> **Status-Update (WP-069):** Foundation 0.4 ist als `v0.4.0-foundation` veröffentlicht (2026-07-04). Nächste Phase — Vorschlag, nicht verbindlich: Foundation 0.5 Planning bzw. Post-Release Maintenance (offene optionale WPs 061–063/066, deferred 064/065). Kein 0.5-Scope festgelegt; kein v1.0.

## Warum Foundation 0.4?

Foundation 0.3 hat NDF als übernehmbar bewiesen. 0.4 härtet diese Übernehmbarkeit: die konkreten Adapter-Konventionslücken aus der WP-047-Validierung schließen und die größte öffentliche i18n-Lücke (Prompts) reduzieren. Arbeitstitel: **Adoption Hardening & Public Usability**.

## Hauptziel

Ein externer Nutzer stolpert beim Adapter nicht mehr über Format-/Pfad-/Präfix-Unklarheiten, und die zentralen öffentlichen Werkzeuge sind zunehmend DE/EN nutzbar — ohne neue Großkonzepte, ohne v1.0.

## Wichtigste Risiken

1. Scope-Wachstum → Gegenmittel: Scope Lock (NDF-WP-058) zuerst; P2/P3 blockieren nicht.
2. i18n-Pflegekosten → priorisierte Umstellung statt Fläche.
3. „Adoption Hardening" zu unscharf → jede P1-Verbesserung an ein WP-047-Finding gebunden.

## Empfohlene Reihenfolge

1. NDF-WP-058 Scope Lock
2. NDF-WP-059 Adapter Conventions Polish ‖ NDF-WP-060 Prompt DE/EN (Kern-Hardening)
3. P2: 061/062/063/066
4. deferred: 064/065
5. NDF-WP-067 Readiness → NDF-WP-068 Release Prep → `v0.4.0-foundation`

## Was bewusst nicht sofort gebaut wird

Keine Website, keine Export-Pipeline, keine CLI, keine ADR-Massenmigration, keine vollständige Academy-Übersetzung. Alles davon bleibt Konzept/Plan oder späteres Release.

## Entscheidung

**Keine neuen großen Inhalte vor dem Scope Lock.** Details: `docs/roadmap/FOUNDATION_0_4_PLAN.md`, `docs/roadmap/FOUNDATION_0_4_WORK_PACKAGES.md`

**Update (WP-058):** Scope Lock ist beschlossen — Release-blocking sind nur 058, 059, 060, 067, 068; 061–063 und 066 optional; 064/065 deferred. WP-060 ist eng gefasst und über WP-067 herabstufbar. Verbindlich: `docs/roadmap/FOUNDATION_0_4_SCOPE_LOCK.md`

## Manuelle Maintenance-Punkte (kein Framework-WP)

Geschlossen (NDF-WP-070) — manual follow-ups from Foundation 0.4 post-release cleanup are closed:

1. Custom neutrality denylist secret (`NDF_PUBLIC_NEUTRALITY_DENYLIST`): verified.
2. Älterer Foundation-0.2-GitHub-Release-Titel: verified correct.
