# Project Adapter Helper

> Sprachstatus / Language status: Foundation 0.2 document. DE/EN alignment pending according to `docs/i18n/DE_EN_LANGUAGE_STANDARD.md`.

## Zweck

Schnelle Entscheidungshilfe: wie viel Project Adapter braucht ein bestehendes Projekt?

Vollständiger Prozess: `docs/project-starter/PROJECT_ADAPTER_V0_2.md`

## Minimaladapter oder Volladapter?

| Situation | Empfehlung |
|---|---|
| kleines Projekt, ein Maintainer, wenig Risiko | Minimaladapter (Profile + Manifest + kleine Queue + Project Brain) |
| produktiv genutztes Projekt, mehrere Module | Volladapter (alle Phasen 0–10) |
| Projekt mit sicherheitsrelevanten oder destruktiven Funktionen | Volladapter, Security zuerst |
| nur Standortbestimmung gewünscht, noch keine NDF-Einführung | nur Phase 0–1 (Intake + Read-only Review) |

## Wann reichen Profile und Manifest?

Wenn das Projekt klein ist, keine riskanten Funktionen hat und zunächst nur nachvollziehbar dokumentiert werden soll. Capability Matrix, Compliance Check und Health Score können später als eigene Work Packages folgen.

## Wann ist der Health Score sinnvoll?

Sobald Fortschritt messbar werden soll — insbesondere vor größeren Verbesserungsphasen. Regel: erst Review-Evidenz (Docs-/Security-Review), dann Score. Ein Score ohne Evidenz ist wertlos.

## Wann kommt die Security Baseline zuerst?

Vor allen anderen Verbesserungen, wenn eines zutrifft:

- das Projekt ist öffentlich erreichbar oder wird es bald
- es verarbeitet fremde Daten oder Accounts
- Secret-Handling ist unklar
- Abhängigkeiten sind lange nicht aktualisiert worden

## Wann ist ein Destructive-Action-Review nötig?

Sobald das Projekt Funktionen hat, die löschen, massenhaft ändern oder irreversibel wirken (auch Admin-/Cleanup-Skripte). Diese Funktionen werden im Adapter nur erfasst; Änderungen laufen ausschließlich über `destructive-blueprint` → `destructive-implementation` (siehe `docs/toolkit/destructive-actions/DESTRUCTIVE_ACTION_TOOLKIT.md`).

## Werkzeuge

- Guide: `docs/project-starter/PROJECT_ADAPTER_V0_2.md`
- Checkliste: `framework/checklists/PROJECT_ADAPTER_CHECKLIST.md`
- Templates: `framework/templates/project-adapter/`
- Prompts: `framework/prompts/project-adapter/`

## Ergebnis

Ein bestehendes Projekt kann nach NDF weitergeführt werden, ohne neu gestartet werden zu müssen — validiert an realen Referenzprojekten (CI/Docker-Referenz und Destructive-Operations-Referenz).
