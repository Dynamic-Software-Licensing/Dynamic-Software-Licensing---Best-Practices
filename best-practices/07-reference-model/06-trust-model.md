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

```
┌──────────────────────────────────────────────────┐
│              CONTROL PLANE (trusted)             │
│                                                  │
│  Entitlements ── Leases ── Keys ── Usage         │
│                                                  │
│  Trust basis: managed infrastructure,            │
│  key custody, audit logging                      │
└────────────────────┬─────────────────────────────┘
                     │
          TLS + Authentication
          (IAM / OIDC / custom)
                     │
┌────────────────────┴─────────────────────────────┐
│            WORKSPACE PLANE (semi-trusted)         │
│                                                  │
│  License Agent ──── Application + SDK            │
│                                                  │
│  Trust basis: identity evidence,                 │
│  signed tokens, local validation                 │
└──────────────────────────────────────────────────┘
```

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
|---|---|---|
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

```
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

The grace period represents a deliberate trade-off between production continuity and strict license enforcement. The parameters of this trade-off are controlled by the vendor (with optional tenant overrides).

## Anti-Tampering Considerations

- Tokens are cryptographically signed; modification invalidates the signature.
- The SDK validates signatures before accepting any token claims.
- The JWKS endpoint is served over TLS to prevent key substitution.
- Token claims include a unique identifier (`jti`) for anti-replay protection.
- The audit log records all issuance and renewal events, enabling detection of anomalous patterns.

## Trust Between Participants

The DSL model involves multiple organizational participants, each with different trust relationships:

| Relationship | Trust Mechanism |
|---|---|
| Customer → Control Plane | Authentication (IAM/OIDC), TLS, audit trails |
| Control Plane → Workload | Identity evidence verification at issuance and renewal |
| Workload → Token | Cryptographic signature validation |
| Vendor → Control Plane | Key custody, entitlement management, policy definition |
| SI → Control Plane | API access with scoped permissions for deployment automation |
| Customer → Vendor | Entitlement agreement, usage transparency via portal and analytics |

## Platform Neutrality

The trust mechanisms described here (signed tokens, identity evidence, key management, TLS) are available across cloud, hybrid, and on-premises environments. The specific implementations of identity evidence and key management vary by platform, but the trust model itself is platform-neutral.
