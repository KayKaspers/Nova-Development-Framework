# Import-Anleitung – NDF Pre-Release Cleanup Package

## Ziel

Dieses Paket bereitet das Repository auf den Foundation-0.1-Release vor.

Es setzt die Root-README wieder als professionelle Framework-Startseite und ergänzt Cleanup-Dokumente und Skripte.

## Schritte

1. ZIP entpacken.
2. Inhalt in das Repository `Nova-Development-Framework` kopieren.
3. Bestehende Dateien überschreiben, wenn Windows danach fragt.
4. Optional: Cleanup-Skript ausführen.
5. GitHub Desktop öffnen.
6. Änderungen prüfen.
7. Commit-Nachricht:

```text
chore(repo): prepare pre-release cleanup
```

8. Commit to main.
9. Push origin.

## Optionaler Cleanup per PowerShell

Im Repository-Root:

```powershell
.\scripts\repository-cleanup\cleanup-root-imports.ps1
```

zeigt zuerst nur an, was verschoben würde.

Zum tatsächlichen Verschieben:

```powershell
.\scripts\repository-cleanup\cleanup-root-imports.ps1 -Apply
```

Danach GitHub Desktop prüfen und committen.
