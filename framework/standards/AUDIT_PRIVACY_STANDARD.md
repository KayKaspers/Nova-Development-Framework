# NDF Standard – Audit Privacy

## Prinzip

Audit muss beweiskräftig sein, ohne sensible Daten zu leaken.

## Erlaubt

- actor id/role
- action type
- resource class
- result
- reason code
- timestamp
- correlation id

## Verboten

- Secrets
- Tokens
- Passwörter
- Host-Pfade
- Inhalte
- sensible Dateinamen
- rohe Request-Bodies
