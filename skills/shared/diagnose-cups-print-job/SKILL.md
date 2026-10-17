---
name: diagnose-cups-print-job
description: Diagnose a stuck or failed CUPS print job on macOS or Linux without cancelling unrelated work or resetting printing.
---

# Diagnose a CUPS print job

Trigger: a macOS/Linux job stalls, a CUPS destination rejects jobs, or one app
cannot print. Outcome: establish job/destination ownership and distinguish app,
queue, scheduler, transport and physical-device failure.

Confirm installed CUPS/client version, local or remote scheduler, queue name,
connection type, owner/job ID, error/time and scope. On macOS begin in Printers &
Scanners; on Linux use the installed printer UI. Ask whether a permitted device
status page works. Printing is an effect, not a read-only probe; use harmless
content with authority and avoid broad job/document metadata collection.

Use installed `lpstat` help/man pages for scoped status reads. `lpstat -p` reports
printer state, `lpstat -a` acceptance, `lpstat -v` device URI and `lpstat -o` jobs;
supply the affected destination where supported. Output can expose usernames,
document names or URI credentials. Acceptance and enabled state differ: a queue
can accept work without processing it. Bare `lpstat` generally reports the current
user's active jobs, not proof all queues are empty. Client queries to a remote
scheduler describe that scheduler, not necessarily a local daemon.

Inspect existing scheduler/backend errors in the same window with minimal scope.
Logs may be restricted, unavailable or rotated; do not enable debug logging or
collect spool content automatically. Compare configured URI/protocol, endpoint
reachability and device readiness; route name/TLS/transport failures to
[network diagnosis](../diagnose-network-path/SKILL.md). Backend completion need
not prove paper output; an offline label need not prove failed hardware.

If evidence supports it, propose one owned job cancellation or supported queue
resume, disclosing lost-work/disruption consequences. Verify installed semantics
and exact job/destination first; bare `cancel`, `cancel -a` and job-data removal
can affect unintended work. System-wide printing reset, scheduler restart, queue
deletion and driver replacement require separate scoped authority and saved
configuration/reconnect recovery through
[reversible repair](../verify-reversible-repair/SKILL.md).

Acceptance is a permitted page at the intended device, original app success,
queue progression and preservation of unrelated jobs. Return observed layer,
owner/ID, action, physical result and gaps without sharing document names.

## Sources

- [CUPS lpstat manual](https://openprinting.github.io/cups/doc/man-lpstat.html)
- [CUPS cancel manual](https://openprinting.github.io/cups/doc/man-cancel.html)
- [Mac printing problems](https://support.apple.com/guide/mac-help/solve-printing-problems-mh14002/mac)

Original guidance informed by documented command behavior; no CUPS manual text or
implementation is incorporated. Upstream manuals retain their own license.
