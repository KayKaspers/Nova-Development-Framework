# NDF Project Adapter v0.2

> Sprachstatus / Language status: Foundation 0.2 document. DE/EN alignment pending according to `docs/i18n/DE_EN_LANGUAGE_STANDARD.md`.
>
> Konventionen / Conventions: Seit Foundation 0.4 gelten verbindliche Manifest-, Output-Pfad- und Health-Score-Konventionen — siehe [PROJECT_ADAPTER_CONVENTIONS.md](PROJECT_ADAPTER_CONVENTIONS.md). Kurz: `PROJECT_MANIFEST.md` ist kanonisch (Markdown), Validierungsoutput liegt unter `examples/<fixture>/adapter-validation-output/` getrennt von erwartetem Output, und der Health Score nutzt die 0.4-Kategorien mit `unknown`/`n/a`-Regeln.

## 1. Zweck

Der Project Adapter überführt ein bestehendes Softwareprojekt strukturiert in das Nova Development Framework — ohne Neustart, ohne riskante Umbauten, ohne dass das Projekt instabil wird.

Ergebnis ist ein vollständiges NDF Project System im Zielprojekt: Profil, Manifest, Project Brain, Capability Matrix, Compliance Check, Health Score und eine typisierte Work Package Queue.

## 2. Wann nutzt man den Adapter?

- Ein bestehendes Projekt soll künftig nach NDF weiterentwickelt werden.
- Ein Projekt braucht eine ehrliche Standortbestimmung (Doku, CI, Security, Release-Reife).
- Ein Team will KI-gestützte Umsetzung mit menschlicher Kontrolle einführen.

Nicht nötig: für neue Projekte — dafür gibt es den Project Starter (`docs/project-starter/NEW_PROJECT_FLOW.md`).

## 3. Voraussetzungen

- Lese-Zugriff auf das Zielprojekt-Repository (lokal oder remote).
- Ein menschlicher Maintainer, der Entscheidungen trifft und Commits freigibt.
- Grundverständnis der NDF-Rollen und Work-Package-Typen (`framework/standards/WORK_PACKAGE_TYPES.md`).

## 4. Rollenmodell

```text
Nova (Planung) -> Implementation Agent (Ausführung) -> Human Maintainer (Review & Freigabe)
```

- **Nova** plant die Adapter-Phasen als Work Packages und reviewt die Ergebnisse.
- **Der Implementation Agent** (z. B. Claude) analysiert read-only und erstellt die NDF-Artefakte.
- **Der menschliche Maintainer** prüft jede Phase, entscheidet GO / REWORK / SPLIT / STOP und führt Commits aus.

## 5. Adapter-Phasen

| Phase | Name | Typ | Ergebnis |
|---|---|---|---|
| 0 | Intake | review-only | ausgefülltes Intake-Template |
| 1 | Repository Read-only Review | review-only | Review Report |
| 2 | Project Profile | docs-only | `project-system/PROJECT_PROFILE.md` |
| 3 | Project Manifest | docs-only | `project-system/PROJECT_MANIFEST.md` (kanonisch Markdown; eingebettetes YAML/JSON erlaubt — siehe Conventions) |
| 4 | Project Brain | docs-only | `project-brain/PROJECT_BRAIN.md` |
| 5 | Capability Matrix | docs-only | `project-system/CAPABILITY_MATRIX.md` |
| 6 | Compliance Check | review-only | `project-system/COMPLIANCE_CHECK.md` |
| 7 | Health Score | health-score-update | `project-system/HEALTH_SCORE.md` |
| 8 | Work Package Queue | docs-only | `project-system/WORK_PACKAGE_QUEUE.md` |
| 9 | First Safe Work Package | je nach Typ | erstes kleines, sicheres WP |
| 10 | Review and Commit | — | Maintainer-Review, Commit, Push |

Phasen 2–8 können in einem `project-adapter`-Work-Package gebündelt werden (vollständige Variante) oder einzeln laufen.

## 6. Benötigte NDF-Artefakte

- Templates: `framework/templates/project-adapter/`
- Checkliste: `framework/checklists/PROJECT_ADAPTER_CHECKLIST.md`
- Prompts: `framework/prompts/project-adapter/`
- Spezifikationen: `docs/project-system/`
- Entscheidungshilfe: `docs/toolkit/PROJECT_ADAPTER_HELPER.md`

## 7. Sicherheitsregeln

1. Phase 0–1 sind strikt read-only: keine Codeänderungen, keine Konfigänderungen.
2. Keine Secrets lesen, kopieren oder in Artefakte übernehmen (`.env`, Keys, Tokens, Credentials).
3. Destruktive Funktionen des Zielprojekts (Löschen, Bulk-Operationen, irreversible Aktionen) werden nur **erfasst**, nie verändert — Änderungen daran laufen später über `destructive-blueprint` → `destructive-implementation`.
4. Jede Phase endet mit einer Rückmeldung an Nova; ohne Freigabe keine nächste Phase.
5. Kein Commit und kein Push durch den Implementation Agent, sofern nicht ausdrücklich freigegeben.
6. Private Namen, interne URLs und personenbezogene Daten gehören nicht in öffentlich sichtbare NDF-Artefakte.

## 8. Umgang mit bestehenden Projekten

- Bestehende Strukturen werden respektiert: NDF-Artefakte kommen **zusätzlich** ins Projekt, vorhandene Dateien werden nicht umgebaut.
- Bestehende Doku wird referenziert, nicht dupliziert.
- Ein Projekt mit starker Technik, aber schwacher Doku beginnt mit Doku-/Status-WPs, nicht mit Features.
- Ein Projekt mit riskanten Funktionen beginnt mit Security-/Destructive-Reviews.

## 9. Minimale Variante

Für kleine Projekte oder einen schnellen Start:

```text
Phase 0 -> Phase 1 -> Phase 2 (Profile) -> Phase 3 (Manifest) -> Phase 8 (kleine Queue) -> Phase 10
```

Capability Matrix, Compliance Check und Health Score können später als eigene Work Packages folgen.

## 10. Vollständige Variante

Alle Phasen 0–10 in Reihenfolge. Empfohlen für Projekte, die produktiv genutzt werden, mehrere Module haben oder sicherheitsrelevante Funktionen enthalten.

## 11. Ergebnisstruktur

Siehe `framework/templates/project-adapter/PROJECT_ADAPTER_OUTPUT_STRUCTURE.md`:

```text
project-system/PROJECT_PROFILE.md
project-system/PROJECT_MANIFEST.md
project-system/CAPABILITY_MATRIX.md
project-system/COMPLIANCE_CHECK.md
project-system/HEALTH_SCORE.md
project-system/WORK_PACKAGE_QUEUE.md
project-brain/PROJECT_BRAIN.md
docs/ndf/README.md
docs/ndf/ADOPTION_NOTES.md
```

## 12. Nächster Schritt nach Adapter-Ausführung

Das erste Work Package aus der Queue umsetzen — klein, sicher, typisiert (z. B. Documentation Stability Review oder Security Baseline Review). Danach etabliert sich der normale NDF-Zyklus: Classify → Plan → Execute → Rückmeldung → Review → Commit.
