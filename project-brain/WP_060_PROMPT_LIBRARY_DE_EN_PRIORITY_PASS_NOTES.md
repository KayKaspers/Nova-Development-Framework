# Project Brain – WP-060 Prompt Library DE/EN Priority Pass Notes

## Ausgangspunkt

WP-060 ist der zweite release-blocking Kern von Foundation 0.4 (Public Usability, laut Scope Lock eng gefasst und über WP-067 herabstufbar). WP-039 hatte bereits 12 Kern-Prompts mit DE/EN-Zweck/Grenzen/Rückmeldung versehen; WP-060 hebt die Adoptions-Erstkontakt-Prompts auf **vollständige** DE/EN-Nutzbarkeit.

## Priorisierte Prompt-Dateien

Vollständig bilingual (Zweck/Rolle/Verwendung/Eingaben/Aufgaben/Grenzen/Erwartete Ausgabe/Rückmeldung, DE+EN gleichwertig):

1. `project-adapter/PROJECT_ADAPTER_INTAKE_PROMPT.md`
2. `project-adapter/PROJECT_SYSTEM_BASELINE_PROMPT.md`
3. `project-adapter/CREATE_PROJECT_ADAPTER.md` (Legacy v0.1)
4. `core/WORK_PACKAGE_CLASSIFICATION_PROMPT.md`
5. `review/WORK_PACKAGE_BOUNDARY_REVIEW_PROMPT.md`

Auswahlbegründung: Das sind die Prompts, die ein externer Nutzer beim Adoptions-Einstieg und bei den zentralen Work-Package-Entscheidungen zuerst braucht. Die 7 priorisierten Security-/Gate-Prompts haben bestätigte DE/EN-Kernabschnitte (WP-039) — ausreichend als Kern, Vollübersetzung bleibt non-blocking.

## Was verbessert wurde

Neben der Bilingualisierung: Sicherheitsgrenzen und Human-Maintainer-Grenzen in beiden Sprachen erhalten, Entscheidungslogik (GO/REWORK/SPLIT/STOP) erhalten, Adapter-Konventions-Verweise erhalten. **Nebenbefund korrigiert:** Der Baseline-Prompt listete noch `PROJECT_MANIFEST.yaml` — auf `.md` gebracht (Konsistenz mit WP-059) und das Präfix-Beispiel `SP-WP` → `XY-WP`.

## Nicht Teil dieses WPs

WP-061 Checklisten, WP-062 Academy, WP-063 ADR — optional, nicht hier. Keine Vollübersetzung aller ~30 Prompts. Kein v1.0.

## Restarbeiten (non-blocking, → 0.5)

Vollständige DE/EN-Übersetzung der übrigen Security-/Fach-Prompts, Blocks, Rollen-Prompts. Stand in `docs/i18n/TRANSLATION_STATUS.md` und `docs/prompts/PROMPT_LIBRARY_DE_EN_PRIORITY_PASS.md`.

## Risiken

- Optionale Prompt-Checklist bewusst **nicht** erstellt (Aufgabe 14) — das Priority-Pass-Dokument reicht, eine zusätzliche Checkliste wäre Rauschen.

## Nächstes empfohlenes WP

Optional 061–063/066, dann NDF-WP-067 – Foundation 0.4 Release Readiness Review (die zwei blocking Kern-WPs 059+060 sind fertig).
