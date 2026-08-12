# 04.01 Core Terms

## Chapter Status

- Status: Reviewed Draft
- Editorial maturity: developed draft
- Normative readiness: informative only
- Open drafting points: no

## Purpose

This section defines the highest-level conceptual terms of the Dynamic Software Licensing (DSL) framework. These core terms span across technical, commercial, and operational domains and appear throughout the best practices document.

## Scope Statement

This section:
- identifies foundational concepts that are not limited to a single technical area,
- establishes a common vocabulary to avoid introducing parallel labels or synonyms,
- anchors downstream architecture and requirement chapters.

It does not define low-level component schemas or platform-specific data elements.

## Definitions

**Auditability** - The structural quality that ensures all license lifecycle events, state transformations, and usage metrics are captured in a tamper-proof, chronologically sequential ledger to satisfy regulatory and corporate compliance.

**Commercial Modality** - The overarching business strategy and contract rules (such as subscription, pool allocation, pre-paid tokens, or post-hoc utility consumption) that govern how structural entitlements are priced and accounted for over time. This term should be used for business framing, not as a replacement for the runtime-facing term License Modality.

**Dynamic Software Licensing (DSL)** - The core collaborative initiative and architectural framework focused on modern software licensing approaches for broadcast and media workloads.

**Ecosystem Fragmentation** - The operational friction, administrative overhead, and multi-vendor incompatibility caused by disparate, proprietary, and isolated legacy licensing solutions implemented across a single production pipeline.

**Identity-Based Binding** - A trust mechanism that binds an active license lease to a cryptographically verifiable software or platform identity token rather than legacy, static hardware properties.

**Licensing as Code** - The architectural philosophy of managing, declaring, and provisioning license states using the exact same automated configuration tools (e.g., IaC pipelines) and version-control workflows as the underlying runtime infrastructure.

**Media Functions** - Following [DMF Reference Architecture](https://tech.ebu.ch/dmf/ra), the Media Functions layer provides well-defined units of functionality that act on media streams, files or objects.

**Media Workloads** - Following [DMF Reference Architecture](https://tech.ebu.ch/dmf/ra), Media Workloads combines multiple standalone, stateless "Media Functions" (such as video/audio mixing, format conversion, and graphics rendering) to execute a targeted production requirement.

**Modality** - Informal shorthand for a licensing usage model. In normative, API, schema, and runtime contexts, the preferred term is License Modality to avoid ambiguity between business framing and runtime enforcement behavior.
