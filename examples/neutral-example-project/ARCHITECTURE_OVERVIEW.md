# SampleProject – Architecture Overview

> Fiktive Grobarchitektur. Bewusst unvollständig — der Adapter soll die Lücken erfassen.

## Angenommene Komponenten

```text
[Browser]
   |
[Web-App (TypeScript, Server-rendered + API)]
   |
[Datenbank (ein Container)]
```

- **Web-App:** UI + API in einem Prozess; Session-basierte Anmeldung.
- **Datenbank:** ein Container, Volume auf dem Host.
- **Reverse Proxy:** „irgendwann geplant", aktuell direkter Port.

## Deployment-Sicht

```text
docker compose up -d
→ app  (Port: siehe widersprüchliche Angaben in sample-docs/)
→ db   (Volume: ./data)
```

Updates: `git pull` + `docker compose up -d --build` — ohne Backup davor (bekanntes Risiko).

## Datenfluss (hohe Ebene)

1. Nutzer meldet sich an (Session-Cookie).
2. Aufgaben/Notizen werden per API gelesen/geschrieben.
3. Löschungen wirken sofort auf die Datenbank (kein Papierkorb, kein Audit).

## Offene Architekturfragen

1. Wo sollen Rollen geprüft werden — nur UI oder serverseitig? (aktuell: faktisch gar nicht)
2. Wie werden Secrets bereitgestellt (Compose-Env, .env-Datei, beides)?
3. Braucht die Wochenübersicht eigene Endpunkte oder reicht Filterung?
4. Wie sähe ein Backup-/Restore-Weg konkret aus?

## Bewusst fehlende Details (Fundmaterial für den Adapter)

- kein Komponenten-/Modulschnitt dokumentiert
- keine Angabe zu Datenmodell oder Migrationsstrategie
- kein Logging-/Monitoring-Konzept
- keine Aussage zu Test-Architektur
