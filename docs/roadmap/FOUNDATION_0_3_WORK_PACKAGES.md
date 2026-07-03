# Foundation 0.3 – Work Package Queue (Draft)

> Status: Planungsentwurf aus WP-044. Reihenfolge und Zuschnitt werden mit dem Scope Lock (NDF-WP-045) eingefroren. / Planning draft; order and scope are frozen with the scope lock (NDF-WP-045).

| ID | Titel | Typ | Priorität | Ziel | Abhängigkeiten | Release-Relevanz |
|---|---|---|---|---|---|---|
| NDF-WP-045 | Foundation 0.3 Scope Lock | docs-only / planning | P1 | 0.3-Umfang final einfrieren, WP-Queue bestätigen, Nicht-Ziele fixieren | WP-044 | Pflicht (Gate für alle weiteren WPs) |
| NDF-WP-046 | Neutral Example Project v0.2 | docs-only / example | P1 | `examples/minimal-ndf-project` zu realistischem, neutralem Adapter-Zielprojekt ausbauen (DE/EN) | WP-045 | Pflicht (Basis für WP-047) |
| NDF-WP-047 | Project Adapter Practical Validation | review-only + docs-only | P1 | Adapter v0.2 Phasen 0–10 vollständig am Beispielprojekt durchspielen; Lücken als Findings zurückführen | WP-046 | Pflicht (Kernbeweis von 0.3) |
| NDF-WP-052 | Public Quality Gate v0.2 | feature (Script) | P1 | Gate härten: u. a. Scan-Schutz gegen private Muster in Prüf-Doku, Prüfung neuer/untracked Dateien vor Commit, Denylist-Workflow-Doku | WP-045 | Pflicht |
| NDF-WP-048 | Prompt Library Full DE/EN Pass | docs-only / i18n | P2 | Restliche ~30 Prompts DE/EN-Kern (Zweck/Grenzen/Rückmeldung) | WP-045 | Soll |
| NDF-WP-049 | Checklist Library Full DE/EN Pass | docs-only / i18n | P2 | Restliche Checklisten (inkl. `security/`, project-starter) DE/EN-Zweck | WP-045 | Soll |
| NDF-WP-050 | Academy Band 1 DE/EN Entry Pass | docs-only / i18n | P2 | Einstiegskapitel (01–04) DE/EN, Einstieg von README aus verlinken | WP-045 | Soll |
| NDF-WP-051 | ADR Structure Consolidation Plan | docs-only / adr-policy | P2 | ADR-Policy entscheiden (Nummernraum, Ablageort, Umgang mit Altbestand) — Plan, noch keine Migration | WP-045 | Soll |
| NDF-WP-053 | Docs Export / Website Readiness Concept | docs-only / concept | P3 | MkDocs-/Export-Konzept konkretisieren (kein Build, keine Pipeline) | WP-045 | Optional |
| NDF-WP-054 | Foundation 0.3 Release Readiness Review | review-only | Release | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.3-Kriterien | P1-WPs done, P2 mehrheitlich | Pflicht |
| NDF-WP-055 | Foundation 0.3 Release Prep | docs-only / release-prep | Release | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide-Update für `v0.3.0-foundation` | WP-054 | Pflicht |

## Reihenfolge-Empfehlung / Recommended order

```text
045 (Scope Lock)
→ 046 → 047 (Adoptionsbeweis)          [parallel möglich: 052]
→ 048 / 049 / 050 / 051 (P2, in beliebiger Reihenfolge)
→ 053 (optional)
→ 054 → 055 (Release-Strecke)
```

## Regeln / Rules

- Jedes WP behält genau einen primären Typ und endet mit Rückmeldung an Nova (ChatGPT).
- Findings aus WP-047 dürfen neue kleine WPs erzeugen; sie laufen vor WP-054 oder werden als bekannte Einschränkung dokumentiert.
- Kein WP startet vor abgeschlossenem Scope Lock (Ausnahme: keiner).
