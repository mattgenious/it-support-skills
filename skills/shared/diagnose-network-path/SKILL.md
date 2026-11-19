---
name: diagnose-network-path
description: Isolate DNS, routing, TCP, TLS, proxy and application connectivity failures across Windows, macOS and Linux.
---

# Diagnose a network path

Use the failing application's exact hostname, port, time/error, network/VPN and
proxy context. Probe only an authorized target; do not silently substitute a
public endpoint. Preserve working access and do not disable certificate checks,
VPN, firewall or endpoint protection to declare success.

Separate the failing layer:

| Layer | Discriminating evidence |
| --- | --- |
| Name resolution | Compare the system/application resolver with authoritative expectations. `dig`/`nslookup`, DoH and browser caches can bypass system split-DNS, search domains or policy; their success does not prove the app resolves correctly. |
| Route/address family | Check selected interface, route, VPN/split tunnel and IPv4/IPv6 paths. ICMP filtering or an intermediate traceroute timeout does not establish endpoint loss. |
| TCP | Test the configured port from the affected context. Refusal, timeout and successful connect imply different boundaries, not a cause by themselves. |
| TLS/proxy | Check clock, hostname/SNI, trust chain, interception and application proxy. Windows WinHTTP proxy is not every application's proxy. Preserve certificate validation. |
| Application | Compare status, redirect/auth behavior and real request with bounded timing. A successful HEAD can differ from GET; redirects may change host and trust/authorization scope. |

Native starting points: Windows `Resolve-DnsName`, `Get-NetRoute`,
`Test-NetConnection` and scoped proxy inspection; Linux `resolvectl` where present,
`getent`, `ip route` and `ss`; macOS `scutil --dns`, `route -n get` and scoped
proxy/network inspection. Commands differ by installed version and permissions.

For authorized `curl` timing, name lookup/connect/TLS/start-transfer/total are
cumulative milestones, not independent durations. Compare meaningful differences
and repeated bounded samples; reused connections and redirects affect attribution.
Avoid exposing headers, credentials, query tokens or captured payloads.

Change one justified owner-controlled setting, then repeat the original app
workflow on the intended network. For Linux throughput/queue contention use
[network performance](../../linux/network/diagnose-network-performance/SKILL.md);
working DNS alone is not network acceptance.

[Adaptation provenance](SOURCE.md) and [upstream notice](LICENSE.upstream).
