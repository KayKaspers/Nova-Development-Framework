# Foundation 0.7 Plan

## DE – Zweck

Dieser Plan definiert den Umfang für Foundation 0.7 (Ergebnis von NDF-WP-097). **Status-Update: Scope locked** (NDF-WP-098, 2026-07-08) — verbindliche Einstufung: [FOUNDATION_0_7_SCOPE_LOCK.md](FOUNDATION_0_7_SCOPE_LOCK.md). Release-blocking sind nur 098, 099 (Checklist-Entscheidung — **erledigt: Option B, optional mit finaler Begründung**, [FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md](FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md)), 100 (v1.x Compatibility Policy / ADR-0031), 101 (Convention Stability), 104, 105. Foundation 0.7 ist nicht released und **nicht v1.0**.

## EN – Purpose

This plan collects the candidates for Foundation 0.7 (result of NDF-WP-097). It is **not a scope lock** — the scope only becomes binding with NDF-WP-098. Foundation 0.7 is not released and **not v1.0**.

## DE – Ausgangslage nach Foundation 0.6

`v0.6.0-foundation` ist veröffentlicht (2026-07-07), Foundation 0.6 ist vollständig abgeschlossen. Übernommene 0.7-Kandidaten aus WP-094/095/096:

1. **v1.x-Kompatibilitätszusage** — im v1.0-Draft das letzte klar `not met` blocking-Kriterium; natürlicher ADR-0031-Kandidat (aus WP-093/WP-079).
2. **Konventions-Stabilität** — v1.0-Kriterium aktuell `partially met` (Adapter-Konventionen seit 0.4 über 0.5/0.6 unverändert = drei Releases); eine Stability Review kann das Richtung `met` heben.
3. **External Validation Evidence Depth** — WP-088 war PASS WITH NOTES; PSV-001: per-Schritt-Belege nicht vollständig. Ein detaillierterer öffentlicher Lauf mit ausgefülltem Feedback-Template könnte volles PASS / `met` bringen.
4. **WP-091 Checklist DE/EN** — seit 0.4 mehrfach optional offen; **kein viertes stilles Verschieben** — 0.7 entscheidet.
5. **WP-092 Academy Entry** — optional offen; entscheiden oder bewusst deferred.
6. **Public Quality Gate operational note (QGM-003)** — kein Blocker; höchstens Monitoring-/Doku-Punkt.
7. **Doku-/i18n-Konsolidierung** — Website/volle i18n bleiben deferred; kleine Konsolidierung optional.
8. **Optionaler v0.6-Release-Body-Polish** — kosmetisch, manueller Human-Maintainer-Punkt, keine GitHub-Schreibaktion in NDF.

## EN – Starting Point After Foundation 0.6

`v0.6.0-foundation` is published (2026-07-07), Foundation 0.6 fully complete. The 0.7 candidates carried over from WP-094/095/096 are listed above — most importantly the v1.x compatibility promise (the last clearly `not met` blocking v1.0 criterion), convention stability (`partially met`), external validation evidence depth (PSV-001), and the WP-091 checklist decision (no fourth silent deferral).

## DE – Arbeitstitel

**Foundation 0.7 – v1.0 Path Consolidation & Compatibility Governance** (v1.0-Pfad-Konsolidierung und Kompatibilitäts-Governance). Nur Arbeitstitel — der Scope Lock (WP-098) bestätigt oder ändert ihn. Foundation 0.7 ist **nicht v1.0** und kein v1.0 Release Candidate.

## EN – Working Title

**Foundation 0.7 – v1.0 Path Consolidation & Compatibility Governance.** Working title only — the scope lock (WP-098) confirms or changes it. Foundation 0.7 is **not v1.0** and no v1.0 release candidate.

## DE – Planungsziel

Foundation 0.7 soll den v1.0-Pfad **konsolidieren** statt v1.0 zu behaupten: die verbleibenden offenen v1.0-Kriterien so weit wie ehrlich möglich schließen (Kompatibilitätszusage entwerfen, Konventions-Stabilität bestätigen, Validierungstiefe erhöhen) und die seit 0.4 mitgeschleppte Checklist-DE/EN-Frage endgültig entscheiden. Je ein Kern-Deliverable pro Titel-Hälfte — bewährtes Muster aus 0.4/0.5/0.6.

## EN – Planning Goal

Foundation 0.7 should **consolidate** the v1.0 path instead of claiming v1.0: close the remaining open v1.0 criteria as honestly as possible (draft the compatibility promise, confirm convention stability, deepen validation evidence) and finally decide the checklist DE/EN question carried since 0.4. One core deliverable per title half — the established 0.4/0.5/0.6 pattern.

## DE – Kandidatenthemen

Vollständige Bewertungsmatrix (Warum / 0.7-Fit / v1.0-Relevanz / Risiko bei erneutem Verschieben / Status / WP / blocking): [FOUNDATION_0_7_WORK_PACKAGES.md](FOUNDATION_0_7_WORK_PACKAGES.md) und `project-brain/WP_097_FOUNDATION_0_7_PLANNING_NOTES.md`.

