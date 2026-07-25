---
section: Conclusion
status: 🔴 NEVER REVIEWED
review: none
flags: inherits 43, 44
owner: editorial-flagger (first), then editor
depends_on: Results regeneration
---

# Conclusion

## Never editorially reviewed. Rewrite last, after Results.

## Numerical conflict with the Abstract — unresolved

| Quantity | Abstract | Conclusion |
|---|---|---|
| Cooling reduction | "up to **0.809 °C**" | "maximum localized **0.80 °C**, mean **0.11 °C** across the grid" |

Rounding may explain the first pair. The mean of 0.11 °C appears **only** in the Conclusion and nowhere in the Abstract — a reviewer comparing the two will read the Abstract as overstating the effect by omitting the mean. Whichever survives regeneration, both sections must report the same statistics.

## Claims inheriting Flag #43 — currently unreproducible

- "combinatorial analysis of 63 species subsets"
- SECPI threshold **3.13**, "performance drop of approximately **28%**"
- crown diameter as dominant variable, **SI = 0.46**

The sensitivity figure (SI = 0.46) may be recoverable from `SensitivityAnalyzer` output even though the 63-subset analysis is not — verify separately rather than assuming they share a fate.

## Framing to tighten in Option A

The Conclusion asserts the study *"successfully developed and validated"* the framework. **"Validated" is doing more work than the evidence supports.** There is no field validation, no remote-sensing comparison, and no real site — the manuscript states this itself (Flag #8, §2.6). Verification against internal mathematical specification is not validation against reality, and a geoscience reviewer will draw that line sharply.

Recommend: *"developed and internally verified,"* with external validation named explicitly as future work. This costs nothing and removes an easy rejection hook.

The practical-recommendation paragraph (prioritize few large-crowned species over complex mixed-species strategies in resource-constrained settings) is the manuscript's strongest contribution. It should survive intact — **provided Flag #43 resolves**, since it rests entirely on the 63-subset analysis.

---

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 2089–2200).
> Content: CONCLUSION, ACKNOWLEDGMENT
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

CONCLUSION
This study successfully developed and validated the Equitable
Integer Lattice Optimization Paradigm, a computational
framework for optimizing urban tree placement within a
discrete urban fabric. By integrating Ant Colony
Optimization with the Synergistic and Equitable Cooling
Performance Index (SECPI), the research addressed the dual
imperative of maximizing biophysical cooling while ensuring
spatial justice. The results demonstrate that the framework is
capable of generating meaningful planting configurations
within a simulated 100 x 100 m² urban grid. The
best-performing configuration under the equity-weighted
scenario achieved a maximum localized cooling reduction of
0.80 °C and a mean reduction of 0.11 °C across the grid,
confirming the model's ability to deliver targeted thermal
relief.
The combinatorial analysis of 63 species subsets revealed that
cooling performance was driven primarily by crown diameter
rather than species richness. Configurations that included
large-crowned species, specifically Pterocarpus indicus
(Narra) and Albizia lebbeck (Akleng-parang), consistently
achieved the highest SECPI scores. Conversely, subsets
lacking these two species fell below a SECPI threshold of
3.13, representing a performance drop of approximately 28%.
The sensitivity analysis further corroborated this, identifying
crown diameter as the single most dominant variable
(Sensitivity Index = 0.46), far outweighing allometric or
shading coefficients. This finding carries significant practical
weight for Philippine urban planners. It suggests that in
resource-constrained settings, prioritizing a few
high-performing species with large crown coverage yields
cooling outcomes superior to complex mixed-species
strategies that rely on smaller trees.
The equity-weighting component of SECPI proved effective
in directing the optimizer toward configurations that allocate
cooling benefits to socially vulnerable zones. The
cross-scenario validation highlighted a distinct trade-off
between aggregate efficiency and distributive equity. While
the efficiency-focused scenario produced a higher mean
cooling intensity of 0.19 °C using a monoculture strategy, the
equity-weighted scenario accepted a 42% reduction in global
mean cooling to redirect benefits toward high-priority
populations. This confirms that the framework successfully
operationalizes resilience thinking by treating equity not as a
secondary constraint but as a fundamental driver of the
optimization process.
The robustness of the framework was established through its
consistent performance across diverse urban morphologies.
The algorithm achieved stable convergence across six distinct
land-use patterns generated by Cellular Automata, performing
best in "Dense Organic" environments where building
clusters create synergistic shading opportunities. This design
choice supports the generalizability of the approach, making
it adaptable to the varied and often informal urban layouts
found in Philippine cities where detailed spatial datasets may
not be readily available.
Several limitations should be noted when interpreting these
findings. The cooling model relies on proxy-based estimations
rather than empirical thermal measurements and does not
account for wind dynamics, anthropogenic heat sources, or
temporal climate variations. Furthermore, the sensitivity
analysis indicates that the model is highly responsive to errors
in crown diameter inputs, necessitating precise field
measurements for future applications. Finally, the treatment
of trees as static lattice points does not reflect growth
trajectories or maintenance requirements over time.
Despite these constraints, the study demonstrates that a
discrete lattice optimization approach, combined with
equity-weighted performance metrics and metaheuristic
search, produces actionable and spatially just tree placement
strategies. The framework contributes a transferable
methodology that bridges computational optimization and
urban ecological planning, providing a rigorous foundation
for future empirical validation and scaled implementation
across climate-vulnerable cities.
Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) 25

RECOMMENDATIONS
Due to the theoretical nature of the framework, future studies
can incorporate Geographic Information Systems (GIS) to
enhance spatial accuracy, empirical verification, and analytical
depth. GIS would enable the integration of multiple spatial
datasets, including land surface temperature, vegetation cover,
population density, and social vulnerability indicators, within a
single geospatial framework allowing precise identification of
intervention zones for potential urban city policymaking.
Applying the model to a specific city would allow validation
against observed land surface temperature data and
demographic distributions, evaluating whether the proposed
equity-weighted prioritization produces measurable cooling
benefits in high-demand areas. Exploration between the
concepts of cooling coverage, cooling intensity and their
trade-offs can also be explored to further advance the rigor of
a justifiable cooling for zones.
INDIVIDUAL AUTHOR’S CONTRIBUTIONS
L.G.; Contributed to research design, code debugging, and in
supervising the research manuscript. V.J.; Contributed to
research methodology, code co-debugging, and in completing
the research manuscript. D.L.Z.; Performed manuscript
revisions, involved in mathematical framework of research.
V.L.; Completed manuscript revisions, suggested revisions in
research design. V.E.; Performed manuscript revisions,
suggested revisions in research methodology. All contributed
to completing the final version of the manuscript.
ACKNOWLEDGMENT
The researchers acknowledge the contribution of
the following: Visual Studio Code for the hosting of Python
and its libraries, Sir Alyson L. Yap for guidance in the
research process, members of the Science Research
Committee for the continuous guidance; and school head Dr.
Warren A. Ramos for his support in research projects in
Caloocan City Science High School.
