# SampleProject – Mock Repository Tree

> Fiktive, aber realistische Repo-Struktur von SampleProject. Nur Markdown-Mock — es existieren keine echten App-Dateien.

```text
sample-project/
  README.md                     # unvollständig (siehe sample-docs/README_INCOMPLETE.md)
  CHANGELOG.md                  # endet vor mehreren Versionen
  package.json
  package-lock.json
  tsconfig.json
  docker-compose.yml            # app + db, Port hart eingetragen
  .env.example                  # unvollständig, teils veraltet
  .github/
    workflows/
      ci.yml                    # angefangen, läuft rot, wird ignoriert
  src/
    server.ts                   # UI + API in einem Prozess
    auth/                       # Session-Login, geteilter Admin
    tasks/                      # Aufgaben-Funktionen
    notes/                      # Notizen inkl. Sofort-Löschung (ein Handler, keine Prüfungen)
    config.ts                   # Konfig teils hart codiert, teils aus .env
  docs/
    deployment.md               # widerspricht der README beim Port
    ideas.md                    # unsortierte Feature-Wünsche
  tests/
    tasks.test.ts               # einzelne Alt-Tests, Abdeckung unbekannt
  data/                         # DB-Volume (im Repo nur als .gitkeep gedacht)
  scripts/
    reset-db.sh                 # ungeschütztes Reset-Skript (zweiter Destructive-Kandidat)
```

## Auffälligkeiten für die Adapter-Analyse

1. `notes/`-Löschpfad und `scripts/reset-db.sh` sind Destructive-Action-Kandidaten.
2. `config.ts` vs. `.env.example`: doppelte, teils widersprüchliche Konfigquellen.
3. `docs/deployment.md` vs. `README.md`: widersprüchliche Port-Angaben.
4. CI-Workflow vorhanden, aber funktionslos — Status unklar.
5. Keine NDF-Artefakte (kein project-system/, kein project-brain/).
