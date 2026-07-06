# Project Brain – WP-071 Foundation 0.5 Planning Notes

## Ausgangslage nach Foundation 0.4

`v0.4.0-foundation` released (2026-07-04), Post-Release-Cleanup (WP-069) und Manual Follow-up Closure (WP-070) abgeschlossen — keine offenen Maintenance-Punkte. 0.4-Statusdokumente sauber (geprüft in WP-071: keine falschen „tag pending"/„prepared"-Stellen in aktuellen Einstiegspunkten).

## Bewertete offene Themen

| Thema (aus 0.4) | Bewertung für 0.5 |
|---|---|
| WP-064 Independent Adapter Validation | **Kern von 0.5** — aufgeteilt in Preparation (WP-073, selbstständig erfüllbar) und Run (WP-074, personenabhängig, mit Ventil) |
| v1.0-Kriterien nicht formalisiert | **Kern von 0.5** — WP-079 als Draft (Messlatte, kein Zeitplan) |
| WP-061 Checklist DE/EN | optional übernommen als WP-075 |
| WP-063 ADR Policy Plan | optional übernommen als WP-076 (dritte Runde — falls in 0.5 wieder unerledigt, für 0.6 Priorisierung oder ehrliches Streichen erwägen) |
| WP-062 Academy Entry | optional übernommen als WP-077 |
| WP-066 Gate Maintenance | optional übernommen als WP-078; sinnvoller Prüfpunkt: verifizieren, dass die CI-Denylist mit dem jetzt gesetzten Secret tatsächlich greift |
| WP-065 Docs Export / Website | deferred übernommen als WP-080 |
| i18n-Rest / Security-Prompts | kein eigenes WP — bleibt priorisierte Restarbeit, ehrlich in der Matrix |

## Vorgeschlagener Fokus

Zielbild **External Validation & 1.0 Path Hardening** übernommen (kritisch geprüft: External Validation ist jetzt der richtige nächste Schritt, weil der Selbstvalidierungs-Bias die einzige strukturelle — nicht bloß inhaltliche — Lücke des Adoptionsbeweises ist; 1.0 Path Hardening ist nicht zu früh, solange es Entwurf bleibt, denn ohne Messlatte lässt sich „kein v1.0" nicht ehrlich steuern). Blocking Kern klein: je ein Kern-Deliverable pro Titel-Hälfte plus Gates.

## Vorgeschlagene WP-Queue

WP-071 (done) → 072 Scope Lock → 073 Validation Prep ‖ 079 v1.0 Criteria Draft → 074 Validation Run → 075–078 optional → 080 deferred → 081 Readiness → 082 Release Prep. Details: `docs/roadmap/FOUNDATION_0_5_WORK_PACKAGES.md` (Draft, kein Scope Lock).

## Bewusst nicht Teil dieses WPs

Kein Scope Lock (erst WP-072), keine Release Notes, kein Tag/Release, keine Umsetzung von 0.5-WPs, keine CI-Änderung, keine v1.0-Behauptung.

## Risiken

Personenabhängigkeit von WP-074 (→ Ventil über WP-081 im Scope Lock festschreiben), v1.0-Missverständnis (→ Draft-Markierung überall), Scope Creep durch 0.4-Reste (→ optional halten).

## Empfehlung an Nova

Planung committen, dann **NDF-WP-072 – Foundation 0.5 Scope Lock** als nächstes WP. Im Scope Lock besonders: exakte Ventil-Formulierung für WP-074 und Änderungsregeln.
