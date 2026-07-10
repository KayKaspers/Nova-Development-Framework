# v1.0 Gap Review & Scope Lock

## DE – Titel

v1.0 Gap Review & Scope-Lock-Prüfung nach Foundation 0.9 und dem docs-only Skills-Ausbau (NDF-WP-139, Skill-assisted Full Prompt Mode).

## DE – Status / Ergebnis

**GO WITH NOTES – v1.0 scope lock candidate.** Der v1.0-**Scope** kann als Kandidat gelockt werden (die 12-Kategorien-Kriterienbasis ist stabil und umfassend); der v1.0-**Release** ist **nicht** freigegeben. Foundation 0.9 bleibt released/published, **nicht v1.0**, kein v1.0 RC, ohne aktive volle v1.x-Zusage. ADR-0031 und ADR-0032 bleiben bindend und unverändert. Das achtteilige Skill-Pack reicht für den v1.0-**Core-Arbeitsmodus**; weitere Skills bleiben optional/post-v1.0, sofern External Validation keinen Bedarf zeigt.

## EN – Status / Result

**GO WITH NOTES – v1.0 scope lock candidate.** The v1.0 **scope** can be locked as a candidate (the 12-category criteria base is stable and comprehensive); the v1.0 **release** is **not** approved. Foundation 0.9 stays released/published, **not v1.0**, no v1.0 RC, no active full v1.x promise. ADR-0031 and ADR-0032 stay binding and unchanged. The eight-skill pack suffices for the v1.0 **core way of working**; further skills stay optional/post-v1.0 unless external validation shows a need.

## DE – Scope

Ehrlicher Abgleich des aktuellen Stands gegen die v1.0-Erwartungen; Identifikation offener Gaps; Scope-Lock-Empfehlung; Definition der WPs vor einem `v1.0.0-rc.1`; Skills-vor-v1.0-Bewertung; Neubewertung der External-Validation-Evidenz-Tiefe; klare nächste WP-Empfehlung. **Nicht im Scope:** v1.0-Aktivierung, v1.0 RC, volle v1.x-Zusage, neue/geänderte Skills, Scripts, Netzwerk, Commit/Push/Tag/Release.

## EN – Scope

Honest comparison of the current state against v1.0 expectations; identification of open gaps; scope-lock recommendation; definition of the WPs before a `v1.0.0-rc.1`; skills-before-v1.0 assessment; re-assessment of external-validation evidence depth; a clear next-WP recommendation. Out of scope: v1.0 activation, v1.0 RC, full v1.x promise, new/changed skills, scripts, network, commit/push/tag/release.

## DE – Input Summary

Ausgewertet: die [v1.0 Readiness Criteria Draft](../../release/V1_0_READINESS_CRITERIA_DRAFT.md) (12 Kategorien, WP-079ff.), die [v1.0 Path Summary](../../roadmap/V1_0_PATH_SUMMARY.md), die [Adoption Evidence and v1.0 Path Review](../foundation-0-9/ADOPTION_EVIDENCE_AND_V1_0_PATH_REVIEW.md) (WP-126), die Skills-first-Artefakte (WP-125–138), die acht Skills (`.claude/skills/`), [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md) und [ADR-0032](../../adr/ADR-0032-skill-security-policy.md).

## EN – Input Summary

Reviewed: the v1.0 readiness criteria draft (12 categories), the v1.0 path summary, the WP-126 adoption/v1.0-path review, the skills-first artifacts (WP-125–138), the eight skills, ADR-0031, and ADR-0032.

## DE – v1.0-Gap-Matrix

Status: **Met** · **Met with notes** · **Gap** · **Blocker** · **N/A**. Grundlage: der Kriterien-Entwurf plus der Skills-first-Strang.

