# 12.02. Threat Model

## Purpose

This section defines the threat model for the Dynamic Software Licensing (DSL) best practices.
It catalogues the principal security and misuse scenarios that the model must withstand, and
provides the structured basis for the trust assumptions (Section 12.03) and the security
controls (Section 12.04).

This section is descriptive: it identifies threats but does not itself state control
requirements. Each threat is given an identifier (`THR-n`) so that controls in Section 12.04
can cite the threats they mitigate.

## Method

The threat model is expressed in four parts:
1. the assets at risk (carried forward from Section 12.01),
2. the actors and adversary classes,
3. the trust boundaries across which threats act,
4. the catalogue of threats, each mapped to the objectives it endangers.

The model is deliberately platform-agnostic. It addresses threats to the licensing model
itself, not the general security of the underlying platform (for example host hardening,
network perimeter, or physical security), which is the responsibility of the platform and
infrastructure providers.

The threat categories follow established threat-modelling practice (for example the STRIDE
categorization, and the OWASP Application Security Verification Standard as a control
checklist). Where adopters add a likelihood/impact rating, an established scoring method such
as CVSS, applied within a risk process such as NIST SP 800-30, **SHOULD** be used rather than
an ad-hoc scale.

## Adversary Classes

The model considers the following adversary classes:

- **External attacker** — has no legitimate entitlement and seeks to obtain, forge, or
  prolong licensed capability.
- **Compromised workload** — a workspace-plane component under adversary control that attempts
  to abuse a legitimate position.
- **Malicious or careless insider (customer side)** — a user with some legitimate access who
  attempts to exceed entitlements or evade controls, deliberately or accidentally.
- **Over-reaching vendor or control-plane operator** — a party who attempts, or is wrongly
  required, to obtain more access or data than the model intends.
- **Network adversary** — able to observe or modify traffic between planes.
- **Over-using customer** — not malicious, but consuming beyond entitled dimensions in ways
  that, if unmetered, cause revenue leakage.
- **Supply-chain adversary** — able to tamper with the license agent, SDK, or its
  distribution.

## Trust Boundaries

Threats act across the trust boundaries defined by the reference model (Chapter 07):

- the boundary between the **control plane** (the trust authority for entitlements, issuance,
  keys, and policy) and the **workspace plane** (lower-trust execution environments),
- the boundary between **tenants**,
- the boundary between the **customer environment** and the **vendor / control-plane
  operator**,
- the **network** path connecting planes.

The license token is the primary trust-carrying artifact that crosses the control-plane to
workspace-plane boundary, and is therefore a focal point of the threat model.

## Threat Catalogue

### THR-1 — Token forgery

An adversary fabricates or alters a license token to grant capability that was never issued,
or to widen granted dimensions. Endangers SEC-OBJ-1, SEC-OBJ-9.

### THR-2 — Token replay or reuse

A valid token is captured and replayed after expiry, or reused on a workload other than the
one it was issued for, to obtain unentitled capability. Endangers SEC-OBJ-1, SEC-OBJ-9.

### THR-3 — Identity spoofing

An adversary presents falsified identity evidence to obtain a lease for a workload it does not
control or is not entitled to. Endangers SEC-OBJ-1, SEC-OBJ-2, SEC-OBJ-8.

### THR-4 — Tampering in transit or at rest

Lease, policy, dimension, or usage data is modified in transit between planes or in storage,
to alter entitlements or to misreport usage. Endangers SEC-OBJ-1, SEC-OBJ-7.

### THR-5 — Over-use and limit evasion

A workload operates beyond its entitled dimensions (for example more channels or higher
throughput than granted) or suppresses usage reporting, causing revenue leakage. Endangers
SEC-OBJ-9.

### THR-6 — Revocation evasion

A revoked lease continues to be used because the revocation is ignored, the workload is kept
offline to avoid receiving it, or the exposure window is unbounded. Endangers SEC-OBJ-9,
SEC-OBJ-3.

### THR-7 — Abuse of offline and grace behavior

