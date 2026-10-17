---
name: diagnose-macos-storage-pressure
description: Distinguish Mac APFS capacity pressure, swap or scratch contention and storage faults before cleanup or repair.
---

# Diagnose macOS storage pressure

Trigger: low-space warnings, failed updates, slow scratch/swap I/O or storage-bound
apps. Confirm disk/container/volume, symptom, backup and requested scope.

Use System Settings Storage, Disk Utility and bounded df/iostat observations.
Distinguish APFS shared container space from per-volume figures, usable free space
from purgeable space, snapshots/Time Machine retention from disposable files, and
capacity from I/O contention. Correlate swap, caches, app scratch, indexing,
sync/backup and update activity. SMART status where supported is partial evidence;
missing status or a passing bit does not prove physical health.

If disconnects, corruption, repeated errors or severe degradation suggest failing
media, prioritize authorized backup/data recovery and minimize stress/writes.
Capacity cleanup is not hardware repair. Disk Utility First Aid is a repair action,
not merely inspection; obtain exact authorization, backup and interruption/recovery
plan before running it, especially on a startup volume.

For space attribution, start with the implicated container and user-selected
folders, then progressively inspect large consumers rather than hashing or walking
the whole home directory. Report permission, cloud-placeholder and mount exclusions;
apparent file size, allocated bytes and APFS shared extents can differ. Candidate
duplicate analysis belongs to [duplicate review](../review-macos-duplicate-files/SKILL.md),
not this capacity assessment.

Prefer supported storage management and owner-selected relocation/removal over
blind deletion. Snapshots, local Time Machine data, caches and application support
can retain rollback, backups, licensing or state; purgeable space is OS-managed.
Do not erase/repartition, delete snapshots or user content without specific approval.
Use [reversible repair](../verify-reversible-repair/SKILL.md), noting
that deletion may have no rollback without backup.

Verify usable space in the same container, the originally failing update/workload
and backup/recovery availability. Report changed capacity, latency, collector gaps
and unresolved media risk separately.

## Sources

- [Disk Utility](https://support.apple.com/guide/disk-utility/welcome/mac)
- [Free storage on Mac](https://support.apple.com/en-us/102624)
