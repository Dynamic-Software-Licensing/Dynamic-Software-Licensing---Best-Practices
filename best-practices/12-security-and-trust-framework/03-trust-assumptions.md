# 12.03 Trust Assumptions

## Purpose

This section states the trust assumptions of the Dynamic Software Licensing (DSL) model: what
the model treats as trustworthy, what it treats as untrusted, and the external dependencies
on which its security rests. These assumptions explain *how* trust is established and bound,
and they delimit the conditions under which the security objectives (Section 12.01) can be
met against the threats (Section 12.02).

Assumptions are identified as `TRUST-n`. Where an assumption imposes an obligation it uses
normative language; where it merely records a precondition it is stated declaratively.

## Trust Boundary Model

The DSL trust model centres on a clear asymmetry between the two planes defined in the
reference model (Chapter 07):

- The **control plane** is the trust authority. It is the source of truth for entitlements,
  performs issuance, holds signing keys, defines and enforces policy, and records audit.
- The **workspace plane** is treated as a lower-trust execution environment. It is where
  applications run and where tokens are validated and enforced locally.
- The **license agent** mediates between the application and the control plane. It is trusted
  to perform local validation and enforcement, but it is not trusted with secrets that would
  let it forge entitlement.
- The **token** is the trust-carrying artifact. Because it is signed by the control plane and
  validated locally, trust can cross the plane boundary without the workspace plane needing
  privileged access to the control plane.

## Trust Assumptions

### TRUST-1 — The control plane is the entitlement authority

The control plane is assumed to be the sole authority for entitlement decisions, lease
issuance, and policy. The workspace plane **MUST NOT** be able to grant itself entitlement or
widen its own dimensions; it can only validate and enforce what the control plane has signed.

### TRUST-2 — Signing keys remain in protected custody

Private signing keys are assumed to be held in a managed key service or hardware security
module. Private key material **MUST NOT** be distributed to, or be recoverable by, the
workspace plane or any client. The security of the entire model rests on this assumption
(see THR-8).

### TRUST-3 — The workspace plane is potentially hostile

The workspace plane is assumed to be potentially compromised or adversarial. Enforcement
therefore relies on locally verifiable signed tokens with bounded validity, not on trusting
the workload's self-report of its own state. Controls are designed so that compromise of a
single workload yields bounded, time-limited gain.

### TRUST-4 — Identity evidence is verifiable and rooted in a trusted authority

Workload identity evidence is assumed to be verifiable against a trusted identity provider or
attestation source — for example an OpenID Connect provider or a workload identity framework
such as SPIFFE/SVID. The strength of a binding is only as strong as the identity evidence
behind it; the model assumes the chosen identity source is itself trustworthy and that its
evidence cannot be trivially forged (see THR-3).

### TRUST-5 — Local time is reasonably accurate

Local validation of expiry and not-before times assumes a reasonably accurate local clock.
Time synchronization **SHOULD** use a standard protocol — Network Time Protocol (RFC 5905),
preferably with Network Time Security (RFC 8915) where integrity of time matters. Because
clocks can still drift or be tampered with, validity windows **MUST** be kept short and
offline operation **MUST** be bounded, so that the value of clock tampering is limited (see
THR-7).

### TRUST-6 — Public keys are discoverable and authenticated

Consumers are assumed to be able to discover the control plane's current public signing keys
through an authenticated, integrity-protected channel — for example a JSON Web Key Set
(RFC 7517) retrieved over TLS (RFC 8446). A consumer **MUST** authenticate the origin of
public keys so that an adversary cannot substitute its own.

### TRUST-7 — Tenant isolation is enforced by the control plane

The control plane is assumed to enforce tenant isolation for all entitlement, lease, usage,
and audit data. The model does not rely on workspace-plane cooperation to maintain isolation
(see THR-9).

### TRUST-8 — Mutual minimization of trust between vendor and customer

The model assumes neither party must over-trust the other. The customer is not required to
grant the vendor access to its infrastructure (addressed by identity evidence and signed
tokens), and the vendor is not required to trust the customer's unverified self-report
(addressed by signed enforcement and metered, audited usage). This mutual minimization is a
defining assumption of the model and directly serves SEC-OBJ-2 and SEC-OBJ-9.

### TRUST-9 — Transport is authenticated and confidential

Communication between planes is assumed to occur over an authenticated, confidential channel.
The model assumes transport-level protection is in place; it does not assume the network
itself is trustworthy (see THR-4, THR-10).

## External Dependencies

The model's security depends on the correctness and availability of:

- a key management service or hardware security module for key custody and rotation,
- one or more trusted identity providers or attestation sources for identity evidence,
- a public-key distribution mechanism,
- transport security (for example mutually authenticated TLS),
- reasonably synchronized time.

A weakness in any of these dependencies weakens the corresponding assumption above. Adopters
**SHOULD** evaluate these dependencies as part of their own threat assessment.

## What the Model Does Not Assume

- It does **not** assume continuous connectivity between planes; bounded disconnection is
  handled by offline and grace behavior (Section 12.06).
- It does **not** assume the integrity of the workspace plane; it assumes the opposite
  (TRUST-3).
- It does **not** assume that the customer trusts the vendor with infrastructure access, nor
  the reverse (TRUST-8).

## References

- FIPS 140-3; NIST SP 800-57 — key custody and management — TRUST-2.
- OpenID Connect; SPIFFE/SVID — identity providers and workload identity — TRUST-4.
- RFC 5905 (NTP); RFC 8915 (NTS) — time synchronization — TRUST-5.
- RFC 7517 (JWK Set); RFC 8446 (TLS 1.3) — authenticated public-key discovery — TRUST-6,
  TRUST-9.

## Relationship to Other Chapters

- The security controls (Section 12.04) implement the obligations implied by these
  assumptions and compensate where an assumption is weak.
- The offline and grace behavior (Section 12.06) defines the bounded relaxation of the
  connectivity assumption.
- The reference model (Chapter 07) and the security framework objectives (Section 12.01)
  provide the structural and goal context.

## Drafting Notes

This section records assumptions and the obligations they imply. It is intentionally explicit
about what is *not* assumed, because over-stated trust is itself a security risk. It remains
platform-agnostic; concrete identity providers and key services are reserved for the
informative annexes.

## Drafting To-Do

- Cross-check TRUST-4 against the identity and binding requirements once Chapter 09 matures.
- Confirm whether a dedicated trust-boundary diagram should be added to the diagrams set.
