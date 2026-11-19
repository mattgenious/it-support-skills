---
name: diagnose-macos-memory-pressure
description: Diagnose sustained Mac memory pressure and swap affecting a workload, including Apple silicon unified-memory demand.
---

# Diagnose macOS memory pressure

Measure the slow workload and trend with Activity Monitor pressure, compression,
swap activity and responsible processes; `vm_stat`/read-only `memory_pressure`
can refine the observation. Used RAM or a nonzero historical swap total alone
does not establish current pressure.

Correlate sustained pressure/page activity with the actual delay. Distinguish
reclaimable cache, a growing process/working set and concurrent CPU/GPU demand;
Apple silicon's unified memory is shared, not separate unlimited GPU capacity.
Protect unsaved work and avoid memory-pressure stress modes or blind cache purges.

Choose a targeted app/workload adjustment with authority; do not disable swap or
system protections. Repeat representative work and compare pressure and latency
over a useful interval. State VM/physical evidence limits and whether relief
lasted after required applications resumed.
