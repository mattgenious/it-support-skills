---
name: diagnose-macos-peripheral-disconnect
description: Isolate Mac USB, Bluetooth, audio or dock failures while preserving input, storage and remote access.
---

# Diagnose a Mac peripheral disconnect

Identify device, transport, hub/dock/power/cable path, macOS/build and whether
only one app or the whole system loses it. Preserve an alternate keyboard,
pointer, display/network or remote-access path before interrupting the active one.
Safely unmount storage and stop its writes before disconnecting.

Correlate scoped USB/Thunderbolt/Bluetooth/audio inventory and relevant logs with
the failure time. Protect serial numbers, addresses and nearby-device identities.
Distinguish enumeration, power/bandwidth, pairing/connection, audio routing/profile
and app permission. Bluetooth microphone activation can switch audio profile and
quality; that is not by itself a failing speaker.

Compare one known-good cable/port/device or bypassed hub when safe and authorized.
Record exactly which change discriminates the cause; broad resets confound the
result. Do not delete all pairings, restart shared daemons or reset system
controllers as a first step.

Use a bounded reversible repair with required-device/access recovery, then repeat
the original workload and reconnect/sleep condition that failed. Verify the real
peripheral, not merely its appearance in inventory.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
