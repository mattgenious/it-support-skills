---
name: investigate-windows-application-device-failure
description: Correlate recurring Windows application hangs, crashes, device resets or service failures without mistaking recovery events for causes.
---

# Investigate a Windows application/device failure

Capture exact symptom, process/device identity, Windows/driver/app builds,
timestamp/timezone and recurrence. Distinguish an app crash/hang, device reset,
service recovery and a whole-system interruption; preserve unsaved work and dumps.

Correlate Reliability Monitor and narrowly scoped Application/System/provider
events with the first failure, not only the recovery notification. Event ID,
driver presence or adjacent timing alone does not establish cause. Check device
instance, error/status and current connection: a historical disconnected or
intentionally disabled PnP entry is not a present hardware failure.

Use a bounded dump/trace only for a specific uncertainty and protect memory/private
paths. Compare a repeatable signature and recent controlled changes; a loaded
driver or named stack frame can be an observer rather than the fault origin.

Choose an evidence-supported, owner-approved repair with rollback and preserved
access; avoid broad driver replacement or service resets. Repeat the original
workflow and observe the relevant recurrence window, distinguishing recovery now
from demonstrated durable resolution.
