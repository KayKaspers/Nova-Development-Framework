# v1.0 RC Readiness Review

## DE – Titel

Readiness-Review für die v1.0-RC-Release-Prep (NDF-WP-142, Skill-assisted Full Prompt Mode) — ehrliche Prüfung der [v1.0 Release Criteria](../../release/V1_0_RELEASE_CRITERIA.md) (WP-141) vor `v1.0.0-rc.1`.

## DE – Status / Ergebnis

**GO WITH NOTES – ready for v1.0 RC Release Prep.** Alle RC-Kriterien (RC-01…RC-13) sind `met` oder `met with notes` mit sichtbaren, akzeptierten Notes; die Allowed RC Notes sind akzeptiert; **kein Final Blocker blockiert einen RC** (die vorhandenen Notes sind final-only oder tracked). Es wird **kein** RC erstellt und v1.0 **nicht** aktiviert. Foundation 0.9 bleibt released/published, **nicht v1.0**, kein RC, keine volle v1.x-Zusage. ADR-0031/0032 unverändert.

## EN – Status / Result

**GO WITH NOTES – ready for v1.0 RC Release Prep.** All RC criteria (RC-01…RC-13) are `met` or `met with notes` with visible, accepted notes; the allowed RC notes are accepted; **no final blocker blocks an RC** (the existing notes are final-only or tracked). No RC is created and v1.0 is not activated. Foundation 0.9 stays released/published, **not v1.0**, no RC, no full v1.x promise. ADR-0031/0032 unchanged.

## DE – Scope

Ehrliche Prüfung der RC-Kriterien, der Allowed RC Notes und der Final Blockers gegen den aktuellen Stand; RC-Go/No-Go; Vorbereitung von WP-143. **Nicht im Scope:** RC erstellen, v1.0/volle v1.x-Zusage aktivieren, neue/geänderte Skills, Scripts, Netzwerk, Commit/Push/Tag/Release.

## EN – Scope

Honest check of RC criteria, allowed RC notes, and final blockers against the current state; RC go/no-go; preparation of WP-143. Out of scope: creating an RC, activating v1.0/full v1.x promise, new/changed skills, scripts, network, commit/push/tag/release.

## DE – Input Summary

Ausgewertet: die [v1.0 Release Criteria](../../release/V1_0_RELEASE_CRITERIA.md) (WP-141), der [v1.0 Gap Review](V1_0_GAP_REVIEW_AND_SCOPE_LOCK.md) (WP-139), der [External Validation Evidence Review](EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md) (WP-140), der [v1.0 Readiness Criteria Draft](../../release/V1_0_READINESS_CRITERIA_DRAFT.md), die acht Skills, [ADR-0031](../../adr/ADR-0031-v1x-compatibility-policy.md), [ADR-0032](../../adr/ADR-0032-skill-security-policy.md), `CHANGELOG.md` und Gate-Läufe.

## EN – Input Summary

Reviewed: the v1.0 release criteria (WP-141), the gap review (WP-139), the external validation evidence review (WP-140), the readiness criteria draft, the eight skills, ADR-0031/0032, the changelog, and gate runs.

## DE – RC Criteria Matrix

Status: **Met** · **Met with notes** · **Gap** · **Blocker** · **N/A**.

| ID | Criterion | Status | Evidence | Notes | RC Impact |
|---|---|---|---|---|---|
| RC-01 | Gate `--strict` + `--self-test` grün | **Met** | lokale Läufe: 0/0/4, self-test passed | auf RC-Commit erneut zu bestätigen | kein |
| RC-02 | New-file neutrality; keine privaten Daten/Secrets/Reviewer-Identitäten | **Met** | Gate v0.2, Kontroll-Greps | — | kein |
| RC-03 | README zweisprachiger, ehrlicher Einstieg | **Met** | `README.md` | — | kein |
| RC-04 | Kern-Prompts DE/EN; Prompt-Index aktuell | **Met** | `docs/prompts/`, Priority-Pass | — | kein |
| RC-05 | Release-Prozess dokumentiert und mehrfach praktiziert | **Met** | 0.2–0.9 Release-Historie | — | kein |
| RC-06 | Human-Maintainer-only | **Met** | Gates, WP-Notes | — | kein |
| RC-07 | ADR-Policy; ADR-0031/0032 accepted | **Met with notes** | `ADR_POLICY.md`, ADR-0031/0032 | Massenmigration deferred (tracked) | akzeptiert |
| RC-08 | ≥1 unabhängiger Validierungslauf | **Met with notes** | WP-088 (öffentlich), WP-074 (privat-neutralisiert) | G-13 Schrittbeleg-Tiefe tracked | akzeptiert (sichtbar) |
| RC-09 | Adapter-Konventionen stabil ≥2 Releases | **Met** | WP-101 Stability Review | — | kein |
| RC-10 | Changelog vollständig; RC-Notes sichtbar | **Met with notes** | `CHANGELOG.md` | RC-Notes werden in WP-143-Release-Notes sichtbar geführt | akzeptiert |
| RC-11 | Prompt-Entscheidungslogik (Kern); Randbestand tracked | **Met with notes** | Stichprobe `framework/prompts/` | Randbestand-Vollprüfung ist Final-Kriterium (F-04) | final-only |
| RC-12 | Skill-Pack docs-only/fail-closed | **Met** | ADR-0032, Skill-Validationen (WP-129/137/138) | acht Skills, keine Automation | kein |
| RC-13 | RC-Kriterien selbstkonsistent; keine v1.0-Claims | **Met** | `V1_0_RELEASE_CRITERIA.md`, Kontroll-Greps | kein positiver v1.0-Claim | kein |

