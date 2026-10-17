---
name: diagnose-network-path
description: Isolate DNS, routing, TCP, TLS, proxy and application connectivity failures across Windows, macOS and Linux.
---

# Diagnose a failed network path

Trigger: a site, application, VPN resource, printer endpoint or remote service is
unreachable or intermittently fails. Outcome: identify the failing layer and a
bounded next action without sacrificing required access or certificate trust.

Record exact error, time/timezone, affected application and destination
(host/protocol/port, stripping credentials and URL query secrets), OS, interface,
VPN/proxy requirement, and whether one app, user, device or site fails. Use an
existing authorized destination; diagnosis does not authorize scanning, public
speed tests, packet capture or bypassing a required network path.

## Choose a discriminating observation

| Observation | What it separates |
| --- | --- |
| Link, address and selected route | Disconnection, DHCP/configuration, wrong interface or route |
| Configured resolver and target A/AAAA answers | Lookup versus transport; split DNS and app-specific DoH |
| Bounded connection to the target's actual port | TCP reachability versus ICMP policy; ping timeout alone proves little |
| TLS error, clock, hostname and chain | Expiry/name/trust failures versus routing; HTTP error is not TCP failure |
| Same request in original app and native CLI | App proxy/DoH/trust/session/policy versus shared host path |
| Repeated comparable samples | Intermittency or destination loss versus one rate-limited intermediate hop |

Windows: start with scoped `Get-NetIPConfiguration`, `Get-NetRoute`,
`Get-DnsClientServerAddress`, `Resolve-DnsName` for the affected name,
`Test-NetConnection` for its port, and `netsh winhttp show proxy`. WinHTTP settings
are not a complete picture of browser, user, environment-variable or app proxies.
On macOS use `scutil --dns`, `scutil --proxy`, `route -n get` for the destination,
and the affected app's lookup. On Linux use `ip address`, `ip route get`, and
`resolvectl status/query` where installed; otherwise inspect the actual resolver.
`dig`/`nslookup` may not exercise the app/system resolver. Limit output to implicated
interfaces/names; raw inventories expose addresses, topology and proxy credentials.

For an authorized HTTPS target, bounded `curl` timing can expose lookup, connect,
handshake, first-byte and total elapsed time. On Windows use `curl.exe` to avoid
alias ambiguity. Retain certificate verification and installed-version-supported
connect/total limits. HEAD may be rejected or differ from the app request; avoid
redirects into unexpected hosts. Timings are cumulative: calculate phase differences
rather than attributing all handshake elapsed time to TLS. Do not expose session
headers or tokens just to reproduce a simple reachability error.

Internal names failing only on VPN suggest split-DNS/routing policy; compare the
selected resolver/path while preserving required VPN access. IPv4/IPv6,
proxy/direct and alternate-network comparisons are experiments, not permanent
fixes, and need authority if they alter exposure or disconnect access. Trace paths
only when earlier evidence points to routing; intermediate ICMP loss is not proof
of end-to-end loss. PMTU needs protocol/path-specific evidence, not a universal
MTU guess. For throughput/loaded-latency issues use
[Linux network performance](../diagnose-linux-network-performance/SKILL.md)
where applicable; do not stress a network to answer a simple DNS question.

## Repair and acceptance

Preserve managed DNS, firewall, proxy, VPN and trust policy. Prefer correction of
the evidenced exact setting through its supported owner. Cache flushes, stack
resets, disconnects and certificate installation change state; plan authority,
reconnect and rollback with [reversible repair](../verify-reversible-repair/SKILL.md).
Disabling TLS validation, security filters or required VPN is not a repair.
Do not install donor probe tools.

Repeat the original request through the required path in the original app; check
any changed resolver/route/trust invariant. Report failing layer, observations,
competing explanation, user result and visibility gaps. Successful ping, HTTP
401/403 or command exit alone is not application acceptance.

## Sources

- [Microsoft DNS client troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/troubleshoot-dns-client-resolution-issues) (factual reference, not copied text)
- [curl options](https://curl.se/docs/manpage.html)
- [Pinned adaptation and license](SOURCE.md)