## EN – Candidate Topics

Full evaluation matrix (why / 0.7 fit / v1.0 relevance / risk if deferred again / status / WP / blocking) in the work package candidates document and the WP-097 brain note.

## DE – Vorgeschlagener Kernfokus

| Priorität (Vorschlag) | Thema |
|---|---|
| P1 | Scope Lock (WP-098) |
| P1 | **Compatibility Governance:** v1.x Compatibility Policy Decision / ADR-0031 Preparation (WP-100) |
| P1 | **v1.0 Path Consolidation:** Project Adapter Convention Stability Review (WP-101) |
| P1 | Checklist DE/EN Decision — priorisieren, optional-mit-Begründung oder streichen (WP-099) |
| P2 | External Validation Evidence Depth Pass (WP-102) — kann von WP-098 blocking gemacht werden |
| P2 | Academy Entry Decision (WP-103) |
| Release | Release Readiness (WP-104) + Release Prep (WP-105) |

## EN – Proposed Core Focus

Same as above: P1 = scope lock, v1.x compatibility policy / ADR-0031 (governance half), convention stability review (consolidation half), checklist DE/EN decision; P2 = external validation evidence depth pass (upgradable to blocking by WP-098), academy entry decision; release track at the end.

## DE – Vorgeschlagene Nicht-Ziele

- Kein v1.0-Release, kein v1.0 Release Candidate, keine v1.0-Reife-Behauptung — 0.7 **konsolidiert den v1.0-Pfad**, mehr nicht.
- Kein v1.0 Scope Lock (das ist ein eigener späterer Zyklus).
- Kein großer Rewrite; keine neuen Großkonzepte ohne Scope-Review.
- Keine vollständige Doku-Website, keine Export-Pipeline, keine CLI.
- Keine vollständige i18n-Abdeckung; keine ADR-Massenmigration.
- Keine Integration realer privater Projekte; Neutralität bleibt Invariante.

## EN – Proposed Non-Goals

No v1.0 release, release candidate, or maturity claim — 0.7 **consolidates the v1.0 path**, nothing more; no v1.0 scope lock (a later dedicated cycle); no big rewrite; no full documentation website, export pipeline, or CLI; no full i18n; no ADR mass migration; no integration of real private projects.

## DE – Risiken

1. **WP-091 wird zum vierten Mal verschoben** — Gegenmittel: WP-099 ist als Entscheidungs-WP angelegt (priorisieren / optional-mit-Begründung / streichen), kein Verschieben zulässig.
2. **v1.x-Kompatibilitätspolicy klingt nach v1.0-Zusage** — Gegenmittel: als Draft/Policy führen (wie v1.0-Kriterien-Draft), keine Termine, kein Release Candidate.
3. **External-Validation-Tiefe erneut personenabhängig** — WP-098 sollte prüfen, ob WP-102 blocking wird und ob ein Ventil analog 0.5/0.6 nötig ist.
4. **Kandidatenliste verleitet zu Scope Creep** — WP-098 hält den blocking Kern klein.
5. **Ein-Personen-Engpass** — unverändert; kleine WPs halten Reviews machbar.

## EN – Risks

(1) WP-091 deferred a fourth time — WP-099 is a decision work package (prioritize / keep-optional-with-rationale / drop), no deferral allowed. (2) The v1.x compatibility policy could read as a v1.0 promise — treat it as a draft/policy, no dates, no release candidate. (3) External validation depth is again person-dependent — WP-098 should decide whether WP-102 becomes blocking and whether a valve analogous to 0.5/0.6 is needed. (4) The candidate list invites scope creep — WP-098 keeps the blocking core small. (5) Single-person bottleneck — unchanged.

## DE – Entscheidungspunkte für den Scope Lock

WP-098 muss klären: (a) finale blocking/optional/deferred-Einstufung; (b) ob WP-102 (Evidence Depth) blocking wird — und falls ja, mit welchem Ventil; (c) WP-099-Entscheidungskorridor (priorisieren / optional-mit-Begründung / streichen) verbindlich machen; (d) ob WP-100 die v1.x-Policy als ADR-0031 entwirft oder nur als Policy-Dokument; (e) Änderungsregeln.

## EN – Scope Lock Decision Points

WP-098 must settle: (a) final blocking/optional/deferred classification; (b) whether WP-102 becomes blocking and with what valve; (c) making the WP-099 decision corridor binding; (d) whether WP-100 drafts the v1.x policy as ADR-0031 or only as a policy document; (e) change rules.

## DE – Erwarteter nächster Schritt

**NDF-WP-098 – Foundation 0.7 Scope Lock.** Kein inhaltliches WP startet vorher.

## EN – Expected Next Step

**NDF-WP-098 – Foundation 0.7 scope lock.** No content work package starts before it.
