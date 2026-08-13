# 10.01. Overview

## Purpose

This section defines the overall purpose and interaction model of the canonical API within the Dynamic Software Licensing (DSL) best practices. It explains how the API fits into the broader architecture and establishes the foundational patterns that all subsequent API operations follow.

## Design Standards

The canonical API adopts the following established standards to ensure interoperability, tooling compatibility, and alignment with industry practice:

| Concern | Standard | Reference |
| --- | --- | --- |
| URL structure | Google AIP (resource-oriented with custom methods) | [AIP-136](https://google.aip.dev/136) |
| JSON field naming | lowerCamelCase | [AIP-140](https://google.aip.dev/140) |
| Error responses | RFC 9457 — Problem Details for HTTP APIs | [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) |
| Key discovery | RFC 7517 — JSON Web Key (JWK) | [RFC 7517](https://datatracker.ietf.org/doc/html/rfc7517) |
| Distributed tracing | W3C Trace Context | [W3C Trace Context](https://www.w3.org/TR/trace-context/) |
| Well-known URIs | RFC 8615 | [RFC 8615](https://www.rfc-editor.org/rfc/rfc8615.html) |

### Rationale

The API URL design follows the Google AIP custom-method pattern rather than pure CRUD REST or verb-based paths. Lease operations such as "renew" and "reissue" are domain-specific actions with side effects (identity re-verification, token re-signing, state transitions) that do not map cleanly to standard HTTP verbs like PATCH or PUT. The custom-method pattern (`:renew`, `:reissue`) preserves resource-oriented structure while being explicit about intent.

JSON payloads use lowerCamelCase for consistency with JWT custom claims, the existing draft content, and the broader ecosystem of JavaScript/TypeScript API consumers.

## Role of the API in the DSL Architecture

The DSL model is built on an API-first principle: all licensing functions are fully accessible via open, well-documented interfaces. There are no operations that require manual intervention, console-only access, or vendor-specific tooling to complete.

The canonical API is the primary interface between:

- The workspace plane (license agents, SDKs, orchestration tools) and the control plane (entitlements, leases, keys, usage, analytics).
- Administrative tools (portals, CLI, IaC modules) and the control plane.
- Event-driven systems (revocation push, policy updates) and workspace-plane agents.

## Interaction Model

The API follows a request-response model over REST for all transactional operations, complemented by a push channel (WebSocket) for asynchronous events.

### REST Operations (Synchronous)

All lease lifecycle and usage operations are exposed as versioned REST endpoints following the Google AIP resource-oriented design:

| Operation | Endpoint | Method | Purpose |
| --- | --- | --- | --- |
| Issue | `/v1/leases` | POST | Request a new lease for a workload |
| Renew | `/v1/leases/{leaseId}:renew` | POST | Extend an active lease |
| Reissue | `/v1/leases/{leaseId}:reissue` | POST | Initiate lease transfer to a new workload |
| Reissue Finalize | `/v1/leases/{leaseId}:finalizeReissue` | POST | Complete a lease transfer |
| Revoke | `/v1/leases/{leaseId}` | DELETE | Terminate a lease |
| Usage Record | `/v1/usage-records` | POST | Submit metered usage events |
| JWKS | `/.well-known/jwks.json` | GET | Retrieve public signing keys (RFC 7517) |

Standard CRUD operations (create a lease, delete a lease) use standard HTTP methods. Domain-specific actions that have side effects beyond simple state mutation use custom methods (`:renew`, `:reissue`, `:finalizeReissue`) following [AIP-136](https://google.aip.dev/136).

### Push Channel (Asynchronous)

The control plane maintains a WebSocket connection to license agents for:

- Revocation events: immediate notification when a lease is revoked.
- Policy updates: notification when vendor changes grace, renewal, or exhaustion parameters.

The push channel is a complement to the REST API, not a replacement. If the push channel is unavailable, revocation and policy changes take effect at the next renewal cycle. Implementations that cannot support WebSocket connections remain fully functional — they rely on token TTL and the renewal cycle for eventual consistency.

## Authentication and Authorization

All API endpoints require authentication. The canonical model supports multiple authentication mechanisms:

- IAM-based authentication (cloud-native workloads).
- OIDC token-based authentication (Kubernetes, federated identity).
- Custom authorizers (on-premises or hybrid environments).

Authorization is enforced per-tenant: a request can only operate on entitlements and leases belonging to the authenticated tenant.

## Common Request Patterns

All REST operations share common structural patterns.

### Request Headers

Every request SHOULD include [W3C Trace Context](https://www.w3.org/TR/trace-context/) headers for distributed tracing:

| Header | Description |
| --- | --- |
| `traceparent` | Identifies the incoming request in a trace (version, trace-id, parent-id, trace-flags) |
| `tracestate` | Carries vendor-specific trace data |

The control plane MUST propagate `traceparent` in responses and internal spans. This enables end-to-end observability across the workspace plane, control plane, and ISV systems using OpenTelemetry-compatible tooling.

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

Failed requests return a structured error response following [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html). The error model is defined in subchapter 10.08.

## Idempotency

Operations that may be retried (e.g., due to network interruption) support idempotency through:

- The `workId` field, which correlates a request to a specific deployment or run.
- The `leaseId` field (in the URL path) for renewal and revocation operations.
- Usage records include timestamps and correlation identifiers to prevent double counting.

## Versioning

The API uses URL-based versioning with a `/v1/` prefix. This provides clear contract boundaries and supports non-breaking evolution within a version and breaking changes across versions. The client descriptor (`client.version`) additionally communicates the agent's software version for diagnostics and forward compatibility negotiation.

## Transport Security

All API communication occurs over TLS. Private connectivity options (VPN, private endpoints) are supported for environments that require them. The push channel (WebSocket) also operates over TLS (WSS).

## Relationship to Other Chapters

- The reference model (Chapter 07) defines the architectural context in which the API operates.
- The canonical data model defines the structure of the objects exchanged through the API.
- The security and trust framework defines the authentication, signing, and validation mechanisms referenced here.
- Detailed payload schemas and examples are provided in annexes.
