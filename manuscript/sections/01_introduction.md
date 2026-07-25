---
section: Introduction (incl. §1.1 Theoretical Foundation, Scope, Delimitations)
status: REVIEWED — corrections agreed, not yet applied
review: Flag Archive v1 + v2
flags: 11, 12, 15, 16, 17
owner: editor
---

# Introduction

## Agreed restructuring — not yet applied

- **#15** — §1.1 Theoretical Foundation ran ~10 paragraphs across 4 subsections plus a diagram. Agreed: condense to **3 paragraphs** in the main text; full version moves to **Supplementary Material S1**.
- **#16** — Scope, Delimitations, Spatial Framework, and Biological Parameters paragraphs carry Methods-level detail (cell-size rationale, coordinate storage, crown geometry assumptions). Agreed: relocate to Methods, leave a short scope statement.
- **#12** — a duplicated sentence ("In tropical settings like the Philippines, these mechanisms can yield local cooling benefits of 2–5°C…") appeared verbatim back-to-back. Confirmed a copy artifact; removed.
- **#17** — Figures 1 and 2 are original artwork by the author team (Canva). Add the attribution line to both captions.
- **#11** — the 100 × 100 m domain is synthetic and non-georeferenced. Reconciled against the Abstract; keep the two consistent.

## Register note for Option A

This is where the high-school thesis voice is most concentrated: motivational framing, beneficiary enumeration ("marginalized communities... academic researchers... environmental NGOs..."), and second-person implication. A Q1 geoscience Introduction states the gap, the contribution, and the scope. The beneficiary paragraph should compress to a single sentence on practical relevance or move to the Discussion.

Preserve every citation. Preserve the delimitations — they are load-bearing and a reviewer will look for them.

---

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 28–384).
> Content: INTRODUCTION incl. research questions and §1.1 Theoretical Foundation
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

INTRODUCTION
The planet is experiencing accelerated warming, with global
temperatures rising by approximately 0.15°C–0.20°C per
decade since 1995, and 2023 reaching 1.40°C above
pre-industrial levels (Lindsey & Dahlman, 2023; WMO, 2023).
This trend is particularly dangerous for urban areas, which
house over half the global population and suffer from the
Urban Heat Island (UHI) effect. The Philippines is especially
vulnerable, with Metro Manila seeing ambient temperatures
4.5°C higher than peri-urban zones due to impermeable
surface coverage exceeding 85% and a lack of green space
that is averaging less than 1.5 m² per capita (Estoque &
Murayama, 2015; DENR-EMB, 2023). Projections suggest
local temperatures could rise by up to 4.1°C by 2100,
threatening public health and economic productivity
(PAGASA, 2018).
To mitigate this thermal stress, urban trees utilize three
primary biophysical mechanisms: shading, evapotranspiration,
and wind modulation (Coutts et al., 2016). Shading directly
reduces mean radiant temperature by blocking solar radiation,
while evapotranspiration cools the air through latent heat
flux—a process governed by species-specific traits like leaf
area and stomatal conductance (Speak et al., 2020; Pace et al.,
2021). In tropical settings like the Philippines, these
mechanisms can yield local cooling benefits of 2-5°C
(Morakinyo & Lam, 2016).
In tropical settings like the Philippines, these mechanisms can
yield local cooling benefits of 2–5°C (Morakinyo & Lam,
2016). However, the success of these nature-based solutions
is dependent on tree placement, crown morphology, and
spatial arrangement, which are often overlooked in
conventional urban planning, as shown in Figure 1 (Bajsanski
et al., 2016; Milosevic et al., 2017).
Despite these benefits, a significant technical gap exists
because high-fidelity models such as ENVI-met and
Computational Fluid Dynamics (CFD) are too
computationally heavy and data-demanding for the rapid,
iterative testing required in algorithmic optimization
(Broadbent et al., 2019; Mirzaei, 2021). Conversely, simpler
tools like SOLWEIG often focus purely on shading and
radiation while neglecting species-specific physiological
processes, leaving a methodological gap between
high-resolution simulations and computationally tractable
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 1

