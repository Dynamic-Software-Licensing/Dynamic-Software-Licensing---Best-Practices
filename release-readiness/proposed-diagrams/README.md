# Proposed Diagrams (Mermaid)  [LARGELY REDUNDANT — recheck against current `main`]

> **Recheck before adopting.** The current `origin/main` already contains rendered diagram
> images (AWS architecture PNGs and an event-production SVG under `diagrams/`). The premise
> that "nothing renders on GitHub" came from a stale snapshot and is no longer accurate.
> These Mermaid versions may still be useful *only* where a GitHub-inline, diffable diagram
> is genuinely wanted that `main` does not already provide — verify case by case. See
> `../00-REVIEW-SUMMARY.md`.

---

## Why Mermaid

The v0.2.0 review found that `diagrams/` contains `.drawio` source files but **no rendered
images**, so nothing renders on GitHub, and `diagrams/README.md` is empty. Several figures
in the PDF (concept relationships, component interaction, AWS architecture, sequences) have
**no source in the repo at all**.

These proposed diagrams are written in **Mermaid**, which:

- renders natively in the GitHub Markdown viewer (no export step),
- is diffable in pull requests (plain text),
- keeps the source and the rendered figure in one place.

This directly fixes the "diagrams don't render on GitHub" consumability problem.

## Contents and mapping to the document

| File | Renders | Replaces / adds | Doc reference |
|---|---|---|---|
| `reference-model.md` | Conceptual reference model | Renders existing `reference-model.drawio` | Ch.07.01 |
| `concept-relationships.md` | Entitlement → Lease → Token relationships | **New** (PDF figure had no source) | Ch.07.01 |
| `component-interaction.md` | Control/workspace plane components + REST/WS | **New** (PDF figure had no source) | Ch.07.02 |
| `lifecycle-state-model.md` | Lease state machine | Renders existing `lifecycle-state-model.drawio` | Annex D |
| `aws-reference-architecture.md` | AWS zones + metering pipeline | **New** (Annex F Figs 2–4 had no source) | Annex F |
| `sequences.md` | Issue / renew-with-loss / reissue failover | **New** (Annex G was prose only) | Annex G |

## Note on the existing `.drawio` files

Two proposed diagrams (`reference-model`, `lifecycle-state-model`) correspond to existing
`.drawio` sources. I could not execute the drawio tool to export those to SVG/PNG, so these
Mermaid versions are provided as GitHub-renderable equivalents. The group can either:

- adopt the Mermaid versions and retire the `.drawio` files, or
- keep the `.drawio` files as editable masters and additionally export SVGs.

Recommendation: standardize on Mermaid for anything that should render inline on GitHub;
keep `.drawio` only where a richer hand-drawn layout is genuinely needed, and commit an
exported SVG alongside it.

## State-name caveat

`lifecycle-state-model.md` uses the **spec's** Annex D state names. The shadow/target lease
state during reissue is shown as an open question (delta D4) rather than importing the
implementation's `SHADOW` — see `../01-spec-vs-implementation-deltas.md`.
