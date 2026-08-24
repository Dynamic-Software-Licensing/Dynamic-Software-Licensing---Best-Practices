# Reference Model (Ch.07)

Platform-neutral view: the trusted Control Plane is the authority for entitlements, leases,
keys, policy, and usage intake; the semi-trusted Workspace Plane runs applications and
enforces locally using signed tokens. The End User Portal is a cross-cutting management
layer.

```mermaid
flowchart LR
  subgraph CP[Control Plane - trusted authority]
    ENT[Entitlements Service]
    LEA[Leases Service]
    KEY[Keys / JWKS Service]
    USG[Usage Service]
    RIS[Reissue Service]
    EVT[Event Orchestrator]
    GW[API Gateway]
  end

  subgraph WP[Workspace Plane - semi-trusted]
    AG[License Agent]
    APP[Application + SDK]
  end

  PORTAL[End User Portal]

  AG -->|REST: issue / renew / reissue / revoke / usage| GW
  GW --> LEA
  GW --> USG
  GW --> ENT
  LEA --> KEY
  LEA --> RIS
  EVT --> LEA
  CP -.->|WebSocket: revocation / policy push| AG
  AG -->|signed token| APP
  APP -->|validate locally via JWKS| KEY

  PORTAL -.->|read state, force-release, capacity| GW
```
