# Project Brain – Next Phase Foundation 0.3

## Warum Foundation 0.3?

Foundation 0.2 hat NDF öffentlich sauber gemacht (Neutralität, Quality Gate, DE/EN-Einstieg). Foundation 0.3 muss beweisen, dass NDF **praktisch übernehmbar** ist: Adapter validieren, Beispielprojekt ausbauen, Werkzeuge durchgängig DE/EN, ADR-Policy klären.

## Hauptziel

Ein externer Nutzer kann NDF ohne interne Vorkenntnisse in einem echten Projekt anwenden (Flow: README → Adapter-Guide → Beispielprojekt).

## Wichtigste Risiken

1. Scope-Wachstum wie in 0.2 → Gegenmittel: Scope Lock (NDF-WP-045) vor allem anderen.
2. Adapter-Praxistest deckt Lücken auf → erwünscht, Puffer für Folge-WPs einplanen.
3. i18n-Pflegekosten → priorisierte Umstellung statt Fläche.

## Empfohlene Reihenfolge

1. NDF-WP-045 Scope Lock
2. NDF-WP-046 Neutral Example Project v0.2 → NDF-WP-047 Adapter Practical Validation (Kernbeweis)
3. NDF-WP-052 Quality Gate v0.2 (parallel möglich)
4. P2: 048/049/050/051 (i18n-Pässe, Academy-Einstieg, ADR-Plan)
5. NDF-WP-054 Readiness → NDF-WP-055 Release Prep → `v0.3.0-foundation`

## Entscheidung

**Keine neuen großen Features vor dem Scope Lock.** Details: `docs/roadmap/FOUNDATION_0_3_PLAN.md` und `docs/roadmap/FOUNDATION_0_3_WORK_PACKAGES.md`

**Update (WP-045):** Scope Lock ist beschlossen — Release-blocking sind nur 045–047, 052, 054, 055; 048–051 optional; 053 deferred candidate. Verbindlich: `docs/roadmap/FOUNDATION_0_3_SCOPE_LOCK.md`
