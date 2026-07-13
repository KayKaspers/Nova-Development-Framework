# NDF-WP-150 – v1.1 Planning / Post-v1.0 Roadmap (Notes)

## Ziel

Den ersten Post-v1.0-Zyklus planen: Ausgangslage nach v1.0.0 dokumentieren, aktive v1.x-Zusage (ADR-0031) berücksichtigen, Known Final Notes (WP-149) in Roadmap-Items überführen, v1.1-Scope + Breaking-/Non-Breaking-Grenzen definieren, nächste WPs priorisieren. Nur Planung; kein v1.1-Release.

## Ergebnis

**GO WITH NOTES – v1.1 planning started.** Start-Gate bestanden (WP-149 committet `eeb2124`, Working Tree sauber, Tag `v1.0.0` → `9dcadc1`, RC-Tag unverändert, 38 Skills). Gate v0.2 grün. Kein Blocker.

## Kontext-Hinweis (Human-Maintainer-Commit)

An HEAD liegt ein neuerer Human-Maintainer-Commit (`d08e35e docs(validation): review first project feedback intake`, zwei project-local Intake-Dokumente). Das ist der **erste reale Projekt-Feedback-Intake** post-v1.0 und adressiert die „kein externes RC-Feedback"-Grenze teilweise. **Neutralität:** der projektspezifische Name/die Details werden **nicht** in meine v1.1-Planungsdokumente übernommen; ich referenziere nur neutral „erster realer Projekt-Feedback-Intake (project-local)".

## v1.1-Scope

**v1.1 = Validation, Enablement & Operational Maturity.** Skills Real-use Review; External Validation Improvement (G-13-Weg A); Project Enablement Validation (Feedback-Intake einbeziehen); Public Documentation Polish; v1.x compatibility maintenance; post-v1.0 risk reduction. Nicht-Ziele: Breaking Changes, inkompatible Prompt-Strukturen, nicht-ADR-konforme Skill-Automation, Netz-/API-/MCP-/Script-Skills ohne neue ADR, private Projektlogik im Public NDF, v1.1-Release durch dieses WP.

## Wichtigste Entscheidungen

- v1.1 bleibt in der v1.x-Kompatibilität; Erweiterungen additiv; Breaking Changes nur per Deprecation/ADR + Human Maintainer.
- WP-Nummerierung: saubere aufsteigende Reihenfolge WP-151…156 übernommen; ersetzt die vorläufige WP-149-Zuordnung (152/153/151/154).
- „kein externes RC-Feedback" von accepted limitation → **teilweise adressiert** durch den ersten Projekt-Feedback-Intake (speist WP-152/153).

## Empfohlene WP-Reihenfolge

WP-151 Skills Real-use Review (P0) → WP-152 External Validation Improvement / G-13-Weg A (P1) → WP-153 Project Enablement Validation (P1) → WP-154 Public Documentation Polish (P2) → WP-155 v1.1 Readiness Review → WP-156 v1.1 Release Prep (nur Doku). Begründung: Betriebs-Evidenz zuerst, dann größter v1.0-Vorbehalt, dann Enablement mit realem Feedback, dann Doku, dann Readiness/Prep.

## v1.x-Kompatibilitätsgrenzen

- Non-breaking: additive docs-only Skills/Doku/Roadmap-Updates, Klarstellungen, optionale Prompt-Profile.
- Needs ADR: Skill-Security-Scope-Erweiterung (Scripts/Netz/Secrets/Automation), Lockerung ADR-0031/0032, neue Fähigkeitsklassen, Denylist-Governance-Änderung.
- Breaking: Entfernen/Umbenennen genutzter Skills, inkompatible Prompt-Mode-Semantik, nicht-additive Adapter-Konventionen, Entfernen öffentlicher Einstiegspunkte.
- Human-Maintainer-only: Commit/Push/Tag/Release, ADR-Annahme, v1.1-Release, Scope-Changes, GO/REWORK/STOP.

## Geänderte / neue Dateien

- **NEU** `docs/roadmap/V1_1_PLAN.md`
- **NEU** `project-brain/WP_150_V1_1_PLANNING_AND_POST_V1_0_ROADMAP_NOTES.md` (diese Notiz)
- `docs/roadmap/V1_0_PATH_SUMMARY.md`, `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Security / ADR-0031 / ADR-0032 / Public Neutrality

ADR-0031 aktiv im v1.x-Kontext, unverändert; ADR-0032 unverändert bindend; keine v1.1-Veröffentlichung/kein Tag/Release durch AI; keine Skills geändert/erstellt; keine Scripts/Netz/Secrets/privaten Daten; keine privaten Projektnamen/Domains/Reviewer-Identitäten (Feedback-Intake nur neutral referenziert); Secret-Name nur als Name; Gate grün. Nächste freie ADR-Nummer: 0033.

## Risiken / offene Punkte

Skill-Sprawl (38 Skills, WP-151); G-13-Weg A braucht realen öffentlichen Lauf (Ein-Personen-Engpass, WP-152); Projekt-Feedback-Neutralität (project-local, WP-153); Breaking Changes vermeiden; kein Zeitplan; kein Scope Lock.

## Nächster empfohlener Schritt

**NDF-WP-151 – Skills Real-use Review** (Skill-assisted Standard/Full Prompt Mode, Opus 4.8).

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-150 hat die v1.1-Planung gestartet (GO WITH NOTES): v1.0.0 bleibt final released, v1.x-Zusage aktiv (ADR-0031); v1.1 = Validation, Enablement & Operational Maturity, nur geplant; Known Final Notes in WP-151…156 überführt; v1.x-Kompatibilitätsgrenzen dokumentiert; erster realer Projekt-Feedback-Intake neutral einbezogen. Keine Breaking Changes/neue Skills/Releases; ADR-0031/0032 unverändert. Nächster Schritt: WP-151 Skills Real-use Review.
