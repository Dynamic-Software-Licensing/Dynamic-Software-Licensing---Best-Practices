# 10.02 — Issue

## Purpose

This section defines the initial license issuance interaction within the canonical API. The Issue operation is the entry point for a workload to acquire a lease and begin operating under a licensed entitlement.

## When Issue Is Used

The Issue operation is invoked when:

- A workload starts for the first time and needs to acquire a license.
- A license agent boots alongside an application and requests initial authorization.
- An orchestration tool or IaC deployment triggers license acquisition as part of provisioning.

Issue is a first-run operation. Once a lease is active, subsequent interactions use Renew (to extend) or Reissue (to transfer).

## Endpoint

```
POST /leases/issue
```

## Interaction Flow

1. The license agent starts alongside the application workload.
2. The license agent collects identity evidence from the runtime environment (e.g., Instance Identity Document, IAM role, Kubernetes Service Account JWT).
3. The license agent generates or retrieves a `workId` to correlate this deployment.
4. The license agent sends a POST request to `/leases/issue` with the required fields.
5. The control plane validates the request:
   - Verifies the tenant's entitlement for the requested application.
   - Checks that the requested dimensions are within the entitlement's limits.
   - Verifies the identity evidence against the expected trust anchor.
   - Checks quota availability (e.g., available lease slots).
6. If validation passes, the control plane:
   - Creates a lease record.
   - Signs a token containing the granted dimensions, binding, policy, and expiry.
   - Writes an entry to the audit log.
   - Returns the lease details to the license agent.
7. The license agent delivers the signed token to the application.
8. The application SDK validates the token locally and begins enforcing dimensions.

## Request Structure

The Issue request contains the following fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `app` | string | Yes | Application identifier (e.g., `"app-A"`) |
| `tenantId` | string | Yes | Tenant identifier |
| `dimensions` | array | Yes | Requested dimension limits (e.g., channels, FPS) |
| `licenseModality` | string | Yes | Requested billing model (e.g., `"hourly"`, `"daily"`, `"monthly"`) |
| `identityEvidence` | object | Yes | Proof of workload identity |
| `workId` | string | Yes | Correlation identifier for this deployment or run |
| `version` | string | No | Application version |
| `environment` | string | No | Environment tag (e.g., `"production"`, `"staging"`, `"dev"`) |
| `client` | object | No | License agent type and version for diagnostics |
| `policyHints` | object | No | Requested policy parameters (e.g., heartbeat interval, grace period) |

### Dimensions

Each dimension entry specifies a name and a requested quantity:

```json
{
  "name": "CHANNELS",
  "quantity": 4
}
```

The control plane may grant fewer than requested if the entitlement has lower limits. The granted values are reflected in the response and token.

### Identity Evidence

The identity evidence structure varies by runtime environment. The canonical model uses a nested object keyed by platform:

```json
{
  "identityEvidence": {
    "aws": {
      "iidDocument": "<base64 json>",
      "iidSignature": "<base64 pkcs7>"
    }
  }
}
```

Other platforms (Kubernetes, on-premises) use their own evidence format within the same structure.

### Policy Hints

The license agent may suggest policy parameters. The control plane is not obligated to honor them — it applies the vendor-defined policy, optionally adjusted by tenant overrides:

```json
{
  "policyHints": {
    "heartbeatSeconds": 60,
    "offlineGraceSeconds": 1800
  }
}
```

## Response Structure

A successful Issue response contains:

| Field | Type | Description |
|---|---|---|
| `leaseId` | string | Unique identifier for the issued lease |
| `app` | string | Application identifier |
| `tenantId` | string | Tenant identifier |
| `token` | string | Signed JWT or PASETO token |
| `issuedAt` | string (ISO 8601) | Timestamp of issuance |
| `expiresAt` | string (ISO 8601) | Timestamp of token/lease expiry |
| `licenseModality` | string | Granted billing model |
| `dimensions` | array | Granted dimension limits (may differ from requested) |
| `boundIdentity` | object | The verified identity the lease is bound to |
| `policy` | object | Enforcement parameters (renewal window, grace period, exhaustion action, alerts) |

### Policy Object

The policy returned in the response governs runtime behavior:

```json
{
  "policy": {
    "heartbeatSeconds": 60,
    "renewBeforeSeconds": 300,
    "offlineGraceSeconds": 1800,
    "onGraceExhausted": "DRAIN",
    "revocationEndpoint": "wss://lic.example.com/revocations"
  }
}
```

## Validation Rules

The control plane applies the following validation during Issue:

| Check | Failure Condition |
|---|---|
| Entitlement exists | Tenant has no entitlement for the requested application |
| Dimensions within limits | Requested dimensions exceed entitlement limits |
| Quota available | All lease slots for this entitlement are already in use |
| Identity evidence valid | Evidence signature verification fails or evidence is expired |
| Modality permitted | Requested modality is not available for this entitlement |
| Environment permitted | Requested environment tag is not allowed by policy |

Failed validation returns a structured error response (see subchapter 10.08).

## Audit

Every Issue operation — successful or failed — is recorded in the audit log with:

- Timestamp
- Tenant and application identifiers
- Requested and granted dimensions
- Identity evidence summary (not the raw evidence)
- Outcome (success or failure reason)
- Lease identifier (if successful)

## Relationship to Other Operations

- After Issue, the license agent uses Renew to maintain the lease.
- If the workload fails over, Reissue transfers the lease to a new identity.
- If the lease must be terminated, Revoke invalidates it.
- The token issued here is validated locally using keys from the JWKS endpoint.