**Zusammenfassung:** Met 8 (RC-01/02/03/04/05/06/09/12/13 → 9), Met with notes 4 (RC-07/08/10/11), Gap 0, Blocker 0. **Bedingung erfüllt:** jedes RC-Kriterium `met` oder `met with notes` mit sichtbarer, akzeptierter Note.

## EN – RC Criteria Matrix

The table checks RC-01…RC-13 with status, evidence, notes, and RC impact. Result: 9 Met, 4 Met with notes (ADR mass-migration deferred; G-13 evidence depth tracked; RC notes to be made visible in WP-143 release notes; prompt-decision-logic remainder is a final criterion), 0 gaps, 0 blockers. Condition satisfied: every RC criterion is `met` or `met with notes` with a visible, accepted note.

## DE – Allowed RC Notes

**Allowed RC Notes accepted.** Alle in WP-141 zugelassenen Notes sind akzeptabel und werden sichtbar dokumentiert:

| Note | Bewertung |
|---|---|
| G-13 External Validation Evidence Depth bleibt `tracked` | akzeptiert (sichtbar in Changelog/Criteria/Evidence Review) |
| ECS-001 Extended Core Skill Real-use History `partially closed` | akzeptiert |
| keine volle v1.x-Zusage vor final | akzeptiert (F-03, erst mit v1.0) |
| RC ist nicht final | akzeptiert (Kandidaten-Label) |
| Project-Enablement-Skills optional/post-v1.0 | akzeptiert |
| optionale Governance-Skills optional | akzeptiert |
| zweiter Fixture-Typ dokumentierte Grenze | akzeptiert (tracked) |

## EN – Allowed RC Notes

**Allowed RC notes accepted.** All notes permitted in WP-141 are acceptable and visibly documented (G-13 tracked, ECS-001 partially closed, no full v1.x promise before final, RC is not final, project-enablement/governance skills optional, second fixture type a documented limit).

## DE – Final Blockers Check

Prüfung der Final Blockers (WP-141) gegen den aktuellen Stand:

| Final Blocker | Aktuell vorhanden? | RC-blocking? |
|---|---|---|
| Gate nicht grün | nein (0/0/4) | — |
| Secret-Wert/private Daten/Reviewer-Identitäten in Public NDF | nein | — |
| ADR-0031/0032 gebrochen | nein (unverändert) | — |
| v1.x-Policy unklar/nicht aktiviert bei v1.0-Claim | nein (kein Claim; Aktivierung ist Final-Kriterium F-03) | **final-only** |
| autonome Git-/Release-Aktionen durch AI | nein | — |
| Skills mit Scripts/Netz/Secrets ohne neue ADR | nein | — |
| G-13 weder vertieft noch als akzeptierte Grenze dokumentiert | n/a für RC (tracked erlaubt); vor **final** zu entscheiden (Weg A/B) | **final-only** |
| Release Criteria inkonsistent | nein | — |
| v1.0-Claims vor Freigabe | nein | — |

- **RC-blocking:** keine.
- **Final-only:** F-03 (volle v1.x-Zusage) und die G-13-Weg-A/B-Entscheidung — beide bewusst vor **v1.0 final**, nicht vor RC.
- **v1.0-Claims sichtbar?** nein. **Volle v1.x-Zusage versehentlich aktiv?** nein. **Inkonsistenzen RC↔Final?** keine gefunden.

## EN – Final Blockers Check

None of the WP-141 final blockers are present in an RC-blocking way. Two items are final-only by design: F-03 (full v1.x promise activation) and the G-13 path-A/B decision — both deliberately before v1.0 final, not before an RC. No v1.0 claims are visible; the full v1.x promise is not accidentally active; no RC↔final inconsistencies were found.

## DE – RC Go/No-Go

**GO WITH NOTES – ready for v1.0 RC Release Prep.** Begründung: alle RC-Kriterien met/met-with-notes mit sichtbaren, akzeptierten Notes; Allowed RC Notes akzeptiert; keine RC-blockierenden Final Blocker; G-13 bleibt tracked (kein RC-Blocker). Der RC ist ein Kandidat mit ehrlichen Notes und darf als Validierungsvehikel vorbereitet werden — die Erstellung/Freigabe bleibt Human-Maintainer-only.