Grace and offline operation are exploited to extend usage indefinitely, for example by
deliberately severing connectivity or tampering with the local clock to defeat expiry.
Endangers SEC-OBJ-9, SEC-OBJ-3.

### THR-8 — Signing key compromise or weak key management

A signing key is exposed, stolen, or not rotated, allowing wholesale forgery of tokens.
Endangers SEC-OBJ-1 (highest-impact threat in the model).

### THR-9 — Cross-tenant access

A tenant gains read or write access to another tenant's entitlements, leases, usage, or audit
data through an isolation failure. Endangers SEC-OBJ-5, SEC-OBJ-7.

### THR-10 — Exfiltration of sensitive data

Usage, pricing, policy, or personal data is disclosed to a party that should not see it,
whether across tenants, to an over-reaching operator, or to a network adversary. Endangers
SEC-OBJ-7.

### THR-11 — Denial of service against control functions

The control plane or its interfaces are overwhelmed or made unavailable, preventing issue and
renewal and thereby threatening production continuity. Endangers SEC-OBJ-3.

### THR-12 — Repudiation

A party disputes a usage record, a lifecycle action, or a policy change because adequate,
tamper-evident audit evidence is absent. Endangers SEC-OBJ-4.

### THR-13 — Excessive privilege into the customer environment

The model or an implementation requires the vendor or control plane to hold standing,
privileged access into the customer environment, expanding the attack surface and violating
least privilege. Endangers SEC-OBJ-2, SEC-OBJ-6.

### THR-14 — Supply-chain compromise of the agent or SDK

The license agent, SDK, or its distribution channel is tampered with, subverting local
validation and enforcement at the source. Endangers SEC-OBJ-1, SEC-OBJ-8.

## Threat-to-Objective Summary

| Threat | Primary objectives endangered |
| :--- | :--- |
| THR-1 Token forgery | SEC-OBJ-1, SEC-OBJ-9 |
| THR-2 Replay / reuse | SEC-OBJ-1, SEC-OBJ-9 |
| THR-3 Identity spoofing | SEC-OBJ-1, SEC-OBJ-2, SEC-OBJ-8 |
| THR-4 Tampering | SEC-OBJ-1, SEC-OBJ-7 |
| THR-5 Over-use / evasion | SEC-OBJ-9 |
| THR-6 Revocation evasion | SEC-OBJ-9, SEC-OBJ-3 |
| THR-7 Grace / offline abuse | SEC-OBJ-9, SEC-OBJ-3 |
| THR-8 Key compromise | SEC-OBJ-1 |
| THR-9 Cross-tenant access | SEC-OBJ-5, SEC-OBJ-7 |
| THR-10 Data exfiltration | SEC-OBJ-7 |
| THR-11 Denial of service | SEC-OBJ-3 |
| THR-12 Repudiation | SEC-OBJ-4 |
| THR-13 Excessive privilege | SEC-OBJ-2, SEC-OBJ-6 |
| THR-14 Supply-chain compromise | SEC-OBJ-1, SEC-OBJ-8 |

## Out of Scope

The following are acknowledged but are not addressed by this chapter, being the
responsibility of platform and infrastructure providers or of other chapters:

- general hardening of hosts, containers, and orchestration platforms,
- network perimeter and physical security,
- vulnerabilities in the licensed application itself unrelated to licensing,
- availability of the underlying platform beyond the licensing control functions.

## References

- STRIDE — threat categorization methodology — informs the threat catalogue structure.
- OWASP Application Security Verification Standard (ASVS) — control checklist for verification.
- CVSS — Common Vulnerability Scoring System — optional likelihood/impact rating.
- NIST SP 800-30 — Guide for Conducting Risk Assessments — risk process.

## Relationship to Other Chapters

- The trust assumptions (Section 12.03) state which of these threats are addressed by design
  assumption versus by active control.
- The security controls (Section 12.04) cite these threat identifiers in their mitigations.
- The reference model (Chapter 07) defines the planes and boundaries referenced here.

This section is descriptive. The threat catalogue is intended to be stable and citable; it
does not use normative keywords. Controls and their normative strength are defined in
Section 12.04.