| ID | Bereich | v1.0-Erwartung | Aktueller Stand | Status | Evidence / Notes | Empfohlene Aktion |
|---|---|---|---|---|---|---|
| G-01 | Scope / Scope Lock | v1.0-Kriterien als verbindliche Zielbasis lockbar | 12-Kategorien-Entwurf stabil, umfassend, ehrlich | **Met with notes** | Criteria Draft (WP-079) | im v1.0-Zyklus verbindlich locken (WP-141) |
| G-02 | Work-Package-Prozess | reproduzierbarer WP-Zyklus | über viele Releases praktiziert | **Met** | Release-Muster, WP-Notes | — |
| G-03 | Prompt Modes | Full/Standard/Short klar begrenzt | validiert (WP-123), skill-assisted bestätigt (WP-134/138) | **Met** | Prompt Modes, Operating Mode | — |
| G-04 | Context Packs | aktuell, wiederverwendbar | Template + 0.9-Pack gepflegt | **Met** | Context Pack, `ndf-context-pack-maintainer` | — |
| G-05 | Compact Context Summary | Pflicht-Handover-Baustein | praktisch adoptiert (WP-122), skill-getragen | **Met** | `ndf-compact-context-summary-runner` | — |
| G-06 | Skills-first Operating Mode | Arbeitsmodus definiert und validiert | dokumentiert (WP-134), real-use-validiert (WP-138) | **Met with notes** | Operating Mode, Real-use Validation | ECS-001 breiter belegen (post-RC ok) |
| G-07 | Public Neutrality | Gate grün, keine privaten Bezüge | Invariante, Gate v0.2 grün | **Met** | Gate strict/self-test | — |
| G-08 | ADR Governance | ADR-Policy entschieden, stabil | Policy adopted (WP-086); ADR-0031/0032 accepted | **Met with notes** | `ADR_POLICY.md`, ADR-0031/0032 | Massenmigration bleibt deferred |
| G-09 | Release Governance | Release-Muster über ≥3 Releases | mehrfach praktiziert; 0.9 reconciled (WP-133) | **Met** | Release-Docs, Reconciliation Notes | — |
| G-10 | Human-Maintainer-only-Regel | nur Mensch committet/taggt/released | durchgängig praktiziert | **Met** | Gates, WP-Notes | — |
| G-11 | v1.x Compatibility Policy | Zusage-Rahmen definiert | ADR-0031 accepted; aktive Zusage erst mit v1.0 | **Met with notes** | ADR-0031 | im v1.0 Scope Lock aktivieren |
| G-12 | Skill Security Policy | fail-closed, docs-only | ADR-0032 accepted; Pack docs-only/fail-closed | **Met** | ADR-0032, Skill-Validationen | — |
| G-13 | External Validation Evidence | ≥1 unabhängiger Lauf, ausreichende Tiefe | 1 öffentlicher Lauf (WP-088, PASS WITH NOTES); Schrittbeleg-Tiefe begrenzt | **Gap (tracked)** | Criteria Kat. 2 | WP-140 Evidence Review vor RC |
| G-14 | Documentation Completeness | Kern-Docs DE/EN nutzbar, ehrliche Matrix | Kern-Docs met; Vollübersetzung Nicht-Ziel | **Met with notes** | Translation Status, Workflow-Docs | Randbestand-Entscheidungslogik prüfen |
| G-15 | Changelog / Release Notes | vollständig, ehrlicher Status | pro Release gepflegt; `ndf-changelog-writer` unterstützt | **Met** | `CHANGELOG.md` | — |
| G-16 | Project Adapter / Project Enablement | Konventions-Stabilität; Onboarding-Pfad | Stabilität bestätigt (WP-101); Enablement-Skills nicht umgesetzt | **Met with notes** | Stability Review, `ndf-existing-project-analysis-runner` | Project-Enablement optional/post-v1.0 |
| G-17 | Sample / Neutral Validation | Adapter gegen neutrales Fixture | PASS WITH NOTES (WP-047); Grenzen dokumentiert | **Met with notes** | SampleProject Validation | zweiter Fixture-Typ offen (Non-Goal/tracked) |
| G-18 | Risk Register / Known Notes | offene Notes ehrlich geführt | DSK-001 closed w/ notes, ECS-001 partially closed; Ein-Personen-Risiko dokumentiert | **Met with notes** | WP-138 Validation, Plan-Risiken | im RC-Pfad fortführen |

**Zusammenfassung:** Met: G-02/03/04/05/07/09/10/12/15 (9). Met with notes: G-01/06/08/11/14/16/17/18 (8). Gap (tracked): G-13 (1). **Blocker: keine.**

## EN – v1.0 Gap Matrix

The table maps 18 areas to v1.0 expectation, current state, status (Met / Met with notes / Gap / Blocker / N/A), evidence, and recommended action, grounded in the criteria draft and the skills-first strand. Summary: 9 Met, 8 Met with notes, 1 tracked Gap (G-13 external-validation evidence depth), **no blockers**.

## DE – v1.0-Scope-Lock-Prüfung

**Scope Lock recommended with notes.** Begründung: Die 12-Kategorien-Kriterienbasis ist stabil, umfassend und ehrlich; es gibt **keine Blocker**, nur ein getracktes Gap (G-13) und acht `met with notes`. Der v1.0-**Scope** (welche Kriterien v1.0 verbindlich fordert) kann daher als **Kandidat** gelockt werden — die verbindliche Fixierung erfolgt im dedizierten v1.0-Zyklus (WP-141). **Wichtig:** Scope Lock ≠ v1.0-Freigabe; die `met with notes`/`Gap`-Punkte müssen vor einem RC geschlossen oder ausdrücklich als Non-Goal bestätigt werden.

