# 07.06 — Trust Model

## Purpose

This section defines how trust is established, maintained, and verified across the Dynamic Software Licensing model. It describes the trust boundaries between components, the mechanisms used to prove identity and integrity, and the assumptions that underpin secure licensing operations.

## Trust Principles

The DSL trust model is based on the following principles:

1. Zero implicit trust: no component trusts another by default. Every interaction requires authentication and verification.
2. Short-lived credentials: lease tokens have limited lifetimes, reducing the window of exposure if a token is compromised.
3. Cryptographic verification: trust is established through cryptographic signatures, not through network location or shared secrets alone.
4. Identity-based binding: workloads are identified by verifiable runtime identities, not hardware attributes.
5. Least privilege: each component has only the permissions necessary for its function.

## Trust Boundaries

The DSL model defines the following trust boundaries:

```mermaid
flowchart TB
    subgraph control[Control Plane (trusted)]
        entitlements[Entitlements]
        leases[Leases]
        keys[Keys]
        usage[Usage]

        entitlements --> leases
        leases --> keys
        keys --> usage
    end

    subgraph workspace[Workspace Plane (semi-trusted)]
        agent[License Agent]
        app[Application + SDK]

        agent --> app
    end

    control -->|TLS + authentication<br/>IAM / OIDC / custom| workspace
```

Control plane trust basis:

- managed infrastructure,
- key custody,
- audit logging.

Workspace plane trust basis:

- identity evidence,
- signed tokens,
- local validation.

### Control Plane Trust

The control plane is the root of trust for the licensing system. It:

- Holds the private signing keys (via a managed key service).
- Makes all entitlement and lease decisions.
- Maintains the authoritative record of active leases and their status.
- Is responsible for the integrity of the audit log.

Trust in the control plane is established through:
- Secure infrastructure management (access controls, encryption, monitoring).
- Key custody in a hardware-backed key management service.
- Immutable audit trails for all operations.

### Workspace Plane Trust

The workspace plane is semi-trusted. It does not make licensing decisions, but it is trusted to:

- Present valid identity evidence during lease requests.
- Enforce the dimension limits and policy rules embedded in the token.
- Report usage accurately.

Trust in the workspace plane is bounded by:
- Token expiry: even if a workload is compromised, the token expires and must be renewed (which requires valid identity evidence).
- Signature verification: the SDK validates that the token was signed by the control plane.
- Binding claims: the token contains binding information (e.g., IAM role ARN) that can be checked against the runtime environment.

## Identity Evidence

Identity evidence is the mechanism by which a workload proves its identity to the control plane. The DSL model supports multiple forms of identity evidence depending on the runtime environment:

| Environment | Identity Evidence | Verification |
| --- | --- | --- |
| Cloud VM (e.g., EC2) | Instance Identity Document (IID) + PKCS7 signature | Control plane verifies the IID signature against the cloud provider's public key |
| Kubernetes | Service Account JWT | Control plane validates the JWT against the cluster's OIDC issuer |
| On-premises | Platform certificate or custom identity token | Control plane validates against a pre-registered trust anchor |
| Hybrid | Mixed evidence types per workload | Control plane supports multiple evidence types per tenant |

Identity evidence is presented at:
- Lease issuance (ISSUE): to establish the initial binding.
- Lease renewal (RENEW): to re-verify that the same workload is still requesting the lease.
- Lease reissue (REISSUE): to establish the identity of the new target workload.

### Identity vs. Hardware Binding

Traditional licensing often binds to hardware identifiers (hostnames, MAC addresses, hardware dongles). The DSL model explicitly replaces this with identity-based binding because:

- Hardware identifiers are not stable in cloud and containerized environments.
- Identity evidence is cryptographically verifiable.
- Identity-based binding supports failover, scaling, and migration without manual license re-binding.

## Token Trust Chain

The trust chain for a lease token follows this path:

1. The control plane's key management service holds the private signing key.
2. The leases service requests a signature from the key management service when issuing or renewing a token.
3. The signed token is delivered to the license agent, which passes it to the application.
4. The application SDK retrieves the public key from the JWKS endpoint (cached locally).
5. The SDK verifies the token signature, confirming it was issued by the control plane.
6. The SDK checks the token claims: expiry, not-before, audience, binding, and dimensions.

At no point does the private key leave the key management service. The trust chain is:

```text
Key Management Service (private key)
    → Leases Service (requests signature)
        → Token (signed artifact)
            → SDK (validates with public key from JWKS)
```

## Revocation Trust

Revocation is a trust-sensitive operation. The model handles it as follows:

- Active revocation: the control plane pushes a revocation event to the license agent via WebSocket. The agent acts immediately.
- Passive revocation: if the agent is offline, the revocation takes effect when the token expires (since renewal will fail) or when the agent reconnects and receives the event.
- Token TTL as a safety net: short token lifetimes ensure that even without active revocation, a compromised or revoked lease cannot be used indefinitely.

