# 11. Canonical Data Model

## Chapter Status

- Status: Working Draft
- Editorial maturity: outline
- Normative readiness: not started
- Open drafting points: yes

## Purpose

This chapter defines the canonical data model structure of the Dynamic Software Licensing best practices.

Its purpose is to organize the main objects and data concepts used across the best practices in a consistent and implementation-oriented way.

## Role Within the Best Practices

The DSL best practices depend on a stable vocabulary not only for architecture and behavior, but also for the objects that move through the system.

This chapter provides the structured home for those objects and should support consistency across:
- the reference model,
- API chapters,
- requirement chapters,
- security and operational behavior,
- schemas and annexes.

## Basis for This Chapter

The current DSL drafts already refer to recurring objects and structured concepts such as:
- lease token,
- entitlement,
- policy,
- usage events,
- identity evidence,
- token claims,
- license envelope. :contentReference[oaicite:24]{index=24} :contentReference[oaicite:25]{index=25} :contentReference[oaicite:26]{index=26}

This chapter should organize those objects coherently.

## Scope of This Chapter

This chapter is intended to define the major canonical objects used by the best practices.

It should focus on structure and interpretation rather than vendor-specific payload detail.

## Structure of This Chapter

This chapter is organized into the following subchapters:

### 01. Lease Object
Defines the main lease-related object structure.

This section should describe the core data needed to represent an active or issued license lease.

### 02. Entitlement Object
Defines the object structure representing entitlement state and granted rights.

This section should describe how authorized usage scope and related policy context are represented.

### 03. Policy Object
Defines the object structure representing policy-driven behavior.

This section should include the conceptual home for renewal, grace, exhaustion, alerting, and related control settings.

### 04. Usage Event Object
Defines the object structure used for metering or usage reporting.

This section should describe the canonical representation of usage events entering the system.

### 05. Token Claims Object
Defines the structure of claims carried in signed tokens.

This section should support consistent understanding of token-level information used in runtime validation.

### 06. Identity Evidence Object
Defines the object structure used to express workload identity evidence.

This section should support the best practices’s trust and binding model.

### 07. License Envelope Object
Defines the object structure used to carry vendor-specific licensing information in a standardized container.

This section should help bridge generic and vendor-specific representations where needed.

## Relationship to Other Chapters

This chapter is closely related to:
- terminology,
- the reference model,
- normative requirements,
- the canonical API model,
- the security and trust framework,
- schemas and related annexes.

It should become the main reference point for shared object definitions in the best practices.

## Editorial Guidance

At the current stage, contributors should focus on:
- stable object boundaries,
- naming consistency,
- conceptual clarity,
- separation between canonical objects and implementation-specific payload examples.

Detailed schema formalization can be added later.

## Possible Future Expansion

If needed, this chapter may later include:
- field-level object descriptions,
- object relationship diagrams,
- lifecycle associations,
- schema references,
- normative constraints on object fields.

## Drafting Note

At the current stage, this chapter should serve as the data-model anchor of the DSL best practices.

Its immediate purpose is to provide a stable structural home for the main object types used throughout the repository.
