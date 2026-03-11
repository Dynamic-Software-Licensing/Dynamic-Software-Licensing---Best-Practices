# 05.01 Stakeholder Groups

## Purpose

This section defines the principal stakeholder categories addressed by the Dynamic Software Licensing recommendation.

Software licensing in broadcast and media environments affects operational, engineering, commercial, governance, and integration functions across multiple organisations. The recommendation addresses all of these constituencies.

## Stakeholder Categories

### Customer Organisations

Customer organisations are the primary operators of broadcast and media workflows. They acquire and deploy software from multiple vendors across heterogeneous environments.

Affected functional groups within customer organisations include:

- operational teams responsible for day-to-day production,
- engineering and architecture teams responsible for infrastructure and deployment,
- finance and procurement teams responsible for cost control and licensing compliance,
- technology leadership responsible for platform strategy and vendor evaluation,
- security and compliance teams responsible for risk assessment and audit obligations.

### Independent Software Vendors (ISVs)

ISVs develop and distribute the software products that are licensed and deployed in broadcast and media workflows.

Licensing-related concerns for ISVs include:

- portfolio complexity arising from supporting multiple licensing models across deployment contexts,
- support burden caused by licensing mechanisms that do not integrate with automated deployment workflows,
- revenue predictability dependent on metering models aligned with actual consumption,
- go-to-market speed affected by the ease with which customers and SIs can deploy and activate licensed software.

### System Integrators (SIs)

System integrators design, deploy, and maintain combined broadcast and media workflow environments on behalf of customers.

Licensing-related concerns for SIs include:

- absence of standardised activation and lifecycle interfaces suitable for IaC workflows,
- operational complexity in managing licenses across multiple vendors with incompatible mechanisms,
- difficulty providing repeatable automated deployment patterns when licensing steps require manual or vendor-specific intervention.

### Industry Bodies and Standards Organisations

Industry bodies and standards organisations provide the governance structure within which the recommendation is developed, maintained, and adopted. Their primary interest is in the long-term credibility, neutrality, and evolution of the framework.

### Platform and Infrastructure Providers

Platform and infrastructure providers supply the underlying compute, network, and service infrastructure on which broadcast and media workflows run.

The recommendation takes a platform-agnostic approach. Reference implementations targeting specific platforms are provided in informative annexes.

## Stakeholder Relationships

- ISVs supply licensed software to customer organisations, directly or through SIs.
- SIs integrate ISV software into customer environments and are accountable for deployment quality and operational continuity.
- Customer organisations operate the resulting systems and bear the commercial and operational consequences of licensing decisions.
- Platform providers supply the infrastructure and identity services on which licensing operations depend.
- Industry bodies govern the framework within which all parties collaborate.

## Scope of This Section

This section defines stakeholder categories at the group level.

Individual perspectives are addressed in Section 02. Use cases are defined in Section 03. Derived requirement themes are summarised in Section 04.
