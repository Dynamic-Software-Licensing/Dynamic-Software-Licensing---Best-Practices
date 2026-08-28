# Changelog

All notable changes to the Dynamic Software Licensing repository should be documented in this file.

This changelog is used to track the evolution of the DSL best practices as an IAMT initiative, including structural, editorial, and content-related changes.

The format is intentionally lightweight at this stage and is primarily intended to support transparency across published baselines and ongoing repository evolution.

## [0.3.0] - 2026-08-28

### Changed

- Added a management summary to the repository README and reused it as dedicated front matter content in the generated PDF
- Separated version information, management summary, change log, and table of contents more clearly in the PDF front matter
- Added lifecycle and sequence diagrams to strengthen visual parity in Annex D and Annex G
- Improved PDF rendering for Markdown lists so bullet lists no longer collapse into inline dash paragraphs
- Improved PDF rendering for inline code inside Markdown tables so long endpoint and path values wrap without overlapping text
- Added consistent PDF header and footer metadata with document title, version, date, and page number on content pages
- Clarified API companion documentation around schema-backed and intentionally Markdown-only model elements
- Aligned the OpenAPI companion and related wording with the current reviewed-draft baseline
- Updated PDF publishing so main tracks the current published release and keeps the latest PDF aligned with official tagged versions
- Integrated the current review-feedback fixes collected on the governance release-readiness branch ahead of the next baseline

## [0.2.0-review-draft] - 2026-08-12

### Changed

- Promoted the main best-practices document from Working Draft to Reviewed Draft status
- Aligned chapter-level status blocks and the central chapter status overview with the current maturity baseline
- Reworked the Governance and Future Work chapter into a substantive closing chapter for the review draft
- Established the current repository baseline as the official review draft for group comment
- Removed visible drafting markers, outdated editorial scaffolding, and transient citation artifacts from the main text
- Clarified the review role of core framing chapters, including status, conventions, terminology, conformance, migration, and operational profiles

## [0.1.0] - 2026-03-10

### Changed

- Initial repository structure for the Dynamic Software Licensing best practices
- Main best practices directory and chapter layout
- Normative and informative annex structure
- Schema and diagram placeholder directories
- Initial root governance and contribution files
- Initial chapter index files for the main best practices structure
- Best practices chapters reorganized into chapter folders
- Chapter entry files aligned to a `00-index.md` structure
- Main best practices layout adjusted for clearer GitHub navigation
- Repository purpose as a working draft for the Dynamic Software Licensing initiative
- Editorial positioning as industry best practices with standard-like structure
- Separation between main best practices content and annex material
