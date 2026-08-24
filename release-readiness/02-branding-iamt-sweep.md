# Branding Sweep — IABM → IAMT  [OBSOLETE — already done on `main`]

## Status: OBSOLETE

This item was based on a **stale snapshot** of the repository. On the current `origin/main`
(commit `57c6548`), branding is **already fully IAMT**:

- `IAMT` references: 13
- `IABM` references: **0**

No branding sweep is required. This file is retained only to record that the original
finding was resolved before the review (not by it).

If you still want to double-check, run from the repo root:

```bash
git grep -I "IABM\|International Association of Broadcasting" origin/main -- '*.md'
```

Expected result: no matches.

Note: verify the logo asset filename separately (a binary asset is not caught by a text
grep), but the text branding is confirmed clean.
