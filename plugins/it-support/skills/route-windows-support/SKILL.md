---
name: route-windows-support
description: Route a Windows support task to its focused capability.
---

# Windows support

For an unclear symptom start with [triage](../evidence-led-triage/SKILL.md).
Load the narrow outcome:

- Slow workload: [resource bottleneck](../identify-windows-resource-bottleneck/SKILL.md);
  slow sign-in: [startup](../diagnose-windows-startup-contention/SKILL.md).
- Recurring app/device failure: [correlate evidence](../investigate-windows-application-device-failure/SKILL.md);
  unexpected reboot: [restart](../investigate-unexpected-restart/SKILL.md).
- [Storage health](../assess-windows-storage-health/SKILL.md),
  [security posture](../assess-windows-security-posture/SKILL.md),
  [printing](../diagnose-windows-print-failure/SKILL.md),
  [WSL/KVM](../diagnose-wsl-kvm/SKILL.md).
- [Network path](../diagnose-network-path/SKILL.md),
  [backup restore](../verify-backup-restore/SKILL.md),
  [evidence handoff](../collect-support-evidence/SKILL.md).

Use [reversible repair](../verify-reversible-repair/SKILL.md) for changes.
Routing grants no machine-change authority.
