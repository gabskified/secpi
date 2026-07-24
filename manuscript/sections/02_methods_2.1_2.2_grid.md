---
section: Methods §2.1–§2.2 (Study Framework, Grid Generation, Equity Inputs)
status: REVIEWED — six confirmed corrections ready to apply
review: Flag Archive v2, code-verified
flags: 25, 28, 33, 37, 42
owner: editor
depends_on: deriver (Flag #9, p0 provenance)
---

# Methods §2.1–§2.2

## Corrections confirmed by execution — apply verbatim in intent

### §2.2.1 — V-zone generation (Flag #42)
The described **"30 m Chebyshev buffer" does not exist in the code.** The implementation is a target-count-driven **4-connected BFS** that halts at `n_v_target`. It produces **deterministically exactly 8 V-cells (8% of the grid) on every run, at every seed, with zero variance**, because `n_v_target = int(round(0.075 × 100)) = 8` is fixed before the BFS begins.

A literal Chebyshev buffer is additionally *geometrically incompatible* with the 5–10% target at this grid size — it cannot be made to work as written regardless of implementation. Rewrite to describe BFS. This is an Editor task, not a code task.

### §2.2.2 — CA transition equation (Flag #25)
The equation shows `t+1` on both sides. Verified verbatim against the PDF — this is a real error, not a transcription artifact. The right-hand side must read `p_i^{kl}(t)`, giving a standard first-order recursive Markov form. The code implements the corrected form; validated at **100/100 seeds landing in target density bands across both morphologies**. Prose symbol labels (k, l, j, P) are also inconsistent with the formula — reconcile them.

### Grid resolution (Flags #28, #33)
Stated three incompatible ways across Methods. Correct values: **coarse 10 m × 10 m, fine 1 m × 1 m.** Fix all three sites, and check Figure 4's caption against them.

### §2.2.3 — production parameters
State the land-use bands as the actual targets: P 55–65%, A 25–40%, V 5–10%. Grid compliance verified at 40/40 seeds (20 organic + 20 linear).

## Open

- **#9** — the 55–65 / 25–40 / 5–10 split still has no citation. With Deriver.
- **#37** — cooling decay confirmed **Euclidean**. The old V-zone buffer used Manhattan; now moot since BFS uses neither. What remains: is "Chebyshev space (ℤ²)" a general lattice-indexing convention, or simply an error to delete? See D-05.
- **`p0 = 0.5`** — undocumented parameter. Do not finalize §2.2.2 until the Deriver reports whether Almeida et al. (2002) specifies an initial-condition convention or whether `p0` can collapse into the existing `p_init`.

---

<!-- PASTE CURRENT §2.1–§2.2 BELOW -->
