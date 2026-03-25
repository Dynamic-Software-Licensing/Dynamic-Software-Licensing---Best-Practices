# 02.01. In Scope

## What These Best Practices Cover

The Dynamic Software Licensing best practices are intended to define a coherent, implementable framework for software licensing in broadcast and media environments. The scope is deliberately focused: the document addresses the licensing layer itself, not the products or workflows that the licensing layer governs.

The following areas are within the scope of these best practices.

## Software Licensing Approaches for Broadcast and Media Workflows

The primary focus is on how software licenses are managed in the context of broadcast, media production, and related media technology workflows. This includes both traditional broadcast environments and modern cloud-based or hybrid production platforms.

The best practices address how licenses should behave in these environments — not how the media workflows themselves should be built.

## Software-Based, Hybrid, and Software-Defined Licensing Concepts

The best practices apply to licensing models that are suited to software-defined, containerized, and cloud-native infrastructure. This includes fully software-based deployments, hybrid models that combine on-premises and cloud resources, and environments where workloads move dynamically between infrastructure tiers.

Hardware-based licensing mechanisms are not the target model, though the best practices acknowledge that migration from hardware-bound approaches is a relevant transition scenario.

## Core Licensing Operations

The following licensing operations are in scope and are defined normatively in this document:

- **Entitlement**: the right to use software, as granted by the software publisher to the customer organization.
- **Lease**: the active, time-bounded allocation of an entitlement to a specific workload or deployment context.
- **Renewal**: the extension of an active lease before it expires.
- **Move**: the transfer of an active lease from one workload or environment to another.
- **Revoke**: the explicit termination of an active lease.
- **Usage recording**: the capture of metered consumption data for billing, auditing, or reporting purposes.

These operations form the operational vocabulary of the DSL framework. All normative content in later chapters is grounded in these concepts.

## API-Oriented Licensing Interactions

The best practices define how licensing functions are exposed and consumed through APIs. This includes the structure of licensing requests, the format of license tokens, the behavior of licensing endpoints, and the patterns for integration with orchestration and automation tooling.

API-oriented interaction is a foundational requirement of the DSL framework, not an optional feature.

## Workload Identity-Based Binding

License binding based on workload identity is in scope. This means that licenses are associated with verifiable software or infrastructure identities rather than with hardware properties such as MAC addresses, hostnames, or hardware dongles.

The best practices define the expectations for identity-based binding, including the requirements that apply to the identity tokens used in licensing requests.

## Metering, Usage Tracking, and Policy Handling

In scope are the mechanism and data models for metering software usage, tracking active license allocations, and enforcing license policies. This includes both real-time enforcement and post-hoc reporting.

Usage-based and consumption-based licensing models are explicitly in scope and are treated as first-class patterns alongside traditional entitlement-based models.

## Observability, Auditability, and Operational Transparency

The best practices define requirements for visibility into the licensing layer. This includes the ability to inspect active leases, monitor consumption against entitlements, produce audit trails of licensing events, and provide cost attribution data to operators and finance stakeholders.

Observability is treated as a structural requirement, not as a monitoring add-on.

## Migration from Legacy Licensing Approaches

Guidance on migration from existing hardware-bound or manual licensing mechanisms toward the DSL target model is in scope. This is addressed as a practical concern: many organizations will need to operate both models simultaneously during a transition period, and the best practices should support that reality without endorsing the continuation of legacy approaches.

Migration guidance is primarily informative. It does not constitute a normative endorsement of legacy licensing patterns.
