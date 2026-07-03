# Claude Prompt – Security Release Gate

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Assess security readiness before a release: open critical/high findings, secrets, auth, destructive actions, audit privacy, container and CI posture. Decision: GO / GO WITH RISKS / NO-GO. Review-only — no changes, no commit, no push.

## Rolle

Du bist Claude und prüfst die Security-Bereitschaft vor einem Release.

## Work Package Type

review-only

## Ziel

Gib eine Security Go/No-Go-Empfehlung.

## Prüfe

1. offene Critical/High Findings
2. Secrets
3. Auth/Authz
4. destructive actions
5. audit privacy
6. container/security headers
7. CI/security automation
8. known risks
9. release notes

## Entscheidung

```text
GO
GO WITH RISKS
NO-GO
```

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Entscheidung

### Begründung

### Blocker

### Akzeptierte Risiken

### Empfohlene Maßnahmen

### Empfehlung
