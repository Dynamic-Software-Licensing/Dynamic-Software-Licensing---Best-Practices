# 07.04. Workspace Plane

## Purpose

This section describes the responsibilities and characteristics of the Workspace Plane within the Dynamic Software Licensing model. The workspace plane is where licensed applications run and where licensing is enforced locally.

## Role in the Architecture

The workspace plane is the runtime environment for applications. It is responsible for:

- Running the licensed application workload.
- Hosting the license agent that mediates between the application and the control plane.
- Providing identity evidence to prove workload authenticity.
- Validating lease tokens locally without requiring a constant connection to the control plane.
- Enforcing dimension limits and policy rules at the point of execution.

The workspace plane does not make licensing decisions. It enforces decisions made by the control plane using the information embedded in signed tokens.

## Design Characteristics

### Runtime Agnostic

The workspace plane is not tied to a specific runtime environment. It may be:

- A cloud virtual machine (e.g., EC2 instance launched from an AMI).
- A container running in an orchestration platform (e.g., Kubernetes pod).
- A bare-metal or virtualized on-premises server.
- A hybrid deployment spanning cloud and on-premises infrastructure.

The licensing model adapts to the runtime through the identity evidence mechanism and the license agent's ability to operate in different environments.

### Local Enforcement

Once a lease token is delivered to the application, enforcement happens locally:

- The application or SDK validates the token signature using cached public keys (JWKS).
- Dimension limits (channels, FPS, bandwidth, etc.) are enforced in-process.
- Token expiry and grace policy are evaluated locally without contacting the control plane.

This design ensures that the application continues to operate during transient network interruptions, governed by the policy embedded in the token.

### Identity-Based Binding

Workloads are identified by their runtime identity rather than hardware attributes. This means:

- No binding to hostnames, MAC addresses, or hardware dongles.
- Identity evidence is derived from the platform (e.g., instance identity documents, IAM roles, Kubernetes service account tokens).
- Binding is verified at lease issuance and renewal, ensuring the token is used by the intended workload.

## Core Components

### License Agent

The license agent is the primary workspace-plane component responsible for all licensing interactions. It runs as a sidecar process, daemon, or CLI alongside the application.

Responsibilities:

| Function | Description |
| --- | --- |
| Identity collection | Gathers identity evidence from the runtime environment |
| Lease request | Calls the control plane to issue a new lease |
| Token delivery | Delivers the signed token to the application (file, socket, or environment variable) |
| Renewal | Schedules and executes lease renewal before token expiry |
| Revocation handling | Receives revocation events via WebSocket and triggers appropriate action |
| Usage reporting | Buffers usage events locally and uploads when connectivity is available |
| Grace enforcement | Monitors token expiry and applies grace policy actions (drain, degrade, stop) |
| Reissue coordination | Participates in lease transfer during failover scenarios |

The license agent abstracts all licensing complexity from the application. From the application's perspective, it receives a valid token and enforces its claims.

### Application SDK

The SDK is an in-process library integrated into the application. It provides:

- Token parsing and signature validation using JWKS public keys.
- Exposure of granted dimension claims (e.g., licensed channel count, FPS limit) to the application.
- Expiry monitoring and grace policy evaluation.
- A simple interface for the application to query its current licensing state.

The SDK validates the token and exposes entitlement data. Dimension enforcement (deciding what happens when a limit is exceeded) is the responsibility of the application itself, since enforcement logic is application-specific and high-liability.

The SDK is designed to be vendor-agnostic and open source, enabling consistent integration across different ISV products.

### Token Validation Flow

The local validation flow within the workspace plane:

1. License agent delivers a signed token to the application.
2. SDK retrieves public keys from the JWKS endpoint (cached after first fetch).
3. SDK validates the token signature, expiry (`exp`), not-before (`nbf`), and audience (`aud`). (The audience claim identifies which application the token was issued for).
4. SDK extracts dimension claims and makes them available to the application.
5. Application enforces dimensions during operation.
6. On token refresh (renewal), the license agent delivers an updated token and the SDK re-validates.

No database or control plane call is in the hot path of token validation.

## Operational Scenarios

### Normal Operation

- License agent starts with the workload, collects identity evidence, requests a lease.
- Token is delivered to the application; SDK validates and enforces.
- License agent renews the lease on a schedule defined by the policy (`renewBeforeSeconds`).
- Usage events are reported periodically.

### Network Interruption

- Application continues operating on the current valid token.
- License agent retries renewal with exponential backoff and jitter.
- If the token expires, the offline grace period begins.
- During grace, the application continues operating (full or degraded, per policy).
- If the outage is expected to outlast the configured grace period, the customer MAY request
  an out-of-band lease extension or a temporary offline token from the vendor or control-plane
  operator. The extension artifact is separately signed, manually entered through an
  administrative interface such as CLI or API, and later reconciled against the primary lease
  once connectivity is restored.
- If grace is exhausted, the configured exhaustion action applies (drain, degrade, or stop).
- When connectivity returns, the license agent renews the lease and resumes normal operation.
- Buffered usage events are uploaded.

### Failover (Reissue)

- A new workload instance starts (e.g., backup EC2 in a blue/green deployment).
- The new license agent requests a reissue from the control plane, referencing the original lease.
- The control plane creates a shadow lease and returns a cutover token.
- On finalization, the original lease is revoked and the new lease is activated.
- The original license agent receives a revocation push and the original workload drains or stops.

### Revocation

- The control plane pushes a revocation event to the license agent via WebSocket.
- The license agent notifies the application/SDK.
- The application executes the configured exhaustion action (drain, degrade, or stop).
- If the license agent is offline when revocation occurs, the revocation is not lost. Because tokens are short-lived, the license agent must eventually contact the control plane to renew. At that point, the control plane rejects the renewal and the revocation takes effect. The maximum delay is bounded by the token's TTL.

## Deployment Patterns

The workspace plane supports multiple deployment patterns:

| Pattern | License Agent Model | Identity Evidence |
| --- | --- | --- |
| Cloud Instance (eg AWS Machine Image (AMI) on EC2) | Daemon or sidecar process | Instance Identity Document (IID) + IAM role |
| Kubernetes | Sidecar container | Service Account JWT |
| On-premises | Daemon or CLI | Platform-specific identity or certificate-based |
| Hybrid | Varies by environment | Mixed evidence types |

The license agent adapts its identity collection and communication patterns to the deployment environment.

## Security Considerations

- Tokens are validated cryptographically; no trust is placed in the delivery mechanism alone.
- Identity evidence is verified by the control plane at every issuance and renewal.
- The license agent communicates with the control plane over TLS. Private connectivity (e.g., VPN, private endpoints) is supported for environments that require it.
- The SDK never stores or transmits the signing private key; it only uses public keys for validation.
- Token TTLs are kept short to limit exposure if a token is compromised.

## Platform Neutrality

This description applies to any runtime environment that can host an application alongside a license agent process and provide some form of workload identity. Platform-specific deployment guides and identity evidence formats are documented in annexes.
