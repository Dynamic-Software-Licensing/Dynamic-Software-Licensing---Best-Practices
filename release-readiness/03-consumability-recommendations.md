# Consumability & Housekeeping Recommendations

> **PARTIALLY OBSOLETE — re-verify against current `main`.** Items about empty schemas,
> missing `api/`, unrendered diagrams, and IABM branding are **already resolved** on the
> current `origin/main` and should be ignored below. The remaining items about document
> *length/repetition and writing style* may still hold, but require a fresh read of the
> current chapters to confirm. See `00-REVIEW-SUMMARY.md`.

These items were identified during review. Those that edit existing content are recorded as
a punch list rather than applied. Strike any item already handled on `main`.

## A. Reduce length and repetition (Finding 6)

The document is ~278 pages. A large fraction is repeated scaffolding rather than technical
content. None of these changes alter normative meaning.

| # | Recommendation | Where | Est. effect |
|---|---|---|---|
| A1 | Collapse the repeated per-chapter and per-subchapter blocks (Purpose / Role Within the Best Practices / Scope / Chapter Positioning / Section Positioning / Relationship to Other Chapters) to a single concise status+purpose block per chapter. | All chapters | Largest single reduction; ~15–25% |
| A2 | Convert Chapter 13 (5 operational profiles) from repeated prose templates to one intro + a comparison table + short per-profile deltas. | Ch.13 | High |
| A3 | Convert Chapter 14 (6 migration phases) from repeated templates to one phase table (activities / outputs / readiness indicators). | Ch.14 | High |
| A4 | Trim Chapter 07 responsibility-model prose that duplicates the RACI tables below it; keep the tables. | Ch.07.07 | Medium |
| A5 | Keep Annexes H and I as quick-reference tables but remove prose that restates Chapter 05. | Annex H, I | Low |

Estimated combined reduction: 20–30% with no loss of technical content.

## B. Resolve ambiguities (Finding 7)

| # | Item | Recommendation |
|---|---|---|
| B1 | SDK vs application enforcement boundary | Add a short conformance note stating the minimum meaning of "enforcement" (SDK validates + exposes claims; application rejects operations exceeding granted dimensions). Ch.07.02 / Ch.09.04. |
| B2 | Grace-period defaults per profile | Provide at least one worked default per operational profile (Ch.13) so implementers are not guessing; keep normative text as "vendor-defined, bounded." |
| B3 | Bare "modality" | Sweep for unqualified "modality" and replace with "License Modality" or "Commercial Modality" per Annex E guidance. |
| B4 | Out-of-band offline token extension | Either formalize it with an API/data-model artifact and a requirement ID, or explicitly mark it non-normative in Ch.07.04. |
| B5 | Uneven normative-readiness labels | Reconcile chapters 9/10/12 status blocks; Ch.09 (where MUST requirements live) should not read as less normatively ready than 10/12. |

## C. Repository housekeeping

| # | Item | Recommendation |
|---|---|---|
| C1 | `WORKFLOW.md` TBD placeholders | Replace the example milestone `TBD` owner/reviewer/editor rows before public release, or clearly mark the section as an illustrative example. |
| C2 | Status alignment | Once content merges, make the PDF version, `best-practices/index.md` status table, per-chapter status blocks, and `CHANGELOG.md` all agree on the real maturity. |
| C3 | Reference-implementation cross-link | Add a prominent link from the best-practices `README.md` to the `dsl-reference-implementation` repo (and vice-versa), so spec and working demo are discoverable from each other. |
| C4 | Diagrams README | Populate the empty `diagrams/README.md` (what each diagram shows, how to edit/export). Covered by the `proposed-diagrams/` package. |
| C5 | Release tagging | When ready, tag a release (e.g. `v0.2.0`) and attach the assembled PDF as a release artifact, so the published version is unambiguous. |
| C6 | Branch-name CI | The allowed branch prefixes (`chapter-`, `annex-`, `schema-`, `fix-`, `governance-`, `workflow-`, `terminology-`) do not include a review/proposal prefix. Either use `governance-` for this package's branch or extend the allowlist. |

## D. Positioning vs best-in-class repos (Finding 1 / question 1)

To reach parity with mature reference repos (e.g. MXL-style), prioritize, in order:

1. Populate the machine-readable artifacts (schemas + OpenAPI) — addressed by this package.
2. Render diagrams natively on GitHub — addressed by this package (Mermaid).
3. Cross-link the working reference implementation (C3).
4. Tag releases and attach the PDF (C5).
5. Then the editorial trimming in Section A for readability.
