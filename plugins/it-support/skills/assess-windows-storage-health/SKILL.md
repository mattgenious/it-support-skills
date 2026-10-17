---
name: assess-windows-storage-health
description: Assess Windows disk warnings, slow I/O or suspected media failure before choosing backup, repair or replacement.
---

# Assess Windows storage health

Confirm the target disk/volume, symptom window and current backup. Distinguish
physical media, transport/controller, filesystem, capacity and workload faults;
a filesystem scan cannot clear a physical disk.

## Evidence and decisions

Use Disk Management, Get-Disk, Get-PhysicalDisk, Get-Volume and bounded disk,
storport/controller events as available. Record model, firmware, bus, device ID,
volume mapping, temperature and collector limitations. Unsupported health counters
are unknown, not zero. Correlate latency, queueing, active time and issuing process
in Resource Monitor with paging, indexing, scanning or updates.

When media detail changes the decision, use a trusted vendor utility or smartctl
from its maintained distribution; verify publisher/hash and acquisition provenance
before execution. Read SMART/NVMe warnings, media/data-integrity errors, pending or
uncorrectable sectors, wear and self-test history against that device family's
definitions. Raw attributes are not universal scores. A passing health bit does
not exclude failure; an old interface error alone does not prove media damage.

- Disappearance, critical warnings, rising uncorrectable errors or severe heat:
  minimize writes and diagnostic stress; prioritize authorized backup/image and
  replacement. Data recovery takes precedence over repair or benchmarking.
- Recurring resets, thermal issues, wear or mixed evidence: choose one check that
  separates media from cable/controller/firmware or filesystem faults.
- No correlated fault: report the observed window and unavailable checks, not a
  guarantee of future health.

## Authority, recovery and verification

Read-only health queries still need collection authority. A supported short
self-test needs explicit approval for device activity, device ID and expected
duration; re-query its result after that window. Avoid long/stress tests on a
failing drive. An explicitly approved chkdsk <volume>: /scan answers filesystem
integrity only; retain result text and relevant event record.

Offline repair, /f, /r, /x, dismount, reboot, firmware/controller changes, trim,
formatting or repartitioning require separate exact authorization and a recovery
plan. Do not manually defragment SSDs or expose volume contents/recovery keys.
Use [reversible repair](../verify-reversible-repair/SKILL.md) for
changes. Verify the affected layer and original symptom without another risky
stress run; report unresolved health uncertainty and backup state.

## Sources

- [smartmontools documentation](https://www.smartmontools.org/wiki/TocDoc)
- [chkdsk](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/chkdsk)
- [Windows Performance Toolkit](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/)
