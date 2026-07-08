# Next Phase – Foundation 0.7

## Status

**Scope locked** (NDF-WP-098, 2026-07-08) — verbindlich: `docs/roadmap/FOUNDATION_0_7_SCOPE_LOCK.md`. Release-blocking: 098 (done) · 099 (done) · **100 v1.x Compatibility Policy / ADR-0031** (ADR-0031 bevorzugt) · **101 Convention Stability Review** · 104 · 105. Optional: 102 (mit Upgrade-Ventil), 103, Doku-/i18n-Konsolidierung.

**Update (WP-099): Checklist DE/EN entschieden — Option B (optional mit finaler Begründung)** (`docs/roadmap/FOUNDATION_0_7_CHECKLIST_DE_EN_DECISION.md`): kein Blocker, kein Auto-Carry mehr, kein Folge-WP.

**Update (WP-100): v1.x Compatibility Policy als ADR-0031 angenommen** (`docs/adr/ADR-0031-v1x-compatibility-policy.md`, Status Accepted): Governance-Rahmen; aktive volle v1.x-Zusage erst mit v1.0; v1.0-Kriterium `met with notes`. Nächste freie ADR-Nummer: 0032.

**Update (WP-101): Convention Stability Review — Stable with notes** (`docs/validation/project-adapter/PROJECT_ADAPTER_CONVENTION_STABILITY_REVIEW.md`): Adapter-Konventionen seit WP-059 über 4 Releases unverändert; ein low-Drift (`.yaml`→`.md`) korrigiert; v1.0-Kriterium + Adapter-Maturity `met with notes`. Alle inhaltlichen blocking WPs erledigt; WP-102/103 nicht aktiviert (bleiben optional).

**Update (WP-104): Foundation 0.7 Release Readiness Review — GO WITH NOTES** (`docs/release/FOUNDATION_0_7_RELEASE_READINESS_REVIEW.md`): Alle release-blocking Kriterien außer WP-104/105 erfüllt und nachgewiesen; Gate strict/self-test grün, Kontroll-Greps sauber, Link-Check über 9 Kern-Dateien 0 broken. Notes ausschließlich non-blocking.

**Update (WP-105): Foundation 0.7 Release Prep — vorbereitet** (`docs/release/FOUNDATION_0_7_RELEASE_NOTES.md`, `..._GO_NO_GO_CHECKLIST.md`, `..._TAGGING_AND_GITHUB_RELEASE_GUIDE.md`): Release Notes (DE/EN, inkl. aller Known Limitations), 26-Punkte-Go/No-Go und Tagging-Guide erstellt; Criteria/CHANGELOG/README/Queue/Plan auf „prepared / tag pending" gehoben. Ein Future-Candidate-Hinweis aufgenommen: **NDF Agent Enablement & Context Economy** inkl. kleinem public-neutralen Claude Skills Pack — **kein Scope, kein blocking WP, in diesem WP nicht erstellt**. **Nächster Schritt: manuelles Go/No-Go + Tagging `v0.7.0-foundation` durch den Human Maintainer**, danach Post-Release-Status-Cleanup als eigenes WP. Nächste freie ADR-Nummer 0032. Noch nicht released, kein v1.0, keine aktive volle v1.x-Zusage.

## Current baseline

Foundation 0.6 released as `v0.6.0-foundation` (2026-07-07); vollständig abgeschlossen, keine offenen Follow-ups.

## Current recommendation

Arbeitstitel **Foundation 0.7 – v1.0 Path Consolidation & Compatibility Governance**: den v1.0-Pfad konsolidieren (Konventions-Stabilität bestätigen, ggf. Validierungstiefe erhöhen) und die Kompatibilitäts-Governance entscheiden (v1.x-Policy / ADR-0031) — ohne v1.0 zu behaupten. Je ein Kern-Deliverable pro Titel-Hälfte.

## Candidate work packages

- **Blocking-Kandidaten:** WP-098 Scope Lock · **WP-099 Checklist DE/EN Decision** (priorisieren/optional-mit-Begründung/streichen — kein viertes Verschieben) · **WP-100 v1.x Compatibility Policy / ADR-0031** · **WP-101 Convention Stability Review** · WP-104 Readiness · WP-105 Release Prep.
- **Optional:** WP-102 Evidence Depth Pass (hochstufbar), WP-103 Academy Entry Decision, Doku-/i18n-Konsolidierung.
- **Deferred/Nicht-Ziel:** Website, volle i18n, ADR-Massenmigration, v1.0-RC, Rewrite, App-Features.

## Open questions for WP-098

1. Wird WP-102 blocking — und mit welchem Ventil (personenabhängig)?
2. WP-099-Entscheidungskorridor verbindlich machen.
3. WP-100 als ADR-0031 oder reines Policy-Dokument?
4. Blocking/optional/deferred-Einstufung + Änderungsregeln.

## Known carry-overs from Foundation 0.6

- WP-091 Checklist DE/EN (seit 0.4 mehrfach offen) → WP-099-Entscheidung.
- WP-093 v1.x Compatibility Policy (v1.0-tracked) → WP-100 / ADR-0031-Kandidat.
- PSV-001 (WP-088 Evidence-Tiefe) → WP-102.
- WP-092 Academy Entry → WP-103.
- QGM-003 (Gate operational note) → Monitoring, kein WP nötig.
- Optionaler v0.6-Release-Body-Polish → manuell/kosmetisch, keine GitHub-Schreibaktion.

## Next recommended WP

**Manuelles Go/No-Go + Tagging `v0.7.0-foundation` durch den Human Maintainer** (WP-105 Release Prep vorbereitet, GO WITH NOTES). Danach Post-Release-Status-Cleanup als eigenes WP. Kein v1.0, keine aktive volle v1.x-Zusage.
