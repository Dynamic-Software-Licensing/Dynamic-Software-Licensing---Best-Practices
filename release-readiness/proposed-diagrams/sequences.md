# Example Sequences (Annex G)

GitHub-renderable versions of the three Annex G sequences, which are currently prose-only.

## Sequence 1 — Initial Issue

```mermaid
sequenceDiagram
  participant App as Application
  participant Agent as License Agent
  participant CP as Control Plane
  participant KMS as Key Service (JWKS)

  Agent->>Agent: collect identity evidence
  Agent->>CP: POST /v1/leases (app, tenantId, identityEvidence, workId, dimensions, modality)
  CP->>CP: validate entitlement, identity, quota
  CP->>KMS: sign token
  CP-->>Agent: 201 { leaseId, token, expiresAt, policy }
  Agent->>App: deliver signed token
  App->>KMS: fetch JWKS (cached)
  App->>App: validate token locally, enforce dimensions
```

## Sequence 2 — Renewal with temporary connectivity loss

```mermaid
sequenceDiagram
  participant App as Application
  participant Agent as License Agent
  participant CP as Control Plane

  Note over Agent: renewal window opens (expiresAt - renewBeforeSeconds)
  Agent->>CP: POST /v1/leases/{id}:renew
  CP--xAgent: control plane unreachable
  loop retry with backoff + jitter (token still valid)
    Agent->>CP: POST /v1/leases/{id}:renew
  end
  alt connectivity returns within grace window
    CP-->>Agent: 200 { token, expiresAt }
    Agent->>App: deliver refreshed token
  else grace window exhausted
    Agent->>App: apply policy action (DRAIN / DEGRADE / STOP)
  end
```

## Sequence 3 — Reissue for failover (two-phase)

```mermaid
sequenceDiagram
  participant New as New Workload Agent
  participant CP as Control Plane
  participant Old as Original Agent

  New->>New: collect target identity evidence
  New->>CP: POST /v1/leases/{id}:reissue (toIdentityEvidence, toWorkId)
  CP->>CP: create SHADOW lease (original still active)
  CP-->>New: 200 { reissueId, cutoverToken, toLease }
  New->>CP: POST /v1/leases/{id}:finalizeReissue (reissueId, cutoverToken)
  CP->>CP: activate shadow, revoke original
  CP-->>New: 200 { state: COMPLETED, revoked: <originalLeaseId> }
  CP-->>Old: WebSocket revocation (or enforced at next renewal if offline)
  Old->>Old: drain / stop per policy
```
