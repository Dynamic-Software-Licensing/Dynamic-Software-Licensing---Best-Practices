# 12.05. Audit and Compliance

## Purpose

This section defines the audit and compliance requirements of the Dynamic Software Licensing
(DSL) best practices. Auditability underpins non-repudiation, dispute resolution, and
operation in regulated environments. This section realizes objective SEC-OBJ-4 and mitigates
the repudiation threat (THR-12).

Requirements are identified as `AUD-n` and use the normative keywords defined in Chapter 03.

## Audit Requirements

### AUD-1 — Comprehensive lifecycle auditing

All license lifecycle operations — issue, renew, reissue, revoke, usage reporting, and policy
change — **MUST** be recorded in an audit log. *Realizes SEC-OBJ-4.*

### AUD-2 — Sufficient audit content

Each audit record **MUST** capture enough to reconstruct the event: the actor or component,
the action, the affected entitlement or lease, the relevant correlation identifiers (for
example the work and lease identifiers), the outcome, and an accurate timestamp. *Mitigates
THR-12.*

### AUD-3 — Append-only and tamper-evident

Audit records **MUST** be append-only and tamper-evident, so that records cannot be silently
altered or deleted after the fact. Log management **SHOULD** follow established guidance
(NIST SP 800-92), and tamper-evidence **SHOULD** use a recognized mechanism such as
cryptographically signed log entries (for example RFC 5848) or hash-chaining rather than a
bespoke scheme. *Mitigates THR-12, THR-4.*

### AUD-4 — Policy-change auditing

Creation and modification of policy and entitlements — including vendor defaults and any
permitted tenant overrides — **MUST** be audited, recording who changed what and when.
*Mitigates THR-12.* (See the policy governance discussion in Section 12.06.)

### AUD-5 — Trustworthy usage records

Usage records **MUST** be recorded in a manner that is tamper-evident and idempotent, so that
buffered or retried submissions cannot cause double counting and so that usage cannot be
silently understated. *Mitigates THR-5, THR-12.* (See also the metering theme T5 in
Chapter 05.)

### AUD-6 — Retention and protection

Audit and usage records **SHOULD** be retained according to a defined retention policy and
**MUST** be protected against unauthorized access, modification, and deletion for their
retention period. *Mitigates THR-10, THR-12.*

### AUD-7 — Exportability for governance

The system **SHOULD** support export of audit and usage data in a consumable form, so that
finance, operations, security, and governance functions can reconcile, report, and
investigate. (Supports Chapter 05 themes T5 and T6.)

## Compliance Alignment

### AUD-8 — Alignment with applicable frameworks

The model **SHOULD** be implementable in a way that aligns with the compliance frameworks
applicable to the adopter's environment. Representative frameworks relevant to media and
broadcast operations include:

- **ISO/IEC 27001** and **ISO/IEC 27002** — information security management and controls,
  with **ISO/IEC 27017** (cloud security) and **ISO/IEC 27018** (PII in public cloud) where
  cloud deployment applies;
- **GDPR** (Regulation (EU) 2016/679) and comparable data-protection regimes — protection of
  personal data;
- **TPN (Trusted Partner Network)** — content security for media and entertainment;
- **SOC 2** (AICPA Trust Services Criteria) — where customers require service-organization
  assurance.

These are illustrative, not exhaustive or mandatory. The specific obligations that apply
depend on the adopter's jurisdiction, customers, and content. This best practice does not
certify compliance; it aims not to obstruct it.

### AUD-9 — Data minimization

Personal and commercially sensitive data **SHOULD** be minimized to what is necessary for
licensing, metering, and audit, and **SHOULD NOT** be collected or retained beyond that need.
*Supports GDPR-style obligations; mitigates THR-10.*

### AUD-10 — Separation of duties for sensitive actions

Where an adopter's compliance regime requires it, sensitive administrative actions (for
example key management or bulk revocation) **SHOULD** support separation of duties and be
individually attributable in the audit record. *Mitigates THR-12, THR-13.*

## Audit and the Trust Model

Audit is the mechanism by which the mutual minimization of trust (TRUST-8) is made
accountable. Because neither party fully trusts the other, both rely on tamper-evident records
to resolve disputes:

- the vendor relies on trustworthy usage and lifecycle records to substantiate charging,
- the customer relies on the same records to verify that charging reflects actual,
  entitled use,
- both rely on policy-change auditing to confirm that grace and entitlement changes were
  authorized.

Auditability therefore is not only a control; it is a precondition for the commercial trust
the model depends on.

## References

- NIST SP 800-92 — Guide to Computer Security Log Management — AUD-1 to AUD-3.
- RFC 5848 — Signed Syslog Messages — tamper-evident logging — AUD-3.
- NIST SP 800-53 (control AC-5, Separation of Duties) — AUD-10.
- ISO/IEC 27001, 27002, 27017, 27018 — information security management — AUD-8.
- GDPR (Regulation (EU) 2016/679) — personal-data protection and minimization — AUD-8, AUD-9.
- TPN (Trusted Partner Network) — media content security — AUD-8.
- SOC 2 (AICPA Trust Services Criteria) — service-organization assurance — AUD-8.

These compliance frameworks are referenced as informative alignment targets; this best
practice does not assert or confer certification against any of them.

## Relationship to Other Chapters

- The security controls (Section 12.04) protect the integrity of the records described here
  (notably SEC-1, SEC-7, SEC-21).
- The metering and observability themes in Chapter 05 (T5, T6) and the operational profiles
  (Chapter 13) consume the exported data described in AUD-7.
- The canonical data model defines the structure of audit and usage records; this section
  defines their required properties, not their schema.

This section is normative for auditability and advisory for compliance alignment. It names
representative compliance frameworks as examples only and avoids asserting certification. It
remains platform-agnostic: specific log stores, retention services, and reporting tools are
reserved for the informative annexes.
