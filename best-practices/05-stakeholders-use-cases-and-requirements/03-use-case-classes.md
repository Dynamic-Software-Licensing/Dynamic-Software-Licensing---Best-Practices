# 05.03 Use Case Classes

## Purpose

This section defines the recurring operational use case classes addressed by these best
practices. A use case class is a category of operating situation that places a
characteristic set of demands on licensing behavior. The classes generalize specific
customer scenarios into reusable patterns so that later requirement themes (Section 5.4)
and workflow definitions (Section 5.5) can be derived once and reused across many concrete
deployments.

This section is written against a dynamic software licensing target model. Each class is
therefore described in terms of how licensing is expected to behave in that situation, not
in terms of any specific product or platform.

## Method and Input Basis

The use case classes below synthesize:
- the stakeholder groups defined in Section 5.1,
- the role-level perspectives defined in Section 5.2,
- team prework (including Miro workshop material),
- the recurring industry use cases captured during the initiative's early analysis.

The classes are intentionally a small, stable set. They are not an exhaustive catalogue of
scenarios; they are the recurring demand patterns that most strongly differentiate licensing
behavior. Concrete customer situations are expected to map onto one primary class, often with
secondary influence from others.

## Use Case Class Schema

Each use case class is specified using the same structure to keep comparison and downstream
mapping consistent:

- **Operating context** — the production situation that characterizes the class.
- **Demand profile** — how load, duration, and predictability behave over time.
- **Licensing pressure** — the specific demands the situation places on licensing behavior.
- **Dominant modalities** — the commercial and consumption modalities most relevant to the
  class (for example time-based, process-based, or outcome-based).
- **Representative scenarios** — illustrative examples that ground the class without becoming
  the definition.
- **Primary lifecycle emphasis** — the licensing lifecycle operations most exercised by the
  class (issue, renew, reissue, revoke, inspect, usage reporting).
- **Key personas** — the Section 5.2 perspectives most affected.

This schema is descriptive. It does not introduce requirement statements; it organizes the
inputs that later sections turn into requirement themes and workflows.

## Overview of the Use Case Classes

Five primary use case classes are defined:

1. Continuous (24/7) Operations
2. Frequent Event-Driven Production
3. Infrequent Event-Driven Production
4. Test and Validation
5. AI-Powered and Outcome-Based Services

A sixth pattern, Resilience and Continuity, is treated as a cross-cutting overlay rather than
a standalone class, because it applies across all five primary classes.

The primary classes are differentiated mainly by **duration and predictability of demand**
and by the **commercial granularity** they require. Continuous operations sit at the
predictable, low-granularity end; infrequent events and outcome-based services sit at the
elastic, high-granularity end.

## 1. Continuous (24/7) Operations

**Operating context**

Always-on production environments that run continuously and cannot tolerate licensing-induced
interruption. The canonical example is playout, but the class covers any sustained,
long-running service.

**Demand profile**

Stable and predictable over long periods. Capacity changes are infrequent and usually
planned. The dominant operational concern is uninterrupted continuity rather than rapid
elasticity.

**Licensing pressure**

- Licensing must never become a single point of failure for live operation.
- Renewal and validation must continue without manual intervention.
- High-availability architectures (including hot/hot and hot/standby) must be supported,
  including the ability to apply an entitlement across primary and backup environments
  serving a single production.
- Expiry must be signalled well in advance so renewals never surprise operations during a
  broadcast window.

**Dominant modalities**

Predictable, low-granularity modalities are acceptable and often preferred: perpetual or
annual commitments. More granular modalities may still be required for bounded experiments
(for example launching a new channel for a limited period) layered on top of the baseline.

**Representative scenarios**

- 24/7 playout of a linear channel.
- A standing production gallery operated continuously.
- Launch of a new international channel for a defined limited period on top of an existing
  continuous estate.

**Primary lifecycle emphasis**

Renew (continuous), inspect (continuity and expiry visibility), reissue (for failover within
high-availability designs).

**Key personas**

Director of Engineering, Operations and DevOps Engineer, Broadcast Engineer / Production
Operator, Finance and Procurement Lead.

## 2. Frequent Event-Driven Production

**Operating context**

Recurring, scheduled events that repeat often enough to be a routine part of operations but
that still scale up and down around each occurrence. Examples include daily news and regular
sports-league coverage.

**Demand profile**

Cyclical and largely foreseeable. Demand rises and falls around known event windows.
Capacity is added for an event and released afterwards, repeatedly.

**Licensing pressure**

- Modalities must offer more granularity than continuous operations, for example monthly
  options that align with recurring event cadence.
- Activation and release must be repeatable and low-friction, because the cycle recurs often.
- Per-product and per-feature differentiation must be supported, because vendors may license
  individual products and features separately.
- Forecasting must account for repeated, partly predictable peaks.

**Dominant modalities**

