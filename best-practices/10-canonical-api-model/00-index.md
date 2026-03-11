# 10. Canonical API Model

## Chapter Status

- Status: Working Draft
- Editorial maturity: outline
- Normative readiness: not started
- Open drafting points: yes

## Purpose

This chapter defines the canonical API structure of the Dynamic Software Licensing best practices.

Its purpose is to organize the core interaction model for licensing workflows in a way that is implementation-oriented, reusable, and consistent across the best practices.

## Role Within the Best Practices

The DSL material already treats API-based interaction as a central principle. Open, documented interfaces are one of the recurring foundations of the proposed licensing model. :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21}

This chapter translates that principle into a structured API view.

## Basis for This Chapter

The current DSL drafts already describe recurring operations such as:
- issue,
- renew,
- move or reissue,
- revoke,
- usage recording,
- public key discovery,
- related request and response patterns. :contentReference[oaicite:22]{index=22} :contentReference[oaicite:23]{index=23}

This chapter should provide the canonical structure for those operations.

## Scope of This Chapter

This chapter is intended to define:
- the overall API interaction model,
- the main operation types,
- the relationship between operations,
- the structure of related behavior such as key discovery and error handling.

It should not yet become a vendor-specific API manual.

## Structure of This Chapter

This chapter is organized into the following subchapters:

### 01. Overview
Defines the overall purpose and interaction model of the canonical API.

This section should explain how the API fits into the broader DSL architecture.

### 02. Issue
Defines the initial license issuance interaction.

This section should describe the purpose and role of the first-run acquisition flow.

### 03. Renew
Defines the renewal interaction.

This section should describe how active runtime continuity is maintained through renewal behavior.

### 04. Move or Reissue
Defines the move or reissue interaction.

This section should describe how failover, cutover, and transfer-oriented scenarios are handled in the DSL model.

### 05. Revoke
Defines the revocation interaction.

This section should describe how administrative or policy-driven invalidation is reflected in the API model.

### 06. Usage Record
Defines the usage reporting interaction.

This section should describe how metering-related events enter the system.

### 07. JWKS and Public Keys
Defines the key-discovery aspect of the API model.

This section should describe how token validation material is published and consumed.

### 08. Error Model
Defines the structure of API error handling.

This section should describe how failures, rejected requests, and non-successful outcomes should be expressed consistently.

## Relationship to Other Chapters

This chapter is closely related to:
- the reference model,
- normative requirements,
- the canonical data model,
- the security and trust framework,
- API contracts in the annexes.

It should serve as the main API-oriented interpretation layer of the best practices.

## Editorial Guidance

At the current stage, contributors should focus on:
- operation structure,
- terminology consistency,
- stable naming of flows,
- clear separation between conceptual API behavior and detailed schema examples.

Detailed payload definitions can be placed in later subchapters or annexes.

## Possible Future Expansion

If needed, this chapter may later include:
- request/response flow diagrams,
- interaction timing notes,
- idempotency guidance,
- error category tables,
- profile-specific API behavior.

## Drafting Note

At the current stage, this chapter should provide the structural home for the canonical licensing interactions of the DSL best practices.

Its immediate purpose is to create a stable API chapter layout before detailed contracts and schemas are refined.
