# 04.04. Operational Terms

## Purpose

This section defines lifecycle transitions, operational workflows, observability mechanisms, and migration tracking vocabulary used in practical deployment scenarios.

## Scope Statement

This section aligns the abstract conceptual framework with real-world production environments and deployment runbooks. It centers on target-state capabilities and transition states without endorsing the permanent use of legacy approaches.

---

## Definitions

**Air-Gapped** - A strict deployment context running within restricted networks entirely separated from the open internet, requiring special local trust validation boundaries and offline sync behavior.

**Failover Auto-Mobility** - The ability of an active license lease to move seamlessly from a failing primary instance to a secondary high-availability (HA) or disaster recovery (DR) instance through automation, completely eliminating manual ISV support intervention.

**Headless Activation** - A completely programmatic, scriptable path to request, bind, and activate a license lease without needing interactive user sessions, graphical interfaces, or manual input.

**Lifecycle Operations** - The complete programmatic sequence of runtime states, transition paths, and compliance validations that a license entitlement and its associated active leases navigate through from initial activation to eventual expiration or retirement.

**Observability** - The structural capability providing real-time transparency, audit logging, and diagnostics regarding active lease allocations, consumption trends, and cost distribution.

**Parallel Operation (Pilot Phase)** - A transitional migration phase where a customer securely deploys and runs legacy licensing mechanisms side by side with the modern DSL target framework to de-risk technical transformation.
