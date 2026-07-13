# Prompt Block – Limits

## Grenzen

- Kein Commit
- Kein Push
- Kein Reset
- Kein Rebase
- Kein Force Push
- Keine großen Refactorings ohne Freigabe
- Keine Secrets erzeugen oder speichern
- Keine riskanten Shell-Kommandos ohne ausdrückliche Anweisung

## Git Read versus Git Write

Read-only-Git-Operationen dürfen für Preflight, Evidenz, Inspektion und Review erlaubt sein. Git-Schreib-, Zustandsänderungs-, netzwerkverändernde und History-ändernde Operationen erfordern eine ausdrückliche Work-Package-Freigabe und bleiben unter Human-Maintainer-Kontrolle.

(EN: Git read-only operations may be allowed for preflight, evidence, inspection and review. Git write, state-changing, network-mutating and history-changing operations require an explicit Work-Package authorization and remain subject to Human-Maintainer control.)

### Sicheres Read-only-Muster (nur die tatsächlich benötigten Befehle erlauben)

```text
git status
git status --short
git diff
git diff --stat
git diff --check
git log
git log --oneline
git show
git rev-parse --show-toplevel
git rev-parse HEAD
git branch --show-current
git remote get-url origin
git tag --points-at HEAD
```

- Diese Liste ist ein Muster, keine Pflicht, alle Befehle auszuführen.
- Read-only bedeutet nicht automatisch Netzwerkzugriff.
- Read-only-Befehle dürfen keine Dateien oder Git-Metadaten verändern.
- Varianten und zusätzliche Argumente müssen denselben Read-only-Charakter behalten.

### Schreibende / zustandsverändernde Operationen (keine Ableitung aus Read-only)

```text
git add · git commit · git push · git pull · git fetch
git checkout · git switch · git reset · git clean
git tag <create/delete> · git merge · git rebase · git stash
git config · git submodule · git lfs
```

- Diese Operationen werden **nicht** durch eine allgemeine Read-only-Freigabe legitimiert.
- `fetch` und `pull` gelten nicht als reine lokale Read-only-Prüfung (Netzwerk/Zustand).
- Tag-Erstellung und Tag-Löschung sind Git Write; `git tag --points-at HEAD` und `git remote get-url origin` bleiben Read-only.

### Netzwerk-Grenze

Kein Netzwerkzugriff, sofern nicht ausdrücklich im Work Package erlaubt. Read-only-Git impliziert keinen Netzwerkzugriff.

### Human-Maintainer-only

Staging, Commit, Push, Tag und Release kontrolliert der Human Maintainer. Ein Implementation Agent führt Commit/Push nicht ohne ausdrückliche, frameworkkonforme Ausnahme aus.

### Prompt-Regel

Ein Work-Package-Prompt soll getrennt angeben: erlaubte Read-only-Git-Befehle · verbotene Git-Write-/State-Changing-Befehle · Netzwerkgrenze · Human-Maintainer-only-Operationen. Kein pauschales „kein Git", wenn derselbe Prompt für Preflight oder Evidenz Git-Leseoperationen benötigt.