models (Lindberg et al., 2008; Huang et al., 2014; Briegel et
al., 2023; Hao et al., 2023).
Figure 1. Conceptualized tree cooling mechanism.
Furthermore, an equity gap persists as most existing
optimization frameworks treat cooling as a purely biophysical
objective, aiming for maximum aggregate temperature
reduction while overlooking the spatial equity dimensions and
the disproportionate heat exposure experienced by vulnerable
populations. In these models, equity is often a secondary
consideration or a post-hoc evaluation rather than the
foundational driver of the optimization itself. This is
compounded by a Philippine context gap, as there is currently
no optimization model that utilizes Philippine Tree
Functional Types (TFTs) to address local urban thermal
vulnerability. Most studies rely on simplified thermal proxies
or assume homogeneous tree traits, thereby overlooking the
unique crown morphologies and cooling signatures of native
species (Zhao et al., 2017; Stojakovic et al., 2020), which
prevents local planners from moving beyond aesthetic
guidelines to performance-based greening strategies.
This study addresses these gaps by developing a formal
computational-mathematical framework that
reconceptualizes urban greening as a problem of equitable,
constrained optimization on a discrete spatial lattice. The
core innovation is the integration of three advanced
components: an integer lattice formalism for rigorous
analysis, a procedural testbed generator (Cellular Automata)
for robustness testing, and a novel equity-driven objective
function—the Synergistic and Equitable Cooling
Performance Index (SECPI)—that explicitly prioritizes
benefits for vulnerable populations. By implementing Ant
Colony Optimization (ACO) to solve this non-submodular
problem, the framework moves beyond generic shading
proxies to model species-specific biophysics and
competitive canopy interactions.
Specifically, the researchers aim to answer the
following questions:
1. How do biophysical traits of Philippine Tree
Functional Types determine species-level cooling
performance?
2. How does Cellular Automata generate
morphologically diverse grids through land use
ratio constraints, zone-type classification, and
spatial transition rules?
3. How does the Ant Colony Optimization
algorithm navigate the constrained solution space
to generate tree placement configurations that
balance aggregate cooling coverage and localized
cooling intensity?
4. What is the performance and sensitivity of the
SECPI-driven optimization, and how does its
output differ; in terms of spatial equity, species
selection, and cooling metrics, from a benchmark
across diverse urban morphologies?
1.1 THEORETICAL FOUNDATION
Three complementary theoretical strands informed the
development of the algorithmic optimization framework
presented in this study: sustainability thinking, complexity
thinking, and resilience thinking. This research adopts an
integrative perspective that selectively draws on each strand's
core logic to collectively support the focus of a discrete,
mathematically formalized optimization framework for urban
greening, thereby shaping the framework's objectives,
structure, and evaluation approach. These perspectives
converge on the need to treat the urban landscape not as a
continuous void but as a structured, finite resource, leading to
the core mathematical formalism of this research:
optimization on an integer lattice. This is to deliver adaptive,
performance-based urban greening strategies tailored to the
tropical Philippine context while addressing both
environmental and social dimensions of urban heat
mitigation.
Figure 2. Theoretical Framework
1.1.1 Sustainability Thinking
Sustainability thinking emphasizes the need to develop
interventions that enhance present-day urban livability
while remaining effective under future climatic conditions
(Yigitcanlar et al., 2024; Scordato & Gulbrandsen, 2024). In
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 2