## EN – v1.0 Scope Lock Assessment

**Scope Lock recommended with notes.** The 12-category criteria base is stable, comprehensive, and honest; there are **no blockers**, only one tracked gap (G-13) and eight `met with notes`. The v1.0 **scope** can be locked as a **candidate** — the binding fixation happens in the dedicated v1.0 cycle (WP-141). Scope lock ≠ v1.0 approval; the `met with notes`/`gap` items must be closed or explicitly confirmed as non-goals before an RC.

## DE – v1.0-RC-Voraussetzungen

Vor einem möglichen `v1.0.0-rc.1` nötig:

| WP-Kandidat | Zweck | Notwendigkeit |
|---|---|---|
| External Validation Evidence Review | G-13 schließen oder als tracked/Non-Goal bestätigen (Schrittbeleg-Tiefe, ggf. zweiter Lauf/Sprache) | **erforderlich** |
| v1.0 Release Criteria Finalization | Kriterien-Entwurf → verbindlicher, gelockter v1.0-Scope | **erforderlich** |
| v1.0 RC Readiness Review | ehrlicher Gesamt-Check gegen die gelockten Kriterien | **erforderlich** |
| v1.0 RC Release Prep | RC-Notes/Go-No-Go/Tagging-Guide (nur Doku, Freigabe durch Human Maintainer) | **erforderlich** |
| Additional Governance Skills (`ndf-release-safety`, `ndf-adr-governance-review`) | Release-/ADR-Struktur | **optional** (kein Blocker; ggf. innerhalb RC-Pfad) |
| Project Enablement Skills | Projekt-Onboarding-Skills | **optional / post-v1.0** |
| Docs Polish / Readme Review | Doku-Feinschliff | **optional** |

## EN – v1.0 RC Prerequisites

Before a possible `v1.0.0-rc.1`: external validation evidence review (close/confirm G-13) — required; v1.0 release criteria finalization (draft → binding locked scope) — required; v1.0 RC readiness review — required; v1.0 RC release prep (docs only, human-maintainer approval) — required. Additional governance skills, project-enablement skills, and docs polish stay optional/post-v1.0.

## DE – Skills-vor-v1.0-Bewertung

- **Reicht das achtteilige Skill-Pack für v1.0?** **Ja, für den v1.0-Core-Arbeitsmodus.** Es trägt Rahmen, Neutralität, Abschlussblöcke, Context-Pack-Pflege, Skill-Qualität, Docs-/Changelog-Konsistenz und Bestandsprojekt-Analyse — validiert (WP-138).
- **`ndf-release-safety` / `ndf-adr-governance-review` vor v1.0 nötig?** **Nein, optional.** Release-/ADR-Governance ist bereits über Prozesse und ADR-0031/0032 abgedeckt; die Skills würden nur strukturieren. Sie können optional im RC-Pfad ergänzt werden.
- **Project-Enablement-Skills vor v1.0 nötig?** **Nein, post-v1.0**, sofern External Validation keinen Bedarf zeigt.
- **Fazit:** *Das achtteilige Skill-Pack reicht für v1.0-Core; weitere Skills bleiben optional oder post-v1.0, sofern External Validation keinen Bedarf zeigt.*

## EN – Skills-before-v1.0 Assessment

The eight-skill pack suffices for the v1.0 core way of working (validated in WP-138). `ndf-release-safety` / `ndf-adr-governance-review` are optional (governance already covered by process + ADR-0031/0032). Project-enablement skills stay post-v1.0 unless external validation shows a need. Conclusion: the eight-skill pack suffices for v1.0-core; further skills stay optional or post-v1.0.

## DE – External-Validation-Evidenz-Bewertung

**Bleibt Met with notes / Gap (tracked) — nicht geschlossen, kein Blocker.** Der Skills-first-Strang (WP-125–138) hat **keine** neue externe Validierung geliefert; er stärkt die Arbeitsweise/Effizienz, nicht die externe Evidenz-Tiefe. Ehrlich: es liegt weiterhin ein öffentlicher unabhängiger Lauf vor (WP-088, PASS WITH NOTES) mit begrenzter Schrittbeleg-Tiefe. **Empfohlene Aktion:** dedizierter External Validation Evidence Review (WP-140) vor einem RC — Tiefe erhöhen oder die Begrenzung ausdrücklich als tracked/Non-Goal bestätigen. Keine erfundene externe Evidenz.

