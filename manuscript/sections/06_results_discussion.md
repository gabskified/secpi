---
section: Results and Discussion (§3.1–§3.x)
status: 🔴 NEVER REVIEWED — two severe findings already, from structural inspection alone
review: none
flags: 43, 44 (proposed) — expect many more
owner: editorial-flagger (first), then editor
depends_on: D-02, D-03, D-06 — ALL BLOCKING
---

# Results and Discussion

## This section has never been editorially reviewed

Flag Archive v1 and v2 both stop at the end of Methods. Two serious defects were found here in a single structural pass while merely mapping section headings. Assume more.

## 🔴 Flag #43 (proposed) — §3.1 has no code path

§3.1 reports evaluation of *"all 63 unique subsets of the six Philippine TFTs,"* five trees per configuration. **`AuditedCode_1.py` contains no combinatorial subset sweep.** Verified: no combinatorial class in the inventory; `itertools` imported at line 11 and never called; `AntColonySystemACO`'s `species_subset` parameter never passed by any caller; `main_revised_validation()`'s nine steps contain no such sweep.

The only combinatorial analyzer in project files is `ComprehensiveSpeciesAnalysis` in `INITIALCODE.md` — **a different experiment**: 31 combinations of five species, `n_trees=10`, 70 × 70 `StudyArea`.

Numbers with no reproducible source: SECPI 4.3916 (mono Akleng-parang, rank 3/63), 4.3856 (mono Narra, rank 27/63), marginal deltas 0.6291 and 0.6283, threshold 3.13, the ~28% cliff, the 0.03% diversity result. These are the manuscript's headline findings and they propagate into the Abstract and Conclusion.

See **D-06**. Recovering the original script is the single highest-value action available right now.

## 🔴 Flag #44 (proposed) — `k` means two different things

§3.1 uses `k` for **species subset size** (k=1 mono-species → k=6 full palette, trees fixed at five). The code and the D-03 statistical design use `k` for **number of trees placed** (k = 1…6, the Wilcoxon pairing variable). Two orthogonal axes, one symbol. Resolve the notation before any Results prose is written.

## Also void here — Option B

§3.3's ACO convergence trace (best-per-iteration fluctuating ≈3.02–3.07, global best reached within the first few iterations, persistent best-vs-average gap) was produced under the superseded self-normalizing scheme. The qualitative reading — a flat landscape near the optimum, constrained by plantable-cell count with only five trees — likely survives regeneration, but **the numbers do not.** Re-run, then re-interpret. Do not assume the plateau finding holds; verify it.

## Structure on record

- §3.1 Species Performance of Selected TFTs
- §3.2 Urban Grid Generation and Equity Zone Classification — §3.2.1 Generated Canonical Grid (Fig. 9), §3.2.2 Equity Weight Spatialization (Fig. 10)
- §3.3 ACO Search Dynamics and Convergence — §3.3.1 Convergence Trajectories (Fig. 11)
- §3.x Sensitivity — crown diameter dominant (SI = 0.46); Duhat height minimal (SI = 0.0027); Narra crown diameter range 12–34 m flagged as the highest-value measurement target

Note §3.2.1 and §3.2.2 appear to be figure captions with little or no accompanying text. Confirm whether prose is missing or was never written — a Results subsection consisting only of a figure will draw a reviewer comment.

## What a reviewer will ask, that the current text does not answer

- Why does a mono-species configuration (k=1 Akleng-parang, SECPI 4.3916) rank **3rd of 63** while the full six-species palette ranks lower? This is the paper's most interesting result and it is currently reported rather than explained.
- Given CPA is weighted 0.7 and LAI 0.3 by construction, is "shading dominates evapotranspiration" a finding or a restatement of the weighting? The manuscript must confront this directly — it is the most likely reviewer objection in the paper.
- Rank 3 vs. rank 27 for two species with near-identical marginal deltas (0.6291 vs. 0.6283) implies the ranking is unstable at the top. What is the run-to-run variance?

---

<!-- PASTE CURRENT RESULTS AND DISCUSSION BELOW -->
