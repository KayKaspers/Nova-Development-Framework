# v1.0 Readiness Criteria Draft

## DE – Zweck

Dieser Entwurf definiert messbare Kriterien, die erfüllt sein müssten, bevor NDF später ehrlich über einen v1.0-Release entscheiden kann. Er ist der Foundation-0.5-Beitrag zur Titel-Hälfte **1.0 Path Hardening** (NDF-WP-079).

## EN – Purpose

This draft defines measurable criteria that would have to be met before NDF can later decide honestly about a v1.0 release. It is Foundation 0.5's contribution to the **1.0 path hardening** half of the title (NDF-WP-079).

## DE – Status

**Draft.** NDF ist **nicht** v1.0. Foundation 0.5 ist **nicht** v1.0 und wird es nicht. Dieser Entwurf gibt nichts frei und ist kein Release Candidate — er ist die Messlatte, an der eine spätere v1.0-Entscheidung geprüft würde. Ein v1.0-Release bräuchte einen eigenen, späteren Zyklus: v1.0 Scope Lock → Umsetzung → Release Readiness → Release Prep → manuelle Freigabe durch den Human Maintainer.

## EN – Status

**Draft.** NDF is **not** v1.0; Foundation 0.5 is not and will not be v1.0. This draft approves nothing and is no release candidate — it is the yardstick against which a later v1.0 decision would be checked. A v1.0 release would need its own later cycle: v1.0 scope lock → implementation → release readiness → release prep → manual approval by the human maintainer.

## DE – Grundsatz

**v1.0 ist eine Vertrauensaussage an Externe:** „Dieses Framework kann von Unbeteiligten anhand der öffentlichen Dokumente sicher übernommen werden." Jedes Kriterium hier muss auf diese Aussage einzahlen und **prüfbar** sein (Nachweis-Spalte). Ehrliche Statuswerte: `met` · `partially met` · `not met` · `open` · `unknown` · `deferred`. Keine falschen Haken — ein `not met` ist Information, kein Makel.

## EN – Principle

**v1.0 is a trust statement to outsiders:** "this framework can be adopted safely by uninvolved people using the public documents alone." Every criterion must serve that statement and be **verifiable** (evidence column). Honest status values: `met` · `partially met` · `not met` · `open` · `unknown` · `deferred`. No false checkmarks — a `not met` is information, not a flaw.

## DE – Was dieser Draft ist

Eine öffentliche, ehrliche, messbare Kriterienbasis; eine Diskussionsgrundlage für Nova (ChatGPT) und den Human Maintainer; ein Instrument, um Fortschritt Richtung v1.0 sichtbar zu machen — inklusive der Punkte, die heute offen sind.

## EN – What This Draft Is

A public, honest, measurable criteria base; a discussion basis for Nova (ChatGPT) and the human maintainer; an instrument to make progress toward v1.0 visible — including what is open today.

## DE – Was dieser Draft nicht ist

Keine v1.0-Freigabe, kein Release Candidate, kein v1.0 Scope Lock, kein Zeitplan, kein Versprechen. Die Kriterien selbst können sich bis zum späteren v1.0 Scope Lock noch ändern (dann verbindlich).

## EN – What This Draft Is Not

No v1.0 approval, no release candidate, no v1.0 scope lock, no schedule, no promise. The criteria themselves may still change until the later v1.0 scope lock (which makes them binding).

## DE – Kriterienübersicht / EN – Criteria Overview

12 Kategorien; „Für v1.0 erforderlich?" unterscheidet **blocking** (muss erfüllt sein) und **tracked** (muss ehrlich dokumentiert sein, blockiert aber nicht). / 12 categories; "required for v1.0?" distinguishes **blocking** (must be met) and **tracked** (must be honestly documented, does not block).

| # | Kategorie / Category | Stand heute / Status today |
|---|---|---|
| 1 | Public Usability | partially met |
| 2 | External Validation | met with notes (öffentlicher Lauf bestätigt, WP-088; Nachweis-Tiefe begrenzt) |
| 3 | Project Adapter Maturity | met with notes (Konventions-Stabilität bestätigt, WP-101) |
| 4 | Documentation & DE/EN Readiness | partially met |
| 5 | Prompt & Checklist Readiness | partially met |
| 6 | Security & Destructive Action Safety | met (framework-seitig) |
| 7 | Public Quality Gate & Neutrality | met |
| 8 | Release Process & Versioning | met (v1.x-Kompatibilität: Governance-Rahmen `met with notes`, ADR-0031) |
| 9 | Governance & Human Maintainer Control | met |
| 10 | ADR / Decision Structure | met with notes (Policy adopted, WP-086) |
| 11 | Maintenance & Backlog Discipline | met |
| 12 | v1.0 Non-Goals / Boundaries | definiert in diesem Draft / defined in this draft |

