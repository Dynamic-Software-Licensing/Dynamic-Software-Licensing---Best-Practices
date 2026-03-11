# Dynamic Software Licensing

An IABM initiative for modern software licensing in broadcast and media workflows.

## Document Purpose

This directory contains the main body of the Dynamic Software Licensing best practices.

The best-practices document is intended to provide a structured, implementation-oriented framework for modern software licensing in broadcast and media workflows. It is not a formal standard, but it is deliberately organized in a standard-like way to support consistency, interoperability, and practical adoption across the industry.

## How to Use This Directory

Each top-level chapter is represented as its own folder.

Within each chapter folder:
- `00-index.md` defines the purpose, scope, and editorial intent of the chapter,
- numbered subchapter files define the detailed structure and working content of that chapter.

This approach is intended to:
- keep the document easy to navigate in GitHub,
- support collaborative drafting in smaller sections,
- make larger chapters easier to review and expand,
- preserve a consistent chapter and subchapter structure.

## Main Chapters

### 00. Status of this Document
Folder: `00-status-of-this-document/`

Defines the status, intended role, maturity, and interpretation of the best practices.

### 01. Introduction
Folder: `01-introduction/`

Explains the industry context, current licensing challenges, and the motivation behind the Dynamic Software Licensing initiative.

### 02. Scope
Folder: `02-scope/`

Defines what the best practices covers, what it excludes, and who it is intended for.

### 03. Conventions and Normative Language
Folder: `03-conventions-and-normative-language/`

Defines writing conventions, interpretation guidance, and the use of normative language such as MUST, SHOULD, and MAY.

### 04. Terminology and Abbreviations
Folder: `04-terminology-and-abbreviations/`

Defines the controlled vocabulary used throughout the best practices, including architecture terms, license and policy terms, operational terms, and abbreviations.

### 05. Stakeholders, Use Cases and Requirements
Folder: `05-stakeholders-use-cases-and-requirements/`

Captures the main stakeholder groups, relevant personas, core use case classes, and the requirement themes derived from them.

This chapter also includes workflow definitions used to derive system requirements.

### 06. Design Principles
Folder: `06-design-principles/`

Defines the core design principles of the DSL best practices, including platform-agnostic and implementation-oriented guidance.

### 07. Reference Model
Folder: `07-reference-model/`

Describes the conceptual and functional architecture of the proposed licensing model, including planes, components, trust relationships, and responsibilities.

### 08. Conformance and Profiles
Folder: `08-conformance-and-profiles/`

Defines conformance targets, implementation profiles, and staged adoption models.

### 09. Normative Requirements
Folder: `09-normative-requirements/`

Contains the main implementation-oriented requirements of the best practices, including identity, policy, API, metering, license modality, security, operational, and integration requirements.

### 10. Canonical API Model
Folder: `10-canonical-api-model/`

Documents the core API interaction model, including issue, renew, move or reissue, revoke, usage recording, key discovery, and error handling.

### 11. Canonical Data Model
Folder: `11-canonical-data-model/`

Defines the main data structures used by the best practices, including lease, entitlement, policy, usage, token claims, identity evidence, and related objects.

### 12. Security and Trust Framework
Folder: `12-security-and-trust-framework/`

Describes the security objectives, threat model, trust assumptions, controls, audit expectations, and offline or grace-related considerations.

### 13. Operational and Deployment Profiles
Folder: `13-operational-and-deployment-profiles/`

Describes operational patterns such as 24/7, event-driven, test, AI-related, hybrid, and disaster recovery-oriented deployment models.

### 14. Migration and Transition
Folder: `14-migration-and-transition/`

Provides the structure for moving from legacy licensing approaches to the DSL target model through staged transition and adoption.

### 15. Governance and Future Work
Folder: `15-governance-and-future-work/`

Captures future development areas, governance considerations, open issues, and longer-term evolution topics for the best practices.

## Chapter Status Overview

Current chapter drafting status (as defined in `GOVERNANCE.md`):

| Chapter | Status | Editorial maturity | Normative readiness |
|---|---|---|---|
| 00. Status of this Document | Working Draft | outline | not started |
| 01. Introduction | Working Draft | outline | not started |
| 02. Scope | Working Draft | outline | not started |
| 03. Conventions and Normative Language | Working Draft | outline | not started |
| 04. Terminology and Abbreviations | Working Draft | outline | not started |
| 05. Stakeholders, Use Cases and Requirements | Working Draft | outline | not started |
| 06. Design Principles | Working Draft | outline | not started |
| 07. Reference Model | Working Draft | outline | not started |
| 08. Conformance and Profiles | Working Draft | outline | not started |
| 09. Normative Requirements | Working Draft | outline | not started |
| 10. Canonical API Model | Working Draft | outline | not started |
| 11. Canonical Data Model | Working Draft | outline | not started |
| 12. Security and Trust Framework | Working Draft | outline | not started |
| 13. Operational and Deployment Profiles | Working Draft | outline | not started |
| 14. Migration and Transition | Working Draft | outline | not started |
| 15. Governance and Future Work | Working Draft | outline | not started |

## Relationship to Annexes

This directory contains the main best practices text.

Supporting material is located outside this directory:
- `annexes/normative/` for normative supporting annexes,
- `annexes/informative/` for examples, mappings, FAQs, and reference architectures.

## Current Drafting Note

At the current stage, this structure is primarily intended to organize the drafting process.

The immediate objective is to:
- stabilize the chapter structure,
- define content boundaries,
- align terminology,
- prepare the best practices for iterative expansion.

Detailed wording and final requirement language will be refined over time.
