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

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 1428–2088).
> Content: RESULTS AND DISCUSSION §3.1–§3.5
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

RESULTS AND DISCUSSION
3.1 Species Performance of Selected TFTs
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 13

The combinatorial species optimization evaluated all 63
unique subsets of the six Philippine TFTs, producing
configurations ranging from mono-species (k=1) to the full
six-species palette (k=6). Each configuration permitted the
ACO to place five trees, drawing freely from the available
species pool. The results reveal consistent patterns in species
dominance, the functional role of diversity, and how the
optimizer allocates species under varying palette sizes.
3.1.1 Biophysical Parameter Profiles
Scientific
Name
Common
Name
Height
(m)
LAI CPA (m2) CD (m)
Lagerstroemia
speciosa
Banaba 9-18 3.5-4.5 78.5-113 10-12
Pterocarpus
indicus
Narra 30 4.0-5.0 113-908 12-34
Mimusops
elengi
Kabiki 9-18 4.5-6.0 78.5-113 10-12
Syzygium
cumini
Duhat 14-30 2.5-4.0 50-95 8-11
Albizia
lebbeck
Akleng-parang 18-30 2.5-3.5 254-707 18-30
Terminalia
catappa
Talisay 35 4.0-5.5 63-177 9-15
Table 3. Morphological and Evapotranspiration Traits of
the 6 TFTs
Scientific
Name
Common
Name
l₀ l₁ h₀ h₁
Lagerstroemia
speciosa
Banaba 0.20 1.8 45.8 0.72
Pterocarpus
indicus
Narra 0.25 1.9 51.2 0.75
Mimusops
elengi
Kabiki 0.22 1.85 48.5 0.73
Syzygium
cumini
Duhat 0.18 1.75 42.3 0.70
Albizia
lebbeck
Akleng-parang 0.15 1.65 46.1 0.68
Terminalia
catappa
Talisay 0.20 1.8 47.2 0.71
Table 4. Species-Specific Parameters of the 6 TFTs
The biophysical parametrization revealed distinct
morphological tiers among the six selected Philippine Tree
Functional Types. As shown in Table 3, Pterocarpus indicus
(Narra) and Albizia lebbeck (Akleng-parang) constitute the
upper tier of canopy coverage. They exhibit expansive crown
diameters of 34 meters and 30 meters respectively. This
results in Crown Projection Areas (CPA) that are nearly three
times larger than the median species in the pool. In contrast,
Syzygium cumini (Duhat) and Terminalia catappa (Talisay)
represent the lower tier with crown diameters ranging from 9
to 15 meters. These physical traits dictate the raw cooling
potential of each species before spatial optimization is applied
3.1.2 Species Cooling Output
Figure 7. Cooling Potential by Species Portfolio
The normalized cooling potential analysis integrates both
shading capability and evapotranspiration efficiency into a
single scalar value between 0 and 1. As illustrated in the bar
chart, Narra achieves the highest score of 0.943. This is
followed closely by Akleng-parang at 0.856. This dominance
is primarily driven by the shading component of the cooling
model which is weighted at 70%. While species like Talisay
and Banaba possess comparable Leaf Area Index (LAI)
values which contribute to evapotranspiration, their limited
crown spread restricts their total cooling output. Talisay
scores only 0.392 and Duhat scores the lowest at 0.284. This
disparity creates a significant performance gap. It suggests
that in a spatially constrained optimization problem with a
fixed number of trees, the algorithm will mathematically favor
the larger species unless specific spatial constraints prevent
their placement.
3.1.3 Canopy Competition Behavior
The optimization framework incorporates a Cumulative
Crown Area (CCA) constraints to prevent unrealistic tree
clustering. The code implements a sigmoidal reduction factor
that penalizes cooling returns when canopy density exceeds a
threshold of 1.2. This mechanism models the biological
reality where overlapping leaves provide diminishing returns
for shade and evapotranspiration.
In the absence of this competition factor, the algorithm
would simply stack the highest-performing trees (Narra) on
top of the most vulnerable grid cells. However, the results
show that the ACO avoids placing trees closer than their
combined radii would allow. The algorithm seeks
configurations where the "cooling footprints" of adjacent
trees touch but do not excessively overlap. This behavior
confirms that the model successfully balances the drive for
maximum cooling intensity with the biophysical constraints
of available planting space.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 14

