---
section: Methods §2.3 (Cooling Model, Allometrics, Species Parameters)
status: REVIEWED — one correction ready, one blocked
review: Flag Archive v2
flags: 20, 30, 35, 38, 41
owner: editor
depends_on: deriver (Flag #30 — BLOCKING)
---

# Methods §2.3

## Correction confirmed — apply

### §2.3.2 — the decay equation is missing a squared term (Flags #35, #38)
The written formula is linear-in-distance; the actual and intended function is **`exp(−λ(d/C_D)²)`** — quadratic, genuinely Gaussian-shaped. It matches the code and correctly reproduces both calibration points (62% at crown edge, 15% at full crown diameter).

**The word "Gaussian" is correct and stays. The equation is what is wrong.** Restoring the squared term closes #35 and #38 together. The earlier 38.7% recalculation that appeared to conflict had assumed the linear form; there was no arithmetic error.

> Provenance caveat: both resolutions cite the missing Entry 3. Re-verify by execution and re-source before closing. See the Entry 3 placeholder in `PROJECT_LOG.md`.

### Production parameters are not illustrative (Flag #41)
`decay_lambda = 1.9`, `cca_threshold = 1.2`, `competition_k = 5.0`. Confirmed twice in the production config. State them plainly as the fixed values used — the current "illustrative example" framing blocks reproducibility.

## 🔴 Blocked — Flag #30, highest-priority Deriver item

The DBH-from-height inversion `DBH = (h/h₀)^(1/h₁)` runs opposite to typical FORMIND allometrics. Confirmed numerically implausible, independently, twice (Entries 1 and 2):

- All six species yield `h < h₀`, ratio **0.278–0.742**
- Resulting DBH: **0.17–0.66 m**
- Computed LAI is **50–420× smaller** than the LAI values the model actually uses

The pipeline sidesteps this by using hardcoded `SPECIES_DATA['LAI']` rather than `get_computed_lai()`. That gap must be disclosed in Methods regardless of how #30 resolves — a reviewer who reads the code will find it.

**Until real H–D equations are sourced, the allometric sensitivity results are invalid.** If no defensible literature source exists for these six species or genus proxies, the fallback is to scope the allometric sensitivity out of the preprint with an explicit stated limitation. Decide early.

Also open: **#20** — AGB estimation-error percentages have no citation.

---

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 879–1150).
> Content: §2.3 Cooling Proxy Model (2.3.1–)
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

2.3 Cooling Proxy Model
Urban trees mitigate thermal stress through three
interconnected biophysical mechanisms: shading,
evapotranspiration, and wind modulation. The enhanced
framework integrates FORMIND's process-based geometry
to model these mechanisms more realistically in tropical
urban contexts.
Shading is primarily determined by Crown Projection Area
(CPA) and canopy architecture, which regulates solar
radiation interception. Evapotranspiration cooling is mediated
by Leaf Area Index (LAI) and stomatal conductance,
representing latent heat flux. Wind modulation effects are
indirectly considered through crown geometry and spacing
arrangements.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 9