## EN – RC Go/No-Go

**GO WITH NOTES – ready for v1.0 RC Release Prep.** All RC criteria met/met-with-notes with visible accepted notes; allowed RC notes accepted; no RC-blocking final blockers; G-13 stays tracked (not an RC blocker). The RC is a candidate with honest notes and may be prepared as a validation vehicle — creation/approval stays human-maintainer-only.

## DE – Skills-Bewertung

- **Achtteiliges docs-only Skill-Pack:** reicht für v1.0-Core (WP-138); RC-tauglich.
- **Zusätzliche Skills vor RC:** keine erforderlich; `ndf-release-safety`/`ndf-adr-governance-review` optional (nicht RC-blockierend). WP-143 kann die Release-Prep-Struktur auch ohne `ndf-release-safety` liefern (dokumentarisch, wie in bisherigen Release-Preps).

## EN – Skills Assessment

The eight-skill docs-only pack suffices for v1.0-core (WP-138) and is RC-ready; no additional skills are required before an RC; release-safety/adr-governance-review stay optional (non-RC-blocking); WP-143 can provide the release-prep structure documentarily without them.

## DE – Vorbereitung WP-143

**WP-143 – v1.0 RC Release Prep** (Kandidat, nicht aktiviert) soll — **nur als Dokumentation, ohne Veröffentlichung** — vorbereiten: RC Release Notes; RC Go/No-Go-Checkliste; RC Tagging Guide (möglicher Tag `v1.0.0-rc.1`, annotated, Pre-Release); GitHub Pre-Release/Release-Candidate-Body; RC Known Notes (G-13 tracked, ECS-001, „nicht final"); Human-Maintainer-only-Schritte. **WP-143 erstellt keinen RC**; Tag/Release/Pre-Release bleiben ausschließlich menschliche Aktionen.

## EN – WP-143 Preparation

WP-143 (candidate, not activated) prepares — documentation only, no publishing — RC release notes, an RC go/no-go checklist, an RC tagging guide (possible tag `v1.0.0-rc.1`, annotated, pre-release), a GitHub pre-release/RC body, RC known notes (G-13 tracked, ECS-001, "not final"), and human-maintainer-only steps. WP-143 creates no RC; tag/release/pre-release stay human-only actions.

## DE – Security / ADR-0031 / ADR-0032 Bewertung

ADR-0031/0032 unverändert bindend; keine v1.0-Aktivierung/RC; volle v1.x-Zusage erst mit v1.0 final (F-03). Keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; keine Skills geändert/erstellt; keine Reviewer-Identitäten/privaten Namen/Domains. Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name. Nächste freie ADR-Nummer: 0033.

## EN – Security / ADR-0031 / ADR-0032 Assessment

ADR-0031/0032 stay binding and unchanged; no v1.0 activation/RC; full v1.x promise only at v1.0 final (F-03); no scripts/network/secrets/private data/git-release actions; no skill changes/creations; no reviewer identities/private names/domains; secret name only as a name; next free ADR number 0033.

## DE – Risks / Open Notes

- **G-13** bleibt der zentrale v1.0-final-Vorbehalt (tracked; im RC sichtbar zu führen; Weg A/B vor final).
- **RC-01/RC-10 sind commit-gebunden:** Gate-Grün und die sichtbaren RC-Notes müssen auf dem tatsächlichen RC-Commit (WP-143) erneut bestätigt werden.
- **Ein-Personen-Engpass** (dokumentiertes Risiko).
- **Kein Zeitplan; kein v1.0-Claim.**

## EN – Risks / Open Notes

G-13 remains the central v1.0-final caveat (tracked; visible in the RC; path A/B before final); RC-01/RC-10 are commit-bound (gate green and visible RC notes must be re-confirmed on the actual RC commit in WP-143); the single-person bottleneck is a documented risk; no schedule; no v1.0 claim.

## DE – Decision

**GO WITH NOTES – ready for v1.0 RC Release Prep.** RC-Kriterien erfüllt oder erfüllt mit Notes; Allowed RC Notes akzeptiert; keine RC-blockierenden Final Blocker; G-13 tracked; keine v1.0-Aktivierung/RC; ADR-0031/0032 unverändert; Foundation 0.9 bleibt nicht v1.0. **Nächster empfohlener WP: WP-143 – v1.0 RC Release Prep.**

## EN – Decision

**GO WITH NOTES – ready for v1.0 RC Release Prep.** RC criteria met or met with notes; allowed RC notes accepted; no RC-blocking final blockers; G-13 tracked; no v1.0 activation/RC; ADR-0031/0032 unchanged; Foundation 0.9 stays not v1.0. Next recommended WP: WP-143 – v1.0 RC Release Prep.
