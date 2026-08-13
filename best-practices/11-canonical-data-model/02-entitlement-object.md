# 11.02. Entitlement Object

## Purpose

This section defines the canonical entitlement object. An entitlement expresses the rights a
tenant holds to use a licensed application or capability under defined limits, modalities, and
policy conditions.

The entitlement object is the upstream authorization record from which leases are issued.

## Role of the Entitlement Object

The entitlement object records:

- which tenant holds the right,
- which product or application is covered,
- which dimensions and limits may be granted,
- which modalities are permitted,
- which default policy applies,
- which scope restrictions or segmentation rules apply.

An entitlement is not itself a runtime grant. It authorizes the control plane to create one or
more leases within its defined bounds.

## Canonical Structure

| Field | Type | Description |
| --- | --- | --- |
| `entitlementId` | string | Unique identifier of the entitlement |
| `tenantId` | string | Tenant that owns the entitlement |
| `app` | string | Product or application identifier |
| `status` | string | Entitlement status such as active, suspended, or expired |
| `allowedModalities` | array | Modalities that may be granted from this entitlement |
| `dimensions` | array | Maximum allowed dimensions and limits |
| `defaultPolicy` | object | Policy applied unless overridden by an allowed tenant rule |
| `scope` | object | Optional project, environment, or operational scope restrictions |
| `quota` | object | Limits on simultaneous or aggregate grant behavior |
| `validFrom` | string | Start of entitlement validity |
| `validUntil` | string | End of entitlement validity, if bounded |

## Required Semantics

### Product scope

The entitlement must identify which licensed capability it governs. In simple cases this is a
single application; in richer cases it may point to a product family, feature set, or
structured catalog entry.

### Dimensions and limits

The `dimensions` field defines the maximum grantable usage scope, for example channels, frame
rate, bandwidth, sessions, or process units. These are the upper bounds from which an issued
lease draws its granted values.

### Allowed modalities

The `allowedModalities` field defines which modality or modalities are permitted for leases
issued from this entitlement. If a requested modality is not present here, the control plane
must not grant it.

### Policy ownership

The `defaultPolicy` field is the baseline vendor-defined policy attached to the entitlement.
Tenant-level overrides may exist only where the vendor permits them and where such overrides
remain auditable and governed.

## Example Shape

```json
{
 "entitlementId": "ENT-001",
 "tenantId": "tenant-a",
 "app": "app-A",
 "status": "ACTIVE",
 "allowedModalities": ["hourly", "daily"],
 "dimensions": [
  {
   "name": "CHANNELS",
   "maxQuantity": 4
  },
  {
   "name": "FPS",
   "maxQuantity": 60
  }
 ],
 "defaultPolicy": {
  "renewBeforeSeconds": 300,
  "offlineGraceSeconds": 1800,
  "onGraceExhausted": "DRAIN"
 },
 "quota": {
  "maxActiveLeases": 2
 }
}
```

## Relationship to Other Objects

- The lease object is derived from the entitlement object.
- The policy object supplies the behavioral policy referenced by the entitlement.
- The usage event object may later reconcile consumption against the granted rights derived from
 the entitlement.

## Section Positioning

This object defines what a tenant is allowed to receive before any runtime lease exists. It is
the commercial and operational source object for lease issuance.