3.1.4 Marginal Contribution of Cooling-Relevant Traits
Figure 8. Marginal Contribution of TFTs
Across all 63 configurations, two species emerged as clear
performance leaders: Akleng-parang (Albizia lebbeck) and
Narra (Pterocarpus indicus). Mono-species Akleng-parang (k=1)
achieved a SECPI of 4.3916, ranking third overall out of 63
configurations, while mono-species Narra scored 4.3856,
ranking 27th. These two species share the largest crown
diameters in the TFT pool (24.0 m and 23.0 m, respectively),
translating to the highest Crown Projection Areas and the
broadest spatial extent of cooling influence under the
Gaussian decay model. The marginal contribution analysis
confirms this quantitatively. Narra and Akleng-parang
exhibited marginal SECPI deltas of approximately 0.6291 and
0.6283, respectively, far exceeding those of the remaining four
species, which clustered near zero or showed slightly negative
contributions.
The four remaining TFTs, namely Talisay (Terminalia catappa),
Banaba (Lagerstroemia speciosa), Kabiki (Mimusops elengi), and
Duhat (Syzygium cumini), occupy a distinctly lower
performance tier. Their crown diameters range from 9.5 m to
12.0 m, roughly half those of Narra and Akleng-parang,
which limits their spatial cooling reach even when their LAI
values are comparable or, in the case of Kabiki, slightly
higher. This result demonstrates that within the current
biophysical proxy, where normalized cooling potential
weights CPA at 0.7 and LAI at 0.3, shading area dominates
the optimizer's selection logic. The high evapotranspiration
capacity of smaller-crowned species does not compensate
sufficiently for their limited spatial footprint under the
Gaussian decay formulation.
3.2 Urban Grid Generation and Equity Zone
Classification
3.2.1 Generated Canonical Grid: Zone Distribution and
Configuration
Figure 9. Canonical Output of Coarse Grid
3.2.2 Equity Weight Spatialization
Figure 10. Equity Weights Spatialization Across Coarse
Grid
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 15

3.3 ACO Search Dynamics and Convergence
3.3.1 Convergence Trajectories Across Runs
Figure 11. ACO Convergence Line Graph
The best-per-iteration SECPI trace fluctuated between
approximately 3.02 and 3.07 across the full run, with no clear
monotonic convergence trend. The global best was reached
early (within the first few iterations) and was never
substantially improved upon in subsequent iterations. This
plateau behavior is consistent with two possible explanations.
First, the solution landscape for this particular grid
configuration may be relatively flat near the optimum,
meaning that many distinct tree placements yield similar
SECPI values. Second, the search space is constrained by the
number of plantable cells available in the CA-generated grid,
which limits the combinatorial diversity that the ants can
explore. With only 5 trees to place and a finite set of plantable
coordinates, the effective search space is small enough that
the ACO encounters near-optimal solutions quickly.
The gap between the best and average SECPI traces is
notable and persistent. The average SECPI per iteration
hovered around 2.99 to 3.02, roughly 0.05 to 0.07 units below
the best. This gap did not close over 30 iterations, indicating
that the pheromone reinforcement mechanism did not fully
drive the ant colony toward consensus on a single dominant
solution. The exploration parameter q0, set at 0.7, allocates
30% of decisions to random exploration, which is sufficient
to maintain diversity but also prevents rapid convergence.
This is by design: a q0 closer to 1.0 would accelerate
convergence but risk premature exploitation of suboptimal
regions, while the current setting preserves the ability to
discover alternative placements throughout the run.
3.3.2 Optimal Placement on Chosen Canonical Grid
Figure 12. Optimal Tree Placements along the Coarse Grid
Figure 13. Optimal Tree Placements along the Fine Grid
The best solution selected 3 Narra trees, 1 Talisay, and 1
Kabiki. The dominance of Narra is expected given its
substantially larger crown projection area (CPA), which gives
it the highest normalized cooling potential among the six
species. The cooling statistics for the best solution show a
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 16

