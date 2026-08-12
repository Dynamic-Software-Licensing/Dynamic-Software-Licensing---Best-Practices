# Annex C. Token Claims

## Purpose

This annex defines the baseline claim set carried in the signed runtime token used by the DSL
model.

## Claim Set Overview

The token must carry enough information for local validation and runtime enforcement without
requiring continuous reachability to the control plane.

## Baseline Claims

| Claim | Type | Purpose |
| --- | --- | --- |
| `iss` | string | Identifies the issuing control plane |
| `sub` | string | Identifies the lease subject or bound workload |
| `aud` | string | Identifies the intended application or service audience |
| `jti` | string | Uniquely identifies the token |
| `iat` | string | States when the token was issued |
| `nbf` | string | States when the token becomes valid |
| `exp` | string | States when the token expires |
| `tenantId` | string | Carries tenant context |
| `leaseId` | string | Correlates the token to the lease record |
| `app` | string | Identifies the licensed application |
| `dimensions` | array | Carries granted dimensions for runtime enforcement |
| `licenseModality` | string | Carries the granted license modality |
| `boundIdentity` | object | Summarizes verified binding context |
| `policy` | object | Carries the effective runtime policy snapshot |

## Claim Semantics

- Standard claims and DSL-specific claims are combined in one signed object.
- The token should contain runtime-relevant information only.
- Sensitive commercial or back-office detail that is not needed for enforcement should remain
 outside the token.
- The claim set should remain stable across token formats that provide equivalent trust
 semantics.

## Relationship to Other Artifacts

- The lease object is the authoritative source for token derivation.
- The policy object contributes the effective runtime behavior controls.
- Key distribution relies on the JWKS endpoint defined in Annex B.

## Annex Positioning

This annex is the compact normative reference for the baseline DSL runtime claim set.
