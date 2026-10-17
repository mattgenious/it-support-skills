---
name: investigate-linux-kernel-crash
description: Investigate Linux panic, oops or lockup using preserved logs or vmcore with exact symbol provenance and sensitive-memory boundaries.
---

# Investigate a Linux kernel crash

Trigger: kernel panic/oops, unexplained reset, soft/hard lockup or existing vmcore.
Outcome: defensible failure classification, evidence gaps and next test/fix owner.
This offline-first specialist path does not authorize crashing a host or installing
a debug toolchain on the affected machine.

## Establish artifact trust

Record incident time/boot, full kernel build, architecture, platform, command
line/config where available, taint, workload trigger and last good version. For
dumps record origin, size, format, checksum, capture/filter method, exact `vmlinux`
GNU build ID and needed module files/build IDs. Matching release text alone is
insufficient. Preserve originals; conversions write new owned files and document
discarded pages. Filtered/truncated regions are unknown, not zero or absent.

vmcores can expose credentials and arbitrary user memory. Use approved local
access-controlled storage, not public uploads/search. Scoped logs, pstore/ramoops
or console evidence can answer classification without full memory. Validate trusted
artifact provenance and analyzer version; parse untrusted dumps in isolation.

## Build a causal rather than final-stack account

Start with chronological logs and earlier watchdog, allocator, hardware/MCE or
I/O warnings. Distinguish faulting task from observer/victim; notification-handler
frames can describe interrupted execution. Separate process OOM from cgroup/system
OOM and deliberate panic-on-OOM policy. Soft lockup, hard lockup and blocked-task
reports describe different progress failures, not interchangeable proof of deadlock
or faulty hardware.

If existing `crash` and matching trusted symbols are available, bounded offline
inspection of `sys`, `log`, `bt` and `mod` can establish build, chronology and module
coverage. Add all-CPU stacks or instruction/object inspection only for a concrete
hypothesis; no donor wrapper is required or shipped. Downgrade claims for mismatched
symbols, absent modules or filtered memory. Retain commands/version and derived
output with the owned evidence.

Rank plausible cause and a competing explanation, supporting evidence and next
discriminating observation. Separate detection site, corruption origin and confirmed
cause. Consult distribution errata/kernel sources with a sanitized signature
(build, class, non-generic frame/subsystem); a matching title is not a verified fix.
External case-study prose is not incorporated.

## Recovery and verification

Live tracing, kdump configuration, sysctl/debug-kernel changes and reboot affect
availability, overhead and storage. Plan exact authority, capture bounds, recovery
and same-session cleanup through
[reversible repair](../verify-reversible-repair/SKILL.md). Deliberate
panic/SysRq crash/kdump tests belong only in explicitly authorized human-controlled
drills with backup, out-of-band access and workload recovery; do not execute or
automate them during diagnosis. Preserve watchdogs and security protections.

Return evidence identity/coverage, earliest anomaly, class, ranked cause, unknowns
and next action. For an approved fix preserve known-good rollback and compare
original workload against changed build/config over a justified window. Without
reproduction or the physical host, a fix remains unverified; upstream claims,
matching stacks and successful boot are insufficient acceptance.

## Sources

- [Kernel bug hunting](https://docs.kernel.org/admin-guide/bug-hunting.html)
- [Kdump](https://docs.kernel.org/admin-guide/kdump/kdump.html)
- [VMCOREINFO](https://docs.kernel.org/admin-guide/kdump/vmcoreinfo.html)
- [Lockup watchdogs](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)
- [Pinned adaptation and license](SOURCE.md)
