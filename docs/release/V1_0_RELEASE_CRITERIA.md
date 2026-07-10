# v1.0 Release Criteria (Finalized for the RC Path)

## DE – Zweck

Finalisierte v1.0 Release Criteria für den kommenden RC-Pfad (NDF-WP-141, Skill-assisted Full Prompt Mode). Baut auf dem [v1.0 Readiness Criteria Draft](V1_0_READINESS_CRITERIA_DRAFT.md), dem [v1.0 Gap Review & Scope Lock](../validation/v1-0/V1_0_GAP_REVIEW_AND_SCOPE_LOCK.md) (WP-139) und dem [External Validation Evidence Review](../validation/v1-0/EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md) (WP-140) auf. Es trennt **RC-Kriterien** von **Final-Kriterien**, legt zulässige **RC-Notes** und **Final-Blocker** fest und dokumentiert die **G-13-Schwelle**. **Dieses WP erstellt keinen RC und aktiviert v1.0 nicht.**

## EN – Purpose

Finalized v1.0 release criteria for the upcoming RC path (NDF-WP-141). Builds on the v1.0 readiness criteria draft, the v1.0 gap review & scope lock (WP-139), and the external validation evidence review (WP-140). It separates **RC criteria** from **final criteria**, defines allowed **RC notes** and **final blockers**, and documents the **G-13 threshold**. **This WP creates no RC and does not activate v1.0.**

## DE – Status / Ergebnis

**GO WITH NOTES.** Kriterien finalisiert; RC- und Final-Kriterien klar getrennt; G-13-Schwelle festgelegt (RC can proceed with notes; v1.0 final: tiefere Evidence **oder** dokumentierte akzeptierte Grenze). Foundation 0.9 bleibt released/published, **nicht v1.0**, kein RC, keine volle v1.x-Zusage. ADR-0031/0032 unverändert. Dies ist der **Kriterien-Lock** des v1.0-Scope-Lock-Kandidaten (WP-139) — kein v1.0-Claim.

## EN – Status / Result

**GO WITH NOTES.** Criteria finalized; RC and final criteria clearly separated; G-13 threshold set (RC can proceed with notes; v1.0 final: deeper evidence **or** a documented accepted boundary). Foundation 0.9 stays released/published, **not v1.0**, no RC, no full v1.x promise. ADR-0031/0032 unchanged. This is the **criteria lock** of the v1.0 scope-lock candidate (WP-139) — no v1.0 claim.

## DE – Grundsatz

v1.0 ist eine Vertrauensaussage an Externe. Ein **RC** (`v1.0.0-rc.1`) ist ausdrücklich ein **Kandidat** mit sichtbaren Notes und darf selbst als Validierungsvehikel dienen; das **finale v1.0** (`v1.0.0`) muss stärker sein. Ehrliche Statuswerte, keine falschen Haken. Verbindliche Einstufung mit dem v1.0 Scope Lock (dieses Dokument macht die Kriterien für den RC-Pfad verbindlich).

## EN – Principle

v1.0 is a trust statement to outsiders. An RC (`v1.0.0-rc.1`) is explicitly a candidate with visible notes and may itself serve as a validation vehicle; the final v1.0 (`v1.0.0`) must be stronger. Honest status values, no false checkmarks. This document makes the criteria binding for the RC path.

## DE – v1.0 RC Criteria (müssen für `v1.0.0-rc.1` erfüllt sein)

