# Lease Lifecycle State Model (Annex D)

Canonical lease states per Annex D. `ISSUED` may be collapsed into `ACTIVE` by an
implementation. The shadow/target-lease state during two-phase reissue is an open question
(delta D4) and is shown as a note, not imported from the implementation's `SHADOW`.

```mermaid
stateDiagram-v2
  [*] --> ISSUED: issue
  ISSUED --> ACTIVE: activate
  ACTIVE --> RENEWED: renew
  RENEWED --> RENEWED: renew
  ACTIVE --> REISSUING: reissue (transfer)
  RENEWED --> REISSUING: reissue (transfer)
  REISSUING --> REVOKED: finalize (original revoked)
  ACTIVE --> REVOKED: revoke
  RENEWED --> REVOKED: revoke
  ACTIVE --> EXPIRED: validity elapsed
  RENEWED --> EXPIRED: validity elapsed
  ACTIVE --> TERMINATED: controlled close
  RENEWED --> TERMINATED: controlled close
  REVOKED --> [*]
  EXPIRED --> [*]
  TERMINATED --> [*]

  note right of REISSUING
    Open question (delta D4):
    the target/shadow lease's
    pending state is not yet
    named in Annex D.
    Implementation uses SHADOW.
  end note
```
