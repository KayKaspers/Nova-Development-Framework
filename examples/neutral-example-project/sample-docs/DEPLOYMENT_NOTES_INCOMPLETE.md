# Deployment Notes (Stand: unklar)

> Fixture-Hinweis / fixture note: Simuliert verstreute, teils widersprüchliche Deployment-Notizen. Lücken und Widersprüche sind Absicht.

## Server

Läuft auf der Team-Maschine unter `example.local`. Zugang hat der Maintainer (example-owner).

## Start

```text
docker compose up -d
```

App danach erreichbar auf Port **8080**.

<!-- Widerspruch: Die README nennt Port 3000. Welcher stimmt, weiß niemand sicher. -->

## Update

```text
git pull
docker compose up -d --build
```

Anmerkung von vor einem halben Jahr: „vorher DB sichern!!" — wie genau, steht nirgends.

## Backup

TODO. Es gab mal ein Skript, siehe `scripts/` — unklar ob `reset-db.sh` gemeint war (das macht aber etwas anderes und ist gefährlich).

## Rollback

Nicht dokumentiert. Bisher-Strategie: „hoffen".

## Offene Fragen

- Welche Umgebungsvariablen braucht Produktion wirklich?
- Wer außer dem Maintainer kann deployen?
- Reverse Proxy / HTTPS — Stand?