Time-based with moderate granularity (annual baseline plus monthly or event-scoped
additions), often combined per product and per feature.

**Representative scenarios**

- Daily news production with predictable studio and graphics demand.
- A recurring sports league with weekly match coverage.
- Seasonal programming that scales a known set of products for a defined run.

**Primary lifecycle emphasis**

Issue and revoke (repeated activation and release), renew, usage reporting, inspect.

**Key personas**

Broadcast Engineer / Production Operator, Operations and DevOps Engineer, Finance and
Procurement Lead, SI Delivery and Operations Lead.

## 3. Infrequent Event-Driven Production

**Operating context**

Large, one-off or rarely-occurring events where capacity is stood up specifically for the
event and torn down afterwards. The canonical example is a major periodic sporting event.

**Demand profile**

Sharp, bounded, and high-magnitude. A significant capacity uplift is needed for a short,
well-defined window, with little or no steady-state footprint between events.

**Licensing pressure**

- Highly granular, consumption-based modalities are required (for example monthly, weekly,
  daily, or hourly) so that cost aligns to a short, intense window.
- Burst capacity must be obtainable quickly and released cleanly when the event ends.
- Managed-service and integrator-led delivery models must be supported, because customers
  often outsource these events (for example outside-broadcast operations or SI-run setups) to
  avoid licensing complexity themselves.
- Forecasting and provisional caps matter, because a single event can dominate the licensing
  bill.

**Dominant modalities**

Fine-grained, consumption-based time modalities (hourly/daily/weekly/monthly), frequently
delivered through a managed-service or reseller commercial arrangement.

**Representative scenarios**

- A major multi-week international sporting event.
- A one-off broadcast of national significance requiring temporary scale-out.
- An outside-broadcast or pop-up production operated on the customer's behalf by an
  integrator.

**Primary lifecycle emphasis**

Issue and revoke around a bounded window, burst-oriented scaling, usage reporting, inspect
for burn-rate visibility.

**Key personas**

Finance and Procurement Lead, Broadcast Director / Engineer, SI Managed Services Portfolio
Lead, SI Commercial and Reselling Lead, ISV Product and Commercial Owner.

## 4. Test and Validation

**Operating context**

Non-production and pre-production activity: validating an end-to-end workflow, building and
stress-testing a new pipeline, or running periodic jobs. Activity is often ad-hoc and
short-lived.

**Demand profile**

Intermittent and bursty, with short durations and unpredictable timing. Environments are
created, exercised, and discarded.

**Licensing pressure**

- Highly granular modalities are required (for example hourly or weekly) so that short
  validation runs do not require production-scale commitments.
- Usage rights must be categorizable by purpose (for example production, test, training,
  disaster recovery) so that test consumption is distinguishable and appropriately governed.
- Self-service access to demo or sandbox entitlements is needed for development and staging
  environments without manual vendor involvement.
- Activation and release must integrate cleanly into automated build and test pipelines.

**Dominant modalities**

Short-duration, granular time modalities and scoped demo or sandbox entitlements, separated
from production entitlement pools.

**Representative scenarios**

- Validating an end-to-end broadcast workflow before go-live.
- Running a periodic transcode or quality-control job.
- Building and stress-testing a new pipeline in a staging account.

**Primary lifecycle emphasis**

Issue and revoke (frequent, short-lived), inspect (which entitlements are allocated and which
features are restricted), usage reporting for cost attribution.

**Key personas**

Operations and DevOps Engineer, SI Solution Architect / Integrator, Director of Engineering,
ISV Support and Customer Success Lead.

## 5. AI-Powered and Outcome-Based Services

**Operating context**

Value-added services where the licensed value is most naturally expressed as a delivered
result rather than as elapsed time or provisioned capacity. Examples include automated
content analysis and highlight generation.

**Demand profile**

Variable and result-driven. Consumption tracks the volume of work performed or outcomes
produced, which may not correlate cleanly with wall-clock time or instance count.

**Licensing pressure**

- Outcome-based and process-based metering must be supported (for example per generated clip,
  per minute of subtitles, per compliance report, or per normalized process unit).
- Usage dimensions must be expressive enough to capture units of delivered value, not only
  time.
- Cost transparency must link delivered outcomes to commercial impact so that value-based
  charging remains explainable and defensible.
- Metering integrity matters, because charging is tied directly to recorded units.

**Dominant modalities**

Outcome-based and process-based modalities (process units, per-result metrics), often layered
onto a time-based or entitlement baseline.

**Representative scenarios**

- Automated content analysis charged per analyzed asset.
- Highlight or clip generation charged per produced clip.
- Subtitle or compliance services charged per minute or per report.

**Primary lifecycle emphasis**

Usage reporting (central to this class), issue and renew for the underlying service
entitlement, inspect for burn-rate and value attribution.

**Key personas**

