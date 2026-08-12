# 05.04 Derived Requirement Themes

## Purpose

This section summarizes the recurring requirement themes that emerge from the stakeholder
groups (Section 5.1), persona perspectives (Section 5.2), and use case classes (Section 5.3).
A requirement theme is a clustered statement of need: a recurring concern that appears across
multiple personas or use case classes and that later chapters translate into structured,
normative requirements.

The themes are the analytical bridge between *needs* and *requirements*. They explain why
later requirement groups exist and provide the rationale against which those requirements can
be evaluated.

## Method and Input Basis

The themes below are derived by aggregation. Where a concern appears repeatedly across
distinct personas, use case classes, or industry challenges, it is consolidated into a single
theme rather than restated per source. The inputs are:

- the role-level success criteria and licensing perspectives in Section 5.2,
- the licensing pressures attached to each use case class in Section 5.3,
- team prework (including the Miro workshop material), in particular the high-impact,
  low-overhead problem statements that were worked into candidate workflows,
- the recurring industry challenges identified during the initiative's early analysis
  (summarized in the challenge mapping below),
- the cross-persona tensions named in Section 5.2.

The themes are intentionally a stable, modest-sized set. They are not requirements
themselves. They do not use normative keywords, and they do not specify API-level or
schema-level behavior. Final normative language is reserved for the normative requirements
chapter.

## Theme Schema

Each theme is specified using the same structure:

- **Theme statement** — the consolidated need in one or two sentences.
- **Originating concerns** — the personas, use case classes, and challenges that give rise to
  the theme.
- **What good looks like** — the observable characteristics that would indicate the theme is
  satisfied, expressed descriptively rather than as requirements.
- **Forward traceability** — the normative requirement group(s) expected to carry the theme
  into formal requirements.

## Requirement Themes

Ten requirement themes are defined.

### T1. Automation and Licensing-as-Code

**Theme statement**

Licensing operations must be expressible and executable as code, so that issuing, renewing,
moving, and releasing licenses can be embedded in infrastructure provisioning and
deployment pipelines without manual steps.

**Originating concerns**

Operations and DevOps Engineer, SI Solution Architect, SI Developer, CTO; the Test and
Validation and Event-Driven use case classes; the "IaC integration gap", "manual setup
processes", and "headless activation gap" challenges.

**What good looks like**

- License lifecycle steps are part of infrastructure-as-code modules and CI/CD pipelines.
- Activation requires no interactive console step and no manual vendor intervention.
- Environments can be created, recovered, and torn down repeatably, including licensing.

**Forward traceability**

General requirements; integration requirements; API requirements.

### T2. Standardized Lifecycle and Interfaces

**Theme statement**

The licensing lifecycle — issue, renew, reissue, revoke, inspect, and usage reporting — must
have consistent, standardized semantics and be accessible through both programmatic and
command-line interfaces.

**Originating concerns**

SI Solution Architect, ISV Licensing Architect, Operations and DevOps Engineer, Industry
Standards Representative; all use case classes; the "missing standard APIs",
"vendor-specific processes", and "CLI/API access gap" challenges.

**What good looks like**

- Lifecycle operations behave consistently across products and vendors.
- The same operations are reachable via API and CLI, suited to different maturity levels.
- Integrators can reuse lifecycle patterns across projects with low customization.

**Forward traceability**

API requirements; general requirements.

### T3. Identity-Based Binding and License Mobility

**Theme statement**

Licenses must bind to verifiable workload identity rather than to static host attributes, so
that entitlements can move between instances and environments to support failover, blue/green
cutover, and hybrid operation.

**Originating concerns**

Director of Engineering, Broadcast Director / Engineer, Platform SRE, Security and Compliance
Lead; the Continuous Operations class and the Resilience and Continuity overlay; the "hardware
binding issues", "license mobility", and "manual ISV intervention" challenges.

**What good looks like**

- Binding uses workload identity evidence, not hostnames or MAC addresses.
- An active entitlement can follow active and standby workloads without downtime or vendor
  involvement.
- Hybrid and disaster-recovery designs are supported by portable binding.

**Forward traceability**

Identity and binding requirements; lease and policy requirements.

### T4. License Modality and Commercial Flexibility

**Theme statement**

The model must support multiple commercial and consumption modalities — time-based (including
fine-grained durations), process-based, and outcome-based — and allow them to be combined
without creating opaque portfolio complexity.

**Originating concerns**

Finance and Procurement Lead, ISV Product and Commercial Owner, License Manager, Procurement;
all use case classes, especially Infrequent Event-Driven and AI/Outcome-Based; the "business
model misalignment", "model transition challenges", and "portfolio complexity" challenges.

