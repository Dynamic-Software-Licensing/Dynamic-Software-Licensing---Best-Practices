# 07.05. End User Portal

## Purpose

This section describes the role of an end-user-facing management interface within the Dynamic Software Licensing model. The End User Portal provides aggregated visibility, self-service capabilities, and operational controls for customers managing licenses across one or more vendors.

## Role in the Architecture

The End User Portal is a cross-cutting component that sits above the control plane and workspace plane. It does not participate in the runtime licensing flow (token issuance, renewal, or validation). Instead, it provides a human-facing layer for:

- Viewing and managing license entitlements and active leases.
- Monitoring usage and capacity across vendors and applications.
- Performing self-service operations (e.g., releasing a stuck license, ordering additional capacity).
- Supporting financial and operational decision-making.

## Core Capabilities

### Multi-Vendor Aggregation

Customers in broadcast and media workflows typically use products from multiple ISVs. The portal provides a unified view across all vendors, showing:

- Active entitlements per vendor and product.
- Current lease status (active, expired, revoked) per workload.
- Dimension utilization (e.g., 3 of 4 licensed channels in use).
- License modality and renewal schedule.

This eliminates the need to log into separate vendor portals to understand overall licensing posture.

### Real-Time License Status

The portal reflects the current state of the licensing system:

- Which leases are active and on which workloads.
- Remaining capacity (available entitlements not yet leased).
- Upcoming expirations and renewal deadlines.
- Feature flags and dimension limits per active lease.

Data is sourced from the control plane's lease and entitlement records.

### Self-Service Operations

The portal enables customers to perform operational actions without contacting the vendor or SI:

| Operation | Description |
| --- | --- |
| Force release | Release a license from a failed or terminated instance, returning it to the available pool |
| View history | Review lease history, including issuance, renewals, reissues, and revocations |
| Request capacity | Initiate a request for additional entitlements or dimension increases |
| Cancel / downgrade | Request cancellation or reduction of entitlements (subject to vendor approval) |
| Alert configuration | Set notification preferences for expiry warnings, grace period triggers, and usage thresholds |

### Usage and Financial Visibility

The portal provides data to support cost management and forecasting:

- Usage summaries by application, dimension, time period, and environment tag (production, staging, dev).
- Cost breakdowns mapped to licensing dimensions and modalities.
- Cost estimation for pre-production planning.
- Historical usage trends for capacity planning.
- Export capabilities for integration with financial systems and reporting tools.

### Emergency Operations

For production-critical scenarios, the portal supports:

- Forced license release when a workload has terminated without proper revocation.
- Visibility into grace period status for workloads experiencing connectivity issues.
- Rapid capacity burst requests for unplanned scaling events.

## Personas Served

The End User Portal serves multiple personas within a customer organization:

| Persona | Primary Use |
| --- | --- |
| Operations team | Monitor active leases, release stuck licenses, verify feature availability |
| Finance officer | Review usage costs, forecast spend, audit license compliance |
| License manager | Compare models, track pool utilization, manage renewals |
| Director of engineering | Plan capacity for events, monitor burst usage, review cross-vendor posture |
| Broadcast engineer | Check license status for assigned workloads, verify dimension limits |

## Interaction with the Control Plane

The portal interacts with the control plane through the same API surface used by license agents, plus additional administrative and reporting endpoints:

- Read entitlements and lease status via query APIs.
- Invoke revocation for force-release operations.
- Access usage and analytics data from the reporting layer.
- Receive event notifications for status changes.

The portal does not bypass the control plane's authorization model. All operations are subject to the same authentication, tenant isolation, and audit logging.

## Interface Considerations

### Multi-Interface Support

The portal complements (but does not replace) the API and CLI interfaces. Customers who prefer programmatic access can achieve the same outcomes through the API. The portal provides a visual layer for scenarios where a graphical overview is more effective.

## Platform Neutrality

The End User Portal is described as a functional capability, not a specific technology. It may be implemented as a web application, integrated into an existing operations dashboard, or provided as a vendor-hosted service. The key requirement is that it surfaces the data and operations described above in a way that is accessible to the personas it serves.
