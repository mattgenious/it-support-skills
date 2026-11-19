---
name: review-macos-duplicate-files
description: Identify verified duplicate-file candidates without treating logical duplicate bytes as reclaimable APFS space.
---

# Review Mac duplicate files

Agree on authorized roots, exclusions and the intended result. Discovery is not
deletion authority. Preserve application bundles/libraries, backups, cloud/sync
state, recovery material and private content outside scope.

Group candidates by size, compare partial content to reduce work, then full stable
content/hash before declaring duplicates. Recheck size/mtime/identity before any
action; files can change during scanning. A filename or partial hash is not proof.
Equal data can have different ownership, metadata/resource forks, roles or required
locations; content equality does not choose which copy is disposable.

Distinguish hard links, APFS clones and cloud placeholders. Logical duplicate bytes
are not a reliable estimate of physical space recoverable; reading placeholders
can download data and consume storage/network.

Present exact verified candidates and intended keeper with those limits. For
authorized cleanup use a recoverable, owned destination and account for sync
propagation, active consumers, metadata and retention; Trash/quarantine is not
automatically harmless. Revalidate before moving, then verify the keeper, original
workflows and actual free space. Retain recovery until its owner releases it.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