this study, this perspective shaped the dual focus on
improving immediate outdoor thermal comfort while
anticipating future increases in thermal stress under climate
change scenarios. Translating this holistic goal into
actionable planning requires the selection of tree species
based on their morphological traits. It also requires
breaking down the continuous urban fabric into
manageable units. This study operationalizes this by
discretizing the urban area into a finite grid of Available
cells. This transforms the philosophical principle of
"optimal resource allocation" into a concrete combinatorial
assignment problem, where decisions (planting a tree of a
specific species) are made for each discrete unit of space.
This discrete representation is fundamental for quantifying
trade-offs and ensuring that cooling benefits are
systematically distributed, aligning with the sustainability
tenet of equitable, long-term planning.
Systems thinking, an underlying principle of sustainability
(Meadows, 2008), influenced the framework's development
by conceptualizing the urban microclimate as a dynamic
system where vegetation, built structures, and social factors
interact to shape thermal experiences. This holistic
approach necessitated integrating multiple environmental
layers—including crown morphology, spatial arrangement,
and equity considerations—rather than treating cooling as
an isolated function of individual trees. By framing urban
cooling as an emergent property of system interactions, the
optimization process seeks configurations that maximize
synergistic effects across the entire study area.
1.1.2 Complexity Thinking
Complexity thinking recognizes that urban environments
function as nonlinear, interconnected systems where small
changes can lead to disproportionate outcomes (Abujder
Ochoa et al., 2025; Turner & Baker, 2019). The cooling
effect of a tree is not independent; it synergizes with or
competes with neighboring trees, creating a
non-submodular objective function where the whole is not
a simple sum of its parts. Furthermore, urban space is
riddled with constraints: building footprints, infrastructure,
and biophysical limits such as canopy overlap (Cumulative
Crown Area). These constraints define a highly complex,
non-convex feasible region within the planning area. To
navigate this complex solution space, a robust search
strategy is required. This study employs Ant Colony
Optimization (ACO), a metaheuristic whose decentralized,
iterative logic is uniquely suited for exploring such
constrained, nonlinear landscapes where traditional
gradient-based or exact methods falter due to
computational intractability.
Adaptation and emergence, central to complexity thinking,
are reflected in the optimization logic (Holland, 1992).
Rather than imposing fixed configurations, the framework
explores adaptive combinations of tree placement and
species selection, allowing effective solutions to emerge
through iterative evaluation. Interconnectedness is treated
as fundamental, with spatial layout, species functionality,
and social vulnerability considered continuously interacting
components within the broader urban system. By
embracing these principles, the framework remains flexible
and responsive to the multi-scalar complexities inherent in
Philippine urban environments, where formal and informal
settlement patterns create unique spatial challenges.
1.1.3 Resilience Thinking
Resilience thinking emphasizes the capacity of systems to
absorb disturbances while maintaining essential functions
and to adapt dynamically to changing conditions (Folke,
2006; Xu et al., 2015). Within the context of urban
microclimate management, resilience is not about resisting
environmental stresses but about enabling urban spaces to
sustain thermal comfort under fluctuating and intensifying
heat pressures. This perspective shaped the framework's
sensitivity to spatial variations in thermal vulnerability and
its incorporation of equity considerations in cooling
distribution.
The development of the Synergistic and Equitable Cooling
Performance Index (SECPI) operationalizes resilience
principles by measuring not only the magnitude of cooling
improvements but also their distribution across socially
vulnerable areas. This recognizes that in rapidly urbanizing
Philippine cities, thermal vulnerability is often spatially
correlated with socioeconomic disadvantage, requiring
interventions that explicitly address these disparities to
build truly resilient communities.
1.1.4. Integrative Perspective to Mathematical Formalization
The development of the optimization framework
synthesized key principles from sustainability, complexity,
and resilience thinking into a cohesive logic. Sustainability
thinking provided the directional goal of enhancing
long-term urban livability through evidence-based greening.
Complexity thinking informed the adoption of adaptive,
decentralized optimization methods capable of navigating
dynamic, nonlinear urban systems. Resilience thinking
introduced spatial equity considerations, highlighting the
need to distribute cooling benefits to vulnerable
populations rather than focusing solely on aggregate
performance metrics.
The imperatives from all three perspectives are unified and
expressed through a single mathematical construct: the
integer lattice. The planning grid is formally represented as
a finite subset of the two-dimensional integer lattice, where
each cell is a coordinate point. This roots the study in the
well-established field of integer and combinatorial
optimization. The problem becomes one of selecting an
optimal subset of lattice points under constraints. The
non-submodular, nonlinear cooling objective aligns with
research on optimizing complex functions over discrete
lattices. The spatial constraints define a specific geometric
feasible region within the lattice, a subject of study in its
own right. The use of the ACO metaheuristic represents a
pragmatic and powerful applied approach to solving this
challenging integer lattice optimization problem for a
real-world ecological application.
This study holds significant implications for sustainable
urban development in the Philippines by adapting
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 3

