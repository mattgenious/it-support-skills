---
name: assess-windows-security-posture
description: Assess Windows protection, update, firewall, encryption and platform posture against actual policy, with scoped evidence.
---

# Assess Windows security posture

Confirm the device, security question, collection window and personal/organization
management owner. Assess controls and material exceptions, not a universal registry
score. Possible active compromise requires evidence preservation and explicit
containment authority before changes; this assessment is not incident eradication.

## Evidence and interpretation

Use only checks relevant to the question, with timestamp and permission/edition
limitations. Examples: Get-MpComputerStatus or registered antivirus status,
Get-NetFirewallProfile, Get-BitLockerVolume (no recovery keys),
Confirm-SecureBootUEFI, Get-Tpm, Get-CimInstance Win32_DeviceGuard,
Get-HotFix and narrowly filtered Get-WinEvent. Update history and supported build
matter: Get-HotFix alone is not complete patch compliance. Unsupported commands or
access denial are unknowns, not control failures.

Report separately: supported build/update state; antivirus health/freshness;
firewall profiles/material exceptions; encryption coverage/protection state;
Secure Boot, TPM and virtualization-based protections; relevant privileged account
or listening-service exposure; security failures in the incident window; policy
source/conflicts. Gather process, DNS/proxy, driver or network evidence only when
it discriminates the stated concern. A setting can be intentional managed policy.

Compare with the owner's actual policy. Without one, describe deviations from
supported defaults, not certification or compliance failure. Avoid opaque registry
baselines and generic warning lists. Rank material exposure, observed posture,
policy-dependent findings and unknowns with evidence/confidence.

## Authority and verification

Assessment does not authorize disabling protection, removing management or changing
accounts. Never retrieve secrets, recovery keys, tokens, cookies or unrelated
personal data. Preserve antivirus/firewall, encryption, Secure Boot, UAC,
credential/application protections, updates and monitoring during other repairs.
Use [reversible repair](../../../shared/verify-reversible-repair/SKILL.md) for an
exact owner-approved correction, recording risk and rollback. Re-check only the
affected control and intended behavior, plus implicated access/protection invariants.
State unresolved exposure and policy decisions calmly.

## Sources

- [Get-MpComputerStatus](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpcomputerstatus)
- [Get-NetFirewallProfile](https://learn.microsoft.com/en-us/powershell/module/netsecurity/get-netfirewallprofile)
- [Get-BitLockerVolume](https://learn.microsoft.com/en-us/powershell/module/bitlocker/get-bitlockervolume)
- [Windows security](https://learn.microsoft.com/en-us/windows/security/)