mean intensity of 0.131 across all fine grid cells, a maximum
of 0.809 directly beneath the canopy, and a standard deviation
of 0.160. The fact that the standard deviation exceeds the
mean reflects the highly localized nature of Gaussian cooling
decay with a decay constant of 1.9: most of the grid receives
minimal cooling, while the areas under and immediately
adjacent to tree crowns receive concentrated benefits. This
spatial inequality in cooling distribution is a direct
consequence of the physically grounded decay model and
represents genuine thermal heterogeneity rather than a
modeling artifact.
The placement coordinates show that the optimizer
distributed trees across the grid rather than clustering them.
The five placements span x-coordinates from 25 to 75 meters
and y-coordinates from 5 to 75 meters, covering much of the
100 by 100 meter domain. This spatial dispersion is consistent
with the competition mechanism encoded in the CCA
(Cumulative Crown Area) penalty, which reduces the marginal
cooling benefit of overlapping crowns and incentivizes the
optimizer to spread trees apart for greater spatial coverage.
The inclusion of a smaller-crowned species (Duhat, CD =
11.0m) alongside three large Narra trees (CD = 34.0m)
suggests that the heuristic information and pheromone trails
guided the algorithm toward complementary placements
where a smaller tree could serve a spatial niche that an
additional large tree could not efficiently fill.
3.3.3 Cooling Coverage-Intensity Trade-Off
The application of the Gaussian decay model with a steep
decay coefficient (λ=1.9) resulted in a highly localized cooling
profile. The analysis of the cooling distribution reveals that
the effective cooling benefit is concentrated within a radius of
approximately 1.5 times the crown diameter. Beyond this
range, the cooling benefit becomes negligible.
Consequently, the optimization prioritized "coverage" over
"overlap." Rather than stacking multiple trees to marginally
increase the intensity at a single point, the ACO distributed
the five trees to cover the widest possible surface area of the
Vulnerable zone. This behavior aligns with the principle of
diminishing returns modeled in the biophysical proxy,
confirming that spatial distribution is more valuable than
localized saturation in this specific simulation environment.
3.4 SECPI Framework Outcomes
The ACO optimizer achieved a best SECPI score of 3.067
over 30 iterations with 15 ants per iteration, placing 5 trees
from a pool of 6 candidate Tree Functional Types. The
convergence trajectory reveals several characteristics of the
optimization process that warrant discussion in terms of both
solution quality and algorithmic behavior.
3.4.1 Mean SECPI Across Subset Sizes
Figure 14. Ef ect of Species Diversity on SECPI
The figure presents the mean SECPI computed across all
combinations at each subset size k, with error bars indicating
variability within each group. Mean SECPI rises from k=1
(approximately 2.990) through k=4 (approximately 3.017),
suggesting that expanding the available palette modestly
improves average performance by increasing the probability
that the ACO has access to at least one high-performing
species. However, the trend reverses at k=5, where mean
SECPI drops to approximately 2.999 before recovering
slightly at k=6 (approximately 3.009). This non-monotonic
pattern reflects the compositional structure of the subsets
rather than a true diversity benefit. At k=1, the mean is
dragged down by the four small-crowned mono-species
configurations (Talisay, Banaba, Kabiki, Duhat), all of which
score below 3.11. As k increases, a growing proportion of
subsets contain at least one of the two dominant species,
raising the group mean. The dip at k=5 likely arises because
all five-species subsets exclude exactly one species, and those
subsets missing Narra or Akleng-parang pull the mean
downward. The overall range of mean SECPI across all k
values spans only about 0.027, reinforcing that subset size
alone is a weak predictor of performance compared to
whether the subset contains a large-crowned species.
3.4.2 The Limited Benefit of Functional Diversity
Beyond the mean trends, individual configuration rankings
confirm that functional diversity offers minimal and
inconsistent gains over well-chosen mono-species
configurations. The top-ranked configuration was the full
6-species palette (k=6, SECPI = 4.3930), but the ACO
allocated trees to only Narra and Talisay, using just 2 of the 6
available species. The second-ranked configuration used a
4-species palette yet placed all five trees as Akleng-parang
alone, scoring 4.3924. The third-ranked was mono-species
Akleng-parang at 4.3916. The spread between the best
configuration (4.3930) and the best mono-species result
(4.3916) is only 0.0014, representing a difference of
approximately 0.03% in SECPI. This margin falls well within
the stochastic variation inherent to the ACO metaheuristic
across independent runs.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 17

