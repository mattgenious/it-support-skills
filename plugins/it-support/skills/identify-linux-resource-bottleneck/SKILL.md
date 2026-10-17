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

Select one measurable change with a supported rollback. Preserve workloads,
volumes, services and security. Avoid global cache drops, blanket service disabling
and storage pruning. Verify latency/throughput for the original workload, keeping
sample duration and fixture constraints explicit.
