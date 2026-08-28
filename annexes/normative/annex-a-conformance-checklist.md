# Annex A. Conformance Checklist

## Purpose

This annex provides a compact checklist structure for assessing whether an implementation can
credibly claim alignment with the DSL best practices and with one of the conformance profiles
defined in Chapter 08.

## How to Use This Annex

This checklist is intended as a review aid, not as a certification instrument. Each statement
should be assessed against observable implementation behavior for the relevant conformance
target.

Possible assessment states include:

- yes,
- partial,
- no,
- not applicable.

## Foundational Checklist

| Area | Checklist statement | Primary requirement anchors |
| --- | --- | --- |
| General architecture | The implementation exposes documented lifecycle behavior rather than manual-only procedures. | GEN-1, GEN-2, API-1 |
| Identity | The grant binds to verifiable workload identity rather than static hardware attributes. | IDB-1, IDB-2 |
| Lease behavior | Lease lifecycle state, renewal, and expiry behavior are explicit and reviewable. | LPR-1, LPR-2, LPR-3 |
| Policy handling | Runtime policy includes bounded grace and defined exhaustion behavior. | LPR-4, LPR-5, OPS-1 |
| Security | Runtime grants are cryptographically protected and validated locally. | SREQ-1, SREQ-2 |
| Observability | Operators can inspect active grants, status, and relevant expiry conditions. | OPS-3, OPS-4 |

## Cloud Native Checklist

| Area | Checklist statement | Primary requirement anchors |
| --- | --- | --- |
| Automation | Licensing can be integrated into CI/CD, IaC, or orchestrated deployment flows. | INT-1, INT-2 |
| Dynamic identity | Identity evidence supports dynamic or cloud-native workload semantics. | IDB-3, IDB-4 |
| Continuity | Renewal retry and continuity behavior remain predictable under transient outage. | OPS-1, OPS-2, LPR-4 |
| API behavior | Lifecycle operations are consistently exposed through documented APIs. | API-1, API-2, API-3 |
| Metering | Usage reporting and attribution support operational and financial interpretation. | MTR-1, MTR-2, MTR-5 |
| Auditability | Operational events are traceable across issue, renew, reissue, and revoke paths. | SREQ-6, OPS-6 |

## Advanced Interoperable Checklist

| Area | Checklist statement | Primary requirement anchors |
| --- | --- | --- |
| Semantic consistency | Canonical API, runtime token, and data model remain aligned across implementations. | API-2, GEN-9, INT-7 |
| Portability | Controlled transfer, reissue, and failover behavior work across environments. | GEN-8, LPR-7, INT-5 |
| Tenant isolation | Multi-tenant controls preserve separation, auditability, and least privilege. | SREQ-4, GEN-6 |
| Modality support | Supported license modalities remain explicit and do not alter core lifecycle semantics. | MOD-1, MOD-2, MOD-5 |
| Integration maturity | External automation and partner-facing integrations preserve documented semantics. | INT-3, INT-5, INT-7 |
| Governance readiness | Terminology, schemas, and lifecycle states are stable enough for repeatable cross-team use. | GEN-1, API-7, LPR-1 |

## Annex Positioning

This annex provides a review-oriented conformance aid tied to Chapter 08 profiles and Chapter
09 requirement groups.
