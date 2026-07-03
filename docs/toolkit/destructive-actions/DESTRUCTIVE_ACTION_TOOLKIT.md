# Destructive Action Toolkit

## Purpose

This toolkit helps NDF projects design and implement dangerous actions safely.

A destructive action is any action that permanently removes, revokes, overwrites, deprovisions, purges or invalidates a resource.

## Examples

- delete backup
- delete container
- remove volume
- delete tenant
- reset production
- revoke token
- delete server record
- purge logs
- deprovision agent-managed resource

## Required NDF Flow

```text
Destructive Blueprint
-> Nova Review
-> Implementation Prompt
-> Focused Tests
-> Kay Review
-> Commit
-> CI
-> Follow-up Health/Risk Update
```

## Mandatory Controls

| Control | Required |
|---|---|
| Blueprint before implementation | yes |
| Managed resource scope | yes |
| Read-only preview | yes |
| Server-side authorization | yes |
| Owner-only for critical actions | yes |
| Multiple confirmations | yes |
| Typed confirmation | yes for irreversible actions |
| Rate limit | yes |
| Audit privacy | yes |
| ADR/Decision Record | yes |
| Tests | yes |

## The Reference Project A Pattern

Reference Project A validated this model with a controlled managed backup delete flow:

- exactly one strictly validated managed backup archive
- exactly derived metadata companion file
- OWNER-only web flow
- token-gated agent endpoint
- warning UI
- three mandatory confirmations
- typed `DELETE BACKUP`
- rate limit
- audit without sensitive file/path data
- ADR and tests

## Toolkit Files

Use these checklists and templates:

- `DESTRUCTIVE_ACTION_BLUEPRINT_CHECKLIST.md`
- `DESTRUCTIVE_IMPLEMENTATION_REVIEW_CHECKLIST.md`
- `OWNER_ONLY_FLOW_CHECKLIST.md`
- `AUDIT_PRIVACY_CHECKLIST.md`
- `BACKUP_DELETE_SAFETY_CHECKLIST.md`
- `AGENT_ENDPOINT_DESTRUCTIVE_CHECKLIST.md`
- `DESTRUCTIVE_ACTION_BLUEPRINT_TEMPLATE.md`
- `DESTRUCTIVE_ACTION_ADR_TEMPLATE.md`
- `DESTRUCTIVE_ACTION_TEST_PLAN_TEMPLATE.md`
- `DESTRUCTIVE_ACTION_RISK_REGISTER_TEMPLATE.md`

## NDF Rule

If a feature can destroy, erase, revoke or deprovision something, it must start as a destructive blueprint.
