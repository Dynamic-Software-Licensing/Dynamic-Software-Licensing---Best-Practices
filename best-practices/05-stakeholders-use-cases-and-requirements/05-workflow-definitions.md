# 05.05. Workflow Definitions

## Purpose

This section defines the canonical workflow patterns used to derive system requirements from
the stakeholder, use case, and challenge analysis in Sections 5.1 to 5.4. A workflow
definition captures *what* happens — the actors, inputs, ordered steps, decisions, and
outputs — independently of *how* any particular platform implements it.

These workflows provide the traceability bridge from challenges and use cases to derived
requirement themes, and ultimately to the normative requirements chapter.

## Method and Input Basis

The workflows below are derived from:
- team prework, in particular the Miro workshop board *IAMT DSL Workflows*, which is the
  primary source baseline for this section,
- the use case classes in Section 5.3 and the requirement themes in Section 5.4,
- the original proposal draft, which contributed the lifecycle-continuity workflows.

The Miro board worked the high-impact, low-overhead problem statements into candidate
workflows using a shared method. That method is adopted here unchanged.

## Workflow Method

A workflow in this section is expressed with a small, consistent vocabulary, following the
method established in the prework:

- **Who** — the actor(s) and their responsibilities.
- **Input** — what enters the workflow.
- **Process step(s)** — the ordered actions, including decision points and branches.
- **Output** — the resulting state or artifact.

### Abstraction principle: what, not how

The defining characteristic of the method is deliberate abstraction. A workflow states what
must happen and in what order; it does not prescribe the implementation. The prework
illustrated this with a simple example — a "clean car" workflow that is *not concerned with*
which route to drive, how payment is made, or how the wash is performed.

Applied to licensing, this means workflow definitions:
- name the licensing lifecycle operations they invoke (issue, renew, reissue, revoke, inspect,
  usage reporting) without specifying their request or response detail,
- describe identity, entitlement, and policy handling in capability terms, not in terms of any
  specific identity provider, key store, or transport,
- remain valid across cloud, hybrid, on-premises, and air-gapped deployments.

API-level and schema-level detail is therefore deliberately out of scope here; it belongs to
the canonical API model chapter and the annexes. The prework's own technical-solution notes
(for example specific machine-to-machine authentication flows) are likewise treated as
implementation detail.

### Decision points and failure paths

Workflows may branch. The prework's transcode example shows a decision step — pass the signal
through if it is already in the required format, otherwise transcode it. Licensing workflows
contain analogous decisions (for example: is the entitlement available? is connectivity
present? has grace been exhausted?). Each workflow below records its principal decision points
and the failure paths that follow when a decision resolves unfavorably.

## Workflow Schema

Each workflow is specified using the following structure, consistent with the chapter scope:

- **Trigger and objective** — what initiates the workflow and what it aims to achieve.
- **Actors** — the roles and components responsible (the "Who").
- **Preconditions and inputs** — required state and inputs before the workflow runs.
- **Steps and decisions** — the ordered process steps, including branches.
- **Outputs and state changes** — resulting artifacts and state transitions.
- **Failure paths and recovery** — what happens when a step or decision fails.
- **Traceability** — the use case classes and requirement themes the workflow serves.

## Workflow Catalogue

The workflows are grouped into two sets:

- **Group A — Adoption and operations workflows.** Derived directly from the Miro problem
  statements. These address the friction of adopting and operating licensing in
  software-defined environments.
- **Group B — Lifecycle continuity workflows.** Derived from the original proposal draft.
  These address the runtime continuity of an active license over its lifetime.

| ID | Workflow | Origin | Primary themes |
| :--- | :--- | :--- | :--- |
| WF-01 | Automated license activation in deployment | Miro: IaC integration gap | T1, T2 |
| WF-02 | License cost estimation (TCO) | Miro: cost predictability | T5, T4 |
| WF-03 | Usage reporting and licensing-unit derivation | Miro: cost usage | T5, T6 |
| WF-04 | Usage-type differentiation | Miro: usage type differentiation | T7, T4 |
| WF-05 | Guided license setup | Miro: manual setup processes | T1, T2 |
| WF-06 | License inventory query and observability | Miro: CLI/API access gap | T6, T2 |
| WF-07 | Identity-based provisional licensing | Miro: hardware binding issues | T3 |
| WF-08 | Offline / air-gapped license acquisition | Miro: remote server dependencies | T9, T8 |
| WF-09 | Lease renewal and continuity | Original draft | T2, T9 |
| WF-10 | Failover reissue and license mobility | Original draft | T3, T9 |
| WF-11 | Revocation and enforcement | Original draft | T8, T2 |
| WF-12 | Grace and offline continuity | Original draft | T9 |
| WF-13 | Burst capacity for events | Original draft | T1, T4 |