algorithmic optimization approaches to local planning
contexts. The research directly aligns with the Department
of Science and Technology's (DOST) Harmonized
National Research and Development Agenda (DOST,
2022), particularly its emphasis on climate-resilient
communities and nature-based solutions. By developing a
computationally accessible framework for evidence-based
tree placement, the study contributes to Sustainable
Development Goal 11 (Sustainable Cities and
Communities) and SDG 13 (Climate Action) (United
Nations, 2015), addressing urban heat island mitigation
through locally adapted strategies.
The practical significance extends to multiple stakeholders.
Urban planners gain accessible, data-driven planting
templates for barangay-scale implementation, moving
beyond aesthetic guidelines to performance-based greening
strategies. The Department of Environment and Natural
Resources (DENR) acquires species-specific cooling
performance metrics to inform species selection guidelines
and urban forestry policies, supporting evidence-based
implementation of Administrative Order 2017-11.
Marginalized communities in heat-vulnerable districts like
Caloocan benefit from targeted interventions that address
thermal inequities through spatial optimization. Academic
researchers receive transferable methodologies for adapting
computational approaches to tropical urban contexts, while
environmental NGOs obtain evidence-based advocacy
tools for green infrastructure investment.
To ensure focus and feasibility, the scope of this study is
limited to the investigation of spatial optimization of urban
tree placement within a defined 100×100 m study area,
focusing exclusively on publicly accessible land use
categories, including sidewalks, road reserves, and
community open spaces. The research framework is
grounded in a specific computational paradigm where
model parameterization is driven by six Philippine Tree
Functional Types (TFTs), classified according to crown
morphology traits and allometric relationships. Social equity
is integrated into the spatial logic through a
vulnerability-based weighting scheme, ensuring that the
optimization objective accounts for demographic
sensitivity. The technical pipeline utilizes a Binary Cellular
Automata model for urban grid generation and employs
Ant Colony Optimization (ACO) via the scikit-opt Python
library. Performance is evaluated using the Synergistic &
Equitable Cooling Performance Index (SECPI), which
compares scenarios through a biophysical proxy and
cumulative competition model.
However, the study is subject to several delimitations
designed to maintain computational focus on spatial
optimization rather than long-term ecological growth. The
assessment of thermal mitigation is restricted to
proxy-based cooling estimations, thereby excluding
high-fidelity microclimate simulations, wind turbulence
modeling, and the influence of anthropogenic heat or
building energy exchange. Furthermore, the model does
not account for subsurface variables—such as soil
composition and groundwater processes—nor does it
reflect temporal dynamics like seasonal or diurnal
variations. Finally, the framework bypasses socio-political
implementation constraints and economic feasibility.
Consequently, the findings represent a prototype for
feasible spatial optimization and strategic decision-support
rather than a comprehensive urban climate model.
Furthermore, the study's spatial framework is defined by a
100 x 100 m² grid,a scale selected to align with ecological
standards for reliable biomass estimation in tropical forests.
This area is discretized into a "coarse grid" of 10 x 10 m²
cells, which serve as the primary units for urban zone
analysis and tree placement optimization. By treating urban
space as a structured two-dimensional integer lattice rather
than a continuous void, the model can calculate how tree
placement impacts specific spatial coordinates.
In this system, each specific spatial coordinate (𝑥, 𝑦)within
the lattice represents a potential planting site or a
"receptor" point for cooling benefits. Because the space is
discretized, every 10 m² cell is assigned a unique coordinate
that stores local data, such as its social vulnerability index
and existing thermal load. This coordinate-based approach
allows the optimization algorithm to evaluate the cooling
contribution of a tree at point 𝐴 on the temperature of a
specific coordinate 𝐵. By mapping these interactions across
a finite set of points, the model can identify the locations
where a tree’s "cooling footprint" maximizes synergy with
neighboring trees and provides the highest equity-weighted
relief to the surrounding cells.
Regarding biological parameters, the model assumes all
trees are mature to evaluate their peak cooling potential.
For spatial modeling, trees are geometrically treated as
circles defined by their mature crown diameter. This
simplification allows the model to calculate shading areas
and evaluate competitive or synergistic canopy interactions
within the discrete lattice. These effects are governed by
Euclidean distance-decay functions, which model the
attenuation of cooling as it spreads from the tree center to
the surrounding grid.
These limitations establish clear boundaries for interpreting
findings and identify priority areas for methodological
refinement in future research, particularly regarding
empirical validation, temporal dynamics, and
implementation feasibility.
While the research methodology itself does not require
significant financial resources (utilizing open-source
software and publicly available data), the study's outputs are
designed for implementation within typical municipal
greening budgets. The optimized planting templates can be
implemented within standardized barangay greening
allocations (approximately ₱2.5M per DILG 2021
guidelines), prioritizing cost-effective species with
demonstrated cooling performance.
This alignment with existing budgetary frameworks
enhances the practical applicability of research findings and
supports evidence-based resource allocation in urban
greening initiatives.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 4

