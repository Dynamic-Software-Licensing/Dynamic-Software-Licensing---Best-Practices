# Governance

## Purpose

This document defines the roles, responsibilities, status definitions, and editorial rules that govern how repository content is drafted, reviewed, and accepted.

The model is intentionally lightweight and focused on practical usability.

## Decision Rule

- Contributors propose.
- Reviewers advise.
- Editors decide.
- Maintainers support operations.

## Roles and Responsibilities

### Contributor

A contributor proposes and develops content changes.

Responsibilities:
- draft and refine chapter content,
- raise terminology, scope, or classification questions,
- submit changes via branch and pull request,
- indicate status intent in the pull request,
- respond to review feedback within the agreed SLA.

Decision scope:
- contributors propose; they do not control merge or status decisions.

### Reviewer

A reviewer provides structured feedback on content under review.

Responsibilities:
- assess clarity, consistency, completeness, and applicability,
- flag terminology, interpretation, or structural concerns,
- provide a review best practices (approve / request changes).

Decision scope:
- reviewers advise; they do not merge unless also acting as editor.

### Editor

An editor protects the coherence of the accepted baseline and makes merge decisions.

Responsibilities:
- assess chapter readiness and status maturity,
- confirm or update repository-visible status signals,
- decide content placement (main document vs annex),
- approve or reject merges into `main`,
- document decisions in the pull request.

Decision scope:
- final editorial decisions on status interpretation, classification, and merge readiness.

### Manager

A manager is responsible for milestone planning, delivery tracking, and priority decisions.

Note: in smaller teams the Editor and Manager role may be held by one person.

Responsibilities:
- define milestones with scope, deadline, and deliverables,
- assign Owner and Reviewer per work item,
- track delivery against milestones,
- monitor blockers and escalate or re-scope as needed,
- chair Weekly Triage and Milestone closing.

Decision scope:
- milestone scope, priorities, deadlines, and re-scheduling decisions.

### Maintainer

A maintainer keeps repository operations stable.

Responsibilities:
- manage repository settings, branch protection, and access,
- maintain templates, workflow configuration, and automation,
- support tagging, releases, and structural housekeeping.

Note: in smaller teams one person may act as Editor, Manager, and Maintainer.

## Status Definitions

Status is tracked centrally at the repository and publication level.

### Status Governance Rule

Contributors indicate status intent in the pull request. Editors confirm repository-visible status
changes in the central status surfaces, rather than by maintaining repeated per-chapter status
blocks.

## Change Categories

| Category | Meaning |
| --- | --- |
| Editorial | Wording, clarity, grammar, formatting without meaning change. |
| Terminology | Introduction, removal, rename, or redefinition of controlled terms. |
| Informative | Examples, mappings, annexes, FAQs, platform-specific content. |
| Normative | Requirements, conformance expectations, profiles, interpretation rules. |
| Structural | Chapter or section reorganisation, file moves, scope changes. |

## Content Classification Rules

- Platform-agnostic requirements and principles → main document.
- Platform-specific examples → informative annexes.
- Normative supporting artifacts → normative annexes where applicable.

## Terminology Governance

Terminology is treated as controlled vocabulary.

Any terminology change must be reflected in:
- `best-practices/04-terminology-and-abbreviations/`,
- `annexes/normative/annex-e-terminology-reference.md`,
- all affected chapters and annexes using the term.

Contributors must not introduce synonyms for established concepts unless there is an explicit editorial decision.

## Editorial Workflow

### Draft

Work is in progress on a chapter branch. The pull request is in draft state. `main` remains unchanged.

### Review

The pull request is marked Ready for review. Editors and reviewers assess quality and readiness. Further commits may be added to address feedback.

### Final

The reviewed pull request is merged to `main`. This updates the accepted published baseline and becomes part of the next versioned repository release.

## Editor Checklist

Before review:
- Pull request scope and affected chapters are clear.
- Branch and PR state match Draft or Review.
- Status intent is stated in the PR description.

During review:
- Text is structurally coherent and fits chapter purpose.
- Terminology is consistent with controlled vocabulary.
- Content placement is correct.
- Proposed status is valid.

Before merge:
- Central publication status references are confirmed.
- Review outcome is complete.
- Merge readiness is confirmed.

After merge:
- Central status references remain accurate.
- `main` reflects the accepted baseline.

## Automated Enforcement

The repository currently uses a simplified workflow model.

### Required checks (blocking)

These checks run automatically on pull requests and are intended to stay lightweight:

| Check | Trigger | Scope |
| --- | --- | --- |
| Branch name validation | PR opened | Enforces branch naming convention |
| PR basics validation | PR opened / edited | Rejects empty or trivial PR descriptions |
| Markdown lint | PR + push to `main` | Checks `.md` formatting |

### Optional checks (manual)

These workflows are available but not automatically enforced:

| Check | Trigger | Scope |
| --- | --- | --- |
| Draft PR creation | Manual (`workflow_dispatch`) | Creates Draft PR for current branch |
| PR labeling | Manual (`workflow_dispatch`) | Applies labels from changed paths |

Auto-close linked issues remains provided by GitHub through `Closes #` semantics.

Manual editorial judgment remains required for merge readiness, content quality, and normative classification.

## Traceability Rule

Decisions affecting terminology, conformance, requirement meaning, chapter structure, or annex classification must be documented in the relevant pull request or issue.
