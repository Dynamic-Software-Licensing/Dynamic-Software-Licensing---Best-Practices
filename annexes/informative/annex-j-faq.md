# Annex J. FAQ

## Purpose

This informative annex captures short answers to recurring review questions about the DSL best
practices.

## Frequently Asked Questions

### What is DSL at a high level?

Dynamic Software Licensing (DSL) is an open best-practices framework for managing software
entitlements, runtime authorization, policy enforcement, and usage observability in dynamic
broadcast and media environments.

### How does DSL differ from traditional license management?

Traditional license management often assumes static hosts, manual assignment, long-lived
instances, and limited workload mobility. DSL separates durable customer rights from runtime
authorization and is designed for automated, policy-driven, and portable operating models.

### Is DSL a formal standard?

No. The repository currently publishes best practices with standard-like structure and
traceability, but it is not presented as a certification or formal standards program.

### Is DSL primarily a reference model or an implementation prescription?

DSL is primarily a shared best-practices reference model. It defines common concepts, lifecycle
semantics, interfaces, and expectations that implementations can adopt, rather than mandating one
product architecture or one deployment blueprint.

### Does DSL use proprietary technology?

No. DSL does not depend on proprietary technology. It combines established architectural and
security patterns and aims to align with existing standards and broadly available implementation
approaches where that supports interoperability.

### Does DSL include security?

Yes. Security is treated as a first-class design concern throughout the model. DSL defines trust,
identity evidence, policy control, auditable actions, and bounded runtime authorization behavior.
Individual implementations still need to apply their own deployment, monitoring, hardening, and
operational security controls.

### What security responsibility remains with an implementation?

DSL defines the expected security model and trust boundaries, but implementations remain
responsible for secure deployment, credential protection, infrastructure hardening, monitoring,
tenant isolation, incident response, and compliance with their own operational environment.

### Does DSL require permanent connectivity to a licensing service?

No. The model is designed around signed, locally validatable runtime artifacts with bounded
renewal and grace behavior. Continuous connectivity is therefore not required, although the
control plane still needs a defined renewal and recovery path.

### Does DSL support failover and disaster recovery?

Yes. The model is explicitly designed to support continuity scenarios such as failover, reissue,
recovery, and bounded grace behavior without reducing licensing to a single fixed host binding.

### Does DSL replace every vendor-specific commercial model?

No. The best practices standardize lifecycle semantics and interoperability patterns, while
allowing vendors to retain differentiated commercial offerings.

### Must an existing licensing system be fully replaced to use DSL?

No. DSL can be introduced incrementally and can complement existing licensing approaches.
Organizations and vendors can adopt the concepts, interfaces, and lifecycle behaviors in stages
rather than replacing their entire licensing estate in a single step.

### Does DSL only fit cloud-native deployments?

No. The model is intended to remain platform-agnostic and to support cloud, on-premises,
hybrid, and resilience-focused environments.

### Is DSL only relevant for large broadcasters or large vendors?

No. The model is relevant wherever software licensing needs to behave predictably across changing
runtime contexts. That can apply to vendors, broadcasters, service providers, integrators, and
smaller teams that still need portability, auditability, and controlled entitlement handling.

### How vendor-neutral is DSL in practice?

DSL is intended to be vendor-neutral at the model and interoperability layer. It defines common
concepts and expected behaviors while leaving room for vendor-specific product differentiation,
commercial models, and implementation choices.

### Why is identity-based binding emphasized so strongly?

Because dynamic workloads, failover, and automation-first operations are difficult to support
reliably with static hardware binding.

### What is the difference between an entitlement, a lease, and a policy?

An entitlement expresses the durable customer right to use a capability. A lease is the
time-bounded runtime grant issued to a specific workload within that right. A policy defines the
runtime control behavior around that lease, including renewal timing, grace limits, and
enforcement actions.

### What is the runtime object in DSL?

The runtime object is the lease and its signed token representation, derived from an
entitlement and governed by an effective policy object.

### What does DSL intentionally not standardize?

DSL does not attempt to standardize every commercial model, every vendor-specific token payload,
every administrative back-office process, or every deployment topology. Its role is to define a
common interoperable baseline, not to remove all implementation choice.

### How does DSL relate to IAM, OIDC, and PKI?

DSL builds on these kinds of trust mechanisms rather than replacing them. Identity evidence,
token signing, verification, and key distribution can be implemented using established IAM,
OIDC, PKI, and related security building blocks.

### How can I try out DSL?

An example implementation is available at
[Dynamic-Software-Licensing/reference-implementation](https://github.com/Dynamic-Software-Licensing/reference-implementation).
It can be deployed in an AWS account to explore the control-plane flows and validate the
specification behavior in practice.

### How do I get started with DSL in practice?

The best starting point is to understand the core vocabulary and lifecycle model, review the main
API and data objects, and then test the reference implementation to see how entitlement, lease,
policy, identity, and usage flows work together in practice.

### Who is this document for?

The best practices are intended for product teams, architects, platform and operations teams,
system integrators, and decision-makers who need a shared model for software licensing in modern
broadcast and media workflows.

### Why does the repository include annexes, schemas, and API artifacts in addition to the main text?

The main chapters define the overall best-practices model, while the annexes provide supporting
detail, examples, and interpretive material. The API and schema artifacts provide a machine-
readable companion baseline for implementations and technical review.

### How can I contribute to DSL?

The best starting point is the IAMT DSL group page at
[theiamt.org/groups/dynamic-software-licensing](https://theiamt.org/groups/dynamic-software-licensing/),
which explains how to join the group and contribute to the ongoing evolution of the best
practices.

## Annex Positioning

This annex provides concise explanatory support for reviewers and new readers of the best
practices and is intentionally positioned as an early informative reference point for recurring
questions.
