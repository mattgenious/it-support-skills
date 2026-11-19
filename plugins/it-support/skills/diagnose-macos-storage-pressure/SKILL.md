---
name: diagnose-macos-storage-pressure
description: Distinguish Mac APFS capacity pressure, swap or scratch contention and storage faults before cleanup or repair.
---

# Diagnose macOS storage pressure

Separate capacity, I/O contention and media/filesystem faults. Map APFS volumes to
their shared container; volume totals, free space, purgeable space, local snapshots
and physical capacity are not additive or equivalent.

Start with native storage/disk inventory, scoped `df`/`diskutil` observations and
the affected workload. Attribute space progressively in authorized directories,
not a blanket home/cloud scan. Compare real free space and app scratch/swap/I/O
needs during the failure; large files alone do not prove they caused it.

Treat recurring resets, corruption or disappearing data as preservation/recovery
signals before cleanup or intensive scans. A healthy summary does not exclude
physical faults. First Aid/repair is a mutation, not passive inspection.

Do not delete snapshots, caches, cloud placeholders or unknown app data just
because they appear reclaimable. Establish ownership, sync/retention consequences,
recovery and authority for exact removals or repairs. Verify actual container
headroom and the original workflow afterward; predicted logical deletion size
need not become immediately reclaimable physical space.
