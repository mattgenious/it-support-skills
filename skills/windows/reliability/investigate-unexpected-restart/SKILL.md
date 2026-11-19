---
name: investigate-unexpected-restart
description: Investigate an unexpected Windows restart.
---

# Investigate an unexpected Windows restart

Establish when the machine stopped/responded/restarted, timezone, user impact
and whether this was planned servicing, a bugcheck, power loss, hang or reset.
Preserve System/Application events, dump files and relevant firmware/UPS evidence.

Build a short chronology around the earliest anomaly, shutdown initiation,
bugcheck/dump and subsequent boot. Kernel-Power or an unexpected-shutdown event
records an interruption; it does not identify its cause. Missing logs or dumps
are evidence gaps, not proof of power loss or hardware failure.

Match exact OS/build, driver/firmware and recurring failure signature; correlate
changes without treating coincidence as causation. Protect crash memory and
personal paths. Do not provoke another crash, clear logs or replace several
drivers to manufacture a clean run.

Choose a supported repair or known-good rollback within authority, preserving
access and recovery. Verify the original workload and recurrence conditions;
one successful boot establishes recovery, not a durable root-cause fix.
