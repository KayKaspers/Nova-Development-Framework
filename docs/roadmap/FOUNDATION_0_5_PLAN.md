# Foundation 0.5 Plan

## DE – Zweck

Dieser Plan definiert den vorgeschlagenen Umfang für Foundation 0.5. Er ist das Ergebnis von NDF-WP-071 (Planning) — **kein Scope Lock**; verbindlich wird der Umfang erst mit NDF-WP-072.

## EN – Purpose

This plan defines the proposed scope for Foundation 0.5. It is the result of NDF-WP-071 (planning) — **not a scope lock**; the scope only becomes binding with NDF-WP-072.

## DE – Status

**Scope locked** (NDF-WP-072, 2026-07-06) — verbindliche Einstufung: [FOUNDATION_0_5_SCOPE_LOCK.md](FOUNDATION_0_5_SCOPE_LOCK.md). Foundation 0.4 ist als `v0.4.0-foundation` veröffentlicht, alle manuellen Follow-ups sind geschlossen (NDF-WP-070). Foundation 0.5 ist nicht released.

## EN – Status

**Scope locked** (NDF-WP-072, 2026-07-06) — binding classification: [FOUNDATION_0_5_SCOPE_LOCK.md](FOUNDATION_0_5_SCOPE_LOCK.md). Foundation 0.4 is published as `v0.4.0-foundation`, all manual follow-ups are closed (NDF-WP-070). Foundation 0.5 is not released.

## DE – Zielbild

**Foundation 0.5 – External Validation & 1.0 Path Hardening**

Zwei Kernideen, je eine pro Titel-Hälfte:

1. **External Validation:** Die größte dokumentierte Schwäche des bisherigen Adoptionsbeweises ist der Selbstvalidierungs-Bias — der Adapter wurde vom selben Implementation Agent validiert, der ihn mitgebaut hat (Grenze aus WP-047, seit 0.3 offen). 0.5 bereitet einen unabhängigen Validierungslauf strukturiert vor und führt ihn durch, soweit eine unbeteiligte Person verfügbar ist.
2. **1.0 Path Hardening:** Der Weg Richtung v1.0 wird erstmals messbar gemacht — als ehrlicher Kriterien-**Entwurf**, nicht als Versprechen. Foundation 0.5 ist ausdrücklich **nicht** v1.0 und behauptet keine v1.0-Reife.

## EN – Target

**Foundation 0.5 – External Validation & 1.0 Path Hardening.** Two core ideas, one per half of the title: (1) address the documented self-validation bias from WP-047 by preparing — and, where an uninvolved person is available, executing — an independent adapter validation run; (2) make the path toward v1.0 measurable for the first time as an honest criteria **draft**, not a promise. Foundation 0.5 is explicitly **not** v1.0 and claims no v1.0 maturity.

## DE – Warum Foundation 0.5 nötig ist

- 0.3 hat bewiesen, dass NDF übernehmbar ist; 0.4 hat die Übernahme gehärtet. Beide Beweise stammen aber aus derselben Rollenkette (Nova (ChatGPT) → Implementation Agent → Human Maintainer). Ohne unabhängige Sicht bleibt der Adoptionsbeweis strukturell einseitig.
- „Kein v1.0" ist bisher nur eine Abgrenzung, keine Messlatte. Solange v1.0-Kriterien nicht formalisiert sind, lässt sich weder Fortschritt noch Fertigwerden ehrlich beurteilen.
- Aus 0.4 sind bewusst verschobene Reste offen (Checklist DE/EN, Academy-Einstieg, ADR-Policy-Plan, Gate-Maintenance, Docs Export/Website-Konzept, i18n-Rest). Sie brauchen eine ehrliche Neubewertung statt automatischer Übernahme.

## EN – Why Foundation 0.5 Is Needed

0.3 proved NDF is adoptable; 0.4 hardened that adoption — but both proofs come from the same role chain. Without an independent perspective, the adoption proof stays structurally one-sided. "Not v1.0" has so far been a disclaimer, not a yardstick; without formalized v1.0 criteria, neither progress nor completion can be judged honestly. And the deliberately deferred 0.4 leftovers need an honest re-evaluation instead of automatic carry-over.

## DE – Vorgeschlagener Fokus

| Priorität | Thema |
|---|---|
| P1 | Scope Lock für Foundation 0.5 (NDF-WP-072) |
| P1 | Independent Adapter Validation Preparation (NDF-WP-073): Testleitfaden, neutrales Setup, Erfolgskriterien, Feedback-Format — damit eine unbeteiligte Person ohne Vorwissen validieren kann |
| P1 | Independent Adapter Validation Run (NDF-WP-074): tatsächlicher unabhängiger Durchlauf; abhängig von Verfügbarkeit einer unbeteiligten Person (Downgrade-Ventil siehe Risiken) |
| P1 | v1.0 Readiness Criteria Draft (NDF-WP-079): messbare Kriterien Richtung v1.0 — Entwurf, kein Commitment |
| P2 | Checklist Library DE/EN Priority Pass (NDF-WP-075, aus 0.4 übernommen) |
| P2 | ADR Policy & Structure Consolidation Plan (NDF-WP-076, aus 0.4 übernommen — nur Policy/Plan) |
| P2 | Academy Band 1 Entry Pass (NDF-WP-077, aus 0.4 übernommen) |
| P2 | Public Quality Gate Maintenance Review (NDF-WP-078, aus 0.4 übernommen) |
| P3 | Docs Export / Website Readiness Concept (NDF-WP-080, aus 0.3/0.4 übernommen — nur Konzept) |
| Release | Foundation 0.5 Release Readiness (NDF-WP-081) + Release Prep (NDF-WP-082) |

## EN – Proposed Focus