Among the top 10 configurations, the ACO used all available
species in only 3 out of 10 cases. Several configurations with
k=4 or k=5 saw the optimizer converge on just one or two
species, predominantly Akleng-parang and Narra. This
underutilization is consistent with the non-submodular
structure of the cooling objective: when canopies from
large-crowned trees overlap at the fine-grid level, the
CCA-based competition factor penalizes additional trees in
close proximity. The optimizer thus favors placing fewer
species with large crowns at well-separated positions rather
than mixing in smaller-crowned species that would contribute
less cooling per unit of grid space occupied.
3.4.3 The Performance Cliff and the Role of
Small-Crowned Species
Both the ranked configurations and the mean SECPI trend
point to a sharp discontinuity between configurations that
include at least one large-crowned species and those that do
not. In the ranked data, the transition occurs between rank 48
(Narra + Kabiki + Duhat, SECPI = 4.3651) and rank 49
(Banaba + Kabiki + Duhat, SECPI = 3.1336), a drop of
approximately 1.23 SECPI units or 28%. All configurations
below this cliff exclude both Narra and Akleng-parang,
relying entirely on species with crown diameters of 12 m or
less.
The Gaussian decay function, which attenuates cooling is
highly sensitive to crown diameter since it directly controls
the denominator of the decay exponent. Halving the crown
diameter from 24 m to 12 m reduces the effective cooling
radius substantially, meaning each tree influences a much
smaller portion of the fine grid. The result is that five
small-crowned trees cannot collectively match the spatial
coverage achievable by configurations that include even a
single large-crowned species.
This does not mean smaller species are without value. Within
the below-cliff tier, species differences still matter.
Mono-species Talisay (SECPI = 3.1065) outperforms
mono-species Duhat (3.0396) despite comparable LAI,
because Talisay's slightly larger crown diameter (12.0 m vs. 9.5
m) provides a broader decay radius. Similarly, the
three-species combination of Banaba + Kabiki + Duhat
(SECPI = 3.1336) marginally outperforms any of its
constituent mono-species configurations, indicating that
within the constrained pool of smaller TFTs, functional
mixing does provide a slight additive benefit by distributing
cooling across complementary spatial positions. These
within-tier differences suggest that if site constraints preclude
large-crowned species due to infrastructure clearance
requirements or root zone limitations, the framework can still
identify the best-performing alternatives from the smaller
TFT pool.
3.4.4 Cross-Scenario Validation
The framework's central claim is that embedding spatial
equity into the optimization objective produces meaningfully
different, and more just, cooling outcomes than
efficiency-only optimization. To test this, a controlled
comparison was conducted between the full SECPI objective
with vulnerability weighting active (WITH VULN) and a
benchmark scenario where vulnerability zones were
reclassified as Prohibited cells and all equity weights were set
to unity (WITHOUT VULN). Both scenarios used identical
CA-generated urban morphologies, the same ACO
hyperparameters, and the same five-tree budget, isolating the
equity mechanism as the sole experimental variable. The
validation is organized around three dimensions: cooling
equity, cooling efficiency, and thermal distribution.
The validation phase necessitated a rigorous comparison
between the equity-weighted optimization
(WITH_VULNERABLE) and a baseline efficiency-only
scenario (WITHOUT_VULNERABLE). The quantitative
results confirm that the SECPI framework successfully
redirects the optimization search process. In the baseline
scenario, the algorithm defaulted to a monoculture strategy,
selecting five Pterocarpus indicus (Narra) trees to maximize
aggregate cooling coverage. This configuration achieved a
mean cooling intensity of 0.192 but resulted in a low SECPI
score of 1.5, as the cooling was distributed without regard for
social priority.
In contrast, the equity-weighted scenario produced a
significantly higher mean SECPI of 3.08, with the best
configuration reaching 3.19. The species composition shifted
from a monoculture to a functional mix, utilizing three Narra
trees, one Terminalia catappa (Talisay), and one Lagerstroemia
speciosa (Banaba). The spatial arrangement also adapted, with
placements such as (45.0, 85.0) and (75.0, 95.0) clustering
around specific high-priority zones. This demonstrates that
the inclusion of vulnerability weights forces the algorithm to
sacrifice the raw coverage of five giant trees in favor of a
mixed-species arrangement that fits biophysically into the
constrained spaces near vulnerable populations.
Cooling Equity Validation
Figure 15. Zonal Cooling Ef iciency Analysis
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 18