## Group A — Adoption and Operations Workflows

### WF-01. Automated License Activation in Deployment

**Trigger and objective**

A deployment pipeline provisions a system and must obtain a working license without any manual
step. Objective: a licensed, running system at the end of an automated deployment.

**Actors**

Operations / DevOps engineer (owner of the pipeline); SI developer (authoring the IaC module);
license agent and control plane (components).

**Preconditions and inputs**

- An entitlement exists for the product and intended environment.
- The deployment carries enough context to determine the usage type.
- Input: a DevOps deployment workflow.

**Steps and decisions**

1. Deploy the system through infrastructure-as-code.
2. Determine the usage type (for example development, test, production, or event).
3. Decision: is a valid entitlement available for that usage type? If not, follow the failure
   path.
4. Activate the license as part of the automated deployment (issue operation).

**Outputs and state changes**

A licensed system; an active lease bound to the workload; an audit record of activation.

**Failure paths and recovery**

- No matching entitlement: the pipeline surfaces a clear, actionable error rather than
  silently proceeding unlicensed; deployment is held or rolled back per pipeline policy.
- Control plane unreachable at activation: retry with backoff; if a pre-issued or cached
  artifact is permitted by policy, proceed under grace (see WF-12), otherwise fail the
  deployment cleanly.

**Traceability**

Use cases: all classes, especially Test and Validation and Event-Driven. Themes: T1, T2;
secondary T7 (usage type).

### WF-02. License Cost Estimation (TCO)

**Trigger and objective**

A team needs to estimate licensing cost for a planned configuration before committing to it.
Objective: a defensible total-cost estimate linked to expected usage.

**Actors**

Finance and procurement lead; director of engineering; ISV product and commercial owner
(catalog/price input).

**Preconditions and inputs**

- A catalog that links dimensions and modalities to price.
- Input: a production or integration template describing the media functions to be deployed.

**Steps and decisions**

1. Map each media function to the media service usage it implies.
2. Map media service usage to the licensing needs it generates.
3. Aggregate usage according to the licenses needed.
4. Convert aggregated usage to costs using the catalog.

**Outputs and state changes**

A total-cost-of-ownership estimate. No runtime licensing state changes (this is a planning
workflow).

**Failure paths and recovery**

- Missing price or dimension mapping for a function: flag the gap explicitly; the estimate
  marks the unpriced element rather than omitting it silently.
- Uncertain usage volumes: produce a ranged estimate with stated assumptions.

**Traceability**

Use cases: Event-Driven (frequent and infrequent), AI/Outcome-Based. Themes: T5, T4;
secondary T6.

### WF-03. Usage Reporting and Licensing-Unit Derivation

**Trigger and objective**

Operations and finance need to understand actual consumption and express it in licensing
terms distinct from infrastructure cost. Objective: derive licensing unit(s) from observed
system usage.

**Actors**

Operations / DevOps engineer; finance and procurement lead; license manager.

**Preconditions and inputs**

- Systems emit usage signals.
- Input: observed system usage across the estate.

**Steps and decisions**

1. Collect usage reporting for each system.
2. Query that usage specifically on its licensing dimensions (separating licensing-relevant
   usage from general infrastructure usage).
3. Derive the licensing unit(s) consumed (for example duration- or value-based units).

**Outputs and state changes**

Licensing unit records suitable for reconciliation, forecasting, and billing inputs. Usage is
stored for later querying.

**Failure paths and recovery**

- Gaps in usage signals: mark periods of missing data rather than interpolating silently.
- Buffered usage after an outage: reconcile idempotently so records are not double-counted.

**Traceability**

Use cases: AI/Outcome-Based, Event-Driven, Continuous. Themes: T5, T6; secondary T4.

### WF-04. Usage-Type Differentiation

**Trigger and objective**

