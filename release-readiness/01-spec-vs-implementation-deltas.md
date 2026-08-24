# Spec vs Implementation Deltas

# Spec vs Implementation Deltas

> **CAUTION — needs re-verification against current `main`.** This delta analysis was
> produced against a stale snapshot and against the PDF alone. The current `origin/main`
> already ships populated schemas and an OpenAPI file under `api/`, so some of these deltas
> may already be resolved on `main`. Before acting on any row, re-check it against the
> current `api/*.schema.json`, `api/dsl-api.openapi.yaml`, and Chapter 10/11 on `main`.
> Do not treat this list as authoritative until that re-check is done. See
> `00-REVIEW-SUMMARY.md`.

---

Purpose: This document lists places where the best-practices spec and the **reference
implementation** (`dsl-reference-implementation`) differ, so the group can converge them.
The best-practices document is the source of truth.

Because the spec is authoritative, most deltas resolve as **"the implementation should be
changed to match the document."** A few are flagged as **"spec gap"** where the
implementation revealed something genuinely missing from the document that the group should
consider adopting into the spec.

Legend for "Proposed resolution":
- **Impl-changes** = document is correct; open a follow-up issue on the implementation repo.
- **Spec-gap** = implementation revealed a real omission; the document should adopt it.
- **Group** = needs an explicit group decision.

> Path-style note (resolved): The best-practices document **consistently** uses the Google
> AIP-136 custom-method (colon) form throughout Chapter 10 (Design Standards 10.01, the
> endpoint tables in 10.02–10.06, the control-plane API surface in 07.03) and Annex B. This
> was verified across the document. The colon form is therefore canonical; see D1.

---

## D1 — API path style (custom method vs sub-resource)

| Source | Value |
|---|---|
| Spec (Ch.10 / Annex B) | `POST /v1/leases/{leaseId}:renew`, `:reissue`, `:finalizeReissue` (Google AIP-136 custom-method colon syntax) |
| Implementation (`dsl-api-stack.ts`) | `POST /v1/leases/{leaseId}/renew`, `/reissue`, `/finalizeReissue` (path segments) |

- **Impact:** Any generated client, the OpenAPI file, and Annex B examples must use one
  form. They are not interchangeable.
- **Proposed resolution:** **Impl-changes.** The document consistently specifies the
  AIP-136 colon form and states the rationale (Ch.10.01). The proposed OpenAPI in this
  package uses the **colon form** to match the spec. The implementation currently uses
  slash segments (`/renew`), likely because some HTTP API Gateway setups handle the `:`
  custom-method form awkwardly — this is a known practical caveat the implementation team
  should confirm they can support before committing to the colon form. If they cannot,
  this escalates to a **Group** decision. Follow-up issue to be filed on the implementation
  repo.

## D2 — Application identifier field name

| Source | Value |
|---|---|
| Spec (Ch.10 Issue request) | `app` |
| Implementation (issue handler, token claims) | request accepts `app`; stores/returns `appId`; token claim is `appId` |

- **Impact:** Token claim and data-model field naming inconsistency.
- **Proposed resolution:** **Group (minor).** The spec is the source of truth and uses
  `app` in the Issue request but `appId`-style naming would be more consistent with
  `tenantId`, `leaseId`, `isvId`. Since this is an internal inconsistency *within* the
  spec's own conventions, the group should confirm the canonical name. Proposed schemas use
  the spec's field names as written; this delta is flagged for a quick editorial decision.

## D3 — `isvId` field (multi-vendor scoping)

| Source | Value |
|---|---|
| Spec | `isvId` is described conceptually (multi-vendor isolation, per-ISV keys) but is **not** a named field in the Ch.11 objects or Annex C claim set |
| Implementation | `isvId` is a first-class field on Entitlement, Lease, UsageRecord, and the entitlement sort key (`APP#{appId}#ISV#{isvId}`) |

- **Impact:** The data model chapter and token-claims annex omit a field the system relies
  on for tenant/vendor separation.
