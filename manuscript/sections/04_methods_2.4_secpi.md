---
section: Methods §2.4 (SECPI Formulation, Classification, Normalization)
status: REVIEWED — substantive rewrite required
review: Flag Archive v2
flags: 5, 26, 33
owner: editor
depends_on: D-02 (normalization ceiling) — BLOCKING
---

# Methods §2.4

## Substantive rewrite required — Option B

The research lead selected **Option B: fixed study-wide reference cutoffs** (D-01, closed). The current text describes the index as *"self-normalizing within the context of each scenario's own cooling output"* and *"scenario-relative rather than absolute."*

**That description is now wrong.** The code implements fixed cutoffs calibrated once via `calibrate_global_reference_cutoffs()`, pooled across k = 1…6, and applied identically at all five ACO instantiation sites. Cutoffs are held constant so that a genuine "more trees improves SECPI" signal is not confounded by the reference frame shifting between k values — that rationale belongs in the rewritten text.

Table 1 (percentile classes 1–4) and the linear weighting structure `W_k = k` survive the change; what changes is *what the percentiles are computed against*.

## Normalization — blocked on D-02

Do not write the 0–5 scale until the ceiling is confirmed.

Theoretical-bounds scheme (min −1.0, max 7.5) is **superseded**: it maps the no-intervention baseline to **0.588**, not 0, and confines realistic outcomes to the bottom ~35% of the scale.

> The baseline is **0.5882**. Entry 1 recorded 2.94 — a double-applied 5× factor. Do not propagate 2.94 anywhere.

Replacement is the **goalposts / distance-to-frontier** method, floor = raw 0.0, ceiling ≈ raw 3.75, clamped to [0, 5]. Cite UNDP HDI technical notes and OECD/JRC (2008) *Handbook on Constructing Composite Indicators* in Methods. Both are strong precedent and a reviewer is unlikely to contest the choice once cited. **The code change is not yet applied.**

## Open

- **#5** — closes when D-02 closes.
- **#26** — "expander heuristic": Almeida et al. (2002)'s term or a team coinage? With Deriver.
- **#33** — the "each cell represents 1 m²" vs. "10×10 fine evaluation grid (10 m² resolution)" contradiction appears *within a single paragraph* of §2.4.2. Fix here as well as in §2.2.

---

<!-- PASTE CURRENT §2.4 BELOW -->
