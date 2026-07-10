# v1.0.0 Final Go/No-Go Checklist

## DE – Status

**Final-Prep-Checkliste (pending Human Maintainer release).** Vorbereitet in NDF-WP-148. Die finale Freigabe (GO/NO-GO) trifft der **Human Maintainer** auf dem tatsächlichen finalen Release-Commit. Der Implementation Agent erstellt keinen Tag/Release. `v1.0.0` ist **noch nicht** veröffentlicht.

## EN – Status

**Final prep checklist (pending human-maintainer release).** Prepared in NDF-WP-148. The final GO/NO-GO decision is the Human Maintainer's on the actual final release commit. The implementation agent creates no tag/release. `v1.0.0` is **not yet** published.

## DE – Final Release Status

- RC: `v1.0.0-rc.1` veröffentlicht (annotated Tag → `4beab84`), unverändert.
- WP-147 Final Readiness: **GO WITH NOTES – ready for v1.0 Final Release Prep** (F-01…F-07: 0 Gaps, 0 Blocker).
- G-13 Final-Weg: **C** (A best-effort, B akzeptierte Grenze).

## DE – RC-Basis geprüft

- [ ] RC `v1.0.0-rc.1` unverändert (Tag → `4beab84`).
- [ ] RC-Basis (RC-01…RC-13) weiterhin erfüllt/mit akzeptierten Notes.

## DE – Final Criteria F-01…F-07

| ID | Kriterium | Erwartung | Auf finalem Commit bestätigen? |
|---|---|---|---|
| F-01 | External Validation `met` oder dokumentierte Grenze | Weg B als akzeptierte Grenze dokumentiert (oder Weg A-Evidenz) | [ ] |
| F-02 | externer Einstieg unabhängig bestätigt | WP-088 + dokumentierte Grenze (Weg B) | [ ] |
| F-03 | volle v1.x-Zusage im finalen Kontext **aktiviert** | mit manueller Veröffentlichung durch Human Maintainer | **[ ] ja (Aktivierung = finaler Schritt)** |
| F-04 | Prompt-Entscheidungslogik vollständig oder Non-Goal | Randbestand als dokumentierte Grenze | [ ] |
| F-05 | RC-Feedback triagiert | „kein RC-Feedback" als Known Limitation dokumentiert | [ ] |
| F-06 | alle RC-Notes geschlossen oder akzeptiert | finale Triage (WP-147) übernommen | [ ] |
| F-07 | Final Readiness + Prep + manuelle Freigabe | WP-147 + WP-148 + Human-Freigabe | [ ] |

## EN – Final Criteria F-01…F-07

The table lists F-01…F-07 with the expected resolution and whether the item is commit-bound; F-03 (v1.x-promise activation) is the final human-maintainer step at publication.

## DE – G-13-Weg-C-Prüfung

- [ ] Weg B (dokumentierte akzeptierte Grenze) im Release-Text/Doku sichtbar.
- [ ] Weg A als best-effort / future improvement gekennzeichnet.
- [ ] Ein-Personen-Engpass transparent; keine erfundene externe Evidenz.
- [ ] Human Maintainer bestätigt Weg C.

## DE – Known Final Notes geprüft

- [ ] G-13 (Weg C), kein externes RC-Feedback (Known Limitation), RDS-001/ADS-001 (Betriebs-Notes), Project-Enablement post-v1.0, zweiter Fixture-Typ (Non-Goal) — alle sichtbar.

## DE – v1.x-Zusage

- [ ] v1.x-Zusage **vorbereitet**, aber erst mit manueller finaler Veröffentlichung **aktiv** (nicht durch Claude).

## DE – Weitere Checks

- [ ] Public-Neutrality-Gate: `python scripts/check_public_quality.py --strict` und `--self-test` grün auf dem finalen Commit.
- [ ] Secret-/Private-Data-Check: Kontroll-Greps sauber; keine Reviewer-Identitäten.
- [ ] ADR-0031/0032-Check: Accepted, unverändert.
- [ ] 38-Skill-Pack-Check: genau 38 docs-only Skills, keine Automation.
- [ ] Changelog-Check: `v1.0.0`-Eintrag vorhanden, Known Final Notes sichtbar, ehrlicher Status.
- [ ] Tagging-Check: Tag `v1.0.0` existiert noch nicht (wird vom Human Maintainer gesetzt).
- [ ] GitHub-Final-Release-Check: **Final release**, **nicht** Pre-release; „Latest" entscheidet der Human Maintainer.
- [ ] Human-Maintainer-only-Bestätigung: Tag/Release nur durch den Human Maintainer.

## EN – Additional Checks

Gate green on the final commit; secret/private-data control greps clean, no reviewer identities; ADR-0031/0032 accepted and unchanged; exactly 38 docs-only skills with no automation; changelog has the `v1.0.0` entry with visible known final notes and honest status; tag `v1.0.0` does not yet exist; GitHub release marked final (not pre-release), "latest" decided by the Human Maintainer; human-maintainer-only confirmation for tag/release.

## DE – Wichtig: commit-gebundene Punkte

Final Gate (Public Quality Gate), Changelog (`v1.0.0`-Eintrag) und der GitHub Release Body sind **auf dem tatsächlichen finalen Release-Commit erneut zu bestätigen**.

## EN – Important: commit-bound items

The final gate, the changelog `v1.0.0` entry, and the GitHub release body must be re-confirmed on the actual final release commit.

## DE – Finale Entscheidung

```text
[ ] GO WITH NOTES  — v1.0 final freigeben (mit sichtbaren Known Final Notes)
[ ] GO WITH BLOCKERS
[ ] NO-GO
```

Entscheidung und Datum trägt der **Human Maintainer** ein. Der Implementation Agent führt keine Freigabe aus.

## DE – Was nicht automatisiert werden darf

```text
Do not run tag/release commands from an implementation agent.
Only the Human Maintainer may create, push, or publish the v1.0.0 tag and GitHub release,
and only the manual final release activates the full v1.x compatibility promise.
```

Keine autonomen Commit-/Push-/Tag-/Release-Aktionen durch Agenten oder Skills (ADR-0032 bindend).
