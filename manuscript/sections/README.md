# manuscript/sections

One file per section. Each carries YAML frontmatter (status, flags, owner, blockers), the confirmed corrections for that section, and a paste marker for the current text.

## Working method

1. Paste current text below the marker.
2. `editor` reads the frontmatter and the notes **before** touching prose.
3. Deliver **Option A (Polish)** and **Option B (Editorial Audit)** together — never one alone.
4. Log the session, update flag statuses, commit.

## Order of operations

Do **not** work front-to-back. Correct order:

```
02, 03, 04, 05  Methods — corrections confirmed, apply now (03/04 partly blocked)
06, 07          Results, Discussion, Conclusion — flag first, then regenerate, then write
01              Introduction — restructuring is independent, do any time
00              Abstract — LAST, downstream of everything
08              References/Appendices — parallel Deriver track
```

## Status

| File | Reviewed | Blocked by |
|---|---|---|
| `00_title_abstract.md` | ✅ | Results, D-04 |
| `01_introduction.md` | ✅ | — |
| `02_methods_2.1_2.2_grid.md` | ✅ | D-05, Deriver (#9, p0) |
| `03_methods_2.3_cooling.md` | ✅ | Deriver (#30) |
| `04_methods_2.4_secpi.md` | ✅ | D-02 |
| `05_methods_2.5_2.6_vv.md` | ✅ | D-03 |
| `06_results_discussion.md` | 🔴 never | D-02, D-03, **D-06** |
| `07_conclusion.md` | 🔴 never | Results |
| `08_references_appendices.md` | ⬜ not started | — |
