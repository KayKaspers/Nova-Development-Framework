# Foundation 0.4 Plan

## Status

Scope locked (NDF-WP-058, 2026-07-04) — verbindliche Einstufung: [FOUNDATION_0_4_SCOPE_LOCK.md](FOUNDATION_0_4_SCOPE_LOCK.md). Arbeitstitel: **Adoption Hardening & Public Usability**.

**Scope-Lock-Regel / Scope lock rule:** Foundation 0.4 bleibt Adoption Hardening & Public Usability mit bewusst kleinem Release-blocking Kern (058, 059, 060, 067, 068 — je ein Deliverable pro Titel-Hälfte). Weitere Wünsche sind optional oder gehen nach 0.5; neue blocking WPs nur über die Änderungsregeln im Scope Lock. / Foundation 0.4 keeps a deliberately small release-blocking core; additional wishes are optional or deferred, new blocking work packages only via the scope lock change rules.

## DE – Ziel

Foundation 0.4 härtet NDF nach dem in 0.3 erbrachten Adoptionsbeweis: Der Project Adapter soll für externe Nutzer **reibungsärmer** werden, die größten DE/EN-Lücken werden priorisiert geschlossen, und die öffentliche Doku-Nutzung wird abgerundet — ohne neue große Konzepte und ohne v1.0-Anspruch.

## EN – Goal

Foundation 0.4 hardens NDF after the adoption proof delivered in 0.3: make the project adapter **less friction-prone** for external users, close the largest DE/EN gaps by priority, and round out public documentation usability — without new large concepts and without a v1.0 claim.

## DE – Warum Foundation 0.4?

Foundation 0.3 hat bewiesen, dass NDF übernehmbar ist. Die praktische Adapter-Validierung (WP-047) hat aber konkrete Konventionslücken aufgedeckt (Manifest-Format, Health-Score-Kategorien, Output-Pfad, Präfix-Beispiel, fehlendes First-Safe-WP-Template), und Teile der Prompt-/Checklist-Bibliothek sowie die Academy sind noch einsprachig. 0.4 schließt genau diese bekannten, benannten Lücken — nicht mehr.

## EN – Why Foundation 0.4?

Foundation 0.3 proved NDF is adoptable. But the practical adapter validation (WP-047) surfaced concrete convention gaps (manifest format, health-score categories, output path, prefix example, missing first-safe-WP template), and parts of the prompt/checklist library and the academy are still monolingual. 0.4 closes exactly these known, named gaps — nothing more.

## DE – Leitprinzipien

1. **Bekannte Lücken schließen, keine neuen öffnen** — 0.4 arbeitet den dokumentierten Backlog ab.
2. **Scope Lock zuerst** (WP-058) — wie in 0.3, gegen Scope Creep.
3. **Klein und messbar** — jede Verbesserung ist an einem konkreten 0.3-Finding oder Matrix-Eintrag festmachbar.
4. **Ehrliche Zweisprachigkeit** — Fortschritt in `docs/i18n/TRANSLATION_STATUS.md` geführt, nicht behauptet.
5. **Neutralität bleibt Invariante** — Public Quality Gate v0.2 grün, keine privaten Bezüge/Suchmuster, new-file neutrality check aktiv.

## EN – Guiding Principles

1. **Close known gaps, open none** — 0.4 works down the documented backlog.
2. **Scope lock first** (WP-058) — as in 0.3, against scope creep.
3. **Small and measurable** — every improvement maps to a concrete 0.3 finding or matrix entry.
4. **Honest bilingualism** — progress tracked in `docs/i18n/TRANSLATION_STATUS.md`, not claimed.
5. **Neutrality stays invariant** — public quality gate v0.2 green, no private references/search patterns, new-file neutrality check active.

## DE – Geplanter Scope

| Priorität | Thema |
|---|---|
| P1 | Scope Lock für Foundation 0.4 |
| P1 | Adapter Conventions Polish (aus WP-047-Backlog: Manifest-Format, Health-Score-Kategorien, Output-Pfad-Konvention, Präfix-Beispiel, First-Safe-WP-Template) |
| P1 | Prompt Library DE/EN Priority Pass (größte öffentliche Nutzbarkeitslücke) |
| P2 | Checklist Library DE/EN Priority Pass |
| P2 | Academy Band 1 Entry Pass (DE/EN-Einstieg) |
| P2 | ADR Policy & Structure Consolidation Plan (nur Policy/Plan) |
| P2 | Public Quality Gate Maintenance Review (v0.2-Nachlauf, leicht) |
| P3 | Independent Adapter Validation Run (durch Unbeteiligte) |
| P3 | Docs Export / Website Readiness Concept (nur Konzept) |
| Release | Foundation 0.4 Release Readiness + Release Prep |