Figure 16. Equity-Weighted Cooling Contribution
The primary test of the equity mechanism is whether the
SECPI-ON scenario successfully redirects cooling benefits
toward vulnerable populations. The Automated Cooling
Interpretation Report provides a direct answer. Under the
optimized WITH VULN configuration, vulnerable zones
received an average cooling intensity of 0.1584, compared to a
global average of 0.1305, yielding an Equity Ratio of
approximately 1.21. The report classified this outcome as
"[SUCCESS] HIGH EQUITY," confirming that the
algorithm prioritized vulnerable zones above the global
baseline. Available zones received an average intensity of
0.1162, and building zones received 0.0807, establishing a
clear spatial gradient where cooling benefits decrease as
distance from vulnerable areas and planting sites increases.
The zonal cooling efficiency chart visualizes this hierarchy
directly. The vulnerable zone bar (0.16) exceeds the global bar
(0.13) by roughly 23%, while the available zone (0.12) and
building zone (0.08) fall progressively below the global mean.
This ordering is not a coincidence of grid geometry. In the
WITHOUT VULN scenario, vulnerable zones are reclassified
as prohibited, so the optimizer has no mechanism to
distinguish socially sensitive areas from any other part of the
grid. The equity weighting in SECPI functions as a spatially
heterogeneous reward signal: fine-grid cells within or near
vulnerable zones carry weights of 2.0 (within 10 m) or 1.5
(within 20 m), compared to a baseline weight of 1.0
elsewhere. This amplification means that a unit of cooling
delivered to a vulnerable cell contributes roughly twice as
much to the SECPI score as the same unit delivered to a
non-vulnerable cell, creating a direct incentive for the ACO to
place trees where their decay envelopes overlap with
high-weight regions.
The combinatorial results reinforce this finding at scale. In
the WITH VULN dataset, SECPI scores span a range from
3.023 to 4.393, a spread of 1.37 units across the 63
configurations. In the WITHOUT VULN dataset, scores
compress into two narrow bands centered at approximately
1.50 and 1.75, with the entire top 48 configurations falling
within a range of only 0.0002. This compression indicates
that without equity weighting, the optimizer lacks a spatially
differentiated signal and converges on nearly identical
aggregate cooling profiles regardless of species composition,
provided at least one large-crowned species is available. The
equity mechanism thus serves a dual function: it distributes
cooling toward vulnerable populations as intended, and it
simultaneously enriches the fitness landscape, enabling the
optimizer to discriminate among configurations that would
otherwise appear equivalent.
Cooling Efficiency Validation
A reasonable concern with equity-driven optimization is that
prioritizing vulnerable zones might reduce overall cooling
performance. The data show this concern is largely
unfounded within the current framework, though the
relationship between equity and efficiency is not
straightforward.
Figure 17. Sub-Optimal Solution with Vulnerability Cells
(Coarse Grid)
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 19

