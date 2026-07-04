# Foundation 0.3 – Work Package Queue

> Status: **Scope locked** (NDF-WP-045, 2026-07-03). Verbindliche Einstufung siehe Spalte „Scope Lock" und [FOUNDATION_0_3_SCOPE_LOCK.md](FOUNDATION_0_3_SCOPE_LOCK.md). / Scope locked; binding classification in the "Scope Lock" column.

| ID | Titel | Typ | Priorität | Ziel | Abhängigkeiten | Scope Lock |
|---|---|---|---|---|---|---|
| NDF-WP-045 | Foundation 0.3 Scope Lock | docs-only / planning-gate | P1 | 0.3-Umfang final einfrieren, WP-Queue bestätigen, Nicht-Ziele fixieren | WP-044 | **release-blocking** (Gate — abgeschlossen mit diesem Dokument) |
| NDF-WP-046 | Neutral Example Project v0.2 | docs-only / example | P1 | Neutrales Adapter-Fixture `examples/neutral-example-project/` (SampleProject, Pre-Adoption-Zustand) | WP-045 | **release-blocking** — angelegt in WP-046 |
| NDF-WP-047 | Project Adapter Practical Validation | review-only + docs-only | P1 | Adapter v0.2 Phasen 0–10 vollständig am Beispielprojekt durchspielen; Lücken als Findings zurückführen | WP-046 | **release-blocking** — validiert in WP-047: **PASS WITH NOTES** (`docs/validation/project-adapter/`) |
| NDF-WP-052 | Public Quality Gate v0.2 | feature (Script) | P1 | Gate härten: u. a. Scan-Schutz gegen private Muster in Prüf-Doku, Prüfung neuer/untracked Dateien vor Commit, Denylist-Workflow-Doku | WP-045 | **release-blocking** — umgesetzt in WP-052 (new-file neutrality check, `--tracked-only`, Self-Tests, Doku + Checkliste) |
| NDF-WP-048 | Prompt Library Full DE/EN Pass | docs-only / i18n | P2 | Restliche ~30 Prompts DE/EN-Kern (Zweck/Grenzen/Rückmeldung) | WP-045 | optional (should-have; Reststand ehrlich dokumentieren) |
| NDF-WP-049 | Checklist Library Full DE/EN Pass | docs-only / i18n | P2 | Restliche Checklisten (inkl. `security/`, project-starter) DE/EN-Zweck | WP-045 | optional (should-have) |
| NDF-WP-050 | Academy Band 1 DE/EN Entry Pass | docs-only / i18n | P2 | Einstiegskapitel (01–04) DE/EN, Einstieg von README aus verlinken | WP-045 | optional (should-have) |
| NDF-WP-051 | ADR Structure Consolidation Plan | docs-only / adr-policy | P2 | ADR-Policy entscheiden (Nummernraum, Ablageort, Umgang mit Altbestand) — Plan, noch keine Migration | WP-045 | optional (should-have; nur Policy, keine Migration) |
| NDF-WP-053 | Docs Export / Website Readiness Concept | docs-only / concept | P3 | MkDocs-/Export-Konzept konkretisieren (kein Build, keine Pipeline) | alle blocking WPs fertig | **deferred candidate** (nur bei Restkapazität, sonst 0.4) |
| NDF-WP-054 | Foundation 0.3 Release Readiness Review | review-only | Release | Ehrliches GO/GO WITH NOTES/REWORK/STOP gegen die 0.3-Kriterien | 046, 047, 052 done | **release-blocking** |
| NDF-WP-055 | Foundation 0.3 Release Prep | docs-only / release-prep | Release | Release Notes, Kriterien-Abschluss, Go/No-Go, Tagging-Guide-Update für `v0.3.0-foundation` | WP-054 | **release-blocking** |

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
- Findings aus WP-047 dürfen neue kleine WPs erzeugen; release-blocking nur, wenn sie den Adoptionsbeweis betreffen — sonst bekannte Einschränkung (Regel im Scope Lock).
- Kein WP startet vor abgeschlossenem Scope Lock (Ausnahme: keiner).
- Änderungen an der Blocking-Einstufung nur gemäß den Änderungsregeln in [FOUNDATION_0_3_SCOPE_LOCK.md](FOUNDATION_0_3_SCOPE_LOCK.md).