| # | Kriterium | Status heute | Nachweis |
|---|---|---|---|
| RC-01 | Public Quality Gate v0.2 `--strict` + `--self-test` grün auf dem RC-Commit | met | Gate-Läufe + CI |
| RC-02 | New-file neutrality check aktiv; keine privaten Daten/Secret-Werte/Reviewer-Identitäten in Public NDF | met | Gate v0.2, Kontroll-Greps |
| RC-03 | README zweisprachiger, ehrlicher Einstiegspunkt (Status, Links, keine falschen Claims) | met | `README.md` |
| RC-04 | Kern-Workflow-/Adoptions-/Security-Prompts DE/EN nutzbar; Prompt-Index aktuell | met | `docs/prompts/`, Priority-Pass |
| RC-05 | Release-Prozess dokumentiert und mehrfach praktiziert (Planning→Scope Lock→Readiness→Prep→manueller Tag→Cleanup) | met | 0.2–0.9 Release-Historie |
| RC-06 | Human-Maintainer-only-Regel (nur Mensch committet/taggt/released) | met | Gates, WP-Notes |
| RC-07 | ADR-Policy entschieden; ADR-0031 (v1.x-Kompatibilität) und ADR-0032 (Skill Security) accepted | met with notes | `ADR_POLICY.md`, ADR-0031/0032 |
| RC-08 | Mindestens ein unabhängiger Validierungslauf dokumentiert und ausgewertet | met with notes | WP-088 (öffentlich), WP-074 (privat-neutralisiert); [Evidence Review](../validation/v1-0/EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md) |
| RC-09 | Adapter-Konventionen stabil über ≥2 Releases (additiv, governed via ADR-0031) | met | WP-101 Stability Review |
| RC-10 | Changelog vollständig, ehrlicher Status; RC-Notes sichtbar dokumentiert | met | `CHANGELOG.md` |
| RC-11 | Jeder Prompt endet mit klarer Entscheidungslogik (Kern-Prompts); Randbestand tracked | met with notes | Stichprobe `framework/prompts/` |
| RC-12 | Skill-Pack docs-only/fail-closed; keine autonomen Git-/Release-Aktionen | met | ADR-0032, Skill-Validationen |
| RC-13 | v1.0-RC-Kriterien in sich konsistent; keine v1.0-Claims vor Freigabe | met | dieses Dokument |

**RC-Bedingung:** Alle RC-Kriterien `met` **oder** `met with notes` mit sichtbarer, akzeptierter Note. Kein RC-Kriterium darf `not met`/`gap` ohne dokumentierte akzeptierte Note sein.

## EN – v1.0 RC Criteria (must be met for `v1.0.0-rc.1`)

The table lists RC-01…RC-13 (gate green, neutrality, README, prompts, release process, human-maintainer-only, ADR policy/ADR-0031/0032, ≥1 independent run, adapter convention stability, changelog with visible RC notes, prompt decision logic, docs-only skill pack, criteria self-consistency). RC condition: every RC criterion `met` or `met with notes` with a visible accepted note; none may be `not met`/`gap` without a documented accepted note.

## DE – v1.0 Final Criteria (müssen für `v1.0.0` final erfüllt sein)

Zusätzlich zu allen RC-Kriterien:

| # | Kriterium | heute | Nachweis / Weg |
|---|---|---|---|
| F-01 | External Validation Evidence auf `met` **oder** dokumentierte akzeptierte Grenze (G-13-Schwelle) | met with notes / tracked | Weg A oder B (siehe G-13-Schwelle) |
| F-02 | Externer Nutzer findet den Einstieg (README→Adapter→Beispiel) ohne Insider-Wissen, unabhängig bestätigt | partially met | tieferer Lauf oder RC-Feedback |
| F-03 | Volle v1.x-Kompatibilitätszusage im v1.0 Scope Lock **aktiviert** (ADR-0031) | not yet (bewusst) | Aktivierung erst mit v1.0-Freigabe |
| F-04 | Prompt-Entscheidungslogik vollständig geprüft (auch Randbestand) **oder** Randbestand als Non-Goal dokumentiert | partially met | Vollprüfung oder dokumentierte Grenze |
| F-05 | RC-Feedback triagiert (umgesetzt oder begründet offen) | n/a (vor RC) | nach RC |
| F-06 | Alle RC-Notes entweder geschlossen oder ausdrücklich als akzeptierte v1.0-Grenze bestätigt | offen | v1.0 Final Readiness |
| F-07 | v1.0 Final Readiness Review + Release Prep durchlaufen, manuelle Human-Maintainer-Freigabe | n/a (später) | eigener Zyklus |

## EN – v1.0 Final Criteria (must be met for `v1.0.0` final)

In addition to all RC criteria: F-01 external validation on `met` or documented accepted boundary (G-13 threshold); F-02 external user entry independently confirmed; F-03 full v1.x promise activated in the v1.0 scope lock; F-04 prompt decision logic fully checked or the remainder documented as a non-goal; F-05 RC feedback triaged; F-06 all RC notes closed or explicitly accepted as v1.0 boundaries; F-07 v1.0 final readiness + release prep + manual human-maintainer approval.

## DE – Allowed RC Notes (im RC zulässig)

