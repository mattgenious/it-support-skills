# IT Support Skills

Open-source, vendor-neutral support guidance for agents working on imperfect
computers. Evidence first. Scoped authority. Recoverable changes. Honest results.
MIT licensed; no support service, remote access server or guaranteed repair.

## Capability index

| OS | Problem type | Skill |
| --- | --- | --- |
| Cross-platform | Triage | [it-support-triage](plugins/it-support/skills/it-support-triage/SKILL.md) |
| Cross-platform | Repair and recovery | [recoverable-repair](plugins/it-support/skills/recoverable-repair/SKILL.md) |
| Windows | Reliability | [windows-reliability-triage](plugins/it-support/skills/windows-reliability-triage/SKILL.md) |
| Windows | Virtualization | [windows-wsl-nested-virtualization](plugins/it-support/skills/windows-wsl-nested-virtualization/SKILL.md) |
| Linux | Performance | [linux-performance-triage](plugins/it-support/skills/linux-performance-triage/SKILL.md) |
| macOS | Performance | [macos-performance-triage](plugins/it-support/skills/macos-performance-triage/SKILL.md) |

Skill directories stay flat for harness discovery; the index supplies OS/type
organization without duplicated content. This initial release contains six
original skills. It does not export any private plugin history or integrations.

## Agent harnesses

- **Copilot CLI:** `/plugin marketplace add mattgenious/it-support-skills`, then
  `/plugin install it-support@it-support-skills`.
- **Claude Code:** `/plugin marketplace add mattgenious/it-support-skills`, then
  `/plugin install it-support@it-support-skills`.
- **Codex:** marketplace metadata is in `.agents/plugins/marketplace.json` and the
  plugin descriptor in `.codex-plugin/plugin.json`. Use your client's supported
  marketplace interface; CLI/version support varies. No remote install claimed.
- **OpenCode:** from a checkout, run `pwsh -File scripts/install-opencode.ps1`.
  Use `-Destination` to select a different skill directory. Existing skills are
  never overwritten; `-WhatIf` previews the operation.
- **Other skill-aware agents:** use `plugins/it-support/skills` as the source.

Only install with the user's authority. Skills guide agents; they do not grant
machine access or approve effects. These manifests are locally validated;
marketplace acceptance and UI loading vary by harness/version and are not
certification by those vendors.

## Contributions

Add original, source-backed guidance to the correct capability owner. Include
trigger, decisive observations, authority boundaries, recovery and verification.
Distinguish observed failures from explanations and known fixes from hypotheses.
Add no credentials, customer records or private infrastructure. For third-party
material, establish license/provenance before incorporating it.

Validate discovery and packaging with `python scripts/validate.py`.
