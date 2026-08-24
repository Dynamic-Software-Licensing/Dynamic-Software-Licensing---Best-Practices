# Component Interaction (Ch.07.02)

Workspace-side responsibilities (identity collection, token delivery, renewal scheduling,
usage buffering, local validation, dimension exposure) interacting with the control-plane
services through the API gateway, with an optional vendor adapter for back-office/marketplace
mirroring.

```mermaid
flowchart LR
  subgraph Workspace[Workspace Plane]
    LA[License Agent]
    APPSDK[Application + SDK]
  end

  subgraph Control[Control Plane]
    GW[API Gateway]
    EO[Event Orchestrator]
    US[Usage Service]
    RS[Reissue Service]
    ES[Entitlements Service]
    LS[Leases Service]
    KS[Keys Service]
    VA[Vendor Adapter - optional]
  end

  LA <-->|REST / WebSocket| GW
  LA -->|deliver token| APPSDK
  GW --> EO
  GW --> US
  GW --> RS
  GW --> ES
  GW --> LS
  LS --> KS
  US --> VA
```
