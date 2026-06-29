# Compliance Check – CastCore Draft

## Summary

CastCore erfüllt bereits viele NDF-Anforderungen für ein reales technisches Projekt, insbesondere durch Docker, CI, Preflight und dokumentierte Build-Gates.

## Check

| Bereich | Status | Bewertung |
|---|---|---|
| README | warning | prüfen und ggf. mit NDF-Abschnitt ergänzen |
| Project Brain | fail | noch nicht im CastCore-Repo als NDF-Artefakt vorhanden |
| Roadmap | warning | NDF-kompatibel prüfen |
| ADRs | warning | wichtige Entscheidungen ggf. nachtragen |
| Prompt Workflow | pass | Nova/Claude-Workflow etabliert |
| Quality Gates | pass | Docker/FFmpeg Build-Gate vorhanden |
| Tests | pass | ffmpeg-freie Tests als wichtiges Prinzip |
| CI/CD | pass | letzter bekannter Stand grün |
| Docker | pass | Docker-first |
| Security | warning | Basis vorhanden, vertiefter Review offen |
| Release Notes | warning | Releaseprozess prüfen |
| Lessons Learned | warning | nach NDF übertragen |

## Hauptlücken

1. CastCore braucht ein Project System im Repo.
2. Project Brain sollte mit realem Status gefüllt werden.
3. docs-status-Instabilität sollte priorisiert werden.
4. Health Score sollte initial erstellt werden.
5. ADRs zu Preflight/FFmpeg/Tests sollten ergänzt werden.

## Empfehlung

NDF-Integration zunächst nur dokumentarisch durchführen.  
Keine funktionalen Codeänderungen im ersten Schritt.
