---
name: diagnose-macos-app-permission
description: Distinguish macOS privacy consent, app identity, sandbox, file access and managed policy failures before a targeted permission repair.
---

# Diagnose a macOS app permission

Identify the denied operation and actual requester: app, helper, terminal/host,
account and macOS/build. Record executable/bundle/signing identity and launch
context; consent granted to one identity does not automatically cover another.

Separate TCC/privacy consent, sandbox entitlement, filesystem ACL/ownership,
login/session and managed policy. Inspect only relevant settings and scoped
errors/logs; permission to diagnose does not authorize revealing private content.
An absent prompt is not proof of denial, and a successful terminal test may use a
different requester than the failing app.

Prefer the correct app's native settings/consent flow and required targeted
relaunch. Have the user make privacy/management decisions. `tccutil reset` revokes
consent and may require fresh interaction; it does not grant access or guarantee
an automatically restorable before-state. Bound any reset to the actual service
and identity with authority.

Preserve signing, management profiles and system protections. Do not edit the
TCC database, disable SIP, remove policy or broadly reset permissions. Verify
the original action from the original requester/session, and distinguish a
managed restriction from a fault that can be repaired locally.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
