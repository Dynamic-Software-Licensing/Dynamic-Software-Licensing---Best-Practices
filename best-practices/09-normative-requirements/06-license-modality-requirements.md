# 09.06 License Modality Requirements

## Purpose

This section defines the requirements governing license modality support in the Dynamic
Software Licensing (DSL) model. It focuses on how different modality types influence runtime,
metering, entitlement interpretation, and lifecycle handling, without prescribing pricing or
commercial packaging.

Requirements in this section are identified as `MOD-n`.

## License Modality Requirements

### MOD-1 — Support for multiple modality types

The DSL model **MUST** support more than one license modality where product and entitlement
policy require it. At a minimum, the best-practices model **MUST** be capable of expressing
time-based, process-based, and outcome-based modality semantics.

### MOD-2 — Explicit modality semantics

For every supported modality, the implementation **MUST** define what is granted, what is
measured, what lifecycle events matter, and what usage dimensions or counters determine
consumption. Modality interpretation **MUST NOT** rely on undocumented commercial shorthand.

### MOD-3 — Consistent modality behavior across lifecycle operations

Issue, renew, reissue, revoke, and usage reporting behavior **MUST** remain coherent with the
selected license modality. A modality **MUST NOT** imply hidden exceptions to core lifecycle
semantics unless those exceptions are explicitly documented and governed by policy.

### MOD-4 — Mixed-modality coexistence

The model **SHOULD** support coexistence of multiple modalities within the same tenant or
account landscape, provided entitlement boundaries remain explicit. Multi-product or
multi-environment deployments **MUST NOT** require a single modality model across all licensed
capabilities.

### MOD-5 — Modality transparency to operators

The active modality **MUST** be visible to the customer or operator together with the granted
dimensions, relevant policy, and resulting lifecycle behavior. A user **MUST** be able to tell
whether a grant behaves as time-based, process-based, or outcome-based without reverse-
engineering vendor logic.

### MOD-6 — No contradiction with policy and metering

A chosen modality **MUST** align with the metering model and policy model used for the same
grant. Implementations **MUST NOT** expose a modality label whose billing or enforcement
behavior cannot be explained by the documented dimensions, policy, and lifecycle controls.

## Relationship to Other Sections

- Section 09.05 defines the metering behavior that operationalizes modality semantics.
- Section 09.03 defines the lifecycle and policy controls that remain applicable regardless of
  modality.
- Section 09.09 defines the external integration expectations for modality-aware automation and
  reporting.

## Section Positioning

This section keeps the DSL model flexible enough for different licensing strategies while
requiring that modality-specific behavior remain explicit, inspectable, and aligned with the
canonical lifecycle and metering model.
