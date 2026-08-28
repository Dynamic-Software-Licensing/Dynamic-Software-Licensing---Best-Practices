# 12.04. Security Controls

## Purpose

This section defines the security controls of the Dynamic Software Licensing (DSL) best
practices. The controls are the normative mechanisms that achieve the security objectives
(Section 12.01) and mitigate the threats (Section 12.02), within the trust assumptions
(Section 12.03).

Controls are identified as `SEC-n` and use the normative keywords defined in Chapter 03. Each
control records the threats it mitigates. Detailed payloads, claim names, endpoints, and
algorithms are out of scope here; they belong to the canonical API and data model and to the
informative annexes.

## Control Families

The controls are organized into families:

- A. Cryptographic integrity and key custody
- B. Token validity and replay resistance
- C. Identity and binding
- D. Secure transport
- E. Least privilege and access control
- F. Revocation and enforcement
- G. Tenant isolation
- H. Agent and supply-chain integrity

## A. Cryptographic Integrity and Key Custody

### SEC-1 — Signed artifacts

Every license token **MUST** be cryptographically signed by the control plane such that any
alteration is detectable. Implementations **SHOULD** use an established signature container
rather than a bespoke scheme — for example JSON Web Signature (RFC 7515) over a JSON Web Token
(RFC 7519), or PASETO — with algorithms drawn from a standard registry (RFC 7518). *Mitigates
THR-1, THR-4.*

### SEC-2 — Local signature validation

A workspace-plane component (application or agent) **MUST** validate a token's signature,
issuer, audience, and validity times before granting or continuing licensed capability, and
**MUST** follow the JSON Web Token Best Current Practices (RFC 8725) — in particular explicit
algorithm allow-listing to prevent algorithm-confusion attacks. Validation **MUST** be
performable locally without a per-use round-trip to the control plane. *Mitigates THR-1,
THR-2.*

### SEC-3 — Protected key custody

Private signing keys **MUST** be generated and held in a managed key service or hardware
security module (for example a module validated to FIPS 140-3), and managed in line with
established key-management guidance (NIST SP 800-57). Private key material **MUST NOT** be
distributed to the workspace plane or embedded in any client. *Mitigates THR-8.*

### SEC-4 — Key rotation

The control plane **MUST** support signing-key rotation without service interruption.
Consumers **MUST** resolve the current public keys through an authenticated discovery
mechanism — for example a JSON Web Key Set (RFC 7517) referenced by key identifier (the `kid`
header of RFC 7515) — and **MUST** support multiple concurrently valid keys so that rotation
does not prematurely invalidate tokens already issued. Rotation cadence **SHOULD** follow
NIST SP 800-57. Compromised keys **MUST** be revocable. *Mitigates THR-8.*

### SEC-5 — Encryption of sensitive data at rest

Commercially sensitive and personal data held by the control plane (including usage, pricing,
and policy) **SHOULD** be encrypted at rest. *Mitigates THR-10.*

## B. Token Validity and Replay Resistance

### SEC-6 — Short-lived tokens

License tokens **MUST** be short-lived, carrying explicit issued-at, expiry, and not-before
times (the `iat`, `exp`, and `nbf` claims of RFC 7519 where JWT is used). Token lifetime **SHOULD** be the
minimum compatible with the operational continuity needs of the use case. *Mitigates THR-2,
THR-6, THR-7.*

### SEC-7 — Unique token identity

Each token **MUST** carry a unique identifier sufficient to support replay detection and
correlation in audit (the `jti` claim of RFC 7519 where JWT is used). *Mitigates THR-2,
THR-12.*

### SEC-8 — Workload-bound tokens

Each token **MUST** be bound to the specific workload identity it was issued for, so that a
captured token cannot be used on a different workload. Sender-constrained (proof-of-possession)
token mechanisms **SHOULD** be used rather than a bespoke binding — for example
mutual-TLS-bound tokens (RFC 8705) or DPoP (RFC 9449), following the proof-of-possession
semantics of RFC 7800. *Mitigates THR-2, THR-3.*

## C. Identity and Binding

### SEC-9 — Verified identity evidence

Issue and renew operations **MUST** require verifiable workload identity evidence, and the
control plane **MUST** verify it against a trusted identity source before issuing or extending
a lease. Standard machine-to-machine authentication and identity mechanisms **SHOULD** be used
rather than proprietary ones — for example the OAuth 2.0 client-credentials grant (RFC 6749),
OpenID Connect, or workload identity frameworks such as SPIFFE/SVID. *Mitigates THR-3.*

