---
name: collect-support-evidence
description: Prepare an authorized minimal diagnostic handoff with integrity, provenance, partial-result warnings and retention boundaries.
---

# Prepare a support evidence handoff

Trigger: another technician needs bounded evidence to answer a specific diagnostic
question. This is an artifact handoff, not a forensic image or continuous telemetry.

## Scope and collect

Confirm target, recipient, purpose, symptom window, permitted fields and destination.
Explain sensitivity and choose the smallest useful evidence groups; a named profile
must resolve to an explicit accepted scope. Connection/access alone does not approve
collection, recurring diagnostics or uploads. Use the task's native collector or
approved organizational adapter; discover its supported interface rather than
inventing flags. Verify tool publisher/hash/provenance before acquired executables
run, and keep collection one-shot unless a bounded trace is specifically authorized.

Record target identity, tool/version, schema/format, collection and event timestamps,
requested and completed fields, failed collectors and warnings. Preserve useful
partial results; missing evidence is not a healthy result. Confirm collection,
transfer and download status separately. Failed transfer is not a delivered bundle.

## Validate and transfer

Inspect authorized fields for secrets, recovery keys, tokens, browser data, unrelated
documents, file contents and command transcripts; omit them unless specifically
needed and authorized. Use filename, size and SHA-256 for final integrity, verifying
an adapter's transfer hash where provided. A hash detects byte changes, not truth,
identity or completeness. Validate schema/version where a collector defines one.

Keep originals only in approved protected storage. Redaction creates a named
derivative with removed field classes documented and its own hash; do not silently
rewrite an original. Send only through the authorized destination, not an ad hoc
public service or full-data chat paste. Include the question to answer, coverage,
uncertainty, sensitivity/recipient, provenance, integrity and retention expectation.

## Verify and clean up

Confirm the recipient can obtain the intended artifact and distinguish verified
receipt from pending transfer. Stop owned collectors and remove only authorized,
owned local/remote staging artifacts after consumers release them; preserve source
logs, credentials/authentication and unrelated files. Report exact residue and safe
cleanup if cleanup fails. Interpretation returns to
[evidence-led triage](../evidence-led-triage/SKILL.md); repair is separately approved.

## Provenance

Original maintainer-owned support guidance, adapted with authorization. This task
specifies a generic evidence contract; collection/transport commands and product
schemas belong to the deployment's separately maintained adapter, not this library.
