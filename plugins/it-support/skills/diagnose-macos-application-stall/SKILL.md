---
name: diagnose-macos-application-stall
description: Diagnose an application stall on macOS.
---

# Diagnose an application stall on macOS.

Trigger: a specific application becomes unresponsive or disrupts a workload.

Identify the affected app, operation, onset and reproduction. Read bounded process
CPU, memory pressure and relevant crash/hang evidence using available native tools.
Separate app-local stalls from system-wide resource pressure, storage waits,
indexing and thermal constraints. Measurements need timestamps and units.

Prefer application-scoped reversible remedies within the user's authorization.
Preserve unsaved work before terminating processes. Do not change privacy, login,
system-motion or security settings to manufacture a pass. Verify responsiveness
on the original workload; VM evidence does not qualify physical Mac behavior.

Use Activity Monitor process sampling and bounded Console crash/spin reports first;
sample/spindump or Instruments are escalation for a question basic evidence cannot
answer. Obtain trace/privilege authority, limit overhead and sensitive paths, and
stop the collector. A busy process need not be hung; check progress and I/O waits.
Route system-wide [memory pressure](../diagnose-macos-memory-pressure/SKILL.md),
[background contention](../diagnose-macos-background-contention/SKILL.md) or
[storage pressure](../diagnose-macos-storage-pressure/SKILL.md) to its owner.
Record recurring signatures and missing evidence, not just a successful app restart.

## Sources

- [Activity Monitor](https://support.apple.com/guide/activity-monitor/welcome/mac)
- [Unified logging](https://developer.apple.com/documentation/os/logging)
- [Performance and metrics](https://developer.apple.com/documentation/xcode/performance-and-metrics)
