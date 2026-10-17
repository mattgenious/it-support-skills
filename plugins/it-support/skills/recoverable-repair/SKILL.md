---
name: recoverable-repair
description: Plan reversible repairs without treating imperfect history as permanent lockout.
---

# Recoverable Repair

Name the current invariant a proposed change protects and its affected resource.
Preserve working configuration and data; prefer supported repair operations with
an exact rollback or forward-recovery path. Capture intent before effects and
verify the user's original symptom afterwards, not merely command exit.

Lost acknowledgements prohibit blindly replaying that operation, not all future
repair work. Preserve its identity and uncertain outcome. Establish or fence the
old executor, then admit new authorized non-conflicting work without inventing
completion, timing or charges. Keep an authenticated observation/recovery route
reachable when normal execution is blocked by incomplete bookkeeping.

Authorization, explicit revocation, code signatures and real concurrent resource
conflicts remain authoritative. Never erase historical evidence to make a guard
pass. A diagnostic or repair instruction does not authorize purchases, credential
changes, security weakening or destructive data removal.
