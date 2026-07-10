# v1.0.0-rc.1 Tagging and GitHub Release Guide

## DE – Zweck

Manuelle Anleitung für den **Human Maintainer** zum Taggen und Veröffentlichen des ersten v1.0 Release Candidate. Der Implementation Agent führt diese Schritte **nicht** aus — Tag und Release sind ausschließlich menschliche Aktionen (ADR-0032).

## EN – Purpose

Manual guide for the **Human Maintainer** to tag and publish the first v1.0 release candidate. The implementation agent does **not** execute these steps — tag and release are human-only actions (ADR-0032).

## DE – Status

**Prep-Guide (pending Human Maintainer release).** `v1.0.0-rc.1` ist noch **nicht** getaggt oder veröffentlicht. Dieser Guide dokumentiert die manuellen Schritte. `v1.0.0-rc.1` ist ein Release Candidate, **nicht** final v1.0; keine volle v1.x-Zusage aktiv.

## EN – Status

**Prep guide (pending human-maintainer release).** `v1.0.0-rc.1` is not yet tagged or published. This guide documents the manual steps. It is a release candidate, not final v1.0; no full v1.x promise active.

## DE – Geplanter Tag / EN – Planned Tag

```text
v1.0.0-rc.1   (annotated Tag)
```

## DE – Geplanter Release-Titel / EN – Planned Release Title

```text
Nova Development Framework v1.0.0 Release Candidate 1
```

## DE – Release-Typ / EN – Release Type

```text
Pre-release / Release Candidate  (nicht "Latest", nicht final)
```

## DE – Voraussetzungen / EN – Prerequisites

- [Go/No-Go-Checkliste](V1_0_RC_1_GO_NO_GO_CHECKLIST.md) mit **GO WITH NOTES** abgeschlossen.
- RC-01 (Gate grün) und RC-10 (Changelog/RC-Notes) auf dem RC-Commit bestätigt.
- GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt.
- `v1.0.0-rc.1` existiert noch nicht.

## DE – Manuelle Schritte / EN – Manual Steps

Nur Dokumentation — **nicht durch den Implementation Agent ausführen**:

```bash
git status
git checkout main
git pull origin main
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
# Changelog prüfen: v1.0.0-rc.1-Eintrag vorhanden, RC-Notes sichtbar
git tag --list v1.0.0-rc.1
git tag -a v1.0.0-rc.1 -m "Nova Development Framework v1.0.0 Release Candidate 1"
git push origin v1.0.0-rc.1
```

GitHub Pre-Release manuell im UI (**Releases → Draft a new release**, Tag `v1.0.0-rc.1`, Target `main`, „Set as a pre-release", **nicht** „Set as the latest release") oder als vom Human Maintainer entschiedener CLI-Schritt (nur Human-Maintainer-Option, nicht ausführen):

```bash
gh release create v1.0.0-rc.1 --title "Nova Development Framework v1.0.0 Release Candidate 1" --notes-file docs/release/V1_0_RC_1_RELEASE_NOTES.md --prerelease
```

Release Body: aus [V1_0_RC_1_RELEASE_NOTES.md](V1_0_RC_1_RELEASE_NOTES.md) übernehmen.

## DE – Human-Maintainer-Schritte (Reihenfolge)

1. Finalen Status prüfen (`git status`, sauberer Working Tree).
2. Gate erneut ausführen (`--strict` + `--self-test`) — muss grün sein (RC-01).
3. Changelog prüfen — `v1.0.0-rc.1`-Eintrag, RC-Notes sichtbar (RC-10).
4. Committen (falls noch offen).
5. Pushen.
6. Annotated Tag `v1.0.0-rc.1` erstellen.
7. Tag pushen.
8. GitHub Pre-Release erstellen (Pre-release/RC, nicht Latest).
9. Release Body aus den RC Release Notes übernehmen.
10. Nach Veröffentlichung kontrollieren (siehe Nachprüfung).

## EN – Human-Maintainer Steps (order)

Check final status → re-run gate (must be green, RC-01) → check changelog (`v1.0.0-rc.1` entry, RC notes visible, RC-10) → commit (if pending) → push → create annotated tag `v1.0.0-rc.1` → push tag → create GitHub pre-release (pre-release/RC, not latest) → take the body from the RC release notes → verify after publishing.

## DE – Nachprüfung / EN – Verification

- [ ] Release erscheint auf GitHub als **Pre-release / Release Candidate** mit Tag `v1.0.0-rc.1` auf `main`, **nicht** als „Latest".
- [ ] Release-Titel ist „Nova Development Framework v1.0.0 Release Candidate 1".
- [ ] Tag ist **annotated** (`git cat-file -t v1.0.0-rc.1` → `tag`).
- [ ] Release Body enthält „not final v1.0", die v1.x-Nicht-aktiv-Aussage und die Known RC Notes (inkl. G-13 tracked).
- [ ] Public-Quality-Gate-Action des RC-Commits ist grün.

## DE – Was nicht automatisiert werden darf / EN – What Must Not Be Automated

```text
Do not run tag/release commands from an implementation agent.
Only the Human Maintainer may create, push, or publish the RC tag and GitHub pre-release.
```

Keine autonomen Commit-/Push-/Tag-/Release-Aktionen durch Agenten oder Skills; keine GitHub-API-Schreibaktion durch den Implementation Agent (ADR-0032 bleibt bindend).

## DE – Rollback-/Correction-Hinweis / EN – Rollback / Correction Note

- **Release-Text/Titel falsch:** GitHub Release editieren (kein Git-Eingriff nötig).
- **Falscher Tag-Stand, noch nicht öffentlich genutzt:** Release löschen, dann Tag löschen und neu setzen:

```bash
git tag -d v1.0.0-rc.1
git push origin :refs/tags/v1.0.0-rc.1
```

- **Bereits öffentlich genutzt:** Tag **nicht** durch AI bewegen; **kein History-Rewrite**. Der Human Maintainer entscheidet über einen Correction Release (z. B. `v1.0.0-rc.2`) oder eine Reconciliation.

## DE – Post-Release-Follow-up / EN – Post-Release Follow-up

Nach Tag + Pre-Release: **NDF-WP-144 – v1.0 RC Feedback Triage / RC Post-Release Review** — RC-Feedback triagieren, Known RC Notes prüfen, G-13-Weg (A oder B) für v1.0 final vorbereiten, Status auf „v1.0 RC released" heben und diesen Guide als historisch markieren. v1.0 final bleibt ein eigener späterer Zyklus (Final Readiness → Final Prep → manuelle Freigabe).

## EN – Post-Release Follow-up

After tag + pre-release: **NDF-WP-144 – v1.0 RC feedback triage / RC post-release review** — triage RC feedback, review the known RC notes, prepare the G-13 path (A or B) for v1.0 final, lift the status to "v1.0 RC released", and mark this guide historical. Final v1.0 stays its own later cycle (final readiness → final prep → manual approval).
