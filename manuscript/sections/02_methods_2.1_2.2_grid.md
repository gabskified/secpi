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

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 385–878).
> Content: METHODOLOGY preamble, §2.1 Study Design, §2.2 Modern Parameterization (2.2.1–2.2.4)
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

METHODOLOGY
Research Design
This study followed an integrated optimization framework for
a multiple case validation of different Philippine TFT
combinations and arrangements, integrating a cellular
automata algorithm for generating different maps used for
optimization. Informed by prior research on urban heat
mitigation and optimization models (Shaamala et al., 2025;
Morakinyo & Lam, 2016), the framework was adapted based
on morphological constraints and equity priorities of a
tropical Philippine urban context. The process involved
several key stages: model parameterization, urban grid
generation, optimization of cooling proxy, analysis of
equity-weighted SECPI, and validation of results. Each step
was designed to address the three complementary strands of
the theoretical framework: sustainability, complexity, and
resilience thinking.
Notably, the development process was not entirely linear.
Decisions regarding species selection, grid resolution, cooling
function calibration, and equity-weighting were revisited
iteratively based on preliminary outputs, data availability, and
emerging insights into the model’s behavior. This flexible,
adaptive approach allowed the framework to be generalizable
across urban contexts, with the research design embracing the
principle of "appropriate complexity", developing methods
sophisticated enough to capture essential dynamics while
remaining computationally feasible and interpretable for
planning applications.
This research is structured around a novel integrative
paradigm for computational urban planning, termed the
Equitable Integer Lattice Optimization Paradigm. The core
problem it addresses is the optimal and just spatial
allocation of discrete green infrastructure resources within
an urban space. Specifically, it investigates the placement of
a finite number of trees to maximize cooling benefits. This
challenge is formalized as a constrained, non-submodular
set function maximization problem defined on a finite
two-dimensional integer lattice, a mathematical structure
that rigorously represents discrete urban space (National
Science Foundation, n.d.; École Polytechnique Fédérale de
Lausanne, n.d.). The critical knowledge gap this paradigm
confronts is the disconnect between traditional
efficiency-focused optimization, which often assumes
diminishing returns (submodularity) for tractability, and the
imperative for distributive justice in urban climate
adaptation. Existing models frequently treat equity as a
secondary constraint or a post-hoc evaluation, rather than
the foundational driver of the optimization objective itself.
Figure 3. The Equitable Integer Lattice Optimization
Paradigm for Computational Analysis on
Non-Submodular Spatial Resource Allocation
The paradigm’s theoretical foundation rests on three
interconnected pillars. First, the formalism of the integer
lattice provides the discrete mathematical backbone,
translating the continuous urban landscape into a
computationally tractable field of candidate sites while
rooting the analysis in combinatorial optimization theory.
Second, it directly engages with the theory of
non-submodular function optimization, acknowledging that
the cooling interactions between trees, featuring synergistic
overlaps and competitive crowding, create marginal gains
that depend profoundly on existing configurations (Bian et
al., 2018). Third, it operationalizes spatial equity by deriving
a weighting function from social vulnerability metrics
(Shaamala et al., 2024), thereby embedding an ethical
framework directly into the core objective function. The
computational-mathematical nexus chosen to navigate this
complex problem is the Ant Colony Optimization (ACO),
hybridized with a procedural generation model. ACO is
uniquely suited for this combinatorial landscape as it
requires no gradient information, excels on discrete graphs,
and uses stigmergic learning to explore the solution space
dynamically.
The methodological pipeline executes this paradigm
through a sequence of structured stages. The initial stage
involves a dual-grid discretization: a coarse integer lattice
defines permissible planting sites, while a fine-resolution
lattice enables the continuous evaluation of the resulting
cooling field. This spatial model is populated using a
Cellular Automata algorithm, which synthesizes
morphologically realistic urban patterns complete with
prohibited, available, and vulnerable cell classifications
based on real urban land-use ratios. The core algorithmic
stage employs a bespoke ACO framework where artificial
ants construct candidate tree configurations. The quality of
each configuration is evaluated by the Synergistic and
Equitable Cooling Performance Index, a novel objective
function that integrates a biophysical cooling proxy, a
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 5

