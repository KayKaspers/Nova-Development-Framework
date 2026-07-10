# NDF-WP-143 – v1.0 RC Release Prep (Notes)

## Ziel

Den ersten v1.0 Release Candidate (`v1.0.0-rc.1`) als **Dokumentation** vorbereiten: RC Release Notes, RC Go/No-Go-Checkliste, RC Tagging-/GitHub-Release-Guide, sichtbare Known RC Notes, Human-Maintainer-only-Schritte. **Kein Tag, kein GitHub Release, keine v1.0-Final-Aktivierung, keine volle v1.x-Zusage.**

## Ergebnis

**GO WITH NOTES – v1.0 RC prepared, pending Human Maintainer release.** Start-Gate bestanden (WP-142 committet `b87f1b6`, Working Tree sauber). Gate v0.2 grün. Kein Blocker.

## Erzeugte RC-Release-Artefakte

- `docs/release/V1_0_RC_1_RELEASE_NOTES.md` — Titel „Nova Development Framework v1.0.0-rc.1 Release Candidate"; Status RC/nicht final; was validiert wird; enthaltene Ergebnisse (Foundation 0.9, WP-125…142); Known RC Notes; Usage-/Human-Maintainer-Hinweise.
- `docs/release/V1_0_RC_1_GO_NO_GO_CHECKLIST.md` — RC-01…13-Prüfung, Allowed RC Notes, Final Blockers Check, weitere Checks, finale Entscheidung (Human Maintainer); RC-01/RC-10 commit-gebunden markiert.
- `docs/release/V1_0_RC_1_TAGGING_AND_GITHUB_RELEASE_GUIDE.md` — Tag `v1.0.0-rc.1` (annotated), Titel „… v1.0.0 Release Candidate 1", Pre-release/RC (nicht Latest); Human-Maintainer-Schritte; Rollback-/Correction-Hinweis; Post-Release-Follow-up WP-144.

## Bekannte RC Notes (sichtbar dokumentiert)

G-13 tracked (kein RC-Blocker); ECS-001 partially closed; RC ≠ final; volle v1.x-Zusage erst mit finalem v1.0; Project-Enablement-Skills optional/post-v1.0; optionale Governance-Skills optional; zweiter Fixture-Typ dokumentierte Grenze; RC-01 (Gate) und RC-10 (Changelog/RC-Notes) auf dem RC-Commit erneut bestätigen.

## Human-Maintainer-only Schritte

git status → Gate erneut (grün, RC-01) → Changelog prüfen (RC-10) → commit → push → annotated Tag `v1.0.0-rc.1` → tag push → GitHub Pre-Release (RC, nicht Latest) → Body aus RC Release Notes → Nachprüfung. Nur der Human Maintainer; kein AI-Agent.

## Was nicht getan wurde

Kein Commit/Push/Tag/GitHub-Release durch Claude; kein RC veröffentlicht; v1.0 final nicht aktiviert; volle v1.x-Zusage nicht aktiviert; keine neuen/geänderten Skills; keine Scripts/Netz/Secrets/privaten Daten; keine Reviewer-Identitäten/privaten Namen/Domains.

## Geänderte / neue Dateien

- **NEU** die drei RC-Release-Dokumente (oben) + `project-brain/WP_143_V1_0_RC_RELEASE_PREP_NOTES.md` (diese Notiz)
- `docs/roadmap/V1_0_PATH_SUMMARY.md`, `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Security / ADR-0031 / ADR-0032 / Public Neutrality

ADR-0031/0032 unverändert bindend; keine v1.0-Final-Aktivierung/kein veröffentlichter RC; keine autonomen Git-/Release-Aktionen; keine Skills geändert; keine Scripts/Netz/Secrets/privaten Daten; Secret-Name nur als Name; Gate grün. Nächste freie ADR-Nummer: 0033.

## Nächster Schritt

**Human Maintainer:** Commit/Push/annotated Tag `v1.0.0-rc.1`/GitHub Pre-Release gemäß Go/No-Go + Tagging-Guide. **Danach:** NDF-WP-144 – v1.0 RC Feedback Triage / RC Post-Release Review (G-13-Weg A/B für v1.0 final vorbereiten).

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-143 hat `v1.0.0-rc.1` als Dokumentation vorbereitet (Release Notes, Go/No-Go, Tagging-Guide) mit sichtbaren Known RC Notes und Human-Maintainer-only-Schritten. Kein Tag/Release durch Claude, kein v1.0 final, keine volle v1.x-Zusage. G-13 bleibt tracked; RC-01/RC-10 auf RC-Commit erneut bestätigen. ADR-0031/0032 unverändert. Ergebnis: GO WITH NOTES – v1.0 RC prepared, pending Human Maintainer release. Nächster Schritt: Human-Maintainer-RC-Release, danach WP-144.
