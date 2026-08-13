# 05.02. Personas and Perspectives

## Purpose

This section defines role-level perspectives derived from the stakeholder groups in
Section 5.1. It captures objectives, operating constraints, and measurable outcomes
that inform use case classification and requirement-theme derivation.

The persona set is written against a dynamic software licensing target model. It therefore
describes how roles expect the model to behave in operation, sales, delivery, and governance.

## Method and Input Basis

The personas below synthesize:
- stakeholder categories from Section 5.1,
- recurring industry challenges,
- team prework (including Miro workshop material).

Personas are not organization charts. They are decision and concern viewpoints used to
guide later analysis.

## Persona Schema

Each persona is specified using the same structure:
- primary focus,
- licensing perspective,
- success criteria.

This schema is used to keep later mappings to use case classes and requirement themes
consistent.

The schema is intentionally compact. It allows reviewers to compare personas on equal
terms and identify where concerns overlap, conflict, or remain insufficiently represented.
This consistency also improves traceability when persona inputs are transformed into use
case classes and workflow decisions.

## Persona Set

The persona set is intentionally cross-functional. It reflects both technical and commercial
decision authority required for cloud-native licensing adoption.

To avoid customer-only bias, this section explicitly includes supplier-side and integrator-side
decision lenses. This is necessary because portability, interoperability, and lifecycle
automation outcomes depend on both product-side and deployment-side accountability.

In operational reality, several personas may be represented by one person or one team,
especially in smaller organizations. The persona model should therefore be read as a set of
decision lenses rather than a rigid staffing model.

## Customer Organization Personas

## 1. Director of Engineering (Customer Organization)

Primary focus:
- architecture resilience,
- delivery speed,
- operational risk reduction.

Licensing perspective:
- requires licensing behavior compatible with high-availability architectures,
- expects controlled scaling without manual relicensing bottlenecks,
- requires predictable spend boundaries for planning and approvals.

Success criteria:
- no critical workflow interruption caused by license handling,
- licensing behavior compatible with high-availability design.

## 2. Operations and DevOps Engineer (Customer Organization)

Primary focus:
- deployability,
- runtime stability,
- repeatable operations.

Licensing perspective:
- requires automation-friendly issue, renew, move, and release behavior,
- expects licensing operations to be manageable through IaC and CI/CD pipelines,
- requires user- and role-based access control over license allocation and checkout,
- requires visibility into allocations, limits, and expiry state.

Success criteria:
- low manual operational load,
- transparent and recoverable license lifecycle under normal and failure conditions.

## 3. Broadcast Engineer / Production Operator (Customer Organization)

Primary focus:
- production continuity,
- practical flexibility during live operations.

Licensing perspective:
- expects floating and movable license behavior across changing runtimes,
- requires emergency adaptation paths during incident or burst conditions,
- expects minimal licensing friction in time-critical operations.

Success criteria:
- licenses do not block operational decisions during active production.

## 4. Finance and Procurement Lead (Customer Organization)

Primary focus:
- budget predictability,
- cost control,
- contractual clarity.

Licensing perspective:
- requires transparent metering and modality options aligned to actual usage,
- expects clear linkage between usage dimensions and commercial impact,
- requires forecasting inputs across planned and event-driven demand.

Success criteria:
- explainable spend with controllable variance,
- no recurring billing surprises caused by opaque license behavior.

## 5. Security and Compliance Lead (Customer Organization)

Primary focus:
- risk control,
- compliance assurance,
- auditable operations.

Licensing perspective:
- requires secure, least-privilege license interactions,
- requires role-scoped and user-scoped entitlements so teams can restrict access to unnecessary licenses,
- requires auditable lifecycle events and policy alignment,
- avoids workflows that require unnecessary privileged vendor access.

Success criteria:
- license operations are compliant, observable, and reviewable.

## Access Control and Entitlement Segmentation (Cross-Persona)

Beyond technical lifecycle handling, multiple personas require policy-level control over
who can access which license rights and when.

This requirement appears in three recurring patterns:
- user- and role-based entitlement assignment to avoid over-provisioning,
- project or production scoped license pools to separate teams and cost centers,
- temporary access windows for external participants (for example rental or guest teams).

