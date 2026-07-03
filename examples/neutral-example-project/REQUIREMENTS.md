# SampleProject – Requirements

> Fiktive Anforderungen. Realistisch klein gehalten.

## Funktionale Anforderungen

1. Aufgaben anlegen, bearbeiten, als erledigt markieren.
2. Notizen anlegen, bearbeiten, durchsuchen.
3. Wochenübersicht über offene/erledigte Aufgaben.
4. Notizen löschen können — künftig **sicher** (Bestätigung, Wiederherstellbarkeit oder Backup, Audit).

## Nicht-funktionale Anforderungen

- Self-Hosted per Docker Compose, Start mit einem Befehl.
- Bedienbar ohne Schulung (kleines Team).
- Nachvollziehbare Releases statt „einfach deployen".

## Sicherheitsanforderungen

- Individuelle Accounts statt geteiltem Admin-Account; mindestens zwei Rollen (Member, Owner).
- Secrets nur über Umgebungsvariablen; dokumentiert, nie im Repo, nie im Chat.
- Fail-closed: Produktion startet nicht mit unsicheren Defaults.
- Destruktive Aktionen (Notiz-Löschung) nur mit Bestätigung + Audit-Eintrag; Planung vor Implementierung.

## Dokumentationsanforderungen

- README führt vollständig von Null zur laufenden Instanz.
- Umgebungsvariablen vollständig dokumentiert (Pflicht/Default).
- Changelog wird pro Release gepflegt.

## DE/EN-Anforderungen

- Team-intern Deutsch; öffentliche Doku (README, Changelog) soll mittelfristig Englisch oder bilingual sein — Stand heute gemischt und unentschieden (bewusste Lücke für den Adapter).

## Betriebsanforderungen

- Backup der Datenbank vor jedem Update.
- Ein dokumentierter Rollback-Weg.
- Logs ohne sensible Inhalte.

## Grenzen

- Kein Mandantenbetrieb, keine Public-SaaS-Ambition.
- Keine Mobile-App.
- Team bleibt klein — keine Enterprise-Prozesse einführen.
