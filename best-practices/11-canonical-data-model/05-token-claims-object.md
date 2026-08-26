# 11.05. Token Claims Object

## Purpose

This section defines the canonical claims carried in a signed runtime token. The token claims
object is the portable, cryptographically protected representation of the lease data required
for local validation and enforcement in the workspace plane.

## Role of the Token Claims Object

The token claims object carries the subset of lease and policy data that the workspace plane
needs at runtime without requiring a live round-trip to the control plane.

The canonical claims model should work whether the token is represented as a JWT, PASETO, or
another established signed token format with equivalent semantics.

## Canonical Structure

| Field | Type | Description |
| --- | --- | --- |
| `iss` | string | Issuer identifier of the control plane |
| `sub` | string | Subject of the grant, typically the bound workload or lease subject |
| `aud` | string | Intended application or service audience |
| `jti` | string | Unique token identifier |
| `iat` | string | Issued-at timestamp in RFC 3339 date-time form |
| `nbf` | string | Not-before timestamp in RFC 3339 date-time form |
| `exp` | string | Expiry timestamp in RFC 3339 date-time form |
| `tenantId` | string | Tenant context |
| `leaseId` | string | Lease identifier |
| `app` | string | Licensed application identifier |
| `dimensions` | array | Granted dimension values |
| `licenseModality` | string | Granted modality |
| `boundIdentity` | object | Binding summary needed for validation semantics |
| `policy` | object | Effective runtime policy snapshot |

## Required Semantics

### Standard and DSL-specific claims

The token claims object should combine widely understood standard claims such as issuer,
audience, token identity, and validity window with DSL-specific claims describing the grant.

When a JWT representation is used, `iat`, `nbf`, `exp`, and `jti` map directly to the corresponding RFC 7519 registered claims. In the canonical DSL model, those time values are represented as RFC 3339 date-time strings for portability across the textual model, JSON Schema artifacts, and examples.

### Runtime sufficiency

The claims carried in the token must be sufficient for local validation and runtime enforcement
of the currently granted capability. That includes validity time, audience, dimensions,
binding, and effective policy.

### Bounded claim scope

Only the claims needed for local validation and enforcement should be carried in the runtime
token. Sensitive back-office or entitlement-management detail that is not required at runtime
should remain in control-plane data stores rather than being pushed into every token.

## Example Shape

```json
{
 "iss": "https://lic.example.com",
 "sub": "workload:i-0abc123def456",
 "aud": "app-A",
 "jti": "tok-001",
 "iat": "2026-08-12T10:00:00Z",
 "nbf": "2026-08-12T10:00:00Z",
 "exp": "2026-08-12T11:00:00Z",
 "tenantId": "tenant-a",
 "leaseId": "L-01HY6G1Q3Z5W6E3Z2N7X0",
 "app": "app-A",
 "dimensions": [
  {
   "name": "CHANNELS",
   "quantity": 4
  }
 ],
 "licenseModality": "hourly",
 "boundIdentity": {
  "platform": "aws",
  "subject": "i-0abc123def456"
 },
 "policy": {
  "offlineGraceSeconds": 1800,
  "onGraceExhausted": "DRAIN"
 }
}
```

## Relationship to Other Objects

- The lease object is the authoritative source from which the token claims are derived.
- The policy object contributes the locally enforceable policy snapshot.
- The identity evidence object informs the verified binding summarized in the claims.

## Section Positioning

This object defines the portable runtime representation of a DSL grant. It is the canonical
bridge between control-plane state and workspace-plane enforcement.
