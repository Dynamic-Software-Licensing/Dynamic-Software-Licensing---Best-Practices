# Changelog

All notable changes to the Dynamic Software Licensing repository should be documented in this file.

This changelog is used to track the evolution of the DSL best practices as an IAMT initiative, including structural, editorial, and content-related changes.

The format is intentionally lightweight at this stage and is primarily intended to support transparency across published baselines and ongoing repository evolution.

## [1.0.0] - 2026-09-07

### Changed

- Added a management summary to the repository README and reused it as dedicated front matter content in the generated PDF
- Separated version information, management summary, change log, and table of contents more clearly in the PDF front matter
- Added lifecycle and sequence diagrams to strengthen visual parity in Annex D and Annex G
- Improved PDF rendering for Markdown lists so bullet lists no longer collapse into inline dash paragraphs
- Improved PDF rendering for inline code inside Markdown tables so long endpoint and path values wrap without overlapping text
- Added consistent PDF header and footer metadata with document title, version, date, and page number on content pages
- Clarified API companion documentation around schema-backed and intentionally Markdown-only model elements
- Aligned the OpenAPI companion and related wording with the current published baseline
- Updated PDF publishing so main tracks the current published release and keeps the latest PDF aligned with official tagged versions
- Integrated the current review-feedback fixes collected on the governance release-readiness branch ahead of the next baseline
- Expanded the FAQ with implementation, migration, security, and onboarding questions for first-time readers
- Removed repeated per-chapter status blocks and centralized status handling in the repository-level guidance and release surfaces
- Promoted the repository baseline from reviewed draft to published best practices version 1.0.0
