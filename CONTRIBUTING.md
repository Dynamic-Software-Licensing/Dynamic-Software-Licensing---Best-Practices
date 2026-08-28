# Contributing

## Purpose

This document describes the practical daily workflow for contributors.

For roles and governance decisions, see [GOVERNANCE.md](GOVERNANCE.md).
For the full operating model, see [WORKFLOW.md](WORKFLOW.md).

## Issue template choice

- For "work on a chapter", use **Chapter Work Item**.
- Use **Chapter Work Item** for almost all other work as well.
- Use **Terminology Proposal** only for term changes.

Practical rule:
- Small term edits inside one chapter: keep them in the chapter task.
- Use a separate terminology issue only for cross-chapter term decisions
  (new term, rename, definition change, or synonym cleanup across files).

## How to work on a chapter

Everything in GitHub UI — no terminal needed.

**Step 1 — Issue**
Open or create an issue for the chapter work. Assign owner, reviewer, and editor.

**Step 2 — Branch**
Go to Code → branch dropdown → New branch.
Name it `chapter-XX-short-topic`, e.g. `chapter-09-identity-binding`.
Branch from `main`.

**Step 3 — Edit**
Switch to your branch. Open the chapter file. Click the pencil icon to edit.
Write a short commit message and commit directly to your branch.
Repeat for each batch of edits — small commits are better than one large one.

**Step 4 — Draft PR**
Open a Pull Request as soon as a first meaningful draft exists.

> ⚠️ GitHub defaults to "Ready for review". Use the small arrow next to the green button
> and select **"Create draft pull request"** instead.

Fill the PR template: issue link, what changed, why, review state.

**Step 5 — Keep editing**
Continue committing to the same branch. The PR updates automatically.
Keep scope tight — if the work grows beyond the issue, open a follow-up issue.

**Step 6 — Ready for review**
When the issue scope is complete, switch the PR from Draft to **Ready for review**.
Check: wording coherent, terminology consistent, open points noted.

Before marking a PR ready for review, also update the next release entry in [CHANGELOG.md](CHANGELOG.md)
and keep [api/dsl-api.openapi.yaml](api/dsl-api.openapi.yaml) on the same version. In this repository,
every merge to `main` is treated as a new release.

**Step 7 — Review and merge**
Reviewer leaves comments. Address them in the same branch.
Resolve conversations after applying fixes.
Editor approves and merges. Issue closes automatically via `Closes #...`.

---

Core rules:
- Never work directly on `main`.
- One issue, one branch, one PR.
- Keep PRs small and focused.

## Branch Naming

Use one of these prefixes:
- `chapter-XX-` for chapter work
- `annex-` for annex work
- `terminology-` for term changes
- `fix-` or `hotfix-` for fixes
- `governance-` for governance/process docs
- `schema-` for schema work
- `workflow-` for GitHub automation

Examples:
- `chapter-09-identity-binding`
- `fix-typo-chapter-07`
- `schema-lease-update`

## PR Minimum Requirements

Each PR should include:
- linked issue (`Closes #123` or `Related to #123`),
- short summary of what changed,
- short explanation of why,
- updated [CHANGELOG.md](CHANGELOG.md) entry for the next release,
- matching version in [api/dsl-api.openapi.yaml](api/dsl-api.openapi.yaml).

Everything else is optional and can be added when helpful.

## Writing Rules

- Write clearly and concretely.
- Keep the main document platform-agnostic.
- Use controlled terminology from Chapter 04 and Annex E.
- Use `MUST`, `SHOULD`, `MAY` only for real implementation expectations.

## Lightweight Review Guidance

Before setting PR to Ready for review, check:
- scope matches the issue,
- wording is coherent,
- terminology is consistent,
- obvious open points are noted.

## Team review flow (practical)

Use this as the default review process for chapter work.

1. Author opens a Draft PR.
2. Author adds all team members as reviewers.
3. Team reviews asynchronously in GitHub (comment / request changes / approve).
4. Author addresses feedback in the same branch.
5. Author resolves conversations after fixes and re-requests review if needed.
6. Merge when all were invited, required approvals are present, and no open
  request-changes remains.
7. Confirm linked issue is closed (automatic via `Closes #...` or manual).

Recommended approval minimum:
- Standard edits: 1 approval.
- Normative/high-impact edits: 2 approvals.

## Terminal (optional)

If you prefer working locally:

```bash
git checkout main && git pull origin main
git checkout -b chapter-09-identity-binding
git add . && git commit -m "Draft chapter 09 identity binding"
git push -u origin chapter-09-identity-binding
```

## Automation

The repository runs a small set of checks automatically.
If a check fails, fix and push again.

Current principle: keep automation helpful, but merges to `main` are release-bearing and therefore
must pass the release-consistency checks. After merge to `main`, the repository creates the
version tag automatically from the top entry in [CHANGELOG.md](CHANGELOG.md).
