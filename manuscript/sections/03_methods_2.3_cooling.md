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

<!-- PASTE CURRENT §2.3 BELOW -->
