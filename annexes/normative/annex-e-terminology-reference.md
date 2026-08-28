# Annex E. Terminology Reference

## Purpose

This annex consolidates selected preferred terms used across the DSL best practices where
terminology discipline is especially important for consistent review.

## Preferred Terms

| Preferred term | Use this term for | Avoid or constrain |
| --- | --- | --- |
| Dynamic Software Licensing (DSL) | The initiative and architectural model described in this repository | Informal alternative labels for the same model |
| Entitlement | The legal and commercial right assigned to a tenant or customer | Using lease as a synonym for entitlement |
| Lease | The active, time-bounded grant derived from an entitlement | Using license as the runtime object when the lease is meant |
| License Modality | The granted commercial and operational usage model at runtime | Ambiguous standalone use of modality where the licensing meaning matters |
| Policy Object | The structured runtime and lifecycle behavior controls associated with a lease | Free-form policy wording when a structured object is meant |
| Identity-Based Binding | Binding to verifiable workload identity | Hardware-bound terminology when workload identity is intended |
| Control Plane | The authoritative system managing leases, policy, and usage intake | Mixing it with runtime-side enforcement components |
| Workspace Plane | The runtime-side enforcement and interaction environment | Referring to it as the control plane |

## Terminology Guidance

- Use License Modality as the preferred term in normative, API, schema, and data-model
 contexts.
- Commercial Modality may still be used when discussing higher-level business framing, but it
 should not replace License Modality where runtime behavior is being specified.
- Modality without qualifier should be avoided where the reader could confuse business framing,
 metering structure, and runtime behavior.
- The same term should preserve the same meaning across requirement, API, data model, and
 operational profile chapters.

## Annex Positioning

This annex is the compact normative terminology reference for cross-chapter consistency in the
published DSL best practices.
