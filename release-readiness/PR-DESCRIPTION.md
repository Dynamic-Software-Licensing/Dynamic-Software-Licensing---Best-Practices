# PR: Release-readiness review package (CORRECTED — rebased onto current `main`)

## Important context

The first version of this package was written against a **stale local checkout of `main`
(~107 commits / ~2.5 months behind)**. That led to several incorrect findings (empty
schemas, missing `api/`, IABM branding, outline-only chapters) that are **not true of the
current `main`**. This branch has now been **rebased onto the current `origin/main`**
(`57c6548`, tag `v0.2.0-review-draft`) and the package content has been corrected.

`main` was not modified by this branch.

## What this PR actually is now

An **additive** `release-readiness/` folder that:

1. Transparently records the correction and what the real current state of `main` is
   (`00-REVIEW-SUMMARY.md`, Section 0).
2. Clearly marks the artifacts that are now **redundant** because `main` already has them:
   - `proposed-schemas/` — superseded by `api/*.schema.json` on `main`. Do not adopt.
   - `proposed-api/` — superseded by `api/dsl-api.openapi.yaml` on `main`. Do not adopt.
   - `02-branding-iamt-sweep.md` — obsolete; branding is already IAMT.
   - `proposed-diagrams/` — largely redundant; `main` already renders diagrams.
3. Flags the items that *might* still be valid but **require re-verification against current
   `main`** (document length/repetition; any remaining spec/impl drift in `api/` vs Ch.10/11).

## Verified current state of `main`

| Item | Current `main` (verified) |
|---|---|
| Chapter status | Reviewed Draft |
| Branding | IAMT only (0 IABM) |
| Schemas | Populated, in `api/` |
| OpenAPI / `api/` | Present (`api/dsl-api.openapi.yaml`) |
| Diagrams | Rendered images present |

## Recommended disposition

This PR is **not** a "here are the gaps to fix" PR anymore. Reviewers should decide:

- Repurpose this branch to carry only genuinely-new, verified additions (dropping the
  redundant `proposed-*` folders), **or**
- Close it and run a fresh review from current `main`.

Do **not** merge the redundant proposed artifacts.
