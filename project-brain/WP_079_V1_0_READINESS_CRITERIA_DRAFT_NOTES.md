# Project Brain – WP-079 v1.0 Readiness Criteria Draft Notes

## Ausgangspunkt nach WP-072/WP-073

Scope locked; External-Validation-Hälfte vorbereitet (WP-073, Lauf WP-074 offen). WP-079 ist das Kern-Deliverable der zweiten Titel-Hälfte „1.0 Path Hardening".

## Warum release-blocking

Ohne Messlatte bleibt „kein v1.0" reine Abgrenzung: Fortschritt Richtung v1.0 wäre nicht messbar, eine spätere Entscheidung Bauchgefühl. Der Draft macht die Entscheidung überprüfbar, bevor sie ansteht — das ist der 0.5-Beitrag, nicht v1.0 selbst.

## Definierte Kriterienbereiche

Alle 12 vorgeschlagenen Kategorien übernommen (kritisch geprüft: keine zusammenlegbar ohne Informationsverlust, keine fehlt). Jede Kategorie als prüfbare Tabelle (Kriterium / Für v1.0? / Stand / Nachweis / Hinweise) mit ehrlichen Statuswerten. Wichtige Design-Entscheidungen:

- **blocking vs. tracked** statt alles-blocking: tracked-Punkte (z. B. Academy-Einstieg, Checklisten-DE/EN) müssen ehrlich dokumentiert sein, blockieren aber nicht.
- **Ehrlicher Ist-Stand:** met (7 Kategorien ganz oder überwiegend), partially met (Usability, Adapter, Doku, Prompts), **not met** klar benannt: unabhängiger Lauf, ADR-Policy-Entscheidung, v1.x-Kompatibilitätszusage.
- **Vollübersetzung explizit NICHT v1.0-erforderlich** (ehrliche Matrix genügt) — verhindert Wunschlisten-Inflation.
- **Neue bewusste Lücke benannt:** v1.x-Versionierungs-/Kompatibilitätszusage fehlt und gehört in den v1.0 Scope Lock.
- **Offene Fragen** dokumentiert (1 Lauf oder je Sprache? Kompatibilitätsumfang? zweiter Fixture-Typ? Zweitmeinung im Go/No-Go?).

## External Validation im Draft

Kategorie 2: „mindestens ein unabhängiger Lauf durchgeführt und ausgewertet" ist **v1.0-blocking** und trägt den expliziten Vermerk, dass das Kriterium auch bei einem WP-074-Ventil-Downgrade in 0.5 bestehen bleibt (Umsetzung der Ventil-Bedingung 7 aus dem Scope Lock). WP-074 wird nirgends als durchgeführt dargestellt.

## v1.0-Claim-Verhinderung

Mehrfach abgesichert: Status-Sektion („Draft. NDF ist nicht v1.0… kein Release Candidate"), eigene „Was dieser Draft nicht ist"-Sektion, Path Summary mit denselben Klarstellungen, README-Zusatz „(v1.0 ist nicht erreicht)", Criteria-Haken mit „bedeutet nicht v1.0-Readiness".

## Neue/geänderte Dateien

Neu: `docs/release/V1_0_READINESS_CRITERIA_DRAFT.md`, `docs/roadmap/V1_0_PATH_SUMMARY.md`, diese Note. Geändert: 0.5-Criteria (WP-079 abgehakt + Links), 0.5-Queue + Plan (WP-079 umgesetzt + Links), NEXT_PHASE (Kern-WPs erledigt, nächster Schritt), CHANGELOG (WP-079-Zeile), README (v1.0-Pfad-Link DE/EN mit Nicht-erreicht-Klarstellung).

## Bewusst nicht getan

Kein v1.0 Scope Lock, kein Release Candidate, keine Termine, keine WP-074-Durchführung, keine 0.5-Release-Vorbereitung, keine Änderung der Ventil-Regeln, keine Validierungsdokument-Änderungen (WP-073-Unterlagen verweisen bereits korrekt; ein zusätzlicher Rück-Link hätte keinen Mehrwert).

## Risiken

1. Draft könnte trotz Markierungen als Ankündigung gelesen werden → Klarstellungen an allen Einstiegspunkten platziert.
2. Statuswerte veralten → gehören bei jedem Release-Readiness-Review (ab WP-081) stichprobenhaft geprüft.
3. Zu harte Kriterien könnten v1.0 dauerhaft blockieren → Nicht-Ziele-Sektion begrenzt bewusst; offene Fragen ans v1.0 Scope Lock delegiert.

## Nächste empfohlene WP

Maintainer-Aktion: Outreach-Versand (Ventil-Bedingung 3). Dann **NDF-WP-074** (Lauf, sobald Validator verfügbar) oder optionale WPs 075–078; Release-Strecke WP-081 → WP-082 danach.
