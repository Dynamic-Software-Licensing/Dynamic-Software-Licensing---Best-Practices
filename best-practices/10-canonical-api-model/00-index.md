# 10. Canonical API Model

## Purpose

This chapter defines the canonical API structure of the Dynamic Software Licensing best practices.

Its purpose is to organize the core interaction model for licensing workflows in a way that is implementation-oriented, reusable, and consistent across the best practices.

## Role Within the Best Practices

The DSL material already treats API-based interaction as a central principle. Open,
documented interfaces are one of the recurring foundations of the proposed licensing model.

This chapter translates that principle into a structured API view.

## Basis for This Chapter

The current DSL drafts already describe recurring operations such as:
- issue,
- renew,
- move or reissue,
- revoke,
- usage recording,
- public key discovery,
- related request and response patterns.

This chapter provides the canonical structure for those operations.

## Scope of This Chapter

This chapter defines:
- the overall API interaction model,
- the main operation types,
- the relationship between operations,
- the structure of related behavior such as key discovery and error handling.

It is not a vendor-specific API manual.

## Structure of This Chapter

This chapter is organized into the following subchapters:

### 01. Overview
Defines the overall purpose and interaction model of the canonical API.

### 02. Issue
Defines the initial license issuance interaction.

### 03. Renew
Defines the renewal interaction.

### 04. Move or Reissue
Defines the move or reissue interaction.

### 05. Revoke
Defines the revocation interaction.

### 06. Usage Record
Defines the usage reporting interaction.

### 07. JWKS and Public Keys
Defines the key-discovery aspect of the API model.

### 08. Error Model
Defines the structure of API error handling.

## Relationship to Other Chapters

This chapter is closely related to:
- the reference model,
- normative requirements,
- the canonical data model,
- the security and trust framework,
- API contracts in the annexes.

It serves as the main API-oriented interpretation layer of the best practices.

## Chapter Positioning

This chapter provides the API-oriented interpretation layer for the DSL best practices.
It turns the lifecycle operations, trust constraints, and data-model concepts from adjacent
chapters into a coherent interaction model with consistent endpoints, request patterns,
authentication expectations, error semantics, and key-discovery behavior.

The chapter is intentionally implementation-oriented but remains vendor-neutral. It defines
the canonical structure and standards profile for API interactions while leaving deployment-
specific realization details and concrete contracts to annexes, schemas, and profile-specific
guidance.
