# Contributing

## Purpose

This document explains how to contribute to this repository in practice.

For role definitions, status values, and governance rules, see [GOVERNANCE.md](GOVERNANCE.md).
For the full team operating model including milestones, ownership, and meeting rhythm, see [WORKFLOW.md](WORKFLOW.md).

## Quick Start

1. An issue exists describing the work and its acceptance criteria.
2. Create a chapter branch from `main`.
3. Make your first commit.
4. Open a **Draft PR** and link the issue (`Closes #<issue>` or `Related to #<issue>`).
5. Keep committing to the same branch.
6. When acceptance criteria are met, switch PR to **Ready for review**.
7. Address review feedback in the same branch.
8. Editor approves and merges to `main`.

Core rules:
- Never work directly on `main`.
- One issue = one branch = one PR.
- Do not open multiple PRs for the same issue.

## Branch Naming Convention

| Prefix | Example | Use for |
|---|---|---|
| `chapter-XX-` | `chapter-09-identity-binding` | Chapter content work |
| `annex-` | `annex-b-api-update` | Annex changes |
| `terminology-` | `terminology-lease-alignment` | Terminology changes |
| `fix-` | `fix-typo-chapter-07` | Small corrections |
| `governance-` | `governance-role-update` | Governance/process changes |
| `schema-` | `schema-lease-update` | Schema changes |
| `workflow-` | `workflow-ci-update` | GitHub Actions changes |

## Pull Request Workflow

### 1. Draft PR (work in progress)

Open a Draft PR as soon as a meaningful first version of the content exists.

- marks work as visible and in progress,
- allows early feedback,
- starts automated checks.

Do not wait until the content is complete before opening the PR.

### 2. Ready for Review

Switch the PR from Draft to Ready for review only when:
- acceptance criteria from the issue are substantially met,
- scope is aligned with the issue,
- any open points are noted clearly in the PR description.

### 3. After Review

- Address review comments in the same branch.
- If significant changes are made after review, re-request review.
- Editor makes the final merge decision.

## Linking Issues

In the PR description, link the issue:
- `Closes #123` — issue will close automatically on merge.
- `Related to #123` — partial implementation; issue stays open.

## PR Description Requirements

Every PR must include:
- what changed and why,
- which issue it relates to,
- change category (Editorial / Terminology / Informative / Normative / Structural),
- status intent (`no status change` or `status change requested`).

These fields are validated automatically.

## Writing Style

- Formal, neutral, implementation-oriented.
- Short paragraphs with explicit section headings.
- Controlled vocabulary (check `best-practices/04-terminology-and-abbreviations.md`).
- No marketing language or vague claims.
- Main document must remain platform-agnostic.

## Normative Language

Use `MUST`, `SHOULD`, `MAY` only where they express clear implementation expectations.
Do not use normative keywords in introductory or explanatory sections.

## Terminology Discipline

Before introducing a new term:
1. Check `best-practices/04-terminology-and-abbreviations.md`.
2. Check `annexes/normative/annex-e-terminology-reference.md`.
3. Use the existing term if one exists.
4. Raise a Terminology issue if a change is needed.

## Platform-Specific Content

Keep the main document platform-agnostic.
Place platform-specific examples in:
- `annexes/informative/annex-f-aws-reference-architecture.md`
- other informative annexes as appropriate.

## Commit Messages

Use clear, concise commit messages:
- `Draft chapter 09 identity binding structure`
- `Align terminology for lease and entitlement`
- `Refine chapter 07 reference model wording`
- `Fix typo in chapter 05 stakeholder section`

## Status Conventions

Use only status values defined in `GOVERNANCE.md`.

For routine drafting commits, you do not need to update chapter status blocks yourself.
In the PR description, always state whether you believe a status change is needed.
Editors confirm and apply status changes.

## Git Quick Reference

```bash
# Start new work
git checkout main
git pull origin main
git checkout -b chapter-09-identity-binding

# Stage and commit
git add best-practices/09-normative-requirements/
git commit -m "Draft chapter 09 identity binding structure"
git push -u origin chapter-09-identity-binding

# Sync with latest main
git checkout main && git pull origin main
git checkout chapter-09-identity-binding
git merge main

# Useful status checks
git branch --show-current
git status
git log --oneline --decorate -n 10
git diff main...HEAD --name-only
```

## GitHub UI Only (No Terminal)

1. Create branch: Code → branch dropdown → New branch → `chapter-XX-name`.
2. Select that branch, open a file, edit with the pencil icon.
3. Commit to the same branch.
4. A Draft PR is created automatically — check Pull Requests.
5. Keep editing and committing to the same branch.
6. When ready: open the PR → Ready for review.
7. Editor merges after approval.

## Automated Checks

All checks run automatically. If a check fails, fix the issue and push again.

| Check | When it runs |
|---|---|
| Branch name validation | PR opened |
| PR description completeness | PR opened / edited |
| PR checklist validation | PR opened / edited |
| Chapter status field validation | PR touches `00-index.md` |
| Markdown lint | PR + push to `main` |
| Status table update | Push to `main` |
| Auto Draft PR | First push to chapter/annex/fix branch |
