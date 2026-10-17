---
name: diagnose-macos-app-permission
description: Distinguish macOS privacy consent, app identity, sandbox, file access and managed policy failures before a targeted permission repair.
---

# Diagnose a Mac application permission failure

Trigger: screen sharing, microphone/camera, Accessibility, automation or protected
file access fails while the device/app otherwise works. Outcome: identify the
requesting app and permission boundary, then verify only the intended capability.

Record OS/app version, exact feature/error/time, interactive account, app location
and bundle identity, and whether the request comes from app, helper, terminal,
browser or remote agent. Consent to one executable/session is not automatically
consent to another. Update, duplicate app, changed signing identity or different
user may explain the result; none alone proves corrupt consent.

Inspect relevant Privacy & Security pane with the user and the app's input/share
settings. Separate TCC privacy consent, sandbox entitlements, ordinary file access,
device selection, application login/license and management restrictions. A greyed
managed control needs its policy owner, not bypass. Use actual installed UI and
supported app instructions where screen/system-audio categories differ by version.
Remote/session limits may require a local test; report that verification boundary.

If logs discriminate the failure, restrict existing Console/unified-log reads to
app and time. Full TCC database reads expose unrelated grants and may need broader
access themselves; do not seek Full Disk Access merely to inventory privacy.
Prefer UI evidence and supported behavior over undocumented database schemas.
Never edit TCC databases, disable SIP or remove profiles to force consent.

## Scoped recovery

Explain capability and requester before user approval; Full Disk Access is broader
than one folder. Preserve unrelated grants. With exact authority, reselect intended
app/capability in supported UI and relaunch only that app after saving work. If
stale consent is supported by evidence, installed-version-supported `tccutil reset`
for one service and verified bundle ID is a fallback: it removes consent and
requires a new user decision, it does not grant access. Global/service-wide resets
are not shortcuts; managed/unsupported services may not reset. Use
[reversible repair](../verify-reversible-repair/SKILL.md), recording
that prior consent may not be automatically restorable.

Verify original action in the same requester/account/session, intended grant only,
and unrelated required access. Do not record private screen/audio content as proof.
Return boundary, requesting identity, consent result, policy owner if blocked and
remaining local-test need.

## Sources

- [Mac Privacy & Security](https://support.apple.com/guide/mac-help/control-what-you-share-mchl2b29231a/27/mac/27)
- [Apple platform security](https://support.apple.com/guide/security/welcome/web)
- [Pinned adaptation and license](SOURCE.md)
