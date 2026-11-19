---
name: investigate-linux-kernel-crash
description: Investigate Linux panic, oops or lockup using preserved logs or vmcore with exact symbol provenance and sensitive-memory boundaries.
---

# Investigate a Linux kernel crash

Distinguish panic/oops/lockup, OOM, userspace failure and power/reset before
attributing cause. Preserve original kernel logs, pstore/serial evidence, vmcore,
capture metadata and the chronology before reboot/cleanup when safely available.
Memory dumps may contain credentials and third-party data; control access and
share only authorized minimal derivatives.

Match the dump to the exact kernel build/build-ID, configuration, `vmlinux`,
modules and debug symbols. A matching release string alone is insufficient.
Record dump filtering, missing pages, truncated logs, taint and analyzer limits;
missing memory is unknown, not zero or proof an object never existed.

Analyze copies with trusted tools in isolation. Establish the first anomaly and
recurring signature; the last stack or named module may be a victim/observer.
Correlate registers, stacks, logs, object state and known changes against a
falsifiable hypothesis rather than declaring cause from one backtrace.

Do not induce a panic, invoke SysRq crash, reload suspect modules or test kdump on
a live target without an explicitly controlled drill, access recovery and owner
authority. Preserve known-good kernel/boot rollback and original evidence.

Recommend the smallest supported repair or rollback, naming unproven hypotheses.
Verify the original workload on the affected physical/virtual environment and
the relevant recurrence window; a successful boot is recovery, not proof of cure.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
