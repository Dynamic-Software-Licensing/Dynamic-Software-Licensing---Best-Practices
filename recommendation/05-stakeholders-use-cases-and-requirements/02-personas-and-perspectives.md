# 05.02 Personas and Perspectives

## Purpose

This section captures the perspectives of specific roles within and across the stakeholder groups defined in Section 01.

Each persona represents a recurring role type encountered across the broadcast and media industry. The concerns described reflect patterns identified across multiple organisations.

## Customer-Side Personas

### Director of Engineering

Responsible for the technical reliability and scalability of production environments.

Principal concerns:

- Ability to operate a redundant production environment using a single license across primary and backup instances in a hot/hot configuration.
- Predictable licensing spend forecastable in advance of production commitments.
- Ability to burst licensed capacity in response to demand increases without advance vendor intervention.
- Advance notification of license expiry sufficient to avoid interruption during live production.
- Support for backup and restore without requiring license re-activation.

### Finance Officer

Responsible for cost control, budget allocation, and licensing compliance.

Principal concerns:

- Visibility into current licensing costs and ability to forecast future spend.
- A cost model accommodating variable consumption patterns: hourly, daily, monthly, and annual.
- Audit capability to identify unused, over-provisioned, or non-compliant licensing positions.
- Where cloud commitments exist, ability to allocate licensing costs against those commitments.

### License Manager

Responsible for day-to-day administration of software licenses across the organisation.

Principal concerns:

- Clear visibility into the current licensing position: licenses held, allocation status, remaining capacity.
- Informed decision-making on licensing model selection across vendors.
- Ability to manage license allocation, release, and renewal without requiring vendor intervention for routine operations.

### CTO and Technology Leadership

Responsible for platform strategy, vendor evaluation, and long-term technical direction.

Principal concerns:

- Ability to evaluate and adopt cloud-based solutions without hardware licensing dependencies.
- Reduction of integration friction when combining best-of-breed software from multiple vendors.
- A licensing framework that does not create vendor lock-in or constrain platform flexibility.

### Operations Team

Responsible for day-to-day deployment and operation of production systems.

Principal concerns:

- Ability to identify available licenses and release licenses from failed or decommissioned instances.
- Access to test and development licenses in non-production environments without consuming production entitlements.
- Ability to deploy resources via IaC including licensing steps as a standard deployment component.
- Advance warning of license expiry aligned with production planning cycles.

### Broadcast Director and Broadcast Engineer

Operates at the production layer. Not responsible for licensing administration, but directly affected by licensing failures during live production.

Principal concerns:

- Ability to use cloud resources as backup to on-premises systems with licenses available across both.
- Ability to use floating licenses across multiple virtual production control rooms.
- Ability to dynamically manage licenses during production in response to failures or burst requirements.
- Minimal licensing overhead during live operation.

### Security Team

Responsible for ensuring third-party software components meet organisational security and compliance requirements.

Principal concerns:

- Confidence that licensing solutions meet applicable security and compliance standards prior to integration.
- Ability to license software without requiring vendors to have direct access to production resources.
- Full auditability of licensing operations to support compliance reviews and incident investigation.

### Procurement

Responsible for the commercial relationship with software vendors.

Principal concerns:

- Clear visibility of pricing tiers and their relationship to service level commitments.
- Ability to compare licensing offerings across vendors on a consistent basis.

## Vendor-Side Personas

### Independent Software Vendor (ISV)

Builds and distributes licensed software products.

Principal concerns:

- Revenue proportional to actual usage, without gaps that lead to under-collection or friction that discourages legitimate use.
- Licensing mechanisms that are secure and resistant to misuse without creating unreasonable operational burden for customers or integrators.
- Support for a range of integration approaches, from manual configuration to fully automated IaC-driven deployment.

## Integration-Side Personas

### SI Developer

Implements deployment and integration solutions that include licensed software.

Principal concerns:

- A well-defined, documented mechanism for including license activation as part of IaC deployments using tools such as Terraform, OpenTofu, or CloudFormation.
- Standard programmatic interfaces callable from deployment scripts and automation pipelines without manual or interactive activation steps.

## Summary of Recurring Concerns

The following concern patterns recur across all personas:

- **Automation**: licensing cannot be included in automated deployment workflows.
- **Resilience**: licensing mechanisms that bind to specific instances or require vendor intervention for failover are incompatible with production continuity requirements.
- **Transparency**: real-time visibility into licensing position, cost, and usage is absent.
- **Portability**: licenses bound to hardware identifiers prevent cloud adoption and hybrid operation.
- **Proportionality**: licensing cost models that do not align with actual consumption create commercial friction.

These patterns are the basis for the requirement themes defined in Section 04.

