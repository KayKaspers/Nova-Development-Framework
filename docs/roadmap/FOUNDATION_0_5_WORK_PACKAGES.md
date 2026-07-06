# Foundation 0.5 – Work Package Queue (Draft)

> Status: **Draft aus NDF-WP-071 — kein Scope Lock.** Die Spalte „Einstufung" enthält Kandidaten-Vorschläge; verbindlich wird die Einstufung erst mit NDF-WP-072. / Draft from NDF-WP-071 — not a scope lock; classification becomes binding with NDF-WP-072.

| ID | Titel | Typ | Priorität | Ziel | Abhängigkeiten | Einstufung (Kandidat) | ggf. → 0.6 |
|---|---|---|---|---|---|---|---|
| NDF-WP-071 | Foundation 0.5 Planning | docs-only / roadmap-planning | P1 | Plan, Queue-Draft, Criteria-Draft, Brain-Notes | 0.4 released + WP-070 | **erledigt mit diesem Dokument** | nein |
| NDF-WP-072 | Foundation 0.5 Scope Lock | docs-only / planning-gate | P1 | Umfang einfrieren, WP-074-Downgrade-Ventil festschreiben, Änderungsregeln | WP-071 | **release-blocking candidate** (Gate) | nein |
| NDF-WP-073 | Independent Adapter Validation Preparation | docs-only | P1 | Testleitfaden + neutrales Setup + Erfolgskriterien + Feedback-Format, damit Unbeteiligte ohne Vorwissen validieren können | WP-072 | **release-blocking candidate** (Kern: External Validation, selbstständig erfüllbar) | nein |
| NDF-WP-074 | Independent Adapter Validation Run | review-only | P1 | Tatsächlicher Durchlauf durch eine unbeteiligte Person; Findings dokumentiert | WP-073 | **release-blocking candidate mit Downgrade-Ventil** über WP-081 (falls keine unbeteiligte Person verfügbar → deferred, ehrlich in Release Notes) | ja (nur via Ventil) |
| NDF-WP-075 | Checklist Library DE/EN Priority Pass | docs-only / i18n | P2 | Übrige Checklisten DE/EN-Kern (aus 0.4/WP-061 übernommen) | WP-072 | optional candidate (should-have) | ja |
| NDF-WP-076 | ADR Policy & Structure Consolidation Plan | docs-only / adr-policy | P2 | ADR-Policy entscheiden (Nummernraum, Ablageort, Altbestand) — nur Plan, keine Migration (aus 0.4/WP-063) | WP-072 | optional candidate (should-have) | ja |
| NDF-WP-077 | Academy Band 1 Entry Pass | docs-only / i18n | P2 | Einstiegskapitel DE/EN, von README verlinkt (aus 0.4/WP-062) | WP-072 | optional candidate (should-have) | ja |
| NDF-WP-078 | Public Quality Gate Maintenance Review | review-only + docs-only | P2 | Gate-Nachlauf inkl. Verifikation, dass die CI-Denylist mit gesetztem Secret greift; kleine Härtung nur bei klarem Bedarf (aus 0.4/WP-066) | WP-072 | optional candidate (should-have) | ja |
| NDF-WP-079 | v1.0 Readiness Criteria Draft | docs-only / concept | P1 | Messbare v1.0-Kriterien als Entwurf (kein Commitment, kein Zeitplan, kein v1.0-Claim) | WP-072 | **release-blocking candidate** (Kern: 1.0 Path Hardening) | nein |
| NDF-WP-080 | Docs Export / Website Readiness Concept | docs-only / concept | P3 | Export-/Website-Konzept konkretisieren — kein Build, keine Pipeline (aus 0.3/0.4/WP-065) | alle blocking WPs fertig | **deferred candidate** (nur bei Restkapazität) | ja |
| NDF-WP-081 | Foundation 0.5 Release Readiness Review | review-only | Release | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.5-Kriterien; entscheidet über das WP-074-Ventil | 073, 079 done; 074 done oder Ventil | **release-blocking candidate** | nein |
| NDF-WP-082 | Foundation 0.5 Release Prep | docs-only / release-prep | Release | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide für `v0.5.0-foundation` | WP-081 | **release-blocking candidate** | nein |

## Reihenfolge / Order (Vorschlag / proposed)

```text
071 (Planning — dieses Dokument)
→ 072 (Scope Lock)
→ 073 (Validation Preparation) ‖ 079 (v1.0 Criteria Draft)     [Kern beider Titel-Hälften]
→ 074 (Validation Run — sobald unbeteiligte Person verfügbar)
→ 075 / 076 / 077 / 078 (optional, beliebige Reihenfolge)
→ 080 (deferred, nur bei Restkapazität)
→ 081 → 082 (Release-Strecke)
```

## Regeln / Rules

- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Kein inhaltliches WP startet vor abgeschlossenem Scope Lock (NDF-WP-072).
- Diese Queue ist ein **Draft**: Einstufungen sind Kandidaten, keine Zusagen. Verbindlichkeit, Downgrade-Ventil-Formulierung und Änderungsregeln kommen aus NDF-WP-072.
- Der blocking Kern bleibt klein: je ein inhaltliches Kern-Deliverable pro Titel-Hälfte (External Validation → 073/074, 1.0 Path Hardening → 079) plus Gates und Release-Strecke.
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv.
