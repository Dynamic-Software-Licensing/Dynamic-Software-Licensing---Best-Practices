# 04.01 Core Terms

## Chapter Status

- Status: Working Draft
- Editorial maturity: outline
- Normative readiness: not started
- Open drafting points: yes

## Purpose

This section defines the architectural layers, system planes, and logical structural components that make up the proposed reference model.

## Scope Statement

This section covers the structural definitions within the licensing ecosystem's functional boundaries. It explicitly focuses on platform-agnostic roles and components rather than cloud-provider-specific implementation details.

--

## Definitions

**Control Plane** - The control plane is the central authority for entitlements, lease lifecycle management, cryptographic key operations, usage metering, and policy enforcement.

**End User Portal** - A customer-facing management interface providing aggregated visibility, multi-vendor asset views, self-service provisioning, and centralized administrative control over license allocation.

**License Broker (Agent)** - A functional component within the workspace plane that acts as an intermediary interface between applications and the Control Plane to coordinate requests like lease renewals or usage recording.

**Platform Neutrality** - The design and architectural attribute of the Licensing SDK that enables it to execute uniformly, predictably, and without modification across diverse operating systems, hardware architectures, and runtime environments.

**Workspace Plane** - The workspace plane is where licensed applications run and where licensing is enforced locally.
