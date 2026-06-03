# 12.06 Offline and Grace Behavior

## Purpose

This section defines how the Dynamic Software Licensing (DSL) model treats continuity under
partial disconnection or control-plane unavailability. It establishes the trust and risk
boundaries of offline validation, grace policies, renewal retries, and bounded continuity.

This is where the model's central tension is resolved in concrete terms: the protection
objectives (Section 12.01) versus the requirement that licensing never become a single point
of failure for live production (SEC-OBJ-3, Chapter 05 theme T9). Requirements are identified
as `OFG-n` and use the normative keywords defined in Chapter 03.

## Principle

The model is designed so that an application does not need a constant connection to a
licensing service. It operates on a short-lived, locally validated token it already holds, and
needs connectivity only to renew that token or to report usage. Offline and grace behavior
governs what happens between successful renewals when connectivity is degraded or lost.

The design intent is that disconnection produces **defined, bounded, observable** behavior —
never an abrupt, unexplained production failure, and never unbounded unlicensed operation.

## Offline and Grace Requirements

### OFG-1 — Local validation without round-trips

A workspace-plane component **MUST** be able to validate its current token locally, without a
per-use round-trip to the control plane, so that transient disconnection does not interrupt
operation. Local validation relies on the signed-token mechanisms profiled in Section 12.04
(JWS/JWT per RFC 7515/RFC 7519, validated per RFC 8725). *Realizes SEC-OBJ-3.*

### OFG-2 — Defined grace policy

A grace policy **MUST** define, at minimum: the renewal window (how early renewal begins), the
offline grace duration (how long operation may continue after expiry without renewal), the
action on grace exhaustion, the alert thresholds, and the renewal retry/backoff behavior.
*Realizes SEC-OBJ-3; mitigates THR-7.*

### OFG-3 — Governed policy ownership

The grace policy **MUST** be defined by the vendor as a product default and **MAY** be
overridden by the tenant only where the vendor permits it. The control plane **MUST** enforce
the resulting effective policy, and all policy definitions and overrides **MUST** be audited
(see AUD-4). *Mitigates THR-7.*

### OFG-4 — Policy conveyed to the enforcement point

The effective policy **MUST** be conveyed to the workspace plane (for example as a snapshot
carried in the token and in the issue/renew response) so that it can be enforced locally even
while disconnected. *Realizes SEC-OBJ-3.*

### OFG-5 — Renewal retries with bounded backoff

While disconnected, the license agent **MUST** continue attempting renewal in the background
using bounded exponential backoff with jitter — a well-established retry pattern — so that
connectivity is used promptly when it returns without overwhelming the control plane on
recovery. *Mitigates THR-11.*

### OFG-6 — Defined exhaustion actions

When the grace window is exhausted, the configured action **MUST** be applied. The model
defines three standard actions:

- **DRAIN** — finish current work and refuse new sessions or jobs;
- **DEGRADE** — continue with a reduced capability profile (for example fewer channels or
  disabled premium features);
- **STOP** — halt licensed operation.

The action is selected by policy according to the use case and the vendor's protection stance.
*Realizes SEC-OBJ-3; mitigates THR-5, THR-7.*

### OFG-7 — Advance alerting

Operators **MUST** be alerted as the grace window counts down, at the thresholds defined in
the policy, so that a human can intervene before production is affected. *Realizes
SEC-OBJ-3.*

### OFG-8 — Bounded offline duration

Offline operation **MUST** be bounded. The combination of short token lifetime and a finite
offline grace duration **MUST** limit how long operation can continue without contact, so that
the value of severing connectivity or tampering with the local clock is limited. *Mitigates
THR-6, THR-7.*

### OFG-9 — Revocation is not evadable beyond the bound

Offline and grace behavior **MUST NOT** be usable to evade revocation beyond the bounded
window. A revocation that could not be delivered while disconnected **MUST** take effect no
later than the next renewal attempt. *Mitigates THR-6.* (Consistent with SEC-18, SEC-19.)

### OFG-10 — Idempotent reconciliation of offline usage

Usage accrued while offline **MUST** be buffered locally and reconciled idempotently when
connectivity returns, so that no usage is lost and none is double counted. *Mitigates THR-5;
supports AUD-5.*

### OFG-11 — Air-gapped operation

Air-gapped operation **MAY** be supported using time-boxed offline licenses delivered through
transferable media. Where it is supported, the reduced functionality and the explicit trust
trade-offs (notably the inability to deliver timely revocation) **MUST** be stated, and the
offline period **MUST** remain bounded (OFG-8). *Mitigates THR-6, THR-7.*

## Trust and Risk Trade-off

Offline and grace behavior is the explicit resolution of the protection-versus-continuity
tension named in Chapter 05 (T8 versus T9):

- Longer grace and longer offline bounds favour continuity but widen the window in which a
  revoked or over-using workload can operate.
- Shorter bounds favour protection but increase sensitivity to connectivity problems.

The model does not prescribe a single setting. Instead it requires that the trade-off be
**explicit, governed, bounded, and observable**: chosen by policy (OFG-2, OFG-3), conveyed to
the enforcement point (OFG-4), bounded in time (OFG-8, OFG-9), and alerted on (OFG-7). The
appropriate point on the spectrum depends on the use case class (Chapter 05, Section 5.3) and
the operational profile (Chapter 13) — a continuous 24/7 production typically favours
continuity, while a strict-protection product may favour STOP with a short bound.

## References

- RFC 7515 (JWS); RFC 7519 (JWT); RFC 8725 (JWT BCP) — locally validatable signed tokens —
  OFG-1 (profiled in Section 12.04).
- RFC 7009 — OAuth 2.0 Token Revocation (conceptual analogue) — OFG-9.

The bounded-backoff-with-jitter retry behavior in OFG-5 follows widely adopted reliability
practice rather than a single specification.

## Relationship to Other Chapters

- The security controls (Section 12.04) provide the short-lived tokens (SEC-6), bounded
  exposure (SEC-19), and revocation (SEC-18) that make bounded offline behavior safe.
- The workflow definitions in Chapter 05 (notably the grace/offline continuity and offline
  acquisition workflows) describe the operational sequences this section secures.
- The operational and deployment profiles (Chapter 13) determine which exhaustion action and
  bounds are appropriate per environment.
- The canonical data model defines the policy structure; this section defines its required
  semantics, not its schema.

## Drafting Notes

This section is normative. It defines the required *semantics* of grace and offline behavior
(windows, actions, bounds, alerting, reconciliation) while leaving the concrete policy schema
and default values to the canonical data model, the per-profile guidance in Chapter 13, and
the informative annexes. The action names DRAIN, DEGRADE, and STOP are treated as a
controlled vocabulary for this behavior.

## Drafting To-Do

- Agree recommended default bounds per operational profile and record them in Chapter 13
  rather than here.
- Confirm the DRAIN/DEGRADE/STOP vocabulary against the terminology chapter.
- Cross-reference OFG-10 with the metering and usage-record requirements in Chapter 09.