- **Proposed resolution:** **Spec-gap.** The implementation revealed a real omission: the
  multi-vendor isolation the document describes conceptually needs a concrete field. Add
  `isvId` to the Ch.11 objects and Annex C. Proposed schemas include `isvId` as an optional
  field so the spec can adopt it without breaking existing single-vendor examples.

## D4 — Lease lifecycle states

| Source | States |
|---|---|
| Spec (Annex D) | `ISSUED`, `ACTIVE`, `RENEWED`, `REISSUING`, `REVOKED`, `EXPIRED`, `TERMINATED` |
| Implementation | `ACTIVE`, `RENEWED`, `SHADOW`, `REVOKED`, `EXPIRED` (no `ISSUED`, `REISSUING`, or `TERMINATED`; adds `SHADOW`) |

- **Impact:** The state model is normative (Annex D) and referenced by conformance. The
  implementation's `SHADOW` (the pending target lease during two-phase reissue) has no spec
  equivalent, and the spec's `REISSUING`/`ISSUED`/`TERMINATED` are not implemented.
- **Proposed resolution:** **Spec-gap + Group.** The spec is authoritative on the canonical
  state set, so the implementation should adopt the spec's names. But the implementation
  exposed a genuine question the spec should answer: during two-phase reissue, the *target*
  lease exists in a pending state before cutover — the spec's `REISSUING` describes the
  *original* lease's transfer but does not clearly name the *shadow/target* lease's state.
  The group should decide whether `REISSUING` covers both or whether a distinct
  shadow/pending state is added to Annex D. Proposed lease schema enumerates the **spec**
  states and adds a note describing the shadow-lease question rather than silently importing
  the implementation's `SHADOW`.

## D5 — Dimension naming convention

| Source | Example dimensions |
|---|---|
| Spec (Ch.10/Ch.11 examples) | `CHANNELS`, `FPS` (upper snake/caps) |
| Implementation (seed data) | `maxChannels`, `maxFps` (lowerCamelCase, `max` prefix) |

- **Impact:** Cosmetic but user-visible; affects every example and any validation.
- **Proposed resolution:** **Impl-changes.** Dimensions are vendor-defined, so the schema
  does not enumerate names. But the *examples* should match the spec; the implementation's
  seed data should be updated to the spec's example dimension names for consistency in
  demos. Proposed schemas keep `name` free-form and use the spec's example names in
  documentation.

## D6 — Entitlement quota field names

| Source | Value |
|---|---|
| Spec (Ch.11 Entitlement) | `quota.maxActiveLeases` (nested object) |
| Implementation | `maxLeases` + `activeLeases` (flat fields on the entitlement) |

- **Impact:** Structural difference in the entitlement object.
- **Proposed resolution:** **Impl-changes.** The spec's nested `quota.maxActiveLeases` is
  authoritative; the proposed entitlement schema follows the spec's nested form. The
  implementation's flat `maxLeases`/`activeLeases` should be reconciled (a follow-up issue
  on the implementation repo). Note for the group: the flat form is arguably simpler and the
  group *may* prefer to amend the spec instead — flagged as a possible spec revision rather
  than assumed.

## D7 — Lease object fields present in impl, absent in spec

| Field (impl) | In spec Ch.11 Lease? |
|---|---|
| `lastRenewedAt` | No (spec has `renewedAt`) |
| `revokeReason` | No |
| `reissueId` | No |
| `cutoverToken` | No (spec keeps cutover token in the reissue response, not on the lease) |
| `appId` | Spec uses `app` |

- **Proposed resolution:** **Mixed.** `renewedAt` (spec) is authoritative — the
  implementation's `lastRenewedAt` should be renamed (**Impl-changes**). `revokeReason` is a
  useful **Spec-gap** the document should adopt (it aids auditability, which the spec
  emphasises). `reissueId`/`cutoverToken` on the lease record are an implementation storage
  detail and should be marked impl-internal, not added to the canonical Ch.11 Lease object.
  Proposed lease schema follows the spec (`renewedAt`), adds optional `revokeReason`, and
  omits `reissueId`/`cutoverToken`.

## D8 — Token TTL derivation

