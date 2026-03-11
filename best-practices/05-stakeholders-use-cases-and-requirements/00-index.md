# 05. Stakeholders, Use Cases and Requirements

## Chapter Status

- Status: Working Draft
- Editorial maturity: outline
- Normative readiness: not started
- Open drafting points: yes

## Purpose

This chapter defines the stakeholder landscape, the principal operational use case classes, and the requirement themes derived from them. It establishes a traceable statement of need for the best practices and provides the rationale against which later normative choices can be evaluated.

## Role Within the Best Practices

This chapter provides the bridge between:
- who is affected,
- what situations they operate in,
- what problems they face,
- what capabilities the best practices needs to support.

## Scope of This Chapter

This chapter covers:
- stakeholder groups,
- personas and perspectives,
- recurring use case classes,
- requirement themes derived from those perspectives and scenarios.

It does not define normative requirements. It explains why those requirements exist and provides context for later normative chapters.

## Structure of This Chapter

This chapter is organized into the following subchapters:

### 01. Stakeholder Groups

Defines the stakeholder categories addressed by the best practices: customer organisations, ISVs, system integrators, industry bodies, and platform providers.

### 02. Personas and Perspectives

Captures the operational, technical, and commercial concerns of specific roles: engineering leadership, finance, operations, security, procurement, ISVs, and SI developers.

### 03. Use Case Classes

Defines recurring operational patterns: 24/7 operations, frequent and infrequent event-driven production, test and validation environments, and AI-powered or outcome-based service scenarios.

### 04. Derived Requirement Themes

Summarises the recurring requirement patterns that emerge from the stakeholder and use case analysis: automation, portability, transparency, security, observability, self-service, usage-based metering, and continuity under failure.

## Relationship to Other Chapters

This chapter informs:
- the design principles chapter,
- the reference model,
- conformance and profiles,
- normative requirements,
- operational and migration chapters.

It provides the rationale for many of the later design and requirement decisions.

In particular, this chapter should be read as the justification layer for later statements on:
- control-plane and workspace-plane responsibilities,
- lifecycle operations for issue, renew, reissue, revoke, and inspect,
- entitlement and lease handling,
- observability and audit expectations,
- commercial model flexibility and profile differentiation.

## Editorial Guidance

At the current stage, this chapter focuses on organizing perspectives and patterns rather than over-specifying detail.

Contributors should aim to:
- keep stakeholder categories distinct,
- avoid duplicating the same concern across multiple personas without explanation,
- connect use cases to requirement themes clearly,
- preserve a practical industry view rather than an abstract one,
- keep the main text platform-agnostic.

Where examples are used, they should illustrate classes of concern rather than vendor-specific implementation choices.

## Possible Future Expansion

If needed, this chapter may later include:
- stakeholder maps,
- persona-to-requirement traceability,
- use-case-to-profile mapping,
- summary tables linking pain points to best practices areas.

Additional future expansion may include:
- cross-references to specific lifecycle operations and canonical model elements,
- a chapter-internal traceability structure linking Sections 01 to 04 more explicitly,
- a concise summary view for readers seeking a non-detailed overview.

## Drafting Note

At the current stage, this chapter serves as the needs and context layer of the best practices.

Its immediate purpose is to make clear which industry problems the DSL initiative is intended to address and why later requirements and architectural choices matter.

This chapter is descriptive and analytical in nature. Later chapters may derive normative statements from it, but this chapter itself primarily establishes scope, relevance, and traceability.

## Drafting To-Do

The following items should be considered in later drafting iterations:
- verify that all four subchapters remain aligned in scope and terminology,
- review whether cross-references to later chapters should be made more explicit,
- confirm whether any content currently in this chapter should later move into annex material,
- assess whether a short summary or overview table should be added at chapter level.
