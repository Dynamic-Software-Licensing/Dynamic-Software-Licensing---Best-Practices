# 11.06. Identity Evidence Object

## Purpose

This section defines the canonical identity evidence object used to present workload identity to
the control plane. The identity evidence object carries the platform-specific proof that a
requesting workload is entitled to receive or renew a bound lease.

## Role of the Identity Evidence Object

The identity evidence object is the input-side counterpart to the `boundIdentity` summary that
later appears in lease and token data. It provides the raw or near-raw evidence needed for the
control plane to validate trust in the requester.

## Canonical Structure

The canonical model uses a nested object keyed by evidence source or platform so that multiple
runtime environments can be represented without changing the surrounding request structure.

| Field | Type | Description |
| --- | --- | --- |
| `aws` | object | AWS-specific identity evidence |
| `kubernetes` | object | Kubernetes or workload-identity evidence |
| `x509` | object | Certificate-based identity evidence |
| `custom` | object | Other governed platform evidence |

The object does not require all fields at once. The relevant platform-specific sub-object is
populated according to the deployment environment.

## Example Shapes

### AWS example

```json
{
 "aws": {
  "iidDocument": "<base64 json>",
  "iidSignature": "<base64 pkcs7>"
 }
}
```

### Kubernetes example

```json
{
 "kubernetes": {
  "serviceAccountToken": "<jwt>",
  "cluster": "cluster-a",
  "namespace": "production"
 }
}
```

## Required Semantics

### Verification source

The object must contain enough information for the control plane to verify the presented
identity against a trusted authority or attestation source.

### Separation from binding summary

Identity evidence is request-time proof, not the long-term canonical representation of the
binding. The control plane should validate the evidence and then retain a verified summary in
the lease and token rather than embedding all raw evidence everywhere.

### Platform variation, stable interpretation

Evidence format may vary by platform, but successful validation must mean the same thing across
implementations: the control plane has verified the requester's claimed workload identity.

## Relationship to Other Objects

- The lease object stores the verified binding summary derived from the evidence.
- The token claims object carries the runtime binding summary, not the full raw evidence.
- The policy and security model govern what happens if evidence is absent, invalid, or stale.

## Section Positioning

This object defines the canonical request-side trust input for issue, renew, and reissue.
It is the data-model home for the identity-based binding principle.