Representative operational scenarios include:
- restricting premium feature licenses to specifically authorized operators,
- allowing studio-rental customers to use only the rights included in their contracted tier,
- enforcing least-privilege defaults while preserving emergency override paths with audit logs.

This cross-persona concern links operational efficiency, security policy, and commercial
packaging. It should therefore be treated as a primary design input for use case and
workflow modeling in Sections 5.3 to 5.5.

## ISV Personas

## 6. ISV Product and Commercial Owner (ISV)

Primary focus:
- product value capture,
- market fit,
- support scalability.

Licensing perspective:
- requires enforceable yet customer-usable entitlement models,
- requires flexibility across customer maturity levels and deployment modes,
- seeks standard interfaces to reduce one-off integration overhead.

Success criteria:
- sustainable revenue protection without blocking customer adoption.

## 7. ISV Licensing Architect (ISV)

Primary focus:
- control-plane design quality,
- lifecycle correctness,
- interoperability and maintainability.

Licensing perspective:
- requires clear and stable lifecycle semantics for issue, renew, move, revoke, and inspect,
- requires identity-aware binding models suitable for elastic runtimes,
- requires cryptographic trust and key-rotation approaches that remain operationally practical.

Success criteria:
- licensing architecture is portable across target environments,
- lifecycle behavior is deterministic and testable under failure and recovery conditions.

## 8. ISV Sales Director (ISV)

Primary focus:
- faster sales cycles,
- higher conversion rates,
- scalable pipeline growth.

Licensing perspective:
- requires clear and easy-to-position commercial packages,
- expects transparent and defensible value metrics for enterprise negotiations,
- requires low-friction onboarding models that reduce pre-sales complexity.

Success criteria:
- reduced time-to-close,
- increased attach rate and expansion revenue across customer segments.

## 9. ISV Partner and Channel Manager (ISV)

Primary focus:
- channel enablement,
- partner revenue growth,
- predictable co-sell operations.

Licensing perspective:
- requires reseller-compatible pricing and entitlement mechanics,
- requires channel-ready visibility for rights, usage, and renewals,
- expects low-dispute alignment between contract terms and operational behavior.

Success criteria:
- partner-led deals scale without recurring licensing disputes,
- channel operations remain commercially and operationally auditable.

## 10. ISV Support and Customer Success Lead (ISV)

Primary focus:
- support scalability,
- operational transparency for customers,
- reduction of avoidable escalation volume.

Licensing perspective:
- requires clear observability signals and support-grade diagnostics,
- requires low-friction remediation paths for entitlement and lease mismatches,
- expects policy and product behavior to be explainable to mixed technical/commercial teams.

Success criteria:
- incident resolution time remains bounded,
- recurring support patterns are reduced through better lifecycle and telemetry design.

## System Integrator Personas

## 11. SI Solution Architect / Integrator (System Integrator)

Primary focus:
- multi-vendor solution delivery,
- deployment repeatability,
- integration reliability.

Licensing perspective:
- requires consistent API and lifecycle semantics across products,
- expects deterministic behavior across cloud and hybrid environments,
- requires clear failure and recovery handling in orchestrated workflows.

Success criteria:
- integration patterns can be reused across projects with low customization overhead.

## 12. SI Delivery and Operations Lead (System Integrator)

Primary focus:
- delivery predictability,
- operational handover quality,
- incident and change governance.

Licensing perspective:
- requires repeatable deployment runbooks that include license lifecycle controls,
- requires clear ownership boundaries for cross-vendor failure handling,
- expects measurable service outcomes for activation latency, renewal reliability, and recovery.

Success criteria:
- projects can be operated in stable mode without recurring licensing exceptions,
- change and incident processes remain effective under peak and failover conditions.

## 13. SI Commercial and Reselling Lead (System Integrator)

Primary focus:
- channel economics and margin sustainability,
- contract alignment across vendor, SI, and customer,
- predictable commercial operations in project and managed-service models.

Licensing perspective:
- requires commercially clear resale and pass-through models,
- requires entitlement and billing data that can be reconciled across all parties,
- expects licensing terms that support both project delivery and recurring service operations.

