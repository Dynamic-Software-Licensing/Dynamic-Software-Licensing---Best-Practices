# 11.04. Usage Event Object

## Purpose

This section defines the canonical usage event object used for metering and reporting in the
DSL model. The usage event object records a unit of consumption associated with a granted lease
or equivalent runtime context.

## Role of the Usage Event Object

The usage event object provides the canonical structure for:

- usage-based billing and reconciliation,
- operational visibility into consumed dimensions,
- post-outage usage replay,
- analytics and audit correlation.

Usage events are reporting artifacts. They support accounting and visibility, but they are not
the primary runtime grant themselves.

## Canonical Structure

| Field | Type | Description |
| --- | --- | --- |
| `leaseId` | string | Lease to which the usage applies |
| `tenantId` | string | Tenant context |
| `productId` | string | Application or product identifier |
| `dimension` | string | Metered dimension name |
| `quantity` | number | Amount consumed |
| `granularity` | string | Measurement granularity or unit |
| `timestamp` | string | Time at which the usage occurred |
| `workId` | string | Correlation identifier for deployment or workflow |
| `submittedAt` | string | Time the usage event reached the control plane |

## Required Semantics

### Attribution

Each usage event must be attributable to a tenant, product, and lease or equivalent grant
context. The event should be sufficiently correlated to support operational and financial
reconciliation.

### Deduplication

Usage event semantics must support idempotent replay. Retried or delayed events must not create
double counting if the same logical event is submitted more than once.

### Separation from enforcement

Usage events should describe consumption, not directly carry authority. The authoritative grant
remains the lease and its signed token.

## Example Shape

```json
{
 "leaseId": "L-01HY6G1Q3Z5W6E3Z2N7X0",
 "tenantId": "tenant-a",
 "productId": "app-A",
 "dimension": "HOURS",
 "quantity": 1,
 "granularity": "minutes",
 "timestamp": "2026-08-12T10:15:00Z",
 "workId": "deploy-i-0abc123def456"
}
```

## Relationship to Other Objects

- The lease object provides the grant context for the usage event.
- The entitlement object defines which dimensions may be reported meaningfully.
- The policy object may govern heartbeat or submission cadence.

## Section Positioning

This object is the canonical reporting unit for consumption-based DSL behavior. It provides the
data-model bridge between runtime operation and billing, analytics, or audit workflows.
