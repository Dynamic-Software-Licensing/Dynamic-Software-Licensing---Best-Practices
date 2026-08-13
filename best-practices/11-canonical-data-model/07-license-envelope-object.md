# 11.07. License Envelope Object

## Purpose

This section defines the canonical license envelope object. The license envelope is an optional
container used when canonical DSL grant data must carry or accompany vendor-specific licensing
artifacts in a structured, interoperable way.

## Role of the License Envelope Object

The DSL model seeks common lifecycle semantics without forcing every vendor to abandon its
existing product-specific license representation immediately. The license envelope object
provides a bridge for those cases by separating:

- canonical DSL metadata that all participants can understand, and
- vendor-specific payloads that remain necessary for a particular implementation.

## Canonical Structure

| Field | Type | Description |
| --- | --- | --- |
| `leaseId` | string | Lease to which the envelope applies |
| `tenantId` | string | Tenant context |
| `app` | string | Licensed application identifier |
| `issuedAt` | string | Envelope creation time |
| `format` | string | Vendor payload format identifier |
| `payload` | object or string | Vendor-specific license content |
| `metadata` | object | Canonical metadata describing how to interpret the payload |

## Required Semantics

### Canonical wrapper, vendor-specific body

The envelope should make it clear which parts are canonically interpretable by DSL tooling and
which parts remain vendor-specific. Canonical lifecycle semantics must not be hidden only in
the vendor-specific payload.

### Optional bridging mechanism

The license envelope is not required for every implementation. If the canonical lease and token
model are sufficient, no additional envelope is needed. The envelope exists for interoperability
bridging and migration scenarios.

### Explicit format declaration

Where a vendor-specific payload is present, the envelope should declare its format explicitly so
that clients know whether they can parse, pass through, or simply store the payload.

## Example Shape

```json
{
 "leaseId": "L-01HY6G1Q3Z5W6E3Z2N7X0",
 "tenantId": "tenant-a",
 "app": "app-A",
 "issuedAt": "2026-08-12T10:00:00Z",
 "format": "vendor-x-license-v2",
 "metadata": {
  "carrier": "embedded",
  "purpose": "feature-enablement"
 },
 "payload": {
  "vendorFeatureFlags": ["HDR", "MULTIVIEW"]
 }
}
```

## Relationship to Other Objects

- The lease object provides the canonical grant context for the envelope.
- The token claims object provides the interoperable runtime enforcement data.
- The envelope may carry vendor-specific feature detail that is not part of the canonical token
 claims set.

## Section Positioning

This object is the canonical bridge between the DSL common model and vendor-specific license
payloads. It supports migration and interoperability without redefining the DSL core lifecycle
or trust semantics.
