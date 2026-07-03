# Project Profile – Reference Project Draft

## Kurzbeschreibung

Referenzprojekt B ist eine self-hosted Medien-, Processing- und Streaming-Suite mit Docker-first-Ansatz.

## Ziel

Referenzprojekt B soll lokale oder self-hosted Medienverarbeitung, FFmpeg-basierte Verarbeitung, Preflight-Prüfungen und stabile Deployments in einer strukturierten Suite bündeln.

## Zielgruppe

- Self-Hosting-Nutzer
- Content Creator
- technische Betreiber
- Nutzer, die Medienverarbeitung und Streaming kontrolliert selbst hosten möchten

## NDF-Relevanz

Referenzprojekt B ist das erste echte Referenzprojekt zur Validierung des Nova Development Frameworks.

## Bekannte Stärken

- Docker-first Ausrichtung
- Preflight 2.0 vorhanden
- CI-Erfahrung vorhanden
- FFmpeg Docker Build-Gate vorhanden
- Tests wurden so angepasst, dass sie keine echte ffmpeg-Binary benötigen
- reale Lessons Learned aus CI, Docker und Docs vorhanden

## Bekannte Risiken

- `docs-status.json` kann durch generierte Datumswerte instabil werden.
- FFmpeg-Versionen müssen kontrolliert bleiben.
- CI darf nicht von lokalen System-Binaries abhängig werden.
- Build-Gates müssen stabil, aber nicht zu spröde sein.
- Dokumentation kann mit wachsender Suite schnell unübersichtlich werden.

## Technische Bereiche

- Backend
- Frontend
- Worker
- Process Manager
- Docker Compose
- Preflight
- CI/CD
- Dokumentation

## NDF-Ziel

Referenzprojekt B soll von NDF-Level 3 auf Level 4 gebracht werden.

## Nächster Meilenstein

Reference Project System Baseline im Referenzprojekt-Repository erstellen.
