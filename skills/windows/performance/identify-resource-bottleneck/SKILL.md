---
name: identify-windows-resource-bottleneck
description: Identify CPU, memory, storage, GPU or power contention limiting a Windows workload without generic tuning.
---

# Identify the resource limiting a Windows workload

Define the affected operation and its latency/throughput baseline, time window,
hardware, power source and recent change. Responsiveness is not throughput: a busy
background job can finish quickly while foreground scheduling or I/O is delayed.

## Collect discriminating evidence

Take a bounded Task Manager/Resource Monitor sample during the symptom; use
Performance Monitor over time when a single sample cannot separate causes.

- CPU: inspect per-core saturation, runnable pressure, frequency, interrupt/DPC
  work and thermal/power limits. Low aggregate use can hide one saturated core.
- Memory: compare available RAM, commit/limit, compression, hard faults and growing
  working sets. Browser tabs, VMs, containers and mapped data can collectively
  exhaust capacity. A high percentage alone does not establish a shortage.
- Disk: correlate latency, queue depth and issuing process with paging, updates,
  indexing, backup and scans. Route warnings or resets to
  [storage health](../../storage/assess-storage-health/SKILL.md).
- GPU: distinguish 3D, copy, video and compute engines, dedicated/shared memory,
  display/capture/overlay and hardware-acceleration workload. Headline GPU use can
  hide the constrained engine.
- Power/thermal: correlate clocks with power policy, battery, heat and airflow;
  high-performance mode can increase heat and worsen sustained throttling.
  Use read-only powercfg capability/blocker reports and supported battery/energy
  reports only when they answer the question; protect report paths and battery
  history. Changed boost/idle policy can trade latency for noise and battery life.

Use Process Explorer/RAMMap for unresolved process/memory attribution or bounded
WPR/WPA traces for scheduling/I/O latency when they will change the decision.
Record tool, units, timestamps, trace overhead and privilege/coverage gaps.

## Decide, authorize and verify

Rank causes with supporting and conflicting evidence. Prefer workload concurrency,
app settings or timing/scope of finite background work over global tuning. Driver,
firmware or app-native updates need supported provenance, compatibility and rollback.
Protection failures route to [security assessment](../../security/assess-security-posture/SKILL.md).

Use [reversible repair](../../../shared/verify-reversible-repair/SKILL.md) for exact
approved changes. Preserve page-file/crash-dump resilience, security, updates,
encryption and system animation preferences; avoid cleaners, debloat bundles,
blanket service disabling and destructive cache/rollback cleanup.

Compare the original operation under equivalent load and power conditions. Confirm
state, user-visible behavior and recurrence window; report cost in battery, heat,
noise or throughput rather than declaring every benchmark gain an improvement.

## Sources

- [Performance Monitor](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon)
- [Windows Performance Toolkit](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/)
- [Sysinternals](https://learn.microsoft.com/en-us/sysinternals/)
- [powercfg](https://learn.microsoft.com/en-us/windows-hardware/design/device-experiences/powercfg-command-line-options)
