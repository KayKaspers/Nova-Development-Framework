# Security Baseline Lessons

## Validierter Security Flow

```text
Security Review -> Finding -> Risk -> Focused Fix -> Test -> Health Score Update
```

## SEC-01 Beispiel

Finding:

```text
Unsichere Production Defaults ohne Fail-Closed-Validierung
```

Mitigation:

- production-only Validator
- Fail closed bei unsicheren Defaults
- keine Secrets in Fehlermeldungen
- Development/Test bleiben nutzbar
- Unit-Test ergänzt
- Health Score moderat angehoben

## NDF-Regel

Security Score steigt nur nach verifizierter Verbesserung.
