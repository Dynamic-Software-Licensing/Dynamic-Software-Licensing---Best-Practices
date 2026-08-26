# 10.08. Error Model

## Purpose

This section defines the structure of API error handling within the canonical API. It describes how failures, rejected requests, and non-successful outcomes are expressed consistently across all operations.

## Standards Compliance

This error model implements [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) (the successor to RFC 7807). All error responses use the `application/problem+json` media type.

## Design Principles

The error model follows these principles:

1. Consistency: all operations use the same RFC 9457 error response structure.
2. Actionability: errors include enough information for the license agent or operator to determine the appropriate next step.
3. Machine-readability: error types are URIs for programmatic handling; extension members provide structured context.
4. Security: error responses do not leak sensitive information about the control plane's internal state, other tenants, or infrastructure details.

## Error Response Structure

All failed API requests return a JSON response with `Content-Type: application/problem+json` following RFC 9457:

| Field | Type | Required | Source | Description |
| --- | --- | --- | --- | --- |
| `type` | string (URI) | Yes | RFC 9457 | URI identifying the error type (e.g., `urn:dsl:error:entitlement-exhausted`) |
| `title` | string | Yes | RFC 9457 | Short, human-readable summary of the problem type |
| `status` | integer | Yes | RFC 9457 | HTTP status code |
| `detail` | string | Yes | RFC 9457 | Human-readable explanation specific to this occurrence |
| `instance` | string (URI) | No | RFC 9457 | URI identifying the specific occurrence (for support correlation) |
| `category` | string | Yes | DSL extension | Error category for programmatic classification |
| `retryable` | boolean | Yes | DSL extension | Whether the client should retry the request |

Additional context relevant to the specific error type MAY be included as extension members at the top level of the response object, as permitted by RFC 9457.

```json
{
  "type": "urn:dsl:error:entitlement-exhausted",
  "title": "Entitlement Exhausted",
  "status": 429,
  "detail": "All lease slots for this entitlement are currently in use.",
  "instance": "urn:dsl:request:req-8f3a2b",
  "category": "quota",
  "retryable": true,
  "entitled": 4,
  "active": 4
}
```

## Error Categories

Errors are grouped into categories that indicate the nature of the failure:

| Category | Description | Typical HTTP Status | Retryable |
| --- | --- | --- | --- |
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

## Standard Error Types

The following error types are defined for the canonical API operations. Each `type` URI follows the pattern `urn:dsl:error:<error-name>`.

### Issue Errors

| Type URI | Category | Title | HTTP Status |
| --- | --- | --- | --- |
| `urn:dsl:error:entitlement-not-found` | not_found | Entitlement Not Found | 404 |
| `urn:dsl:error:entitlement-exhausted` | quota | Entitlement Exhausted | 429 |
| `urn:dsl:error:dimensions-exceeded` | policy | Dimensions Exceeded | 403 |
| `urn:dsl:error:modality-not-permitted` | policy | Modality Not Permitted | 403 |
| `urn:dsl:error:environment-not-permitted` | policy | Environment Not Permitted | 403 |
| `urn:dsl:error:identity-verification-failed` | identity | Identity Verification Failed | 403 |

### Renew Errors

| Type URI | Category | Title | HTTP Status |
| --- | --- | --- | --- |
| `urn:dsl:error:lease-not-found` | not_found | Lease Not Found | 404 |
| `urn:dsl:error:lease-revoked` | conflict | Lease Revoked | 409 |
| `urn:dsl:error:lease-expired` | expired | Lease Expired | 410 |
| `urn:dsl:error:identity-mismatch` | identity | Identity Mismatch | 403 |
| `urn:dsl:error:entitlement-revoked` | conflict | Entitlement Revoked | 409 |

### Reissue Errors

| Type URI | Category | Title | HTTP Status |
| --- | --- | --- | --- |
| `urn:dsl:error:lease-not-found` | not_found | Lease Not Found | 404 |
| `urn:dsl:error:lease-not-active` | conflict | Lease Not Active | 409 |
| `urn:dsl:error:reissue-already-pending` | conflict | Reissue Already Pending | 409 |
| `urn:dsl:error:identity-verification-failed` | identity | Identity Verification Failed | 403 |
| `urn:dsl:error:reissue-not-found` | not_found | Reissue Not Found | 404 |
| `urn:dsl:error:cutover-token-invalid` | authentication | Cutover Token Invalid | 401 |
| `urn:dsl:error:reissue-deadline-expired` | expired | Reissue Deadline Expired | 410 |

### Revoke Errors

| Type URI | Category | Title | HTTP Status |
| --- | --- | --- | --- |
| `urn:dsl:error:lease-not-found` | not_found | Lease Not Found | 404 |
| `urn:dsl:error:lease-already-revoked` | conflict | Lease Already Revoked | 409 |
| `urn:dsl:error:revoke-not-authorized` | authorization | Revoke Not Authorized | 403 |

### Usage Record Errors

| Type URI | Category | Title | HTTP Status |
| --- | --- | --- | --- |
| `urn:dsl:error:lease-not-found` | not_found | Lease Not Found | 404 |
| `urn:dsl:error:invalid-dimension` | validation | Invalid Dimension | 400 |
| `urn:dsl:error:invalid-timestamp` | validation | Invalid Timestamp | 400 |

## License Agent Behavior on Errors

The license agent SHOULD handle errors based on the `category` and `retryable` extension members:

| Scenario | Agent Behavior |
| --- | --- |
| `retryable: true` | Retry with exponential backoff and jitter (per `renewBackoff` policy) |
| `retryable: false`, category `validation` | Log the error; do not retry; alert the operator |
| `retryable: false`, category `identity` | Log the error; do not retry; the workload identity configuration needs attention |
| `retryable: false`, category `conflict` (lease revoked) | Treat as revocation; apply exhaustion action |
| `retryable: false`, category `quota` | Wait for capacity; optionally alert the operator |
| `retryable: false`, category `expired` | Treat as terminal; a new Issue is required |
| Category `internal` or `unavailable` | Retry with backoff; if retries are exhausted, enter grace period logic |

The `instance` field, when present, SHOULD be included in support tickets or log entries to enable the control plane operator to correlate the error with server-side diagnostics.

## Security Considerations

Error responses MUST NOT expose:

- Internal infrastructure details (e.g., database names, Lambda function ARNs, stack traces).
- Information about other tenants or their entitlements.
- Detailed cryptographic failure reasons that could aid an attacker.

The `detail` field SHOULD be informative enough for debugging but generic enough to avoid information leakage. The `instance` field SHOULD use opaque identifiers (not internal resource paths).

## Relationship to Other Chapters

- Each API operation (Issue, Renew, Reissue, Revoke, Usage Record) references this error model for its failure cases.
- The grace policy (defined in the reference model) governs how the license agent behaves when errors prevent renewal.
- The audit log records both successful and failed operations, including the error `type`.
- The `application/problem+json` content type is defined by [RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html) and supersedes the earlier RFC 7807.
