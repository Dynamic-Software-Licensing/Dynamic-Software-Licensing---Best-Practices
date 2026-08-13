# 09.03. Lease and Policy Requirements

## Purpose

This section defines the requirements governing lease lifecycle behavior, policy ownership,
renewal timing, grace behavior, exhaustion actions, and revocation effects. These requirements
ensure that runtime continuity and enforcement behavior remain explicit, bounded, and
consistent across implementations.

Requirements in this section are identified as `LPR-n`.

## Lease and Policy Requirements

### LPR-1 — Explicit lease state

An implementation **MUST** manage leases as explicit state with identifiable lifecycle phases,
including at least issued, active, renewed, reissued, revoked, expired, and exhausted or
terminated outcomes where applicable.

### LPR-2 — Policy-defined renewal behavior

Renewal behavior **MUST** be governed by explicit policy parameters communicated by the control
plane. At a minimum, policy **MUST** define when renewal begins, how retry behavior operates,
what grace period applies after expiry, and what action is taken when grace is exhausted.

### LPR-3 — Local policy enforceability

The effective lease policy **MUST** be conveyed to the workspace plane in a form that can be
enforced locally during interruption. Runtime behavior during disconnection **MUST NOT** depend
on an implicit, server-only interpretation of grace or exhaustion rules.

### LPR-4 — Bounded continuity

Continued operation after missed renewal **MUST** remain bounded by explicit token lifetime and
grace policy. An implementation **MUST NOT** permit indefinite continuation without successful
contact with the control plane or an explicitly governed offline mechanism.

### LPR-5 — Defined exhaustion actions

When grace is exhausted or a lease can no longer continue, the resulting action **MUST** be
defined by policy. The implementation **MUST** apply a documented outcome such as drain,
degrade, or stop rather than failing unpredictably.

### LPR-6 — Revocation semantics

The model **MUST** support revocation of active leases. When revocation cannot be delivered
immediately, its effect **MUST** take hold no later than the next successful lifecycle contact
or the bounded validity window of the currently issued token.

### LPR-7 — Reissue without double consumption

Reissue behavior **MUST** support controlled mobility of licensed capability without producing
an undefined interval in which both the original and replacement workload appear fully
authorized beyond policy. The cutover semantics **MUST** be explicit and auditable.

### LPR-8 — Inspectable lifecycle state

Lease lifecycle state, effective policy, expiry, and recent transitions **MUST** be inspectable
through documented administrative or programmatic interfaces so that operators can understand
why a workload is active, renewing, degraded, or stopped.

## Relationship to Other Sections

- Section 09.02 defines the identity rules that govern issue, renew, and reissue.
- Section 09.07 defines the revocation, token, and trust protections that make bounded
  continuity safe.
- Section 09.08 defines the operational handling of alerts, interruption, and recovery.

## Section Positioning

This section defines the runtime semantics of leasing in the DSL model. It is the bridge
between the conceptual lifecycle in the reference model and the operational continuity rules in
the security and operations chapters.