Figure 18. Sub-Optimal Solution with Vulnerability Cells
(Fine Grid)
Figure 19. Sub-Optimal Solution without Vulnerability Cells
(Coarse Grid)
Figure 20. Sub-Optimal Solution with Vulnerability Cells
(Fine Grid)
A direct trade-off between equity and raw thermal efficiency
was observed. The "WITHOUT_VULNERABLE" scenario
achieved a global maximum cooling intensity of 1.15 °C and a
mean intensity of 0.19 °C. Under the
"WITH_VULNERABLE" scenario, these values decreased to
a maximum of 0.80 °C and a mean of 0.11 °C. This reduction
of approximately 42% in mean cooling intensity represents
the "cost" of equity. The algorithm purposely avoided placing
the largest trees in open, low-priority areas where they could
achieve maximum crown spread. Instead, it selected smaller
trees like Banaba and positioned larger trees in tighter,
high-priority zones where canopy overlap penalties might
limit their total cooling output. This confirms that the SECPI
objective function successfully prioritizes the distribution of
cooling benefits over the sheer magnitude of temperature
reduction.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 20

Thermal Distribution Comparison
Figure 21. Cooling Distribution of Narra Tree
Figure 22. Cooling Decay Profile of Narra Tree
Figure 23. Cooling Distribution of Talisay Tree
Figure 24. Cooling Decay Profile of Talisay Tree
Figure 25. Cooling Distribution of Akleng-Parang Tree
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 21

Figure 26. Cooling Decay Profile of Akleng-Parang Tree
Figure 27. Cooling Distribution of Duhat Tree
Figure 28. Cooling Decay Profile of Duhat Tree
Figure 29. Cooling Distribution of Kabiki Tree
Figure 30. Cooling Decay Profile of Kabiki Tree
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 22