## EN – Planned Scope

Same as above: P1 = scope lock, adapter conventions polish, prompt DE/EN priority pass; P2 = checklist DE/EN, academy entry, ADR policy plan, quality gate maintenance; P3 = independent adapter run, docs export/website concept; release track at the end.

## DE – Nicht-Ziele

- Keine v1.0-Reife und keine v1.0-Versprechen.
- Keine vollständige Website, keine fertige Export-Pipeline, keine CLI-Implementierung (nur Konzepte).
- Keine vollständige Academy-Übersetzung.
- Kein History-Rewrite, keine ADR-Massenmigration (nur Policy/Plan).
- Keine Integration realer privater Projekte.
- Keine neuen großen Framework-Konzepte ohne Scope-Review.

## EN – Non-Goals

No v1.0 maturity or promises; no complete website, export pipeline, or CLI (concepts only); no full academy translation; no history rewrite, no bulk ADR migration (policy/plan only); no integration of real private projects; no new large framework concepts without a scope review.

## DE – Release-Kandidaten

Zielrelease: `v0.4.0-foundation` (Foundation Pre-Release). Kandidat, sobald die P1-Themen abgeschlossen sind und die P2-Themen mehrheitlich erledigt oder bewusst verschoben sind. Kriterien: `docs/release/FOUNDATION_0_4_RELEASE_CRITERIA.md`

## EN – Release Candidates

Target release: `v0.4.0-foundation` (foundation pre-release). Candidate once P1 topics are complete and P2 topics are mostly done or consciously deferred. Criteria: `docs/release/FOUNDATION_0_4_RELEASE_CRITERIA.md`

## DE – Risiken

1. **Scope-Wachstum** — Gegenmittel: Scope Lock als erstes WP; P2/P3 dürfen den Release nicht blockieren.
2. **i18n-Pflegeaufwand** — bilinguale Dokumente verdoppeln Änderungskosten; Umstellung bleibt priorisiert statt flächig.
3. **„Adoption Hardening" wirkt unscharf** — Gegenmittel: jede P1-Verbesserung ist an ein konkretes WP-047-Finding gebunden.
4. **Ein-Personen-Engpass** — Human Maintainer ist einziger Freigabepunkt; kleine WPs halten Reviews machbar.

## EN – Risks

1. **Scope growth** — mitigation: scope lock first; P2/P3 must not block the release.
2. **i18n maintenance cost** — bilingual docs double change cost; transition stays prioritized, not blanket.
3. **"Adoption hardening" can feel vague** — mitigation: each P1 improvement is tied to a concrete WP-047 finding.
4. **Single-person bottleneck** — the human maintainer is the only approval point; small work packages keep reviews feasible.

## DE – Erfolgskriterien

1. Die Adapter-Conventions-Backlog-Punkte 1–3 (should-have aus WP-047) sind umgesetzt; ein externer Nutzer stolpert nicht mehr über Format-/Pfad-Unklarheiten.
2. Die höchstpriorisierte DE/EN-Lücke (Prompts) ist geschlossen; der Reststand ist ehrlich in der Matrix geführt.
3. ADR-Policy ist entschieden und dokumentiert (Plan, keine Migration).
4. Public Quality Gate v0.2 bleibt grün und wird bei Bedarf leicht gewartet.
5. `v0.4.0-foundation` ist mit ehrlichen Release Notes veröffentlichbar — kein v1.0.

## EN – Success Criteria

1. Adapter conventions backlog items 1–3 (WP-047 should-haves) are implemented; external users no longer trip over format/path ambiguities.
2. The highest-priority DE/EN gap (prompts) is closed; the remaining state is tracked honestly in the matrix.
3. The ADR policy is decided and documented (plan, no migration).
4. Public quality gate v0.2 stays green and receives light maintenance if needed.
5. `v0.4.0-foundation` can be released with honest release notes — not v1.0.
