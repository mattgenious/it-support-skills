---
name: evidence-led-triage
description: Diagnose a support symptom using scoped evidence.
---

# Diagnose a support symptom using scoped evidence.

Establish the authorized target, symptom, onset and desired outcome. Use the
smallest read-only observation that distinguishes plausible causes. Separate
application failure, OS failure, transport failure and missing evidence.

Record target identity, tool/version, timestamps and collector status. A failed
collector is not a healthy machine. Prefer native supported diagnostics over a
new agent, background watcher or broad machine dump. Avoid reading unrelated
files, command history, credentials or customer communications.

Distinguish immediate data-loss, heat, protection or resource-exhaustion risk from
ordinary slowness before choosing the next check. Record frequency, affected
workload and recent changes; normalize event and collection timezones. Preserve
usable partial observations with their warnings. Access alone does not authorize
a scheduled collector, recurring diagnostics or broader security/network reads.

For Windows, use focused Get-CimInstance, Get-Process, Get-Counter, Get-Volume or
bounded Get-WinEvent fields as the question requires; route present-device status
and problem codes to [application/device investigation](../investigate-windows-application-device-failure/SKILL.md).
Use the [Windows router](../route-windows-support/SKILL.md),
[Mac router](../route-macos-support/SKILL.md) or [Linux router](../route-linux-support/SKILL.md) to
select the symptom owner. Do not manufacture a diagnosis from one utilization
sample, alert or time coincidence.

Present decisive facts, ranked explanations with supporting/conflicting evidence,
unknowns and one discriminating next action. Move to
[repair](../verify-reversible-repair/SKILL.md) only within exact authorization;
route storage risk to preservation before corrective writes. Use
[evidence handoff](../collect-support-evidence/SKILL.md) when another
technician needs a scoped artifact. Verify the next observation answers the
question, and state what the sample cannot establish.

## Sources

- [Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent)
- Original maintainer-owned support guidance, adapted with authorization; no
  third-party text or private collection adapter is included.