A team needs license rights categorized by purpose so that non-production use is distinguished
and governed. Objective: associate a purpose-specific license with a need.

**Actors**

Operations / DevOps engineer; security and compliance lead; ISV product and commercial owner.

**Preconditions and inputs**

- The model supports usage-type categorization (for example production, test, training,
  disaster recovery).
- Input: a development, test, training, or other categorized need.

**Steps and decisions**

1. Create or select a special license type matching the need's category.
2. Associate the license with the requesting context.

**Outputs and state changes**

Categorized development/test (or other purpose) capacity, distinguishable from production
entitlement pools.

**Failure paths and recovery**

- Requested category not offered: surface the unavailable category; do not silently fall back
  to a production entitlement.
- Category misuse (for example test capacity used in production): detectable through the usage
  type recorded on the lease and reported via WF-03.

**Traceability**

Use cases: Test and Validation; Resilience and Continuity overlay (DR category). Themes: T7,
T4; secondary T5.

### WF-05. Guided License Setup

**Trigger and objective**

A system is set up outside a full IaC pipeline (a more manual path for lower-maturity adopters)
but still needs a correctly associated license. Objective: a licensed application via a
guided, repeatable setup.

**Actors**

Operations team; ISV support and customer success lead.

**Preconditions and inputs**

- A documented setup path exists.
- Input: a manual setup workflow.

**Steps and decisions**

1. Install the system.
2. Determine the usage type (development, test, production, or event).
3. Associate the appropriate license (issue operation).

**Outputs and state changes**

A licensed application; an active lease; an audit record.

**Failure paths and recovery**

- Wrong usage type selected: correctable by re-association; the change is audited.
- This workflow is intentionally the lower-automation counterpart to WF-01; adopters are
  expected to graduate from WF-05 to WF-01 as maturity increases.

**Traceability**

Use cases: all classes (lower-maturity adopters). Themes: T1, T2; secondary T7.

### WF-06. License Inventory Query and Observability

**Trigger and objective**

An integrator or operator needs transparent visibility of licenses across systems and vendors.
Objective: observability into which licenses exist, which are in use, and where.

**Actors**

SI solution architect / integrator; operations team; license manager.

**Preconditions and inputs**

- Licenses are inspectable through a programmatic or command-line interface.
- Input: an integrator query workflow.

**Steps and decisions**

1. Query the license system(s) for licenses within a specific context (applying filters such
   as tenant, product, environment, or status) — inspect operation.
2. Decision: are results complete across all relevant systems? If a source is unreachable,
   follow the failure path.

**Outputs and state changes**

A consolidated view of licenses available and in use, including their location. No state
change (read-only).

**Failure paths and recovery**

- A source system is unreachable: report partial results explicitly, marking which sources
  were not reached, rather than presenting an incomplete view as complete.

**Traceability**

Use cases: all classes; strongest for Continuous and Test and Validation. Themes: T6, T2.

### WF-07. Identity-Based Provisional Licensing

**Trigger and objective**

A workload must be licensed by its verifiable identity rather than by a host attribute, so the
license is not node-locked. Objective: a provisionally licensed application bound to workload
identity.

**Actors**

Platform SRE; operations / DevOps engineer; ISV licensing architect.

**Preconditions and inputs**

- The workload can present identity evidence.
- Input: a provisional system to be licensed.

**Steps and decisions**

1. Install the system.
2. Decision: is the presented identity evidence valid? If not, follow the failure path.
3. License the provisional application by binding to the workload identity (issue operation),
   not to a hostname or MAC address.

**Outputs and state changes**

A provisionally licensed application bound to workload identity; an active lease.

**Failure paths and recovery**

- Invalid or absent identity evidence: deny issuance with a clear reason; do not fall back to
  host-based binding.
- Identity rotation or replacement: handled by reissue (WF-10) rather than re-installation.

**Traceability**

Use cases: Continuous, Resilience and Continuity overlay. Themes: T3; secondary T8.

### WF-08. Offline / Air-Gapped License Acquisition

**Trigger and objective**

A system has no connection to a remote licensing service and must still be licensed.
Objective: a licensed application in an air-gapped environment.

**Actors**

Security and compliance lead; operations team.

**Preconditions and inputs**

- An offline licensing path is supported, including transfer via portable media.
- Input: an air-gapped system.