Figure 31. Cooling Distribution of Banaba Tree
Figure 32. Cooling Decay Profile of Banaba Tree
The spatial pattern of cooling, beyond its zonal averages,
reveals how the equity mechanism reshapes the thermal
landscape at the fine-grid level. The single-tree radial decay
profile for Narra (Figure [Single Tree Radial Decay: Narra])
provides the baseline for interpreting multi-tree
configurations. The left panel shows a smooth, radially
symmetric cooling distribution centered at the tree position
(50 m, 50 m), with peak intensity near 0.85 that decays
concentrically outward. The right panel traces this decay as a
function of distance: cooling intensity remains above 0.6
within the crown radius (11.5 m, marked by the dashed red
line), drops below 0.2 at approximately 25 m, and approaches
zero beyond 40 m. This profile confirms that the Gaussian
decay parameterization (λ=1.9, CD=23.0 m for Narra)
produces a cooling footprint that extends well beyond the
physical crown boundary, consistent with the empirical
finding that tree cooling effects propagate 2 to 3 crown radii
into the surrounding environment through advective and
radiative processes.
When five trees are placed under the WITH VULN objective,
their individual decay envelopes are spatially arranged to
maximize overlap with vulnerable zones. The JSON
placement data illustrate this. In the 1-species WITH VULN
configuration, trees are positioned at coordinates including
(25, 95), (25, 45), and (45, 45), clustering toward grid regions
where vulnerability weights are elevated. In the corresponding
WITHOUT VULN configuration, trees appear at (25, 15),
(15, 15), and (25, 55), reflecting a distribution driven purely by
maximizing coverage of available cells without spatial
preference. The WITH VULN placements produce a thermal
distribution where the highest cooling intensities coincide
with the most socially sensitive areas, whereas the
WITHOUT VULN placements distribute cooling more
uniformly but without targeting.
The coverage metric from the zonal analysis quantifies this
spatial targeting. Under WITH VULN, 4.80% of vulnerable
fine-grid cells received cooling intensity above 0.5, which
represents direct canopy-level or near-canopy cooling. While
this percentage may appear modest, it must be interpreted in
the context of the five-tree budget covering a 100 x 100 m
grid. Each Narra tree's high-intensity zone (above 0.5)
extends roughly 15 m from its trunk, covering approximately
707 m² per tree, or 3,535 m² for five trees. Against a total grid
area of 10,000 m², this corresponds to theoretical maximum
high-intensity coverage of about 35%, but only a fraction of
the grid is classified as vulnerable. The 4.80% figure thus
reflects the proportion of vulnerable cells specifically
receiving strong cooling, confirming that the optimizer
successfully positioned trees to deliver their most intense
cooling to the areas that need it most, rather than distributing
that intensity evenly across the entire grid.
3.5 Sensitivity Analysis
A one-at-a-time (OAT) parameter sensitivity analysis was
conducted to identify which input parameters most strongly
influence SECPI outcomes and to assess the robustness of
the optimization framework to uncertainty in its biophysical
inputs.
3.5.1 Parameter-Specific Level Sensitivity
The analysis swept 40 parameters across four categories:
species morphological traits (crown diameter, height), species
allometric constants (l0, l1, h0, h1), cooling model parameters
(decay lambda, CCA threshold, competition steepness), and
the shade-evapotranspiration weighting ratio. Each parameter
was evaluated at its low and high bounds while all others were
held at baseline values, and the resulting SECPI was averaged
over three independent ACO runs per configuration to
reduce stochastic noise. The baseline SECPI was 3.0576.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 23

