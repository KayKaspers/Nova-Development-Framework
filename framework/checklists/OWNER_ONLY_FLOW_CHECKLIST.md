# Checklist – Owner-only Flow

## DE – Zweck

Diese Checkliste gilt für Owner-only-Aktionen (irreversible Deletes, Resets, Token-Revokes): serverseitige Owner-Prüfung, sichere Bestätigungs-UX und sichere Audit-Events.

## EN – Purpose

This checklist applies to owner-only actions (irreversible deletes, resets, token revokes): server-side owner check, safe confirmation UX and safe audit events.

## Use When

- [ ] irreversible delete
- [ ] backup delete
- [ ] production reset
- [ ] tenant delete
- [ ] token/key revoke
- [ ] agent destructive action
- [ ] billing/security critical mutation

## Backend

- [ ] Owner role checked server-side
- [ ] Non-owner denied
- [ ] Admin role not silently treated as Owner unless decided
- [ ] Direct endpoint call protected
- [ ] Audit includes actor role

## Frontend

- [ ] Warning visible
- [ ] Impact preview visible
- [ ] Multiple confirmations if high risk
- [ ] Typed confirmation if irreversible
- [ ] Action button disabled until valid
- [ ] Result message visible

## Tests

- [ ] Owner succeeds
- [ ] Non-owner fails
- [ ] Missing confirmation fails
- [ ] Wrong typed confirmation fails
- [ ] Audit event safe
