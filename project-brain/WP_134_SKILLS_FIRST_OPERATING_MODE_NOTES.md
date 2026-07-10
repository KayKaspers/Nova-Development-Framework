# NDF-WP-134 – Skills-first Operating Mode & Prompt Compression Validation (Notes)

## Ziel

Das in WP-129 implementierte Docs-only Skills MVP in den laufenden NDF-Arbeitsmodus einbinden (Skills-first Operating Mode) und die reale Prompt-Kompression/Token-Economy validieren, ohne NDF-Governance zu schwächen. DSK-001 mindestens teilweise schließen. Keine neuen/Extended Skills.

## Reconciliation-Hinweis

Der Human Maintainer hat zwei WP-134-Varianten eingefügt („Skills Prompt Compression Validation" und „Skills-first Operating Mode & Prompt Compression Baseline"). Sie sind komplementär; WP-134 wurde als **ein** kohärentes Paket ausgeführt: ein Validierungsdokument + ein Operating-Mode-Dokument + diese Notes.

## Ergebnis

**GO WITH NOTES.** Start-Gate bestanden (WP-129 committet `4f93582`, Working Tree sauber, vier MVP-Skills vorhanden). Gate v0.2 grün (0/0/3). Kein Blocker.

## Verwendete Skills (verhaltensbasiert, docs-only Repo-Artefakte)

`ndf-work-package-runner`, `ndf-compact-context-summary-runner`, `ndf-public-neutrality-guard`, `ndf-context-pack-maintainer` — geprüft: vorhanden, docs-only, ADR-0032-konform, für Prompt-Kompression nutzbar. Sie ersetzen keine Gates/Human Review und führen keine Git-/Release-Aktionen aus.

## Prompt-Kompressionsbefund

Drei repräsentative Prompt-Typen (Vorher/Nachher) verglichen:
- Normaler WP: Ersparnis **hoch** (~40–60 % Overhead), Governance unverändert, geeignet.
- Release-/Post-Release: Ersparnis **mittel** (~25–40 %), release-kritische Grenzen bleiben explizit, geeignet mit Notes (Full Pflicht).
- Skills-/Governance: Rahmen **hoch**, Substanz **gering** (~30–45 % gesamt), Governance unverändert, geeignet mit Notes (Full Pflicht).

Zielprofile (Korridore, keine exakten Tokenversprechen): Short ~20–30 %, Standard ~40–55 %, Full ~60–75 % der bisherigen Full-Basis.

## Neue Prompt-Profile

- **Short (skill-assisted):** kleine Checks/Statuspflege/einfache Doku.
- **Standard (skill-assisted):** normale WPs/Blueprints/Reviews — **neuer Default**.
- **Full (skill-assisted):** Release/ADR/Security/v1.0/neue Skill-Implementierungen — bleibt Pflicht für kritische Fälle.

## DSK-001 Status

**Partially closed** — strukturelle Kompressions-Baseline erstellt; empirische Real-Use-Messung bleibt offen (ADR-0032 verbietet Scripts/Instrumentierung hier). Vollständiger Abschluss über eine spätere Real-use-Validierung (WP-139).

## Governance / ADR-0032 / Public Neutrality

Public Neutrality, ADR-0031, ADR-0032, Human-Maintainer-only, Rückmeldung an Nova, Compact Context Summary bleiben stabil. Skills tragen die Regeln, ersetzen keine Gates. ADR-0032 unverändert. Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` nur als Name, Wert nie. Gate grün, new-file neutrality check aktiv.

## Geänderte / neue Dateien

- **NEU** `docs/validation/foundation-0-9/SKILLS_PROMPT_COMPRESSION_VALIDATION.md`
- **NEU** `docs/validation/foundation-0-9/SKILLS_FIRST_OPERATING_MODE.md`
- **NEU** `project-brain/WP_134_SKILLS_FIRST_OPERATING_MODE_NOTES.md` (diese Notiz)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md`, `docs/roadmap/FOUNDATION_0_9_PLAN.md`
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md`, `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md`
- `CHANGELOG.md`

## Priorisierte nächste Skill-WPs (Kandidaten, nicht aktiviert)

WP-135 (External Skills Landscape & Project Skill Prioritization) → WP-136 (NDF Extended Skills Pack Blueprint) → WP-137 (Project Enablement Skills Blueprint) → WP-138 (Docs-only Extended Skills MVP Implementation) → WP-139 (Skill Prompt Compression Real-use Validation, schließt DSK-001) → v1.0 Gap Review & Scope Lock.

## Risiken / offene Punkte

DSK-001 teilweise offen (WP-139); Over-Compression (Full-Pflichtfälle + Short-Verbotsliste bindend); Skills ≠ Gates; keine Extended Skills/keine Aktivierung durch WP-134.

## Nächster empfohlener Schritt

**NDF-WP-135 – External Skills Landscape & Project Skill Prioritization** (docs-only, Skill-assisted Standard/Full Prompt Mode, empfohlenes Modell Claude Opus 4.8). Alternativ direkt **WP-139** (Real-use-Validierung), falls DSK-001-Abschluss priorisiert wird.

## Rückmeldung-an-Nova-kompatible Zusammenfassung

WP-134 hat den Skills-first Operating Mode dokumentiert und die Prompt-Kompression des MVP validiert (GO WITH NOTES). Strukturelle Kompression hoch–sehr hoch; DSK-001 Partially closed; Governance stabil; keine neuen/Extended Skills; ADR-0032 unverändert; Foundation 0.9 bleibt nicht v1.0. Nächster empfohlener Schritt: WP-135.
