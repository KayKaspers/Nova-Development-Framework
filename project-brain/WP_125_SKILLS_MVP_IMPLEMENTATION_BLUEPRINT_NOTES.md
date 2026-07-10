# NDF-WP-125 – Skills MVP Implementation Blueprint (Notes)

## Ziel

Blueprint für ein späteres, docs-only, fail-closed NDF Skills Pack MVP erstellen — mit Fokus auf Token-Economy, Claude-Usage-Limit-Schonung, weniger Prompt-Overhead, sichere WP-Ausführung, Public Neutrality, ADR-0032-Konformität, v1.0-Alltagstauglichkeit und klarer Trennung Skill/Project Knowledge/Prompt. WP-125 erstellt **nur** den Blueprint; kein aktives Skill Pack.

## Ergebnis

**GO WITH NOTES – WP-129 recommended with constrained docs-only MVP scope.** Start-Gate bestanden (WP-133 committet `6bb1697`, Working Tree sauber). Kein Blocker gefunden.

## Input Summary

ADR-0031, ADR-0032 / Skill Security Policy, Skills MVP Design (WP-111), Skills MVP Decision (WP-124, Option B), Prompt Modes (WP-113), Context Economy (WP-109), Context Pack Template + Foundation 0.9 Context Pack, 0.9-Evidence (WP-122/123/126), WP-133 Reconciliation Notes.

## Skill-Kandidaten (bewertet)

Zehn Kandidaten bewertet: `ndf-work-package-runner`, `ndf-release-runner`, `ndf-public-neutrality-gate-runner`, `ndf-compact-context-summary-runner`, `ndf-adr-review-runner`, `ndf-security-review-runner`, `ndf-context-pack-maintainer`, `ndf-prompt-mode-selector`, `ndf-human-maintainer-handoff-runner`, `ndf-v1-readiness-review-runner`. Kriterien: Zweck, Token-Ersparnis, Risiko, docs-only-Eignung, v1.0-Relevanz, MVP-Relevanz, eigenständig vs integriert.

## Empfohlenes MVP Skill Set (4)

- `ndf-work-package-runner` (WP-Rahmen + Guardrails + Prompt-Mode-Auswahl; größter Overhead-Treiber)
- `ndf-compact-context-summary-runner` (Rückmeldung an Nova + Compact Context Summary + Handoff)
- `ndf-public-neutrality-guard` (Neutralitäts-/Secret-Namensregel-Erinnerung; ersetzt Gate nicht)
- `ndf-context-pack-maintainer` (Context Pack aktuell halten; Grundlage für Standard/Short Prompt Mode)

## Empfohlenes Extended Skill Set

`ndf-release-safety`, `ndf-adr-governance-review` (fasst ADR- + Security-Review), `ndf-v1-readiness-review`, ggf. `ndf-prompt-mode-selector` (nur falls integriert nicht reicht).

## Nicht empfohlene / zurückgestellte Skills

`ndf-release-runner` eigenständig im MVP (release-/tag-nah, selten), `ndf-security-review-runner` eigenständig (Risiko autonomer Sicherheitsurteile), `ndf-human-maintainer-handoff-runner` (redundant), `ndf-prompt-mode-selector` eigenständig (geringe Eigen-Ersparnis), `ndf-v1-readiness-review-runner` im MVP (selten, Full-Pflicht). Kategorisch nie als Skill: Git-/Release-Aktionen, Scripts, Netzwerk, Secret-Werte, private Projektlogik.

## Wichtige Design-Klarstellung

Kandidat 3 wird als `ndf-public-neutrality-guard` (nicht `-gate-runner`) geführt: „Runner" auf dem Gate würde Script-Ausführung implizieren — nach ADR-0032 im MVP verboten. Der reale Gate (`scripts/check_public_quality.py`) bleibt separat und maßgeblich.

## Token-Economy-Einschätzung

