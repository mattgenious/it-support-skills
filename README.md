# IT support skills

Vendor-neutral diagnosis and recovery for Windows, Linux and macOS. Skills guide
judgment; they do not grant permission to change machines, accounts or services.

## Find an outcome

Use the OS router for an unclear symptom, or load a task directly. Each task
retains its own consequential safety and evidence limits.

| Scope | Canonical skills |
| --- | --- |
| Shared workflow | [Triage](skills/shared/evidence-led-triage/SKILL.md), [evidence handoff](skills/shared/collect-support-evidence/SKILL.md), [reversible repair](skills/shared/verify-reversible-repair/SKILL.md), [uncertain operation](skills/shared/recover-uncertain-operation/SKILL.md), [backup restore](skills/shared/verify-backup-restore/SKILL.md) |
| Shared diagnostics | [Network path](skills/shared/diagnose-network-path/SKILL.md), [CUPS print job](skills/shared/diagnose-cups-print-job/SKILL.md) |
| [Windows router](skills/windows/SKILL.md) | [Resource bottleneck](skills/windows/performance/identify-resource-bottleneck/SKILL.md), [startup](skills/windows/performance/diagnose-startup-contention/SKILL.md), [application/device failure](skills/windows/reliability/investigate-application-device-failure/SKILL.md), [restart](skills/windows/reliability/investigate-unexpected-restart/SKILL.md), [storage health](skills/windows/storage/assess-storage-health/SKILL.md), [security posture](skills/windows/security/assess-security-posture/SKILL.md), [printing](skills/windows/printing/diagnose-print-failure/SKILL.md), [WSL/KVM](skills/windows/virtualization/diagnose-wsl-kvm/SKILL.md) |
| [Linux router](skills/linux/SKILL.md) | [Resource bottleneck](skills/linux/performance/identify-resource-bottleneck/SKILL.md), [boot/service delay](skills/linux/boot/diagnose-boot-service-delay/SKILL.md), [network performance](skills/linux/network/diagnose-network-performance/SKILL.md), [kernel crash](skills/linux/reliability/investigate-kernel-crash/SKILL.md) |
| [macOS router](skills/macos/SKILL.md) | [Application stall](skills/macos/performance/diagnose-application-stall/SKILL.md), [background contention](skills/macos/performance/diagnose-background-contention/SKILL.md), [memory pressure](skills/macos/performance/diagnose-memory-pressure/SKILL.md), [storage pressure](skills/macos/storage/diagnose-storage-pressure/SKILL.md), [duplicates](skills/macos/storage/review-duplicate-files/SKILL.md), [app permission](skills/macos/access/diagnose-app-permission/SKILL.md), [peripheral disconnect](skills/macos/devices/diagnose-peripheral-disconnect/SKILL.md), [kernel panic](skills/macos/reliability/investigate-kernel-panic/SKILL.md), [sleep/wake continuity](skills/macos/sleep-wake/verify-sleep-wake-continuity/SKILL.md) |

## Install

The `it-support` plugin contains 28 tasks and 3 routers. Canonical skills live in
`skills/`; `plugins/it-support/skills/` is generated flat discovery output, not a
second authoring surface. Skill names and canonical paths are stable in 0.4.1.

For Claude Code or GitHub Copilot CLI, register this repository as a marketplace
and install `it-support@it-support-skills` with the client's native `plugin`
command. Update an existing installation with:

```text
copilot plugin update it-support@it-support-skills
claude plugin update it-support@it-support-skills
```

Inspect the native plugin/skill list and load a changed skill in the actual
client before claiming it is in use. Updating a cache does not reload an already
running session.

The Codex descriptor is `plugins/it-support/.codex-plugin/plugin.json`; the
Agent Plugins descriptor is `plugins/it-support/plugin.json`. Use the client's
supported marketplace/plugin mechanism, not a second hand-maintained skill copy.

OpenCode's initial-copy installer preserves existing same-name directories:

```powershell
pwsh -File scripts/install-opencode.ps1 -WhatIf
pwsh -File scripts/install-opencode.ps1
```

It does not replace existing skills; an existing destination requires its owner's
update/rollback procedure. `-Destination` selects an explicit skill directory.

## Maintain

Edit the canonical task and any task-local assets, then regenerate and check:

```text
python scripts/package_skills.py
python -m unittest discover -s scripts -p test_package_skills.py
python scripts/validate.py
```

Relative skill links are rewritten for flat discovery; task-local assets travel
with their owner. Keep public guidance free of private infrastructure, credentials
and operational records. [AGENTS.md](AGENTS.md) defines placement.

Original material is [MIT](LICENSE). Adapted tasks link their pinned `SOURCE.md`
and exact `LICENSE.upstream`; those notices remain with canonical and generated
copies. Source-level scope and exclusions are recorded there, not a license grant
for an entire upstream repository. Historical adoption/research inventories remain
in Git history rather than the runtime library.