**What good looks like**

- Modalities span perpetual, annual, monthly, weekly, daily, hourly, process-unit, and
  outcome-based forms.
- OpEx-oriented models (pre-pay, post-pay, burn-down, point-based) and CapEx/perpetual models
  can coexist in one account landscape.
- Granularity can be selected to match the use case without forcing a single model.

**Forward traceability**

License modality requirements; metering requirements.

### T5. Usage-Based Metering and Cost Transparency

**Theme statement**

Usage must be metered through expressive dimensions and surfaced transparently, so that
consumption can be attributed, forecast, and reconciled, and so that licensing cost is clearly
distinguishable from platform cost.

**Originating concerns**

Finance and Procurement Lead, ISV Product and Commercial Owner, SI Commercial and Reselling
Lead; the AI/Outcome-Based and Event-Driven classes; the "cost transparency" and "usage type
differentiation" challenges; the Miro cost-predictability and cost-usage problem statements.

**What good looks like**

- Dimensions capture time, capacity, process units, and outcomes as appropriate.
- Usage can be attributed by project, show, environment, and cost center.
- Licensing cost is reported separately from underlying platform cost, with forecasting
  inputs and historical reconciliation.

**Forward traceability**

Metering requirements; license modality requirements.

### T6. Observability and Self-Service

**Theme statement**

Stakeholders must have clear visibility into allocation, usage, limits, expiry, and forecast,
and must be able to perform routine actions — including releasing licenses back to the pool
and adding capacity — without vendor involvement.

**Originating concerns**

Operations and DevOps Engineer, License Manager, ISV Support and Customer Success Lead,
Finance and Procurement Lead; the Continuous and Test and Validation classes; the "end user
portal absence", "self-service capabilities", and "cost transparency" needs; the Miro
license-inventory query problem statement.

**What good looks like**

- Active allocations, remaining capacity, feature flags, and expiry are visible across
  vendors, ideally through a unified view.
- Operators can release orphaned or failed-instance licenses and add capacity themselves.
- Advance expiry warnings prevent surprises during production windows.

**Forward traceability**

Operational requirements; general requirements; metering requirements.

### T7. Access Control and Entitlement Segmentation

**Theme statement**

Access to license rights must be governable by user, role, and scope, so that organizations
can apply least-privilege defaults, separate teams and cost centers, and grant
time-boxed access to external participants.

**Originating concerns**

Security and Compliance Lead, Operations and DevOps Engineer, ISV Product and Commercial
Owner, SI Commercial and Reselling Lead; the Access Control and Entitlement Segmentation
cross-persona concern in Section 5.2; the Test and Validation and Event-Driven classes; the
Miro usage-type-differentiation problem statement.

**What good looks like**

- Entitlements can be assigned by user and role to avoid over-provisioning.
- Project- or production-scoped pools separate teams and cost centers.
- Temporary access windows (for example rental or guest teams) are supported, with
  least-privilege defaults and audited emergency overrides.

**Forward traceability**

Security requirements; operational requirements; license modality requirements.

### T8. Security, Trust, and Auditability

**Theme statement**

Licensing must be cryptographically secured, auditable, and operable without granting vendors
access to customer infrastructure, balancing intellectual-property protection against
production continuity.

**Originating concerns**

Security and Compliance Lead, ISV Licensing Architect, Platform SRE; all use case classes;
the "security vulnerabilities", "trust vs availability balance", and "remote server
dependencies" challenges.

**What good looks like**

- Artifacts are signed and validated locally; credentials are short-lived; keys are managed
  and rotated.
- All lifecycle operations are auditable, with append-only records of who did what and when.
- Vendors do not require privileged access to customer resources; identity evidence is
  presented by the workload instead.

**Forward traceability**

Security requirements; identity and binding requirements.

### T9. Continuity Under Failure and Grace Behavior

**Theme statement**

Licensing must tolerate transient connectivity loss and component failure through local
validation, renewal retries, defined grace policies, and controlled degradation, so that
licensing is never a single point of failure for live production.

**Originating concerns**

Director of Engineering, Broadcast Director / Engineer, Platform SRE, Operations and DevOps
Engineer; the Continuous Operations class and the Resilience and Continuity overlay; the
"grace policy gaps", "offline licensing requirements", and "trust vs availability balance"
challenges; the Miro air-gapped / remote-server problem statement.

**What good looks like**

- Applications continue using a locally validated artifact when the licensing service is
  briefly unreachable.
- Grace windows and exhaustion actions (drain, degrade, stop) are defined, governed, and
  alerted on before they affect production.
