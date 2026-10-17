---
name: verify-macos-sleep-wake-continuity
description: Verify actual macOS sleep and wake continuity.
---

# Verify actual macOS sleep and wake continuity.

Trigger: a support session or workload must survive real system sleep/wake.

Capture baseline boot identity, relevant executor and approval state. Use a genuine
user-authorized sleep action; confirm OS sleep/wake events and state transitions.
A frozen remote display or paused VM is not proof of system sleep. Inspect sleep
preventers read-only if the requested transition did not occur.

After wake, verify original task identity, usable access and local stop controls
without replacement approval. Then verify explicit End closes access. Preserve
power, display, login and system-motion preferences; use no settings changes to
make acceptance pass. Report fixture blockers separately from product failures.