## DE – Public Usability / EN – Public Usability

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| README ist zweisprachiger, ehrlicher Einstiegspunkt (Status, Links, keine falschen Claims) | blocking | met | `README.md` DE/EN-Statusblock je Foundation-Release | seit WP-036, laufend gepflegt |
| Adoptions-Erstkontakt-Prompts vollständig DE/EN nutzbar | blocking | met | `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md` (5 Prompts) | WP-060 |
| Ein externer Nutzer findet den Einstieg (README → Adapter → Beispiel) ohne Insider-Wissen | blocking | partially met | bestätigt durch unabhängige Sicht (Kategorie 2) | bisher nur Selbstprüfung |
| Academy-/Lernpfad-Einstieg vorhanden | tracked | not met | Academy Band 1 Entry (WP-077, optional in 0.5) | blockiert v1.0 nicht, muss aber ehrlich benannt sein |

## DE – External Validation / EN – External Validation

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Mindestens **ein** unabhängiger Adapter-Validierungslauf durchgeführt und ausgewertet | **blocking** | **met with notes** | Auswertungsberichte unter `docs/validation/project-adapter/independent-runs/` | WP-074 (privater Referenzkontext, PASS WITH NOTES) **+ WP-088: öffentliche SampleProject-Runbook-Validierung unabhängig positiv bestätigt** (`2026-07-07-public-sampleproject-runbook-validation/`), keine Blocker/High-Findings. Note: Schrittbelege in der neutralisierten Rückmeldung begrenzt (evidence-quality note, tracked). Kein v1.0-Claim |
| Findings aus unabhängiger Validierung triagiert (umgesetzt oder begründet offen) | blocking | met | Folge-WPs bzw. begründete Backlog-Einträge | für den 2026-07-06-Lauf: keine Blocker/High-Findings; 2 Info-Findings dokumentiert und als tracked eingestuft |
| Validierungsunterlagen (Runbook, Brief, Templates) öffentlich und neutral | blocking | met | `docs/validation/project-adapter/INDEPENDENT_*.md` | WP-073 |

## DE – Project Adapter Maturity / EN – Project Adapter Maturity

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Adapter-Konventionen stabil (Manifest, Output-Pfade, Health-Score) über ≥ 2 Releases unverändert oder nur additiv | blocking | **met with notes** | `docs/validation/project-adapter/PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md` (NDF-WP-101) | Konventionen seit WP-059 (0.4) unverändert über 0.4→0.7 (4 Releases); Note: künftige Änderungen governed über ADR-0031, volle v1.x-Zusage erst mit v1.0 |
| Adapter praktisch validiert gegen neutrales Fixture | blocking | met | `SAMPLEPROJECT_ADAPTER_VALIDATION.md` (PASS WITH NOTES) | WP-047; Selbstvalidierung — Ergänzung durch Kategorie 2 |
| Grenzen dokumentiert (kein echter Code im Fixture, Monorepo/Teams > 10 nicht abgedeckt) | tracked | met | „Grenzen der Validierung" im Validierungsdokument | ehrlich dokumentiert seit WP-047 |
| Adapter-Backlog leer oder jeder Punkt begründet offen | blocking | partially met | `PROJECT_ADAPTER_V0_2_IMPROVEMENT_BACKLOG.md` | Punkte 1–5 addressed; Punkt 6 prepared, Lauf offen |

## DE – Dokumentation und DE/EN-Reife / EN – Documentation and DE/EN Readiness

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Kern-Workflow-Dokumente DE/EN nutzbar | blocking | met | Workflow-Docs (WP-038), README (WP-036) | |
| Übersetzungsstand ehrlich geführt (keine behauptete Vollständigkeit) | blocking | met | `docs/i18n/TRANSLATION_STATUS.md` | Matrix seit WP-035 |
| Vollständige Zweisprachigkeit der gesamten Bibliothek | **nicht erforderlich / not required** | not met | — | bewusst kein v1.0-Kriterium: ehrliche Matrix genügt; Vollübersetzung wäre Wunschliste |
| Checklisten-Kernbestand DE/EN nutzbar | tracked | not met | Checklist DE/EN Pass (WP-075, optional in 0.5) | |

