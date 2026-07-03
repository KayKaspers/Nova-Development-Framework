# Checklist – Audit Privacy

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
