# 05.04 Derived Requirement Themes

## Purpose

This section identifies the principal requirement themes derived from the stakeholder concerns and use case analysis in Sections 01 through 03.

Each theme represents a recurring pattern of need that appears across multiple personas, use cases, or stakeholder groups. This section is analytical in nature and does not define normative requirements. Normative requirements are defined in Chapter 09.

## Derived Requirement Themes

### RT-01: Automation and IaC Integration

The inability to include licensing in automated deployment workflows is a consistently identified high-friction point across all stakeholder groups and use cases.

This theme drives requirements for:

- an API-first licensing interface accessible without manual or GUI-mediated steps,
- a CLI interface suitable for startup scripts and automation pipelines,
- defined programmatic interfaces for issue, renew, move, revoke, and inspect operations,
- IaC module patterns that include licensing as a standard deployment step.

### RT-02: Identity-Based Binding and Portability

Licensing mechanisms that bind to hardware identifiers (hostnames, MAC addresses, dongles) are incompatible with cloud and hybrid deployments where infrastructure is ephemeral and instance identity is dynamic.

This theme drives requirements for:

- binding licenses to workload identity evidence (IAM roles, service account tokens, instance identity documents) rather than hardware identifiers,
- lifecycle operations supporting license mobility between instances without requiring ISV intervention,
- separation of license entitlement from the specific infrastructure on which it is currently active.

### RT-03: Resilience and Continuity Under Failure

Licensing mechanisms that fail hard when a renewal cannot be completed are incompatible with broadcast production continuity requirements.

This theme drives requirements for:

- short-lived signed tokens with local validation, so that the licensing control plane is not in the critical path of application operation,
- defined grace period behaviour specifying how the licensing agent behaves when the licensing service is unreachable,
- configurable degradation options (drain, degrade, stop) allowing operators to align grace behaviour with specific continuity requirements,
- advance expiry notification providing sufficient warning for operational response.

### RT-04: Flexible and Proportional Commercial Models

A single time-based subscription model does not adequately serve the range of operational patterns in the broadcast and media industry.

This theme drives requirements for:

- multiple time-based granularities: hourly, daily, monthly, annual,
- outcome-based and process-unit-based metering where time-based models are inappropriate,
- flexible dimension definitions representing the relevant billing unit for each product and use case,
- ability to combine multiple dimension types within a single licensing arrangement.

### RT-05: Transparency and Observability

Real-time visibility into licensing position, cost, and usage is absent across finance, operations, and management functions.

This theme drives requirements for:

- real-time or near-real-time usage reporting from the licensing control plane,
- a unified management view aggregating license status across multiple vendors,
- usage event recording at sufficient granularity to support cost attribution and audit,
- license inventory visibility including active allocations, available capacity, and expiry schedules.

### RT-06: Security and Auditability

Licensing mechanisms must meet organisational security standards, resist misuse, and support full auditability of operations.

This theme drives requirements for:

- cryptographic signing of license tokens enabling tamper detection and local validation,
- comprehensive audit logging of all licensing lifecycle events,
- zero-trust design patterns not requiring vendors to have direct access to customer production resources,
- alignment with applicable security and compliance frameworks.

### RT-07: Self-Service and Reduced Operational Dependency

Routine licensing operations should not require vendor intervention.

This theme drives requirements for:

- an end-user portal providing aggregated license management capability across vendors,
- programmatic interfaces enabling customer-managed license operations,
- defined recovery procedures that do not require ISV intervention for standard failure scenarios,
- defined recovery procedures not requiring ISV intervention for standard failure scenarios,
- self-service visibility into active licenses, remaining capacity, feature flags, and alerts.

### RT-08: Usage Type Differentiation

Production, test, development, and disaster recovery environments have materially different licensing implications. The absence of a usage type model results in test activity consuming production entitlements and prevents accurate reporting of production exposure.

This theme drives requirements for:

- a defined set of usage types within the licensing data model: production, test, development, disaster recovery,
- the ability to issue and track entitlements with distinct usage type designations,
- reporting on usage type alignment between deployed workloads and their entitlements.

### RT-09: Offline and Air-Gapped Operation

A subset of deployments operate with limited or no connectivity to external services, including secure production environments, outside broadcast configurations, and disaster recovery scenarios.

This theme drives requirements for:

- offline licensing capability enabling continued operation without connectivity to the licensing control plane,
- local token validation without real-time communication with a remote server,
- defined behaviour during extended offline periods, including any limitations on feature availability or grace duration.

### RT-10: Multi-Vendor and Cross-Platform Consistency

Broadcast and media environments involve software from multiple vendors across heterogeneous infrastructure. Vendor-specific and platform-specific licensing mechanisms create integration complexity and operational inconsistency.

This theme drives requirements for:

- a platform-agnostic licensing interface operating across cloud, hybrid, and on-premises deployments,
- a standardised API surface that ISVs can implement consistently regardless of their underlying licensing infrastructure,
- a vendor-agnostic client-side SDK or agent model normalising licensing integration for application developers and SI developers.

## Mapping to Later Chapters

| Requirement Theme | Primary Chapter Reference |
|---|---|
| RT-01: Automation and IaC Integration | Chapter 09, Chapter 10 |
| RT-02: Identity-Based Binding and Portability | Chapter 09, Chapter 11 |
| RT-03: Resilience and Continuity | Chapter 09, Chapter 12 |
| RT-04: Flexible Commercial Models | Chapter 09, Chapter 11 |
| RT-05: Transparency and Observability | Chapter 09, Chapter 10 |
| RT-06: Security and Auditability | Chapter 12 |
| RT-07: Self-Service | Chapter 07, Chapter 09 |
| RT-08: Usage Type Differentiation | Chapter 09, Chapter 11 |
| RT-09: Offline Operation | Chapter 09, Chapter 12 |
| RT-10: Multi-Vendor Consistency | Chapter 07, Chapter 08 |

## Scope of This Section

Normative requirements derived from these themes are defined in Chapter 09.

Design choices in the reference model (Chapter 07) are traceable to the themes in this section.

Conformance profiles (Chapter 08) represent graduated approaches to satisfying the requirement themes.