non-linear competition factor, and an equity-weighted
benefit classification system. Implementation leverages
parallel computing to manage the computational load of
evaluating myriad configurations across the fine-scale grid.
A rigorous validation and verification protocol is integral to
the paradigm. Verification ensures mathematical and
algorithmic correctness through unit tests against simplified
analytic cases. The primary validation, however, is designed
to empirically demonstrate the paradigm’s core
sociotechnical contribution. This is achieved through a
controlled comparative case study analysis between an
equity-driven optimization and an efficiency-only
benchmark. A successful validation will quantitatively show
that the full paradigm meaningfully redirects cooling
resources toward predefined high-vulnerability zones, even
at the cost of marginal reductions in aggregate cooling
output. Furthermore, the paradigm’s robustness is tested
across multiple generated urban morphologies to ensure its
conclusions are not artifacts (or errors) of a single spatial
layout. Uncertainty from parameter estimation, such as in
species allometrics, is propagated through the model to
distinguish stable algorithmic insights from parametric
noise. Lastly, A controlled analysis will be conducted on
fixed urban morphology, varying only the available species
portfolio of mono-species, up to multi-species, to check if
the model leverages species functional diversity to create
higher-performing or more resilient cooling solutions.
The expected outcomes of this paradigm are both
theoretical and applied. Tangible deliverables include an
open-source computational solver for equitable spatial
resource allocation and a comparative dataset of optimized
plans for canonical urban forms. Scientifically, the paradigm
aims to advance the integration of justice-oriented
objectives into discrete optimization frameworks, bridging
computational mathematics, urban ecology, and spatial
planning theory. Its transdisciplinary impact lies in
providing a transferable methodology for a host of spatial
allocation problems where equity is paramount, from public
service deployment to climate resilience infrastructure.
Finally, the paradigm is conducted with explicit ethical and
sustainable research considerations. It proactively encodes
distributive justice into its objective function, commits to
full open-source reproducibility to empower
under-resourced planners, and justifies the computational
energy expenditure by its ultimate goal of fostering
low-carbon, thermally just, and climate-resilient urban
communities.
2.1 Study Design
This study employs a computational, mathematical modelling
research design to develop and test a generalized framework
for optimizing urban tree placement. The urban tree
placement problem is formalized as a constrained
optimization on a two-dimensional integer lattice (ℤ²), where
each Available grid cell represents a discrete point. Following
the reasoning of Kunhle et al., the cooling function is
expected to be non-submodular due to synergistic and
competitive interactions between tree canopies. For such
complex, non-submodular optimization problems on discrete
structures, exact solutions are often computationally
prohibitive. Therefore, Ant Colony Optimization (ACO)
metaheuristic, a proven strategy for navigating large
combinatorial search spaces, was applied to identify
high-performing configurations.
2.2 Modern Parameterization
Species selection prioritized rampant, culturally relevant
Philippine trees with diverse crown morphologies to capture a
range of cooling mechanisms. Data collection focused
exclusively on morphological traits directly influencing
shading potential, specifically mature crown diameter and tree
height. These parameters were sourced from Philippine
forestry databases (DENR-ERDB; UPLB-CFNR) and
peer-reviewed literature on tropical urban forestry (Abino et
al., 2014).
2.2.1 Biophysical Inputs of Tree Functional Types
(TFTs)
The six selected Philippine Tree Functional Types (TFTs),
Terminalia catappa (Talisay), Pterocarpus indicus (Narra),
Lagerstroemia speciosa (Banaba), Syzygium cumini (Duhat),
Albizia lebbeck (Akleng-parang), and Mimusops elengi
(Kabiki), were chosen to provide a comprehensive
biophysical representation for mapping cooling gradient
decay. This group captures the full spectrum of cooling
mechanisms essential for urban environments being the
evergreen tree types: Narra, with its wide spreading crown
and moderate-to-fast growth, it is included to model the
maximum potential for extensive shade cooling across large
areas; Kabiki, Talisay, and Banaba represent common,
multifunctional species with slow-to-moderate growth, broad
and dense canopies, and adaptive urban traits that provide
high shade and evapotranspiration benefits; and Duhat and
Akleng-parang is critical for its very dense foliage, urban
adaptability and moderate-to-fast growth, ensuring the model
incorporates high Leaf Area Index (LAI) species that
prioritize cooling via evapotranspiration. By modeling these
diverse canopy structures and cooling potentials (from the
expansive Narra to the dense Duhat), the study can accurately
map how cooling effects dissipate over space, yielding
relevant insights for effective urban greening strategies.
2.2.2 Cellular Automata and Procedural Generation of
Land Use
Recent studies on above-ground biomass (AGB) estimation
in tropical forests demonstrate that plot size has a significant
influence on reducing relative estimation errors. Using the
PTM-2 model together with a plot-level H–D model,
researchers found that small plots measuring 10 × 10 m
produce large errors of about 50%, while increasing the plot
size to 50 × 50 m reduces errors to around 10%. This
reduction continues, with a 100 × 100 m plot decreasing the
error to approximately 5%, beyond which further expansion
yields minimal improvement. Consequently, these studies
recommend 100 × 100 m as the minimum reliable reference
plot size for AGB estimation.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 6

