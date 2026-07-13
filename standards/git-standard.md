# Git Standard

## Empfohlener Einsteigerweg
GitHub Desktop verwenden.

## Commit-Format
Conventional Commits:

```text
feat(scope): kurze Beschreibung
fix(scope): kurze Beschreibung
docs(scope): kurze Beschreibung
chore(scope): kurze Beschreibung
```

## Verbot ohne ausdrückliche Freigabe
- force push
- reset --hard
- clean -fd
- rebase
- branch delete

## Git Read/Write-Taxonomie

NDF trennt Git-Leseoperationen von Git-Schreib-/Zustandsänderungsoperationen. Ein Work-Package-Prompt definiert eine **spezifische** Read-only-Allowlist mit genau den benötigten Befehlen; er leitet daraus keine Schreibrechte ab.

### Git Read (kann für Preflight/Evidenz/Review erlaubt sein)

```text
git status · git status --short
git diff · git diff --stat · git diff --check
git log · git log --oneline · git show
git rev-parse --show-toplevel · git rev-parse HEAD
git branch --show-current · git remote get-url origin
git tag --points-at HEAD
```

- Read-only-Befehle verändern keine Dateien oder Git-Metadaten.
- Read-only bedeutet keinen Netzwerkzugriff.
- Varianten/zusätzliche Argumente müssen den Read-only-Charakter behalten.

### Git Write / State-Changing / Network-Mutating (ausdrückliche Freigabe erforderlich)

```text
git add · git commit · git push · git pull · git fetch
git checkout · git switch · git reset · git clean
git tag <create/delete> · git merge · git rebase · git stash
git config · git submodule · git lfs
```

- Werden nicht durch eine allgemeine Read-only-Freigabe legitimiert.
- `fetch`/`pull` sind keine reine lokale Read-only-Prüfung (Netzwerk/Zustand).
- Tag-Erstellung/-Löschung ist Git Write.

## Human-Maintainer-Kontrolle

Staging, Commit, Push, Tag und Release kontrolliert ausschließlich der Human Maintainer. Ein Implementation Agent führt kein Commit/Push/Tag/Release ohne ausdrückliche, frameworkkonforme Ausnahme aus.

## Hinweis: Work-Package-spezifische Allowlist

Die konkrete erlaubte Read-only-Git-Liste wird pro Work Package festgelegt (nur die tatsächlich benötigten Befehle). Diese Datei ist ein Standard-Bezug, keine Git-Einsteigeranleitung und keine vollständige Git-Dokumentation.
