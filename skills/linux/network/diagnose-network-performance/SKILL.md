---
name: diagnose-linux-network-performance
description: Separate Linux application or DNS latency, socket queues, retransmissions and interface/path contention with bounded evidence.
---

# Diagnose Linux network performance

Trigger: a Linux workload has slow responses, poor throughput or intermittent
network stalls. Identify the authorized endpoint/path, interface, workload,
latency/throughput baseline and time window, including container/namespace context.
Do not turn a performance request into network scanning.

Compare application timing with DNS lookup and connection latency. Use bounded ss,
ip -s link, nstat and ethtool read-only statistics where available to distinguish
socket queues, retransmissions, link errors and drops. tc inspection can identify
queueing/shaping; changes are separate actions. Correlate CPU/softirq, storage waits,
virtualization steal, cgroup limits and noisy neighbors with
[resource diagnosis](../../performance/identify-resource-bottleneck/SKILL.md).
Cumulative counters need deltas and workload timing; old errors or one timeout do
not locate a fault. A healthy local link cannot clear the remote service/path.

Choose one discriminating next check rather than a sysctl recipe. Prefer app
concurrency/batching/configuration or a demonstrated endpoint/path correction.
Offload, congestion-control, queue, firewall and namespace settings are scoped
contracts, not universal speed switches. Packet capture requires separate sensitive
data authority, interface/filter/duration and retention; stop it after the window.
Tools and privileges vary by distro; absence is a coverage gap, not permission to
install or loosen kernel/security policy.

Changes require exact owner approval, captured configuration, management-aware
rollback and recovery if access drops. Preserve firewall, mandatory access controls,
mitigations, auditing and updates. Use
[reversible repair](../../../shared/verify-reversible-repair/SKILL.md).
Verify the same endpoint/workload's latency, throughput and errors plus continued
access; report local evidence, unresolved path assumptions and collector overhead.

## Sources

- [Linux kernel administration](https://docs.kernel.org/admin-guide/index.html)
- Local distribution manuals for ss, ip, nstat, ethtool and tc (match installed version).
