---
name: verify-reversible-repair
description: Plan and verify a reversible machine repair.
---

# Verify a reversible repair

Define the user-visible outcome, target/owner, allowed change and invariants.
Check authority, dependencies, unsaved work, backups/recovery and how access will
survive interruption. Save the relevant before-state; a nominal undo command is
not recovery if credentials, networking or the only input device disappear.

Choose one coherent, evidence-supported change with a usable rollback. Explain
necessary service/reboot interruption and cross-user impact before acting.
Preserve security, update management, crash evidence, pagefile policy and OS
animation/reduced-motion preferences; do not trade them away for a generic score.

Compare both configuration and the original workflow afterward, including the
relevant recurrence window. Command success is not symptom resolution. Revert
only the owned change when acceptance fails and rollback is safer. Stop on lost
recovery, storage warnings or unstable access; record residual risk and untested scope.
For a material unintended mutation, stabilize impact, preserve evidence and
disclose it through the owning reporting path; confirm receipt or state that it
remains unrecorded. [Reconcile uncertain effects](../recover-uncertain-operation/SKILL.md)
before replaying them.
