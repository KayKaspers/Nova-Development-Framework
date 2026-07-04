# Project Profile – SampleProject (Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation.

| Feld | Wert / Value |
|---|---|
| Projektname | SampleProject |
| Projekttyp | Self-Hosted-Webanwendung (Aufgaben, Notizen, Statusübersichten) / self-hosted web app |
| Zweck | zentrale Aufgaben- und Notizenverwaltung für ein kleines Team (3–8 Personen) |
| Zielgruppe | kleines Team + ein Maintainer (example-owner) |
| Tech-Basis (angenommen) | TypeScript-Web-App, Docker Compose, eine Datenbank, Basic Auth, Markdown-Doku — laut Brief; Code nicht einsehbar (Fixture), daher **not evidenced im Detail** |
| Deployment | Docker Compose auf Team-Maschine (`example.local`); Port widersprüchlich dokumentiert (3000 vs. 8080) — **unklar** |
| Dokumentationsstand | lückenhaft: README bricht bei Installation ab, Deployment-Notizen widersprüchlich, Changelog seit mehreren Versionen ungepflegt |
| Sicherheitsstand | rudimentär: geteilter Admin-Account, keine Rollen, kein Audit, Secret-Handling ungeklärt (`.env` per Chat), Löschfunktion ungeschützt |
| i18n-Stand | gemischt DE/EN, keine Entscheidung dokumentiert |
| Release-/Betriebsstand | kein Release-Prozess, kein Backup, kein Rollback-Weg — „einfach deployen" |
| NDF-Level (Ist) | **Level 0 – Nicht angebunden** (keinerlei NDF-Struktur; `docs/project-starter/NDF_LEVEL_GUIDE.md`) |
| NDF-Level (Ziel nach Baseline) | Level 1–2 (Manifest, Profile, Queue, Project Brain) |

## Bekannte Lücken

1. Installations-/Betriebsdoku unvollständig und widersprüchlich (Port).
2. Umgebungsvariablen undokumentiert; fail-closed-Verhalten unbekannt.
3. Keine Rollen, kein Audit, ungeschützte Löschfunktion (+ `reset-db.sh`).
4. CI vorhanden, aber rot und ignoriert; Testabdeckung unbekannt.
5. Keine Roadmap-, Release- oder Work-Package-Systematik.

## Adapter-Eignung

Gut geeignet für die NDF-Übernahme: klein, ein Maintainer, klar benannte Schmerzen, keine Alt-NDF-Struktur, motivierter gewünschter Endzustand (siehe `../PROJECT_BRIEF.md`).

## Offene Fragen (aus dem Review)

1. Welcher Port gilt (3000 oder 8080)? → klären in SP-WP-004.
2. Welche Env-Variablen sind Pflicht? → Teil der Security Baseline.
3. Gilt `reset-db.sh` noch oder ist es tot? → Review klären.
4. DE/EN-Zielzustand der öffentlichen Doku? → Entscheidung des Maintainers nötig.
