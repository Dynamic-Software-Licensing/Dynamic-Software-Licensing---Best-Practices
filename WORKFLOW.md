# Team Workflow Operating Model

## Purpose

This document defines how the team works together on this repository.
It covers milestone planning, issue-based delivery, roles per work item, and the path from planning to merge.

For governance rules and status definitions, see [GOVERNANCE.md](GOVERNANCE.md).
For contribution mechanics (branch, PR, git commands), see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Roles in the Team

| Role | Primary responsibility |
|---|---|
| Manager | Milestone planning, priority, delivery tracking |
| Editor | Content decisions, status confirmation, merge approval |
| Owner / Contributor | Content creation, branch work, PR |
| Reviewer | Quality review against scope and acceptance criteria |

The Manager and Editor role may be combined in one person.

---

## GitHub Objects and Their Purpose

| Object | Purpose |
|---|---|
| Milestone | Time-bounded delivery goal with scope and deadline |
| Issue | One work item with scope, owner, acceptance criteria |
| Branch | Working context for one issue |
| Draft PR | Active change in progress; early visibility |
| Ready for Review PR | Formal review request |
| Project | Central tracking board for all issues and PRs |

**Key principle:**
- Issue = what and why
- Branch = where work happens
- PR = how decisions are made

---

## Project Board

The team uses a GitHub Project as the central tracking board.

### Recommended Fields

| Field | Type | Purpose |
|---|---|---|
| Status | Single select | Workflow stage |
| Chapter | Text | Affected chapter number |
| Type | Single select | Editorial / Terminology / Informative / Normative / Structural |
| Priority | Single select | P1 / P2 / P3 |
| Owner | Person | Contributor responsible |
| Reviewer | Person | Assigned reviewer |
| Editor | Person | Decision owner |
| Target Date | Date | Deadline |
| Milestone | Text | Milestone name |
| Blocked | Yes/No | Escalation flag |

### Status Values

| Status | Meaning |
|---|---|
| Backlog | Identified but not yet planned |
| Ready | Issue defined, roles assigned, DoR met |
| Drafting | Active work in branch + Draft PR |
| Review | PR is Ready for review |
| Editor Decision | Awaiting merge or rework decision |
| Done | Merged, issue closed |
| Deferred | Moved to next milestone |

### Recommended Automations in Project

- PR opened as Draft → Status to `Drafting`
- PR set to Ready for review → Status to `Review`
- PR merged → Status to `Done`
- Issue closed → Status to `Done`

---

## End-to-End Workflow

### Phase A: Milestone Planning

**Who:** Manager (or Editor/Manager)

1. Define milestone name, start date, and end date.
2. Define 3–7 concrete deliverables with scope and target state.
3. Assign priority (P1 / P2 / P3) to each deliverable.
4. Assign Owner, Reviewer, and Editor per deliverable.

**Output:** Milestone with clear deliverables and ownership.

---

### Phase B: Issue Definition

**Who:** Manager + Owner

1. Create one issue per deliverable.
2. Fill in:
   - Goal
   - In scope / out of scope
   - Acceptance criteria (testable)
   - Affected chapter or files
   - Owner, Reviewer, Editor
   - Deadline
   - Milestone
3. Add issue to Project and set status to `Ready`.

**Output:** Work items with clear scope and roles.

---

### Phase C: Start Drafting

**Who:** Owner

1. Create branch from `main` (`chapter-XX-<short-topic>`).
2. Start working on the content.
3. Open a **Draft PR** once a first meaningful version exists.
   - Not before any content exists.
   - Not after everything is finished.
4. Link the issue in the PR (`Closes #<issue>` or `Related to #<issue>`).
5. Set Project status to `Drafting`.

**Output:** Visible, trackable work in progress.

**Target timing:** Draft PR open by 30–50% completion.

---

### Phase D: Ready for Review

**Who:** Owner

Switch PR from Draft to **Ready for review** when:
- Acceptance criteria are substantially met.
- Scope is aligned with the issue.
- Open points are noted in the PR description.

