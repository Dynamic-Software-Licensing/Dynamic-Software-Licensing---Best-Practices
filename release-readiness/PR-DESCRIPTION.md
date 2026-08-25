# PR: Release-readiness review of current `main`

## What this is

An **additive** `release-readiness/` folder containing a single review document,
`CURRENT-MAIN-REVIEW.md`, with findings verified against the **current** `main`
(`57c6548`, tag `v0.2.0-review-draft`). It changes nothing in `best-practices/`,
`annexes/`, `api/`, or `diagrams/`.

## Context (transparency)

An earlier version of this branch was written against a stale local checkout of `main`
(~107 commits behind) and contained incorrect findings plus redundant proposed artifacts.
That content has been **removed**. The branch is rebased onto current `main` and now carries
only the corrected review. `main` was not modified by this branch.

## Findings (all verified against current `main`)

Healthy: IAMT branding (0 IABM), consistent schemas/API/data-model, AIP-136 paths, chapter
statuses aligned, no empty files or TODO markers.

To resolve before release:
1. **F1 (High):** `api/dsl-api.openapi.yaml` version is `0.1.0-review-draft`; CHANGELOG/tag are `0.2.0-review-draft`.
2. **F2 (Med):** revoke `reason` enum in OpenAPI (5) vs Chapter 10.05 (7).
3. **F3 (Med):** Annex D / Annex G figures exist only as tables/prose.
4. **F4 (Low/Med):** Chapter 13.02 SVG image path has unencoded spaces.
5. **F5 (Low):** entitlement status casing — prose lowercase vs schema uppercase.
6. **F6 (Low/decision):** License Envelope (Ch.11.07) has no JSON schema.

## Suggested disposition

Most findings are one- or two-line fixes. Recommend turning F1–F6 into small individual PRs
or issues against `main`, then closing this review branch.
