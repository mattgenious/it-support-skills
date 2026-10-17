---
name: verify-reversible-repair
description: Plan and verify a reversible machine repair.
---

# Plan and verify a reversible machine repair.

Trigger: a diagnosis supports a specific machine change.

Name the intended user outcome, exact target and current invariant. Establish
permission and a supported rollback or forward-recovery route before effects.
Preserve user files and working configuration; prefer the smallest coherent change.
Record intent, execute the authorized repair and test the original symptom.
A successful command exit alone does not establish the repair worked.

Report changed state, verification and remaining uncertainty. Roll back only the
owned change when indicated. Lost responses route to recover-uncertain-operation;
repair permission does not imply data deletion, purchases or security weakening.
