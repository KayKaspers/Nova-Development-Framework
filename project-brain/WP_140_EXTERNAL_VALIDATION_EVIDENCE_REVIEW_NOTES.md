# NDF-WP-140 – External Validation Evidence Review (Notes)

## Ziel

Den wichtigsten offenen v1.0-Gap G-13 (External Validation Evidence Depth) aus WP-139 ehrlich prüfen: welche Evidenz existiert, wie belastbar sie ist, ob sie für einen v1.0 RC reicht, ob zusätzliche Validierung nötig ist, G-13-Status, und die WP-141-Entscheidung vorbereiten. Keine neue externe Validierung, keine erfundene Evidenz.

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-139 committet `29eb710`, Working Tree sauber). Gate v0.2 grün. Kein Blocker.

## Evidence-Quellen (read-only geprüft, im Repo vorhanden)

Zwei unabhängige Läufe (`docs/validation/project-adapter/independent-runs/`): 2026-07-06 privater Referenzkontext (WP-074, PASS WITH NOTES) und 2026-07-07 öffentliche SampleProject-Runbook-Validierung (WP-088, PASS WITH NOTES). Plus SampleProject Adapter Validation (WP-047), Convention Stability Review (WP-101), Gate Maintenance Review (WP-089), 0.9-Reviews (WP-122/123/126), Skill-Validationen (WP-138). Keine erfundene Evidenz.

## Evidence-Matrix (Zusammenfassung)

9 Quellen: **strong 2** (Konventions-Stabilität WP-101, Gate-Maintenance WP-089), **moderate 5**, **limited 1** (privater Referenzlauf WP-074), weak 0, insufficient 0. Wichtigste: E-01 öffentlicher unabhängiger Runbook-Lauf (WP-088, counts with notes) + E-04 Konventions-Stabilität (counts for v1.0). Wichtigste Limits: Schrittbeleg-Tiefe (E-01/E-02), Selbstvalidierungsanteil (E-03/E-07/E-08).

## G-13-Status

**Partially closed / remains tracked for RC.** Zwei echte unabhängige Läufe (PASS WITH NOTES, keine Blocker) → mehr als „open"; begrenzte Schrittbeleg-Tiefe + ein privat-kontextueller Lauf → nicht „Closed". Vor RC nicht nötig; vor v1.0 final nötig (tieferer schrittbelegter öffentlicher Lauf ODER dokumentierte akzeptierte Grenze).

## RC-Fähigkeit

**RC can proceed with notes.** RC ist Kandidat, kein finaler Vertrauensanspruch; darf als Validierungsvehikel dienen; vorhandene Evidenz + ehrliche Note tragen einen RC. v1.0 final muss stärker sein. Glaubwürdigkeitsrisiko gering bei ehrlicher RC-Note; Public Neutrality gewahrt.

## Empfohlene zusätzliche Validierung

Neutraler SampleProject-Re-Run mit Schrittbelegen (vor v1.0 final oder dokumentierte Grenze); zweiter unabhängiger Lauf (empfohlen); öffentlicher v1.0 RC dry-run (vor RC empfohlen); zweiter Fixture-Typ (optional/Non-Goal); Prompt-Mode-Validierung (optional); public-neutral reproducibility checklist + external reviewer checklist ohne Identität (empfohlen).

## Entscheidung für WP-141

**WP-141 bleibt `v1.0 Release Criteria Finalization`.** G-13 blockiert die Finalisierung nicht; die Finalisierung soll die G-13-Evidence-Note und die „vor v1.0 final"-Schwelle (RC vs. final) verbindlich verankern. Kein blockierender vorgeschalteter Validierungslauf; zusätzlicher Lauf als empfohlener pre-v1.0-final-Schritt/RC-dry-run in die Kriterien aufnehmen.

## Geänderte / neue Dateien

- **NEU** `docs/validation/v1-0/EXTERNAL_VALIDATION_EVIDENCE_REVIEW.md`
- **NEU** `project-brain/WP_140_EXTERNAL_VALIDATION_EVIDENCE_REVIEW_NOTES.md` (diese Notiz)
- `docs/roadmap/V1_0_PATH_SUMMARY.md` (dokumentarisch)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Security / ADR-0031 / ADR-0032 / Public Neutrality

ADR-0031/0032 unverändert bindend; keine v1.0-Aktivierung/RC; keine Skills geändert/erstellt; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; keine Reviewer-Identitäten/privaten Namen/Domains; Secret-Name nur als Name; Gate grün. Nächste freie ADR-Nummer: 0033.

## Risiken / offene Punkte

G-13 bleibt zentraler v1.0-final-Vorbehalt (tracked, kein RC-Blocker); Selbstvalidierungsanteil; Ein-Personen-Engpass begrenzt zusätzliche Läufe; kein Zeitplan; keine erfundene Evidenz.

## Nächster empfohlener Schritt

**NDF-WP-141 – v1.0 Release Criteria Finalization** (Full/Skill-assisted Full Prompt Mode, Opus 4.8).

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-140 hat G-13 (External Validation Evidence Depth) geprüft: zwei echte unabhängige Läufe (PASS WITH NOTES) + starke Governance-/Stabilitäts-Evidence, aber begrenzte Schrittbeleg-Tiefe → G-13 Partially closed / tracked for RC; RC can proceed with notes; v1.0 final braucht tiefere Evidenz oder dokumentierte Grenze. Keine erfundene Evidenz, keine v1.0-Aktivierung; ADR-0031/0032 unverändert; Foundation 0.9 bleibt nicht v1.0. Nächster Schritt: WP-141 v1.0 Release Criteria Finalization.
