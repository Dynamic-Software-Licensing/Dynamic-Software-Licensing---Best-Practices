# 08.04 Profile B - Cloud Native

## Purpose

This section defines the profile for implementations that apply the DSL model in a strongly
automated, cloud-native, and operations-integrated manner.

## Profile Intent

The Cloud Native profile builds on the Foundational profile and adds stronger expectations for
automation, observability, and dynamic workload handling.

## Core Expectations

An implementation aligned with this profile should provide:

- API-first lifecycle handling as the normal operating mode,
- integration with deployment automation and infrastructure workflows,
- stronger identity evidence flows for dynamic workloads,
- mature renewal, retry, and grace handling under transient failure,
- inspectable runtime state and usage reporting suitable for operations and finance,
- support for elastic or event-driven operational behavior.

## Typical Characteristics

- cloud or orchestrated runtime environments,
- regular CI/CD and infrastructure automation,
- higher workload churn and stronger need for reissue or rapid issue behavior,
- broader telemetry and tracing expectations,
- tighter dependency on tenant isolation and secure default behavior.

## Suitable Adoption Scenarios

This profile is typically suitable for:

- dynamic media services running on cloud or container platforms,
- event-driven capacity changes,
- operational models that expect automation-first deployment and recovery,
- organizations that already treat licensing as part of platform engineering.

## Section Positioning

This profile defines the level at which DSL is no longer only compatible with cloud-native
operations, but actively supports them.
