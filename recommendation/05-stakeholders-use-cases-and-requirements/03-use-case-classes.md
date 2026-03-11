# 05.03 Use Case Classes

## Purpose

This section defines the principal operational use case classes that the Dynamic Software Licensing recommendation is designed to support.

Each use case class represents a distinct combination of operational characteristics, licensing granularity requirements, and infrastructure assumptions. The classes are representative, not exhaustive.

## Use Case Class Definitions

### UC-01: Continuous 24/7 Operations

Covers broadcast and media workflows that run continuously without interruption. Typical examples include playout systems, master control environments, and always-on monitoring infrastructure.

Operational characteristics:

- High availability and continuity are primary requirements.
- License renewal and validation must not introduce service interruption risk.
- Resilience mechanisms, including hot standby and failover configurations, must be supported by the licensing model.
- Licensing cost is typically aligned to a recurring subscription model (annual or perpetual), but granular burst capacity may also be required.

Licensing requirements implied:

- License mobility across primary and standby instances.
- Grace period behaviour maintaining production operation when the licensing service is temporarily unreachable.
- Advance expiry notification aligned with operational planning cycles.
- Local token validation avoiding real-time dependency on the licensing control plane in the hot path.

### UC-02: Frequent Event-Driven Production

Covers workflows activated for recurring but non-continuous events. Typical examples include news production, regular sports league coverage, and recurring special programming.

Operational characteristics:

- Licensing must be available for planned events without requiring advance provisioning lead times incompatible with editorial planning cycles.
- Granularity finer than annual is required; monthly or per-event licensing is typical.
- Multiple vendors may be involved, with different products requiring different licensing terms for the same event.
- The licensing model must accommodate variation in scale across events of different sizes.

Licensing requirements implied:

- Time-bounded licensing with monthly or shorter granularity.
- Ability to scale licensed capacity within an event window.
- Unified multi-vendor management.
- Cost attribution per event for financial reporting.

### UC-03: Infrequent High-Scale Events

Covers workflows activated infrequently but at high scale. Typical examples include Olympic Games coverage, major sports championships, and large-scale live event productions.

Operational characteristics:

- Licensing granularity must be very fine: daily, hourly, or outcome-based billing may be required.
- The scale of deployment is significantly larger than routine operations and may involve managed service providers, outside broadcast operators, or SI-managed environments.
- Complexity of licensing management at peak scale argues for maximum automation.
- The organisation operating the infrastructure may not be the direct licensee for all products in use.

Licensing requirements implied:

- Fine-grained time-based or consumption-based licensing modalities.
- Delegated or brokered licensing in managed service scenarios.
- Full automation of license issue, renewal, and release at event scale.
- Audit trail supporting post-event cost reconciliation.

### UC-04: Test, Validation, and Development Environments

Covers non-production environments used for system validation, pipeline testing, software integration, and development work.

Operational characteristics:

- Licensing cost must be clearly separated from production licensing.
- Granularity may be very fine; hourly or intermittent access is typical.
- The same software products used in production may require testing under different entitlement scopes.
- Test environments are frequently built and destroyed; full IaC integration is required.

Licensing requirements implied:

- Distinct usage type or rights category for test, development, and validation contexts.
- Fine-grained time-based modalities.
- IaC integration including licensing steps in automated environment build and teardown.
- Clear separation of test entitlements from production entitlements in the data model.

### UC-05: AI-Powered and Outcome-Based Services

Covers workflows delivering value through AI-driven or automated processing, where the natural billing unit is the outcome produced, not time elapsed. Typical examples include automated content analysis, highlight generation, subtitle production, and compliance checking.

Operational characteristics:

- Processing volume and timing are unpredictable and variable.
- Time-based licensing models are poorly aligned with actual value delivery.
- Outcome-based billing requires metering at the level of individual results: per clip, per minute of subtitles, per compliance report, per inference operation.

Licensing requirements implied:

- Outcome-based and process-unit-based metering in addition to time-based models.
- Flexible dimension definitions representing the relevant billing unit for each product.
- Usage recording at sufficient granularity to support billing reconciliation.
- Ability to combine outcome-based and time-based dimensions within a single licensing arrangement.

### UC-06: Hybrid and Disaster Recovery Configurations

Covers deployments spanning cloud and on-premises infrastructure, or including explicit disaster recovery provisions alongside primary production systems.

Operational characteristics:

- Licensing must support operation across cloud and on-premises environments from a single entitlement.
- Disaster recovery configurations require licenses available on standby instances activatable within a defined recovery time objective.
- Air-gapped or connectivity-constrained environments may be involved.

Licensing requirements implied:

- Identity-based binding not tied to physical hardware identifiers.
- License mobility operations (reissue, move) enabling seamless failover without ISV intervention.
- Offline licensing capability with defined grace behaviour for air-gapped environments.
- Hybrid licensing across cloud and non-cloud targets from a single entitlement.

## Relationship Between Use Cases and Profiles

The use case classes defined in this section inform the conformance profiles described in Chapter 08:

- UC-01 and UC-06 inform the Foundational profile: continuity, resilience, and offline operation.
- UC-02 and UC-03 inform the Cloud-Native profile: scalability, fine-grained modalities, and automation.
- UC-04 informs requirements across all profiles, in particular usage type differentiation and IaC integration.
- UC-05 informs the Advanced Interoperable profile: outcome-based metering and flexible dimension models.

A detailed use-case-to-profile mapping is provided in Annex I.

## Scope of This Section

This section defines use case classes at the pattern level. It does not define normative interface requirements.

Normative requirements derived from these classes are defined in Chapter 09. Design choices in the reference model (Chapter 07) are traceable to the classes defined here.

