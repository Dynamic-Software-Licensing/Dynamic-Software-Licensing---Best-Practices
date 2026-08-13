# 10.06. Usage Record

## Purpose

This section defines the usage reporting interaction within the canonical API. The Usage Record operation allows license agents and SDKs to submit metered consumption events to the control plane for billing, analytics, and compliance purposes.

## When Usage Record Is Used

The Usage Record operation is invoked:

- Periodically by the license agent during normal operation (e.g., per-minute heartbeats).
- At session boundaries (session start/stop events).
- After connectivity is restored, to upload buffered usage events that were collected during an outage.

Usage recording is a continuous background operation. It does not affect the application's ability to operate — it is a reporting function, not an enforcement function.

## Endpoint

```http
POST /v1/usage-records
```

## Interaction Flow

1. The license agent or SDK collects usage data during operation (e.g., minutes of active use, sessions, process units).
2. At the configured interval, the license agent sends a POST request to `/v1/usage-records`.
3. The control plane validates and stores the usage event:
   - Hot store for operational queries and near-real-time dashboards.
   - Cold store (e.g., data lake) for long-term analytics, billing reconciliation, and reporting.
4. The control plane acknowledges receipt.

### During Connectivity Loss

1. The license agent buffers usage events locally.
2. When connectivity is restored, the license agent uploads all buffered events.
3. The control plane processes them idempotently — duplicate submissions (same timestamp, lease, dimension) are deduplicated, preventing double counting.

## Request Structure

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `leaseId` | string | Yes | Identifier of the active lease |
| `tenantId` | string | Yes | Tenant identifier |
| `productId` | string | Yes | Application identifier |
| `dimension` | string | Yes | The metered dimension being reported (e.g., `"HOURS"`, `"SESSIONS"`, `"PROCESS_UNITS"`) |
| `quantity` | number | Yes | Amount consumed |
| `granularity` | string | Yes | Time granularity of the measurement (e.g., `"minutes"`, `"hours"`) |
| `timestamp` | string (ISO 8601) | Yes | When the usage occurred |
| `workId` | string | Yes | Correlation identifier for the deployment |

```json
{
  "leaseId": "L-...",
  "tenantId": "t-123",
  "productId": "app-A",
  "dimension": "HOURS",
  "quantity": 1,
  "granularity": "minutes",
  "timestamp": "2025-10-13T16:15:00Z",
  "workId": "deploy-i-0abc123def456"
}
```

## Response Structure

A successful response acknowledges receipt:

```json
{
  "status": "accepted"
}
```

The control plane does not return detailed processing results in the synchronous response. Analytics and aggregated usage data are available through the reporting layer and End User Portal.

## Usage Dimensions

Usage dimensions align with the dimension model defined in the entitlement and lease. Common usage dimensions include:

| Dimension | Description | Typical Granularity |
| --- | --- | --- |
| `HOURS` | Time-based usage | Per minute or per hour |
| `SESSIONS` | Session-based usage (start/stop) | Per session |
| `CHANNELS` | Active channel count over time | Per minute |
| `PROCESS_UNITS` | Normalized compute units (transcoding, inference, pixel operations) | Per operation or per minute |
| `BANDWIDTH` | Data throughput | Per GB or per minute |
| `CLIPS` | Outcome-based (e.g., generated clips, subtitles) | Per item |

Vendors define which dimensions apply to their products. The canonical model does not prescribe a fixed set — it provides the structure for any dimension to be reported.

## Idempotency

Usage records support idempotent submission through the combination of:

- `leaseId` + `timestamp` + `dimension` as a natural deduplication key.
- The `workId` for additional correlation.

This ensures that retried submissions (e.g., after a network timeout where the agent is unsure if the original request was received) do not result in double counting.

## License Modality Compatibility

The usage recording model is designed to be compatible with marketplace-style metering. This means:

- Usage events can be mirrored to an ISV's back-office billing system via the optional Vendor Adapter.
- Usage events can be mapped to marketplace metering APIs where applicable.
- The dimension and quantity structure aligns with common marketplace metering schemas.

## Audit

Usage events are stored with full traceability:

- Tenant, application, and lease identifiers.
- Timestamp and dimension details.
- Work ID for deployment correlation.
- Submission timestamp (when the event was received, which may differ from the usage timestamp if buffered).

## Relationship to Other Operations

- Usage recording runs alongside the Renew cycle but is independent of it. A failed renewal does not prevent buffered usage from being submitted later.
- Usage data informs the analytics and reporting available through the End User Portal.
- Usage reconciliation is a shared responsibility between the control plane, ISV, and customer (as defined in the responsibility model).
