# 10.08 — Error Model

## Purpose

This section defines the structure of API error handling within the canonical API. It describes how failures, rejected requests, and non-successful outcomes are expressed consistently across all operations.

## Design Principles

The error model follows these principles:

1. Consistency: all operations use the same error response structure.
2. Actionability: errors include enough information for the license agent or operator to determine the appropriate next step.
3. Machine-readability: error codes are structured for programmatic handling, not just human reading.
4. Security: error responses do not leak sensitive information about the control plane's internal state, other tenants, or infrastructure details.

## Error Response Structure

All failed API requests return a JSON response with the following structure:

| Field | Type | Required | Description |
|---|---|---|---|
| `error` | string | Yes | Machine-readable error code |
| `message` | string | Yes | Human-readable description of the error |
| `category` | string | Yes | Error category for programmatic classification |
| `retryable` | boolean | Yes | Whether the client should retry the request |
| `details` | object | No | Additional context (e.g., which field failed validation, remaining quota) |

```json
{
  "error": "ENTITLEMENT_EXHAUSTED",
  "message": "All lease slots for this entitlement are currently in use.",
  "category": "quota",
  "retryable": true,
  "details": {
    "entitled": 4,
    "active": 4
  }
}
```

## Error Categories

Errors are grouped into categories that indicate the nature of the failure:

| Category | Description | Typical HTTP Status | Retryable |
|---|---|---|---|
| `validation` | Request is malformed or missing required fields | 400 | No (fix the request) |
| `authentication` | Caller identity could not be verified | 401 | No (fix credentials) |
| `authorization` | Caller does not have permission for this operation | 403 | No |
| `not_found` | Referenced resource (lease, entitlement) does not exist | 404 | No |
| `conflict` | Operation conflicts with current state (e.g., lease already revoked, reissue already in progress) | 409 | No (resolve conflict) |
| `quota` | Entitlement quota is exhausted | 429 or 403 | Yes (after a lease is released) |
| `identity` | Identity evidence verification failed | 403 | No (fix identity) |
| `policy` | Request violates a policy constraint (e.g., modality not permitted, environment not allowed) | 403 | No (adjust request) |
| `expired` | Referenced resource has expired (lease, cutover token, reissue deadline) | 410 | No |
| `internal` | Unexpected control plane error | 500 | Yes (with backoff) |
| `unavailable` | Control plane is temporarily unavailable | 503 | Yes (with backoff) |

## Standard Error Codes

The following error codes are defined for the canonical API operations:

### Issue Errors

| Error Code | Category | Description |
|---|---|---|
| `ENTITLEMENT_NOT_FOUND` | not_found | Tenant has no entitlement for the requested application |
| `ENTITLEMENT_EXHAUSTED` | quota | All lease slots are in use |
| `DIMENSIONS_EXCEEDED` | policy | Requested dimensions exceed entitlement limits |
| `MODALITY_NOT_PERMITTED` | policy | Requested license modality is not available |
| `ENVIRONMENT_NOT_PERMITTED` | policy | Requested environment tag is not allowed |
| `IDENTITY_VERIFICATION_FAILED` | identity | Identity evidence could not be verified |

### Renew Errors

| Error Code | Category | Description |
|---|---|---|
| `LEASE_NOT_FOUND` | not_found | Lease does not exist |
| `LEASE_REVOKED` | conflict | Lease has been revoked and cannot be renewed |
| `LEASE_EXPIRED` | expired | Lease has expired beyond the grace period |
| `IDENTITY_MISMATCH` | identity | Workload identity does not match the lease binding |
| `ENTITLEMENT_REVOKED` | conflict | Underlying entitlement has been revoked |

### Reissue Errors

| Error Code | Category | Description |
|---|---|---|
| `LEASE_NOT_FOUND` | not_found | Original lease does not exist |
| `LEASE_NOT_ACTIVE` | conflict | Original lease is not in an active state |
| `REISSUE_ALREADY_PENDING` | conflict | A reissue is already in progress for this lease |
| `IDENTITY_VERIFICATION_FAILED` | identity | Target workload identity could not be verified |
| `REISSUE_NOT_FOUND` | not_found | Reissue operation does not exist (finalize phase) |
| `CUTOVER_TOKEN_INVALID` | authentication | Cutover token does not match or has expired |
| `REISSUE_DEADLINE_EXPIRED` | expired | Reissue was not finalized within the allowed time window |

### Revoke Errors

| Error Code | Category | Description |
|---|---|---|
| `LEASE_NOT_FOUND` | not_found | Lease does not exist |
| `LEASE_ALREADY_REVOKED` | conflict | Lease has already been revoked |
| `REVOKE_NOT_AUTHORIZED` | authorization | Requester does not have permission to revoke |

### Usage Record Errors

| Error Code | Category | Description |
|---|---|---|
| `LEASE_NOT_FOUND` | not_found | Referenced lease does not exist |
| `INVALID_DIMENSION` | validation | Reported dimension is not recognized for this product |
| `INVALID_TIMESTAMP` | validation | Timestamp is malformed or outside acceptable range |

## License Agent Behavior on Errors

The license agent should handle errors based on the `category` and `retryable` fields:

| Scenario | Agent Behavior |
|---|---|
| `retryable: true` | Retry with exponential backoff and jitter (per `renewBackoff` policy) |
| `retryable: false`, category `validation` | Log the error; do not retry; alert the operator |
| `retryable: false`, category `identity` | Log the error; do not retry; the workload identity configuration needs attention |
| `retryable: false`, category `conflict` (lease revoked) | Treat as revocation; apply exhaustion action |
| `retryable: false`, category `quota` | Wait for capacity; optionally alert the operator |
| `retryable: false`, category `expired` | Treat as terminal; a new Issue is required |
| Category `internal` or `unavailable` | Retry with backoff; if retries are exhausted, enter grace period logic |

## Security Considerations

Error responses must not expose:

- Internal infrastructure details (e.g., database names, Lambda function ARNs, stack traces).
- Information about other tenants or their entitlements.
- Detailed cryptographic failure reasons that could aid an attacker.

The `message` field should be informative enough for debugging but generic enough to avoid information leakage.

## Relationship to Other Chapters

- Each API operation (Issue, Renew, Reissue, Revoke, Usage Record) references this error model for its failure cases.
- The grace policy (defined in the reference model) governs how the license agent behaves when errors prevent renewal.
- The audit log records both successful and failed operations, including the error code.
