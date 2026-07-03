# NDF Standard – Destructive Actions

## Pflichtablauf

```text
Blueprint -> Review -> Implementation -> Tests -> Audit -> Commit
```

## Pflichtkontrollen

- Blueprint
- Managed Scope
- Read-only Preview
- serverseitige Authorization
- Confirmation Flow
- Typed Confirmation bei irreversiblen Aktionen
- Rate Limit
- Audit Privacy
- Tests
- ADR

## Nicht erlaubt ohne ADR

- Wildcard Delete
- arbitrary host path
- shell delete mit User Input
- companion file delete aus User Input
- audit von sensiblen Rohwerten
