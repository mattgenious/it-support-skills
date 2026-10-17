---
name: investigate-macos-kernel-panic
description: Investigate Mac unexpected restarts and panic reports without treating a stack name as proof or provoking another panic.
---

# Investigate a Mac kernel panic

Trigger: unexpected restart, repeated panic report or sleep/wake reboot. Outcome:
a correlated failure signature and justified recovery/escalation path, not a
faulty-driver guess from one function name.

Confirm OS/build, model/architecture, incident time/timezone, last good state,
updates, power and peripherals. Distinguish kernel panic from app crash, shutdown,
battery/power loss and hang. Resume-only failures correlate with
[sleep/wake continuity](../../sleep-wake/verify-sleep-wake-continuity/SKILL.md).
Preserve existing Console/DiagnosticReports artifacts before filtering; prefer a
scoped panic report over broad sysdiagnose. Reports can expose host identity,
serials, paths and memory-related details.

Extract OS/kernel build, panic string, incident/boot context, uptime, implicated
process/thread, backtrace and extensions where present. Formats differ across
releases and Intel/Apple silicon; record missing/truncated sections. Find earliest
preceding error and stable signature across available incidents. A watchdog stack
can name the observer; last-loaded extension can be incidental. Proprietary fields
and addresses need matching-build evidence; avoid unsupported symbol decoding or
another machine's interpretation.

Rank regression, peripheral/driver, storage, thermal/power and hardware hypotheses
from chronology and recurrence. Search vendor notes using sanitized signature/build,
not raw reports/identifiers. A matching forum title or passing diagnostic is not
confirmed cause or guaranteed fix.

If useful and authorized, use Apple diagnostics, controlled peripheral comparison
or architecture-appropriate Safe Mode after saving work and preserving recovery
access. These may require restart and local interaction; Windows-host review cannot
establish Mac hardware acceptance. Failing storage has data-preservation priority.
Do not provoke panic, mass-unload extensions, reset security/power settings or apply
generic Intel SMC/NVRAM recipes to Apple silicon. Updates/reinstalls use
[reversible repair](../../../shared/verify-reversible-repair/SKILL.md) with backup,
compatibility, recovery and exact permission.

Return signature, decisive evidence, competing explanations and next owner/action.
After authorized change verify original workload and appropriate recurrence window;
one clean boot is partial evidence, not cured intermittent panic. Preserve reports
and state physical-Mac verification still required.

## Sources

- [Mac restarted because of a problem](https://support.apple.com/en-us/102382)
- [Apple Diagnostics](https://support.apple.com/en-us/102550)
- [Pinned adaptation and license](SOURCE.md)
