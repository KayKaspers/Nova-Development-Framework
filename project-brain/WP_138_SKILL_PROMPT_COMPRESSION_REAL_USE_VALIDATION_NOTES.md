# NDF-WP-138 – Skill Prompt Compression Real-use Validation (Notes)

## Ziel

Real-use-Validierung des acht-teiligen NDF-Skill-Packs für Prompt-Kompression/Token-Economy und Bewertung der offenen Notes DSK-001 und ECS-001. Keine neuen Skills, keine Skill-Änderungen.

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-137 committet `7caab18`, Working Tree sauber, genau acht Skills). Gate v0.2 grün. Kein Blocker.

## Skills geprüft

Acht Skills, alle Markdown-only, ADR-0032-konform, real-use-tauglich: Core-MVP (`ndf-work-package-runner`, `ndf-compact-context-summary-runner`, `ndf-public-neutrality-guard`, `ndf-context-pack-maintainer`) + Extended-Core (`ndf-skill-quality-reviewer`, `ndf-existing-project-analysis-runner`, `ndf-docs-polish-runner`, `ndf-changelog-writer`). Keine Scripts/ausführbaren Dateien; keine optionalen Release-/ADR-Skills; ADR-0032 unverändert.

## Prompt-Kompressionsbefund (vier Real-use-Fälle)

- Normaler Doku-/Review-WP: ~45–60 %, Governance unverändert, geeignet.
- Skills-/Governance-WP: ~30–45 % (Rahmen hoch, Substanz gering), Governance verbessert (Skill-Review-Checkliste), geeignet mit Notes (Full Pflicht).
- Existing-Project-Analysis-WP: ~40–55 %, Governance verbessert (Neutralitätsgrenze strukturell), geeignet mit Notes.
- Changelog-/Docs-Polish-WP: ~50–65 %, Governance unverändert, geeignet.

## DSK-001 / ECS-001 Status

- **DSK-001 → Closed with notes** (Kern-Skills seit WP-134 über mehrere reale WPs genutzt; strukturell + praktisch belegt; keine exakte Token-Instrumentierung, ADR-0032-konform nicht möglich).
- **ECS-001 → Partially closed** (Extended-Core-Skills erst seit WP-137, kurze Nutzungshistorie; voller Abschluss nach breiterer Anwendung).

## Skills-first Default Entscheidung

**Bestätigt mit Notes.** Standard = Default (normale WPs); Full = Security/Release/ADR/v1.0/neue Skills; Short = kleine Checks mit Context Pack. Note: Governance-/Release-/v1.0-Substanz bleibt explizit; Extended-Core-Skills brauchen breitere Nutzung (ECS-001) vor weiterer Lockerung.

## Roadmap-Empfehlung

**Option A: WP-139 – v1.0 Gap Review & Scope Lock.** Skill-Pack genügt, um den v1.0-Pfad strukturiert zu prüfen. Optionale Governance-Skills (release-safety, adr-governance-review, v1-readiness-review) und Project-Enablement bleiben Kandidaten, innerhalb/nach dem Gap Review priorisierbar — kein Blocker. Bewertete Alternativen: B (Project Enablement Blueprint), C (Additional Core Governance Skills Blueprint).

## Geänderte / neue Dateien

- **NEU** `docs/validation/foundation-0-9/SKILL_PROMPT_COMPRESSION_REAL_USE_VALIDATION.md`
- **NEU** `project-brain/WP_138_SKILL_PROMPT_COMPRESSION_REAL_USE_VALIDATION_NOTES.md` (diese Notiz)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Security / ADR-0032 / Public Neutrality

ADR-0032 unverändert bindend; keine neuen/geänderten Skills; `.claude/skills` unverändert; keine Scripts/Netz/Secrets/privaten Daten/Git-Release-Aktionen; keine privaten Projektnamen/Domains; Secret-Name nur als Name; Gate grün.

## Risiken / offene Punkte

ECS-001 teilweise offen (breitere Real-use-Historie); keine exakte Token-Messung (Schätzbereiche); Over-Compression (Full-Pflichtfälle + Short-Verbotsliste bindend, Substanz explizit); Skills advisory ≠ Gate.

## Nächster empfohlener Schritt

**NDF-WP-139 – v1.0 Gap Review & Scope Lock** (Full Prompt Mode, Opus 4.8).

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-138 hat das acht-teilige Skill-Pack real-use-validiert (GO WITH NOTES): reale Prompt-Overhead-Reduktion ~40–65 % je Prompt-Typ, Governance stabil/verbessert. DSK-001 Closed with notes, ECS-001 Partially closed. Skills-first Standard-Default bestätigt mit Notes. Keine neuen/geänderten Skills; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0. Nächster Schritt: WP-139 v1.0 Gap Review & Scope Lock.
