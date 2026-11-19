---
name: diagnose-cups-print-job
description: Diagnose a stuck or failed CUPS print job on macOS or Linux without cancelling unrelated work or resetting printing.
---

# Diagnose a CUPS print job

Identify the affected user, queue, exact job and scheduler: local CUPS and a remote
print server can report different states. Protect document titles, user names and
credential-bearing device URIs in evidence.

Use scoped `lpstat` options for jobs, destinations, default, device and scheduler.
Bare `lpstat` is a partial view. A queue can accept jobs while disabled for
processing; distinguish acceptance, held/stopped state, filter/backend failure,
transport and the physical device. Correlate the job's error/time with relevant
CUPS logs and printer status; do not print document content into diagnostics.

Test only an authorized page and configured transport. Preserve other users'
jobs. Cancelling an exact owned job, resuming a queue and restarting a scheduler
have different scopes; establish authority and dependencies before each. Avoid
blanket cancellation, spool-directory deletion, system resets and driver
replacement without evidence and a recovery plan.

Verify the job traverses the intended queue and an actual page emerges correctly.
Backend completion or an empty queue alone is not physical-print acceptance.
