# Annex J. FAQ

## Purpose

This informative annex captures short answers to recurring review questions about the DSL best
practices.

## Frequently Asked Questions

### Is DSL a formal standard?

No. The repository currently publishes best practices with standard-like structure and
traceability, but it is not presented as a certification or formal standards program.

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

## Annex Positioning

This annex provides concise explanatory support for reviewers and new readers of the draft.
