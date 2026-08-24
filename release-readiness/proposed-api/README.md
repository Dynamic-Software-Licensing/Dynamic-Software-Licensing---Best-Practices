# Proposed API Contract  [REDUNDANT — superseded by `api/` on current `main`]

> **Do not adopt.** The current `origin/main` already contains `api/dsl-api.openapi.yaml`
> (~20 KB) and `api/README.md`. This proposed contract was written against a stale snapshot
> that had no `api/` directory. It is retained only for a historical diff against the
> already-merged version. See `../00-REVIEW-SUMMARY.md`.

---

## (original note, kept for context)


This folder provides the machine-readable API contract that Annex B of the best-practices
document references but which does not yet exist in the repository (`api/README.md` and
`api/dsl-api.openapi.yaml` are currently missing).

## Contents

- `dsl-api.openapi.yaml` — OpenAPI 3.1 contract for the canonical DSL control-plane API.

## Source of truth and conventions

- Generated from the **best-practices document** (Chapter 10, Annex B) — the document is
  authoritative.
- **Path style:** Google AIP-136 custom-method (colon) form — `:renew`, `:reissue`,
  `:finalizeReissue` — as specified consistently throughout Chapter 10 and Annex B.
- **Errors:** RFC 9457 Problem Details (`application/problem+json`), per Chapter 10.08.
- **Field shapes:** mirror the proposed JSON Schemas in `../proposed-schemas/`.

## Known deltas vs the reference implementation

Recorded in `../01-spec-vs-implementation-deltas.md`. The most important for this contract:

- **D1** — the implementation currently serves slash paths (`/renew`); this contract uses
  the spec's colon form. Confirm API Gateway support before finalizing.
- **D10** — token `sub`/`iss` semantics differ; the contract follows the spec.
- **D9** — the implementation's `/v1/admin/*` endpoints are demo-only and are intentionally
  **not** part of this canonical contract.

## How to adopt

After group approval, create an `api/` directory at the repo root and move
`dsl-api.openapi.yaml` and this README into it (updating Annex B references if paths
change). Keep it in sync with Chapter 10 — the document remains the primary authority if a
wording ambiguity arises.

## Validation

The contract is OpenAPI 3.1. Validate with any OpenAPI tool, e.g.:

```bash
npx @redocly/cli lint dsl-api.openapi.yaml
# or
python3 -c "import yaml,sys; yaml.safe_load(open('dsl-api.openapi.yaml')); print('YAML OK')"
```