## Grace Period Trust

During a grace period (when the license agent cannot reach the control plane to renew), the system operates on a trust-but-verify basis:

- The application continues operating based on the locally held token and its embedded policy.
- The grace period is bounded (defined by `offlineGraceSeconds` in the policy).
- When grace expires, the configured exhaustion action applies (drain, degrade, or stop).
- When connectivity returns, the license agent must successfully renew to continue operation.
- Upon successful renewal after a grace period, operation SHOULD resume automatically without manual intervention. This is the expected default behavior for programmatically configured deployments. Implementations that require manual restart after grace recovery MUST document this clearly.

The grace period represents a deliberate trade-off between production continuity and strict license enforcement. The parameters of this trade-off are controlled by the vendor (with optional tenant overrides).

### Grace Period Configuration Guidance

The `offlineGraceSeconds` value may be configured as either:

- A fixed pre-defined value (e.g., 1800 seconds / 30 minutes) set by the vendor as a default.
- A function-based value derived from operational context (e.g., a multiple of the token TTL, or proportional to the application's typical session duration).

The choice between fixed and function-based grace periods is a vendor policy decision. The following guidelines apply:

| Consideration | Guidance |
| --- | --- |
| Short-lived workloads (event-driven, serverless) | Shorter grace periods (minutes) are appropriate; the workload can restart quickly |
| Long-running production chains (live broadcast) | Longer grace periods (30–60 minutes) protect against transient network issues |
| High-value workloads | Grace periods should be long enough to allow human investigation before disruption |
| Metered / consumption-based entitlements | Grace periods should be bounded to limit unbilled usage during outages |

Vendors SHOULD document their grace period defaults and whether tenant overrides are permitted. Tenants SHOULD NOT need to guess how much time they have before an exhaustion action fires.

## Anti-Tampering Considerations

- Tokens are cryptographically signed; modification invalidates the signature.
- The SDK validates signatures before accepting any token claims.
- The JWKS endpoint is served over TLS to prevent key substitution.
- Token claims include a unique identifier (`jti`) for anti-replay protection.
- The audit log records all issuance and renewal events, enabling detection of anomalous patterns.

## Trust Between Participants

The DSL model involves multiple organizational participants, each with different trust relationships:

| Relationship | Trust Mechanism |
| --- | --- |
| Customer → Control Plane | Authentication (IAM/OIDC), TLS, audit trails |
| Control Plane → Workload | Identity evidence verification at issuance and renewal |
| Workload → Token | Cryptographic signature validation |
| Vendor → Control Plane | Key custody, entitlement management, policy definition |
| SI → Control Plane | API access with scoped permissions for deployment automation |
| Customer → Vendor | Entitlement agreement, usage transparency via portal and analytics |

### Multi-Vendor Trust in a Shared Control Plane

In a multi-vendor environment, the expectation is that a single DSL control plane serves multiple ISVs. This raises the question of how each ISV can trust that their licensing logic is enforced correctly and that their entitlements are not tampered with.

The DSL model addresses this through:

1. Cryptographic isolation: each ISV MAY have dedicated signing keys managed within the control plane's key management service. Tokens signed with ISV-specific keys cannot be forged or repurposed across vendors.

2. Logical tenant and vendor separation: entitlements, leases, and usage data are scoped per vendor and per tenant. No ISV can access, modify, or observe another ISV's entitlement records or usage data.

3. Immutable audit logging: all lease operations (issue, renew, revoke) are recorded in an append-only audit log. ISVs can access audit data for their own products to verify correct enforcement.

4. Vendor-specific policy encapsulation: each ISV defines their own entitlement catalog, dimension definitions, policies (grace, renewal, exhaustion), and pricing. These are stored and enforced per-vendor within the control plane. The control plane applies the correct vendor's policy when processing a lease request for that vendor's product.

5. Optional call-home / audit webhook: the control plane MAY support an outbound webhook or event stream per ISV, allowing vendors to receive real-time notifications of lease operations for their products. This enables independent auditing without requiring ISVs to trust the control plane operator blindly.

6. Concurrent lease enforcement: the control plane enforces quota constraints (e.g., a license with dimension of 1 can only have one active lease at a time). Lease binding to a verified workload identity prevents a single license from being concurrently leased to multiple workloads.

This architecture ensures that adding a new vendor to a shared control plane does not require changes to the API or message flow. Each ISV's business logic, policy, and security boundaries are encapsulated within their entitlement and key configuration.

## Platform Neutrality

The trust mechanisms described here (signed tokens, identity evidence, key management, TLS) are available across cloud, hybrid, and on-premises environments. The specific implementations of identity evidence and key management vary by platform, but the trust model itself is platform-neutral.
