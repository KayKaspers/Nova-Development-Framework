# Checklist – Backup Delete Safety

## Scope

- [ ] Only managed backups can be deleted
- [ ] One backup per request
- [ ] No arbitrary path parameter
- [ ] No wildcard delete
- [ ] Backup filename/resource ID strictly validated
- [ ] Resolved path remains inside managed backup directory

## Companion Metadata

- [ ] Metadata file is exactly derived
- [ ] Metadata path is not supplied by user
- [ ] Metadata path remains inside managed scope
- [ ] Missing metadata behavior is defined

## Authorization / Confirmation

- [ ] Owner-only or explicitly approved role
- [ ] Read-only preview
- [ ] Warning UI
- [ ] Multiple confirmations
- [ ] Typed confirmation, e.g. `DELETE BACKUP`
- [ ] Rate limit

## Audit

- [ ] Backup delete audited
- [ ] No sensitive filename/path/content/checksum if forbidden
- [ ] Success/failure captured

## Tests

- [ ] valid backup delete
- [ ] invalid backup name rejected
- [ ] traversal rejected
- [ ] metadata derivation tested
- [ ] unauthorized actor rejected
- [ ] wrong confirmation rejected