**Steps and decisions**

1. Acquire a license for a defined period, potentially generated ahead of time and carried on
   transferable media.
2. Transfer the license to the air-gapped system.
3. Validate the license locally on the target system.

**Outputs and state changes**

A licensed application operating offline for the defined period, with reduced functionality
where applicable.

**Failure paths and recovery**

- License period expiry with no connectivity: defined offline behavior applies (see WF-12),
  with advance local warnings.
- Transfer integrity failure: validation rejects a tampered or corrupt artifact.

**Traceability**

Use cases: Resilience and Continuity overlay; Test and Validation (isolated environments).
Themes: T9, T8; secondary T3.

## Group B — Lifecycle Continuity Workflows

These workflows describe the runtime continuity of an active license. They are expressed at
the same abstraction level as Group A; the underlying lifecycle operations are defined in the
canonical API model chapter and are not detailed here.

### WF-09. Lease Renewal and Continuity

**Trigger and objective**

An active lease approaches expiry and must be extended without interrupting operation.
Objective: uninterrupted continuity through timely renewal.

**Actors**

License agent (component); operations / DevOps engineer (policy owner).

**Preconditions and inputs**

An active lease with a renewal window and policy; input: the approaching expiry of the lease.

**Steps and decisions**

1. Begin renewal ahead of expiry, within the renewal window (renew operation).
2. Decision: did renewal succeed before expiry? If not, enter grace handling (WF-12).
3. On success, continue operation under the extended lease.

**Outputs and state changes**

An extended lease and a refreshed local artifact; continuity preserved.

**Failure paths and recovery**

- Renewal fails: retry with backoff; on continued failure, WF-12 governs behavior; advance
  expiry warnings are raised so operations are not surprised during a production window.

**Traceability**

Use cases: Continuous, Event-Driven. Themes: T2, T9; secondary T6.

### WF-10. Failover Reissue and License Mobility

**Trigger and objective**

An active workload fails or is replaced (including planned blue/green cutover), and its
entitlement must follow to a new workload without manual vendor intervention. Objective:
mobility of an active entitlement across workloads.

**Actors**

Broadcast director / engineer; platform SRE; license agent and control plane.

**Preconditions and inputs**

An active lease; a replacement workload able to present its own identity evidence; input: a
failover or cutover event.

**Steps and decisions**

1. Initiate transfer of the lease to the new workload identity (reissue operation).
2. Decision: planned cutover or unplanned failover? A planned cutover may use a pre-issued
   cutover artifact if connectivity is briefly unavailable.
3. Finalize the transfer: activate the new binding and revoke the old.

**Outputs and state changes**

The entitlement now bound to the new workload; the prior binding revoked; an audit record of
the transfer.

**Failure paths and recovery**

- Control plane briefly unreachable during planned cutover: proceed on a pre-issued artifact,
  then finalize and revoke once reconnected.
- New identity evidence invalid: transfer is denied; the original binding remains until a
  valid target is presented.

**Traceability**

Use cases: Continuous, Event-Driven, Resilience and Continuity overlay. Themes: T3, T9.

### WF-11. Revocation and Enforcement

**Trigger and objective**

An administrator or a policy condition requires an active license to be terminated. Objective:
prompt, auditable revocation with controlled application response.

**Actors**

Security and compliance lead / administrator; control plane; license agent.

**Preconditions and inputs**

An active lease; a revocation trigger (administrative action or policy violation); input: the
revocation request.

**Steps and decisions**

1. Mark the lease revoked in the control plane (revoke operation).
2. Decision: is the affected workload currently reachable? If reachable, push the revocation;
   if not, it takes effect at the next renewal.
3. The application responds per policy (for example drain to a safe state).

**Outputs and state changes**

A revoked lease; the application brought to its policy-defined post-revocation state; an audit
record.

**Failure paths and recovery**

- Workload offline at revocation: revocation is enforced at the next renewal; exposure is
  bounded by short artifact lifetimes.

**Traceability**

Use cases: all classes. Themes: T8, T2; secondary T9.

### WF-12. Grace and Offline Continuity

**Trigger and objective**

Connectivity to the licensing service is lost while a workload is running. Objective: defined,
governed behavior that protects production continuity while bounding exposure.

**Actors**

