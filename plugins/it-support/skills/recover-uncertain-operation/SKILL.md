---
name: recover-uncertain-operation
description: Recover from an uncertain operation without replaying it.
---

# Recover from an uncertain operation without replaying it.

Trigger: an operation lost its acknowledgement, executor or completion record.

Preserve the original operation identity, inputs, evidence and unknown outcome.
Establish whether its executor is alive and which resources it may still affect.
Use authenticated read-only observation before another conflicting mutation.
When the old executor is stopped or safely fenced, permit independently authorized
non-conflicting work without fabricating its completion time, success or charges.
Retain a reachable observation and recovery path; incomplete bookkeeping alone
must not permanently lock out all future support.

Reconcile exact evidence instead of blindly repeating a command or payment.
Current authorization, explicit revocation and signatures remain authoritative.
Do not delete historical evidence to bypass a guard. Report whether execution is
fenced, accounting remains uncertain and new work is actually usable.
