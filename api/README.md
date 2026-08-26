# API Artifacts

This directory contains the machine-readable API companion artifacts for the Dynamic Software
Licensing review draft.

GitHub renders the OpenAPI YAML file as source code in the repository browser. This Markdown
overview provides a GitHub-friendly entry point while keeping the OpenAPI contract and JSON
schemas available in the same location.

## Files in This Directory

| File | Purpose |
| --- | --- |
| [dsl-api.openapi.yaml](dsl-api.openapi.yaml) | Canonical machine-readable OpenAPI companion for the baseline REST surface |
| [entitlement.schema.json](entitlement.schema.json) | Entitlement data model |
| [lease.schema.json](lease.schema.json) | Lease data model |
| [policy.schema.json](policy.schema.json) | Policy data model |
| [token-claims.schema.json](token-claims.schema.json) | Token-claims data model |
| [usage-event.schema.json](usage-event.schema.json) | Usage-record data model |

This directory contains the core machine-readable artifacts with closed, reusable payload shapes.
Some Chapter 11 objects remain documented only in Markdown when they intentionally carry
deployment-specific or vendor-specific structure, such as the optional license envelope.

## Baseline REST Surface

| Operation | Endpoint | Method | Purpose |
| --- | --- | --- | --- |
| Issue | `/v1/leases` | POST | Request a new lease for a workload |
| Renew | `/v1/leases/{leaseId}:renew` | POST | Extend an active lease |
| Reissue | `/v1/leases/{leaseId}:reissue` | POST | Initiate transfer to a new workload identity |
| Reissue finalize | `/v1/leases/{leaseId}:finalizeReissue` | POST | Complete a controlled lease transfer |
| Inspect | `/v1/leases/{leaseId}` | GET | Retrieve current lease state without changing lifecycle state |
| Revoke | `/v1/leases/{leaseId}` | DELETE | Terminate an active lease |
| Usage record | `/v1/usage-records` | POST | Submit usage or metering events |
| JWKS | `/.well-known/jwks.json` | GET | Retrieve public signing keys |

## What the OpenAPI Covers

- request and response structures for the baseline lifecycle endpoints,
- common security expectations,
- RFC 9457 problem-details responses,
- example payloads for successful flows and a quota-related error case,
- references to the underlying JSON schemas used by the review draft.

## How to Use These Artifacts

- Use [dsl-api.openapi.yaml](dsl-api.openapi.yaml) as the machine-readable source for review,
  contract testing, mock generation, or client scaffolding.
- Use the JSON schema files when validating individual payload shapes outside the full API
  contract.
- Use [../annexes/normative/annex-b-api-contracts.md](../annexes/normative/annex-b-api-contracts.md)
  and Chapter 10 as the textual authority if interpretation questions arise.

## GitHub Rendering Note

GitHub does not provide a native interactive OpenAPI renderer in the normal repository file
view. For that reason, this directory keeps a readable Markdown index next to the raw OpenAPI
and schema files.
