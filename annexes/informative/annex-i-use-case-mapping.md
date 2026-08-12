# Annex I. Use Case Mapping

## Purpose

This informative annex summarizes how the primary use case classes map to dominant lifecycle,
metering, and continuity expectations.

## Use Case Mapping Summary

| Use case class | Dominant lifecycle emphasis | Typical modality emphasis | Key operational concern |
| --- | --- | --- | --- |
| Continuous operations | renew, inspect, reissue | low-granularity time commitments | uninterrupted continuity |
| Frequent event-driven production | issue, revoke, renew, inspect | recurring time-bounded uplift | repeatable scale-up and release |
| Infrequent event-driven production | issue, revoke, usage reporting | fine-grained or burst-oriented usage | short intense demand windows |
| Test and validation | issue, revoke, inspect | short-lived scoped usage | low-friction ephemeral access |
| AI-powered and outcome-based services | usage reporting, inspect, renew | process-based or outcome-based | trustworthy attribution |
| Resilience and continuity overlay | renew, reissue, revoke | profile-dependent | bounded failover and recovery |

## Interpretation Notes

- The resilience and continuity overlay is cross-cutting rather than a standalone primary use
 case class.
- More than one modality may apply to the same operational class.
- The mapping is intended to support traceability into Chapters 09, 13, and 14.

## Relationship to the Main Document

- Chapter 05.03 defines the use case classes in detail.
- Chapter 05.05 defines the workflow patterns derived from them.
- Chapter 13 shows how those patterns surface in concrete operational profiles.

## Annex Positioning

This annex is a compact review aid for cross-checking lifecycle and modality assumptions across
the draft.
