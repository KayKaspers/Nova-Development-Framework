# Foundation 0.3 Plan

## Status

In planning (nach Release `v0.2.0-foundation`, 2026-07-03)

## DE – Ziel

Foundation 0.3 entwickelt NDF von einem **stabilisierten öffentlichen Framework** zu einem **praktisch übernehmbaren Framework**: Ein externer Nutzer soll NDF nicht nur verstehen, sondern in einem echten Projekt anwenden können — mit validiertem Project Adapter, einem nachvollziehbaren neutralen Beispielprojekt und durchgängig zweisprachigen Werkzeugen.

## EN – Goal

Foundation 0.3 evolves NDF from a **stabilized public framework** into a **practically adoptable framework**: an external user should not only understand NDF but be able to apply it to a real project — with a field-validated project adapter, a traceable neutral example project, and consistently bilingual tooling.

## DE – Warum Foundation 0.3?

Foundation 0.2 hat bewiesen, dass das Framework öffentlich sauber ist (Neutralität, Quality Gate, DE/EN-Einstieg). Was noch fehlt, ist der Beweis der **Übernehmbarkeit**: Der Adapter v0.2 wurde noch nie praktisch durchgespielt, das Beispielprojekt ist minimal, Teile der Prompt-/Checklist-Bibliothek und die Academy sind einsprachig, und die ADR-Struktur trägt dokumentierten Altbestand.

## EN – Why Foundation 0.3?

Foundation 0.2 proved that the framework is publicly clean (neutrality, quality gate, DE/EN entry). What is still missing is proof of **adoptability**: adapter v0.2 has never been exercised in practice, the example project is minimal, parts of the prompt/checklist library and the academy are monolingual, and the ADR structure carries documented legacy.

## DE – Leitprinzipien

1. **Beweis vor Ausbau** — erst den Adapter praktisch validieren, dann erweitern.
2. **Scope Lock zuerst** — keine neuen großen Features, bevor der 0.3-Umfang eingefroren ist.
3. **Klein und typisiert** — jedes Work Package bleibt klein, mit genau einem Typ.
4. **Ehrliche Zweisprachigkeit** — DE/EN-Fortschritt wird in der Translation-Status-Matrix geführt, nicht behauptet.
5. **Neutralität bleibt Invariante** — Quality Gate grün, keine privaten Bezüge, keine privaten Suchmuster in Doku.

## EN – Guiding Principles

1. **Proof before expansion** — validate the adapter in practice first, then extend.
2. **Scope lock first** — no new large features before the 0.3 scope is frozen.
3. **Small and typed** — every work package stays small, with exactly one type.
4. **Honest bilingualism** — DE/EN progress is tracked in the translation status matrix, not claimed.
5. **Neutrality stays invariant** — quality gate green, no private references, no private search patterns in docs.

## DE – Geplanter Scope

| Priorität | Thema |
|---|---|
| P1 | Scope Lock für Foundation 0.3 |
| P1 | Project Adapter Praxistest am neutralen Beispielprojekt |
| P1 | Neutral Example Project v0.2 (als Adapter-Zielprojekt ausgebaut) |
| P1 | Public Quality Gate v0.2 (Lessons aus 0.2: u. a. Schutz vor privaten Mustern in Prüf-Doku, sauberer Denylist-Workflow) |
| P2 | Prompt Library Full DE/EN Pass |
| P2 | Checklist Library Full DE/EN Pass |
| P2 | Academy Band 1 DE/EN Entry Pass (Einstiegskapitel) |
| P2 | ADR-Konsolidierungsplan bzw. klare ADR-Policy |
| P3 | Docs-Export-/Website-Readiness-Konzept |
| Release | Foundation 0.3 Release Readiness + Release Prep |

## EN – Planned Scope

Same as above: P1 = scope lock, adapter field validation, neutral example project v0.2, quality gate v0.2; P2 = full DE/EN passes for prompts, checklists and academy entry, ADR consolidation plan; P3 = docs export/website readiness concept; release track at the end.

## DE – Nicht-Ziele

- Keine v1.0-Reife und keine v1.0-Versprechen.
- Keine vollständige Website, keine fertige Export-Pipeline, keine CLI-Implementierung (nur Konzepte).
- Keine vollständige Academy (nur Einstieg DE/EN).
- Kein History-Rewrite, keine ADR-Massenmigration ohne eigenen Plan.
- Keine Integration realer privater Projekte in das öffentliche Repository.

## EN – Non-Goals

- No v1.0 maturity and no v1.0 promises.
- No complete website, no finished export pipeline, no CLI implementation (concepts only).
- No complete academy (entry chapters DE/EN only).
- No history rewrite, no bulk ADR migration without a dedicated plan.
- No integration of real private projects into the public repository.

## DE – Release-Kandidaten

Zielrelease: `v0.3.0-foundation` (Foundation Pre-Release). Kandidat, sobald die P1-Themen abgeschlossen und die P2-Themen mehrheitlich erledigt oder bewusst verschoben sind. Kriterien: `docs/release/FOUNDATION_0_3_RELEASE_CRITERIA.md`

## EN – Release Candidates

Target release: `v0.3.0-foundation` (foundation pre-release). Candidate once the P1 topics are complete and the P2 topics are mostly done or consciously deferred. Criteria: `docs/release/FOUNDATION_0_3_RELEASE_CRITERIA.md`

## DE – Risiken

1. **Scope-Wachstum** wie in 0.2 (Neutralisierung/i18n kamen ungeplant dazu) — Gegenmittel: Scope Lock als erstes WP.
2. **Adapter-Praxistest deckt Lücken auf** — erwünscht, kann aber Folge-WPs erzeugen; Puffer einplanen.
3. **i18n-Pflegeaufwand** — bilinguale Dokumente verdoppeln Änderungskosten; Umstellung bleibt priorisiert statt flächig.
4. **Ein-Personen-Engpass** — Human Maintainer ist einziger Freigabepunkt; kleine WPs halten Reviews machbar.

## EN – Risks

1. **Scope growth** as in 0.2 — mitigation: scope lock as the first work package.
2. **Adapter field test reveals gaps** — desirable, but may spawn follow-up work packages; plan buffer.
3. **i18n maintenance cost** — bilingual documents double change cost; transition stays prioritized, not blanket.
4. **Single-person bottleneck** — the human maintainer is the only approval point; small work packages keep reviews feasible.

## DE – Erfolgskriterien

1. Der Project Adapter wurde vollständig an einem neutralen Beispielprojekt durchgespielt; Erkenntnisse sind zurückgeflossen.
2. Ein externer Nutzer kann den Adoptions-Flow von README → Adapter-Guide → Beispielprojekt ohne interne Vorkenntnisse nachvollziehen.
3. Prompts, Checklisten und Academy-Einstieg sind gemäß Matrix DE/EN nutzbar.
4. ADR-Policy ist entschieden und dokumentiert.
5. Quality Gate v0.2 ist grün und schützt zusätzlich vor den in 0.2 gefundenen Fehlerklassen.
6. `v0.3.0-foundation` ist mit ehrlichen Release Notes veröffentlichbar.

## EN – Success Criteria

1. The project adapter has been fully exercised on a neutral example project; findings flowed back.
2. An external user can follow the adoption flow README → adapter guide → example project without insider knowledge.
3. Prompts, checklists and the academy entry are DE/EN usable per the matrix.
4. The ADR policy is decided and documented.
5. Quality gate v0.2 is green and additionally protects against the failure classes found in 0.2.
6. `v0.3.0-foundation` can be released with honest release notes.
