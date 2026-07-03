# Claude Prompt – Destructive Action Implementation Gate

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Check whether a destructive work package may be implemented: an approved blueprint plus all safety controls (scope, preview, server-side authorization, typed confirmation, rate limit, audit privacy, tests, ADR) must exist. Decision: ALLOW IMPLEMENTATION / BLOCK IMPLEMENTATION / REQUIRE BLUEPRINT UPDATE. Review-only — no commit, no push.

## Rolle

Du bist Claude und prüfst, ob ein destruktives Work Package implementiert werden darf.

## Work Package Type

review-only

## Ziel

Vor Implementierung eines destruktiven Work Packages prüfen, ob alle Voraussetzungen erfüllt sind.

## Prüfe

1. Gibt es einen freigegebenen Blueprint?
2. Ist der Ressourcen-Scope strikt definiert?
3. Gibt es read-only Preview?
4. Gibt es serverseitige Autorisierung?
5. Gibt es Confirmation UX?
6. Gibt es typed confirmation?
7. Gibt es Rate Limit?
8. Gibt es Audit Privacy?
9. Gibt es Testplan?
10. Gibt es ADR/Decision Record?

## Entscheidung

```text
ALLOW IMPLEMENTATION
BLOCK IMPLEMENTATION
REQUIRE BLUEPRINT UPDATE
```

## Grenzen

Keine Codeänderungen. Kein Commit. Kein Push.

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Entscheidung

### Fehlende Voraussetzungen

### Risiken

### Empfehlung
