---
name: investigate-macos-kernel-panic
description: Investigate Mac unexpected restarts and panic reports without treating a stack name as proof or provoking another panic.
---

# Investigate a Mac kernel panic

Distinguish kernel panic, app crash, power loss and hang. Preserve original panic
and relevant diagnostic/system reports with exact Mac model, architecture,
macOS/build, timestamps and recent peripheral/software changes; redact derivatives,
not the original evidence.

Compare the earliest error and recurring panic signature. A driver/process named
in the stack may observe or suffer the fault rather than cause it. Match build
and symbol provenance; mark missing/truncated reports or unavailable symbols as
limits. Correlate power, storage, memory and peripheral evidence without declaring
hardware failure from one report.

Do not provoke another panic or perform broad extension deletion, SMC/NVRAM resets
or OS reinstall as diagnosis. Any targeted disconnect/rollback/update needs owner
authority, unsaved-work protection and an access/recovery plan.

Verify the original workload and relevant recurrence window on the affected
physical Mac. A guest test or one successful boot establishes neither hardware
health nor durable panic resolution.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