ISV Product and Commercial Owner, Finance and Procurement Lead, ISV Sales Director, Security
and Compliance Lead (metering integrity).

## Cross-Cutting Overlay: Resilience and Continuity

Resilience and continuity needs — failover, blue/green cutover, hybrid operation, and
disaster recovery — appear across all five primary classes rather than forming a standalone
class. They are therefore treated as an overlay that intensifies the licensing pressure of
whichever primary class is in effect.

Characteristic demands of the overlay include:
- license mobility between instances and environments without manual vendor intervention,
- the ability to move or reissue an active entitlement to a replacement workload during
  failover,
- use of cloud capacity as a backup to on-premises resources in hybrid designs,
- portable identity evidence so that the same entitlement can follow active and standby
  workloads,
- defined behavior when connectivity to licensing services is briefly lost.

The overlay binds most strongly to Continuous Operations (where interruption is least
tolerable) and to Event-Driven Production (where failover during a live event is
business-critical). It corresponds to the hybrid and disaster-recovery operational profile in
the operational and deployment profiles chapter.

## Use Case Classes Versus Usage Types

The use case classes above describe a **demand pattern** — how load, duration, and
predictability behave. They should not be confused with the **usage type** of an environment,
which describes its *purpose*: for example production, test, training, disaster recovery, or
event. These are two orthogonal axes:

- The use case class answers "what is the demand shape?" (continuous, event-driven, ad-hoc,
  outcome-driven).
- The usage type answers "for what purpose is this capacity being consumed?" (production
  versus test versus training versus DR versus event).

Any class can run under more than one usage type. A continuous environment usually runs as a
production usage type but may have a parallel test instance; an event-driven environment may
be exercised as a test usage type before going live. The names overlap in ordinary language —
"Test and Validation" is a class while "test" is also a usage type, and "event" appears on
both axes — so the distinction is stated explicitly here to avoid conflation.

Usage type is significant because the team prework (the Miro workshop) threads it through
several candidate workflows: usage type is determined during automated activation and guided
setup, and a dedicated workflow creates purpose-specific license types. It is therefore
carried forward as a requirement theme (access control and entitlement segmentation, T7 in
Section 5.4) and as a workflow (usage-type differentiation in Section 5.5), rather than as an
additional use case class here.

## Use Case Class Comparison

The following table summarizes the differentiating characteristics. It is informative and
intended to aid orientation, not to constrain mapping.

| Use Case Class | Demand predictability | Duration | Required granularity | Dominant modality emphasis | Lifecycle emphasis |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Continuous (24/7) Operations | High | Long-running | Low (baseline) | Perpetual / annual | Renew, inspect, reissue |
| Frequent Event-Driven | Cyclical, foreseeable | Recurring windows | Moderate | Annual + monthly / event-scoped | Issue, revoke, renew, usage |
| Infrequent Event-Driven | Sharp, bounded | Short, intense | High | Hourly / daily / weekly / monthly | Issue, revoke, burst, usage |
| Test and Validation | Low, ad-hoc | Short-lived | High | Granular time + demo / sandbox | Issue, revoke, inspect |
| AI / Outcome-Based | Result-driven | Variable | High (per result) | Outcome / process-based | Usage, issue, renew |

## Relationship to Operational and Deployment Profiles

The use case classes in this section are demand patterns expressed from the stakeholder and
scenario viewpoint. The operational and deployment profiles chapter expresses closely related
patterns from the runtime and deployment viewpoint. The two are intended to align:

- Continuous (24/7) Operations aligns with the continuous broadcast profile.
- Frequent and Infrequent Event-Driven Production align with the event production profile.
- Test and Validation aligns with the test and validation profile.
- AI-Powered and Outcome-Based Services aligns with the AI outcome services profile.
- The Resilience and Continuity overlay aligns with the hybrid and disaster-recovery profile.

This alignment is intentional. Use case classes explain *why* a demand pattern exists from a
stakeholder perspective; operational profiles explain *how* it is run. Conformance and
profile differentiation in later chapters can therefore reference either viewpoint
consistently.

## Traceability to Subsequent Sections

This section informs:
- Section 5.4 by exposing the recurring pressures that aggregate into requirement themes,
- Section 5.5 by identifying the lifecycle operations and decision points each class
  exercises, which structure the canonical workflows.

The intended traceability chain is: stakeholder groups (5.1) → role perspectives (5.2) → use
case classes (5.3) → requirement themes (5.4) and workflow definitions (5.5).

## Section Positioning

This section is descriptive and analytical. It classifies operating situations and the
licensing pressures they create; it does not prescribe normative requirement language and
does not specify API-level or schema-level behavior. Those concerns are addressed in the
canonical API model and in the normative requirements chapter.

## Review Focus

Review comments on this section should focus on whether the class set is complete, whether it
aligns with the operational profiles chapter, and whether the mapping from class to downstream
requirements remains clear and defensible.