Entfallbar (sehr hoch/hoch): Rollenbeschreibung, harte Grenzen, Neutralitäts-/Secret-Regeln, Abschlussformat, Rückmeldung an Nova, Compact Context Summary, Self-Check. Bleibend: WP-Ziele, Aufgaben, Dateipfade, Commit-Message, WP-Sonderregeln, erwartetes Ergebnis. Reduktion qualitativ hoch–sehr hoch (Zielkorridor, keine exakte Zahl). Risiko Over-Compression → Guardrails wandern in Skills, Short-Prompt-Verbotsliste bleibt bindend.

## Skill vs Project Knowledge vs Prompt

Skill = stabile öffentliche Verhaltensregeln (Rolle, Human-only, Neutralität, Secret-Regeln, Abschlussformate, Self-Check, Modus-Vorschlag). Project Knowledge = stabiler öffentlicher Kontext (ADR-Texte, Prompt-Mode-Definitionen, Phasenstatus/Context Pack, Known Notes, v1.0 Notes, Modellregel). Prompt = WP-spezifisch (Ziele, Dateipfade, Commit-Message, Sonderregeln).

## Security / ADR-0032 Bewertung

Alle empfohlenen Skills: docs-only, fail-closed, keine Scripts/Netz/Secrets/privaten Daten, keine Git-/Release-/Tag-Aktionen, jede Ausgabe ein Vorschlag. Secret-Name `NDF_PUBLIC_NEUTRALITY_DENYLIST` darf genannt werden, Wert nie. ADR-0032 unverändert bindend, nicht gelockert.

## Public-Neutrality-Bewertung

Gate v0.2 `--strict` + `--self-test` grün, new-file neutrality check aktiv. Keine privaten Projektnamen, Domains, Suchmuster, Reviewer-Identitäten, Secret-Werte. Zulässige Rollenformulierung DE/EN eingehalten.

## Empfehlung zu WP-129

**Bedingt aktivieren (Ja, enger Scope):** genau die vier MVP-Skills, docs-only, fail-closed; Bedingungen — ausdrücklicher Human-Maintainer-Scope-Change, ADR-0032 bindend, Gate grün, 13-Punkte-Validierungsplan als Abnahme. Fehlend: formale Aktivierungsentscheidung + Prompt-Vorher/Nachher-Nachweis (im WP-129-Start zu erbringen). WP-125 setzt WP-129 nicht um.

## Skill-Nichtaktivierung

Kein `.claude/skills`, keine `SKILL.md`, keine Skill-Dateien, keine Scripts angelegt. WP-129/130/131/132 nicht aktiviert. Kein aktives Skill Pack nach WP-125.

## Geänderte / neue Dateien

- **NEU** `docs/validation/foundation-0-9/SKILLS_MVP_IMPLEMENTATION_BLUEPRINT.md`
- **NEU** `project-brain/WP_125_SKILLS_MVP_IMPLEMENTATION_BLUEPRINT_NOTES.md` (diese Notiz)
- `docs/roadmap/FOUNDATION_0_9_WORK_PACKAGES.md` (WP-125-Zeile: Blueprint erledigt)
- `docs/roadmap/FOUNDATION_0_9_PLAN.md` (dokumentarischer Hinweis WP-125)
- `project-brain/NEXT_PHASE_FOUNDATION_0_9.md` (Next WP → WP-129 bedingt empfohlen)
- `project-brain/CONTEXT_PACK_FOUNDATION_0_9.md` (Last/Next WP, History, Next Prompt Recommendation)

## Risiken / offene Punkte

Scope Creep (Blueprint ≠ Implementierung), Over-Compression, Neutralitäts-Fehldeutung (`-guard` ≠ Gate-Runner), Skill-Overlap (bewusst integriert), Blueprint-Verfall (vor WP-129 erneut prüfen), kein Zahlenversprechen bei Token-Ersparnis.

## Nächster empfohlener Schritt

**NDF-WP-129 – Docs-only Skills MVP Implementation** — nur mit ausdrücklichem Human-Maintainer-Scope-Change und engem Scope (die vier MVP-Skills), ADR-0032-konform, docs-only. WP-130/131/132 bleiben optional/nicht aktiviert.