Set Project status to `Review`.

---

### Phase E: Review

**Who:** Reviewer

1. Review against the issue's acceptance criteria.
2. Review for terminology consistency and structural coherence.
3. Leave specific, actionable comments on the diff.
4. Provide: Approve, Request Changes, or Comment.

**SLA:** First response within 2 business days.

---

### Phase F: Rework

**Who:** Owner

1. Address review comments in the same branch.
2. Resolve conversations in the PR.
3. For significant changes after addressing feedback, re-request review.

**SLA:** Response within 2 business days.

---

### Phase G: Editor Decision and Merge

**Who:** Editor

After review is complete, the Editor decides:

| Decision | Action |
|---|---|
| Merge | PR is merged to `main`, issue closes automatically |
| Rework | PR returns to `Drafting`, Owner is notified |
| Defer | Item is moved to next milestone; Project status to `Deferred` |

The decision is briefly documented in the PR.

After merge:
- Issue closes (via `Closes #` link or manually).
- Project status set to `Done`.
- Chapter status updated if relevant.

---

## Definition of Ready (DoR)

An issue is ready to start when:
- [ ] Goal and scope are clear.
- [ ] Acceptance criteria are written and testable.
- [ ] Owner, Reviewer, and Editor are assigned.
- [ ] Target date and milestone are set.
- [ ] Issue is in Project with status `Ready`.

---

## Definition of Done (DoD)

A work item is done when:
- [ ] Acceptance criteria are met.
- [ ] Review is complete.
- [ ] Editor decision is documented in the PR.
- [ ] PR is merged to `main`.
- [ ] Issue is closed.
- [ ] Project status is `Done`.

---

## Operational Rules

- No work directly on `main`.
- One issue = one branch = one PR.
- No PR without a linked issue.
- Maximum 1 active Draft PR per chapter at a time (WIP limit).
- Blockers unresolved for more than 24 hours: mark `Blocked = Yes` in Project and escalate to Editor/Manager.
- Keep PRs focused and reasonably small to maintain reviewable diffs.

---

## PR Sizing Guidance

Small, focused PRs lead to better review quality and render correctly as rich diffs in GitHub.

| Guideline | Rationale |
|---|---|
| One issue topic per PR | Keeps scope clear |
| Separate structural and content changes | Structure first, then detail |
| Avoid large table or list rebuilds in a single PR | GitHub rich diff breaks on large table changes |
| Split large chapter redrafts into 2–3 sequential PRs | Keeps each PR reviewable |

If a rich diff is not rendering (`This rich diff is not supported`), the PR is likely too large. Split it.

---

## Meeting Rhythm

### Weekly Triage (30 minutes)

Participants: Manager, Editor, Owners

- Review milestone progress.
- Prioritise new issues.
- Identify and resolve blockers.
- Re-scope if needed.

### Weekly Review Board (45–60 minutes)

Participants: Reviewer, Owner, Editor

- Only items in `Review` or `Editor Decision`.
- Resolve open review comments.
- Confirm merge or rework decisions.

### Milestone Closing (30 minutes)

- Document Done vs Deferred.
- Note reasons for deferred items.
- Prepare next milestone.

---

## Escalation

Escalate to Editor/Manager when:
- Deadline risk is visible.
- Reviewer SLA is not met.
- Scope change is needed.
- Disagreement persists after 2 review rounds.

All escalation decisions are documented briefly in the PR or issue.

---

## Example: Milestone with 3 Deliverables

**Milestone:** `M1 – Chapter 09 Structure Stabilisation`
**End date:** 28 March 2026

| Issue | Owner | Reviewer | Editor | Deadline |
|---|---|---|---|---|
| 09.01 General Requirements structure | TBD | TBD | TBD | 20 Mar |
| 09.02 Identity and binding section cleanup | TBD | TBD | TBD | 24 Mar |
| 09.03 Lease and policy boundary sharpening | TBD | TBD | TBD | 28 Mar |

Each deliverable: one issue, one branch, one PR, one decision.
