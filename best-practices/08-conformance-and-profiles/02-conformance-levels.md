# 08.02. Conformance Levels

## Purpose

This section defines how different degrees of DSL alignment can be expressed without reducing
the best practices to a binary pass or fail model.

## Role of Conformance Levels

Organizations and vendors will adopt the DSL model in stages. A structured conformance view
must therefore distinguish foundational alignment from more mature automation,
interoperability, and operational capability.

The purpose of the levels is to support realistic adoption sequencing while keeping the
direction of travel clear.

## Level Interpretation

Conformance levels should be read as cumulative. Each higher level assumes the capabilities of
the previous one and adds stronger expectations.

The levels defined in this chapter are expressed through three implementation profiles:

- Foundational,
- Cloud Native,
- Advanced Interoperable.

## Quick Profile Selection

The following table is intended as the fastest way to understand which profile best matches an
implementation context.

| If the implementation mainly needs... | Most likely profile |
| --- | --- |
| a first credible production baseline with signed tokens, identity binding, and bounded continuity | Foundational |
| API-first automation, dynamic workloads, and operations-integrated lifecycle handling | Cloud Native |
| repeatable cross-vendor semantics, hybrid portability, and mature interoperability evidence | Advanced Interoperable |

## Practical Comparison

| Dimension | Foundational | Cloud Native | Advanced Interoperable |
| --- | --- | --- | --- |
| Main goal | Replace manual or hardware-bound licensing with a credible DSL baseline | Make DSL a normal part of automated cloud or orchestrated operations | Make DSL reliable across products, teams, partners, and environments |
| Typical runtime shape | One main environment, limited hybrid complexity | Dynamic cloud, container, or automation-first workloads | Hybrid, DR, multi-product, or ecosystem-facing environments |
| Identity expectations | Verifiable workload identity is present and used consistently | Identity evidence supports dynamic runtime behavior and stronger automation | Identity semantics remain stable across different platforms and partner boundaries |
| Operational focus | Predictable issue, renew, revoke, and bounded grace handling | Retry, renewal, reissue, and usage behavior remain reliable under workload churn | Portability, traceability, tenant isolation, and semantic consistency remain dependable at scale |
| Integration depth | Limited but real automation | CI/CD, IaC, and operational tooling are normal integration points | External partners and multiple internal teams can rely on the same semantics |
| Best fit for | first DSL production rollout | cloud-native rollout | mature interoperability target |

## How to Read a Profile Claim

A profile claim is useful only when it answers three practical questions:

1. Which conformance target is being claimed: control plane, workspace plane, interface, or end-to-end system?
2. Which operational behaviors can be demonstrated, not just designed?
3. Which later profile expectations are intentionally out of scope for the current implementation?

Without those three clarifications, a profile statement is too vague to help operators,
customers, or integration partners.

## Assessment Logic

When an implementation claims alignment with a profile, the claim should cover the relevant
target surface identified in Section 08.01 and should be supportable by documented behavior,
not only architectural intention.

Reasonable evidence may include:

- documented API or workflow behavior,
- observed lifecycle handling,
- token and policy structures,
- operational controls and audit records,
- integration artifacts used in deployment and recovery.

## What the Levels Are Not

These levels are not intended to become:

- a formal certification program,
- a maturity score for the entire business,
- a replacement for detailed security or legal review,
- a mandate that every implementation immediately target the highest profile.

## Relationship to Requirements

The conformance levels rely on Chapter 09 for substantive requirements. The levels interpret
those requirements as practical adoption bundles rather than redefining them.

For review and implementation assessment, Annex A is the most direct companion to this chapter
because it translates the profiles into compact checklist statements.

## Section Positioning

This section establishes the staged interpretation model that the profile subchapters and
conformance checklist build on.
