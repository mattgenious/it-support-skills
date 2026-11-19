---
name: diagnose-windows-print-failure
description: Diagnose a Windows printer or stuck queue while preserving other users jobs, managed drivers and the access path.
---

# Diagnose Windows print failure

Identify the user, queue, exact job and path: application/client, print server,
configured port/transport and physical printer. Keep document titles, user names
and private addresses out of unnecessary evidence.

Use scoped `Get-Printer`, `Get-PrintJob`, `Get-PrinterPort` and spooler/service
observations where available; correlate the affected job with PrintService and
device evidence. Distinguish offline/paused queue, held job, driver/rendering
failure, authentication, transport and paper/device errors. A service running
does not prove a healthy print path.

Check the configured protocol/endpoint rather than assuming raw TCP 9100.
Use only an authorized test page; first separate one application's failure from
all applications or users.

Cancel only the exact authorized job. Restarting a shared spooler, clearing spool
files, removing a printer/driver or resetting printing affects other jobs/users
and requires explicit scope and recovery. Preserve managed drivers, dependencies
and remote access; do not run a broad reset as diagnosis.

Verify the user's application prints through the intended queue and the physical
page is correct. An empty queue or successful API result alone is not acceptance.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
