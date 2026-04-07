# 10.05 — Revoke

## Purpose

This section defines the revocation interaction within the canonical API. The Revoke operation terminates an active lease, invalidating the workload's right to continue operating under that license.

## When Revoke Is Used

The Revoke operation is invoked when:

- An administrator explicitly terminates a license (e.g., policy violation, contract termination).
- A policy rule triggers automatic revocation (e.g., entitlement expiry, quota enforcement).
- A reissue operation finalizes and the original lease must be invalidated.
- A workload is decommissioned and the license should be returned to the available pool.
- A customer force-releases a stuck license via the End User Portal.

Revoke is a terminal operation. Once a lease is revoked, it cannot be renewed or reissued. A new Issue is required to acquire a fresh lease.

## Endpoint

```
POST /leases/revoke
```

## Interaction Flow

### When the License Agent Is Online

1. An administrator, policy engine, or system operation sends a POST request to `/leases/revoke`.
2. The control plane validates the request:
   - Confirms the lease exists and is active.
   - Confirms the requester has authorization to revoke (admin, policy engine, or tenant with appropriate permissions).
3. The control plane:
   - Sets the lease status to `revoked`.
   - Records the revocation reason.
   - Writes an entry to the audit log.
   - Pushes a revocation event to the license agent via WebSocket.
4. The license agent receives the revocation event and notifies the application/SDK.
5. The application executes the configured exhaustion action:
   - DRAIN: finish current work, refuse new sessions.
   - DEGRADE: apply reduced functionality (e.g., fewer channels, disable premium features).
   - STOP: halt the licensing gate, application stops.

### When the License Agent Is Offline

1. The control plane sets the lease status to `revoked` and records the event.
2. The WebSocket push fails because the agent is not connected.
3. The application continues operating on its current token until it expires.
4. When the token expires, the license agent attempts to renew.
5. The control plane rejects the renewal because the lease is revoked.
6. The license agent applies the exhaustion action.

The maximum delay before revocation takes effect is bounded by the token's TTL. Short token lifetimes limit this window.

## Request Structure

| Field | Type | Required | Description |
|---|---|---|---|
| `leaseId` | string | Yes | Identifier of the lease to revoke |
| `reason` | string | Yes | Reason for revocation (e.g., `"policy_violation"`, `"admin_action"`, `"entitlement_expired"`, `"decommissioned"`, `"force_release"`) |

```json
{
  "leaseId": "L-01HY6G1Q3Z5W6E3Z2N7X0",
  "reason": "policy_violation"
}
```

## Response Structure

| Field | Type | Description |
|---|---|---|
| `status` | string | Resulting lease status (`"revoked"`) |

```json
{
  "status": "revoked"
}
```

## Revocation Reasons

The canonical model defines the following standard revocation reasons:

| Reason | Description |
|---|---|
| `admin_action` | Explicit revocation by an administrator |
| `policy_violation` | Automated revocation triggered by a policy rule |
| `entitlement_expired` | The underlying entitlement has expired or been removed |
| `decommissioned` | The workload has been terminated and the license is being returned |
| `force_release` | Customer-initiated release via the End User Portal for a stuck or failed instance |
| `reissue_cutover` | Revocation as part of a reissue finalization (system-initiated) |
| `quota_exceeded` | Entitlement quota has been reduced below current active leases |

Implementations may extend this list with additional vendor-specific reasons.

## Authorization

Revocation requires elevated permissions. Not all API consumers can revoke a lease:

| Actor | Can Revoke | Typical Scenario |
|---|---|---|
| Tenant administrator | Yes | Admin action, force release, decommissioning |
| Policy engine (control plane) | Yes | Automated policy enforcement, entitlement expiry |
| Reissue service (control plane) | Yes | Cutover finalization |
| License agent | No | Agents do not self-revoke; they receive revocation events |
| Application/SDK | No | Applications execute exhaustion actions, not revocations |

## Audit

Every Revoke operation is recorded in the audit log with:

- Timestamp
- Lease identifier
- Revocation reason
- Requesting actor (admin, policy engine, reissue service)
- Delivery status (WebSocket push succeeded or agent was offline)

## Relationship to Other Operations

- Revoke terminates a lease that was created via Issue.
- After revocation, the lease cannot be renewed. A new Issue is required.
- Revoke is called internally by the Reissue finalization flow to invalidate the original lease.
- The exhaustion action executed by the application is governed by the policy that was embedded in the token at issuance or last renewal.
