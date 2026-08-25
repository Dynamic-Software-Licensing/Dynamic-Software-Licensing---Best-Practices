# DSL Best Practices — Release-Readiness Review (current `main`)

Baseline reviewed: `origin/main` at `57c6548` ("Simplify public PDF note in README"),
tag `v0.2.0-review-draft`. This branch is rebased onto that commit.

Method: verified directly against the current repository content (chapters, annexes,
`api/`, `diagrams/`, root docs). No files were changed by this review.

> Provenance note: an earlier version of this package was mistakenly written against a
> stale local checkout of `main` (~107 commits behind). That produced several false
> findings (empty schemas, missing `api/`, IABM branding). Those claims are withdrawn.
> This document replaces them with findings verified against the current `main`.

---

## Summary

The repository is in good shape and close to release-ready. Branding, schemas, the API
contract, chapter statuses, and internal references are largely consistent. The items below
are the remaining, concrete inconsistencies worth resolving before the public release.

## Confirmed healthy (no action needed)

- **Branding:** IAMT throughout the document body; **0 `IABM`** occurrences. Logo
  `assets/IAMT-logo.png` exists with matching filename case.
- **Schemas & data model:** `api/` contains the OpenAPI plus 5 JSON Schemas. Field names are
  consistent across the schemas, Chapter 11, and Annex C. All 5 schemas use `draft/2020-12`
  and a consistent `$id` convention.
- **Endpoints:** AIP-136 custom-method (colon) paths are consistent across `api/`,
  Chapter 10, Chapter 7, and Annex B.
- **Status/version framing:** all 16 chapters are "Reviewed Draft"; `best-practices/index.md`
  matches the per-chapter status blocks; README, index, and Chapter 00 agree.
- **Hygiene:** no empty files, no TODO/TBD/FIXME markers, no dangling `schemas/` references;
  Annex B relative links to `api/` resolve; all 4 embedded images resolve.

## Findings to resolve (priority order)

### F1 — OpenAPI version is stale (High)
`api/dsl-api.openapi.yaml` declares `info.version: 0.1.0-review-draft`, but `CHANGELOG.md`
and the git tag are `0.2.0-review-draft`.
- **Action:** bump `info.version` to `0.2.0-review-draft`.

### F2 — Revoke reason enum mismatch (Medium)
Chapter 10.05 lists 7 revocation reasons (`admin_action`, `policy_violation`,
`entitlement_expired`, `decommissioned`, `force_release`, `reissue_cutover`,
`quota_exceeded`); the OpenAPI `reason` enum lists only the first 5.
- **Action:** either add `reissue_cutover` and `quota_exceeded` to the enum, or add a note in
  Chapter 10.05 / the OpenAPI that the request enum is deliberately a client-supplied subset
  (the two omitted reasons are system-initiated).

### F3 — Annex D / Annex G figures exist only as tables/prose (Medium)
Annex D (lifecycle state model) and Annex G (example sequences) are described as tables and
numbered prose. Chapter 7's concept and component diagrams already exist as inline Mermaid.
- **Action:** confirm whether the PDF figures for these annexes should be added as inline
  Mermaid (state diagram for Annex D; sequence diagrams for Annex G) for parity, or whether
  tables/prose are intentionally the canonical form.

### F4 — SVG image path contains unencoded spaces (Low/Medium)
Chapter 13.02 embeds `../../diagrams/DSL Event Based Production.svg`. It resolves on GitHub,
but spaces in Markdown image URLs are fragile in some renderers and PDF pipelines.
- **Action:** rename the file to a hyphenated name (e.g. `dsl-event-based-production.svg`)
  and update the reference, or URL-encode the spaces as `%20`.

### F5 — Entitlement status casing inconsistent (Low)
Chapter 11.02 prose uses lowercase (`active`, `suspended`, `expired`); the schema enum is
uppercase (`ACTIVE`, `SUSPENDED`, `EXPIRED`). Lease status is uppercase in both.
- **Action:** align the Chapter 11.02 prose to uppercase to match the schema and the lease
  convention.

### F6 — License Envelope object has no JSON schema (Low / decision)
Chapter 11.07 defines a License Envelope object, but there is no
`api/license-envelope.schema.json`. It is documented as optional.
- **Action:** decide whether to add a schema for completeness or explicitly note that the
  envelope is intentionally schema-optional.

## Suggested disposition of this branch

This review replaces the earlier stale package. The redundant proposed artifacts
(`proposed-schemas/`, `proposed-api/`, `proposed-diagrams/`) and obsolete notes
(`00-REVIEW-SUMMARY.md`, `01-spec-vs-implementation-deltas.md`, `02-branding-iamt-sweep.md`,
`03-consumability-recommendations.md`) have been removed, because `main` already resolves
what they proposed and they were the only remaining source of stale `IABM`/`schemas/`
references in the repo.

Recommended next step: turn F1–F6 into small, individual PRs (or issues) against `main`.
Most are one- or two-line fixes.
