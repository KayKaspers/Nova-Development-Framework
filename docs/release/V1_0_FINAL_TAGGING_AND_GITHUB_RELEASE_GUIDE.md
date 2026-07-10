# v1.0.0 Final Tagging and GitHub Release Guide

## DE – Zweck

Manuelle Anleitung für den **Human Maintainer** zum Taggen und Veröffentlichen des finalen `v1.0.0`-Release. Der Implementation Agent führt diese Schritte **nicht** aus — Tag, Release und die Aktivierung der v1.x-Zusage sind ausschließlich menschliche Aktionen (ADR-0032/ADR-0031).

## EN – Purpose

Manual guide for the **Human Maintainer** to tag and publish the final `v1.0.0` release. The implementation agent does **not** execute these steps — tag, release, and v1.x-promise activation are human-only actions (ADR-0032/ADR-0031).

## DE – Status

**Final-Prep-Guide (pending Human Maintainer release).** `v1.0.0` ist noch **nicht** getaggt oder veröffentlicht. Dieser Guide dokumentiert die manuellen Schritte.

## DE – Geplanter Tag / EN – Planned Tag

```text
v1.0.0   (annotated Tag)
```

## DE – Geplanter Release-Titel / EN – Planned Release Title

```text
Nova Development Framework v1.0.0
```

## DE – Release-Typ / EN – Release Type

```text
Final release  (nicht Pre-release; "Latest" entscheidet der Human Maintainer)
```

## DE – Voraussetzungen / EN – Prerequisites

- [Final Go/No-Go-Checkliste](V1_0_FINAL_GO_NO_GO_CHECKLIST.md) mit **GO WITH NOTES** abgeschlossen.
- Final Gate (grün), Changelog (`v1.0.0`-Eintrag) und Release Body auf dem finalen Commit bestätigt.
- GitHub Secret `NDF_PUBLIC_NEUTRALITY_DENYLIST` gesetzt.
- `v1.0.0` existiert noch nicht; RC `v1.0.0-rc.1` unverändert.

## DE – Manuelle Schritte / EN – Manual Steps

Nur Dokumentation — **nicht durch den Implementation Agent ausführen**:

```bash
git status
git checkout main
git pull origin main
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
# Changelog prüfen: v1.0.0-Eintrag vorhanden, Known Final Notes sichtbar
# Release Body prüfen: docs/release/V1_0_FINAL_RELEASE_NOTES.md
git tag --list v1.0.0
git tag -a v1.0.0 -m "Nova Development Framework v1.0.0"
git push origin v1.0.0
```

GitHub Final Release manuell im UI (**Releases → Draft a new release**, Tag `v1.0.0`, Target `main`, **nicht** „Set as a pre-release"; „Set as the latest release" nach Ermessen des Human Maintainers) oder als vom Human Maintainer entschiedener CLI-Schritt (nur Human-Maintainer-Option, nicht ausführen):

```bash
gh release create v1.0.0 --title "Nova Development Framework v1.0.0" --notes-file docs/release/V1_0_FINAL_RELEASE_NOTES.md --latest
```

Release Body: aus [V1_0_FINAL_RELEASE_NOTES.md](V1_0_FINAL_RELEASE_NOTES.md) (Abschnitt „GitHub Release Body") übernehmen.

## DE – Human-Maintainer-Schritte (Reihenfolge)

1. Finalen Status prüfen (`git status`, sauberer Working Tree).
2. Gate erneut ausführen (`--strict` + `--self-test`) — muss grün sein.
3. Changelog prüfen — `v1.0.0`-Eintrag, Known Final Notes sichtbar.
4. Release Body prüfen (keine falschen Claims, keine privaten Daten).
5. Committen (falls noch offen).
6. Pushen.
7. Annotated Tag `v1.0.0` erstellen.
8. Tag pushen.
9. GitHub Final Release erstellen (Final, nicht Pre-release).
10. Release Body aus den Final Release Notes übernehmen.
11. **v1.x-Kompatibilitätszusage im veröffentlichten finalen Kontext bestätigen** (ADR-0031) — erst hiermit aktiv.
12. Nach Veröffentlichung kontrollieren (siehe Nachprüfung).

## EN – Human-Maintainer Steps (order)

Check final status → re-run gate (must be green) → check changelog (`v1.0.0` entry, known final notes) → check release body → commit (if pending) → push → create annotated tag `v1.0.0` → push tag → create GitHub final release (final, not pre-release) → take the body from the final release notes → **confirm the v1.x compatibility promise in the published final context (ADR-0031) — active only here** → verify after publishing.

## DE – Nachprüfung / EN – Verification

- [ ] Release erscheint auf GitHub als **Final release** mit Tag `v1.0.0` auf `main`, **nicht** als Pre-release.
- [ ] Release-Titel ist „Nova Development Framework v1.0.0".
- [ ] Tag ist **annotated** (`git cat-file -t v1.0.0` → `tag`).
- [ ] Release Body enthält die v1.x-Policy-Aussage, das 38-Skill-Pack, Security-/ADR-Hinweise und die Known Final Notes.
- [ ] Public-Quality-Gate-Action des finalen Commits ist grün.
- [ ] `git tag` zeigt `v0.1.0-foundation` … `v0.9.0-foundation`, `v1.0.0-rc.1`, `v1.0.0`.

## DE – Was nicht automatisiert werden darf / EN – What Must Not Be Automated

```text
Do not run tag/release commands from an implementation agent.
Only the Human Maintainer may create, push, or publish the v1.0.0 tag and GitHub release,
and only the manual final release activates the full v1.x compatibility promise.
```

Keine autonomen Commit-/Push-/Tag-/Release-Aktionen durch Agenten oder Skills; keine GitHub-API-Schreibaktion durch den Implementation Agent (ADR-0032 bleibt bindend).

## DE – Rollback-/Correction-Hinweis / EN – Rollback / Correction Note

- **Release-Text/Titel falsch:** GitHub Release editieren (kein Git-Eingriff nötig).
- **Falscher Tag-Stand, noch nicht öffentlich genutzt:** Release löschen, dann Tag löschen und neu setzen:

```bash
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0
```

- **Bereits öffentlich genutzt:** Tag **nicht** durch AI bewegen; **kein History-Rewrite**. Der Human Maintainer entscheidet über einen Correction Release (z. B. `v1.0.1`) oder eine Reconciliation.

## DE – Post-Release-Follow-up / EN – Post-Release Follow-up

Nach Tag + finalem Release: **NDF-WP-149 – v1.0 Final Post-Release Review / Reconciliation** — finalen Release read-only verifizieren (annotated Tag, Final/nicht Pre-release, v1.x-Zusage im veröffentlichten Kontext aktiv), Known Final Notes prüfen, Status auf „v1.0 released" heben, RC-/RC-Prep-/Final-Prep-Dokumente als historisch markieren. Kein Tag-Move; kein History-Rewrite.

## EN – Post-Release Follow-up

After tag + final release: **NDF-WP-149 – v1.0 final post-release review / reconciliation** — verify the final release read-only (annotated tag, final/not pre-release, v1.x promise active in the published context), review the known final notes, lift the status to "v1.0 released", and mark the RC/RC-prep/final-prep docs historical. No tag move; no history rewrite.
