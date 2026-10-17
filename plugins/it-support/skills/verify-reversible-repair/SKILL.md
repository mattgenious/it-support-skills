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

Assess interruption, data, security, management-policy and access risk before
acting. Capture the current state and pre-change behavior, exact supported tool
and rollback. Boot/storage/encryption/firmware actions need backups or recovery
media as appropriate; reconnect and local recovery must remain possible if remote
access drops. A restart needs its own approval and a reachable return path.
Prefer affected-app reinitialization, narrow supported configuration and native
repair/rollback over broad resets or driver/cleanup bundles. Preserve page files,
crash-dump resilience, system animation preferences, protections and management.
Do not expand one repair into unrelated cleanup or recurring automation.

Apply one coherent change; stop on unexpected scope, storage warnings, lost
rollback or unstable access. Preserve failure logs. Verify three things: intended
state plus implicated security/access invariants; original user-visible behavior;
and an appropriate recurrence/stability window. Collector failure is not a pass.
Roll back only the owned change if acceptance fails and rollback is safer than
further experimentation.

If the agent causes a material unintended mutation (data/account damage, required
software removal, wrong-target setting or broken access), stabilize impact first,
preserve evidence and recovery state, then report factual action/current impact
through the owner's authorized incident process. Harmless typos, rejected commands
and existing defects are not unintended state changes. Confirm recording/receipt;
if unavailable, preserve the proposed note in approved storage and state that it
is not recorded. Avoid secrets, transcripts, blame and unsupported causes.

Report change, state/behavior/stability evidence, restart status, uncertainty and
rollback availability. Lost acknowledgements use
[uncertain-operation recovery](../recover-uncertain-operation/SKILL.md), not blind
replay. Repair permission does not imply deletion, purchases or security weakening.

## Sources

- Original maintainer-owned repair and incident-reporting judgment, adapted with
  authorization. Platform-supported repair interfaces and organization-specific
  incident adapters remain the implementation authority.
