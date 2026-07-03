# NDF Standard – Local Testing Policy

## Regeln

- Bei Codeänderung kleinsten relevanten Test ausführen.
- Docker-Verfügbarkeit prüfen.
- Bei falschem Testpfad im Container Pfad suchen.
- Umgebungsausfall von Codeausfall trennen.
- CI bleibt finale integrierte Prüfung.

## Docker-Path-Discovery

```sh
find . -name '<test-file>' -print
```
