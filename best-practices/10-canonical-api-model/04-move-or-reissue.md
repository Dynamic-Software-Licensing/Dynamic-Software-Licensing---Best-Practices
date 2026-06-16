# 10.04 — Move or Reissue

## Status
- Editorial maturity: working draft
- Normative readiness: not started

## Purpose

This section defines the move or reissue interaction within the canonical API. The Reissue operation transfers an active lease from one workload to another, supporting failover, blue/green deployments, and planned migration scenarios without requiring a new entitlement or causing license downtime.

## When Reissue Is Used

The Reissue operation is invoked when:

- A workload fails and a backup instance needs to take over the license (disaster recovery).
- A blue/green deployment cutover requires the license to move to the new environment.
- A planned migration moves the application to a different host, container, or region.
- An instance is replaced due to corruption and the license must follow.

Reissue is not used for routine renewal (use Renew) or for acquiring a new license (use Issue).

## Two-Phase Design

Reissue uses a two-phase approach to ensure atomic transfer without downtime:

1. Shadow phase: a shadow lease is created on the target workload while the original lease remains active.
2. Finalize phase: the shadow lease is activated and the original lease is revoked.

This design ensures that at no point are both leases fully active simultaneously (preventing double-use), and at no point are both leases inactive (preventing downtime).

## Endpoints

```http
POST /v1/leases/{leaseId}:reissue           (Phase 1: shadow)
POST /v1/leases/{leaseId}:finalizeReissue   (Phase 2: finalize)
```

## Phase 1: Shadow

### Interaction Flow

1. A new workload instance starts (e.g., backup EC2, new Kubernetes pod).
2. The license agent on the new instance collects its identity evidence.
3. The license agent sends a POST request to `/v1/leases/{leaseId}:reissue` referencing the original lease.
4. The control plane validates:
   - The original lease exists and is active.
   - The requesting tenant owns the original lease.
   - The new identity evidence is valid.
5. The control plane creates a shadow lease:
   - The shadow lease is bound to the new workload identity.
   - The original lease remains active during this phase.
   - A cutover token is generated to authorize finalization.
6. The control plane returns the shadow lease details, including the cutover token.

### Request Structure

The original lease identifier is provided in the URL path. The request body contains:

| Field | Type | Required | Description |
|---|---|---|---|
| `toIdentityEvidence` | object | Yes | Identity evidence of the target workload |
| `toWorkId` | string | Yes | Work ID for the target deployment |

```http
POST /v1/leases/L-01HY6G1Q3Z5W6E3Z2N7X0:reissue
```

```json
{
  "toIdentityEvidence": {
    "aws": {
      "iidDocument": "...",
      "iidSignature": "..."
    }
  },
  "toWorkId": "deploy-i-0def789abc123"
}
```

### Response Structure

| Field | Type | Description |
|---|---|---|
| `reissueId` | string | Identifier for this reissue operation |
| `cutoverToken` | string | Authorization token required to finalize |
| `toLease` | object | Shadow lease details (lease ID, token, expiry, dimensions, policy) |

```json
{
  "reissueId": "M-9kqj8f",
  "cutoverToken": "ct-7f2e...",
  "toLease": {
    "leaseId": "L-02...",
    "token": "<signed token for new workload>",
    "expiresAt": "...",
    "dimensions": [...],
    "policy": {...}
  }
}
```

## Phase 2: Finalize

### Interaction Flow

1. The orchestrator or license agent on the new workload confirms the target is ready.
2. A POST request is sent to `/v1/leases/{leaseId}:finalizeReissue` with the reissue ID and cutover token.
3. The control plane:
   - Validates the cutover token.
   - Revokes the original lease.
   - Activates the shadow lease as the new active lease.
   - Pushes a revocation event to the original license agent via WebSocket.
4. The original workload receives the revocation and executes its exhaustion action (drain or stop).
5. The new workload continues operating on the now-active lease.

### Request Structure

The lease identifier is provided in the URL path. The request body contains:

| Field | Type | Required | Description |
|---|---|---|---|
| `reissueId` | string | Yes | Identifier from the shadow phase |
| `cutoverToken` | string | Yes | Authorization token from the shadow phase |

```http
POST /v1/leases/L-01HY6G1Q3Z5W6E3Z2N7X0:finalizeReissue
```

```json
{
  "reissueId": "M-9kqj8f",
  "cutoverToken": "ct-7f2e..."
}
```

### Response Structure

| Field | Type | Description |
|---|---|---|
| `state` | string | Outcome of the finalization (e.g., `"COMPLETED"`) |
| `revoked` | string | Lease ID of the original (now revoked) lease |

```json
{
  "state": "COMPLETED",
  "revoked": "L-01HY6G1Q3Z5W6E3Z2N7X0"
}
```

## Timeout and Deadline

The reissue operation has a deadline. If finalization does not occur within a configured time window:

- The shadow lease is automatically expired.
- The original lease remains active.
- The reissue operation is recorded as abandoned in the audit log.

This prevents orphaned shadow leases from consuming entitlement quota indefinitely.

## Validation Rules

### Shadow Phase

| Check | Failure Condition |
|---|---|
| Original lease exists and is active | Lease not found, already revoked, or expired |
| Tenant owns the original lease | Requesting tenant does not match |
| Target identity evidence is valid | Evidence verification fails |
| No pending reissue for this lease | Another reissue is already in progress |

### Finalize Phase

| Check | Failure Condition |
|---|---|
| Reissue ID exists and is pending | Reissue not found or already completed/expired |
| Cutover token is valid | Token does not match or has expired |

## Audit

Both phases are recorded in the audit log:

- Shadow phase: original lease ID, target identity, reissue ID, timestamp.
- Finalize phase: reissue ID, revoked lease ID, activated lease ID, timestamp, outcome.
- Abandoned reissues (timeout) are also logged.

## Relationship to Other Operations

- Reissue assumes a lease was previously created via Issue.
- After finalization, the new lease follows the normal Renew cycle.
- The revocation of the original lease during finalization follows the same logic as Revoke.
- If the original workload is offline when revocation is pushed, the revocation takes effect at the next renewal attempt (which will be rejected).
