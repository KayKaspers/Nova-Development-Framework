# Foundation 0.4 – Work Package Queue (Draft)

> Status: Planungsentwurf aus WP-057. Die verbindliche Einstufung (release-blocking / optional / deferred) wird mit dem Scope Lock (NDF-WP-058) eingefroren. / Planning draft; the binding classification is frozen with the scope lock (NDF-WP-058).

| ID | Titel | Typ | Priorität | Ziel | Abhängigkeiten | Draft-Einstufung | ggf. → 0.5 |
|---|---|---|---|---|---|---|---|
| NDF-WP-058 | Foundation 0.4 Scope Lock | docs-only / planning-gate | P1 | 0.4-Umfang einfrieren, Queue bestätigen, Nicht-Ziele fixieren | WP-057 | release-blocking (Gate) | nein |
| NDF-WP-059 | Adapter Conventions Polish | docs-only | P1 | WP-047-Backlog 1–3 umsetzen: Manifest-Format-Konvention, Health-Score-Kategorien, Output-Pfad-Konvention; dazu Präfix-Beispiel und First-Safe-WP-Template | WP-058 | release-blocking (Kern-Hardening) | nein |
| NDF-WP-060 | Prompt Library DE/EN Priority Pass | docs-only / i18n | P1 | größte öffentliche i18n-Lücke schließen: übrige zentrale Prompts DE/EN-Kern | WP-058 | release-blocking | Rest ggf. 0.5 |
| NDF-WP-061 | Checklist Library DE/EN Priority Pass | docs-only / i18n | P2 | übrige Checklisten DE/EN-Zweck | WP-058 | optional (should-have) | ja |
| NDF-WP-062 | Academy Band 1 Entry Pass | docs-only / i18n | P2 | Einstiegskapitel (01–04) DE/EN, von README verlinkt | WP-058 | optional (should-have) | ja |
| NDF-WP-063 | ADR Policy & Structure Consolidation Plan | docs-only / adr-policy | P2 | ADR-Policy entscheiden (Nummernraum, Ablageort, Altbestand) — nur Plan, keine Migration | WP-058 | optional (should-have) | ja |
| NDF-WP-064 | Independent Adapter Validation Run | review-only | P3 | Adapter durch Unbeteiligte(n) durchspielen lassen (Selbstvalidierungs-Bias aus WP-047 adressieren) | WP-059 | deferred candidate | ja |
| NDF-WP-065 | Docs Export / Website Readiness Concept | docs-only / concept | P3 | MkDocs-/Export-Konzept konkretisieren (kein Build, keine Pipeline) | alle blocking WPs fertig | deferred candidate (aus 0.3) | ja |
| NDF-WP-066 | Public Quality Gate Maintenance Review | review-only + docs-only | P2 | v0.2-Nachlauf: Gate weiterhin grün, Doku/Checkliste aktuell, kleine Härtung nur bei klarem Bedarf | WP-058 | optional (should-have) | ja |
| NDF-WP-067 | Foundation 0.4 Release Readiness Review | review-only | Release | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.4-Kriterien | 059, 060 done | release-blocking | nein |
| NDF-WP-068 | Foundation 0.4 Release Prep | docs-only / release-prep | Release | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide für `v0.4.0-foundation` | WP-067 | release-blocking | nein |

## Draft-Reihenfolge / Draft order

```text
058 (Scope Lock)
→ 059 (Adapter Conventions Polish) ‖ 060 (Prompt DE/EN)     [Kern-Hardening]
→ 061 / 062 / 063 / 066 (optional, beliebige Reihenfolge)
→ 064 / 065 (deferred, nur bei Restkapazität)
→ 067 → 068 (Release-Strecke)
```

## Hinweis / Note

Dies ist ein **Draft**. Die verbindliche release-blocking/optional/deferred-Einstufung entsteht erst in NDF-WP-058 (Scope Lock) analog zum 0.3-Vorgehen. Kein WP startet vor abgeschlossenem Scope Lock.
