---
name: diagnose-windows-startup-contention
description: Diagnose slow Windows sign-in or recurring startup load and select a reversible, dependency-aware change.
---

# Diagnose Windows startup contention

Separate firmware/boot, authentication, profile/shell and application readiness.
Measure the stage the user experiences; last boot time is not sign-in readiness.
Compare a representative slow start with a useful baseline and distinguish finite
servicing/indexing/sync from recurring unnecessary work.

Correlate startup apps, scheduled tasks, services and relevant boot/logon events
with CPU, I/O and memory during the delay. Task Manager's Startup impact is a
lead, not proof or a dependency map. Inspect the publisher, trigger and management
owner before treating an entry as expendable. Capture a bounded WPR boot/logon
trace only if its overhead, sensitive contents and reboot are justified.

Preserve authentication, security, management, backup, networking and required
device/app services. Prefer disabling one verified optional entry with a saved
before-state over removing it; check demand-start functionality and dependent
applications. A reboot or sign-out needs an access/unsaved-work plan.

Verify the same user's readiness time and the affected app after an authorized
change, including the next relevant startup. Report finite maintenance separately
from an improvement that is likely to persist.
