---
name: diagnose-linux-network-performance
description: Separate Linux application or DNS latency, socket queues, retransmissions and interface/path contention with bounded evidence.
---

# Diagnose Linux network performance

Define the affected flow, namespace/container, direction, expected throughput or
latency and exact slow interval. Use [network path](../diagnose-network-path/SKILL.md)
first when DNS/TCP/TLS/proxy reachability is uncertain; a healthy link does not
establish a healthy remote service.

Compare bounded deltas from `ip -s link`, scoped `ss` socket state/queues and
available TCP statistics with the application's timings. Lifetime retransmission
or drop counters without an interval are not the current loss rate. Distinguish
send/receive queue pressure, retransmissions, listener backlog and remote delay.

Correlate host/container CPU, softirq, steal, memory, storage and cgroup limits;
network-shaped stalls can originate outside the NIC. Confirm route/interface,
MTU and negotiated link context rather than treating nominal link speed as
achieved throughput.

Prefer existing workload observations. Active throughput tests can saturate
shared links; packet capture can expose payload/credentials. Both need justified
scope, duration, destination and authority. Do not apply universal sysctl,
offload, MTU or firewall changes. Verify one evidence-supported reversible change
against the same flow and interval, including impact on other consumers.
