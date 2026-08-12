# 11.03 Policy Object

## Purpose

This section defines the canonical policy object used to govern runtime behavior of leases in
the DSL model. The policy object carries the parameters that determine renewal timing, grace
behavior, exhaustion handling, alerting, and related operational controls.

## Role of the Policy Object

The policy object provides the behavioral rules that connect entitlement intent to runtime
enforcement. It should make the operational meaning of a grant explicit and locally
enforceable.

## Canonical Structure

| Field | Type | Description |
| --- | --- | --- |
| `renewBeforeSeconds` | integer | How early renewal should start before expiry |
| `offlineGraceSeconds` | integer | How long operation may continue after expiry without renewal |
| `onGraceExhausted` | string | Standardized exhaustion action |
| `heartbeatSeconds` | integer | Expected runtime or reporting heartbeat interval, if used |
| `renewBackoff` | object | Retry behavior for renewal attempts |
| `alertThresholds` | array | Thresholds at which operator alerts should fire |
| `revocationEndpoint` | string | Push endpoint information, if applicable |
| `tenantOverridesAllowed` | boolean | Whether tenant override of selected settings is permitted |

## Required Semantics

### Explicit local enforceability

The effective policy must be expressible in a way that the workspace plane can enforce locally
while disconnected. Policy semantics must not depend on hidden control-plane logic only.

### Standard exhaustion actions

The canonical model recognizes three controlled exhaustion outcomes:

- `DRAIN` — finish current work and refuse new work,
- `DEGRADE` — continue with reduced capability,
- `STOP` — terminate licensed operation.

Implementations may extend these internally, but the meaning of the canonical set should remain
stable for interoperability and operator understanding.

### Retry behavior

The `renewBackoff` object should define bounded retry semantics, for example:

```json
{
 "initialMs": 2000,
 "maxMs": 30000,
 "jitter": true
}
```

### Policy ownership and override

The policy object is vendor-defined by default. Tenant override is not inherent; it is a
governed capability that exists only where explicitly permitted and audited.

## Example Shape

```json
{
 "renewBeforeSeconds": 300,
 "offlineGraceSeconds": 1800,
 "onGraceExhausted": "DRAIN",
 "heartbeatSeconds": 60,
 "renewBackoff": {
  "initialMs": 2000,
  "maxMs": 30000,
  "jitter": true
 },
 "alertThresholds": [900, 300, 60],
 "tenantOverridesAllowed": true
}
```

## Relationship to Other Objects

- The entitlement object carries the default policy source.
- The lease object carries the effective policy snapshot.
- The token claims object carries the runtime policy data required for local enforcement.

## Section Positioning

This object is the canonical home for renewal, grace, exhaustion, and alert semantics. It
provides the behavioral data model behind the operational and security expectations in the DSL
best practices.
