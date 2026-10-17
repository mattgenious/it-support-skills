---
name: diagnose-macos-memory-pressure
description: Diagnose sustained Mac memory pressure and swap affecting a workload, including Apple silicon unified-memory demand.
---

# Diagnose macOS memory pressure

Trigger: system-wide sluggishness, allocation failures or swap growth accompany
memory-heavy work. Record hardware, affected operation, baseline responsiveness and
concurrent apps/VMs/containers. A specific hung app belongs to
[application stall](../diagnose-macos-application-stall/SKILL.md).

Use bounded Activity Monitor Memory observations and vm_stat or read-only
memory_pressure reporting (not modes that generate pressure). Compare the pressure
graph, compression, swap growth, wired memory and working sets over the symptom
window. Used memory alone is not shortage; compression can defer swap. On Apple
silicon, GPU/media/AI and CPU workloads share memory. CPU percentages span logical
cores and may exceed 100%; pair process activity with pressure, not guesses.

Identify aggregate demand from browser tabs, Electron apps, dev servers, VMs and
local models. Check usable storage if swap/scratch capacity is implicated and route
to [storage pressure](../diagnose-macos-storage-pressure/SKILL.md).
Prefer reduced concurrency, supported app lifecycle/tab suspension or equivalent
stable native builds over cache purges or system resets.

Exact changes require user approval and unsaved-work protection. Do not kill apps,
delete support data or change FileVault, Gatekeeper, SIP, endpoint policy or global
motion settings to gain memory. Use [reversible repair](../verify-reversible-repair/SKILL.md).
Verify pressure/swap trend and original responsiveness under comparable demand;
report physical-memory constraints rather than promising a tuning cure. A VM sample
does not establish physical Mac performance.

## Sources

- [Activity Monitor memory](https://support.apple.com/guide/activity-monitor/view-memory-usage-actmntr1004/mac)
- [Activity Monitor guide](https://support.apple.com/guide/activity-monitor/welcome/mac)
