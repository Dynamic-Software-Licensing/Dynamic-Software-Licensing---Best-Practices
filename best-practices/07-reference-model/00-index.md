# 07. Reference Model

## Chapter Status

- Status: Working Draft
- Editorial maturity: outline
- Normative readiness: not started
- Open drafting points: yes

## Purpose

This chapter defines the conceptual and functional reference model of the Dynamic Software Licensing best practices.

Its purpose is to describe the main structural elements of the proposed licensing model and the relationships between them.

## Role Within the Best Practices

The reference model is one of the central chapters of the best practices.

It translates the design principles into an architectural view that can be used to explain:
- how the licensing model is structured,
- which components and planes exist,
- how responsibilities are separated,
- how trust and interaction flow through the system.

## Architectural Basis

The current DSL material already distinguishes between major architectural areas such as:
- the Control Plane,
- the Workspace Plane,
- an End User Portal,
- associated components such as a Broker or License Agent, SDK integration, keys, usage services, and analytics. :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}

This chapter should organize that model into a consistent reference structure.

## Scope of This Chapter

This chapter is intended to describe:
- the conceptual model,
- the functional components,
- the major planes,
- trust relationships,
- responsibility boundaries.

It should not yet become a platform-specific implementation chapter.

## Structure of This Chapter

This chapter is organized into the following subchapters:

### 01. Conceptual Model
Defines the abstract concepts and their relationships.

This section should describe the high-level DSL model in conceptual terms before moving into implementation detail.

### 02. Functional Components
Defines the main logical components of the licensing model.

This section should identify the core services and functional building blocks that appear across implementations.

### 03. Control Plane
Defines the responsibilities and characteristics of the Control Plane.

This section should describe the central services for entitlements, leases, keys, usage, analytics, and policy handling.

### 04. Workspace Plane
Defines the responsibilities and characteristics of the Workspace Plane.

This section should describe where applications run and how the broker, SDK, identities, and local token validation fit into the model.

### 05. End User Portal
Defines the role of an end-user-facing management interface.

This section should describe aggregated visibility, multi-vendor views, self-service capabilities, and customer-facing operational controls where applicable.

### 06. Trust Model
Defines how trust is established and maintained across the system.

This section should describe binding, identity evidence, signed tokens, validation assumptions, and related trust boundaries.

### 07. Responsibility Model
Defines which participant or component is responsible for which aspect of the model.

This section should help clarify vendor, customer, broker, control-plane, and operational responsibilities.

## Relationship to Other Chapters

This chapter informs:
- conformance and profiles,
- normative requirements,
- canonical API and data models,
- security and operational chapters,
- relevant annexes and diagrams.

It should act as the main architectural reference point for the rest of the best practices.

## Editorial Guidance

At the current stage, contributors should focus on:
- stable structure,
- clear separation of concerns,
- consistent use of terminology,
- platform-neutral description of the model.

Implementation examples should be reserved for annexes unless they are needed for conceptual clarity.

## Possible Future Expansion

If needed, this chapter may later include:
- explicit component relationship diagrams,
- request and trust flow summaries,
- responsibility tables,
- state and lifecycle cross-references.

## Drafting Note

At the current stage, this chapter should serve as the primary architectural overview of the Dynamic Software Licensing best practices.

Its immediate purpose is to stabilize the model that later API, requirement, security, and migration chapters will build upon.
