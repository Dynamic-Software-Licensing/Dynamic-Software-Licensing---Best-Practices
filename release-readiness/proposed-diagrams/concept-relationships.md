# Concept Relationships (Ch.07.01)

Entitlement authorizes dimensions, policy, and modality; a Lease is derived from an
entitlement, bound via identity evidence, correlated via work ID, governed by policy, and
expressed as a signed Token.

```mermaid
flowchart TD
  E[Entitlement]
  D[Dimensions]
  P[Policy]
  IE[Identity Evidence]
  W[Work ID]
  LM[License Modality]
  L[Lease]
  T[Token]

  E -->|authorizes| D
  E -->|authorizes| P
  E -->|authorizes| LM
  D -->|carried into| L
  P -->|governs| L
  IE -->|binds| L
  W -->|correlates| L
  LM -.->|constrains| L
  L -->|expressed as| T

  subgraph TokenContent[Token carries]
    TD[dimensions]
    TP[policy]
    TB[binding]
    TX[expiry]
  end
  T --- TokenContent
```
