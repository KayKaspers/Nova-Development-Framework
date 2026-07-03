# Reference Project A Lessons Learned

## L-001 – Destructive Actions brauchen einen Blueprint

Keine Delete-/Purge-/Remove-/Deprovision-Funktion ohne vorherigen Blueprint.

## L-002 – Read-only vor destructive

Vor Löschung muss klar angezeigt werden, was betroffen ist.

## L-003 – OWNER-only ist ein Standardpattern

High-risk Operationen brauchen serverseitige OWNER-Prüfung, nicht nur UI-Schutz.

## L-004 – Mehrfachbestätigung reduziert Fehlbedienung

Warnanzeige, Pflichtbestätigungen und getippte Bestätigung sind Security-relevant.

## L-005 – Audit darf nicht leaken

Audit muss beweisen, dass etwas passiert ist, darf aber keine sensiblen Details enthalten.

## L-006 – Managed Scope verhindert Pfadmissbrauch

Keine freien Host-Pfade. Keine unvalidierten Dateinamen. Keine unsichere Companion-File-Ableitung.

## L-007 – Agent-Endpunkte sind Security Boundaries

Agent-Endpunkte brauchen Token-Gate, Scope, Rate Limit, Audit und minimale Antwortdaten.

## L-008 – ADRs sind Pflicht bei irreversiblen Entscheidungen

Jede irreversible oder sicherheitsrelevante Architekturentscheidung braucht ADR/Decision Record.
