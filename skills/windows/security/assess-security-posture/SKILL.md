---
name: assess-windows-security-posture
description: Assess Windows protection, update, firewall, encryption and platform posture against actual policy, with scoped evidence.
---

# Assess Windows security posture

Agree on the device, actual organizational policy and assessment scope. Start
read-only; assessment is not permission to change protections, enroll a device,
perform incident eradication or expose recovery keys.

Inspect supported native status for:

- Active endpoint-protection provider, health, signatures and real-time controls;
  another managed provider can legitimately replace Defender.
- Servicing/update state, pending restart and supported OS/build. `Get-HotFix`
  alone is not a complete update inventory.
- Firewall profiles/rules in the actual network context, management ownership,
  encryption coverage/protection state, Secure Boot and TPM where applicable.

Separate observed compliant, noncompliant and unknown/unavailable results.
Unsupported cmdlets, permission denial and stale inventory do not prove disabled
protection. A generic score is not policy, and a healthy posture check does not
prove absence of compromise.

Report consequential gaps with exact bounded evidence and the responsible owner.
For authorized remediation preserve recovery/access and management policy, save
before-state and verify effective protection afterward; do not disable security
to improve compatibility or a benchmark.
