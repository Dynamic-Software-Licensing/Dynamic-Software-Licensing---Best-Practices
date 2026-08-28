# Annex B. API Contracts

## Purpose

This annex consolidates the canonical API surface referenced throughout Chapter 10 into a
compact contract summary for review and cross-reference.

## Contract Scope

The canonical API defines lifecycle and reporting operations between the workspace plane and
the control plane. The annex does not replace the detailed explanatory text in Chapter 10, but
it provides a stable summary of the baseline contract surface.

## Baseline Endpoints

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

## Common Request Expectations

Baseline requests should include:

- `app`,
- `tenantId`,
- `identityEvidence`,
- `client`,
- trace context where supported,
- `workId` when idempotent correlation is required.

## Common Response Expectations

Successful lifecycle responses should include at least:

- `leaseId`,
- `token`,
- `expiresAt`,
- `policy`.

The exact response shape may vary by operation, but these elements define the core runtime
contract.

## Error Model

Errors should be expressed using the Problem Details structure defined by RFC 9457 and should
preserve enough detail for automation, diagnostics, and tenant-safe troubleshooting.

## Contract Notes

- Custom methods are used where lifecycle behavior has domain-specific side effects.
- The push channel for revocation or policy updates complements, but does not replace, the REST
 API.
- Implementations may add vendor-specific fields only where they do not break canonical
 semantics.

## Machine-Readable OpenAPI Companion

A GitHub-friendly overview of the machine-readable API artifacts is provided at
[api/README.md](../../api/README.md).

The underlying OpenAPI companion contract for the baseline REST surface is provided at
[api/dsl-api.openapi.yaml](../../api/dsl-api.openapi.yaml).

The OpenAPI artifact captures the canonical endpoints, common request and response structures,
security expectations, and the RFC 9457 problem-details error envelope in a form that can be
used for review, mock generation, client scaffolding, and contract testing.

For the current published baseline, Annex B and Chapter 10 remain the primary textual
authorities if a wording ambiguity exists. The OpenAPI file is intended to stay aligned with
that baseline contract surface, not to redefine it independently.

## Annex Positioning

This annex is the compact normative reference surface for the baseline API operations of the
published DSL best practices.