| Source | Value |
|---|---|
| Spec | "short-lived"; TTL not numerically defined |
| Implementation | `TTL = renewBeforeSeconds * 3` |

- **Proposed resolution:** **Impl (informative).** Document the `3x` heuristic as a
  non-normative example default in Ch.12/Annex, keeping the normative requirement as
  "short-lived and bounded."

## D9 — Admin/demo endpoints

| Endpoint (impl) | In spec? |
|---|---|
| `POST /v1/admin/reset` | No (demo-only) |
| `GET /v1/admin/observability` | No (demo-only) |

- **Proposed resolution:** **Impl-only.** Keep out of the canonical API. The proposed
  OpenAPI marks them clearly as non-normative/demo extensions so they are not mistaken for
  part of the standard surface.

## D10 — Token issuer / subject / audience values

| Claim | Spec (Annex C) | Implementation |
|---|---|---|
| `iss` | `https://lic.example.com` (a URL) | `dsl-control-plane` (an opaque string) |
| `sub` | `workload:<id>` (the bound workload) | `tenantId` |
| `aud` | `appId` | `appId` |

- **Impact:** `sub` semantics differ materially (workload vs tenant). This matters for
  validation logic and is the highest-priority delta.
- **Proposed resolution:** **Impl-changes.** The spec (Annex C) is authoritative: `sub` =
  the bound workload identity (that is what the lease binds to), and `tenantId` is already a
  separate claim, so putting the tenant in `sub` is redundant. `iss` should also be a URL
  per the spec. The implementation should change both. Proposed token-claims schema follows
  the spec. This delta should be called out explicitly to the implementation team because it
  changes token validation logic.

## D11 — Token date claim types (found while generating the token-claims schema)

| Source | `iat` / `nbf` / `exp` representation |
|---|---|
| Spec (Annex C prose / example) | ISO-8601 strings (e.g. `"2026-08-12T11:00:00Z"`) |
| RFC 7519 (cited by the spec) | NumericDate — integer seconds since epoch |
| Implementation (`token_signer.py`) | integer `NumericDate` (RFC-correct) |

- **Impact:** A validator built from the Annex C examples would reject RFC-compliant
  tokens, and vice-versa. This is an internal contradiction in the spec (it cites RFC 7519
  but shows string dates).
- **Proposed resolution:** **Spec editorial fix.** Annex C examples should show NumericDate
  integers for `iat`/`nbf`/`exp` to match RFC 7519 and the implementation. Proposed
  token-claims schema uses integers. Low effort, but should be corrected before publication
  because it affects interoperability.

---

## Summary of resolutions

Source of truth = the best-practices document. Default action is therefore "implementation
changes to match spec," except where the implementation exposed a genuine spec gap.

| Delta | Resolution | Action owner | Priority |
|---|---|---|---|
| D1 API path style (`:renew`) | Impl-changes (confirm gateway support) | Impl repo | High |
| D10 `sub`/`iss` claim semantics | Impl-changes | Impl repo | High |
| D4 Lease states / shadow-lease naming | Spec-gap + Group | Spec (Annex D) + group | High |
| D3 add `isvId` to spec | Spec-gap | Spec (Ch.11, Annex C) | Medium |
| D2 `app` vs `appId` naming | Group (editorial) | Spec | Medium |
| D6 quota field shape | Impl-changes (or spec revision) | Impl repo / group | Medium |
| D7 lease fields (`renewedAt`, `revokeReason`, cutover) | Mixed | Spec + impl repo | Low/Medium |
| D5 dimension example names | Impl-changes | Impl repo (seed data) | Low |
| D8 token TTL heuristic | Spec-gap (informative) | Spec (informative note) | Low |
| D9 admin/demo endpoints | Impl-only (kept out of canonical API) | Impl repo | Low |
| D11 token date claim types (string vs NumericDate) | Spec editorial fix | Spec (Annex C) | Medium |

**Highest-priority items for the working group:** D4 (shadow-lease state — a real spec
gap), D10 (`sub` semantics — changes validation logic), and confirming D1 (whether the
implementation's API Gateway can serve the AIP-136 colon form).
