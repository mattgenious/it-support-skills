---
name: identify-windows-resource-bottleneck
description: Identify CPU, memory, storage, GPU or power contention limiting a Windows workload without generic tuning.
---

# Identify a Windows resource bottleneck

Measure the affected workflow during a bounded slow interval and a useful
comparison. Record OS/build, hardware, process/instance, workload and power mode.
Preserve unsaved work; overheating or suspected media failure takes precedence.

| Candidate | Evidence that distinguishes it |
| --- | --- |
| CPU | Per-core and responsible-process activity, effective clocks, interrupts/DPC and runnable work. Low total CPU can conceal one saturated core; high CPU can be useful work. |
| Memory | Commit/limit, available memory, hard-fault/page activity and workload trend. Used RAM alone is not pressure; a hard fault can read a mapped file, not just pagefile. |
| Storage | Device/process I/O, latency and queue during the delay. Active time or free capacity alone does not establish a bottleneck or media health. |
| GPU | Relevant engine, dedicated/shared memory and CPU/GPU synchronization. One aggregate percentage can hide engine saturation. |
| Power/thermal | Clock/thermal/power-limit evidence on the actual AC/battery and cooling setup. More performance can cost heat, battery or stability. |

Start with Task Manager, Resource Monitor and scoped performance counters.
Use bounded WPR/ETW only for a named unresolved question, with recording size,
overhead, permissions and sensitive trace contents controlled. Installed tools and
counter names vary by build/language.

Link the constrained resource and responsible work to the user's delay before
proposing a change. Preserve pagefile/crash-dump policy, security, update agents
and OS motion preferences. Apply one authorized reversible change, repeat the
same workflow and report actual improvement plus residual uncertainty.
