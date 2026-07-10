# Foundation 0.9 Go/No-Go Checklist

## DE – Zweck

Finale Prüfung vor Tag und GitHub Release `v0.9.0-foundation`. Durchführung durch den **Human Maintainer**; der Implementation Agent erstellt weder Tag noch Release.

## EN – Purpose

Final check before tag and GitHub release `v0.9.0-foundation`. Performed by the **Human Maintainer**; the Implementation Agent creates neither tag nor release.

## DE – Status

**Vorbereitet (Release Prep, NDF-WP-128).** Foundation 0.9 ist **noch nicht released**; der Tag `v0.9.0-foundation` ist noch nicht gesetzt. Erwartetes Ergebnis bei sauberem Durchlauf: `GO WITH NOTES – ready for manual release by Human Maintainer`.

## EN – Status

**Prepared (release prep, NDF-WP-128).** Foundation 0.9 is **not yet released**; the tag `v0.9.0-foundation` is not yet set. Expected result on a clean pass: `GO WITH NOTES – ready for manual release by Human Maintainer`.

## DE – Vor dem Release / EN – Before Release

```powershell
git status
git branch --show-current
git tag --list v0.9.0-foundation
python scripts/check_public_quality.py --strict
python scripts/check_public_quality.py --self-test
```

- [ ] Working Tree sauber vor dem Tagging (WP-127 + WP-128 committet).
- [ ] Branch ist `main`, in sync mit `origin/main`.
- [ ] Public Quality Gate `--strict` passed.
- [ ] Public Quality Gate `--self-test` passed.
- [ ] `v0.9.0-foundation` existiert noch nicht vor dem manuellen Tagging.

## DE – Scope Lock und Release-blocking WPs / EN – Scope Lock and Release-Blocking WPs

- [ ] Scope Lock vorhanden und eingehalten (`FOUNDATION_0_9_SCOPE_LOCK.md`, validation-first).
- [ ] WP-121 done · WP-122 done (GO WITH NOTES) · WP-123 done (GO WITH NOTES) · WP-124 done (Option B) · WP-126 done (GO WITH NOTES) · WP-127 done (GO WITH NOTES).
- [ ] WP-128 docs prepared (Release Notes, diese Checkliste, Tagging-Guide).
- [ ] Release Criteria aktuell; alle Kriterien bis auf finalen Tag/Release erfüllt.
- [ ] Release Notes geprüft (inkl. aller Known Notes).
- [ ] Tagging Guide geprüft.
- [ ] CHANGELOG vorbereitet (0.9-Sektion, „pending manual release", Not v1.0).
- [ ] Context Pack Foundation 0.9 aktuell (WP-128 done, Release-Schritt als nächstes).

## DE – Known Notes / EN – Known Notes

- [ ] Foundation 0.9 nirgends als v1.0 oder v1.0 RC dargestellt.
- [ ] Volle v1.x-Kompatibilitätszusage nirgends als aktiv dargestellt.
- [ ] Short-Prompt-Ersteinsatz-Note sichtbar (noch kein praktischer Einsatz).
- [ ] Externe Validierungs-Evidenz-Tiefe als v1.0-tracked sichtbar.
- [ ] WP-133 als Post-Release-Schritt dokumentiert (nicht vorgezogen).

## DE – ADR / Governance / EN – ADR / Governance

- [ ] ADR-0031 accepted und unverändert.
- [ ] ADR-0032 accepted und unverändert.
- [ ] Nächste freie ADR-Nummer: ADR-0033.

## DE – Skill Security / EN – Skill Security

- [ ] Kein aktives Claude Skills Pack.
- [ ] Keine `.claude/skills`.
- [ ] Keine `SKILL.md`.
- [ ] Keine neuen Skill-Scripts.
- [ ] WP-125 optional/conditional (nicht aktiviert); WP-129 optional/nicht aktiviert; WP-130/131/132 optional.

## DE – Public Neutrality / EN – Public Neutrality

- [ ] Keine privaten Projektnamen, Reviewer-Daten, Kontaktwege, echten Domains oder Secret-Werte in getrackten Dateien.
- [ ] Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name (nie Wert/Denylist-Begriffe).
- [ ] New-file neutrality check aktiv.

## DE – Tagging / GitHub Pre-Release Readiness / EN – Tagging / Release Readiness

- [ ] Tag geplant als **annotated**: `v0.9.0-foundation`.
- [ ] Release-Titel „Nova Development Framework v0.9.0 Foundation" geprüft (kein Secret-Name, kein Platzhalter — Lehre aus dem 0.2-Titel-Fehler).
- [ ] Release-Typ **Pre-release**.
- [ ] Release Body enthält „This is not a v1.0 release.", die v1.x-Nicht-aktiv-Aussage und „No active Claude Skills Pack".

## DE – Human-Maintainer-Handoff / EN – Human Maintainer Handoff

- [ ] Bestätigt: Der Implementation Agent hat keinen Tag und kein GitHub Release erstellt.
- [ ] Der Human Maintainer hat alle Punkte geprüft und gibt den Release frei.
- [ ] Nach dem Release: WP-133 Post-Release Cleanup einplanen.

## DE – Ergebnis / EN – Result

```text
Datum / Date:        __________
Entscheidung / Decision:  GO | GO WITH NOTES | NO-GO
Begründung / Reason: __________
Freigabe / Approved by (Human Maintainer): __________
```

Bei GO: weiter mit `docs/release/FOUNDATION_0_9_TAGGING_AND_GITHUB_RELEASE_GUIDE.md`.