### SEC-10 — Identity-based binding

Binding **MUST** use verifiable workload identity. Binding **MUST NOT** rely solely on static
host attributes such as hostname or MAC address. *Mitigates THR-3.* (See also the design
principle on identity-based binding in Chapter 06.)

### SEC-11 — Fail-closed on invalid identity

If identity evidence is absent, invalid, or unverifiable, issuance or renewal **MUST** be
denied. The system **MUST NOT** fall back to host-based binding or to an unauthenticated
grant. *Mitigates THR-3.*

## D. Secure Transport

### SEC-12 — Authenticated, confidential transport

All communication between the workspace plane and the control plane, including the push
channel used for revocation and policy updates, **MUST** use authenticated, confidential
transport: TLS 1.3 (RFC 8446) or later, with mutually authenticated TLS where feasible.
*Mitigates THR-4, THR-10.*

### SEC-13 — Private connectivity options

For environments with stricter requirements, private network connectivity options **SHOULD**
be supported in addition to public endpoints. *Mitigates THR-10, THR-11.*

## E. Least Privilege and Access Control

### SEC-14 — Least-privilege components

Every control-plane function and workspace-plane component **MUST** operate with the least
privilege necessary for its role. *Mitigates THR-13, THR-9.*

### SEC-15 — No privileged vendor access

The model **MUST NOT** require standing privileged access by the vendor or control-plane
operator into the customer environment. The customer presents identity evidence; the vendor
does not reach into customer infrastructure. *Mitigates THR-13.* (Realizes SEC-OBJ-2.)

### SEC-16 — Per-tenant authorization

Every request **MUST** be authorized in the context of its authenticated tenant. A request
**MUST NOT** be able to read or modify another tenant's entitlements, leases, usage, or audit
data. *Mitigates THR-9.*

### SEC-17 — Role- and scope-based entitlement access

Access to entitlements **SHOULD** be governable by user, role, and scope (for example
project- or production-scoped pools and time-boxed external access), with least-privilege
defaults. Established access-control models **SHOULD** be used rather than ad-hoc schemes —
for example role-based access control (ANSI/INCITS 359), attribute-based access control
(NIST SP 800-162), or OAuth 2.0 scopes (RFC 6749). Emergency overrides **SHOULD** be permitted
but **MUST** be audited. *Mitigates THR-5, THR-9.* (Realizes Chapter 05 theme T7.)

## F. Revocation and Enforcement

### SEC-18 — Revocation capability

The control plane **MUST** support revocation of an active lease (conceptually analogous to
OAuth 2.0 token revocation, RFC 7009). When the affected workload is reachable, revocation
**SHOULD** be delivered promptly through the push channel; when it is not reachable, revocation
**MUST** take effect no later than the next renewal. *Mitigates THR-6.*

### SEC-19 — Bounded exposure window

The maximum time a revoked or expired entitlement can remain in use **MUST** be bounded by the
token lifetime and the offline grace bound (Section 12.06). *Mitigates THR-6, THR-7.*

### SEC-20 — Enforcement of granted dimensions

The workspace plane **MUST** enforce the dimensions and limits carried in the validated token,
and **MUST NOT** permit operation beyond them. *Mitigates THR-5.*

## G. Tenant Isolation

### SEC-21 — Logical tenant separation

Tenant data **MUST** be logically separated, and isolation **MUST** be enforced by the control
plane rather than relying on workspace-plane cooperation. Cryptographic separation of
per-tenant data **SHOULD** be applied where feasible. *Mitigates THR-9, THR-10.*

## H. Agent and Supply-Chain Integrity

### SEC-22 — Integrity-verified distribution

The license agent and SDK **SHOULD** be distributed as integrity-verified, signed artifacts
through trustworthy channels, so that consumers can verify authenticity before deployment.
Established secure-development and supply-chain practices **SHOULD** be applied — for example
the NIST Secure Software Development Framework (NIST SP 800-218), SLSA provenance, and
artifact signing (such as Sigstore or in-toto attestations). *Mitigates THR-14.*

### SEC-23 — Minimal client secrets

