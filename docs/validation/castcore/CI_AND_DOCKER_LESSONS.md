# CI and Docker Lessons

## CastCore zeigte

- Docker muss lokal verfügbar sein.
- DNS/Pull-Probleme sind keine Codefehler.
- `docker pull docker/dockerfile:1` kann die Basis prüfen.
- Container-Pfade können vom Repo-Pfad abweichen.
- Der kleinste relevante Test ist oft besser als die ganze Suite.

## NDF-Regeln

1. Trenne Umgebungsausfall von Codeausfall.
2. Führe zuerst den kleinsten relevanten Test aus.
3. Nutze Path Discovery im Container.
4. CI bleibt die finale integrierte Prüfung.
5. Committe nur scoped files.

## Docker-Checkliste

- [ ] Docker läuft
- [ ] Compose verfügbar
- [ ] Pull funktioniert
- [ ] Service baut
- [ ] Testpfad existiert im Container
- [ ] fokussierter Test grün
