# Project Brain – WP-027 Work Package Type Integration Notes

## Why This WP Exists

SpeakCore and CastCore showed that NDF needs a formal Work Package type system.

## Key Decisions

- Every Work Package gets a primary type.
- Every Claude prompt includes the type.
- Review-only, docs-only, code-fix, security-code-fix and health-score-update are distinct.
- Destructive actions require blueprint before implementation.

## Impact

Future NDF work should now be easier to control and review.

## Next Recommended Work Packages

1. NDF-WP-028 – Destructive Action Toolkit Checklist
2. NDF-WP-029 – Security Prompt Library Expansion
3. NDF-WP-030 – Health Score Automation Concept
4. NDF-WP-031 – Academy Examples from SpeakCore and CastCore
