---
name: windows-reliability-triage
description: Investigate Windows restarts and failures with bounded native evidence.
---

# Windows Reliability Triage

Use LastBootUpTime, a narrow Get-WinEvent provider/time filter and relevant
installed update or device metadata to build a UTC incident timeline. Distinguish
unexpected-shutdown evidence from the cause of shutdown. Correlate recurring
fault signatures with a plausible mechanism before naming a cause.

For a peripheral, separate absent, intentionally disabled, driver-failed and
hardware-failed states. Do not clear logs or reinstall unrelated drivers. Do not
use registry cleaners or generic driver-updater bundles. Verify a repair against
one concrete reproduction or recurrence window; report what remains untested.
