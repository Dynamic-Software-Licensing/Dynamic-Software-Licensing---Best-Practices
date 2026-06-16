# 10.03 — Renew

## Status
- Editorial maturity: working draft
- Normative readiness: not started

## Purpose

This section defines the renewal interaction within the canonical API. The Renew operation extends the lifetime of an active lease, ensuring continuous operation of a licensed workload without interruption.

## When Renew Is Used

The Renew operation is invoked:

- Periodically by the license agent before the current token expires, as governed by the `renewBeforeSeconds` policy parameter.
- After a transient network interruption, when the license agent reconnects and needs to re-establish a valid lease.
- As a background operation — the application is typically unaware that renewal is happening.

Renew is a continuation operation. It assumes a lease has already been issued via the Issue operation.

## Endpoint

```http
POST /v1/leases/{leaseId}:renew
```

## Interaction Flow

1. The license agent monitors the current token's expiry and the `renewBeforeSeconds` policy value.
2. When the renewal window opens (e.g., 5 minutes before expiry), the license agent sends a POST request to `/v1/leases/{leaseId}:renew`.
3. The control plane validates the request:
   - Confirms the lease is still active (not revoked or expired beyond grace).
   - Re-verifies the identity evidence to confirm the same workload is requesting renewal.
   - Checks that the underlying entitlement is still valid.
4. If validation passes, the control plane:
   - Extends the lease TTL.
   - Signs a new token with an updated expiry.
   - Updates the lease record.
   - Returns the new token and expiry to the license agent.
5. The license agent delivers the updated token to the application.
6. The application SDK re-validates the new token and continues operating.

## Request Structure

The lease identifier is provided in the URL path. The request body contains:

| Field | Type | Required | Description |
|---|---|---|---|
| `identityEvidence` | object | Yes | Current proof of workload identity |
| `workId` | string | No | Correlation identifier for the deployment or production chain |

```http
POST /v1/leases/L-01HY6G1Q3Z5W6E3Z2N7X0:renew
```

```json
{
  "identityEvidence": {
    "aws": {
      "iidDocument": "...",
      "iidSignature": "..."
    }
  },
  "workId": "deploy-i-0abc123def456"
}
```

Identity evidence is required at every renewal to re-verify that the requesting workload is the same one the lease was originally bound to. This prevents a compromised or migrated token from being renewed by an unauthorized workload.

The `workId` field is optional but recommended. It enables correlation of individual leases to a higher-level production chain or workload group, supporting aggregated billing and operational visibility across multi-resource deployments.

## Response Structure

A successful Renew response contains:

| Field | Type | Description |
|---|---|---|
| `leaseId` | string | Lease identifier (unchanged) |
| `token` | string | New signed token with updated expiry |
| `expiresAt` | string (ISO 8601) | New expiry timestamp |

```json
{
  "leaseId": "L-01HY6G1Q3Z5W6E3Z2N7X0",
  "token": "<new signed token>",
  "expiresAt": "2025-10-13T18:10:00Z"
}
```

If the vendor has updated the policy since the last renewal, the response may also include an updated `policy` object. The license agent should apply the new policy parameters going forward.

## Renewal Timing and Backoff

The license agent follows this renewal strategy:

1. Begin renewal attempts at `expiresAt - renewBeforeSeconds` (e.g., 5 minutes before expiry).
2. If the first attempt fails, retry with exponential backoff and jitter as defined by the policy's `renewBackoff` parameters:

   ```json
   {
     "renewBackoff": {
       "initialMs": 2000,
       "maxMs": 30000,
       "jitter": true
     }
   }
   ```

3. Continue retrying until either:
   - Renewal succeeds, or
   - The token expires and the offline grace period begins.

## What Happens When Renewal Fails

If the license agent cannot successfully renew before the token expires:

| Phase | Duration | Behavior |
|---|---|---|
| Token valid | Before `expiresAt` | Application operates normally; license agent retries renewal |
| Grace period | `expiresAt` to `expiresAt + offlineGraceSeconds` | Application continues operating (full or degraded per policy); license agent continues retrying |
| Grace exhausted | After grace period ends | Configured exhaustion action applies: DRAIN, DEGRADE, or STOP |

When renewal eventually succeeds (e.g., after network recovery), the application returns to normal operation with a fresh token.

## Validation Rules

The control plane applies the following validation during Renew:

| Check | Failure Condition |
|---|---|
| Lease exists and is active | Lease not found, already revoked, or expired beyond grace |
| Identity evidence matches | Workload identity does not match the lease binding |
| Entitlement still valid | Underlying entitlement has been revoked or modified |
| Quota still available | Entitlement quota has been reduced below current usage |

A failed renewal returns a structured error response (see subchapter 10.08). The license agent treats a rejected renewal the same as an expired token — the grace period and exhaustion logic apply.

## Audit

Every Renew operation is recorded in the audit log with:

- Timestamp
- Lease identifier
- Identity evidence summary
- Outcome (success, failure reason)
- New expiry (if successful)

## Relationship to Other Operations

- Renew follows Issue and maintains the lease during normal operation.
- If renewal is permanently rejected (e.g., entitlement revoked), the effect is equivalent to Revoke.
- Renew does not change the lease binding, dimensions, or modality. To change these, a new Issue or entitlement modification is required.
- If the workload needs to move to a different identity (e.g., failover), Reissue is used instead of Renew.
