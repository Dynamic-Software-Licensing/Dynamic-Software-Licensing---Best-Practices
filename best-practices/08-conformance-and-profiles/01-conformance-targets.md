# 08.01. Conformance Targets

## Purpose

This section defines the kinds of implementation surfaces to which DSL conformance language can
reasonably apply.

## Why Conformance Targets Matter

The best practices describe a complete operating model, but not every participant implements
every part of that model. Conformance therefore needs to state what exactly is being assessed.

Without this distinction, profile claims become ambiguous. A control plane, a license agent,
an administrative portal, and a vendor integration may each align with the best practices in
different ways.

## Primary Conformance Targets

The DSL best practices should be understood as applying to the following target types:

- control-plane implementations,
- workspace-plane implementations,
- supporting operator and automation interfaces,
- end-to-end deployment patterns that combine these elements.

## Control-Plane Conformance

A control-plane implementation is the system that manages entitlements, leases, policy,
revocation state, token issuance, and usage intake.

Conformance at this layer concerns:

- lifecycle semantics,
- identity verification and binding,
- signed artifact issuance,
- policy handling,
- auditability and observability,
- documented API behavior.

## Workspace-Plane Conformance

A workspace-plane implementation is the runtime-side component that requests, validates,
enforces, renews, and reports according to DSL semantics.

Conformance at this layer concerns:

- local validation behavior,
- policy enforcement,
- identity presentation,
- renewal and retry behavior,
- bounded continuity and grace handling,
- usage attribution where applicable.

## Interface Conformance

Administrative interfaces, SDKs, CLI tools, portals, and automation adapters may also be
assessed for DSL alignment where they expose or rely on canonical lifecycle operations.

Conformance here concerns whether these tools preserve the same semantics rather than whether
they share a specific implementation style.

## System-Level Conformance

Some conformance statements only make sense when assessed across the combined system. Examples
include:

- end-to-end traceability,
- cutover and reissue behavior,
- tenant isolation,
- coherence between API, token, policy, and operational behavior.

## Out of Scope

Conformance in this document does not imply:

- legal certification,
- commercial fairness,
- product feature parity across vendors,
- a requirement that every implementation expose identical internal architecture.

## Section Positioning

This section defines the implementation boundaries to which the profile and checklist logic of
the DSL best practices may be applied.
