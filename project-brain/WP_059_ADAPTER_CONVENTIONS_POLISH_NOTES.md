# Project Brain – WP-059 Adapter Conventions Polish Notes

## Ausgangspunkt

WP-047 (Project Adapter Practical Validation) endete mit **PASS WITH NOTES** — keine release-blocking Findings, aber drei should-have-Konventionslücken plus zwei later-Template-Punkte im Improvement Backlog. WP-059 (release-blocking für Foundation 0.4, Kern „Adoption Hardening") schließt genau diese.

## Adressierte Findings

1. **Manifest-Format** → Konvention: `PROJECT_MANIFEST.md` ist kanonisch (Markdown), YAML/JSON nur eingebettet/abgeleitet, keine Maschinenpflicht, Unknowns explizit markiert.
2. **Health-Score-Kategorien** → verbindliche Foundation-0.4-Kategorien: Documentation, Security, Operations, Testing/CI, Release Readiness, Maintainability, Governance/Workflow, i18n/Language Readiness (Evidenzpflicht, `unknown`/`n/a` mit Begründung).
3. **Output-Pfad-Konvention** → Validierung `examples/<fixture>/adapter-validation-output/`, erwartet `expected-adapter-output/`, zentral `docs/validation/project-adapter/`, produktionsnah `project-system/`/`project-brain/`/`docs/project-adoption/` nur nach Maintainer-Entscheidung; keine stillen Überschreibungen; expected ≠ actual.
4. **Präfix-Beispiel** → Queue-Template nutzt Platzhalter `XY-WP` statt `SP-WP` (Kollision mit SampleProject behoben).
5. **First-Safe-WP-Template** → neu: `FIRST_SAFE_WORK_PACKAGE_TEMPLATE.md`.

## Geänderte/neue Dateien

Neu: `docs/project-starter/PROJECT_ADAPTER_CONVENTIONS.md` (bilingual), `framework/templates/project-adapter/FIRST_SAFE_WORK_PACKAGE_TEMPLATE.md`. Geändert: Guide (Link), Helper (Konventions-Block), 3 Templates (Health Score, Output Structure, Review Report, Queue-Präfix), Checkliste, 3 Adapter-Prompts (Konventions-Verweis), Backlog + Validierungsnachweis (addressed markiert), Roadmap/Criteria/Changelog.

## Bewusst nicht erledigt

Later-Punkt 6 (unabhängiger Adapter-Testlauf) bleibt Foundation-0.4-deferred (NDF-WP-064). Keine neuen Adapter-Features, keine Adapter-Automatisierung, keine maschinelle Manifest-Pflicht.

## Risiken

- Health-Score-Kategorien wurden gegenüber dem alten Template geändert (CI/CD→Testing/CI, +Operations, +i18n, Architecture/Project Brain/Workflow Adoption → Governance/Workflow). Alte Beispiel-Outputs (SampleProject-Validierung) bleiben historisch unverändert; das ist konsistent, weil sie den damaligen Lauf dokumentieren.

## Nächstes empfohlenes WP

NDF-WP-060 – Prompt Library DE/EN Priority Pass (release-blocking, parallel möglich gewesen).
