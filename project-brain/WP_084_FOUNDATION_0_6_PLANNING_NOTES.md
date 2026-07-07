# Project Brain – WP-084 Foundation 0.6 Planning Notes

## Ausgangslage nach Foundation 0.5

`v0.5.0-foundation` released und nachbereitet (WP-083), keine offenen Follow-ups; 0.5-Einstiegspunkte sauber (geprüft: kein „tag pending"/„prepared" mehr, v1.0 nirgends behauptet). Die 0.6-Kandidaten aus WP-083 waren vollständig und klar.

## Warum 0.6 nötig ist

0.5 hat offene Punkte sichtbar und messbar gemacht (v1.0-Draft mit 8 `not met`-Einträgen, Known Limitations, ADR-Dauerläufer mit verbindlicher Regel). Ohne 0.6 blieben sie Beobachtungen — 0.6 macht daraus Entscheidungen und Nachweise.

## Leitidee

**Adoption Confidence & Governance Hardening** (Nova-Vorschlag übernommen; kritisch geprüft: beide Hälften haben je ein klares Kern-Deliverable — Governance → ADR-Entscheidung, Adoption Confidence → öffentlicher Fixture-Lauf — das bewährte Muster aus 0.4/0.5).

## Übernommene Kandidaten aus WP-083

Alle sechs vollständig übernommen: ADR-Entscheidung, öffentlicher Runbook-Lauf, Checklist/i18n, Gate Maintenance inkl. CI-Denylist-Proof, Academy Entry, v1.x-Kompatibilitäts-Policy-Draft.

## Vorgeschlagene WP-Liste (Kandidaten, nicht gelockt)

084 Planning (done) · 085 Scope Lock · 086 ADR Decision · 087 Validation Prep (falls nötig) · 088 Public Validation Run · 089 Gate Maintenance · 090 CI Denylist Proof (entfällt ggf. in 089) · 091 Checklist DE/EN · 092 Academy · 093 v1.x Policy Draft · 094 Readiness · 095 Release Prep.

## Vorgeschlagene Blocking-Kandidaten (nicht final)

085, 086, 088, 089, 094, 095 — Nova-Empfehlung übernommen. Begründung: kleiner Kern nach 0.4/0.5-Muster (Gates + je ein Deliverable pro Leitideen-Hälfte + leichter Gate-Nachlauf). 087/090–093 optional; Website/i18n-Vollausbau/ADR-Migration/v1.0-RC deferred. **Final entscheidet WP-085.**

## Risiken

ADR-Wiederholungsschleife (→ Sonderregel greift, „streichen" erlaubt, „später" nicht); Personenabhängigkeit von WP-088 (→ Ventil-Prüfung in WP-085, Empfehlung: 0.5-Muster); Scope Creep bei 12 Kandidaten (→ kleiner blocking Kern); v1.x-Draft als Zusage lesbar (→ Draft-Markierung).

## Nicht-Ziele

Kein v1.0/RC, kein Rewrite, keine Website/CLI, keine volle i18n, keine ADR-Massenmigration, keine 0.6-Release-Zusage.

## Nächste WP

**NDF-WP-085 – Foundation 0.6 Scope Lock.**

## Bewusst nicht entschieden

Blocking-Einstufung (nur Empfehlung), WP-088-Ventil-Formulierung, WP-090-Eigenständigkeit, Priorisierung der optionalen WPs, Zieldatum — alles WP-085 bzw. später.
