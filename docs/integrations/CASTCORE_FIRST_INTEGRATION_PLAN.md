# CastCore First Integration Plan

## Zweck

CastCore soll als erstes echtes Projekt nach NDF angebunden werden.

## Warum CastCore?

CastCore eignet sich besonders gut, weil es bereits reale Projektmerkmale besitzt:

- Docker-orientierte Architektur
- CI-Erfahrung
- Preflight 2.0
- FFmpeg Build-Gate
- Dokumentationsstatus
- echte Risiken und Lessons Learned
- realer Entwicklungsworkflow mit Nova und Claude

## Ziel

CastCore erhält eine NDF Project System Baseline.

## Erwarteter NDF-Level

Start:

```text
Level 3
```

Ziel:

```text
Level 4
```

## Zu erzeugende Artefakte

Für CastCore:

```text
project-system/
├── project-manifest.yaml
├── PROJECT_PROFILE.md
├── CAPABILITY_MATRIX.md
├── COMPLIANCE_CHECK.md
├── HEALTH_SCORE.md
└── WORK_PACKAGE_QUEUE.md

project-brain/
├── PROJECT_BRAIN.md
├── LESSONS_LEARNED.md
├── RISKS.md
└── DECISIONS.md

docs/ndf/
├── WORKFLOW.md
├── QUALITY_GATES.md
└── RELEASE_PROCESS.md
```

## Bekannter CastCore-Status

- Preflight 2.0 ist implementiert.
- CI war grün.
- FFmpeg Docker Build-Gate ist vorhanden.
- Backend, process-manager und worker prüfen ffmpeg/ffprobe.
- Tests sollen ffmpeg-frei und gemockt bleiben.
- `docs-status.json` kann durch generierte Datumswerte CI-Diffs verursachen.
- Remote-URL lowercase funktioniert per Redirect, sollte aber sauber dokumentiert werden.

## Erste empfohlene Work Packages

### CCI-WP-001 – CastCore Project System Baseline

Erstelle Project Manifest, Profile, Capability Matrix und Work Package Queue.

### CCI-WP-002 – CastCore Compliance Check

Bewerte CastCore gegen NDF-Standards.

### CCI-WP-003 – CastCore Health Score

Bewerte Architektur, Tests, CI, Docker, Dokumentation und Release Readiness.

### CCI-WP-004 – docs-status Stability Fix Prompt

Erstelle Claude-Prompt für stabilen Umgang mit `docs-status.json`.

### CCI-WP-005 – CastCore Lessons Learned Import

Überführe CastCore-Learnings zurück ins NDF.

## Risiken

- CastCore darf nicht durch NDF-Integration instabil werden.
- Keine großen Codeänderungen als erster Schritt.
- Integration zuerst dokumentarisch, dann technisch.
- CI darf nicht durch unnötige Änderungen gefährdet werden.

## Empfehlung

Erste CastCore-Integration als eigenes Paket vorbereiten, nicht direkt in diesem Planning-Package.
