---
section: Methods §2.5–§2.6 (Verification & Validation, Uncertainty, Bias & Limitations)
status: REVIEWED — one blocking flag
review: Flag Archive v2
flags: 39
owner: editor
depends_on: D-03 (outcome metric) → code-stressor execution — BLOCKING
---

# Methods §2.5–§2.6

## 🔴 Flag #39 — the significance claim has no test behind it

§2.5.2 claims a *"statistically significant redirection of resources"* toward high-vulnerability zones in the SECPI-ON case, with **no test named, no replicate count, no significance threshold, no p-value.** A reviewer will reject this on sight. It cannot go into a preprint as written.

Recommended design, pending D-03:

- **Test:** paired Wilcoxon signed-rank (non-parametric; proportions across few configurations are unlikely to be normal and n is small)
- **Pairing:** WITH-vulnerable vs. WITHOUT-vulnerable on the same grid and k
- **n = 30** — k = 1…6 × 5 existing restarts per k
- **Outcome metric — the open decision:** proportion of delivered cooling landing in V-zones *(recommended — independent of SECPI, avoids circularity)*, **or** proportion of trees placed adjacent to V-zones. Pre-specify one. Testing both and reporting the better one is p-hacking and a reviewer will catch it.
- **Report:** test name, n, statistic, two-sided p, and matched-pairs rank-biserial correlation as effect size

**If non-significant:** soften to descriptive — *"a greater share of cooling benefit was allocated to high-vulnerability zones under the vulnerability-weighted objective (median X% vs. Y%)"* — with no significance language anywhere. This outcome is acceptable and must not be reframed into implication.

⚠️ Note also that `AutomatedInterpreter.interpret_scenario_comparison()` prints `"Difference: SIGNIFICANT"` whenever `|Δ| > 0.1`. That is a hardcoded magnitude threshold, **not a statistical test.** No output from that function may be described as significance in the manuscript.

## §2.5.3 — uncertainty quantification

Described as "Morris-method One-at-a-Time (OAT) screening." Verify the terminology: Morris screening and plain OAT are distinct methods, and the implementation is `SensitivityAnalyzer.run_oat_analysis(n_samples=3)`. If it is plain OAT, call it plain OAT.

Also relevant: the allometric branch of this analysis previously returned fabricated values (`baseline × np.random.uniform(0.98, 1.02)`). That has been removed, but §2.5.3's claims about allometric sensitivity remain blocked on Flag #30.

## §2.6 — bias and limitations

Well-constructed and citation-backed; the lightest-touch section in the manuscript. Additions needed: the hardcoded-LAI vs. computed-LAI gap (§2.3), and the deterministic 8-cell V-zone (§2.2.1) if it is not disclosed there.

---

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 1342–1427).
> Content: §2.5 Verification and Validation (2.5.1–2.5.3), §2.6 Mitigation of Bias and Limitations
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

2.5 Verification and Validation
The robustness and mathematical integrity of the Equitable
Integer Lattice Optimization Paradigm are established
through a structured verification and validation (V&V)
protocol. This section details the procedures used to ensure
that the computational implementation accurately reflects the
mathematical formulations of the Synergistic and Equitable
Cooling Performance Index (SECPI) while delivering reliable,
generalizable insights for urban heat mitigation and
distributive justice (Shi et al., 2016).
2.5.1 Verification
The verification stage focuses on confirming the
code-to-mathematical correspondence of the framework,
ensuring that the algorithmic logic correctly executes the
intended biophysical and optimization functions. This process
begins with unit verification, where individual components of
the cooling proxy model are tested against canonical cases.
For example, the radial decay of a single tree’s cooling effect
is verified to conform to its theoretical range, and the
Cumulative Crown Area (CCA) penalty is checked to ensure it
correctly reduces cooling output in synthetic, overcrowded
setups. Furthermore, algorithmic verification is conducted by
testing the Ant Colony Optimization (ACO) performance on
a simplified, submodular proxy function. In these scenarios, a
standard greedy algorithm serves as a benchmark; the ACO
must match or closely approximate this benchmark to verify
its capability to navigate complex search spaces before being
applied to the full non-linear SECPI objective.
2.5.2 Validation
Validation of the paradigm is achieved through a multi-step
process that tests the framework's performance across diverse
urban and biological scenarios. Morphological robustness
validation involves running the optimization pipeline on
varied urban forms, such as organic clusters, grids, and sparse
suburban layouts generated by the Cellular Automata (CA)
model. The framework is considered validated if the
ACO-SECPI logic consistently produces intelligible
configurations that outperform random placements across all
morphologies, demonstrating generalizability beyond a single
spatial layout. Functional diversity validation is performed by
keeping the urban morphology fixed while varying the
available species portfolio. This step confirms whether the
model effectively leverages the unique functional traits of
different Philippine Tree Functional Types (TFTs), such as
the expansive shading of Narra (Pterocarpus indicus) or the
dense evapotranspiration of Duhat (Syzygium cumini), to
create higher-performing and more resilient cooling solutions.
The final stage, cross-scenario validation, empirically
demonstrates the paradigm’s core contribution to spatial
justice through a comparative case study. The framework is
run under two conditions: a "SECPI-ON" case using the full
equity-driven objective and a "SECPI-OFF" case that ignores
equity weights (We = 1) to focus solely on aggregate cooling
efficiency. A successful validation is marked by a statistically
significant redirection of resources toward high-vulnerability
zones in the SECPI-ON case. This demonstrates the model's
capacity to enact distributive justice (Cutter et al., 2003), even
when it necessitates a marginal trade-off with aggregate
cooling output.
2.5.3 Uncertainty Quantification
To ensure that the insights derived from the optimization are
robust results of the algorithmic logic rather than artifacts of
parametric noise, a formal uncertainty quantification is
integrated into the protocol. Parameter
uncertainty—specifically regarding allometric coefficients for
Leaf Area Index (LAI) and cooling decay constants, is
propagated through the model via a Morris-method
One-at-a-Time (OAT) screening approach. This sensitivity
analysis quantifies the variance in the final SECPI score and
assesses the stability of the tree configurations. By
distinguishing robust algorithmic trends from sensitivities to
input parameters, this step ensures that the resulting urban
forestry recommendations are reliable under the inherent
variability of biological and environmental data.
2.6 Mitigation of Bias and Limitations
The study acknowledges several potential sources of bias and
limitations. High ambient humidity in Metro Manila may
reduce real-world evapotranspiration cooling compared to
simulation outputs, possibly leading to overestimation of
thermal benefits (Morakinyo & Lam, 2016). The absence of
empirical field validation means that model results rely
entirely on literature-derived and database parameters, which
may not fully capture local microclimatic variability (Kim et
al., 2023). Complex aerodynamic effects in dense high-rise
environments may be underrepresented in the Gaussian
cooling model (Li et al., 2024).
