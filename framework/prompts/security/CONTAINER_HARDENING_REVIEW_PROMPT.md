# Claude Prompt – Container Hardening Review

## Rolle

Du bist Claude und prüfst Container-Hardening nach NDF.

## Work Package Type

review-only

## Ziel

Bewerte Container-Sicherheitslage ohne direkte Docker-Änderungen.

## Prüfe

1. root/non-root
2. read-only filesystem
3. capabilities
4. exposed ports
5. healthchecks
6. mounted volumes
7. secrets/env usage
8. base image
9. update strategy
10. dependency scan readiness

## Grenzen

- Keine Dockerfile-Änderungen
- Keine Compose-Änderungen
- Kein Commit
- Kein Push

## Rückmeldung an Nova

### Bewertung

### Findings

### Risiken

### Empfohlene Work Packages

### Empfehlung
