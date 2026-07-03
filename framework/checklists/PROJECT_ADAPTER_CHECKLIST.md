# Project Adapter Checklist

## EN – Purpose

This checklist accompanies every project adapter run: preflight, repository status, privacy and secret rules, read-only analysis, detection of Docker/CI/docs/security/destructive features, role model, initial Health Score, typed work packages, and the feedback to Nova (ChatGPT).

Für jede Adapter-Ausführung abarbeiten. Bezugsdokument: `docs/project-starter/PROJECT_ADAPTER_V0_2.md`

## Preflight

- [ ] Intake-Template ausgefüllt (`PROJECT_ADAPTER_INTAKE_TEMPLATE.md`)
- [ ] Ziel und Umfang mit dem menschlichen Maintainer geklärt (minimal vs. vollständig)
- [ ] Work-Package-Typ je Phase festgelegt

## Repository-Status

- [ ] `git status` im Zielprojekt geprüft (sauberer Arbeitsstand oder bewusst dokumentiert)
- [ ] Default-Branch und Branch-Strategie erfasst
- [ ] Offene PRs/laufende Arbeiten notiert

## Private Daten vermeiden

- [ ] Keine privaten Projekt- oder Personennamen in NDF-Artefakte übernommen, wenn diese öffentlich werden können
- [ ] Interne URLs/Hosts nur wenn nötig und als intern gekennzeichnet
- [ ] Public/Private-Status des Zielprojekts im Intake erfasst

## Secrets

- [ ] Keine `.env`-, Key-, Token- oder Credential-Dateien gelesen oder kopiert
- [ ] Keine Secrets in Reports, Profiles oder Manifeste übernommen
- [ ] Fundstellen von Secrets im Repo nur als Risiko gemeldet (ohne Inhalt)

## Analysephase (read-only)

- [ ] Keine Codeänderungen
- [ ] Keine Konfig-/CI-Änderungen
- [ ] Kein Commit, kein Push

## Erkennung

- [ ] Docker/Container-Setup erkannt und dokumentiert
- [ ] CI/CD-Workflows erkannt und Status erfasst
- [ ] Doku-Stand bewertet (README, Architektur, Betrieb)
- [ ] Security-Merkmale erfasst (Auth, Secret-Handling, Abhängigkeiten)
- [ ] Destruktive Funktionen identifiziert (Löschen, Bulk, irreversibel) und markiert

## Rollenmodell

- [ ] Menschlicher Maintainer / Owner-Rolle erfasst
- [ ] Review- und Freigabeweg dokumentiert (Nova → Implementation Agent → Human Maintainer)

## Health Score

- [ ] Initialer Health Score über alle Kategorien geschätzt (`PROJECT_ADAPTER_HEALTH_SCORE_TEMPLATE.md`)
- [ ] Bewertungen mit Evidenz begründet, nicht geraten

## Work Packages

- [ ] Erste Queue erstellt (`INITIAL_WORK_PACKAGE_QUEUE_TEMPLATE.md`)
- [ ] Jedes WP hat genau einen primären Typ
- [ ] Erstes WP ist klein und sicher (kein destructive, kein großes Feature)

## Rückmeldung an Nova

- [ ] Review Report erstellt (`PROJECT_ADAPTER_REVIEW_REPORT_TEMPLATE.md`)
- [ ] Empfehlung GO / REWORK / SPLIT / STOP mit Begründung
- [ ] Offene Risiken und nächste Schritte benannt
