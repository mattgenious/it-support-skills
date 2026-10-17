---
name: investigate-windows-application-device-failure
description: Correlate recurring Windows application hangs, crashes, device resets or service failures without mistaking recovery events for causes.
---

# Investigate Windows application or device failure

Trigger: an application, service or peripheral repeatedly fails without a whole
machine restart. Whole-system interruption belongs to
[restart investigation](../investigate-unexpected-restart/SKILL.md).

Record component identity, symptom, first/latest occurrence, frequency, recovery
and recent app/driver/firmware/update or peripheral changes. Use Reliability Monitor,
Windows Error Reporting identifiers and bounded Get-WinEvent -FilterHashtable
queries for relevant providers/window. Inspect present devices with
Get-PnpDevice -PresentOnly and focused status/problem-code properties when needed.
A historical non-OK entry can mean disconnected or intentionally disabled, not a
repair target. Distinguish driver load failure from hardware-reported fault.

Normalize timestamps and timezone. Group recurring provider/event IDs, fault
buckets, exception signatures and device identities. Separate precursor, primary
fault and recovery noise. A recent update or adjacent event is not causal proof;
seek recurrence, mechanism and competing explanations. Route media/controller
warnings to [storage health](../../storage/assess-storage-health/SKILL.md),
active contention to [resource diagnosis](../../performance/identify-resource-bottleneck/SKILL.md).

Preserve logs/dumps and unsaved work. Collection does not authorize clearing logs,
deleting dumps, disabling error reporting, restarting, uninstalling or mass driver
updates. Choose one discriminating check; scoped repair uses
[reversible repair](../../../shared/verify-reversible-repair/SKILL.md).
Verify the original reproduction and a stated recurrence window; give observed
signatures, hypotheses, missing evidence and unresolved risk, not a volume of alerts.

## Sources

- [Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent)
- [Get-PnpDevice](https://learn.microsoft.com/en-us/powershell/module/pnpdevice/get-pnpdevice)
