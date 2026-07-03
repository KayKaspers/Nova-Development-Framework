# Destructive Action Blueprint Template

## Work Package

`<PROJECT>-WP-### – <title>`

## Type

`destructive-blueprint`

## Action

What will be deleted, revoked, reset or deprovisioned?

## Resource Scope

### Allowed

- resource

### Forbidden

- resource

## Managed Resource Rule

How is the resource proven to be managed by the application?

## Read-only Preview

What will the user see before execution?

## Authorization

Required role:

```text
OWNER | ADMIN | custom
```

Server-side checks:

- check

## Confirmation Flow

- warning
- checkbox 1
- checkbox 2
- typed confirmation

Typed confirmation:

```text
DELETE <RESOURCE>
```

## Rate Limit

Define rate limit.

## Audit Privacy

### Include

- safe fields

### Exclude

- sensitive fields

## Tests

- valid target
- invalid target
- unauthorized actor
- wrong confirmation
- audit privacy

## ADR

Required:

```text
yes
```

## Recommendation

```text
ALLOW IMPLEMENTATION | REWORK BLUEPRINT | STOP
```
