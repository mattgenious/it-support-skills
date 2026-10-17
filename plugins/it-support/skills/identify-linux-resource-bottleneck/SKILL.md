---
name: identify-linux-resource-bottleneck
description: Identify the resource limiting a Linux workload.
---

# Identify the resource limiting a Linux workload.

Start from the affected workload and compare CPU saturation, runnable tasks,
memory pressure, swap, storage latency and network waits. Use available tools
such as vmstat, free, ps, iostat or /proc pressure data for a bounded sample.
Account for containers/cgroups before interpreting host totals. A cache is not a
memory leak; high utilization alone is not the user's bottleneck.

Load average includes runnable and uninterruptible tasks, not just CPU use.
Compare user/system, iowait, steal, IRQ/softirq and per-core demand before blaming
CPU. PSI reports delayed work: some versus all stalled tasks discriminate severity.
Use available memory, reclaim, major faults and swap traffic rather than used RAM;
account for tmpfs, kernel slabs, huge pages and aggregate workloads. Storage latency,
queueing, writeback and throughput differ; high utilization is device-dependent.
Inspect cgroup v2 quotas/pressure, VM steal, affinity/NUMA or noisy neighbors when
host-wide figures hide workload limits. Record kernel/distro, units, time window,
tool availability, permissions and evidence gaps.

Bounded journal/kernel, sensor and frequency evidence can separate thermal/power,
driver/firmware, hardware errors or failing storage from software demand. Profiling
with perf, ftrace or eBPF is a next step only for a named unresolved scheduling,
lock, allocation or application-latency question: obtain privilege/privacy authority,
record overhead and stop afterward; do not loosen perf security or lockdown.

Prefer demonstrated app configuration, algorithms, indexes, concurrency, batching
or caching over global kernel tuning. Swap/zram, overcommit, huge-page/OOM policy,
schedulers, read-ahead, writeback, mounts, RAID/discard and firmware are workload-
and recovery-sensitive contracts, not universal recommendations. Distribution and
configuration-management ownership matter. Preserve security/mitigations, services,
volumes and data; avoid cache drops, blanket disabling and pruning. Storage risk
requires backup/preservation before further writes.

Select one measurable change with exact approval and supported rollback via
[reversible repair](../verify-reversible-repair/SKILL.md).
Verify original latency/throughput and competing workload impact under comparable
load/power conditions, stating sample duration and fixture constraints. Network
waits route to [network diagnosis](../diagnose-linux-network-performance/SKILL.md);
slow readiness to [boot/service diagnosis](../diagnose-linux-boot-service-delay/SKILL.md).

## Sources

- [Linux administration](https://docs.kernel.org/admin-guide/index.html)
- [Memory management](https://docs.kernel.org/admin-guide/mm/index.html)
- [Pressure Stall Information](https://docs.kernel.org/accounting/psi.html)
- [CPU frequency scaling](https://docs.kernel.org/admin-guide/pm/cpufreq.html)
- [cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html)
- [perf security](https://docs.kernel.org/admin-guide/perf-security.html)