## DE – Prompt- und Checklisten-Reife / EN – Prompt and Checklist Readiness

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Prompt-Index vollständig und aktuell | blocking | met | `docs/prompts/` Index (WP-035) | |
| Adoptions-Prompts voll bilingual, Security-/Gate-Prompts mindestens DE/EN-Kern | blocking | met | Priority-Pass-Dokument (WP-060) | |
| Jeder Prompt endet mit klarer Entscheidungslogik (GO/GO WITH NOTES/REWORK/STOP o. Ä.) | blocking | partially met | Stichprobe über `framework/prompts/` | Kern-Prompts ja; vollständige Prüfung steht aus (unknown für Randbestand) |
| Checklisten decken Release-, Security- und Adapter-Strecke ab | tracked | met | `framework/checklists/` | DE/EN-Stand siehe Kategorie 4 |

## DE – Security und Destructive-Action-Safety / EN – Security and Destructive Action Safety

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Destructive-Action-Muster vorhanden (Blueprint → Review → Gate → Test) | blocking | met | `framework/prompts/security/DESTRUCTIVE_ACTION_*.md` (WP-028) | |
| Security-Prompt-Bibliothek vorhanden und verlinkt | blocking | met | `framework/prompts/security/` (WP-029) | |
| Read-only-Grundsatz für Analyse-Phasen dokumentiert | blocking | met | Adapter Phasen 0–1, Runbook | |
| Framework selbst enthält keine ausführbare Angriffsfläche (Doku-Framework, nur Gate-Skript) | blocking | met | Repo-Struktur; einziges Skript: `scripts/check_public_quality.py` | Skript wird per Self-Test geprüft |

## DE – Public Quality Gate und Neutralität / EN – Public Quality Gate and Neutrality

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Gate strict + self-test grün auf dem Release-Commit | blocking | met | lokale Läufe + CI-Action | Invariante seit 0.2 |
| New-file neutrality check aktiv (auch untracked Dateien) | blocking | met | Gate v0.2 (WP-052) | Antwort auf den WP-040-Vorfall |
| Custom-Denylist-Secret gesetzt und als gepflegt dokumentiert | blocking | met | `NDF_PUBLIC_NEUTRALITY_DENYLIST` verifiziert (WP-070); CI-Denylist-Wirksamkeit bewertet: **Evidence-Level strong** (WP-089, `docs/quality/PUBLIC_QUALITY_GATE_MAINTENANCE_REVIEW.md`) | Prüfpunkt geschlossen; bei künftigen Gate-Reviews wiederholen |
| Keine privaten Projekt-/Personenbeispiele in öffentlichen Dateien | blocking | met | Kontroll-Greps + Gate | Invariante |

## DE – Release-Prozess und Versionierung / EN – Release Process and Versioning

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Release-Muster dokumentiert und über ≥ 3 Releases praktiziert (Planning → Scope Lock → Readiness → Prep → manueller Tag → Cleanup) | blocking | met | 0.2/0.3/0.4 vollständig durchlaufen | 0.5 wird vierter Durchlauf |
| Tags unveränderlich; ältere Foundations frozen | blocking | met | v0.1–v0.4-Tags nie verschoben | Invariante |
| Changelog vollständig pro Release, ehrlicher Status | blocking | met | `CHANGELOG.md` | |
| v1.0-Versionierungs-/Kompatibilitätszusage definiert (was bedeutet v1.x für Nutzer?) | blocking | **met with notes** | `docs/adr/ADR-0031-v1x-compatibility-policy.md` (Accepted, NDF-WP-100) | Governance-Rahmen angenommen (Kompatibilitätskategorien, Breaking-/Deprecation-Regeln, Aktivierungsschwelle); die **aktive** volle v1.x-Zusage tritt erst mit v1.0 in Kraft — bleibt v1.0-tracked |

## DE – Governance und Human-Maintainer-Kontrolle / EN – Governance and Human Maintainer Control

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Rollenmodell dokumentiert (Nova (ChatGPT) → Implementation Agent → Human Maintainer) | blocking | met | Workflow-/Rollen-Docs (WP-031/037) | |
| Nur der Human Maintainer committet, taggt, released | blocking | met | praktiziert über alle WPs; in Gates dokumentiert | |
| Jedes WP endet mit Review-Entscheidung (GO/GO WITH NOTES/REWORK/STOP) | blocking | met | WP-Notes im `project-brain/` | |
| Ein-Personen-Engpass als Risiko dokumentiert | tracked | met | Plan-/Scope-Lock-Risikoabschnitte | strukturell nicht lösbar vor v1.0, aber ehrlich benannt |

