---
name: recover-uncertain-operation
description: Recover from an uncertain operation without replaying it.
---

# Recover an uncertain operation

A timeout or lost receipt does not establish failure. Preserve the original
operation ID, target, request and last evidence. Use the authoritative read-only
status/journal and actual target effect to distinguish pending, committed, failed
and unknown; verify the original executor is stopped or fenced before a retry
that could duplicate a consequential effect.

Use the supported recovery/resume path. Do not forge completion, clear a live
lease, replay a charge/send/write, or delete history to make bookkeeping agree.
If ambiguity remains, report the exact missing observation and owner boundary.
Uncertain bookkeeping must not indefinitely block independently authorized,
nonconflicting work.