Figure 4. Theoretical study area using a discrete 100 m x
100 m grid.
To generate the coarse optimization grid (GC) with realistic
and structurally coherent arrangements of P, V, and A cells,
the Cellular Automata (CA) model was employed. CA is a
well-established, grid-based dynamic system ideal for
simulating urban growth patterns through simple local
rules, making it suitable for synthesizing plausible urban
morphologies for computational testing. The
implementation is a modified binary urban CA model
designed for initial spatial configuration rather than
temporal growth simulation (Chakraborty et al., 2022).
Figure 5. Flowchart of Cellular Automata (CA) for
Generation of Coarse Grid Cell States
The procedural generation of synthetic urban morphologies
used to test the optimization algorithm is implemented via a
Cellular Automata (CA) model. The approach is grounded in
the formal CA framework for land-use dynamics, which
conceptualizes urban growth as transitions between discrete
cell states on a lattice (Almeida et al., 2002). In this
formalism, a system of N cells can occupy one of M mutually
exclusive states. The general formula is as follows:
𝑁𝑖
𝑘
(𝑡) = 1, 𝑁𝑖
𝑙
(𝑡) = 0 𝑓𝑜𝑟 𝑘 ≠ 𝑙, 𝑙 = 1, 2, 3,..., 𝑀,
𝑘
∑ 𝑁𝑖
𝑘
(𝑡) = 1
For cell i at time t, this is defined as: where k and l represent
distinct land-use states. The aggregate dynamics are then
driven by transition rules, which can be analyzed as a
first-order Markov process (Almeida et al., 2002, Eqs. 11-13).
The paper adapts this framework by defining three core states
for each cell: Prohibited (P), Vulnerable (V), and Available
(A).
Model Setup and Initialization
The process begins with an empty m x n coarse grid (GC).
An initial seed density (pinit), typically 5-10%, is used to
randomly set a corresponding proportion of cells to the
Prohibited (P) state. These seeds represent the initial nuclei
of urban development.
Transition Rules
The model iterates for a predefined number of generations (
𝑡 ). During each iteration, the state of every cell is 𝑚𝑎𝑥
reevaluated based on its current state and the configuration of
cells within its Moore neighborhood (the eight surrounding
cells). The transition rule is probabilistic and captures the
positive feedback dynamics inherent in urban frontier
expansion, wherein existing development attracts further
development (Almeida et al., 2002).
To model this aggregation process, particularly the growth of
urban clusters at their periphery, the paper implements an
expander heuristic adapted from the foundational cellular
automata (CA) model of Almeida et al. (2002). This heuristic
is explicitly designed to generate the clustered, contiguous
urban forms characteristic of organic growth by weighting
transition probabilities according to the local density of the
target land use. The transition probability for a
non-prohibited cell i from k to l to convert to the Prohibited
(P) state j is given by:
𝑝
𝑖
𝑘𝑙
(𝑡 + 1) = γ[
𝑗∈Ω𝑖
∑ 𝑁𝑗
𝑙
(𝑡)
8
]𝑝
𝑖
𝑘𝑙
(𝑡 + 1)
where 𝑁 denotes the number of neighboring cells within
𝑗
𝑙
(𝑡)
the eight-cell Moore neighborhood Ω already in the P state,
𝑖
and the ratio provides a normalized measure of
neighborhood saturation, representing the density of existing
development surrounding cell i, while γ is a normalization
coefficient ensuring that the resulting probabilities remain
within the unit interval.
Generating Morphological Archetypes
By tuning the parameters pinit and γ, the CA model can
generate distinct coarse-grid archetypes for robustness
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 7

