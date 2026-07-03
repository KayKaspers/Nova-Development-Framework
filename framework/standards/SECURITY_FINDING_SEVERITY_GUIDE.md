# NDF Standard – Security Finding Severity Guide

## Purpose

This guide helps classify security findings consistently.

## Severity Levels

### Critical

Use when exploitation can directly lead to:

- remote code execution
- full account takeover
- production data deletion
- secret exfiltration
- unauthenticated destructive action
- bypass of owner/admin authorization

### High

Use when exploitation can lead to:

- token forgery
- privilege escalation
- production start with insecure secrets
- destructive action misuse
- broad data exposure
- insecure default in production

### Medium

Use when exploitation is plausible but requires additional conditions:

- missing CSP
- container runs as root
- incomplete rate limiting
- incomplete origin checks
- weak hardening
- insufficient audit privacy

### Low

Use when risk is limited or mostly hardening-related:

- missing optional automation
- incomplete docs
- minor information exposure
- weak warning text
- non-critical header missing

## Status Values

- Open
- Mitigated
- Accepted
- Superseded
- Needs Review

## Required Finding Fields

```yaml
id: "SEC-001"
title: ""
severity: ""
status: ""
affected_area: ""
evidence: ""
risk: ""
recommended_wp: ""
```
