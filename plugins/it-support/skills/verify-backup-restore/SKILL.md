---
name: verify-backup-restore
description: Recover selected files or validate a backup by staging and checking restored data before any production replacement.
---

# Verify a backup restore

Confirm the requested data/application, exact recovery point/timezone, consistency
needs, encryption-key availability and authorized destination. A successful backup
job or file listing does not establish usable recovery. Record unavailable,
excluded or stale content and the acceptable loss window.
Use the backup owner's supported restore path without changing/pruning the backup
repository. Suspected ransomware/corruption needs isolation before opening content.

Restore into a new isolated destination, not over live data. Resolve links,
mounts, sync roots, watchers and integrations before writing; prevent a restored
application from sending, executing jobs or using live credentials. Preserve
originals and current writes. Availability of a key does not authorize exposing it.

Check representative critical files by content/hash as appropriate, permissions,
ownership and required metadata; open the actual file format or application in
isolation. For databases, verify application-consistent recovery rather than only
archive extraction. Report tested and untested scope, corruption and missing
dependencies explicitly.

Promotion is a separate consequential action: establish authority, current-state
backup, intervening-write loss, downtime and rollback before replacing production.
Verify the user's workflow after promotion; retain or remove staging/backups only
under their retention policy.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
