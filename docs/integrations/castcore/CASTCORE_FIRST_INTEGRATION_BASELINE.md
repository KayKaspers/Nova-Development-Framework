# CastCore First Integration Baseline

## Status

Draft Baseline

## Prepared

2026-06-29

## Zweck

CastCore wird als erstes echtes Projekt genutzt, um das Nova Development Framework praktisch zu validieren.

Foundation 0.1 hat das Framework aufgebaut.  
Foundation 0.2 soll beweisen, dass NDF auf reale Projekte anwendbar ist.

## Warum CastCore?

CastCore ist als erstes Referenzprojekt geeignet, weil es bereits echte technische und organisatorische Eigenschaften besitzt:

- Docker-first Projekt
- Backend-, Frontend-, Worker- und Process-Manager-Strukturen
- Preflight-System
- CI-Erfahrung
- FFmpeg Docker Build-Gate
- dokumentierte Risiken
- reale Lessons Learned
- bestehender Nova → Claude → Kay Workflow

## Integrationsziel

CastCore soll eine NDF Project System Baseline erhalten:

```text
project-system/
├── project-manifest.yaml
├── PROJECT_PROFILE.md
├── CAPABILITY_MATRIX.md
├── COMPLIANCE_CHECK.md
├── HEALTH_SCORE.md
└── WORK_PACKAGE_QUEUE.md
```

## Integrationsprinzip

```text
erst dokumentieren → dann prüfen → dann gezielt verbessern
```

## Grenzen

Diese Integration darf nicht:

- sofort große Codeänderungen auslösen
- CI destabilisieren
- Docker-Builds verändern
- Preflight umbauen
- Tests von ffmpeg-Mocking zurück auf echte ffmpeg-Binaries führen
- ungeprüfte Repo-Operationen durchführen

## Erwarteter NDF-Level

Start:

```text
Level 3
```

Ziel:

```text
Level 4
```

## Bekannter CastCore-Stand

- Preflight 2.0 ist implementiert.
- CI war grün.
- FFmpeg Docker Build-Gate ist vorhanden.
- Backend, Process Manager und Worker prüfen ffmpeg/ffprobe.
- Tests sollen ffmpeg-frei und gemockt bleiben.
- `docs-status.json` kann durch generierte Datumswerte CI-Diffs verursachen.
- Remote-URL-Lowercase funktioniert per Redirect, sollte aber sauber dokumentiert werden.

## Ergebnis dieser Baseline

Dieses Paket liefert noch keine vollständige CastCore-Integration im CastCore-Repo.  
Es liefert die NDF-seitige Referenz, wie diese Integration sauber erfolgen soll.

## Nächster Schritt

Ein separates CastCore-Repo-Paket oder Claude-Prompt erzeugen, der in CastCore selbst die Project-System-Dateien erstellt.