Figure 33. Sensitivity Index Tornado Diagram
The sensitivity index (SI), defined as the normalized absolute
effect size ( ), identifies a single parameter
|𝑆𝐸𝐶𝑃𝐼
ℎ𝑖𝑔ℎ−𝑆𝐸𝐶𝑃𝐼𝑙𝑜𝑤
|
𝑆𝐸𝐶𝑃𝐼
𝑏𝑎𝑠𝑒𝑙𝑖𝑛𝑒
as overwhelmingly dominant: Narra's crown diameter. With
an SI of 0.4435, it exceeds the second-ranked parameter
(Talisay.h1, SI = 0.0045) by nearly two orders of magnitude.
Sweeping Narra's crown diameter from its manuscript low of
12.0 m to its high of 34.0 m produced SECPI values of 3.024
and 4.380, respectively, an absolute effect of 1.356 SECPI
units. This finding is consistent with the combinatorial results
reported in Section 3.2, which identified a sharp performance
cliff between configurations containing large-crowned species
and those without. When Narra's crown diameter is set to its
lower bound (12.0 m), it effectively loses its dominance over
smaller-crowned species, collapsing the optimizer into the
lower performance tier. When set to its upper bound (34.0
m), the expanded decay envelope amplifies both direct
cooling coverage and the vulnerability-weighted reward,
producing SECPI scores comparable to the top-ranked
combinatorial configurations.
All remaining 39 parameters exhibit sensitivity indices below
0.005, indicating that the framework is robust to moderate
uncertainty in these inputs. The second through tenth most
sensitive parameters, in descending order, are Talisay.h1 (SI =
0.0045), Talisay crown diameter (0.0043), Akleng-parang.l0
(0.0037), Duhat crown diameter (0.0033), Banaba.l0 (0.0032),
CCA threshold (0.0032), Narra.h1 (0.0030), Narra.l0 (0.0030),
and Duhat.h0 (0.0028). These parameters produce absolute
SECPI effects ranging from 0.009 to 0.014, which are small
relative to the baseline but not negligible. Their presence in
the top ten confirms that the model responds to both
morphological inputs (crown dimensions that govern the
Gaussian decay denominator) and allometric constants (which
determine LAI through the l0⋅DBHl1 relationship), though
the response magnitudes are comparable in this secondary
tier.
3.4.2 Category-Level Sensitivity
Figure 34. Parameter Category Sensitivity Summary
Aggregating sensitivity indices by category reveals a clear
hierarchy. Species Morphology dominates with a mean SI of
1.3068, driven almost entirely by the Narra crown diameter
outlier. Removing that single parameter would reduce the
category mean to approximately 0.002, placing it on par with
the other categories. Species Allometry parameters rank
second with a mean SI of 0.1857, followed by Species
Allometry (0.0727) and Weighting (0.0236).
The relatively low sensitivity of the Cooling Model category is
noteworthy. The CCA threshold (SI = 0.0032) and
competition steepness (SI = 0.0021) govern the sigmoidal
competition factor that penalizes canopy overlap, yet their
influence on SECPI is modest. This suggests that the
competition mechanism, while structurally important for
preventing unrealistic canopy stacking, does not substantially
alter the optimizer's preferred spatial configurations within
the tested range. Similarly, the decay lambda parameter (SI =
0.0015) has limited impact, indicating that the Gaussian decay
rate is not a critical source of model uncertainty given the
current grid resolution and tree spacing.
The shade-evapotranspiration weight ratio (shade_weight, SI
= 0.0017) exhibited the lowest sensitivity of any category.
Sweeping this parameter from 0.5 to 0.9, which shifts the
normalized cooling potential from a balanced CPA-LAI
formulation to a strongly shade-dominated one, produced a
SECPI difference of only 0.005. This insensitivity arises
because the two dominant species (Narra and Akleng-parang)
rank highest on both CPA and LAI dimensions, so altering
the relative weight between these components does not
change the optimizer's species preference or spatial strategy.
The weighting ratio would become more consequential in
scenarios where the species pool contained trees with high
LAI but small crowns, or vice versa, creating a genuine
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 24

trade-off between shading and evapotranspiration that the
current TFT set does not strongly exhibit.
3.4.3 Implications for Model Robustness and Data
Collection
The concentration of sensitivity in a single morphological
parameter carries two practical implications. First, the
framework's outputs are robust to the typical uncertainties
associated with allometric estimation in tropical forestry. The
allometric constants sourced from literature (l0, l1, h0, h1)
were swept across a 15% uncertainty band, and none
produced SECPI effects exceeding 0.014. This means that
even if the species-specific constants carry estimation errors
of this magnitude, the optimization recommendations,
particularly species ranking and spatial placement logic,
remain stable.
Second, the outsized influence of crown diameter identifies it
as the single most critical field measurement for future
empirical calibration. The manuscript's reported range for
Narra crown diameter (12 to 34 m) spans nearly a three-fold
difference, reflecting the species' high morphological
plasticity across growth stages and site conditions. Narrowing
this range through site-specific crown surveys would
disproportionately reduce the uncertainty envelope around
SECPI predictions. For planning applications, this suggests
that investing in crown diameter measurements for the
dominant candidate species yields a far greater return in
model precision than refining any other input parameter.
Height measurements, by contrast, showed minimal
sensitivity across all species (the highest being Duhat height at
SI = 0.0027), confirming that the allometric pathway from
height to DBH to LAI introduces sufficient buffering to
dampen the effect of height uncertainty on final cooling
estimates.
