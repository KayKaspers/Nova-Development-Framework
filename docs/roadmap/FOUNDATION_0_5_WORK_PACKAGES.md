# Foundation 0.5 – Work Package Queue

> Status: **Scope locked** (NDF-WP-072, 2026-07-06). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_5_SCOPE_LOCK.md](FOUNDATION_0_5_SCOPE_LOCK.md). / Scope locked; binding classification in the "Scope Lock" column.

| ID | Titel | Typ | Priorität | Ziel | Abhängigkeiten | Scope Lock | ggf. → 0.6 |
|---|---|---|---|---|---|---|---|
| NDF-WP-071 | Foundation 0.5 Planning | docs-only / roadmap-planning | P1 | Plan, Queue-Draft, Criteria-Draft, Brain-Notes | 0.4 released + WP-070 | **erledigt** (Planung, 2026-07-06) | nein |
| NDF-WP-072 | Foundation 0.5 Scope Lock | docs-only / planning-gate | P1 | Umfang einfrieren, WP-074-Downgrade-Ventil festschreiben, Änderungsregeln | WP-071 | **release-blocking** (Gate — abgeschlossen mit dem Scope-Lock-Dokument, NDF-WP-072) | nein |
| NDF-WP-073 | Independent Adapter Validation Preparation | docs-only | P1 | Testleitfaden + neutrales Setup + Erfolgskriterien + Feedback-Format, damit Unbeteiligte ohne Vorwissen validieren können | WP-072 | **release-blocking** (Kern: External Validation) — umgesetzt in WP-073: Preparation, Runbook, Validator Brief, Feedback- + Outreach-Template (`docs/validation/project-adapter/`) | nein |
| NDF-WP-074 | Independent Adapter Validation Run | review-only | P1 | Tatsächlicher Durchlauf durch eine unbeteiligte Person; Findings dokumentiert | WP-073 | **release-blocking** — durchgeführt in WP-074: neutralisierter unabhängiger Review, privater Referenzkontext, **PASS WITH NOTES** ([independent-runs/2026-07-06](../validation/project-adapter/independent-runs/2026-07-06-private-reference-validation/README.md)); Ventil nicht benötigt | nein |
| NDF-WP-075 | Checklist Library DE/EN Priority Pass | docs-only / i18n | P2 | Übrige Checklisten DE/EN-Kern (aus 0.4/WP-061 übernommen) | WP-072 | optional (should-have) | ja |
| NDF-WP-076 | ADR Policy & Structure Consolidation Plan | docs-only / adr-policy | P2 | ADR-Policy entscheiden (Nummernraum, Ablageort, Altbestand) — nur Plan, keine Migration (aus 0.4/WP-063) | WP-072 | optional (should-have) — Sonderregel: bei erneutem Nichterledigen in 0.6 priorisieren oder streichen (Scope Lock) | ja |
| NDF-WP-077 | Academy Band 1 Entry Pass | docs-only / i18n | P2 | Einstiegskapitel DE/EN, von README verlinkt (aus 0.4/WP-062) | WP-072 | optional (should-have) | ja |
| NDF-WP-078 | Public Quality Gate Maintenance Review | review-only + docs-only | P2 | Gate-Nachlauf inkl. Verifikation, dass die CI-Denylist mit gesetztem Secret greift; kleine Härtung nur bei klarem Bedarf (aus 0.4/WP-066) | WP-072 | optional (should-have) | ja |
| NDF-WP-079 | v1.0 Readiness Criteria Draft | docs-only / concept | P1 | Messbare v1.0-Kriterien als Entwurf (kein Commitment, kein Zeitplan, kein v1.0-Claim) | WP-072 | **release-blocking** (Kern: 1.0 Path Hardening) — umgesetzt in WP-079: [`V1_0_READINESS_CRITERIA_DRAFT.md`](../release/V1_0_READINESS_CRITERIA_DRAFT.md) + [`V1_0_PATH_SUMMARY.md`](V1_0_PATH_SUMMARY.md); nur Entwurf, kein v1.0-Claim | nein |
| NDF-WP-080 | Docs Export / Website Readiness Concept | docs-only / concept | P3 | Export-/Website-Konzept konkretisieren — kein Build, keine Pipeline (aus 0.3/0.4/WP-065) | alle blocking WPs fertig | **deferred** (nur bei Restkapazität) | ja |
| NDF-WP-081 | Foundation 0.5 Release Readiness Review | review-only | Release | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.5-Kriterien; entscheidet über das WP-074-Ventil | 073, 079 done; 074 done oder Ventil | **release-blocking** — durchgeführt in WP-081: **GO WITH NOTES** ([`FOUNDATION_0_5_RELEASE_READINESS_REVIEW.md`](../release/FOUNDATION_0_5_RELEASE_READINESS_REVIEW.md)); Ventil-Prüfung entfiel (WP-074 done) | nein |
| NDF-WP-082 | Foundation 0.5 Release Prep | docs-only / release-prep | Release | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide für `v0.5.0-foundation` | WP-081 | **release-blocking** | nein |

## Reihenfolge / Order

```text
071 (Planning — erledigt)
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
- Die Einstufung ist mit NDF-WP-072 **verbindlich gelockt**. Änderungen (inkl. WP-074-Downgrade-Ventil) nur gemäß den Regeln in [FOUNDATION_0_5_SCOPE_LOCK.md](FOUNDATION_0_5_SCOPE_LOCK.md).
- Der blocking Kern bleibt klein: je ein inhaltliches Kern-Deliverable pro Titel-Hälfte (External Validation → 073/074, 1.0 Path Hardening → 079) plus Gates und Release-Strecke.
- Neutralität bleibt Invariante: Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv.
