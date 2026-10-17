---
name: review-macos-duplicate-files
description: Identify verified duplicate-file candidates without treating logical duplicate bytes as reclaimable APFS space.
---

# Review Mac duplicate-file candidates

Trigger: find duplicates before reclaiming storage. Outcome: scoped, trustworthy
candidates and a retention decision, not deletion by filename/apparent size.
General capacity investigation belongs to
[storage pressure](../diagnose-macos-storage-pressure/SKILL.md).

Agree exact folders, exclusions, evidence destination and whether online-only
files may download. Prefer an existing trusted read-only tool; inspect its version
and scan behavior first. Do not install donor tooling implicitly. Protect media
libraries, app bundles, backup repositories, system folders and synchronized/shared
data from generic removal. Skip symlink traversal; report denied, offline, sparse
or changing files as coverage gaps. An unreadable tree is not a clean tree; avoid
full-home hashing by default.

Use size grouping, bounded partial hashing to narrow candidates, then full-content
hashes for remaining stable files. Partial hash or filename alone is insufficient.
Record algorithm, paths and size/mtime before and after reads; changed files need
re-evaluation. Before removal recheck retained and candidate content (or byte
comparison for stronger assurance), metadata, ownership and app relationships.
Identical bytes can have different ACLs, extended attributes or intended uses.
Hard links share a file, APFS clones share extents and cloud stubs may not occupy
their apparent size: duplicate logical bytes do not guarantee physical savings.

The user selects the retained instance. Explain sync propagation, references,
backup retention and metadata differences. Use app-level consolidation for managed
libraries. With specific authority choose recoverable approved quarantine/move,
preserving paths and avoiding collisions. Moving can propagate through sync;
Trash is not durable backup and cross-volume movement can alter metadata or use
space. Use [reversible repair](../verify-reversible-repair/SKILL.md);
deletion/emptying Trash needs its own approval and verified recovery.

Verify retained content/app use, actual same-container free space and restore path.
Return scope, full comparison evidence, exclusions, chosen action, physical savings
and uncertainty separately. Finding duplicates is an observation, not failure or
an instruction to delete.

## Sources

- [APFS shared space](https://support.apple.com/guide/disk-utility/add-delete-or-erase-apfs-volumes-dskua9e6a110/mac)
- [Pinned adaptation and license](SOURCE.md)