Clients **MUST NOT** hold secrets that would allow them to forge entitlement or bypass
validation. Any client credentials **MUST** be limited to authenticating requests, not to
granting capability. *Mitigates THR-8, THR-14.*

## Control-to-Threat Matrix

| Threat | Mitigating controls |
| :--- | :--- |
| THR-1 Token forgery | SEC-1, SEC-2 |
| THR-2 Replay / reuse | SEC-2, SEC-6, SEC-7, SEC-8 |
| THR-3 Identity spoofing | SEC-8, SEC-9, SEC-10, SEC-11 |
| THR-4 Tampering | SEC-1, SEC-12 |
| THR-5 Over-use / evasion | SEC-17, SEC-20 |
| THR-6 Revocation evasion | SEC-6, SEC-18, SEC-19 |
| THR-7 Grace / offline abuse | SEC-6, SEC-19 (with Section 12.06) |
| THR-8 Key compromise | SEC-3, SEC-4, SEC-23 |
| THR-9 Cross-tenant access | SEC-14, SEC-16, SEC-17, SEC-21 |
| THR-10 Data exfiltration | SEC-5, SEC-12, SEC-13, SEC-21 |
| THR-11 Denial of service | SEC-13 (with availability design in Chapter 13) |
| THR-12 Repudiation | SEC-7 (with audit controls in Section 12.05) |
| THR-13 Excessive privilege | SEC-14, SEC-15 |
| THR-14 Supply-chain compromise | SEC-22, SEC-23 |

Two threats are mitigated primarily outside this section: THR-11 (denial of service) depends
on availability and scaling design in the operational and deployment profiles (Chapter 13),
and THR-12 (repudiation) depends on the audit controls in Section 12.05. These are noted here
so the matrix does not appear to leave them uncovered.

## References

This section profiles, rather than restates, established standards. The following are the
principal references; specific algorithm and parameter choices are deferred to the canonical
model and informative annexes.

Normative references (mechanisms a conforming implementation builds on):

- RFC 7515 — JSON Web Signature (JWS) — SEC-1, SEC-4.
- RFC 7517 — JSON Web Key (JWK / JWK Set) — SEC-4.
- RFC 7518 — JSON Web Algorithms (JWA) — SEC-1.
- RFC 7519 — JSON Web Token (JWT), including the `iat`, `exp`, `nbf`, and `jti` claims — SEC-1,
  SEC-6, SEC-7.
- RFC 8725 — JSON Web Token Best Current Practices — SEC-2.
- RFC 8705 — OAuth 2.0 Mutual-TLS client authentication and certificate-bound access tokens —
  SEC-8, SEC-12.
- RFC 9449 — OAuth 2.0 Demonstrating Proof of Possession (DPoP) — SEC-8.
- RFC 7800 — Proof-of-Possession key semantics for JWTs — SEC-8.
- RFC 6749 — OAuth 2.0 Authorization Framework (client-credentials grant; scopes) — SEC-9,
  SEC-17.
- RFC 8446 — TLS 1.3 — SEC-12.
- RFC 7009 — OAuth 2.0 Token Revocation (conceptual analogue) — SEC-18.

Informative references (guidance and good practice):

- NIST SP 800-57 — Recommendation for Key Management — SEC-3, SEC-4.
- FIPS 140-3 — Security requirements for cryptographic modules — SEC-3.
- NIST SP 800-162 — Attribute-Based Access Control — SEC-17.
- ANSI/INCITS 359 — Role-Based Access Control — SEC-17.
- NIST SP 800-218 — Secure Software Development Framework (SSDF) — SEC-22.
- SLSA, Sigstore, in-toto — supply-chain provenance and artifact signing — SEC-22.
- OpenID Connect; SPIFFE/SVID — workload and federated identity — SEC-9.
- PASETO — alternative signed-token format — SEC-1.

## Relationship to Other Chapters

- The objectives (Section 12.01) state the goals these controls achieve; the threat model
  (Section 12.02) defines what they defend against.
- The canonical API model (Chapter 10) defines how the lifecycle operations referenced here
  are invoked; the canonical data model defines the artifacts; the security and trust
  controls are the constraints on both.
- The normative requirements chapter (Chapter 09) is expected to reference these controls in
  its security requirements section.

This section is normative. It states mechanisms and their required strength while remaining
platform-agnostic and free of API- and schema-level detail. Algorithm choices, claim names,
and endpoint definitions are deliberately deferred to the canonical model and annexes.
