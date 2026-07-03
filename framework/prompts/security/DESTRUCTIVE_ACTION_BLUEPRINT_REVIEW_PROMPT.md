# Claude Prompt – Destructive Action Blueprint Review

> Sprachstatus / Language status: Foundation 0.2 prompt. Zweck, Grenzen und Rückmeldung DE/EN. / Purpose, boundaries and feedback DE/EN.

## EN – Purpose

Review a destructive action blueprint before implementation is allowed: managed scope, read-only preview, authorization, confirmations, rate limit, audit privacy, test plan and ADR. Decision: ALLOW IMPLEMENTATION / REWORK BLUEPRINT / STOP. Review-only — no code changes, no commit, no push.

## Rolle

Du bist Claude und prüfst einen Blueprint für eine destructive Action nach NDF.

## Work Package Type

review-only

## Ziel

Bewerte, ob der Blueprint sicher genug ist, bevor Implementierung erlaubt wird.

## Prüfe

1. Managed Scope
2. Read-only Preview
3. Authorization
4. Confirmation Flow
5. Typed Confirmation
6. Rate Limit
7. Audit Privacy
8. Test Plan
9. ADR
10. Remaining Risks

## Grenzen

Keine Codeänderungen. Kein Commit. Kein Push.

## Rückmeldung an Nova

Nova (ChatGPT) ist die ChatGPT-basierte Planungs-, Architektur- und Review-Rolle (siehe `docs/workflow/NOVA_CHATGPT_ROLE.md`). / Nova (ChatGPT) is the ChatGPT-based planning, architecture and review role.

### Entscheidung

`ALLOW IMPLEMENTATION | REWORK BLUEPRINT | STOP`

### Begründung

### Fehlende Controls

### Risiken

### Empfehlung
