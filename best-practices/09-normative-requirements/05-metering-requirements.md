# 09.05 Metering Requirements

## Purpose

This section defines the requirements for usage metering, reporting granularity, correlation,
deduplication, and operational transparency of consumed license dimensions.

Requirements in this section are identified as `MTR-n`.

## Metering Requirements

### MTR-1 — Structured usage dimensions

Where a license modality depends on consumption, usage **MUST** be expressed through structured
dimensions with unambiguous semantics. The model **MUST** support vendor-defined dimensions,
but each dimension **MUST** be documented well enough for customers and integrators to
understand what is being measured.

### MTR-2 — Correlated usage attribution

Usage events **MUST** be attributable to at least a tenant, product or application context,
lease or equivalent grant context, and time of use. Implementations **SHOULD** also support
correlation to a higher-level work or deployment context where that improves transparency and
reconciliation.

### MTR-3 — Bounded buffering during interruption

When connectivity is unavailable, usage events **MUST** be bufferable for later submission so
that short outages do not create blind spots in consumption reporting. Buffered reporting
**MUST** remain bounded by documented policy and storage assumptions.

### MTR-4 — Idempotent reconciliation

The control plane **MUST** process retried or delayed usage events idempotently so that
recovered or repeated submissions do not produce double counting.

### MTR-5 — Separation of usage reporting and runtime enforcement

Usage reporting **MUST** be treated as a reporting and reconciliation function rather than as a
per-use synchronous enforcement dependency. Failure to submit usage immediately **MUST NOT** by
itself force abrupt runtime termination when the current lease and policy remain otherwise
valid.

### MTR-6 — Transparent consumption visibility

The model **MUST** provide enough visibility for customers and operators to understand consumed
dimensions, relevant time windows, and the relationship between active runtime state and
reported usage. Usage transparency **SHOULD** support forecasting, reconciliation, and audit.

### MTR-7 — Compatibility with different modalities

The metering model **MUST** support time-based, process-based, capacity-based, and
outcome-based usage expressions where applicable, without assuming that a single dimension type
fits all products.

## Relationship to Other Sections

- Section 09.06 defines how license modalities determine whether and how usage dimensions are
  applied.
- Section 09.08 defines the operational visibility and alerting expectations associated with
  metering.
- Section 09.09 defines how usage reporting participates in broader automation and external
  system integration.

## Section Positioning

This section translates the DSL need for cost transparency and expressive metering into
practical requirement language. It ensures that usage data is meaningful, attributable, and
reconcilable without turning metering into a fragile runtime dependency.
