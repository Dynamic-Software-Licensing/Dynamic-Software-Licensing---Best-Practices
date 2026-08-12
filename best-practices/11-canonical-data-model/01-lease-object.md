# 11.01 Lease Object

## Purpose

This section defines the canonical lease object used by the Dynamic Software Licensing (DSL)
best practices. The lease object represents the active or historical grant of licensed
capability from the control plane to a specific workload identity.

The lease object is the runtime state anchor of the DSL model. It links entitlement,
identity, policy, token issuance, lifecycle operations, and usage attribution.

## Role of the Lease Object

The lease object records:

- which tenant and application the grant belongs to,
- which identity the grant is bound to,
- which dimensions and license modality were granted,
- which policy governs runtime behavior,
- what lifecycle state the lease is currently in,
- which token material and audit-relevant timestamps are associated with it.

The lease object exists independently of the token string that carries the runtime grant. A
token is a portable signed artifact derived from the lease; the lease remains the control
plane's authoritative record.

## Canonical Structure

| Field | Type | Description |
| --- | --- | --- |
| `leaseId` | string | Unique identifier of the lease |
| `tenantId` | string | Tenant to which the lease belongs |
| `app` | string | Licensed application or product identifier |
| `entitlementId` | string | Source entitlement from which the lease was derived |
| `status` | string | Current lifecycle status of the lease |
| `licenseModality` | string | Granted modality governing lifecycle and metering behavior |
| `dimensions` | array | Granted dimensions and limits |
| `boundIdentity` | object | Verified identity to which the lease is bound |
| `policy` | object | Effective policy governing renewal, grace, and exhaustion |
| `issuedAt` | string | Time at which the lease was issued |
| `expiresAt` | string | End of current validity window |
| `renewedAt` | string | Most recent successful renewal time, if any |
| `revokedAt` | string | Revocation time, if revoked |
| `workId` | string | Optional higher-level correlation identifier |
| `tokenRef` | object | Reference to the current signed token or token metadata |

## Required Semantics

### Lifecycle status

The `status` field expresses the control-plane view of the lease lifecycle. Canonical values
should include at least:

- `ISSUED` — created and granted,
- `ACTIVE` — currently valid for runtime use,
- `RENEWED` — active after one or more successful renewals,
- `REISSUING` — in controlled transfer to a new identity,
- `REVOKED` — no longer permitted,
- `EXPIRED` — validity window ended without further continuation,
- `TERMINATED` — closed after controlled end of use.

Implementations may map these values to their internal state machine, but the externally
visible semantics should remain consistent.

### Granted dimensions

The `dimensions` field contains the actual granted limits, not merely the originally requested
values. Each entry should identify what is being limited and the amount granted.

```json
{
 "name": "CHANNELS",
 "quantity": 4
}
```

### Bound identity

The `boundIdentity` field is the verified identity summary that the control plane accepted for
this lease. It should be sufficient to explain binding and audit the lease, but it should not
require raw identity evidence to remain embedded in the lease record.

### Policy snapshot

The `policy` field is the effective policy snapshot applied to this lease. It is the policy
that must be enforced by the workspace plane during local validation and interruption.

## Example Shape

```json
{
 "leaseId": "L-01HY6G1Q3Z5W6E3Z2N7X0",
 "tenantId": "tenant-a",
 "app": "app-A",
 "entitlementId": "ENT-001",
 "status": "ACTIVE",
 "licenseModality": "hourly",
 "dimensions": [
  {
   "name": "CHANNELS",
   "quantity": 4
  }
 ],
 "boundIdentity": {
  "platform": "aws",
  "subject": "i-0abc123def456"
 },
 "policy": {
  "renewBeforeSeconds": 300,
  "offlineGraceSeconds": 1800,
  "onGraceExhausted": "DRAIN"
 },
 "issuedAt": "2026-08-12T10:00:00Z",
 "expiresAt": "2026-08-12T11:00:00Z",
 "workId": "deploy-i-0abc123def456"
}
```

## Relationship to Other Objects

- The entitlement object defines the rights from which the lease is derived.
- The policy object defines the behavior snapshot carried by the lease.
- The token claims object describes the signed runtime representation of key lease data.
- The usage event object records consumption associated with the lease.

## Section Positioning

This object is the canonical runtime grant record of the DSL model. It should be read as the
stateful counterpart to the signed token used for local enforcement.
