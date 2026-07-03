# SampleProject – Project Brief

> Fiktives Projekt / fictitious project. Dient als Intake-Input für den Project Adapter (Phase 0).

## Projektbeschreibung

SampleProject ist ein fiktives, kleines Self-Hosted-Webprojekt zur Verwaltung neutraler Aufgaben, Notizen und einfacher Statusübersichten für ein kleines Team. Es ist über zwei Jahre „nebenbei" gewachsen: Features entstanden nach Bedarf, Dokumentation und Struktur hinkten hinterher.

## Zielgruppe

Ein kleines Team (3–8 Personen), das seine Aufgaben und Notizen selbst hosten will, plus ein Maintainer (example-owner), der das Projekt allein betreut.

## Geplanter Nutzen

- zentrale Aufgabenliste mit Status
- geteilte Notizen mit einfacher Suche
- Wochenübersicht („Was ist offen, was ist erledigt?")

## Angenommene Tech-Basis

```text
TypeScript-based web application
Docker deployment (docker-compose)
simple database (single container)
basic authentication (username/password)
Markdown documentation
CI planned but incomplete
```

## Aktueller Reifegrad

Funktioniert „bei uns" — aber: keine Tests-Systematik, Doku unvollständig, Deployment nur per Zuruf bekannt, Security nie systematisch geprüft.

## Bekannte Lücken (Selbstauskunft des Maintainers)

1. README erklärt die Installation nicht vollständig.
2. Niemand weiß sicher, welche Umgebungsvariablen wirklich nötig sind.
3. Das Löschen von Notizen ist „einfach ein Button" — ohne Bestätigung, ohne Backup.
4. CI wurde angefangen, läuft aber nicht.
5. Roadmap existiert nur im Kopf des Maintainers.

## Gewünschter NDF-Einsatz

Der Maintainer möchte SampleProject nach NDF überführen: nachvollziehbare Struktur, ehrliche Standortbestimmung, sichere Weiterentwicklung mit kleinen Work Packages — ohne das Projekt neu zu schreiben.

## Gewünschtes Ergebnis nach Adapter-Durchlauf

- Project Profile, Manifest und Project Brain existieren und stimmen mit der Realität überein.
- Ein initialer Health Score mit Evidenz.
- Eine kleine, typisierte Work Package Queue mit einem sicheren ersten Schritt.
- Der Lösch-Use-Case ist als Destructive-Action-Planungsfall erfasst (nicht implementiert).

## Public/Private Status

Fiktiv öffentlich (das Fixture liegt in einem öffentlichen Repository — deshalb ausschließlich neutrale Namen und Platzhalter).
