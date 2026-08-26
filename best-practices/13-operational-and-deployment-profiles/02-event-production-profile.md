# 13.02. Event Production Profile

## Chapter Status

- Status: Reviewed Draft
- Editorial maturity: developed draft
- Normative readiness: informative only
- Open drafting points: no

## Purpose

This chapter defines the operational and deployment profile for Event Productions used by the Dynamic Software Licensing best practices.

Its purpose is to describe the practical runtime environments and operating patterns that the best practices supports.

## Background
This section describes a reference implementation of the DSL for live event production using software media functions deployed as containerized services in a Kubernetes cluster environment, hosted either on-premises or in a public cloud.

No single licensing model applies across all event scenarios. Requirements vary and continue to evolve as the industry transitions from hardware appliance-based solutions to software-defined infrastructure. Licensing terms may cover a seasonal production, a major international event spanning several weeks, or shorter, more granular periods of use.

Demand is increasing for consumption-based licensing models that enable costs to be forecast and aligned directly with production events and budgets. Accordingly, hourly and minute-based usage models are gaining interest.

Live production spans multiple tiers, from Tier 1 and Tier 1+ international sporting events to Tier 2 and Tier 3 lower leagues and minority sports. Production budgets, creative requirements, audience expectations, and availability requirements vary by tier. Continuity requirements in the event of system failure also vary accordingly.

Higher-tier productions typically require redundant services, which must also be licensed. Lower-tier productions may not justify a full 1+1 redundancy model and may instead require lease transfer or reissue from a failed instance to a replacement or standby instance.

## Live Production Workload Example

The diagram below illustrates a simplified live production workload intended to highlight the key concepts.

![Event Production](../../diagrams/DSL%20Event%20Based%20Production.svg)

The workload represents an event-based production deployment. Resources are ephemeral and are deployed only for the duration of the production, including pre-event setup and post-event tear-down.

Media functions used within the workload must be licensed appropriately. The licensing scheme must support ephemeral deployment. Each media function must obtain the required lease and associated license dimensions before operation and must release the lease when the workload terminates. The model must also support schedule overruns, such as extra time in sports events, through lease extension or renewal.

In the scenario described, the workload supports a small studio operation comprising:

- **Studio Cameras** deployed on the studio floor. These may require feature licenses, such as HDR processing. Cameras may be network-connected or air-gapped.
- **Input Processing** functions used to normalize and convert studio camera output. These may require frame synchronization, facility time alignment, or other licensed advanced features.
- A **Switcher** providing vision mixing for compositing video elements. The switcher may require licenses for supported input types, input counts, or advanced processing functions such as keyers.
- An **Audio Mixer** providing program audio mixing from studio cameras and external microphones. The audio mixer may require licenses for specific filters and effects.
- **Output Processing** used to combine switcher and audio mixer outputs for onward distribution. This may require licenses for signal encoding.

## How DSL addresses Event Production

The industry is transitioning toward software-defined infrastructure and new licensing models. The DSL addresses event-based licensing requirements and supports the following scenarios:

- Multivendor ecosystems and best-of-breed deployments, with vendor-specific license models for required features and dimensions
- Platform-neutral licensing for both public cloud and on-premises deployments
- Leasing of licenses and associated dimensions for a defined validity period
- Usage metering to support consumption-based models
- Lease extension for overrunning events and schedule changes
- High-availability deployments, including licensing of redundant instances and lease transfer from failed instances to replacement instances

Adoption of the DSL may not be uniform across the vendor community in the early stages. However, the best practices defined in this repository are intended to provide a vendor-neutral solution developed by the industry for the needs of end users, system integrators, and ISVs.

## Chapter Positioning

This chapter provides the operational interpretation layer for event-driven deployments within
the DSL best practices.

It connects the abstract lifecycle, entitlement, metering, and continuity concepts from the
earlier chapters to a concrete deployment profile with short-lived workloads, schedule-driven
runtime, and tier-dependent availability expectations.