Same as above: P1 = scope lock, independent validation preparation + run, v1.0 readiness criteria draft; P2 = checklist DE/EN, ADR policy plan, academy entry, gate maintenance (all carried over from 0.4); P3 = docs export/website concept; release track at the end.

## DE – Release-blocking Kandidaten

Nur Kandidaten — verbindlich erst mit dem Scope Lock (NDF-WP-072):

- NDF-WP-072 (Scope Lock — Gate)
- NDF-WP-073 (Validation Preparation — Kern: External Validation, selbstständig erfüllbar)
- NDF-WP-074 (Validation Run — Kern: External Validation; mit explizitem Downgrade-Ventil über WP-081, falls keine unbeteiligte Person verfügbar ist)
- NDF-WP-079 (v1.0 Criteria Draft — Kern: 1.0 Path Hardening)
- NDF-WP-081 / NDF-WP-082 (Release-Strecke)

## EN – Release-blocking Candidates

Candidates only — binding with the scope lock (NDF-WP-072): WP-072 (gate), WP-073 (validation preparation, self-contained), WP-074 (validation run, with an explicit downgrade valve via WP-081 if no uninvolved person is available), WP-079 (v1.0 criteria draft), WP-081/082 (release track).

## DE – Optionale Kandidaten

NDF-WP-075 (Checklist DE/EN), NDF-WP-076 (ADR Policy Plan), NDF-WP-077 (Academy Entry), NDF-WP-078 (Gate Maintenance) — alle should-have, keiner blockiert den Release. Unerledigtes wird ehrlich in Release Notes und Translation-Status-Matrix geführt.

## EN – Optional Candidates

WP-075 (checklist DE/EN), WP-076 (ADR policy plan), WP-077 (academy entry), WP-078 (gate maintenance) — all should-have, none blocks the release; unfinished items are tracked honestly in release notes and the translation status matrix.

## DE – Deferred / Nicht Teil von 0.5

- NDF-WP-080 Docs Export / Website Readiness Concept (deferred candidate — nur bei Restkapazität; kein Build, keine Pipeline)
- Restliche i18n-Flächenübersetzung (bleibt priorisiert statt flächig; kein DE/EN-Massenprojekt)
- Vollständige Security-/Gate-Prompt-Übersetzung (bleibt DE/EN-Kern-Stand aus 0.4)
- ADR-Massenmigration (erst nach beschlossener Policy aus WP-076, frühestens 0.6)
- v1.0-Release selbst (0.5 erstellt nur den Kriterien-Entwurf)

## EN – Deferred / Not Part of 0.5

WP-080 docs export/website concept (deferred candidate); remaining blanket i18n translation; full security/gate prompt translation; bulk ADR migration (only after the WP-076 policy, 0.6 at the earliest); the v1.0 release itself (0.5 only drafts the criteria).

## DE – Nicht-Ziele

- Keine v1.0-Reife und keine v1.0-Versprechen — der Criteria Draft ist eine Messlatte, kein Zeitplan.
- Kein Big-Bang, kein Rewrite bestehender Framework-Teile.
- Keine Website, keine Export-Pipeline, keine CLI (höchstens Konzept via WP-080).
- Kein DE/EN-Massenprojekt; Übersetzung bleibt priorisiert.
- Keine Integration realer privater Projekte; Neutralität bleibt Invariante.
- Keine neuen Großkonzepte ohne Scope-Review.

## EN – Non-Goals

No v1.0 maturity or promises (the criteria draft is a yardstick, not a schedule); no big bang, no rewrite; no website, export pipeline, or CLI (concept only via WP-080); no blanket DE/EN project; no integration of real private projects; no new large concepts without a scope review.

## DE – Risiken

1. **Abhängigkeit von Unbeteiligten (größtes Risiko):** WP-074 braucht eine Person außerhalb der bisherigen Rollenkette. Gegenmittel: WP-073 macht die Vorbereitung unabhängig erfüllbar; für WP-074 definiert der Scope Lock ein explizites Downgrade-Ventil über die Readiness Review (WP-081) — analog zum WP-060-Ventil in 0.4.
2. **v1.0-Missverständnis:** Ein Criteria Draft kann als Release-Ankündigung gelesen werden. Gegenmittel: jede Erwähnung als „Entwurf/Draft" markieren; Invariante „kein v1.0-Claim" bleibt in Kriterien und Gate-Kultur.
3. **Scope-Wachstum durch 0.4-Reste:** Vier übernommene optionale WPs verleiten zum Vollständigkeitsanspruch. Gegenmittel: sie bleiben optional; der blocking Kern hat wie in 0.4 je ein Deliverable pro Titel-Hälfte.
4. **Ein-Personen-Engpass:** Der Human Maintainer bleibt einziger Freigabepunkt — kleine WPs halten Reviews machbar.

## EN – Risks

(1) Dependence on uninvolved people — WP-073 stays self-contained and WP-074 gets an explicit downgrade valve via the readiness review; (2) v1.0 misunderstanding — every mention marked as draft, "no v1.0 claim" stays invariant; (3) scope growth via 0.4 leftovers — they stay optional, the blocking core keeps one deliverable per title half; (4) single-person bottleneck — small work packages keep reviews feasible.

## DE – Nächster Schritt

**NDF-WP-072 – Foundation 0.5 Scope Lock:** Queue verbindlich einstufen (release-blocking / optional / deferred), Downgrade-Ventil für WP-074 festschreiben, Änderungsregeln definieren. Kein inhaltliches WP startet vor dem Scope Lock.

## EN – Next Step

**NDF-WP-072 – Foundation 0.5 scope lock:** classify the queue bindingly, fix the WP-074 downgrade valve, define change rules. No content work package starts before the scope lock.