## DE – ADR- und Entscheidungsstruktur / EN – ADR and Decision Structure

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| ADR-Policy entschieden (Nummernraum, Ablageort, Altbestand) **oder** als Known Limitation mit Regel dokumentiert | blocking | **met with notes** | `docs/adr/ADR_POLICY.md` (NDF-WP-086, 2026-07-07: Minimal ADR Policy adopted) | Notes: Massenmigration bleibt deferred; die Policy muss sich in künftigen WPs bewähren |
| Nummernkollisionen im Altbestand aufgelöst oder als frozen dokumentiert | tracked | partially met | Struktur-Review (WP-033) | dokumentierter Altbestand |

## DE – Maintenance- und Backlog-Disziplin / EN – Maintenance and Backlog Discipline

| Kriterium / Criterion | Für v1.0? / Required? | Stand / Status | Nachweis / Evidence Needed | Hinweise / Notes |
|---|---|---|---|---|
| Backlogs mit ehrlichem Status je Punkt (addressed/later/prepared) | blocking | met | Adapter-Backlog u. a. | |
| Kein stilles Mehrfach-Verschieben (Priorisieren-oder-Streichen-Regel) | blocking | met | WP-076-Sonderregel im 0.5 Scope Lock | Muster für künftige Dauerläufer |
| Post-Release-Cleanup nach jedem Release (kein veralteter „pending"-Status in Einstiegspunkten) | blocking | met | WP-043/056/069-Muster | |
| Manuelle Follow-ups werden geschlossen und verifiziert dokumentiert | blocking | met | WP-070-Muster | |

## DE – v1.0-Nicht-Ziele / EN – v1.0 Non-Goals

Diese Punkte sind **ausdrücklich keine** v1.0-Voraussetzungen — sie dürfen einen v1.0-Release nicht implizit blockieren:

- Vollständige Übersetzung des gesamten Repositories (ehrliche Matrix genügt)
- Website, Export-Pipeline, CLI oder sonstige Tooling-Automatisierung (Konzepte genügen)
- Vollständig ausgearbeitete Academy
- ADR-Massenmigration (Policy-Entscheidung genügt, siehe Kategorie 10)
- Multi-Maintainer-Governance (Ein-Personen-Modell ist dokumentiertes Risiko, kein Blocker)
- Abdeckung von Monorepos/großen Teams durch den Adapter (dokumentierte Grenze)

These are **explicitly not** v1.0 prerequisites and must not implicitly block a v1.0 release: full repository translation (an honest matrix suffices); website/export pipeline/CLI (concepts suffice); a fully written academy; bulk ADR migration (the policy decision suffices); multi-maintainer governance (the single-person model is a documented risk, not a blocker); adapter coverage of monorepos/large teams (a documented limit).

## DE – Offene Fragen / EN – Open Questions

1. Reicht **ein** unabhängiger Validierungslauf für v1.0, oder braucht es Läufe in beiden Sprachen (DE und EN)? / Is **one** independent run enough, or one per language?
2. Was genau verspricht v1.x an Kompatibilität (Struktur? Prompts? Konventionen?) — zu klären im v1.0 Scope Lock. / What exactly does v1.x promise in compatibility — to be settled in the v1.0 scope lock.
3. Braucht v1.0 einen zweiten neutralen Fixture-Typ (z. B. Projekt mit Code) oder bleibt das dokumentierte Grenze? / Does v1.0 need a second fixture type (with code), or does that stay a documented limit?
4. Wer außer dem Human Maintainer könnte eine v1.0-Go/No-Go-Zweitmeinung geben (z. B. der Independent Validator)? / Who besides the maintainer could give a v1.0 second opinion?

## DE – Nächste Schritte / EN – Next Steps

1. Foundation 0.5 regulär abschließen: WP-074 (Lauf oder Ventil) → optionale WPs → WP-081 → WP-082. / Complete Foundation 0.5: WP-074 (run or valve) → optional WPs → WP-081 → WP-082.
2. Offene v1.0-Kriterien (External Validation, ADR-Policy, Versionierungszusage) über 0.5/0.6-WPs schließen. / Close the open v1.0 criteria via 0.5/0.6 work packages.
3. Erst danach: eigener v1.0-Zyklus mit Scope Lock, der diese Kriterien verbindlich macht. Kein Zeitplan in diesem Draft. / Only then: a dedicated v1.0 cycle whose scope lock makes these criteria binding. No schedule in this draft.
