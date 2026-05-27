# 02.02. Out of Scope

## What These Best Practices Do Not Cover

The following areas are explicitly outside the scope of the DSL best practices. They may be referenced where useful for context, but they are not the subject of normative guidance in this document.

Maintaining clear out-of-scope boundaries is important for the integrity of the best practices. Without them, the document risks becoming a general-purpose integration guide rather than a focused framework for the licensing layer itself.

## A New Licensing Model, Not a Wrapper Around Existing Ones

The DSL best practices define a new approach to software licensing. They do not describe how to integrate, extend, or federate existing proprietary licensing systems.

This distinction is fundamental. The goal is not to build a compatibility layer on top of current vendor-specific licensing mechanisms. It is to define what a modern, interoperable licensing model should look like when built from the ground up for software-defined and cloud-native environments.

Organizations implementing the DSL framework are expected to adopt the target model. Migration guidance is provided to support the transition from legacy approaches, but the legacy approaches themselves are not in scope as reference models or design inputs.

## The Media Functions Themselves

The best practices address the licensing layer. The software products and media functions (sometimes referred to as media services in deployment documentation) that consume licenses — transcoders, graphics engines, ingest systems, quality control tools, playout systems, and similar applications — are considered only as consumers of the licensing API. Their internal design, configuration, and operation are outside the scope of this document.

## ERP, CRM, and Financial System Integration

The DSL framework defines how licensing data can be made available for billing and cost attribution purposes. It does not define how that data integrates with customer or vendor ERP systems, CRM platforms, or financial management tools.

These integrations are organization-specific and commercially sensitive. They fall outside the boundary of a vendor-neutral best practices document.

## Legal Contract Wording

The best practices do not contain or define legal license agreements, terms of use, or contractual language. The framework operates at the technical and operational level. Commercial and legal terms remain the responsibility of the contracting parties.

## Commercial Price Lists and Licensing Economics

Pricing models, rate cards, and commercial licensing structures are outside the scope of this document. The best practices define the mechanisms by which usage is tracked and entitlements are enforced. How that usage is priced is a commercial decision, not a technical one.

## Vendor-Specific Product Packaging

The DSL framework is designed to be vendor-neutral. It does not define how any specific vendor should package, version, or bundle their software products for licensing purposes. Product packaging remains a vendor-internal concern.

## Formal Certification Procedures

The best practices do not establish a formal certification scheme, test suite, or accreditation process. Conformance guidance is provided to help implementors understand what the framework requires, but this is not a certification program.

## Platform-Specific Implementation Detail

Where implementation detail is necessary to illustrate a concept, it is provided in informative annexes rather than in the main best practices. The core document is intentionally platform-agnostic and implementation-neutral.

AWS-specific, Azure-specific, GCP-specific, or other cloud-provider-specific implementation patterns belong in informative annexes. They do not belong in the normative body of the best practices.

Likewise, on-premises and hybrid deployment examples may be used for illustration, but they must not alter or narrow the normative requirements of the platform-agnostic DSL model.
