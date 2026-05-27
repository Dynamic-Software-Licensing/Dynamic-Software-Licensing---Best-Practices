# 02.03. Intended Audience

## Who This Document Is Written For

The DSL best practices are written for a broad technical and operational audience across the broadcast and media technology industry. Different parts of the document will be more directly relevant to some groups than others, but the framework as a whole is intended to be readable and useful across the following stakeholder groups.

The audience framing in this section is intentionally aligned with the stakeholder groups and persona lenses formalized later in Section 5.1 and Section 5.2. This keeps scope language and role expectations consistent across the document.

## Manufacturers and Independent Software Vendors

Software vendors who develop products used in broadcast and media production environments are a primary audience. For manufacturers, the best practices define what a conformant licensing interface looks like, what operations it must support, and how it should integrate with customer infrastructure.

Vendors who implement the DSL framework can expect their licensing interfaces to work consistently across the range of customer environments that have adopted the same framework — reducing the per-customer integration burden significantly.

## Broadcasters and Media Organizations

Operators who license software from multiple vendors are a central beneficiary of the DSL framework. For broadcasters and media organizations, the best practices define what they should be able to expect from a conformant licensing implementation: automation support, observability, portability, and operational predictability.

This audience includes both technical operations teams and the procurement and finance stakeholders who need visibility into software costs and consumption.

## System Integrators

System integrators who design and deploy multi-vendor production environments need a shared foundation for how licensing works across the systems they build. The DSL best practices provide that foundation. Integrators can use the framework to define consistent integration patterns, avoid vendor-specific workarounds, and deliver solutions where the licensing layer does not become a bottleneck.

## Architects and Platform Designers

Platform architects who design cloud-based, hybrid, or on-premises production infrastructure need to understand how licensing fits into the infrastructure model. The best practices define licensing as a platform component — one that must be designed for, not bolted on. This audience will find the reference model, API contracts, and conformance guidance most directly relevant.

## Operations and Engineering Teams

Engineers responsible for deploying, operating, and maintaining production environments are a practical audience for much of the normative content. Concepts such as lease lifecycle management, workload identity binding, usage recording, and observability are directly applicable to day-to-day operational work.

## Finance and Procurement Stakeholders

Finance and procurement teams who manage software vendor relationships and operational cost attribution benefit from the visibility that a conformant DSL implementation provides. The observability and usage-recording requirements in the best practices are designed to produce the data these teams need — cost attribution by workload, event, or project; consumption trend visibility; and alignment between contracted entitlements and actual usage.

## Security and Compliance Stakeholders

Security architects and compliance teams have a direct interest in how licenses are bound, how access to licensing APIs is controlled, and how audit trails are produced. The best practices treat security as a structural requirement rather than an add-on, and the trust and security framework chapters are written with this audience in mind.
