# NDF-WP-141 – v1.0 Release Criteria Finalization (Notes)

## Ziel

Die v1.0 Release Criteria auf Basis von WP-139 (Gap Review) und WP-140 (External Validation Evidence Review) finalisieren: RC-Kriterien und Final-Kriterien trennen, G-13-Schwelle festlegen, zulässige RC-Notes und Final-Blocker definieren, Skills-vor-RC/final bewerten, nächste WPs festlegen. Kein RC, keine v1.0-Aktivierung.

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-140 committet `13af69c`, Working Tree sauber). Gate v0.2 grün. Kein Blocker.

## v1.0 Release Criteria Summary

- **RC Criteria:** RC-01…RC-13 (Gate grün, Neutralität, README, Prompts, Release-Prozess, Human-Maintainer-only, ADR-Policy/ADR-0031/0032, ≥1 unabhängiger Lauf, Konventions-Stabilität, Changelog mit sichtbaren RC-Notes, Prompt-Entscheidungslogik, docs-only Skill-Pack, Selbstkonsistenz). Bedingung: alle met oder met with notes (akzeptierte, sichtbare Note).
- **Final Criteria:** F-01…F-07 (External Validation met oder dokumentierte Grenze; externer Einstieg unabhängig bestätigt; volle v1.x-Zusage im v1.0 Scope Lock aktiviert; Prompt-Entscheidungslogik vollständig oder Randbestand als Non-Goal; RC-Feedback triagiert; alle RC-Notes geschlossen/akzeptiert; Final Readiness + Prep + manuelle Freigabe).
- **Allowed RC Notes:** G-13 tracked, ECS-001 partially closed, keine volle v1.x-Zusage vor final, RC ≠ final, Project-Enablement optional/post-v1.0, Governance-Skills optional, zweiter Fixture-Typ dokumentierte Grenze.
- **Final Blockers:** Gate nicht grün; Secret/private Daten/Reviewer-Identitäten in Public NDF; ADR-0031/0032 gebrochen; v1.x-Policy unklar bei Claim; autonome Git-/Release-Aktionen durch AI; Skills mit Scripts/Netz/Secrets ohne neue ADR; G-13 weder vertieft noch als akzeptierte Grenze dokumentiert; Kriterien inkonsistent; v1.0-Claims vor Freigabe.

## G-13 Behandlung

- **RC:** RC can proceed with notes; G-13 bleibt tracked; keine Blockade bei sichtbarer Note; RC darf Validierungsvehikel sein.
- **v1.0 final:** eine von zwei Schwellen — **Weg A** (tieferer öffentlicher neutraler Lauf mit Schrittbelegen → `met`) **oder Weg B** (dokumentierte akzeptierte Grenze/Known Limitation, ehrlich/sichtbar/begründet). Keine erfundene Evidenz; Wegwahl im Final Readiness Review, Human-Maintainer-bestätigt.

## Skills-Bewertung

Achtteiliges Skill-Pack reicht für v1.0-Core (WP-138); keine zusätzlichen Skills sind RC-Blocker; `ndf-release-safety`/`ndf-adr-governance-review` optional; Project-Enablement optional/post-v1.0; neue Skills vor RC nur bei Human-Maintainer-Scope-Change, ADR-0032-konform.

## Nächste WPs

Kein Zwischen-WP nötig. WP-142 v1.0 RC Readiness Review → WP-143 v1.0 RC Release Prep → manueller RC-Release (Human Maintainer) → RC-Feedback-Triage → v1.0 Final Readiness (G-13-Weg A/B) → v1.0 Final Prep → manuelle v1.0-Freigabe.

## Geänderte / neue Dateien

- **NEU** `docs/release/V1_0_RELEASE_CRITERIA.md`
- **NEU** `project-brain/WP_141_V1_0_RELEASE_CRITERIA_FINALIZATION_NOTES.md` (diese Notiz)
- `docs/roadmap/V1_0_PATH_SUMMARY.md` (dokumentarisch)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Security / ADR-0031 / ADR-0032 / Public Neutrality

ADR-0031/0032 unverändert bindend; volle v1.x-Zusage erst mit v1.0 (F-03); keine v1.0-Aktivierung/RC; keine Skills geändert/erstellt; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; keine Reviewer-Identitäten/privaten Namen/Domains; Secret-Name nur als Name; Gate grün. Nächste freie ADR-Nummer: 0033.

## Risiken / offene Punkte

G-13 zentraler v1.0-final-Vorbehalt (Weg A oder B vor final); Ein-Personen-Engpass (stützt ggf. Weg B); Kriterien-Drift kontrolliert durch diesen Lock; kein Zeitplan; kein v1.0-Claim.

## Nächster empfohlener Schritt

**NDF-WP-142 – v1.0 RC Readiness Review** (Full/Skill-assisted Full Prompt Mode, Opus 4.8).

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-141 hat die v1.0 Release Criteria finalisiert (RC-Kriterien RC-01…13, Final-Kriterien F-01…07 getrennt), die G-13-Schwelle festgelegt (RC mit Notes; v1.0 final Weg A tieferer Lauf oder Weg B akzeptierte Grenze), Allowed RC Notes und Final Blockers definiert. Achtteiliges Skill-Pack reicht für v1.0-Core; keine v1.0-Aktivierung/RC; ADR-0031/0032 unverändert; Foundation 0.9 bleibt nicht v1.0. Nächster Schritt: WP-142 v1.0 RC Readiness Review.