## EN – External Validation Evidence Assessment

**Stays met with notes / tracked gap — not closed, not a blocker.** The skills-first strand added **no** new external validation; it strengthens the way of working, not evidence depth. Honestly: one public independent run remains (WP-088, PASS WITH NOTES) with limited per-step evidence. Recommended action: a dedicated external validation evidence review (WP-140) before an RC — increase depth or explicitly confirm the limit as tracked/non-goal. No invented external evidence.

## DE – Empfohlene nächste WPs

1. **WP-140 – External Validation Evidence Review** (G-13 schließen/bestätigen).
2. **WP-141 – v1.0 Release Criteria Finalization** (Kriterien verbindlich locken).
3. **WP-142 – v1.0 RC Readiness Review** (Gesamt-Check gegen gelockte Kriterien).
4. **WP-143 – v1.0 RC Release Prep** (RC-Notes/Go-No-Go/Tagging-Guide, nur Doku).

Optional/parallel und nicht blockierend: Additional Governance Skills, Project-Enablement-Skills, Docs Polish. **Begründung der Reihenfolge:** Evidenz vor Kriterien-Lock, Lock vor Readiness, Readiness vor Prep; Freigabe des RC bleibt beim Human Maintainer.

## EN – Recommended Next WPs

WP-140 (external validation evidence review) → WP-141 (v1.0 release criteria finalization) → WP-142 (v1.0 RC readiness review) → WP-143 (v1.0 RC release prep, docs only). Optional/non-blocking: additional governance skills, project-enablement skills, docs polish. Rationale: evidence before criteria lock, lock before readiness, readiness before prep; RC approval stays with the Human Maintainer.

## DE – Security / ADR-0031 / ADR-0032 Bewertung

ADR-0031 (v1.x Compatibility Policy) und ADR-0032 (Skill Security Policy) sind **ausreichend stabil** für den v1.0-Pfad und bleiben unverändert. Die aktive volle v1.x-Zusage tritt erst mit v1.0 in Kraft (im v1.0 Scope Lock zu aktivieren). Das Skill-Pack ist docs-only/fail-closed; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen. Nächste freie ADR-Nummer: 0033.

## EN – Security / ADR-0031 / ADR-0032 Assessment

ADR-0031 and ADR-0032 are **stable enough** for the v1.0 path and stay unchanged. The active full v1.x promise takes effect only at v1.0 (to be activated in the v1.0 scope lock). The skill pack is docs-only/fail-closed. Next free ADR number: 0033.

## DE – Risks / Open Notes

- **G-13 External Validation** bleibt der wichtigste offene Punkt vor einem RC (tracked, kein Blocker).
- **ECS-001** (Extended-Core-Skills) nur partially closed — breitere Real-use-Historie post-RC ok.
- **Ein-Personen-Engpass** dokumentiertes Risiko, strukturell nicht vor v1.0 lösbar.
- **Scope-Lock-Missverständnis:** Scope Lock lockt die Zielkriterien, nicht die v1.0-Freigabe.
- **Kein Zeitplan** — der v1.0-Pfad ist definiert, nicht terminiert.

## EN – Risks / Open Notes

G-13 external validation is the key open item before an RC (tracked, not a blocker); ECS-001 only partially closed (broader real-use history post-RC ok); single-person bottleneck is a documented, structurally-unsolvable-before-v1.0 risk; scope lock locks the target criteria, not the v1.0 approval; no schedule — the path is defined, not dated.

## DE – Decision

**GO WITH NOTES – v1.0 scope lock candidate.** Keine Blocker; ein getracktes Gap (G-13); Scope Lock als Kandidat empfohlen mit Notes; achtteiliges Skill-Pack reicht für v1.0-Core; External Validation bleibt vor RC zu vertiefen; v1.0/RC/volle v1.x-Zusage **nicht** aktiviert; ADR-0031/0032 unverändert; Foundation 0.9 bleibt nicht v1.0. **Nächster empfohlener WP: WP-140 – External Validation Evidence Review.**

## EN – Decision

**GO WITH NOTES – v1.0 scope lock candidate.** No blockers; one tracked gap (G-13); scope lock recommended as a candidate with notes; the eight-skill pack suffices for v1.0-core; external validation still to be deepened before an RC; v1.0/RC/full v1.x promise **not** activated; ADR-0031/0032 unchanged; Foundation 0.9 stays not v1.0. Next recommended WP: WP-140 – External Validation Evidence Review.
