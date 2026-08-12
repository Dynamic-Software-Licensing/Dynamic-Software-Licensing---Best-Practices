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
- confirm or update chapter status fields,
- decide content placement (main document vs annex),
- approve or reject merges into `main`,
- document decisions in the pull request.

Decision scope:
- final editorial decisions on chapter status, classification, and merge readiness.

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

Status is used at two levels: repository maturity and chapter-level drafting status.

### Repository Maturity

| Value | Meaning |
| --- | --- |
| Working Draft | Structure and content are still evolving. |
| Reviewed Draft | Structure is broadly stable; key sections have been reviewed. |
| Candidate Best Practices | Technically and editorially mature enough for final validation. |
| Published Best Practices | Approved as published industry best practices. |

### Chapter Status Fields

Each chapter `00-index.md` must contain a `## Chapter Status` section with the following fields.

**Status**

| Value | Meaning |
| --- | --- |
| Working Draft | Chapter structure or content is still actively changing. |
| Reviewed Draft | Chapter has been reviewed and is broadly stable. |
| Candidate Best Practices Text | Chapter content is considered ready for final best practices. |
| Stable for Cross-Reference | Chapter is stable enough to be referenced by other chapters. |

**Editorial maturity**

| Value | Meaning |
| --- | --- |
| outline | Structure exists; substantive drafting has not started. |
| partial draft | First substantive content exists; significant sections are still incomplete. |
| developed draft | Substantial draft content exists across planned sections. |
| review-ready | Chapter is complete enough for structured editorial review. |

**Normative readiness**

| Value | Meaning |
| --- | --- |
| not started | No normative-level text has been drafted. |
| informative only | Chapter provides context or explanation only. |
| partially normative | Some normative intent or requirement language is present. |
| ready for normative review | Normative content is sufficiently complete for focused review. |

**Open drafting points**

| Value |
| --- |
| yes |
| no |

### Quick Selection Rule

- Mostly headings or placeholders: `outline` + `not started`.
- First real text but clearly incomplete: `partial draft` + `not started` or `informative only`.
- Broadly written across sections: `developed draft` + `informative only` or `partially normative`.
- Ready for formal review: `review-ready` + matching normative readiness.

Default fallback: choose the lower maturity value when unsure.

### Chapter Status Block Template

```markdown
## Chapter Status

- Status: Working Draft
- Editorial maturity: outline
- Normative readiness: not started
- Open drafting points: yes
```

### Status Governance Rule

Contributors indicate status intent in the pull request. Editors confirm repository-visible status changes. Contributors should not update chapter status blocks on routine content commits unless a status change is clearly justified.

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
- `best-practices/04-terminology-and-abbreviations.md`,
- `annexes/normative/annex-e-terminology-reference.md`,
- all affected chapters and annexes using the term.

Contributors must not introduce synonyms for established concepts unless there is an explicit editorial decision.

## Editorial Workflow

### Draft

Work is in progress on a chapter branch. The pull request is in draft state. `main` remains unchanged.

### Review

The pull request is marked Ready for review. Editors and reviewers assess quality and readiness. Further commits may be added to address feedback.

### Final

The reviewed pull request is merged to `main`. This represents the accepted baseline for the current stage. It does not mean the overall best-practices document is fully published.

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
- Final status values are confirmed.
- Review outcome is complete.
- Merge readiness is confirmed.

After merge:
- Status overview tables are accurate.
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
| Chapter status field validation | Manual (`workflow_dispatch`) | Validates allowed status values |
| Status table update | Manual (`workflow_dispatch`) | Regenerates `best-practices/index.md` table |
| Draft PR creation | Manual (`workflow_dispatch`) | Creates Draft PR for current branch |
| PR labeling | Manual (`workflow_dispatch`) | Applies labels from changed paths |

Auto-close linked issues remains provided by GitHub through `Closes #` semantics.

Manual editorial judgment remains required for merge readiness, content quality, and normative classification.

## Traceability Rule

Decisions affecting terminology, conformance, requirement meaning, chapter structure, or annex classification must be documented in the relevant pull request or issue.
