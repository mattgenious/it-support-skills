---
name: investigate-unexpected-restart
description: Investigate an unexpected Windows restart.
---

# Investigate an unexpected Windows restart.

Trigger: an unexpected reboot, bugcheck or shutdown interrupted work.

Read LastBootUpTime and bounded Get-WinEvent records for the incident window.
Correlate Kernel-Power, unexpected-shutdown, bugcheck and Windows Error Reporting
signals with relevant update, driver or storage observations. Normalize timestamps
to UTC. A shutdown record is evidence of interruption, not its cause.

Separate crash, planned servicing restart, power loss and incomplete logging.
Seek repeated signatures and a plausible mechanism before assigning causation.
Preserve logs and dumps; do not clear history or disable error reporting/dump
collection to make results look clean. Include onset/frequency, recovery and recent
hardware/power/firmware/security changes. Group repeated bugcheck/failure signatures
and separate precursor, primary fault and recovery noise. Collection failures and
missing event windows are unknowns, not proof of stability.

Route disk/controller concerns to [storage health](../../storage/assess-storage-health/SKILL.md),
protection/policy concerns to [security assessment](../../security/assess-security-posture/SKILL.md).
Propose one discriminating check or [authorized reversible repair](../../../shared/verify-reversible-repair/SKILL.md),
with an explicit reproduction/recurrence window. Reboots, rollback, uninstall or
firmware/driver changes require exact approval and recovery. Do not reinstall
unrelated drivers or use cleaners. State when the cause remains unproven.

## Sources

- [Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent)
- Original maintainer-owned reliability guidance, adapted with authorization.
