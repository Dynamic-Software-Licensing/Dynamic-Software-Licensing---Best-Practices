# 07.07. Responsibility Model

## Purpose

This section defines which participant or component is responsible for which aspect of the Dynamic Software Licensing model. It clarifies the boundaries between vendors (ISVs), customers, system integrators (SIs), the control plane, and the workspace plane to avoid ambiguity in implementation and operation.

## Participants

The DSL model involves the following participants:

| Participant | Role |
| --- | --- |
| Independent Software Vendor (ISV) | Produces the licensed application; defines entitlement catalogs, dimensions, pricing, and default policies |
| Customer | Consumes the licensed application; manages workloads, monitors usage, and controls spend |
| System Integrator (SI) | Deploys and integrates licensed applications on behalf of customers; automates licensing via IaC |
| Control Plane Operator | Operates the licensing control plane infrastructure (may be the ISV, a shared service, or a managed platform) |
| Workspace Operator | Operates the runtime environment where applications and license agents run (typically the customer or SI) |

## Responsibility Matrix

### Entitlement Lifecycle

| Responsibility | ISV | Customer | SI | Control Plane |
| --- | --- | --- | --- | --- |
| Define product catalog and dimensions | Owns | | | |
| Define pricing and modalities | Owns | | | |
| Define default policies (grace, renewal, exhaustion) | Owns | | | |
| Provision entitlements for a tenant | Initiates (direct sale) | Initiates (self-service or marketplace) | Initiates (on behalf of customer) | Stores and enforces |
| Request entitlement changes (upgrade, downgrade) | | Requests | Requests | Processes |
| Approve entitlement overrides (e.g., extended grace) | Approves | Requests | Requests (on behalf of customer) | Applies |
| Monitor entitlement utilization | | Monitors | Monitors | Provides data |

### Lease Lifecycle

| Responsibility | License Agent | Control Plane | Application/SDK | Customer/Ops | SI |
| --- | --- | --- | --- | --- | --- |
| Collect identity evidence | Owns | | | | |
| Request lease (ISSUE) | Initiates | Validates and issues | | | |
| Deliver token to application | Delivers | | Receives | | |
| Validate token signature and claims | | | Owns | | |
| Enforce dimension limits | | | Owns | | |
| Schedule and execute renewal (RENEW) | Initiates | Validates and extends | | | |
| Initiate reissue for failover (REISSUE) | Initiates | Creates shadow, finalizes | | Triggers (manual or automated) | Triggers (automated via IaC/orchestration) |
| Handle revocation event | Receives and acts | Pushes event | Executes exhaustion action | Monitors | Monitors |
| Apply grace policy on connectivity loss | Enforces | | Enforces locally | Monitors | Monitors |

### Usage and Metering

| Responsibility | License Agent | Control Plane | Customer | ISV | SI |
| --- | --- | --- | --- | --- | --- |
| Collect usage events | Owns | | | | |
| Buffer usage during connectivity loss | Owns | | | | |
| Submit usage records | Submits | Receives and stores | | | |
| Provide usage analytics and reports | | Owns | Consumes | Consumes | Consumes (on behalf of customer) |
| Reconcile usage with billing | | Provides data | Reviews | Reconciles | Reviews (on behalf of customer) |
| Mirror usage to marketplace or back-office | | Owns (via Vendor Adapter) | | Receives | |
| Dispute or query usage discrepancies | | Provides audit data | Raises | Responds | Raises (on behalf of customer) |

### Security and Trust

| Responsibility | Control Plane | License Agent | Application/SDK | ISV | Customer | SI |
| --- | --- | --- | --- | --- | --- | --- |
| Manage signing keys | Owns | | | | | |
| Sign lease tokens | Owns | | | | | |
| Publish JWKS public keys | Owns | | | | | |
| Validate token signatures | | | Owns | | | |
| Present identity evidence | | Owns | | | | |
| Verify identity evidence | Owns | | | | | |
| Enforce TLS for all communication | Enforces | Enforces | | | Enforces (infrastructure) | Enforces (infrastructure) |
| Maintain audit logs | Owns | | | | Reviews | Reviews (on behalf of customer) |
| Define security policies | | | | Defines | Overrides (if permitted) | Advises customer |
| Monitor for anomalies | Monitors | | | Monitors | Monitors | Monitors (on behalf of customer) |
| Manage network security (VPN, private endpoints) | Supports | | | | Configures | Configures (on behalf of customer) |

### Deployment and Integration

