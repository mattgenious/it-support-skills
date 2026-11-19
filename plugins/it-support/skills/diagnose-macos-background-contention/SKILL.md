---
name: diagnose-macos-background-contention
description: Identify Mac login items, maintenance, extensions or thermal and energy contention delaying foreground work.
---

# Diagnose macOS background contention

Observe the actual foreground delay with macOS/architecture, AC/battery state
and relevant process/resource trends. Distinguish finite Spotlight, Photos,
sync, backup or update work from a recurring unwanted job before disabling it.

Correlate CPU/I/O/memory, energy, effective clocks/thermal pressure where exposed,
login/background items, extensions and launchd ownership. System daemons,
per-user agents and app-managed helpers have different owners and lifecycles.
A familiar process name or high cumulative energy is not cause by itself; a
guest can lack physical power/thermal evidence.

Inspect narrowly and preserve privacy, management, security, backup and ongoing
sync. Prefer the owning app's scheduling/pause/removal controls with a known
recovery path. Do not broadly delete plists, unload daemons, reset SMC/NVRAM or
disable protections to improve a resource snapshot.

After an authorized targeted change, repeat the foreground workflow under the
same power/workload conditions and check required background functions. Report
temporary relief from paused maintenance separately from a durable improvement,
including battery/thermal tradeoffs.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