- Air-gapped and offline operation is supported with appropriately reduced functionality.

**Forward traceability**

Lease and policy requirements; operational requirements; security requirements.

### T10. Interoperability and Anti-Fragmentation

**Theme statement**

The model must standardize core concepts and interfaces while allowing implementation
flexibility, so that adopters avoid siloed, vendor-specific licensing and platform lock-in.

**Originating concerns**

Industry Standards Representative, SI Solution Architect, ISV Product and Commercial Owner;
all use case classes; the "vendor lock-in risks", "missing standard APIs", and "industry
knowledge gap" challenges; the standardization-vs-differentiation tension in Section 5.2.

**What good looks like**

- Core concepts, token structure, and lifecycle operations are standardized; vendor
  implementations remain free to differentiate.
- Solutions function across cloud, hybrid, on-premises, and air-gapped environments.
- Terminology and semantics remain stable across vendors and drafting cycles.

**Forward traceability**

General requirements; API requirements; integration requirements.

## Challenge-to-Theme Coverage

The initiative's early analysis grouped recurring industry challenges by impact and overhead.
The table below maps those challenges onto the themes above to confirm that the theme set
provides coverage. It is informative.

| Challenge | Primary theme(s) |
| :--- | :--- |
| IaC integration gap | T1 |
| Manual setup processes | T1, T2 |
| Usage type differentiation (prod/test/training/DR) | T5, T7 |
| Remote server dependencies | T8, T9 |
| Hardware binding issues | T3 |
| CLI/API access gap | T2 |
| Cost transparency | T5, T6 |
| Model transition challenges | T4 |
| License interdependencies | T4, T10 |
| Business model misalignment | T4 |
| Industry knowledge gap | T10 |
| Vendor-specific processes | T2, T10 |
| Missing standard APIs | T2, T10 |
| Headless activation gap | T1 |
| Manual ISV intervention | T3, T9 |
| Portfolio complexity | T4 |
| Security vulnerabilities | T8 |
| License mobility | T3 |
| Customer maturity variations | T2, T6 |
| Offline licensing requirements | T9 |
| Trust vs availability balance | T8, T9 |
| Vendor lock-in risks | T10 |
| End user portal absence | T6 |
| Grace policy gaps | T9 |

## Theme Tensions

Several themes pull against one another. These tensions are expected and are recorded here so
that later requirement and design work treats them as explicit trade-offs rather than as
defects:

- **Protection vs continuity** — T8 (security and trust) vs T9 (continuity under failure):
  stricter enforcement reduces availability headroom; longer grace increases exposure.
- **Flexibility vs simplicity** — T4 (modality flexibility) vs T5/T6 (transparency and
  self-service): finer-grained commercial models can reduce explainability.
- **Standardization vs differentiation** — T2/T10 (standardized interfaces and
  interoperability) vs vendor desire to differentiate implementation and packaging.
- **Control vs low friction** — T7 (access control and segmentation) vs T1 (automation):
  tighter access governance can add steps to automated flows.

These map directly to the cross-persona tensions named in Section 5.2.

## Forward Traceability to Normative Requirements

The themes are intended to flow into the normative requirements chapter. The table below
records the primary mapping; a theme may also contribute secondarily to other groups.

| Theme | Primary normative requirement group |
| :--- | :--- |
| T1 Automation and Licensing-as-Code | Integration; General |
| T2 Standardized Lifecycle and Interfaces | API; General |
| T3 Identity-Based Binding and Mobility | Identity and Binding |
| T4 License Modality and Commercial Flexibility | License Modality |
| T5 Usage-Based Metering and Cost Transparency | Metering |
| T6 Observability and Self-Service | Operational |
| T7 Access Control and Entitlement Segmentation | Security; Operational |
| T8 Security, Trust, and Auditability | Security |
| T9 Continuity Under Failure and Grace Behavior | Lease and Policy |
| T10 Interoperability and Anti-Fragmentation | General; Integration |

## Drafting Notes

This section is descriptive and analytical. It consolidates needs into themes and traces them
forward; it does not state normative requirements, does not use normative keywords as
requirement language, and does not define API-level or schema-level behavior. The normative
requirements chapter is the place where these themes become disciplined, testable
requirements.

## Drafting To-Do

The following items should be considered in later drafting iterations:
- confirm the forward-traceability mapping against the final subchapter structure of the
  normative requirements chapter,
- verify that every persona success criterion in Section 5.2 is represented by at least one
  theme,
- consider whether the theme tensions warrant a dedicated trade-off discussion in the design
  principles chapter.
