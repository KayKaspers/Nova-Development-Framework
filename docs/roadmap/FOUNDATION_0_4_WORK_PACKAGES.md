# Foundation 0.4 – Work Package Queue

> Status: **Scope locked** (NDF-WP-058, 2026-07-04). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_4_SCOPE_LOCK.md](FOUNDATION_0_4_SCOPE_LOCK.md). / Scope locked; binding classification in the "Scope Lock" column.

| ID | Titel | Typ | Priorität | Ziel | Abhängigkeiten | Scope Lock | ggf. → 0.5 |
|---|---|---|---|---|---|---|---|
| NDF-WP-058 | Foundation 0.4 Scope Lock | docs-only / planning-gate | P1 | 0.4-Umfang einfrieren, Queue bestätigen, Nicht-Ziele fixieren | WP-057 | **release-blocking** (Gate — abgeschlossen mit diesem Dokument) | nein |
| NDF-WP-059 | Adapter Conventions Polish | docs-only | P1 | WP-047-Backlog 1–3 umsetzen: Manifest-Format-Konvention, Health-Score-Kategorien, Output-Pfad-Konvention; dazu Präfix-Beispiel und First-Safe-WP-Template | WP-058 | **release-blocking** (Kern: Adoption Hardening) — umgesetzt in WP-059 (`PROJECT_ADAPTER_CONVENTIONS.md`) | nein |
| NDF-WP-060 | Prompt Library DE/EN Priority Pass | docs-only / i18n | P1 | meistgenutzte zentrale Prompts DE/EN-Kern (Priority Pass, nicht gesamte Bibliothek) | WP-058 | **release-blocking** (Kern: Public Usability) — umgesetzt in WP-060: 5 Adoptions-Prompts voll bilingual + 7 Security-/Gate-Prompts DE/EN-Kern (`PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md`) | Rest → 0.5 |
| NDF-WP-061 | Checklist Library DE/EN Priority Pass | docs-only / i18n | P2 | übrige Checklisten DE/EN-Zweck | WP-058 | optional (should-have) | ja |
| NDF-WP-062 | Academy Band 1 Entry Pass | docs-only / i18n | P2 | Einstiegskapitel (01–04) DE/EN, von README verlinkt | WP-058 | optional (should-have) | ja |
| NDF-WP-063 | ADR Policy & Structure Consolidation Plan | docs-only / adr-policy | P2 | ADR-Policy entscheiden (Nummernraum, Ablageort, Altbestand) — nur Plan, keine Migration | WP-058 | optional (should-have) | ja |
| NDF-WP-064 | Independent Adapter Validation Run | review-only | P3 | Adapter durch Unbeteiligte(n) durchspielen lassen (Selbstvalidierungs-Bias aus WP-047 adressieren) | WP-059 | **deferred candidate** (nur wenn Unbeteiligte verfügbar) | ja |
| NDF-WP-065 | Docs Export / Website Readiness Concept | docs-only / concept | P3 | MkDocs-/Export-Konzept konkretisieren (kein Build, keine Pipeline) | alle blocking WPs fertig | **deferred candidate** (aus 0.3) | ja |
| NDF-WP-066 | Public Quality Gate Maintenance Review | review-only + docs-only | P2 | v0.2-Nachlauf: Gate weiterhin grün, Doku/Checkliste aktuell, kleine Härtung nur bei klarem Bedarf | WP-058 | optional (should-have) | ja |
| NDF-WP-067 | Foundation 0.4 Release Readiness Review | review-only | Release | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.4-Kriterien | 059, 060 done | **release-blocking** — durchgeführt in WP-067: **GO WITH NOTES** (`docs/release/FOUNDATION_0_4_RELEASE_READINESS_REVIEW.md`) | nein |
| NDF-WP-068 | Foundation 0.4 Release Prep | docs-only / release-prep | Release | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide für `v0.4.0-foundation` | WP-067 | **release-blocking** — done: `v0.4.0-foundation` veröffentlicht 2026-07-04; Post-Release-Cleanup in WP-069 | nein |

## Reihenfolge / Order

```text
058 (Scope Lock)
→ 059 (Adapter Conventions Polish) ‖ 060 (Prompt DE/EN)     [Kern-Hardening]
→ 061 / 062 / 063 / 066 (optional, beliebige Reihenfolge)
→ 064 / 065 (deferred, nur bei Restkapazität)
→ 067 → 068 (Release-Strecke)
```

## Regeln / Rules

- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Kein WP startet vor abgeschlossenem Scope Lock (WP-058 ist damit erledigt).
- Änderungen an der Blocking-Einstufung nur gemäß den Änderungsregeln in [FOUNDATION_0_4_SCOPE_LOCK.md](FOUNDATION_0_4_SCOPE_LOCK.md) — insbesondere das WP-060-Downgrade-Ventil über WP-067.
