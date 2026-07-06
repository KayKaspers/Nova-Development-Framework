# Project Brain – WP-072 Foundation 0.5 Scope Lock Notes

## Ausgangslage nach WP-071

Foundation 0.5 war geplant (Zielbild External Validation & 1.0 Path Hardening), Queue und Criteria lagen als Draft vor. Keine Statusfehler in den 0.5-/0.4-Dokumenten gefunden (0.5 nirgends als released, v1.0 nirgends als erreicht).

## Kritische Bewertung des Drafts

Der Draft hält stand: nicht zu groß (blocking Kern = 2 inhaltliche Deliverables + 3 Gates), realistisch (073 selbstständig erfüllbar, 079 reine Doku-Arbeit), kein Scope Creep (alle 0.4-Reste optional/deferred statt automatisch übernommen). Einstufung unverändert übernommen; Präzisierung nur beim WP-074-Ventil und der WP-076-Sonderregel.

## Finaler Scope (verbindlich)

- **Release-blocking:** 072 (Gate, done), 073 (Validation Prep), 074 (Validation Run, mit Ventil), 079 (v1.0 Criteria Draft), 081 (Readiness, entscheidet Ventil), 082 (Release Prep).
- **Optional:** 075 (Checklist DE/EN), 076 (ADR Policy Plan — Sonderregel: bei erneutem Nichterledigen in 0.6 verbindlich priorisieren oder ehrlich streichen; drittes stilles Verschieben unzulässig), 077 (Academy Entry), 078 (Gate Maintenance, inkl. Verifikation der scharfen CI-Denylist).
- **Deferred:** 080 (Docs Export/Website Concept) + i18n-Rest, Security-Prompt-Vollübersetzung, ADR-Massenmigration, v1.0-Release selbst.

## WP-074-Entscheidung und Downgrade-Ventil

WP-074 bleibt **release-blocking** — External Validation ist der Kern der Titel-Hälfte und darf nicht von vornherein weich sein. Gegen die Personenabhängigkeit: präzises 8-Bedingungen-Ventil über WP-081 (Nova-Vorschlag übernommen und verschärft): (1) 073 vollständig, (2) sofort ausführbarer Plan, (3) mindestens ein dokumentierter realistischer Anfrage-Versuch (neutraler Kanal/Rolle, kein privater Name), (4) niemand im vertretbaren Zeitfenster verfügbar, (5) explizite Begründung in WP-081, (6) Known Limitation in den Release Notes, (7) kein v1.0-Claim **und** unabhängige Validierung bleibt offenes v1.0-Kriterium in WP-079 (verhindert Dauerausweg), (8) Maintainer-Bestätigung im Go/No-Go. Ventil gilt nur für 074.

## WP-079-Entscheidung und v1.0-Abgrenzung

WP-079 bleibt release-blocking: Ohne Messlatte ist „1.0 Path Hardening" leer. Dreifache Abgrenzung gegen v1.0-Missverständnis: überall Draft-Markierung, Invariante „kein v1.0-Claim — auch nicht implizit" in den Criteria, kein v1.0 Release Candidate als Nicht-Ziel im Scope Lock.

## Risiken

Ventil zu früh gezogen (→ Bedingungen 2–4 verlangen echten dokumentierten Versuch), v1.0-Missverständnis (→ dreifache Abgrenzung), WP-076-Dauerschleife (→ Sonderregel), Ein-Personen-Engpass (unverändert).

## Empfehlung an Nova

Scope Lock committen; danach WP-073 als nächstes inhaltliches WP (parallel/danach WP-079). Beim späteren WP-081 die Ventil-Bedingungen wörtlich gegen das Scope-Lock-Dokument prüfen.

## Nächster Schritt

**NDF-WP-073 – Independent Adapter Validation Preparation.**
