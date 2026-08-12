# 05.01 Stakeholder Groups

## Purpose

This section defines the stakeholder categories addressed by these best practices.
It establishes the stakeholder taxonomy used by Sections 5.2 through 5.5 and provides
the basis for traceable requirement derivation in later chapters.

## Stakeholder Model

The Dynamic Software Licensing (DSL) landscape comprises five primary stakeholder groups:

1. Customer Organizations
2. Independent Software Vendors (ISVs)
3. System Integrators (SIs)
4. Platform and Infrastructure Providers
5. Industry Bodies and Governance Participants

These groups are distinguished by decision authority, operating responsibility,
and lifecycle accountability.

In practice, these stakeholder groups do not operate in isolation. Licensing outcomes are
produced through coordinated decisions across commercial, technical, and governance
boundaries. This is particularly visible in cloud and hybrid environments, where entitlement
state, workload identity, deployment automation, and financial controls must remain aligned.

The reference perspective throughout this chapter is a dynamic software licensing model.
The text therefore centers on target-state capabilities and operating behavior.

## Scope Statement

This section:
- identifies stakeholder groups relevant to DSL adoption and operation,
- describes their primary concerns at category level,
- defines the boundary to persona-level analysis in Section 5.2.

This section does not:
- define role-specific user stories,
- define implementation-specific controls,
- introduce normative requirement statements.

## Shared Dynamic Baseline

Across all stakeholder groups, a common dynamic baseline is expected:

- API-accessible lifecycle operations,
- elastic and highly available control functions,
- auditable and cryptographically protected license artifacts,
- operational observability for usage, limits, and forecast,
- automation-ready integration into deployment workflows.

This shared baseline is relevant because later chapter content is intended to remain
platform-agnostic while still being implementation-oriented. The stakeholder model therefore
anchors concerns in capability terms rather than vendor-specific product terms.

## 1. Customer Organizations

Customer organizations operate media, broadcast, and adjacent production environments and
consume licensed capabilities across steady-state, event-driven, and validation contexts.

Primary concern areas include:
- predictable and explainable licensing spend,
- timely activation and deactivation of licensed capabilities,
- continuity during failover and recovery scenarios,
- operational transparency for audit and compliance.

Customer organizations typically contain multiple internal roles (for example engineering,
operations, finance, security, and procurement). Role-specific perspectives are addressed
in Section 5.2.

From a lifecycle perspective, customer organizations are the primary source of demand
signals: they define required service levels, resilience expectations, and acceptable
commercial envelopes. Their constraints strongly influence what is considered operationally
viable in later workflow and requirement sections.

## 2. Independent Software Vendors (ISVs)

ISVs define, deliver, and support licensable products and features.
They balance commercial protection objectives with operational usability expectations.

Primary concern areas include:
- protecting license integrity and preventing misuse,
- supporting multiple commercial modalities (for example annual and usage-based),
- reducing onboarding and deployment friction across dynamic runtime environments,
- scaling support through automation and standard interfaces.

ISVs are also responsible for offering commercially coherent models that can combine
time-based commitments, process-based consumption units, and outcome-based value metrics
without creating opaque portfolio complexity.

Accordingly, ISVs carry dual accountability: they must preserve commercial integrity while
ensuring that license controls remain operable within automated customer environments.
This dual accountability is a recurring theme across Sections 5.3 to 5.5.

## 3. System Integrators (SIs)

SIs implement, integrate, and operate multi-vendor solutions for customer organizations.
They translate architectural intent into repeatable delivery and operations patterns.

Primary concern areas include:
- automating licensing in IaC and CI/CD workflows,
- integrating heterogeneous vendor licensing behaviors,
- minimizing manual activation paths and exception handling,
- ensuring operational consistency across environments.

Because SIs typically bridge multiple vendors and customer teams, they are often the first
to encounter interoperability gaps. Their perspective is therefore essential for identifying
where lifecycle semantics need to be standardized to support repeatable delivery.

## 4. Platform and Infrastructure Providers

Platform and infrastructure providers supply execution, identity, orchestration,
and observability capabilities required by licensed workloads.

Primary concern areas include:
- identity-based workload binding instead of host-bound constraints,
- secure and auditable interactions with licensing control functions,
- resilient operation during scale-out, replacement, and failover,
- interoperability between platform services and licensing workflows.

In many deployments, platform constraints determine what is practically achievable in
license lifecycle automation. For this reason, platform and infrastructure perspectives are
not merely implementation detail; they are preconditions for feasible design choices.

## 5. Industry Bodies and Governance Participants

Industry bodies and governance participants align terminology, baseline expectations,
and interoperability direction across vendors and adopters.

Primary concern areas include:
- common language for lifecycle operations and entitlements,
- consistent interpretation of portability and compliance requirements,
- reducing fragmentation caused by siloed licensing approaches,
- maintaining traceability from industry pain points to best practice guidance.

Governance participants also provide continuity across drafting cycles by keeping core
terminology and intent stable while implementations evolve. This continuity is necessary to
maintain comparability across profiles, conformance levels, and migration paths.

## Cross-Group Interaction Summary

The stakeholder groups interact through recurring responsibility boundaries:

- customer organizations define operational and commercial demand,
- ISVs publish licensable capabilities and policy envelopes,
- SIs integrate and operationalize cross-vendor workflows,
- platform providers supply identity and runtime control primitives,
- governance participants sustain interoperability alignment and shared terminology.

Taken together, these interaction boundaries define the context in which use case classes
and workflow definitions should be interpreted. They also provide the basis for evaluating
whether proposed requirements are complete, balanced, and operationally credible.

## Boundary to Section 5.2

This section defines stakeholder categories at group level.
Section 5.2 defines role-level perspectives within and across those groups.

## Section Positioning

This section is descriptive and analytical.
It provides context and traceability input for downstream architecture and requirement
chapters and does not itself introduce normative requirement language.
