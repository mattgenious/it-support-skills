---
name: route-windows-support
description: Route a Windows support task to its focused capability.
---

# Windows support

For an unclear symptom start with [triage](../shared/evidence-led-triage/SKILL.md).
Load the narrow outcome:

- Slow workload: [resource bottleneck](performance/identify-resource-bottleneck/SKILL.md);
  slow sign-in: [startup](performance/diagnose-startup-contention/SKILL.md).
- Recurring app/device failure: [correlate evidence](reliability/investigate-application-device-failure/SKILL.md);
  unexpected reboot: [restart](reliability/investigate-unexpected-restart/SKILL.md).
- [Storage health](storage/assess-storage-health/SKILL.md),
  [security posture](security/assess-security-posture/SKILL.md),
  [printing](printing/diagnose-print-failure/SKILL.md),
  [WSL/KVM](virtualization/diagnose-wsl-kvm/SKILL.md).
- [Network path](../shared/diagnose-network-path/SKILL.md),
  [backup restore](../shared/verify-backup-restore/SKILL.md),
  [evidence handoff](../shared/collect-support-evidence/SKILL.md).

Use [reversible repair](../shared/verify-reversible-repair/SKILL.md) for changes.
Routing grants no machine-change authority.