testing:
- Organic/Clustered Morphology: Achieved by
applying a low activation threshold and moderate
neighborhood weighting within the expander
heuristic, producing tight, irregular clusters of P cells
akin to historical urban cores.
- Sparse/Suburban Morphology: Achieved by
applying a high activation threshold and weak
neighborhood influence within the expander
heuristic, resulting in dispersed, isolated P cells with
large interstitial A zones.
- Linear/Corridor Morphology: Achieved by biasing
the initial seed placement or transition rules along a
vector, simulating development along a major
transport route.
Post-Processing for V and A Cells:
Once the CA simulation stabilizes, producing a stable
configuration of P cells, the Vulnerable (V) zones are
algorithmically assigned. Points representing key social
infrastructure are placed either at the centroid of large P
clusters or at strategic junctions between them. All coarse
cells within a specified buffer distance of these points are
then classified as V, overriding their previous state. Finally, all
cells not classified as P or V are definitively assigned as
Available (A). This final GC grid serves as the landscape on
which the ACO algorithm performs the tree placement
optimization.
2.2.3 Equity and Policy Inputs
The integration of equity considerations into the optimization
framework addresses uniform distribution of urban cooling
benefits, prioritizing populations that are thermally and
socially vulnerable. In this study, equity refers to the
proportional allocation of cooling resources based on
vulnerability (cooling intensity) rather than uniform spatial
distribution. This approach aligns with resilience thinking,
where climate adaptation strategies are designed to protect
populations most at risk of heat-related stress. To ensure
clarity in the interpretation of the optimization framework
and results, several key terms are defined as follows:
Social vulnerability refers to the degree to which a population
is susceptible to harm from heat exposure due to
demographic, socioeconomic, or infrastructural conditions. In
urban Philippine contexts, this often includes children, elderly
populations, patients near health centers, and residents in
high-density housing areas.
Equity weight is a numerical multiplier assigned to specific
spatial zones to reflect their relative priority in the
optimization process. Higher weights increase the
contribution of cooling improvements in those zones to the
SECPI objective function.
Cooling benefit class refers to the categorization of grid cells
based on relative cooling performance using percentile
thresholds derived from the distribution of total cooling
values in a given scenario.
Percentile-based classification is a self-normalizing method
that divides cooling values into quartiles (25th, 50th, 75th
percentiles) to ensure fair comparison across scenarios with
different absolute cooling magnitudes.
The table below presents the ordinal classification system
used to categorize cooling intensity across the fine
evaluation grid. The continuous cooling output is divided
into four percentile-based benefit classes.
Percentile Class
0-25th Class 1: Minimal Benefit
26-50th Class 2: Moderate Benefit
51st-75th Class 3: Substantial Benefit
76th-100th Class 4: High Benefit
Table 1. Relative Cooling Ef ectiveness Percentiles
This classification ensures that performance assessment is
scenario-relative rather than absolute. Instead of relying on
fixed temperature thresholds, cooling performance is
evaluated based on how much area shifts into
higher-performing quartiles compared to a baseline
configuration. This method enables meaningful comparison
between randomized, clustered, and optimized planting
layouts while preserving distributional sensitivity.
The linear weighting structure (𝑊 = k) assigns greater
𝑘
importance to improvements in higher cooling classes,
reinforcing the objective of maximizing not only total cooling
but also high-intensity cooling zones.
Table 2. Social Vulnerability Weight Table
Spatial equity was operationalized by assigning numerical
weights to different urban zone types based on their social
sensitivity to heat stress.
Schools and health centers concentrate physiologically and
socially vulnerable sub-populations including children, the
elderly, and patients, who exhibit the greatest susceptibility
to heat-related illness and mortality. A doubled weight
reflects the heightened public health consequence of
thermal discomfort in these facilities, where heat stress can
directly impair service delivery and harm high-risk
occupants (Wolf & McGregor, 2013).
High-density residential zones combine elevated per-area
population exposure with prolonged dwell time, meaning
residents, particularly low-income households lacking
mechanical cooling, bear a disproportionate cumulative
heat burden. The weight above standard reflects the dual
effect of both higher population concentration and lower
adaptive capacity at the household level. (Norton et al.,
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 8
Zone Type Equity Weight
Near schools/health centers 2.0
High-density residential 1.5
Commercial/industrial 1.0
Parks/empty lots 0.5

2015).
Commercial and industrial areas serve as the baseline
reference weight given their role as primary economic
zones with significant impervious surface coverage and
anthropogenic heat generation. While daytime occupational
heat exposure is a concern, the absence of overnight
residential dwell time limits cumulative individual exposure
relative to residential and institutional zones (Estoque et al.,
2017).
Parks and vacant lots function as net cooling sources
through evapotranspiration, shading, and reduced
impervious surface fraction, thereby contributing positively
to the urban thermal environment rather than intensifying
heat stress. A reduced weight reflects their inherently lower
cooling demand and the principle that equity-based
prioritization should redirect resources toward thermally
underserved zones with active heat burdens (Norton et al.,
2015; Estoque et al., 2017).
2.2.4 Optimization Inputs and Integer Lattice
Formalization
The urban space is represented at two resolutions: coarse
optimization grid and a fine evaluation grid. The coarse
optimization grid is a lower-resolution grid of 10 x 10 cells,
where each cell measures 10 m² and represents a potential
planting location. A tree, if placed, is positioned at the cell’s
center. The discretization transforms the infinite continuous
search space into a finite integer lattice, formally defining the
optimization problem as a binary integer program: maximize
the objective function by selecting a subset of lattice points
for planting. The fine evaluation grid is a higher-resolution
grid of 10 x 10 cells, with a resolution of 10 m² per cell, used
to evaluate the cooling effects of a blanking configuration.
The cooling contribution of a tree placed at a Coarse-Grid
cell is calculated for every point on this fine-grid, enabling a
smooth, detailed visualization of the cooling field and a
precise calculation of area-based metrics.
The foundation of the discrete, grid-based optimization is the
classification of the integer lattice into three mutually
exclusive cell states: Vulnerable (V), Prohibited (P), and
Available (A). The ratios of these states are not arbitrary but
are derived to construct a synthetic yet realistic urban testbed
that reflects the morphological constraints of a dense, tropical
city like Caloocan. This approach ensures the model's
solutions are relevant to actual planting constraints, such as
building footprints, infrastructure, and socially sensitive
zones.
Prohibited Cells (P)
These cells represent impervious surfaces and permanent
infrastructure where tree planting is physically impossible or
prohibited. This class includes building footprints, major
roads, pavements, and other fixed urban elements. Based on
the characterization of urban cities with mixed commercial,
industrial, and residential activities, a foundational ratio was
established where prohibited cells constitute approximately
55-65% of the coarse optimization grid (GC). This high
percentage reflects the dense built environment that defines
the optimization challenge.
Vulnerable Cells (V)
This critical class designates areas where cooling interventions
yield the highest social benefit. Cells are assigned to this
category based on proximity to predefined social
infrastructure. Following principles of spatial equity and
climate vulnerability mapping, it prioritizes areas near schools,
health centers, and high-density residential zones. For
instance, all coarse grid cells within a 30-meter Chebyshev
buffer of a "school" point are classified as V. In the synthetic
testbed, these zones are algorithmically placed in relation to
building clusters. Vulnerable cells typically comprise 5-10% of
GC, ensuring they are high-priority targets without being so
pervasive as to trivialize the optimization problem.
Available Cells (A)
This class represents all remaining space deemed potentially
available for urban greening, such as sidewalks, park strips,
pocket parks, vacant lots, and easements. The available
planting area is therefore a residual of the urban form,
calculated as 𝐴 = 1 − (𝑃 + 𝑉). Using the ratios above, A
cells constitute approximately 25-40% of the coarse grid. This
range aligns, intending to test the framework's efficiency
under significant spatial constraints. The specific spatial
arrangement of these A cells is determined not randomly, but
by the Cellular Automata model, which clusters P cells and
leaves interstitial and peripheral spaces available, mimicking
real urban morphology.
For a given coarse grid GC with a total of NC cells, the cell
state assignment is a function
𝑆: 𝐺
𝐶 → {𝑃, 𝑉, 𝐴}
The optimization is constrained such that tree placement is
permitted only in cells where 𝑆(𝑐𝑒𝑙𝑙) = A, and the objective
function (SECPI) is weighted by the vulnerability mapping
where 𝑆(𝑐𝑒𝑙𝑙) = V.
