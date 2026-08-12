# 07.03 — Control Plane

## Purpose

This section describes the responsibilities and characteristics of the Control Plane within the Dynamic Software Licensing model. The control plane is the central authority for entitlements, lease lifecycle management, cryptographic key operations, usage metering, and policy enforcement.

## Role in the Architecture

The control plane serves as the trusted backend for all licensing decisions. It:

- Is the single source of truth for entitlements and active leases.
- Issues, renews, reissues, and revokes leases.
- Signs tokens using managed cryptographic keys.
- Records usage events for billing and analytics.
- Pushes revocation and policy update events to workspace-plane agents.

The control plane does not run application workloads. It is logically and operationally separated from the workspace plane.

## Design Characteristics

### Serverless and Elastic

The control plane is designed to be serverless — services execute only when invoked and scale elastically with demand. There is no persistent compute running when idle. This aligns with the principle that licensing infrastructure should not impose fixed operational overhead.

### Event-Driven

Asynchronous operations (lease expiry, renewal reminders, reissue deadlines, alerts) are handled through an event orchestration layer. Events trigger downstream processing without requiring polling or long-lived connections from the control plane side.

### Multi-Tenant with Isolation

The control plane supports multiple tenants with logical isolation. Each tenant's entitlements, leases, and usage data are separated. Cryptographic separation (per-tenant or per-product keys) may be applied depending on the deployment model.

### API-First

All control plane operations are exposed through well-documented REST APIs. There are no operations that require manual intervention or console-only access. This supports IaC integration, CI/CD pipelines, and programmatic license management.

## Core Services

### Entitlements Management

Manages the catalog of what each tenant is entitled to use:

- Products and applications available to the tenant.
- Dimensions and limits per entitlement (e.g., 4 channels, 60 FPS).
- License modality (hourly, daily, monthly, annual, consumption-based).
- Default policies (grace periods, renewal windows, exhaustion actions).
- Quota tracking to prevent over-issuance.

### Lease Lifecycle

Handles the full lifecycle of leases through the following operations:

| Operation | Description |
| --- | --- |
| ISSUE | Validate entitlement, verify identity evidence, sign and return a lease token |
| RENEW | Extend the TTL of an active lease, return a fresh token |
| REISSUE | Create a shadow lease on a new workload, finalize to transfer and revoke the original |
| REVOKE | Terminate a lease (admin action, policy trigger, or entitlement change) |

Each operation writes to an append-only audit log.

### Token Signing and Key Management

- Signing keys are held in a managed key service (e.g., HSM-backed).
- Tokens are signed at issuance and renewal.
- Public keys are published at a JWKS endpoint for local validation by workspace-plane components.
- Key rotation is supported via key identifiers (`kid`) in token headers.

### Usage Metering

- Accepts usage records from license agents with dimensions, quantities, and timestamps.
- Stores records in both a hot store (operational queries) and a cold store (analytics, billing).
- Supports idempotent submission for reliability during network interruptions.
- Usage dimensions are modeled to be compatible with marketplace-style metering.

### Event Orchestration

- Manages timers for lease expiry, renewal nudges, and reissue deadlines.
- Triggers alerts at configurable thresholds (e.g., 15 minutes of grace remaining).
- Fans out events to notification channels and downstream services.

### Push Channel (Revocation and Policy Updates)

- Maintains persistent connections (e.g., WebSocket) to license agents.
- Pushes revocation events when a lease is revoked (admin, policy, or reissue finalization).
- Pushes policy updates when vendor changes grace or renewal parameters.
- If the agent is offline, revocation takes effect at the next renewal attempt.

## API Surface

The control plane exposes the following primary endpoints:

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/leases/issue` | POST | Request a new lease |
| `/leases/renew` | POST | Renew an existing lease |
| `/leases/reissue` | POST | Initiate lease transfer (shadow) |
| `/leases/reissue/finalize` | POST | Complete lease transfer |
| `/leases/revoke` | POST | Revoke a lease |
| `/usage/record` | POST | Submit usage events |
| `/.well-known/jwks.json` | GET | Retrieve public signing keys |

Authentication is required for all endpoints (IAM, OIDC, or custom authorizer). Throttling and perimeter protection are applied at the gateway level.

## Data Model (Logical)

The control plane manages the following logical data entities:

- Tenants: organizational identity and configuration.
- Products: application definitions and dimension catalogs.
- Entitlements: per-tenant, per-product allocation with dimensions, modality, and policy.
- Leases: active and historical lease records with status, binding, expiry, and audit trail.
- Usage Events: metered consumption records.
- Audit Log: append-only record of all lease operations.

## Observability

The control plane provides:

- Logging of all API calls and service invocations.
- Metrics for lease issuance rates, renewal success/failure, revocation events, and usage volumes.
- Tracing across service boundaries for debugging and performance analysis.
- API-level auditing for compliance and security review.
- Per-tenant throttle and quota monitoring.

Depending on the system design, logs, metrics, and traces can be stored in a unified platform such as OpenTelemetry or Grafana stack.

## Security Posture

- Zero-trust: no implicit trust between components; all requests are authenticated and authorized.
- Least-privilege: each service has only the permissions it needs.
- Encryption: data encrypted in transit (TLS) and at rest.
- Key management: signing keys are never exposed outside the key management service.
- Audit: all operations are logged with immutable audit trails.

## Platform Neutrality

This description is intentionally platform-neutral. The control plane can be implemented using any combination of API gateways, compute services, databases, key management systems, and event buses that satisfy the described characteristics. Platform-specific reference implementations are provided in annexes.
