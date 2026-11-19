---
name: diagnose-wsl-kvm
description: Diagnose missing WSL nested virtualization.
---

# Diagnose WSL/KVM

Record Windows build/architecture, WSL package/kernel, exact distro/version,
physical/VM host and workload requirement. Distinguish WSL 1 from 2 and guest
virtualization capability from host hardware/firmware support.

Check read-only Windows feature/hypervisor state and the distro's CPU flags,
kernel/module diagnostics, `/dev/kvm` identity/permissions and effective KVM
availability. A device node can be stale; CPU flags or a loaded module alone do
not prove usable acceleration. Where justified and installed, a bounded diskless
QEMU KVM initialization probe with networking disabled can discriminate permission
from unavailable acceleration without booting an untrusted guest; stop the owned
probe on timeout.

Inspect the effective WSL configuration before editing. `nestedVirtualization`
defaults to true on supported configurations; writing it again is not a verified
repair. Distinguish elevated HCS `ProcessorCapabilities` query error `0x8007000D`
from an access-denied result. Preserve exact errors/builds; these observations do
not by themselves identify a firmware or security-policy cause.

A WSL shutdown/restart interrupts all distros and consumers such as Docker;
establish authority and save work/access first. Do not disable VBS/security,
replace system binaries or downgrade drivers as an automatic cure. Make a
supported targeted change only when evidence and recovery justify it, then repeat
the KVM/workload probe. Unchanged failure remains unresolved, not a claimed fix.

[WSL configuration defaults](https://learn.microsoft.com/en-us/windows/wsl/wsl-config).
