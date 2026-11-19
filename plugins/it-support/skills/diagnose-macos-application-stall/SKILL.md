---
name: diagnose-macos-application-stall
description: Diagnose an application stall on macOS.
---

# Diagnose a macOS application stall

Protect unsaved work. Establish app/build, macOS/architecture, failing action,
duration and whether other apps still respond. Separate slow progress from a
hang, blocked UI from background work, and one app from whole-system pressure.

Correlate Activity Monitor CPU/memory/disk/network with a bounded sample or
spindump when justified; protect document paths and memory contents. High CPU can
be progress, low CPU a wait; neither alone identifies cause. Check pressure,
external dependencies and relevant app errors before force quitting.

Prefer an app-native cancel/save or supported recovery. A force quit loses work
and requires appropriate authority; restarting the Mac is not a substitute for
isolating an app failure. Verify the same operation and recovery of required
documents after a targeted change. VM evidence does not establish physical Mac
graphics, thermal or peripheral behavior.