- **G-13 External Validation Evidence Depth** bleibt `tracked` (begrenzte Schrittbeleg-Tiefe; ein Lauf privat-kontextuell) — zulässig, solange sichtbar dokumentiert.
- **ECS-001** Extended-Core-Skill-Real-use-Historie `partially closed` — zulässig.
- **Keine volle v1.x-Zusage vor finalem v1.0** — der RC aktiviert sie nicht.
- **RC ist kein finaler v1.0** — ausdrücklich als Kandidat gekennzeichnet.
- **Optionale Project-Enablement-Skills** bleiben post-v1.0/optional.
- **Optionale Governance-Skills** (`ndf-release-safety`, `ndf-adr-governance-review`) bleiben optional, sofern kein neuer Gap entsteht.
- **Zweiter Fixture-Typ (Projekt mit Code)** bleibt dokumentierte Grenze/tracked.

## EN – Allowed RC Notes

G-13 stays tracked (limited per-step depth; one private-context run) if visibly documented; ECS-001 partially closed; no full v1.x promise before final v1.0; the RC is not final v1.0 (candidate label); optional project-enablement skills stay post-v1.0/optional; optional governance skills stay optional unless a new gap arises; a second fixture type stays a documented limit/tracked.

## DE – Final Release Blockers (vor v1.0 final zwingend geschlossen oder akzeptiert)

Ein v1.0 final ist **blockiert**, wenn eines gilt:

- Public-Quality-Gate nicht grün (strict/self-test) auf dem Release-Commit.
- Secret-Wert oder private Daten/private Projektnamen/echte Domains/Reviewer-Identitäten in Public NDF.
- ADR-0031 oder ADR-0032 gebrochen.
- v1.x Compatibility Policy unklar/nicht aktiviert bei v1.0-Claim.
- Autonome Git-/Release-Aktionen durch einen AI-Agenten.
- Skills mit Scripts/Netz/Secrets ohne neue ausdrückliche ADR-Entscheidung.
- **G-13 weder vertieft (Weg A) noch bewusst als akzeptierte Grenze dokumentiert (Weg B).**
- Release Criteria selbst inkonsistent.
- v1.0-Claims vor der Freigabe.

## EN – Final Release Blockers

A final v1.0 is blocked if: the gate is not green on the release commit; a secret value / private data / private names / real domains / reviewer identities appear in public NDF; ADR-0031/0032 is broken; the v1.x compatibility policy is unclear/not activated at a v1.0 claim; an AI agent performs autonomous git/release actions; skills add scripts/network/secrets without a new explicit ADR decision; **G-13 is neither deepened (path A) nor deliberately documented as an accepted boundary (path B)**; the release criteria are internally inconsistent; v1.0 claims appear before approval.

## DE – G-13-Schwelle (External Validation Evidence Depth)

Basierend auf [WP-140](../validation/v1-0/EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md):

- **Für RC:** `RC can proceed with notes`. G-13 bleibt `tracked`; keine Blockade, solange die Note sichtbar im RC-Changelog/-Text steht. RC darf als Validierungsvehikel dienen.
- **Für v1.0 final:** eine der beiden Schwellen muss erfüllt sein:
  - **Weg A – Tieferer öffentlicher neutraler Validierungslauf mit Schrittbelegen** (die sechs Runbook-Schritte einzeln belegt; öffentliches Fixture; keine Reviewer-Identität im Public NDF), der die Evidence auf `met` hebt.
  - **Weg B – Dokumentierte akzeptierte Grenze / Known Limitation** für v1.0 final: die begrenzte Schrittbeleg-Tiefe wird ausdrücklich als bewusst akzeptierte v1.0-Grenze dokumentiert (ehrlich, sichtbar), mit Begründung (z. B. Ein-Personen-Engpass).

**Keine neue Evidenz erfinden.** Der Weg (A oder B) wird im v1.0 Final Readiness Review (WP-142+) gewählt und vom Human Maintainer bestätigt.

## EN – G-13 Threshold

Based on WP-140: for RC, `RC can proceed with notes` (G-13 stays tracked, note visible, RC may be a validation vehicle). For v1.0 final, one of two paths: **A** a deeper public neutral run with per-step evidence lifting it to `met`, or **B** a documented accepted boundary / known limitation for v1.0 final (honest, visible, justified). No invented evidence; the path is chosen in the v1.0 final readiness review and confirmed by the Human Maintainer.

## DE – Skills-vor-RC/final-Bewertung

