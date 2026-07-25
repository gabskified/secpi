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

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 1151–1341).
> Content: §2.4 Optimization Process (2.4.1 ACO, 2.4.2 SECPI)
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

2.4 Optimization Process
The optimization process involves the utilization of Ant
Colony Optimization (ACO), a metaheuristic algorithm
involving the use of artificial agents to place ‘pheromones’
within a solution space to minimize the Synergistic and
Equitable Cooling Performance Index (SECPI), an objective
function derived from Bio-Thermal Gain Index (BTGI), a
metric of human physiological response to temperature
differences (Shaamala, 2025).
2.4.1 Ant Colony Optimization
This is the algorithm used for the study. According to
Shaamala (2024), the ant colony algorithm (ACO) uses
artificial agents akin to ants placing pheromones within a
graph (solution space), guiding their search to optimal paths
within that graph. The study contextualizes the use of the
ACO algorithm through a performance analysis comprising
two parts: scenario generation evaluation and
post-optimization evaluation. Scenario generation evaluation
involves tree placement optimization using the ACO
algorithm in clustered and randomized patterns and
comparison of cooling with the baseline scenario. The ACO
was implemented using the scikit-opt library in Python.
The ACO metaheuristic is employed to solve the
combinatorial placement problem on the coarse integer
lattice:
● Artificial "ants" probabilistically traverse a discrete
grid, selecting a cell and a species for planting. The
probability is influenced by: 1) Heuristic
Information (η): The innate desirability (e.g., cooling
coefficient, vulnerability weight of the cell), and 2)
Pheromone Trail (τ): A collective memory deposited
by previous ants, reinforcing choices that led to
high-quality solutions.
● After all ants construct a full planting configuration,
its quality is evaluated using the cooling model and
SECPI. Pheromones on the paths of high-scoring
solutions are reinforced, while global evaporation
occurs to prevent stagnation.
● The algorithm was configured with a colony size of
50 artificial ants over 100 iterations. Over many
iterations, the colony's search concentrates on the
most promising regions of the vast solution space,
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 11

