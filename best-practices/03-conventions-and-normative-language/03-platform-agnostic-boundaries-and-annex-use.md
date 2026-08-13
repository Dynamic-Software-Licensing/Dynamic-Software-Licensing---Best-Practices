# 03.03. Platform-Agnostic Boundaries and Annex Use

## Purpose

This section defines how the core best-practices document remains platform-agnostic while still
allowing concrete examples, deployment references, and implementation-specific material to be
included in a controlled way.

## Core Document Boundary

The main body of the best practices is written to be reusable across vendors, deployment
models, and operational environments. Its primary role is to define the conceptual model,
requirement structure, security posture, API interpretation, and shared data semantics.

For that reason, the core document avoids becoming:
- vendor-specific,
- cloud-provider-specific,
- tied to one product packaging model,
- overloaded with examples that narrow the interpretation of the general model.

## When Material Belongs in the Core Text

Material belongs in the core document when it:
- defines reusable concepts,
- establishes interpretation rules,
- supports cross-vendor alignment,
- expresses requirements or conformance-relevant guidance,
- clarifies common lifecycle, trust, or policy behavior.

## When Material Belongs in an Annex

Material belongs in an annex when it is primarily:
- platform-specific,
- deployment-profile-specific,
- example-oriented,
- mapping-oriented,
- explanatory support that would interrupt the flow of the core text.

Normative annexes may be used when consistent interpretation needs structured supporting
material. Informative annexes are used for examples, reference architectures,
walkthroughs, mappings, and FAQ-style support.

## Handling Platform-Specific References

Platform-specific references are allowed where they improve clarity, but they are contained
deliberately.

In practice this means:
- the main text describes the generic rule first,
- platform examples are separated clearly from the generic rule,
- examples do not redefine the general model,
- annexes carry the main burden of technology-specific elaboration.

The AWS reference architecture annex is an example of this separation: it interprets the model
for one concrete platform without redefining the platform-neutral baseline.

## Annex Selection Logic

The annex boundary is applied consistently:
- if the material is required for consistent interpretation across implementations, consider a
  normative annex,
- if the material is illustrative, comparative, or example-driven, use an informative annex,
- if the material is essential to understanding the model itself, keep it in the core document.

This prevents the main document from becoming either too abstract to implement or too specific
to generalize.

## Section Positioning

This section defines the boundary discipline that keeps the best practices reusable and
maintainable. It is used when deciding whether new content belongs in a chapter of the main
document or in a supporting annex.
