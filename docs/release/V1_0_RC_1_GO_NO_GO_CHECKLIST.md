# v1.0.0-rc.1 Go/No-Go Checklist

## DE – Status

**Prep-Checkliste (pending Human Maintainer release).** Vorbereitet in NDF-WP-143. Die finale Freigabe (GO/NO-GO) trifft der **Human Maintainer** auf dem tatsächlichen RC-Commit. Der Implementation Agent erstellt keinen Tag/Release. `v1.0.0-rc.1` ist ein Release Candidate, **nicht** final v1.0.

## EN – Status

**Prep checklist (pending human-maintainer release).** Prepared in NDF-WP-143. The final GO/NO-GO decision is the Human Maintainer's on the actual RC commit. The implementation agent creates no tag/release. `v1.0.0-rc.1` is a release candidate, not final v1.0.

## DE – Pre-Release-Status

- Foundation 0.9: `released / published — reconciliation documented` (`v0.9.0-foundation`).
- WP-142 RC Readiness: **GO WITH NOTES – ready for v1.0 RC Release Prep**.
- RC-Kriterien (WP-141/142): 9 Met, 4 Met with notes, 0 Gaps, 0 Blocker.

## EN – Pre-Release Status

Foundation 0.9 released/published; WP-142 RC readiness GO WITH NOTES; RC criteria 9 Met, 4 Met with notes, 0 gaps, 0 blockers.

## DE – RC-Kriterien-Prüfung (RC-01…RC-13)

| ID | Kriterium | Erwartung | Auf RC-Commit bestätigen? |
|---|---|---|---|
| RC-01 | Gate `--strict` + `--self-test` grün | grün | **[ ] ja (commit-gebunden)** |
| RC-02 | New-file neutrality; keine privaten Daten/Secrets/Reviewer-Identitäten | erfüllt | [ ] |
| RC-03 | README zweisprachiger, ehrlicher Einstieg | erfüllt | [ ] |
| RC-04 | Kern-Prompts DE/EN; Prompt-Index aktuell | erfüllt | [ ] |
| RC-05 | Release-Prozess dokumentiert/praktiziert | erfüllt | [ ] |
| RC-06 | Human-Maintainer-only | erfüllt | [ ] |
| RC-07 | ADR-Policy; ADR-0031/0032 accepted | erfüllt (Note: Massenmigration deferred) | [ ] |
| RC-08 | ≥1 unabhängiger Lauf | erfüllt (Note: G-13 tracked) | [ ] |
| RC-09 | Adapter-Konventionen stabil ≥2 Releases | erfüllt | [ ] |
| RC-10 | Changelog vollständig; RC-Notes sichtbar | erfüllt | **[ ] ja (commit-gebunden)** |
| RC-11 | Prompt-Entscheidungslogik (Kern); Randbestand tracked | erfüllt (Note: Randbestand → F-04) | [ ] |
| RC-12 | Skill-Pack docs-only/fail-closed (acht Skills) | erfüllt | [ ] |
| RC-13 | RC-Kriterien selbstkonsistent; keine v1.0-Claims | erfüllt | [ ] |

## EN – RC Criteria Check (RC-01…RC-13)

The table lists RC-01…RC-13 with the expectation and whether the item is commit-bound. RC-01 (gate green) and RC-10 (changelog/RC notes visible) must be re-confirmed on the actual RC commit.

## DE – Allowed RC Notes Prüfung

- [ ] G-13 External Validation Evidence Depth als `tracked` **sichtbar** dokumentiert.
- [ ] ECS-001 `partially closed` dokumentiert.
- [ ] „RC ist nicht final" sichtbar.
- [ ] „volle v1.x-Zusage erst mit finalem v1.0" sichtbar.
- [ ] Project-Enablement- und optionale Governance-Skills als optional dokumentiert.
- [ ] Zweiter Fixture-Typ als dokumentierte Grenze.

## EN – Allowed RC Notes Check

Confirm G-13 tracked, ECS-001 partially closed, "RC is not final", "full v1.x promise only at final v1.0", optional project-enablement/governance skills, and second fixture type as a documented limit are all visibly documented.

## DE – Final Blockers Check (dürfen nicht vorliegen)

- [ ] Public-Quality-Gate grün (kein `not green`).
- [ ] Kein Secret-Wert / keine privaten Daten / privaten Projektnamen / echten Domains / Reviewer-Identitäten in Public NDF.
- [ ] ADR-0031/0032 unverändert und eingehalten.
- [ ] Keine autonome Git-/Release-Aktion durch einen AI-Agenten.
- [ ] Keine Skills mit Scripts/Netz/Secrets ohne neue ADR.
- [ ] Kein v1.0-Claim vor der Freigabe; volle v1.x-Zusage **nicht** aktiviert.
- [ ] Release Criteria konsistent.

## EN – Final Blockers Check (must be absent)

Confirm: gate green; no secrets/private data/private names/real domains/reviewer identities in public NDF; ADR-0031/0032 unchanged and honored; no autonomous AI git/release action; no skills with scripts/network/secrets without a new ADR; no v1.0 claim before approval and the full v1.x promise not activated; release criteria consistent.

## DE – Weitere Checks

- [ ] Public-Neutrality-Gate: `python scripts/check_public_quality.py --strict` und `--self-test` grün auf dem RC-Commit.
- [ ] Secret-/Private-Data-Check: Kontroll-Greps sauber.
- [ ] ADR-0031/0032-Check: Accepted, unverändert.
- [ ] Skill-Pack-Check: genau acht docs-only Skills, keine Automation.
- [ ] Changelog-Check: `v1.0.0-rc.1`-Eintrag vorhanden, RC-Notes sichtbar, RC als „pending/prepared" ehrlich benannt.
- [ ] Tagging-Check: Tag `v1.0.0-rc.1` existiert noch nicht (wird vom Human Maintainer gesetzt).
- [ ] GitHub-Pre-Release-Check: als Pre-release/Release Candidate, **nicht** „Latest", **nicht** final.
- [ ] Human-Maintainer-only-Bestätigung: Tag/Release nur durch den Human Maintainer.

## EN – Additional Checks

Gate green on the RC commit; secret/private-data control greps clean; ADR-0031/0032 accepted and unchanged; skill pack exactly eight docs-only skills with no automation; changelog has the `v1.0.0-rc.1` entry with visible RC notes honestly marked pending/prepared; tag `v1.0.0-rc.1` does not yet exist; GitHub pre-release marked as pre-release/RC, not "Latest", not final; human-maintainer-only confirmation for tag/release.

## DE – Finale Entscheidung

```text
[ ] GO WITH NOTES  — RC freigeben (mit sichtbaren Known RC Notes)
[ ] GO WITH BLOCKERS
[ ] NO-GO
```

Entscheidung und Datum trägt der **Human Maintainer** ein. Der Implementation Agent führt keine Freigabe aus.

## EN – Final Decision

The Human Maintainer records the decision (GO WITH NOTES / GO WITH BLOCKERS / NO-GO) and date. The implementation agent performs no approval.

## DE – Was nicht automatisiert werden darf

```text
Do not run tag/release commands from an implementation agent.
Only the Human Maintainer may create, push, or publish the RC tag and GitHub pre-release.
```

Keine autonomen Commit-/Push-/Tag-/Release-Aktionen durch Agenten oder Skills (ADR-0032 bindend).
