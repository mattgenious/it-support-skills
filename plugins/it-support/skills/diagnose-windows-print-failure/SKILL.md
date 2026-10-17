---
name: diagnose-windows-print-failure
description: Diagnose a Windows printer or stuck queue while preserving other users jobs, managed drivers and the access path.
---

# Diagnose a Windows print failure

Trigger: missing/offline printer, stuck job, wrong destination, or one app cannot
print. Outcome: locate failure at document/app, client queue, server, transport or
device and verify a harmless print through the original path.

Identify local versus shared/server queue, exact destination and job owner,
connection type, scope, error/time, recent driver/change and whether the printer
can print its built-in status page. Establish authority to send a page; printing
discloses content and consumes supplies. Use harmless content, not customer data.
Distinguish client and print-server observations explicitly.

Start with Settings and printer status display. Read `Get-Printer` for the named
queue, driver and port; use `Get-CimInstance Win32_Printer` if PrintManagement is
unavailable. Check `Get-Service Spooler`; missing cmdlets/access denied are evidence
gaps, not an empty queue or healthy service. Use `Get-PrintJob -PrinterName` only
for the affected queue and `Get-PrinterPort` for its configured transport. Scope
existing PrintService logs to the incident; enabling disabled logs is a change.
Document names, spool content, account/server names and addresses are sensitive.

A printer that cannot print its own status page needs device/consumables/paper
attention before Windows resets. A device that prints locally but not through
its network queue needs port/server/path evidence. Probe only the configured
transport (IPP, SMB, vendor protocol, etc.), not an assumed port 9100 or subnet
scan. Disabled discovery or stale status polling can label a working printer
offline; the label alone does not establish hardware failure. For name/path
issues use [network diagnosis](../diagnose-network-path/SKILL.md).
Compare one known-small document in the original app and another supported app
only with permission, noting rendering differences and exact queue selected.

## A bounded intervention

If one job blocks the queue, identify its owner and exact ID before proposing
cancellation; that loses queued work and may need resubmission. Spooler restart
affects all local queues and can disrupt shared users; disclose scope and obtain
specific permission. Clearing spool directories, removing all printers or replacing
every driver is not a first-line intervention. Preserve managed queues/defaults,
signed vendor-supported drivers and server ownership. Use
[reversible repair](../verify-reversible-repair/SKILL.md) for the
smallest supported change, including reconnect and saved queue configuration.

Verify the permitted page physically emerged at the intended printer, the named
job completed, and other affected users/queues remain available. An empty queue
could mean cancellation, not printing success. Return failure layer, queue/job
evidence, action scope, page result and unresolved driver/device risk.

## Sources

- [Windows printing troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/windows-server/printing/troubleshoot-printing-and-best-practices)
- [PrintManagement](https://learn.microsoft.com/en-us/powershell/module/printmanagement/)
- [Pinned adaptation and license](SOURCE.md)
