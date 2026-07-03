# SampleProject – Current State

> Fiktiver Ist-Zustand für die Adapter-Analyse (Phase 1). Bewusst lückenhaft.

## Vorhanden

- Web-App (TypeScript) mit Aufgaben- und Notizen-Funktionen — läuft beim Team „irgendwie stabil"
- `docker-compose.yml` für App + Datenbank
- README (unvollständig, siehe `sample-docs/README_INCOMPLETE.md`)
- verstreute Deployment-Notizen (`sample-docs/DEPLOYMENT_NOTES_INCOMPLETE.md`)
- angefangener Changelog (`sample-docs/CHANGELOG_INCOMPLETE.md`)
- ein angefangener CI-Workflow, der seit Monaten rot ist und ignoriert wird

## Fehlt

- vollständige Installations-/Betriebsdoku
- dokumentierte Umgebungsvariablen (welche sind Pflicht? welche haben Defaults?)
- Tests-Systematik (es gibt „ein paar" Tests, niemand kennt die Abdeckung)
- Project Brain / Arbeitsgedächtnis
- Work-Package- oder Aufgabenstruktur für die Entwicklung selbst
- Health-Score- oder Reifegrad-Systematik
- Release-Prozess (es wird „einfach deployt")

## Bekannte Probleme

1. Notizen-Löschung: sofort, ohne Bestätigung, ohne Backup, ohne Audit-Eintrag.
2. Der Admin-Account wird vom ganzen Team geteilt.
3. Fehlermeldungen zeigen teils interne Details an.
4. Die Datenbank wird nie gesichert („war bisher nicht nötig").

## Technische Schulden

- zwei halbfertige Feature-Branches, die niemand mehr zuordnen kann
- auskommentierter Code „für später"
- Konfigwerte teils hart im Code, teils in `.env`, teils in beidem
- Abhängigkeiten seit über einem Jahr nicht aktualisiert

## Dokumentationslücken

- README bricht bei der Installation ab
- Deployment-Notizen widersprechen sich (zwei verschiedene Ports genannt)
- Changelog endet vor mehreren Versionen
- keine Sicherheits- oder Betriebsdoku

## Sicherheitslücken (Konzeptniveau)

- Secret-Handling ungeklärt (`.env` wird per Chat geteilt — als Praxis dokumentiert, keine echten Werte)
- keine Rollen: eingeloggt = darf alles
- kein Audit-Logging
- Löschfunktion ohne jede Schutzmaßnahme (siehe `SECURITY_NOTES.md`)

## Offene Fragen an den Project Adapter

1. Welches NDF-Level hat SampleProject ehrlich?
2. Was ist das sicherste erste Work Package?
3. Muss der Lösch-Use-Case sofort ein `destructive-blueprint` werden oder reicht die Erfassung?
4. Welche Doku-Lücke blockiert Adoption am stärksten?
