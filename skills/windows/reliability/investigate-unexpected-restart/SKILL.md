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
Preserve logs and dumps. Propose one discriminating next check or authorized
reversible repair, with an explicit verification window. Do not reinstall unrelated
drivers or use registry cleaners. State when the cause remains unproven.
