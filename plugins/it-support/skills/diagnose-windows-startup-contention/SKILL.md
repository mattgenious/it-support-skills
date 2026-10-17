---
name: diagnose-windows-startup-contention
description: Diagnose slow Windows sign-in or recurring startup load and select a reversible, dependency-aware change.
---

# Diagnose Windows startup contention

Trigger: sign-in is slow or the desktop remains busy after login. Define whether
boot, authentication, shell readiness or an app's usable state is delayed. Record
hardware, baseline elapsed time, recent changes and whether this is first boot
after servicing. Preserve access, work and startup configuration.

## Distinguish the cause

Task Manager Startup impact is a lead, not proof. Correlate process trees and CPU,
memory and disk activity during the affected interval in Task Manager/Resource
Monitor. Enumerate only implicated startup apps, services, scheduled tasks, shell
extensions and app self-start mechanisms. Autoruns from Microsoft's distribution
can expose hidden entry points; record publisher, path, trigger and owner before
judging an entry. Security, backup and management components may be required.

Finite updates, indexing, cloud sync and security scans differ from repeated
unnecessary startup work. Prefer completion, scheduling or scope changes over
removal. If the owner remains unclear or boot dependencies dominate, take a bounded
Windows Performance Recorder boot trace and analyze with Windows Performance
Analyzer under trace/privacy authority rather than disabling a list of services.

## Change and verify

With exact user and policy-owner approval, disable one nonessential app's supported
autostart setting, recording how to restore it. Never disable security, updates,
backup, accessibility or remote access to make login look fast. Preserve system
animation/display preferences. Reboot/sign-out needs separate interruption
approval and a reachable recovery path. Use [reversible repair](../verify-reversible-repair/SKILL.md).

Compare the same boot/login conditions and user-ready milestone, not just a startup
impact label. Confirm the app still works on demand and security/access/backup
remain intact. Distinguish warm-cache and post-update differences from a durable
improvement; restore the owned setting if behavior regresses.

## Sources

- [Autoruns](https://learn.microsoft.com/en-us/sysinternals/downloads/autoruns)
- [Windows Performance Toolkit](https://learn.microsoft.com/en-us/windows-hardware/test/wpt/)
