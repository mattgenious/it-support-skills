---
name: assess-windows-storage-health
description: Assess Windows disk warnings, slow I/O or suspected media failure before choosing backup, repair or replacement.
---

# Assess Windows storage health

Separate physical media, controller/cabling, filesystem and capacity pressure.
Map the affected volume to its real disk/storage stack before interpreting status.
If data is disappearing, the device resets or media failure is plausible, preserve
data first and minimize writes/repeated reads; a stress test is not a backup.

Correlate scoped storage/controller/System events with native disk/volume health,
reliability counters where exposed and actual I/O latency. A healthy status bit
does not rule out failure. SMART/raw values are vendor/transport dependent; USB,
RAID and virtual disks can conceal physical telemetry. Mark absent evidence
unknown rather than translating it into good health.

Check free capacity separately from wear or corruption. `chkdsk /scan` assesses
supported filesystem state, not media health; even online checks consume I/O.
An offline `/f`, `/r` or `/x`, vendor self-test, firmware action or disk replacement
needs distinct authority, backup/recovery and downtime planning. Avoid exhaustive
scans on suspected failing media before preservation.

Recommend monitoring, scoped filesystem repair, recovery or replacement from the
actual evidence. Verify both the storage state and original workflow afterward;
a repaired filesystem does not establish that the hardware is sound.
