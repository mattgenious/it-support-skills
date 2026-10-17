---
name: verify-backup-restore
description: Recover selected files or validate a backup by staging and checking restored data before any production replacement.
---

# Verify a backup restore

Trigger: recover lost files, check backup usability, or restore prior application
state. Outcome: evidence the selected recovery point restores usable data, keeping
live state intact until separately authorized promotion. A successful backup job
or archive listing is not proof of recovery.

Confirm data owner, exact files/app/database, requested time and acceptable loss,
backup identity/timezone, encryption/key availability, restore tool/version,
capacity and retention. Keys stay in approved credential interfaces, not chat,
command arguments, logs or repositories. Use the existing backup system's supported
restore procedure; this does not set up a provider or grant access to others' data.

Inspect catalog/manifest and relevant health history without pruning, repairing
or changing the backup repository. Record immutable snapshot/version, scope,
exclusions and consistency method. Copying an active database may be unusable
without application-aware backup or transaction logs. Suspected corruption,
ransomware or failing media needs evidence preservation and an isolated recovery
environment before mounting or executing restored content.

## Restore without replacing live data

Choose a new approved destination with sufficient capacity and no overlapping
source/live paths, symlink/reparse redirection, cloud sync, production mounts or
app watchers. Restore only requested scope; preserve backup and current files.
Even staging writes/test-service startup need authority. Databases use compatible
isolated tooling with outbound integrations disabled; do not activate recovered
mailers, schedulers or automation against production credentials.

Check manifest completeness, counts/sizes, known hashes where available,
permissions/ownership, timestamps and required extended metadata. Hash agreement
establishes byte equality with its reference, not application consistency or
malware absence. Open representative permitted files in a safe viewer; for databases
check documented integrity, schema, sample records and app relationships, not row
count alone. Record omissions, unreadable files, incompatibility, elapsed time and
actual recovery point. A partial restore can meet a narrow need; disclose exclusions.

## Promotion is a separate decision

Show overwritten targets, downtime, new data lost since snapshot, current-state
preservation, recovery path and acceptance before replacement. Obtain specific
permission for live promotion; a drill ends in staging. Prefer recovered files
alongside current files when sufficient. Use
[reversible repair](../verify-reversible-repair/SKILL.md); disclose when rollback
cannot preserve intervening writes before effects.

After promotion verify original files/workflow, access controls, app consistency
and ongoing backup availability. Remove only owned staging after final consumers
release it under agreed retention; retain sensitive recovered data in approved
storage until then. Return recovery point, verified scope/function, loss/downtime,
untouched live state or exact promotion, and restoration gaps. Do not implicitly
schedule recurring drills.

## Sources

- [restic restore](https://restic.readthedocs.io/en/stable/050_restore.html)
- [Time Machine recovery](https://support.apple.com/guide/mac-help/restore-items-backed-up-with-time-machine-mh11422/mac)
- [Pinned adaptation and license](SOURCE.md)
