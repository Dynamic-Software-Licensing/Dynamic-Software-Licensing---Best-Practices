# 09.01. General Requirements

## Purpose

This section defines the general requirements that apply across the Dynamic Software Licensing
(DSL) best practices. These requirements establish the baseline expectations that every
DSL-aligned implementation must satisfy before topic-specific requirements for identity,
policy, API behavior, metering, security, operations, or integration are applied.

The requirements in this section are intentionally cross-cutting. They express the structural
expectations that make the rest of the best practices coherent and interoperable.

## Requirement Scope

The requirements in this section apply to the DSL model as a whole, including:

- the control plane,
- the workspace plane,
- the interfaces between them,
- administrative and automation-facing clients,
- the interpretation of policies, tokens, and lifecycle operations.

Detailed requirements for specific domains are defined in later sections of this chapter.

## General Requirements

### GEN-1 — Open and documented interfaces

All licensing lifecycle behavior that is required for normal operation **MUST** be available
through open, documented interfaces. An implementation **MUST NOT** depend on undocumented,
manual, or vendor-private operational steps for routine issue, renew, reissue, revoke, usage
reporting, or administrative inspection behavior.

### GEN-2 — Separation of decision and enforcement

The DSL model **MUST** separate licensing decision authority from runtime enforcement. The
control plane **MUST** remain the authoritative source for entitlements, leases, policy, and
signing, while the workspace plane **MUST** enforce granted capability locally based on the
artifacts issued by the control plane.

### GEN-3 — Local runtime continuity

An implementation **MUST** support local validation and local enforcement of the currently
granted license state so that licensed workloads do not require a per-use synchronous round
trip to the control plane. Any continued operation during interruption **MUST** remain bounded
by explicit token and policy constraints.

### GEN-4 — Identity-based operation

Issue, renew, and reissue behavior **MUST** operate on verifiable workload or actor identity
rather than on static hardware fingerprints alone. An implementation **MUST NOT** treat host
attributes such as hostname, MAC address, or manually copied machine identifiers as the sole
basis for trust.

### GEN-5 — Policy-governed lifecycle behavior

Lifecycle behavior **MUST** be governed by explicit policy rather than by hidden client logic
or ad hoc operator intervention. Renewal timing, grace behavior, exhaustion actions, usage
handling, and revocation effects **MUST** be determinable from documented server-defined policy
and issued runtime artifacts.

### GEN-6 — Tenant-aware isolation and control

The model **MUST** preserve tenant separation across entitlements, leases, usage, policy, and
administrative actions. A tenant **MUST NOT** be able to observe, modify, or consume another
tenant's licensing state except where an explicitly delegated cross-tenant governance model is
defined and audited.

### GEN-7 — Operational transparency

An implementation **MUST** provide sufficient observability for operators and administrators to
understand current license state, recent lifecycle actions, and material failures. At a
minimum, the model **MUST** support inspection of lease state, visibility into renewal or
revocation outcomes, and traceability of significant license lifecycle events.

### GEN-8 — Platform-neutral applicability

The core DSL model **MUST** remain platform-neutral at the best-practices level. Platform-
specific realization details **MAY** vary by deployment environment, but those variations
**MUST NOT** change the core lifecycle semantics, trust model, or interoperability assumptions
defined by these best practices.

### GEN-9 — Interoperable extension boundaries

Implementations **MAY** extend the canonical model with vendor-specific fields, controls, or
automation patterns where needed, but such extensions **MUST NOT** undermine the canonical
interpretation of lifecycle operations, token validity, tenant isolation, or policy behavior.
Where extensions affect interoperability, they **SHOULD** be explicitly documented.

## Relationship to Other Sections

- Section 09.02 refines the identity and binding requirements introduced by GEN-4.
- Section 09.03 refines the policy and lifecycle expectations introduced by GEN-3 and GEN-5.
- Section 09.04 specifies the interface expectations introduced by GEN-1.
- Sections 09.07 and 09.08 further develop the security and operational expectations
  introduced by GEN-6 and GEN-7.

## Section Positioning

This section provides the baseline requirement layer for the rest of Chapter 09. It should be
used to assess whether later domain-specific requirements remain aligned with the core DSL
principles of openness, local enforceability, identity-based trust, tenant separation, and
platform-neutral interoperability.
