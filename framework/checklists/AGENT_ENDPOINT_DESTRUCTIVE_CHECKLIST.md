# Checklist – Agent Endpoint Destructive Action

## Endpoint

- [ ] Dedicated endpoint
- [ ] No generic `/exec`
- [ ] Strict request schema
- [ ] Minimal response body

## Authentication / Authorization

- [ ] Token gate
- [ ] Scope validation
- [ ] Managed resource only
- [ ] Rate limit
- [ ] Audit

## Input Safety

- [ ] No raw command from request
- [ ] No raw host path from request
- [ ] No wildcard operation
- [ ] No shell expansion
- [ ] Canonical validation

## Output Safety

- [ ] No secrets
- [ ] No host paths if sensitive
- [ ] No token echo
- [ ] No raw stack trace to user

## Documentation

- [ ] ADR required
- [ ] Risk entry required
- [ ] Operator docs updated
