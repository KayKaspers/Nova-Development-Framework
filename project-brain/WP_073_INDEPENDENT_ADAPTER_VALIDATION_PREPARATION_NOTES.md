# Project Brain – WP-073 Independent Adapter Validation Preparation Notes

## Ausgangspunkt nach WP-072

Foundation 0.5 scope-locked; WP-073 ist das erste inhaltliche WP (Kern der External-Validation-Hälfte). Adressierte Lücke: Selbstvalidierungs-Bias aus WP-047 (Backlog-Punkt 6, seit 0.3 offen).

## Was vorbereitet wurde

Vollständiges, sofort nutzbares Validierungspaket unter `docs/validation/project-adapter/` — alle Unterlagen DE/EN:

1. `INDEPENDENT_ADAPTER_VALIDATION_PREPARATION.md` — Ziel, Rolle, Umfang, Erfolgskriterien, Übergabe, Ventil-Bezug
2. `INDEPENDENT_ADAPTER_VALIDATION_RUNBOOK.md` — 6 Schritte mit Zeitangaben (Zeitbox 60–120 Min.), Phasen-Prüffragen (minimale Variante 0→1→2→3→8→10, Rest optional), Entscheidungswerte PASS/PASS WITH NOTES/REWORK/FAIL/STOP, Abbruchkriterien; Anker-Effekt-Schutz (WP-047-Lauf erst nach eigenem Urteil ansehen)
3. `INDEPENDENT_VALIDATOR_BRIEF.md` — NDF- und Rollen-Erklärung ohne Vorwissen, Aufgabe, Rückfrage-Regeln (inhaltliche Fragen erst als Finding), Neutralitäts-/Datenschutzregeln
4. `INDEPENDENT_VALIDATION_FEEDBACK_TEMPLATE.md` — Metadaten, neutrale Independence-Beschreibung (keine personenbezogene Pflichtangabe), Phasen-Tabelle, Verständlichkeit/Output/Konventionen/DE-EN, Sicherheit/Neutralität, Blocker, Empfehlungen, Gesamtbewertung
5. `INDEPENDENT_VALIDATION_OUTREACH_TEMPLATE.md` — versandfertige DE+EN-Anfrage mit Platzhaltern (`<independent-reviewer>` etc.) + Format zur neutralen Dokumentation des Versuchs (Ventil-Bedingung 3)
6. `independent-runs/README.md` — Ergebnisort für WP-074 (`<YYYY-MM-DD>-adapter-validation/`), Regeln (keine Fake-Ergebnisse, WP-047-Outputs nie überschreiben, Gate gilt)

## Wie WP-074 jetzt starten kann

Maintainer verschickt Outreach → Validator erhält Brief + Runbook + Feedback-Template (nur Lesezugriff) → Lauf in 60–120 Min. → Feedback zurück → Ablage unter `independent-runs/` → WP-074 wertet aus → Ergebnis fließt in WP-081.

## Vorbereitete Ventil-Bedingungen

Bedingung 1 (WP-073 vollständig) erfüllt; Bedingung 2 (sofort ausführbarer Plan) durch das Runbook erfüllt; Bedingung 3 (dokumentierter Anfrage-Versuch) **ermöglicht, nicht behauptet** — der Versand ist eine spätere Maintainer-Aktion; Bedingungen 4–8 liegen bei WP-081/Maintainer.

## Bewusst nicht durchgeführt

Kein Validierungslauf, keine Fake-Validator-Person, kein Fake-Output, kein Anfrage-Versand, kein leerer Run-Ordner (nur README), keine Release-Vorbereitung.

## Risiken

1. Anfrage-Versuch sollte **zeitnah** nach dem Commit starten — je später, desto wahrscheinlicher endet WP-074 im Ventil statt im echten Lauf.
2. Runbook bewertet Nachvollziehbarkeit per Trockenlauf (keine schriftlichen Phasen-Outputs verlangt) — bewusster Kompromiss zugunsten der 60–120-Min.-Zeitbox; ein tieferer Lauf bleibt für später möglich.

## Nächste empfohlene WP

**NDF-WP-079 – v1.0 Readiness Criteria Draft** (zweite blocking Kern-Hälfte); parallel dazu Maintainer-Aktion: Outreach-Versand + neutrale Dokumentation des Versuchs.
