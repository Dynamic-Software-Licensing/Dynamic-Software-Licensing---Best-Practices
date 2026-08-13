![IAMT Logo](assets/IAMT-logo.png)

# Dynamic Software Licensing Best Practices

## Purpose

This repository contains the reviewed draft of an IAMT industry best practices document for software-based, dynamic software licensing in broadcast and media workflows.

The best-practices document is not a formal standard. It is deliberately structured in a standard-like way to support alignment across manufacturers, operators, system integrators, and industry stakeholders.

## Scope of This Repository

This repository is used to:
- define and evolve the structure of the best-practices document,
- capture terminology and architectural concepts,
- document normative and informative content separately,
- support collaborative drafting and review in a transparent, versioned way.

This repository does **not** yet represent a final published best-practices document.

## Document Structure

| Area | Purpose |
| --- | --- |
| `best-practices/` | Core best practices chapters |
| `annexes/normative/` | Normative annexes required for consistent interpretation |
| `annexes/informative/` | Examples, mappings, FAQs, reference architectures |
| `api/` | Machine-readable API contract and data schemas |
| `diagrams/` | Architecture and sequence diagrams |

## How to Navigate

- [best-practices/index.md](best-practices/index.md) — chapter list and status overview
- [best-practices/04-terminology-and-abbreviations/](best-practices/04-terminology-and-abbreviations/) — controlled vocabulary
- [best-practices/09-normative-requirements/](best-practices/09-normative-requirements/) — normative requirements structure

## Working Principles

- Terminology first.
- Structure before detail.
- Platform-agnostic main document.
- Clear separation of normative and informative content.
- Versioned development through Git and GitHub.

## Team Workflow

- [WORKFLOW.md](WORKFLOW.md) — team operating model: milestones, issues, roles, delivery
- [CONTRIBUTING.md](CONTRIBUTING.md) — branch, PR, git commands, writing rules
- [GOVERNANCE.md](GOVERNANCE.md) — roles, status definitions, editorial rules

## Current Status

Repository status: **Reviewed Draft**

The main document is now organized as a complete review draft for group comment ahead of the planned end-of-August release. See [best-practices/index.md](best-practices/index.md) for chapter-level status.

## Automated PDF Build

A manual GitHub Actions workflow is available at `.github/workflows/build-review-pdf.yml`.

It assembles a combined Markdown source and renders a PDF artifact using Pandoc.

A separate workflow at `.github/workflows/publish-latest-pdf.yml` publishes the latest release-oriented PDF to GitHub Pages whenever changes are merged into `main`.

Two source manifests are provided:

- `.github/review-pdf-manifest.txt` for a review-facing PDF that includes repository framing pages such as `README.md` and `api/README.md`
- `.github/release-pdf-manifest.txt` for a leaner release-oriented PDF that excludes those repository navigation pages

Chapter `00-index.md` files are now always included because they provide the main chapter entry points and the intended publication hierarchy in the PDF.

Mermaid diagrams are pre-rendered into PNG assets during the workflow so that the PDF export includes the diagrams as images instead of raw code blocks.

The generated PDF filename is versioned automatically from `CHANGELOG.md`. The review profile keeps the review suffix, for example `dynamic-software-licensing-best-practices-v0.2.0-review-draft.pdf`, while the release profile emits the cleaner publication-style name `dynamic-software-licensing-best-practices-v0.2.0.pdf`.

The GitHub Pages publication workflow also emits a stable download filename, `dynamic-software-licensing-best-practices-latest.pdf`, alongside the versioned release-style PDF. To use this path, GitHub Pages must be enabled for the repository with GitHub Actions as the deployment source.

The generated PDF source now includes an explicit cover page and a fixed-position table of contents before the document body, so the export behaves more like a publication artifact than a raw Markdown concatenation.
