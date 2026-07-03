# NDF Toolkit CLI Future Specification

## Ziel

Langfristig kann das Toolkit als CLI umgesetzt werden.

## Mögliche Befehle

```bash
ndf init
ndf project manifest
ndf project profile
ndf prompt select
ndf template select
ndf check
ndf health
ndf release prepare
```

## Beispiel

```bash
ndf init --name SampleProject --type web-suite --docker true
```

## Nicht in v0.1 enthalten

- echte CLI
- automatische Dateierzeugung
- automatische Health-Checks
- automatische Commits

## Warum?

Erst muss das Modell stabil sein. Dann wird automatisiert.