2.3.1 Data Normalization and Derivation of Crown-Projection Area
and Leaf Area Index
To enable a fair and integrated comparison of diverse Tree
Functional Types (TFTs) within the optimization algorithm,
data normalization must be employed. This process converts
species-specific absolute measurements onto a common,
dimensionless scale from 0 to 1. Without this step, the
algorithm would be biased toward larger species simply due
to the scale of their raw numbers, overlooking the potential
efficiency or strategic value of smaller species. The
normalization of two key biophysical traits, being Crown
Projection Area (CPA) and Leaf Area Index (LAI), forms the
basis of each tree's "cooling potential" score in the model.
Crown Projection Area (CPA)
CPA estimates the two-dimensional area shaded by a tree's
canopy at noon, which is the primary driver of radiant heat
reduction. It is calculated directly from the species-specific
mature crown diameter (CD), assuming a roughly circular
canopy footprint:
𝐶𝑃𝐴 =
π
4
· 𝐶
𝐷
2
Represents the maximum shading footprint at solar noon. For
species where reliable 'ultimate spread' (crown diameter) data
were available from horticultural sources (PictureThis;
DENR-ERDB), this value was used directly to calculate
Crown Projection Area. The normalized CPA used in the
model is:
𝐶𝑃𝐴 =
𝐶𝑃𝐴
𝐶𝑃𝐴
𝑚𝑎𝑥
Where 𝐶𝑃𝐴 is the largest CPA among all candidate TFTs. 𝑚𝑎𝑥
Crown Diameter (CD)
Crown Diameter defines the maximum horizontal extent of
tree canopy at maturity, measured in meters. This parameter
directly scales the shading footprint and influences spatial
configuration decisions, particularly for optimizing canopy
overlap in clustered arrangements (Morakinyo & Lam, 2016).
Tree Height (h)
Mature tree height (m) influences vertical shading geometry
and interaction with urban canyon effects. While the
simplified model does not explicitly model three-dimensional
solar geometry, height informs the categorization of trees into
functional groups and constrains placement in proximity to
buildings and infrastructure (Park et al., 2020).
Diameter at Breast Height (DBH)
A crucial step in estimating the Leaf Area Index (LAI) for the
cooling model is determining a reliable value for Diameter at
Breast Height (DBH), the standard metric in forestry and
allometry. Directly measured DBH data for specific planting
sites is often unavailable during the planning stage. Therefore,
established allometric relationships are employed to
approximate DBH using more commonly available data. The
most robust method leverages existing allometric constants
for tropical trees. The FORMIND model provides a
well-established equation (Fischer et al., 2016):
𝐷𝐵𝐻 = (
ℎ
ℎ
0
)
(
1
ℎ
1
)
Where h is tree height, and ℎ and are species-specific
0
ℎ
1
parameters.
Leaf Area Index (LAI)
LAI quantifies the total single-sided leaf area per unit of
ground area. It is a critical proxy for a tree’s capacity for
evaporative cooling. Direct measurement is impractical for
urban planning; therefore, allometric scaling was used for
estimation.
𝐿𝐴𝐼 = 𝑙
0
· 𝐷𝐵𝐻
𝑙
1
Where DBH is the tree’s Diameter at Breast Height, and 𝑙
0
and 𝑙 are species-specific parameters.
1
2.3.2. Biophysical Non-Submodular Cooling Proxy Model
The core adaptation from Shaamala et al. (2025) is the
replacement of the Universal Thermal Climate Index (UTCI)
with a simplified cooling proxy. The cooling contribution of a
tree at any point in space is modeled using a distance-decay
function based on its crown diameter:
𝐶(𝑖, 𝑗) = 0. 70
𝐶𝑃𝐴
𝑗
𝐶𝑃𝐴
𝑚𝑎𝑥 ( ) + 0. 30
𝐿𝐴𝐼
𝑗
𝐿𝐴𝐼𝑚𝑎𝑥 ( )
⎡
⎢
⎣
⎤
⎥
⎦
· 𝑒𝑥𝑝(− λ ·
𝑑
𝑖𝑗
𝐶
𝐷,𝑗
)
⎰
⎱
⎱
⎰
·
1
1+𝑒𝑥𝑝(𝑘 · (𝐶𝐶𝐴
𝑔𝑟𝑜𝑢𝑛𝑑(𝑖)−𝐶𝐶𝐴𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑))
Where C(i,j) is the cooling at fine-grid point i from tree j, is
the normalized crown diameter of tree j, 𝑑 is the Euclidean
𝑖𝑗
distance, and λ is a decay constant calibrated from literature
on tropical tree cooling gradients (Morakinyo & Lam, 2016).
The sigmoidal reduction factor 𝑅 models diminishing
𝑐𝑜𝑚𝑝
(𝑖)
returns, adding trees where vegetation already exists yields
less benefit. The total cooling score for a configuration is the
sum of contributions from all trees across all grid points,
where it provides a spatially explicit, relative measure of
cooling effectiveness suitable for optimization.
𝐶
𝑡𝑜𝑡𝑎𝑙
(𝑖) =
𝑗=1
𝑁𝑡𝑟𝑒𝑒𝑠
∑ 𝐶(𝑖, 𝑗)
The relative contribution of shading (α₁ = 0.70) and
evapotranspiration (α₂ = 0.30) to the cooling proxy was
weighted at 0.70 and 0.30, respectively. This weighting is
supported by empirical studies in tropical humid cities where
shading accounts for 71–84% of daytime cooling (Morakinyo
et al., 2016), with evapotranspiration playing a secondary role
due to high ambient humidity limiting latent heat flux (Souza
et al., 2021; Yang et al., 2023).
2.3.3. Modeling Canopy Competition: Cumulative Crown Area
(CCA) and Sigmoidal Reduction Factor
A critical advancement in the cooling model is the explicit
incorporation of competition between adjacent trees. In
dense urban plantings, overlapping canopies compete for light
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 10

