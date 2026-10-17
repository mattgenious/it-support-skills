---
name: diagnose-wsl-kvm
description: Diagnose missing WSL nested virtualization.
---

# Diagnose missing WSL nested virtualization.

Trigger: QEMU/KVM or a nested VM stopped working inside WSL, especially after a
host update or reboot. Working Windows Terminal or Docker containers do not prove
nested virtualization works.

1. Read Windows/WSL/kernel versions, CPU vendor, firmware virtualization state and
   whether a Windows hypervisor is active. Do not infer UEFI disablement from an
   absent guest CPU flag alone.
2. In the exact WSL distribution, check svm (AMD) or vmx (Intel), the matching
   kvm_amd/kvm_intel module and focused kernel errors. /dev/kvm can be a stale
   device node; its existence is not proof of usable acceleration.
3. Test an empty QEMU instance with KVM, no disk/network and a bounded supervisor
   timeout. Exit for unavailable acceleration isolates the prerequisite from any
   guest OS. A paused healthy instance will require normal timeout cleanup.
4. Verify .wslconfig against current Microsoft documentation. nestedVirtualization
   defaults to true; making it explicit is a diagnostic hypothesis, not a cure.
   WSL shutdown interrupts all distributions and Docker: inspect consumers first
   and obtain approval for any actual interruption.
5. If firmware is enabled but SVM/VMX is hidden, investigate current Windows/WSL
   regressions. An elevated read-only HCS ProcessorCapabilities query can identify
   ERROR_INVALID_DATA (0x8007000D); an unelevated access result is not equivalent.

October 2026 maintainer reports describe AMD nested virtualization lost after
Windows servicing. An independently tested diskless KVM failure plus missing SVM
and elevated HCS 0x8007000D matches that signature; it does not prove every affected
update identity or establish a universal fix. Recheck current vendor status.

Sources:
- https://learn.microsoft.com/en-us/windows/wsl/wsl-config
- https://github.com/microsoft/WSL/issues/41917

Do not disable VBS, edit hypervisor binaries, swap system DLLs, downgrade WSL or
uninstall a security update as an automatic workaround. Update rollback has
reported boot-recovery risks and requires exact approval, servicing compatibility
and a rollback/recovery plan. An unresolved upstream prerequisite is an honest
blocker, not permission to weaken the machine. After repair, prove guest flags,
usable KVM and the original workload. Label an unverified workaround as such.
