# Project Brain – SampleProject (Adapter Validation)

> This file is generated as part of NDF-WP-047 Project Adapter Practical Validation for the neutral SampleProject fixture. It is not production project documentation.
> Diese Datei ist Validierungsoutput für das neutrale SampleProject-Fixture und keine produktive Projektdokumentation — **nicht** zu verwechseln mit dem NDF-eigenen `project-brain/`.

## Stand (nach Adapter-Baseline)

SampleProject ist ein gewachsenes Level-0-Projekt mit funktionierender App, aber ohne Struktur: Doku lückenhaft/widersprüchlich, Security rudimentär, kein Release-Prozess. Mit diesem Adapter-Lauf existieren erstmals Profile, Manifest, Findings, Capability Matrix, Compliance Check, Health Score und eine initiale Work Package Queue.

## Aktuelle Entscheidungen

1. NDF-Übernahme additiv — kein Rewrite des Projekts.
2. Erste Arbeit ist review-/docs-only (SP-WP-001); nichts Riskantes vor der Security Baseline.
3. Notiz-Löschung und `reset-db.sh` werden **nur** über `destructive-blueprint` → nach Freigabe `destructive-implementation` angefasst.
4. Rollenmodell-Ziel: `member`/`owner`, serverseitig geprüft.

## Offene Fragen

Port (3000/8080)? Pflicht-Env-Variablen? `reset-db.sh` noch in Gebrauch? DE/EN-Ziel der öffentlichen Doku?

## Bekannte Risiken

Siehe `FINDINGS.md` (5× high: geteilter Admin, Secrets, Löschung, reset-db.sh, kein Backup/Release-Prozess) und `../RISKS.md`.

## NDF-Adoptionsziel

Level 0 → Level 1 mit der Baseline (Manifest, Profile, Queue), danach Level 2 (Project Brain gepflegt, Standards, erste ADRs). Kein Sprung auf Level 3+ vor stabiler Doku und Security Baseline.

## Empfohlene Arbeitsweise

Nova (ChatGPT) plant kleine, typisierte Work Packages → Implementation Agent setzt genau eines um → Rückmeldung → Human Maintainer (example-owner) prüft und veröffentlicht. Keine Commits/Pushes durch den Agent.

## Nächste Work Packages

Siehe `INITIAL_WORK_PACKAGE_QUEUE.md` — Start: SP-WP-001 (Repository & Documentation Baseline Review).
