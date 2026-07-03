# Checklist – Audit Privacy

## DE – Zweck

Diese Checkliste sichert das Prinzip „Belege ohne Leaks“: Audit-Events enthalten Ereignis, Akteur, Ressourcen-Klasse und Ergebnis — niemals Tokens, Secrets, Dateiinhalte oder volle Host-Pfade.

## EN – Purpose

This checklist protects the principle of evidence without leakage: audit events contain event, actor, resource class and result — never tokens, secrets, file contents or full host paths.

## Required Principle

```text
Evidence without leakage
```

## Include

- [ ] event type
- [ ] actor ID or actor class
- [ ] actor role
- [ ] resource class
- [ ] result
- [ ] reason code if useful
- [ ] timestamp
- [ ] request/correlation ID if available

## Do Not Include

- [ ] raw tokens
- [ ] API keys
- [ ] passwords
- [ ] secret values
- [ ] file contents
- [ ] full host paths
- [ ] sensitive filenames
- [ ] raw request body for sensitive actions
- [ ] checksums if they reveal inventory

## Tests

- [ ] Audit contains expected safe fields
- [ ] Audit does not contain secrets
- [ ] Audit does not contain raw path
- [ ] Failure audit is safe
