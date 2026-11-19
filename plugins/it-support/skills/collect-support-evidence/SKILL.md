---
name: collect-support-evidence
description: Prepare an authorized minimal diagnostic handoff with integrity, provenance, partial-result warnings and retention boundaries.
---

# Collect support evidence

Agree on target/time window, recipient, authorized categories, sensitive exclusions
and retention. Minimize collection: logs can expose identities, paths, document
names, tokens and memory. Access permission is not permission to send them.

Use the maintained collector for one-shot collection unless a bounded trace is
authorized; verify acquired executable provenance before running it. Preserve its version, target identity, timestamps,
scope, warnings, failures and partial coverage. Success status is not proof every
category was collected. Validate the output schema and final artifact integrity;
hash the final bytes after packaging. A hash proves byte agreement, not truth or
completeness. Keep originals intact in approved protected storage; redact into a clearly
identified derivative with its own hash and limits.

Treat collection, transfer and recipient receipt as separate outcomes. Use the
approved protected channel, confirm the intended recipient can open and interpret
the artifact, and give the minimal reproduction and coverage gaps. Reconcile an
uncertain upload before retrying. Clean only authorized, owned staging after its
consumer has released it; preserve required originals and recovery records.
Stop owned collectors and report any cleanup residue.
