![IAMT Logo](assets/IAMT-logo.png)

# Dynamic Software Licensing Best Practices

## Purpose

This repository contains the reviewed draft of an IAMT industry best practices document for software-based, dynamic software licensing in broadcast and media workflows.

The best-practices document is not a formal standard. It is deliberately structured in a standard-like way to support alignment across manufacturers, operators, system integrators, and industry stakeholders.

## Management Summary

Dynamic Software Licensing (DSL) defines an interoperable framework for licensing software in
dynamic broadcast and media environments. It is aimed at operating models in which applications,
media functions, and supporting services may run across on-premises, cloud, hybrid, and
resilience-oriented topologies. In those environments, licensing must behave as a governed runtime
capability rather than as a fixed activation step tied to a single host or appliance.

The main problem DSL addresses is the gap between traditional licensing assumptions and current
deployment practice. Many established licensing systems were built around static infrastructure,
manual fulfillment, long-lived instances, and limited workload mobility. Modern operations depend
on automated provisioning, short-lived runtime contexts, controlled failover, API-based control
planes, and policy-driven service continuity. When the licensing layer does not match those
conditions, it introduces avoidable operational risk, slows deployment, complicates recovery, and
reduces portability across environments and vendors.

DSL responds to that problem by separating commercial entitlement from runtime authorization.
Entitlements define the durable customer rights for an application or capability. Leases represent
the time-bounded runtime grants issued to specific workloads within those rights. Policies define
renewal timing, grace behavior, and enforcement actions. Identity evidence and binding rules define
how the control plane establishes trust in the requesting workload. Usage and metering events
provide the basis for audit, analytics, and commercial reconciliation. This gives DSL a complete
lifecycle for issue, renew, reissue, revoke, inspect, and observe operations without coupling the
model to a single vendor architecture.

From a management perspective, the benefit of DSL is control with fewer structural dependencies.
The framework improves clarity over who is entitled to use what, under which conditions, for how
long, and with which audit trail. That supports governance, service continuity, tenant separation,
security review, and operational accountability across vendors, customers, and integrators. It also
reduces the risk that licensing becomes the constraint that blocks cloud transition, disaster-
recovery planning, cross-site mobility, or multi-vendor deployment choices.

DSL is intentionally specified as an open best-practice model, not as a proprietary product design.
It does not require a single commercial modality, a single token format for all vendor-specific
payloads, or a single deployment technology. Instead, it defines a common vocabulary and a stable
set of architectural expectations that different implementations can adopt while preserving local
product differentiation. This is relevant to software vendors designing licensing platforms,
customer organizations evaluating portability and governance, system integrators assembling
multi-vendor solutions, and industry groups seeking a shared reference model.

This repository provides that model in a form that can be reviewed and implemented. The document
set includes terminology, design principles, a reference model, conformance framing, normative
requirements, canonical API definitions, canonical data-model definitions, security and trust
guidance, operational profiles, and migration considerations. Its purpose is to provide a practical
basis for decision-making, architecture review, implementation planning, and further industry
alignment, rather than a purely conceptual position paper.

## Scope of This Repository

This repository is used to:
- define and evolve the structure of the best-practices document,
- capture terminology and architectural concepts,
- document normative and informative content separately,
- support collaborative drafting and review in a transparent, versioned way.

This repository does **not** yet represent a final published best-practices document.

## Document Structure

| Area | Purpose |
| --- | --- |
| `best-practices/` | Core best practices chapters |
| `annexes/normative/` | Normative annexes required for consistent interpretation |
| `annexes/informative/` | Examples, mappings, FAQs, reference architectures |
| `api/` | Machine-readable API contract and data schemas |
| `diagrams/` | Architecture and sequence diagrams |

## How to Navigate

- [best-practices/index.md](best-practices/index.md) — chapter list and status overview
- [best-practices/04-terminology-and-abbreviations/](best-practices/04-terminology-and-abbreviations/) — controlled vocabulary
- [best-practices/09-normative-requirements/](best-practices/09-normative-requirements/) — normative requirements structure

## Working Principles

- Terminology first.
- Structure before detail.
- Platform-agnostic main document.
- Clear separation of normative and informative content.
- Versioned development through Git and GitHub.

## Team Workflow

- [WORKFLOW.md](WORKFLOW.md) — team operating model: milestones, issues, roles, delivery
- [CONTRIBUTING.md](CONTRIBUTING.md) — branch, PR, git commands, writing rules
- [GOVERNANCE.md](GOVERNANCE.md) — roles, status definitions, editorial rules

## Current Status

Repository status: **Reviewed Draft**

The main document is now organized as a complete review draft for group comment ahead of the planned end-of-August release. See [best-practices/index.md](best-practices/index.md) for chapter-level status.

## PDF Availability

The document is also available as a PDF through the repository releases.

The latest rolling draft PDF is published under the `latest` prerelease, and version-specific PDFs are attached to the corresponding tagged releases.

See the releases page for downloads: [https://github.com/Dynamic-Software-Licensing/Dynamic-Software-Licensing---Best-Practices/releases](https://github.com/Dynamic-Software-Licensing/Dynamic-Software-Licensing---Best-Practices/releases).

## License

This repository is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE).

The license does not grant rights to use the IAMT name, logo, or other trademarks, except as permitted by Section 6 of the Apache License, Version 2.0.
