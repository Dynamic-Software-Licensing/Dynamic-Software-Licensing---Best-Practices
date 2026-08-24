# Proposed JSON Schemas  [REDUNDANT — superseded by `api/` on current `main`]

> **Do not adopt.** The current `origin/main` already contains populated schemas in the
> `api/` directory (`api/lease.schema.json`, `api/entitlement.schema.json`, etc.), and they
> are more developed than the versions here (they use `$defs` and tighter constraints).
> These proposed files were written against a stale snapshot that had empty schema files.
> They are retained only for a historical diff. See `../00-REVIEW-SUMMARY.md`.

---

## (original note, kept for context)


These five schemas populate the currently-empty files in `schemas/`. They are generated
from the **best-practices document (source of truth)** — Chapter 11 (Canonical Data Model),
Annex C (Token Claims), and Annex D (Lifecycle and State Model) — using JSON Schema
draft 2020-12 and lowerCamelCase field naming per the document's stated conventions
(Ch.10.01, AIP-140).

Where the running reference implementation differs, the schema follows the **spec** and the
difference is recorded in `../01-spec-vs-implementation-deltas.md`. Inline `$comment` fields
flag the notable deltas so reviewers see them in context.

Files:

- `entitlement.schema.json` — the upstream authorization record (Ch.11.02).
- `lease.schema.json` — the runtime grant record (Ch.11.01, states per Annex D).
- `policy.schema.json` — runtime behavioural policy (Ch.11.03, Ch.12.06).
- `token-claims.schema.json` — signed runtime token claims (Ch.11.05, Annex C).
- `usage-event.schema.json` — metered usage record (Ch.11.04).

To adopt: after group approval, copy the approved files into the repo's top-level
`schemas/` directory (replacing the empty placeholders), in a small follow-up PR.

Validation: these are standard draft 2020-12 schemas and can be checked with any JSON
Schema validator (e.g. `check-jsonschema`, `ajv`).
