# 07. Reference Model

## Chapter Status

- Status: Reviewed Draft
- Editorial maturity: developed draft
- Normative readiness: informative only
- Open drafting points: no

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
- associated components such as a License Agent (Broker), SDK integration, keys, usage services, and analytics.

This chapter organizes that model into a consistent reference structure.

## Scope of This Chapter

This chapter describes:
- the conceptual model,
- the functional components,
- the major planes,
- trust relationships,
- responsibility boundaries.

It remains a platform-neutral reference chapter rather than a platform-specific implementation chapter.

## Structure of This Chapter

This chapter is organized into the following subchapters:

### 01. Conceptual Model
Defines the abstract concepts and their relationships.

### 02. Functional Components
Defines the main logical components of the licensing model.

### 03. Control Plane
Defines the responsibilities and characteristics of the Control Plane.

### 04. Workspace Plane
Defines the responsibilities and characteristics of the Workspace Plane.

### 05. End User Portal
Defines the role of an end-user-facing management interface.

### 06. Trust Model
Defines how trust is established and maintained across the system.

### 07. Responsibility Model
Defines which participant or component is responsible for which aspect of the model.

## Relationship to Other Chapters

This chapter informs:
- conformance and profiles,
- normative requirements,
- canonical API and data models,
- security and operational chapters,
- relevant annexes and diagrams.

It acts as the main architectural reference point for the rest of the best practices.

## Chapter Positioning

This chapter serves as the primary architectural overview for the review draft.

It is used during review as the architectural reference point for API behavior, trust
boundaries, operational responsibilities, and chapter-to-chapter consistency.
