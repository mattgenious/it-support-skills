---
name: diagnose-linux-boot-service-delay
description: Diagnose slow Linux boot or systemd service readiness using dependency, journal and resource evidence before changing units.
---

# Diagnose Linux boot/service delay

Measure the delayed user-visible readiness: kernel boot, login, network, mount
or application availability. Record distro/init system, boot identity and clock;
systemd tools do not apply to every Linux target.

On systemd, combine `systemd-analyze` timing, `critical-chain`, relevant unit
dependencies and scoped boot/unit journal entries. `blame` measures activation
duration, including parallel work; its longest row need not delay the requested
outcome. A unit marked active may not yet serve its actual clients.

Distinguish CPU/I/O contention, device/network waits, failed dependencies, retry
timeouts and application initialization. Check the real dependent's readiness
and package/configuration-management owner before proposing a unit edit. Missing
journal coverage is not evidence that a stage was healthy.

Preserve boot, storage, networking, security and remote access. Prefer an
owner-controlled drop-in with saved state and rollback over editing vendor units
or disabling a slow-looking dependency. Reboot/service interruption requires
authority and a recovery path. Verify the original readiness metric and dependent
behavior, not only `systemctl` success.
