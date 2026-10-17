---
name: diagnose-macos-background-contention
description: Identify Mac login items, maintenance, extensions or thermal and energy contention delaying foreground work.
---

# Diagnose macOS background contention

Trigger: login stays busy, fans/battery use rise or foreground work slows while
background processes run. Define the workload, elapsed-time/energy baseline, power
source, model and recent upgrade/change. Distinguish finite post-upgrade maintenance
from persistent unwanted activity.

Use Activity Monitor CPU/Energy/Disk/Network and Login Items & Extensions first.
Correlate Spotlight, Photos analysis, iCloud, Time Machine and updates with the
symptom window. Inspect implicated launch agents/daemons, menu-bar utilities,
browser extensions and endpoint tools; identify publisher/owner and purpose rather
than treating all persistence as unwanted. For unresolved latency, bounded sample,
Console predicates, fs_usage/nettop or Instruments/xctrace may discriminate cause;
record tool availability, elevated access, overhead and sensitive path/process data.
Do not leave tracing or verbose log streaming running after the check.

Correlate thermal pressure, battery health, Low/High Power Mode, displays/scaling,
HDR/refresh, capture/video conferencing, peripherals and graphics demand with
sustained slowdown. Fanless and actively cooled models differ. Apple silicon native
builds may reduce translation cost when functionally equivalent and stable; an
Intel-only process is not itself a defect. Route sustained pressure to
[memory diagnosis](../diagnose-macos-memory-pressure/SKILL.md) or
[storage diagnosis](../diagnose-macos-storage-pressure/SKILL.md).

Prefer allowing finite maintenance to finish or supported timing/scope changes.
Exact login-item/app changes need approval, captured state and rollback; removal
can break sync, backup, licensing, accessibility, security or access. Safe Mode,
alternate accounts or disconnected peripherals require authorized disruption;
platform-specific NVRAM/SMC/recovery/reinstall/erase are not generic tuning.
Preserve power/display/motion preferences and security/management protections.
Use [reversible repair](../verify-reversible-repair/SKILL.md).

Verify foreground readiness and energy/heat cost under comparable conditions,
confirm required background functions still work, and stop the temporary collector.
Report finite maintenance, persistent contention and unproven thermal hypotheses
separately. Physical hardware claims need physical Mac evidence.

## Sources

- [Login Items & Extensions](https://support.apple.com/guide/mac-help/change-login-items-extensions-settings-mtusr003/mac)
- [Activity Monitor energy](https://support.apple.com/guide/activity-monitor/view-energy-consumption-actmntr43697/mac)
- [Performance and metrics](https://developer.apple.com/documentation/xcode/performance-and-metrics)
- [Unified logging](https://developer.apple.com/documentation/os/logging)
- [Apple Platform Security](https://support.apple.com/guide/security/welcome/web)
