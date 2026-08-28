# 11. Canonical Data Model

## Purpose

This chapter defines the canonical data model structure of the Dynamic Software Licensing best practices.

Its purpose is to organize the main objects and data concepts used across the best practices in a consistent and implementation-oriented way.

## Role Within the Best Practices

The DSL best practices depend on a stable vocabulary not only for architecture and behavior, but also for the objects that move through the system.

This chapter provides the structured home for those objects and supports consistency across:
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
- license envelope.

This chapter organizes those objects coherently.

## Scope of This Chapter

This chapter defines the major canonical objects used by the best practices. It focuses on
structure and interpretation rather than vendor-specific payload detail.

## Structure of This Chapter

This chapter is organized into the following subchapters:

### 01. Lease Object
Defines the main lease-related object structure.

### 02. Entitlement Object
Defines the object structure representing entitlement state and granted rights.

### 03. Policy Object
Defines the object structure representing policy-driven behavior.

### 04. Usage Event Object
Defines the object structure used for metering or usage reporting.

### 05. Token Claims Object
Defines the structure of claims carried in signed tokens.

### 06. Identity Evidence Object
Defines the object structure used to express workload identity evidence.

### 07. License Envelope Object
Defines the object structure used to carry vendor-specific licensing information in a standardized container.

## Relationship to Other Chapters

This chapter is closely related to:
- terminology,
- the reference model,
- normative requirements,
- the canonical API model,
- the security and trust framework,
- schemas and related annexes.

It is the main reference point for shared object definitions in the best practices.

## Chapter Positioning

This chapter serves as the shared data-model anchor for the review draft.

It is reviewed for consistency of object boundaries, naming, and alignment with the
canonical API model, schemas, and security assumptions.
