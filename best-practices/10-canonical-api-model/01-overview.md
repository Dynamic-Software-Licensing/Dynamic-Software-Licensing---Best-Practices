# 10.01 — Overview

## Purpose

This section defines the overall purpose and interaction model of the canonical API within the Dynamic Software Licensing (DSL) best practices. It explains how the API fits into the broader architecture and establishes the foundational patterns that all subsequent API operations follow.

## Role of the API in the DSL Architecture

The DSL model is built on an API-first principle: all licensing functions are fully accessible via open, well-documented interfaces. There are no operations that require manual intervention, console-only access, or vendor-specific tooling to complete.

The canonical API is the primary interface between:

- The workspace plane (license agents, SDKs, orchestration tools) and the control plane (entitlements, leases, keys, usage, analytics).
- Administrative tools (portals, CLI, IaC modules) and the control plane.
- Event-driven systems (revocation push, policy updates) and workspace-plane agents.

## Interaction Model

The API follows a request-response model over REST for all transactional operations, complemented by a push channel (WebSocket) for asynchronous events.

### REST Operations (Synchronous)

All lease lifecycle and usage operations are exposed as REST endpoints:

| Operation | Endpoint | Method | Purpose |
|---|---|---|---|
| Issue | `/leases/issue` | POST | Request a new lease for a workload |
| Renew | `/leases/renew` | POST | Extend an active lease |
| Reissue | `/leases/reissue` | POST | Initiate lease transfer to a new workload |
| Reissue Finalize | `/leases/reissue/finalize` | POST | Complete a lease transfer |
| Revoke | `/leases/revoke` | POST | Terminate a lease |
| Usage Record | `/usage/record` | POST | Submit metered usage events |
| JWKS | `/.well-known/jwks.json` | GET | Retrieve public signing keys |

All operations use POST except JWKS discovery, which uses GET. This reflects the fact that lease operations are state-changing actions, not idempotent reads.

### Push Channel (Asynchronous)

The control plane maintains a WebSocket connection to license agents for:

- Revocation events: immediate notification when a lease is revoked.
- Policy updates: notification when vendor changes grace, renewal, or exhaustion parameters.

The push channel is a complement to the REST API, not a replacement. If the push channel is unavailable, revocation and policy changes take effect at the next renewal cycle.

## Authentication and Authorization

All API endpoints require authentication. The canonical model supports multiple authentication mechanisms:

- IAM-based authentication (cloud-native workloads).
- OIDC token-based authentication (Kubernetes, federated identity).
- Custom authorizers (on-premises or hybrid environments).

Authorization is enforced per-tenant: a request can only operate on entitlements and leases belonging to the authenticated tenant.

## Common Request Patterns

All REST operations share common structural patterns:

### Request Structure

Every request includes:

- An application identifier (`app`) indicating which licensed product is being addressed.
- A tenant identifier (`tenantId`) indicating the organizational context.
- Identity evidence (`identityEvidence`) proving the workload's identity.
- A client descriptor (`client`) with agent type and version for diagnostics.

### Response Structure

Every successful response includes:

- A lease identifier (`leaseId`) for correlation and subsequent operations.
- A signed token (`token`) for local validation and enforcement.
- An expiry timestamp (`expiresAt`) indicating when the lease or token expires.
- A policy object (`policy`) with enforcement parameters.

### Error Responses

Failed requests return a structured error response. The error model is defined in subchapter 10.08.

## Idempotency

Operations that may be retried (e.g., due to network interruption) support idempotency through:

- The `workId` field, which correlates a request to a specific deployment or run.
- The `leaseId` field for renewal and revocation operations.
- Usage records include timestamps and correlation identifiers to prevent double counting.

## Versioning

The API includes a version indicator in the client descriptor (`client.version`) to support forward compatibility. The canonical model does not prescribe a URL-based versioning scheme at this stage; versioning strategy is reserved for implementation guidance.

## Transport Security

All API communication occurs over TLS. Private connectivity options (VPN, private endpoints) are supported for environments that require them. The push channel (WebSocket) also operates over TLS (WSS).

## Relationship to Other Chapters

- The reference model (Chapter 07) defines the architectural context in which the API operates.
- The canonical data model defines the structure of the objects exchanged through the API.
- The security and trust framework defines the authentication, signing, and validation mechanisms referenced here.
- Detailed payload schemas and examples are provided in annexes.
