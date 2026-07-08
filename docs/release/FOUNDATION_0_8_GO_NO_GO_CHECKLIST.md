# Foundation 0.8 Go/No-Go Checklist

## DE – Zweck

Finale Prüfung vor Tag und GitHub Release `v0.8.0-foundation`. Durchführung durch den **Human Maintainer**; der Implementation Agent erstellt weder Tag noch Release.

## EN – Purpose

Final check before tag and GitHub release `v0.8.0-foundation`. Performed by the **Human Maintainer**; the Implementation Agent creates neither tag nor release.

## DE – Status

**Vorbereitet (Release Prep, NDF-WP-115).** Foundation 0.8 ist **noch nicht released**; der Tag `v0.8.0-foundation` ist noch nicht gesetzt.

## EN – Status

**Prepared (release prep, NDF-WP-115).** Foundation 0.8 is **not yet released**; the tag `v0.8.0-foundation` is not yet set.

## DE – Vor dem Release / EN – Before Release

```powershell
git status
git branch --show-current
git tag --list v0.8.0-foundation
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
```

- [ ] Working Tree sauber vor dem Tagging / working tree clean before tagging.
- [ ] Branch ist `main`.
- [ ] Public Quality Gate `--strict` passed.
- [ ] Public Quality Gate `--self-test` passed.
- [ ] `v0.8.0-foundation` existiert noch nicht vor dem manuellen Tagging.

## DE – Release-blocking Kriterien / EN – Release-Blocking Criteria

- [ ] Readiness Review ist GO WITH NOTES oder besser (WP-114).
- [ ] WP-108 done.
- [ ] WP-109 done.
- [ ] WP-110 done.
- [ ] WP-111 done.
- [ ] WP-113 done.
- [ ] WP-114 done.
- [ ] WP-115 docs prepared (Release Notes, diese Checkliste, Tagging-Guide).
- [ ] Release Notes geprüft.
- [ ] Tagging Guide geprüft.

## DE – Sicherheits- und Neutralitätskriterien / EN – Security and Neutrality Criteria

- [ ] Keine privaten Projektnamen, Reviewer-Daten, Kontaktwege, echten Domains oder Secret-Werte in getrackten Dateien.
- [ ] Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name (nie Wert/Denylist-Begriffe).
- [ ] Public Quality Gate new-file neutrality check aktiv.

## DE – Skill-Pack-Kriterien / EN – Skill Pack Criteria

- [ ] WP-112 optional und nicht aktiviert.
- [ ] Kein aktives Claude Skills Pack.
- [ ] Keine `.claude/skills`.
- [ ] Keine `SKILL.md`.
- [ ] Keine neuen Skill-Scripts.

## DE – v1.0-Abgrenzung / EN – v1.0 Boundary

- [ ] ADR-0031 accepted; ADR-0032 accepted; nächste freie ADR-Nummer ADR-0033.
- [ ] Foundation 0.8 nicht v1.0, kein v1.0 Release Candidate.
- [ ] Volle v1.x-Kompatibilitätszusage nicht als aktiv dargestellt.

## DE – Manuelle Human-Maintainer-Entscheidung / EN – Manual Human Maintainer Decision

- [ ] Release-Titel „Nova Development Framework v0.8.0 Foundation" geprüft (kein Secret-Name, kein Platzhalter — Lehre aus dem 0.2-Titel-Fehler).
- [ ] Release-Typ Pre-release.
- [ ] Bestätigt: Der Implementation Agent hat keinen Tag und kein GitHub Release erstellt.
- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.

## DE – Ergebnis / EN – Result

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_8_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`.
