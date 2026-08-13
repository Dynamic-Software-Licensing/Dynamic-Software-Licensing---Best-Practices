# 09.02. Identity and Binding Requirements

## Purpose

This section defines the requirements for workload identity, identity evidence, and binding
behavior in the Dynamic Software Licensing (DSL) model. These requirements ensure that a lease
is granted and renewed for the intended workload and that mobility and failover do not depend
on static host fingerprints.

Requirements in this section are identified as `IDB-n`.

## Identity and Binding Requirements

### IDB-1 — Verifiable identity evidence

Issue and renew operations **MUST** require verifiable identity evidence representing the
requesting workload or actor. The control plane **MUST** validate that evidence against a
trusted identity source before granting or extending licensed capability.

### IDB-2 — Identity-based binding

Lease binding **MUST** be based on verifiable workload identity rather than on static hardware
attributes alone. Hostname, MAC address, serial number, or similar machine properties **MUST
NOT** be treated as the sole basis of binding.

### IDB-3 — Binding continuity on renewal

Renewal **MUST** re-verify that the requester remains the identity to which the lease was
granted. A renewal request with missing, invalid, or mismatched identity evidence **MUST** be
rejected.

### IDB-4 — Controlled mobility through reissue

When licensed capability moves from one workload identity to another, the move **MUST** occur
through an explicit reissue or equivalent transfer operation governed by the control plane.
Identity changes **MUST NOT** be handled as silent renewal of the original binding.

### IDB-5 — Platform-specific evidence, common semantics

Different deployment environments **MAY** use different identity evidence formats, but the
meaning of successful verification **MUST** remain consistent: the control plane has verified
that the requester is authorized to act for the identified workload in the stated tenant
context.

### IDB-6 — No privileged vendor dependency

The identity and binding model **MUST NOT** require standing privileged access by the vendor
or control-plane operator into the customer runtime environment. Trust **MUST** be established
through presented evidence and protocol interaction rather than remote operator access.

### IDB-7 — Binding visibility and auditability

The effective binding state **MUST** be auditable and inspectable. For each active lease, the
system **MUST** be able to show which verified identity it is bound to, when that binding was
established, and when it was last re-verified.

## Relationship to Other Sections

- Section 09.03 defines how identity-bound leases behave over time through renewal, grace,
  and revocation policy.
- Section 09.04 defines the interface behavior through which issue, renew, and reissue are
  exposed.
- Section 09.07 defines the security controls that protect identity evidence and binding trust.

## Section Positioning

This section translates the DSL design principle of identity-based binding into explicit
requirements. It should be read together with the trust model and security controls, which
define how the verification is secured, and with the API model, which defines how binding is
carried through lifecycle operations.
