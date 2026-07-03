# Destructive Action Test Plan Template

## Action

`<action>`

## Required Tests

### Authorization

- [ ] owner succeeds
- [ ] non-owner fails
- [ ] unauthenticated fails

### Validation

- [ ] valid resource accepted
- [ ] invalid resource rejected
- [ ] traversal rejected
- [ ] unmanaged resource rejected

### Confirmation

- [ ] missing confirmation rejected
- [ ] wrong typed confirmation rejected
- [ ] correct typed confirmation accepted

### Rate Limit

- [ ] rate limit enforced
- [ ] failure mode documented

### Audit

- [ ] success audited
- [ ] failure audited or documented
- [ ] no sensitive fields in audit

### Execution

- [ ] only intended resource affected
- [ ] companion resource handled safely
