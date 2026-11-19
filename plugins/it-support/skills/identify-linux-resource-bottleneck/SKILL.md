---
name: identify-linux-resource-bottleneck
description: Identify the resource limiting a Linux workload.
---

# Identify a Linux resource bottleneck

Observe a bounded slow interval and comparable healthy work. Record distro/kernel,
physical/VM/container context, workload and namespace/cgroup. Use available native
tools such as `top`, `vmstat`, `pidstat`, `iostat` and `/proc/pressure` without
installing a monitoring stack merely to collect a snapshot.

| Candidate | Distinction that changes the diagnosis |
| --- | --- |
| CPU | Per-core runnable work, user/system/IRQ, steal and quotas/affinity. Load includes uninterruptible tasks; iowait and aggregate CPU are not standalone disk/CPU diagnoses. |
| Memory | Available/reclaimable memory, working set, faults, swap activity and PSI trends, not used RAM alone. Interpret cgroup limits/events and NUMA placement where relevant. |
| I/O | Device/process throughput, latency, queue and blocked work; shared/virtual storage can conceal the underlying limit. Capacity and media health are separate. |
| Pressure | PSI `some` versus `full`, scoped to host or cgroup, describes stalled work; correlate it with the actual application delay. |
| Power | Effective clocks, throttling and thermal/power limits on the real host, where observable. A guest may lack that telemetry. |

Differentiate resource saturation from lock contention, external latency and
intentional throttling. Use bounded profiling/tracing only for a concrete missing
observation, protecting overhead and sensitive data. Suspected media failure
calls for preservation, not stress.

Change one justified owner-controlled setting with rollback; preserve kernel
protections and service dependencies. Repeat the original workload and report
the limiting evidence, useful effect and remaining uncertainty.
