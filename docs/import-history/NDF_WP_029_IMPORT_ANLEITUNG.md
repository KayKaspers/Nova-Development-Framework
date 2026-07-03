# Import-Anleitung – NDF-WP-029 Security Prompt Library Expansion

## Zielrepository

`Nova-Development-Framework`

## Zweck

Dieses Paket erweitert die NDF-Prompt-Bibliothek um Security-spezifische Prompts, Checklisten und Standards.

Es baut auf den Erkenntnissen aus den Referenzprojekten auf:

- Referenzprojekt A: destructive actions, Owner-only, Audit Privacy, Agent-Endpunkte
- Referenzprojekt B: Security Baseline Review, Fail-closed Secret Validation, CSP, Container-Hardening, Health Score

## Import-Schritte

1. ZIP entpacken.
2. Inhalt in das NDF-Repository kopieren.
3. Änderungen prüfen.
4. Commit erstellen:

```text
feat(prompts): expand security prompt library
```

5. Push origin.

## Erwartete Bereiche

```text
docs/toolkit/security-prompts/
framework/prompts/security/
framework/checklists/security/
framework/standards/
docs/academy/
docs/adr/
project-brain/
docs/roadmap/
```

Foundation 0.1 bleibt eingefroren. Dieses Paket gehört zu Foundation 0.2.
