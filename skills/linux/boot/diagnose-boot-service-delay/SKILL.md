---
name: diagnose-linux-boot-service-delay
description: Diagnose slow Linux boot or systemd service readiness using dependency, journal and resource evidence before changing units.
---

# Diagnose Linux boot or service delay

Trigger: boot, login or a named service takes too long or repeatedly stalls.
Confirm distribution, kernel, init system, boot identity, affected readiness
milestone and recent changes. On non-systemd hosts, use the init system's supported
timing/status/log interface; do not pretend systemd commands cover every Linux.

For systemd, compare systemd-analyze time, blame and critical-chain with bounded
journalctl -b -u <unit> and unit status/dependencies. A long blame duration may be
parallel or noncritical; dependency order and actual readiness matter. Separate
firmware/kernel time, unit activation, failed dependency, device/network wait and
application initialization. Inspect implicated services, timers, desktop autostart,
package jobs, indexing/logging and monitoring by purpose and owner.

For a busy service, correlate unit/cgroup CPU, memory, I/O and pressure with the
workload; host totals may hide quotas or noisy neighbors. Route to
[resource diagnosis](../../performance/identify-resource-bottleneck/SKILL.md).
Device/thermal errors need bounded journal/kernel evidence, not service tuning.

Prefer app readiness/configuration fixes or supported scheduling over disabling
units. Distribution package and configuration-management ownership can overwrite
local changes. Capture current unit/drop-in, dependencies and rollback; exact
restart/enable/disable/timeout changes and reboot require owner authorization,
service-impact assessment and access recovery. Preserve backup, updates, firewall,
mandatory access controls, auditing and encryption. Use
[reversible repair](../../../shared/verify-reversible-repair/SKILL.md).

Verify the original boot/service milestone under equivalent conditions, its
dependents and a bounded post-change journal window. Command success or a reduced
blame number alone does not prove usable service readiness.

## Sources

- [systemd-analyze](https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html)
- [systemd resource control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html)
