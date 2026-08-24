# AWS Reference Architecture (Annex F, informative)

GitHub-renderable version of the AWS-specific realization (Annex F Figs 2–4). Informative
only — AWS services are one possible realization of the platform-neutral model; they are
not required for DSL alignment.

## High-level architecture (Annex F, Fig. 2)

```mermaid
flowchart LR
  subgraph Client[Workspace]
    MS[Media Service / SDK / Sidecar]
  end

  subgraph Entry[Public Entry Layer]
    R53[Route 53]
    WAF[WAF + Shield]
    APIGW[API Gateway]
  end

  subgraph CP[Licensing Control Plane]
    L1[Lambda: issue / reissue]
    L2[Lambda: renew / inspect]
    DDB[(DynamoDB: leases / entitlements / policy)]
    KMS[KMS signing]
    EB[EventBridge]
    COG[Cognito - optional]
  end

  subgraph Obs[Observability & Security]
    CW[CloudWatch]
    XR[X-Ray]
    CT[CloudTrail + Config]
    SH[Security Hub / GuardDuty]
  end

  MS --> R53 --> WAF --> APIGW
  APIGW --> L1 --> DDB
  APIGW --> L2 --> DDB
  L1 --> KMS
  L2 --> EB
  CP --> Obs
```

## Metering & usage pipeline (Annex F, Fig. 4)

```mermaid
flowchart LR
  MS[Media Services] -->|usage events| KDS[Kinesis Data Streams]
  KDS --> KF[Kinesis Firehose]
  KF --> S3[(S3 raw + curated)]
  S3 --> GLUE[Glue catalog / ETL]
  GLUE --> ATH[Athena]
  ATH --> QS[QuickSight dashboards]
  S3 -.->|export| EXT[External billing / marketplace]
```