- **Achtteiliges docs-only Skill-Pack reicht für v1.0-Core** (validiert WP-138).
- **Keine zusätzlichen Skills sind RC-Blocker.**
- **`ndf-release-safety` / `ndf-adr-governance-review` bleiben optional** (Governance via Prozess + ADR-0031/0032 abgedeckt).
- **Project-Enablement-Skills bleiben optional/post-v1.0.**
- **Neue Skill-Implementierungen vor RC nur bei ausdrücklichem Human-Maintainer-Scope-Change** und ADR-0032-konform.

## EN – Skills-before-RC/final Assessment

The eight-skill docs-only pack suffices for v1.0-core (WP-138); no additional skills are RC blockers; release-safety/adr-governance-review stay optional; project-enablement skills stay optional/post-v1.0; new skill implementations before an RC only on an explicit human-maintainer scope change and ADR-0032-compliant.

## DE – Nächste WPs

1. **WP-142 – v1.0 RC Readiness Review** (ehrlicher Check gegen die RC-Kriterien dieses Dokuments; G-13-Note sichtbar).
2. **WP-143 – v1.0 RC Release Prep** (RC-Notes/Go-No-Go/Tagging-Guide, nur Doku; Freigabe durch Human Maintainer).
3. **Danach:** manueller RC-Release durch den Human Maintainer.
4. **Danach:** RC-Feedback-Triage → v1.0 Final Readiness (G-13-Weg A/B wählen) → v1.0 Final Prep → manuelle v1.0-Freigabe.

**Kein Zwischen-WP zwischen WP-141 und WP-142 nötig:** G-13 blockiert die Readiness nicht; die G-13-Schwelle ist hier festgelegt. Optionale Validierungsläufe/Governance-Skills laufen parallel/nicht blockierend.

## EN – Next WPs

WP-142 (v1.0 RC readiness review against these RC criteria) → WP-143 (v1.0 RC release prep, docs only, human-maintainer approval) → manual RC release → RC feedback triage → v1.0 final readiness (choose G-13 path A/B) → v1.0 final prep → manual v1.0 approval. No intermediate WP needed between 141 and 142; optional validation runs/governance skills run in parallel, non-blocking.

## DE – Security / ADR-0031 / ADR-0032 Bewertung

ADR-0031 und ADR-0032 bleiben bindend und unverändert. Die volle v1.x-Zusage wird erst mit v1.0 aktiviert (F-03). Keine v1.0-Aktivierung/RC in diesem WP. Keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen. Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name. Nächste freie ADR-Nummer: 0033.

## EN – Security / ADR-0031 / ADR-0032 Assessment

ADR-0031/0032 stay binding and unchanged; the full v1.x promise activates only at v1.0 (F-03); no v1.0 activation/RC here; no scripts/network/secrets/private data/git-release actions; secret name only as a name; next free ADR number 0033.

## DE – Risks / Open Notes

- **G-13** bleibt der zentrale v1.0-final-Vorbehalt (tracked; Weg A oder B vor final).
- **Ein-Personen-Engpass** begrenzt zusätzliche unabhängige Läufe (dokumentiertes Risiko; stützt ggf. Weg B).
- **Kriterien-Drift:** die Kriterien sind mit diesem Lock verbindlich; Änderungen nur per dokumentierter Entscheidung.
- **Kein Zeitplan; kein v1.0-Claim.**

## EN – Risks / Open Notes

G-13 remains the central v1.0-final caveat (path A or B before final); the single-person bottleneck limits additional independent runs (documented risk; may support path B); criteria drift is controlled by this lock (changes only via a documented decision); no schedule; no v1.0 claim.

## DE – Decision

**GO WITH NOTES.** v1.0 Release Criteria finalisiert; RC- und Final-Kriterien getrennt; G-13-Schwelle festgelegt (RC mit Notes; final Weg A/B); achtteiliges Skill-Pack reicht für v1.0-Core; keine v1.0-Aktivierung/RC; ADR-0031/0032 unverändert; Foundation 0.9 bleibt nicht v1.0. **Nächster empfohlener WP: WP-142 – v1.0 RC Readiness Review.**

## EN – Decision

**GO WITH NOTES.** v1.0 release criteria finalized; RC and final criteria separated; G-13 threshold set (RC with notes; final path A/B); the eight-skill pack suffices for v1.0-core; no v1.0 activation/RC; ADR-0031/0032 unchanged; Foundation 0.9 stays not v1.0. Next recommended WP: WP-142 – v1.0 RC Readiness Review.