Success criteria:
- reselling and procurement workflows are operationally simple and auditable,
- commercial disputes are minimized through clear rights, usage, and billing traceability.

## 14. SI Sales and Account Director (System Integrator)

Primary focus:
- faster customer acquisition,
- deal expansion,
- portfolio monetization across services.

Licensing perspective:
- requires licensing offers that can be explained and priced quickly in proposals,
- expects flexible packaging for project-based and managed-service sales motions,
- requires strong commercial traceability to support enterprise procurement reviews.

Success criteria:
- reduced proposal-to-close cycle time,
- higher conversion and expansion rates in SI-led opportunities.

## 15. SI Managed Services Portfolio Lead (System Integrator)

Primary focus:
- profitable managed service operations,
- SLA adherence,
- lifecycle cost control.

Licensing perspective:
- requires lifecycle controls aligned with managed-service operating models,
- expects predictable renewal and entitlement behavior across customer estates,
- requires auditable usage and billing linkage for service reporting.

Success criteria:
- managed-service margins remain stable,
- SLA outcomes are met without recurring licensing escalations.

## Ecosystem and Governance Personas

## 16. Platform SRE / Runtime Reliability Lead (Platform Provider)

Primary focus:
- runtime reliability,
- failure-domain containment,
- observable and recoverable control-plane behavior.

Licensing perspective:
- requires licensing control components to satisfy reliability and recovery objectives,
- expects telemetry, alerting, and health semantics suitable for platform operations,
- requires lifecycle operations to remain robust under scaling, replacement, and rollback.

Success criteria:
- licensing control functions meet reliability targets in production-like conditions,
- platform operations teams can diagnose and recover license-related incidents quickly.

This persona ensures that licensing architecture is operable as part of real platform
operations, not only valid as an application-level concept.

## 17. Industry Standards and Policy Representative (Governance)

Primary focus:
- interoperability alignment,
- terminological consistency,
- sustainable cross-vendor guidance.

Licensing perspective:
- requires lifecycle semantics and terminology that can be interpreted consistently,
- expects traceability from industry pain points to recommended practices,
- requires guidance that supports implementation diversity without semantic drift.

Success criteria:
- cross-vendor interpretations remain compatible,
- standardization artifacts remain stable across drafting iterations.

This persona represents long-term alignment pressure and helps prevent fragmentation of
meaning across implementations.

## Cross-Persona Tensions

The personas above reveal recurring trade-offs:

- protection vs operational agility,
- predictability vs burst flexibility,
- strict control vs low-friction self-service,
- platform neutrality vs deep platform optimization.

An additional recurring tension concerns commercial model design:
- simplicity and predictability vs fine-grained value-based charging.
- OPEX model flexibility (burn-down, pre-pay, post-pay, point-based) vs CAPEX/perpetual procurement consistency.

In practice, organizations often combine several of these models in one account landscape.
This creates additional friction points:
- customer demand for predictable budgeting vs supplier need for usage-linked monetization,
- SI resale simplicity vs mixed vendor contract logic,
- entitlement clarity at runtime vs billing flexibility across tiers and periods.

Supplier and integrator perspectives add two additional recurring tensions:
- product differentiation vs interoperability standardization,
- implementation flexibility vs supportability at scale.

For SI-led delivery models, another recurring tension is visible:
- channel simplicity and resale viability vs high-granularity commercial customization.

These tensions are expected and should be addressed explicitly in Sections 5.3 to 5.5.

The purpose of naming these tensions is to make trade-offs explicit early. Later sections
should treat them as design inputs rather than as unresolved side effects.

## Traceability to Subsequent Sections

This section informs:
- Section 5.3 by grounding recurring use case classes,
- Section 5.4 by exposing recurring requirement themes,
- Section 5.5 by framing workflow decision points and failure paths.

The intent is explicit traceability from stakeholder groups (Section 5.1), to role-level
perspectives (Section 5.2), to scenario and workflow structure (Sections 5.3 to 5.5).

## Section Positioning

This section is descriptive and analytical.
It does not prescribe normative requirement language; it captures role-level viewpoints
that justify later design and requirement choices.
