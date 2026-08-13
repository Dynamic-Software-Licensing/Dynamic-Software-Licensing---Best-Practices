# 09.08. Operational Requirements

## Purpose

This section defines the operational requirements for continuity, observability, outage
handling, recovery, and routine operator interaction in the Dynamic Software Licensing (DSL)
model.

Requirements in this section are identified as `OPS-n`.

## Operational Requirements

### OPS-1 — Defined continuity behavior

The licensing model **MUST** behave predictably during transient control-plane or network
interruption. Continued operation, degraded operation, or stop behavior **MUST** be governed
by documented policy rather than by implicit client-specific fallback.

### OPS-2 — Background renewal and recovery

The license agent or equivalent runtime component **MUST** attempt renewal in the background
before expiry and continue retrying during interruption using a bounded retry strategy. When
connectivity returns, recovery **MUST** restore normal licensed operation without requiring
full redeployment where the grant remains valid.

### OPS-3 — Operator visibility into current state

Operators **MUST** be able to inspect current lease state, expiry horizon, effective policy,
and recent lifecycle outcomes. The system **SHOULD** make it clear whether a workload is in
normal operation, renewal retry, grace, degraded mode, or exhaustion.

### OPS-4 — Advance alerting

The model **MUST** support advance alerting for conditions that may affect licensed operation,
including renewal failure trends, impending expiry, grace countdown, repeated usage-submission
failure, and revocation or policy changes where those require operator action.

### OPS-5 — Routine self-service actions

The model **SHOULD** support documented, customer-visible mechanisms for routine administrative
actions such as inspection, controlled release or revocation initiation where authorized, and
capacity-related visibility, without requiring vendor-side manual intervention for every such
task.

### OPS-6 — Recovery with audit continuity

Recovery after interruption **MUST** preserve the ability to reconstruct what occurred. Renewal
attempts, policy transitions, grace entry, exhaustion actions, reissue cutover, and delayed
usage submission **MUST** remain auditable across the outage boundary.

### OPS-7 — Profile-sensitive behavior

Operational behavior **MUST** be configurable or governable in a way that can reflect the
needs of different deployment profiles, such as continuous production, burst event workloads,
testing environments, and stricter protection scenarios, without changing the underlying DSL
core semantics.

## Relationship to Other Sections

- Section 09.03 defines the lifecycle and policy semantics behind continuity behavior.
- Section 09.05 defines the usage buffering and reconciliation expectations relevant to outage
  handling.
- Section 09.07 defines the security bounds that limit how far operational continuity may
  extend.

## Section Positioning

This section expresses the practical operating expectations of the DSL model. It ensures that
the best practices remain usable in production environments where licensing behavior is part of
day-to-day operations rather than an abstract contract only.