converging toward a high-performing, synergistic
arrangement of trees.
Figure 6. The utilized flowchart showing the process of Ant
Colony Optimization (ACO).
2.4.2 Synergistic and Equitable Cooling Performance
Index (SECPI)
The Synergistic & Equitable Cooling Performance Index
(SECPI) is a novel metric adapted from Shaamala’s
Bio-Thermal Gain Index (BTGI), which itself utilizes the
Universal Thermal Climate Index (UTCI). The UTCI is a
standardized, multi-parameter index that models human
physiological response to the thermal environment, providing
a comprehensive measure of thermal comfort that integrates
the effects of air temperature, humidity, wind speed, and
radiant heat (Bröde et al., 2012). Building upon this temporal
stress-assessment framework, the SECPI serves as the
comprehensive objective function for this optimization
framework. Its purpose is to quantitatively evaluate and score
any given urban tree configuration based on two integrated
criteria: the magnitude of cooling improvement and the equity
of its distribution across socially vulnerable areas.
The SECPI operates on the fine-resolution evaluation grid,
GF, which discretizes the study area into uniform cells. For
any cell i ∈ GF, the total experienced cooling, Ctotal(i), is first
computed by summing the biophysically-scaled,
distance-decayed contributions from all trees in the
configuration, followed by the application of the sigmoidal
competition reduction factor, Rcomp(i), as defined in the
cooling proxy model. This value, Ctotal(i), represents the final,
competition-adjusted cooling benefit at that location.
To translate the continuous cooling field into a distributional
metric, each cell i is assigned to one of four ordinal benefit
classes based on quartiles of the cooling distribution across
GF. Let Q1, Q2, and Q3, represent the 25th, 50th, and 75th
percentiles (first, second, and third quartiles) of the set
𝐶 for the scenario being evaluated. The
𝑡𝑜𝑡𝑎𝑙
(𝑖) : 𝑖 ∈ 𝐺
𝐹
{ }
classification function is formally defined as:
This quartile-based classification ensures that the
performance assessment is self-normalizing within the
context of each scenario's own cooling output. The area
proportion, Ak, for a given benefit class k and a specific
scenario (e.g., optimized or baseline) is then calculated as the
count of cells in that class divided by the number of grid cells:
𝐴
𝑘 =
𝑖 ∈ 𝐺
𝐹
|{ : 𝐶𝑙𝑎𝑠𝑠(𝑖) = 𝑘}|
𝐺
𝐹
| |
The core of the SECPI measures the shift in these area
proportions from a baseline scenario (e.g., no trees or a
random placement) to an optimized planting scenario. This
shift 𝐴 is weighted by a fixed benefit-class
𝑘,𝑜𝑝𝑡𝑖𝑚𝑖𝑧𝑒𝑑 − 𝐴𝑘,𝑏𝑎𝑠𝑒
weight, Wk, which increases linearly (Wk = k) to assign greater
value to improvements in higher-cooling classes. Crucially, to
integrate spatial equity, this weighted shift is further
multiplied by the mean social vulnerability weight of all cells
that have shifted into class under the optimized scenario. Let
We (i) be the predefined social vulnerability weight for cell i.
The mean equity weight for class k in the optimized scenario
𝑊 is calculated as:
𝑒,𝑘
𝑊𝑒,𝑘 =
1
|{𝑖 : 𝐶𝑙𝑎𝑠𝑠(𝑖) = 𝑘 𝑖𝑛 𝑡ℎ𝑒 *𝑜𝑝𝑡𝑖𝑚𝑎𝑙* 𝑠𝑐𝑒𝑛𝑎𝑟𝑖𝑜}| ∑ 𝑊𝑒
(𝑖)
The complete SECPI formula, which sums these
equity-weighted improvements across all four benefit classes,
is therefore:
𝑆𝐸𝐶𝑃𝐼 =
𝑘=1
4
∑ (𝐴
𝑘,𝑜𝑝𝑡𝑖𝑚𝑖𝑧𝑒𝑑 − 𝐴𝑘,𝑏𝑎𝑠𝑒
) · 𝑊𝑘
[ ] · 𝑊𝑒,𝑘
A positive SECPI score indicates a net improvement over the
baseline, with the magnitude reflecting the degree of
improvement. The index's design ensures that higher scores
result from configurations that not only generate greater
cooling (shifting area into Classes 3 and 4) but do so
preferentially in locations of higher social vulnerability, as
captured by the 𝑊 term.
𝑒,𝑘
This makes the SECPI a single, interpretable metric that
guides the Ant Colony Optimization algorithm toward
solutions that are biophysically effective, cognizant of
tree-tree competition, and socially equitable.
To minimize the index or function in a predetermined
number of cycles, the objective function from Shaamala’s
work (2024) is used. Let 𝑖 and 𝑗 be the index representing
potential tree locations and the set comprising all viable tree
locations within the defined area, respectively. Let 𝑝 also be
the predetermined number of trees to be distributed within a
defined area. Thus, the objective function is notated as:
Maximize 𝑓(𝑥 , where represents the
1
, 𝑥
2
,..., 𝑥
𝑖
) 𝑓(𝑥
1
, 𝑥
2
,..., 𝑥
𝑖
)
SECPI, where 𝑥 indicates the binary decision of placing a
𝑖
tree at the 𝑖 potential site. Then,
𝑡ℎ
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 12

𝑖∈1
∑ 𝑥
𝑖 = 𝑝
𝑥 , where
𝑖
∈ {0, 1}, ∀
𝑖
∈ 𝐼
The spatial visualization and heatmap generation in this study
are derived purely from theoretical simulation outputs within
a 100 m × 100 m discrete grid framework, where each cell
represents 1 m². Cooling effects are computed per cell based
on tree placements modeled as lattice points of Chebyshev
space (ℤ²), with decay functions applied to propagate cooling
intensity across the grid. Resulting heatmaps generated
programmatically using Python’s Matplotlib and Seaborn
libraries depict the spatial distribution as continuous color
gradients across a 10×10 fine evaluation grid (10 m²
resolution), where warmer colors represent higher cooling
intensity (ΔT) interpolated from the discrete coarse-grid
planting layout. Comparative heatmaps are used to illustrate
synergy effects, spatial equity weighting, and the performance
of the proposed Synergistic and Equitable Cooling
Performance Index (SECPI), providing the basis for
interpreting optimization outcomes in a computational
context.
