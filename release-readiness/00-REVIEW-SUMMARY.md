# DSL Best Practices — Release Readiness Review (corrected against current `main`)

Status: Proposal for working-group review
Baseline: `origin/main` at commit `57c6548` ("Simplify public PDF note in README"),
tag `v0.2.0-review-draft`. This branch is rebased onto that commit.

---

## 0. Important correction notice (read first)

An earlier version of this review package was written against a **stale local checkout of
`main` that was ~107 commits behind** the real repository (a snapshot from late May 2026).
That stale snapshot showed empty chapters, empty schema files, no `api/` directory, and
`IABM` branding — **none of which is true of the current `main`.** Several findings in the
first draft were therefore wrong.

This corrected version was produced after `git fetch` and re-verification against the
**current** `origin/main`. The branch has been rebased onto current `main`, so it is now
`0 behind`. `main` itself was not modified.

**Verified current state of `main` (all previously "missing/empty" items are already done):**

| Item | First (stale) review claimed | Actual state on current `main` (verified) |
|---|---|---|
| Chapter status | "Working Draft / outline / not started" | **Reviewed Draft** across chapters (e.g. Ch.09: Reviewed Draft / developed draft / partially normative) |
| Branding | "IABM everywhere; inconsistent with IAMT" | **IAMT only** — 13 IAMT references, **0 IABM** |
| JSON Schemas | "all 5 files are 0 bytes" | **Populated** and moved to `api/` (`api/lease.schema.json` etc., with `$defs` and constraints) |
| OpenAPI / `api/` dir | "missing; broken Annex B reference" | **Present** — `api/dsl-api.openapi.yaml` (~20 KB) + `api/README.md` |
| Diagrams | "only `.drawio` sources; nothing renders" | **Rendered images present** — AWS PNGs + an event-production SVG under `diagrams/` |
| Repo maturity | "empty outline" | README: **Repository status: Reviewed Draft** |

## 1. What survived the correction

Because the repository is far more advanced than the stale snapshot suggested, most of the
original package is now **redundant** and should not be presented as new work:

- `proposed-schemas/` — **redundant.** `main` already has populated schemas in `api/`, and
  they are more developed than our versions. **Do not adopt.** Retained only for a diff (see
  `01-spec-vs-implementation-deltas.md`).
- `proposed-api/dsl-api.openapi.yaml` — **redundant.** `main` already has an OpenAPI file.
  **Do not adopt.**
- `proposed-diagrams/` — **largely redundant.** `main` already renders AWS diagrams and an
  event-production SVG. The Mermaid versions may still be useful *only* where a
  GitHub-inline, diffable diagram is wanted that `main` does not yet have — this must be
  checked case by case, not assumed.
- `02-branding-iamt-sweep.md` — **obsolete.** Branding is already IAMT on `main`.

What may still hold, **but only after re-verification against current `main`** (not yet
done in depth):

- Consumability / length / repetition observations (Finding 6, original) — these describe
  the *document's writing style*, which the merges may or may not have changed. Needs a
  fresh read of current chapters before asserting anything.
- Spec-vs-implementation drift (D1–D11) — some deltas may now be resolved on `main`; the
  ones that remain need to be re-checked against `main`'s current `api/` schemas and Ch.10,
  not against the PDF alone.

## 2. Honest status of this package

This package should **not** be pushed/opened as a "here are the gaps" PR in its original
form, because its central premise was based on a stale snapshot. It has been corrected to:

1. Rebase onto the real `main` (done).
2. Record the correction transparently (this document).
3. Mark the redundant artifacts clearly so nobody mistakes them for needed additions.

The genuinely useful next step is a **fresh, correct review against current `main`** —
see Section 3.

## 3. Recommended next actions

1. **Re-run the review against current `main`** to produce findings that are actually true
   now. Candidate areas worth checking (unverified): document length/repetition, any
   remaining spec/impl drift in `api/` vs Ch.10/11, cross-reference integrity, and whether
   the rendered diagrams cover every figure referenced in the text.
2. **Decide the fate of this branch.** Options:
   - Repurpose it to carry only genuinely-new, verified additions (drop the redundant
     `proposed-*` folders).
   - Or close it and start a fresh review branch from current `main`.
3. **Do not adopt** `proposed-schemas/`, `proposed-api/`, or `02-branding-iamt-sweep.md` —
   superseded by `main`.

## 4. Provenance / lessons

- Root cause: the review was performed on a local checkout without first running
  `git fetch` and comparing to `origin/main`. The local `main` was ~107 commits and ~2.5
  months stale.
- Fix applied: fetch, verify current state, rebase the branch onto current `main`, and
  correct every factual claim in this package.
- Guardrail for next time: always `git fetch` and diff against `origin/main` (and check for
  release tags) **before** assessing repository state.
