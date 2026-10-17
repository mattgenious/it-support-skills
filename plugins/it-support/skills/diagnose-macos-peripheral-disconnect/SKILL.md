---
name: diagnose-macos-peripheral-disconnect
description: Isolate Mac USB, Bluetooth, audio or dock failures while preserving input, storage and remote access.
---

# Diagnose a Mac peripheral disconnect

Trigger: input drops, Bluetooth audio glitches, USB/dock device vanishes or the
expected audio input/output is unavailable. Outcome: identify physical, transport,
profile, app or permission scope without losing the working control path.

Record device/connection, Mac model/OS, battery/power, hub/dock/cable topology,
error/time, sleep/wake context and affected apps. Establish alternate input/access
before disconnect or re-pair; the only keyboard, remote link or backup drive is
not disposable. With mounted storage preserve writes and safe eject; corruption
or repeated I/O errors needs [storage diagnosis](../diagnose-macos-storage-pressure/SKILL.md),
not repeated hot-unplug tests.

Begin in Bluetooth, Sound or app device selection. Check input/output, mute,
profile and connection state. Bluetooth output can change quality when an app
activates its microphone; compare that transition before declaring RF/hardware
damage. Camera/mic privacy errors use
[app permissions](../diagnose-macos-app-permission/SKILL.md).

Where needed use scoped `system_profiler` USB/Bluetooth/audio data or System
Information, and existing Console events around the disconnect. Inventories expose
serials, Bluetooth addresses and nearby names; keep implicated entries only.
Permission errors or missing visibility are not absence of hardware. Correlate
power, sleep, cable/hub compatibility and app activity. With permission compare
one variable (known-good port/cable, direct link, app or already-available device);
one comparison does not prove a universal faulty chipset.

Prefer exact selection and supported vendor/OS guidance. Re-pairing loses saved
pairing, Bluetooth service restart affects all devices, and preference deletion is
a broad reset; none is default diagnosis. Driver/firmware/OS updates need
compatibility, backup and scoped authority. Preserve paired input, mounted data,
access, power and management state using
[reversible repair](../verify-reversible-repair/SKILL.md).

Verify original workload through the same connection and a relevant reconnect or
sleep transition only if authorized; confirm input, data and required audio/access
remain available. Return observed scope, comparison, recovery and recurrence or
hardware uncertainty.

## Sources

- [Mac USB problems](https://support.apple.com/guide/mac-help/if-a-usb-device-doesnt-work-with-mac-mchlf779ae93/mac)
- [Bluetooth sound quality](https://support.apple.com/en-us/102217)
- [Pinned adaptation and license](SOURCE.md)