| Responsibility | ISV | SI | Customer | Control Plane |
| --- | --- | --- | --- | --- |
| Provide IaC modules (Terraform/CFN) | Provides | Extends and customizes | | |
| Include licensing in deployment automation | | Integrates | Integrates (if self-deploying) | |
| Provide license agent binaries/packages | Provides | Distributes to customer environments | | |
| Provide application SDK | Provides | | Integrates (if building custom apps) | |
| Configure license agent for the environment | | Configures | Configures (if self-managing) | |
| Operate the control plane | Operates (or shared) | | | Operates |
| Operate the workspace environment | | Operates (on behalf of customer) | Operates (if self-managing) | |
| Provide CI/CD integration examples | Provides | Provides | | |
| Troubleshoot licensing issues in deployment | Supports (product-level) | Troubleshoots (environment-level) | Reports issues | Provides diagnostics |

### End User Portal

| Responsibility | Control Plane | Customer | ISV | SI |
| --- | --- | --- | --- | --- |
| Provide portal interface | Provides (or ISV) | | Provides (or shared) | |
| View license status and usage | | Views | Views | Views (on behalf of customer) |
| Force-release stuck licenses | | Executes | | Executes (on behalf of customer) |
| Request additional capacity | | Requests | Approves | Requests (on behalf of customer) |
| Configure alerts and notifications | | Configures | | Configures (on behalf of customer) |
| Provide multi-vendor aggregated view | Provides | Consumes | Contributes data | Consumes (on behalf of customer) |
| Onboard new vendor products into portal | Provides integration | | Registers products | Coordinates |

## Responsibility Boundaries

### Vendor (ISV) Boundary

The vendor is responsible for:
- Defining what is licensed (products, dimensions, modalities).
- Setting the rules of licensing (policies, grace periods, exhaustion actions).
- Providing the tools for integration (SDK, license agent, IaC modules).
- Providing detailed usage reports to the customer.

The vendor is not responsible for:
- Operating the customer's workloads.
- Managing the customer's infrastructure or identity systems.
- Making runtime enforcement decisions (these are delegated to the application logic, using claims exposed by the license token and SDK).

### Customer Boundary

The customer is responsible for:
- Operating their workloads and ensuring the license agent is deployed.
- Presenting valid identity evidence from their runtime environment.
- Monitoring their license usage and managing spend.
- Responding to alerts and managing capacity for events.

The customer is not responsible for:
- Defining licensing terms or policies (though they may request overrides).
- Operating the control plane (unless self-hosted).
- Implementing the SDK or license agent (these are provided by the vendor).

### System Integrator Boundary

The SI is responsible for:
- Deploying and configuring licensed applications in the customer's environment.
- Integrating licensing into IaC and CI/CD pipelines.
- Providing operational support for licensing workflows.
- Acting on behalf of the customer for provisioning, capacity requests, monitoring, and troubleshooting where the SI is the engaged operational partner.
- Advising the customer on policy settings, modality choices, and capacity planning.

The SI is not responsible for:
- Defining licensing terms (these are set by the ISV).
- Operating the control plane.
- Developing the SDK or license agent.
- Approving entitlement changes (this remains with the ISV).

### Control Plane Boundary

The control plane is responsible for:
- All licensing decisions (issuance, renewal, reissue, revocation).
- Key management and token signing.
- Usage recording and analytics.
- Audit logging and compliance data.
- Push notifications for revocation and policy updates.

The control plane is not responsible for:
- Running application workloads.
- Enforcing dimensions at runtime (this is the application logic's responsibility, with the SDK exposing the granted claims).
- Managing the customer's infrastructure.

## Shared Responsibilities

Some responsibilities are shared between participants:

| Area | Shared Between | Nature of Sharing |
| --- | --- | --- |
| Policy definition | ISV + Customer (+ SI as advisor) | Vendor sets defaults; customer may request overrides; SI advises on appropriate settings |
| Entitlement provisioning | ISV + Customer + SI | Any party may initiate depending on the commercial relationship |
| Deployment automation | ISV + SI + Customer | Vendor provides modules; SI integrates and customizes; customer may self-integrate |
| Security monitoring | Control Plane + Customer + ISV + SI | Each monitors their own boundary; SI monitors on behalf of customer where engaged |
| Usage reconciliation | Control Plane + ISV + Customer + SI | Control plane provides data; ISV and customer reconcile; SI may review on customer's behalf |
| Observability | Control Plane + Customer + SI | Control plane provides metrics and logs; customer or SI integrates into monitoring |
| Troubleshooting | ISV + SI + Control Plane | ISV handles product issues; SI handles environment issues; control plane provides diagnostics |

## Platform Neutrality

This responsibility model applies regardless of the underlying platform. The specific tools and services used by each participant vary by environment, but the allocation of responsibilities remains consistent across cloud, hybrid, and on-premises deployments.