and air, leading to a saturation effect where adding more
foliage in the same area yields diminishing cooling returns. To
model this biophysical reality, the Cumulative Crown Area
(CCA) was integrated, adapted from forest ecology models
like FORMIND (Fischer et al., 2016), with a sigmoidal
reduction factor.
The CCA quantifies the total canopy coverage at any given
point on the ground. For a specific location, represented by a
fine-resolution grid cell at coordinates (x, y), it is calculated as
the sum of the Crown Projection Areas (CPA) of all trees
whose canopies extend over that spot. In forest ecology, CCA
represents the sum of crown projection areas within a given
vertical layer of foliage, normalized by patch area. For a given
scenario in a discrete grid allowing for canopy competition,
𝐶𝐶𝐴
𝑔𝑟𝑜𝑢𝑛𝑑
(𝑥, 𝑦) =
1
𝐴
𝑐𝑒𝑙𝑙 𝑗=1
𝑁𝑡𝑟𝑒𝑒𝑠
∑ 𝐶𝑃𝐴
𝑗
· δ(𝑑
𝑗
(𝑥, 𝑦) ≤ (
𝐶
𝐷
2
)
𝑗
)
Where 𝐶𝐶𝐴 is the cumulative crown area at grid
𝑔𝑟𝑜𝑢𝑛𝑑
(𝑥, 𝑦)
cell (x,y), 𝐴 is the area of grid cell (1 square meter), is
𝑐𝑒𝑙𝑙
𝐶𝑃𝐴
𝑗
the crown projection area of tree j, and δ(·) is the indicator
function that equals 1 if the distance from a point (x, y) to
tree j is less than or equal to the tree’s crown radius ( ) and 0
𝐶
𝐷
2
if otherwise. In essence, CCA is a spatially explicit map of
total leaf layer density. A CCA value of 1.0 means the grid cell
is fully covered by a single canopy layer. Values greater than
1.0 indicate significant overlap from multiple trees.
Sigmoidal Reduction Factor (𝑅 )
𝑐𝑜𝑚𝑝
Simply having a high CCA does not linearly reduce cooling;
the effect is nonlinear. To derive the decay constant λ, the
researchers worked backwards from empirical literature on
urban tree cooling (Bowler et al., 2010; Shashua-Bar &
Hoffman, 2000; Rahman et al., 2020), which indicates that
cooling diminishes to approximately 15% at a distance of one
full crown diameter from the trunk. Solving the equation
yields λ=1.897, which was rounded to 1.9 for model
implementation. This value produces physically consistent
cooling profiles, with approximately 62% of maximum
cooling at the crown edge and near-zero cooling beyond 1.5
times the crown diameter, aligning with observed field
measurements of individual tree cooling gradients. Initial
overlap may have little impact, but beyond a critical density,
competition severely limits further cooling gains. This
relationship is modeled using a sigmoidal (S-shaped)
reduction factor, 𝑅 (Morakinyo & Lam, 2016).
𝑐𝑜𝑚𝑝
(𝑖)
𝑅
𝑐𝑜𝑚𝑝
(𝑖) =
1
1+𝑒𝑥𝑝(𝑘 · (𝐶𝐶𝐴
𝑔𝑟𝑜𝑢𝑛𝑑
(𝑖)−𝐶𝐶𝐴
𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑
))
Where CCAthreshold is the critical crown area density where
competition begins to significantly reduce cooling efficacy
(e.g., 1.2). This can be tuned for different zones (e.g., a lower
threshold of 1.0 for pedestrian areas to ensure ample light
and air flow). The steepness parameter k controls how
abruptly the reduction takes effect once the threshold is
crossed.
This mechanism ensures the ACO algorithm avoids
unrealistic, counterproductive solutions that pack too many
trees into a small area. It incentivizes the algorithm to
discover configurations that balance wide coverage with
strategic spacing, reflecting real-world arboricultural
guidelines for tree planting. The parameters (𝐶𝐶𝐴 , k)
𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑
can be calibrated using empirical data on microclimate
conditions under varying canopy densities (Morakinyo &
Lam, 2016), making the model adaptable to different urban
contexts and tree species, including Philippine TFTs (Abino
et al., 2014).
