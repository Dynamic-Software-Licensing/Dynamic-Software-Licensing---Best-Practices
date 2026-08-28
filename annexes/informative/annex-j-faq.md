# Annex J. FAQ

## Purpose

This informative annex captures short answers to recurring review questions about the DSL best
practices.

## Frequently Asked Questions

### What is DSL at a high level?

Dynamic Software Licensing (DSL) is an open best-practices framework for managing software
entitlements, runtime authorization, policy enforcement, and usage observability in dynamic
broadcast and media environments.

### Is DSL a formal standard?

No. The repository currently publishes best practices with standard-like structure and
traceability, but it is not presented as a certification or formal standards program.

### Does DSL use proprietary technology?

No. DSL does not depend on proprietary technology. It combines established architectural and
security patterns and aims to align with existing standards and broadly available implementation
approaches where that supports interoperability.

### Does DSL include security?

Yes. Security is treated as a first-class design concern throughout the model. DSL defines trust,
identity evidence, policy control, auditable actions, and bounded runtime authorization behavior.
Individual implementations still need to apply their own deployment, monitoring, hardening, and
operational security controls.

### Does DSL require permanent connectivity to a licensing service?

No. The model is designed around signed, locally validatable runtime artifacts with bounded
renewal and grace behavior.

### Does DSL replace every vendor-specific commercial model?

No. The best practices standardize lifecycle semantics and interoperability patterns, while
allowing vendors to retain differentiated commercial offerings.

### Does DSL only fit cloud-native deployments?

No. The model is intended to remain platform-agnostic and to support cloud, on-premises,
hybrid, and resilience-focused environments.

### Why is identity-based binding emphasized so strongly?

Because dynamic workloads, failover, and automation-first operations are difficult to support
reliably with static hardware binding.

### What is the runtime object in DSL?

The runtime object is the lease and its signed token representation, derived from an
entitlement and governed by an effective policy object.

### How can I try out DSL?

An example implementation is available at
[Dynamic-Software-Licensing/reference-implementation](https://github.com/Dynamic-Software-Licensing/reference-implementation).
It can be deployed in an AWS account to explore the control-plane flows and validate the
specification behavior in practice.

### How can I contribute to DSL?

The best starting point is the IAMT DSL group page at
[theiamt.org/groups/dynamic-software-licensing](https://theiamt.org/groups/dynamic-software-licensing/),
which explains how to join the group and contribute to the ongoing evolution of the best
practices.

## Annex Positioning

This annex provides concise explanatory support for reviewers and new readers of the best
practices and is intentionally positioned as an early informative reference point for recurring
questions.