License agent (enforces policy); operations / DevOps engineer and ISV (define policy).

**Preconditions and inputs**

An active, locally validated artifact and an applicable grace policy; input: loss of
connectivity.

**Steps and decisions**

1. Continue operating on the locally validated artifact (no round-trip required).
2. Retry renewal in the background with backoff.
3. Decision: did connectivity return within the grace window? If yes, resume normal renewal
   (WF-09).
4. If the grace window is exhausted, apply the policy-defined action: drain, degrade, or stop.

**Outputs and state changes**

Either restored normal operation or a controlled, policy-defined degradation; alerts raised as
the grace window counts down; buffered usage reconciled on reconnection.

**Failure paths and recovery**

- Grace exhausted: the configured action (drain/degrade/stop) takes effect, having alerted
  operations beforehand.

**Traceability**

Use cases: Continuous, Resilience and Continuity overlay. Themes: T9; secondary T8.

### WF-13. Burst Capacity for Events

**Trigger and objective**

A planned event requires additional capacity for a bounded window. Objective: scale licensed
capacity up for the event and release it cleanly afterwards.

**Actors**

Director of engineering; broadcast director / engineer; finance and procurement lead.

**Preconditions and inputs**

Event capacity plans and applicable guardrail policies; input: an event capacity request.

**Steps and decisions**

1. Request additional entitlements or dimensions for the event window (issue operation under
   guardrail policy).
2. Decision: is the request within guardrails and forecasted budget? If not, it is held for
   approval.
3. Operate at scaled capacity during the event.
4. Release the additional capacity when the event ends (revoke operation), returning licenses
   to the pool.

**Outputs and state changes**

Temporarily scaled capacity during the event; capacity released and reconciled afterwards;
usage recorded for forecasting.

**Failure paths and recovery**

- Guardrail or budget exceeded: the request is held rather than silently granted, preserving
  spend predictability.
- Failure to release after the event: detectable through inventory (WF-06) and reclaimed.

**Traceability**

Use cases: Event-Driven (frequent and infrequent). Themes: T1, T4; secondary T5, T6.

## Traceability Summary

The table consolidates workflow-to-use-case and workflow-to-theme mappings. It is the
chapter-internal bridge intended to support derivation of normative requirements.

| Workflow | Primary use case class(es) | Requirement themes |
| :--- | :--- | :--- |
| WF-01 Automated activation | All; Test, Event-Driven | T1, T2, T7 |
| WF-02 Cost estimation (TCO) | Event-Driven, AI/Outcome | T5, T4, T6 |
| WF-03 Usage reporting / units | AI/Outcome, Event-Driven, Continuous | T5, T6, T4 |
| WF-04 Usage-type differentiation | Test and Validation; DR overlay | T7, T4, T5 |
| WF-05 Guided setup | All (lower maturity) | T1, T2, T7 |
| WF-06 Inventory query | All; Continuous, Test | T6, T2 |
| WF-07 Identity-based provisional licensing | Continuous; Continuity overlay | T3, T8 |
| WF-08 Offline / air-gapped acquisition | Continuity overlay; Test | T9, T8, T3 |
| WF-09 Renewal and continuity | Continuous, Event-Driven | T2, T9, T6 |
| WF-10 Failover reissue / mobility | Continuous, Event-Driven, overlay | T3, T9 |
| WF-11 Revocation and enforcement | All | T8, T2, T9 |
| WF-12 Grace / offline continuity | Continuous, overlay | T9, T8 |
| WF-13 Burst capacity | Event-Driven | T1, T4, T5, T6 |

## Relationship to Other Chapters

- The canonical API model chapter defines the lifecycle operations these workflows invoke
  (issue, renew, reissue, revoke, usage reporting, inspect). This section names those
  operations but does not specify their payloads.
- The normative requirements chapter derives testable requirements from these workflows via
  the requirement themes in Section 5.4.
- The operational and deployment profiles chapter expresses the runtime environments in which
  these workflows execute.
- Implementation-specific realizations (for example particular authentication flows or
  reference architectures) belong in the informative annexes.

## Section Positioning

This section is descriptive and analytical. It defines workflow patterns at the "what, not
how" level established in the prework. It does not prescribe normative requirement language
and does not contain API-level or schema-level detail; both are out of scope for this section.
