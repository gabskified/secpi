---
section: Title, Author Block, Abstract, Keywords
status: REVIEWED — rewrite blocked
review: Flag Archive v1 + v2
blocking: D-04 (title), and every number below is void pending Results regeneration
flags: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
owner: editor
---

# Title & Abstract

## ⚠️ Do not polish this section yet

The Abstract is the **last** section to be rewritten, not the first. Every quantitative claim in it is downstream of Results, and Results are void (Option B) or unreproducible (Flag #43). Polishing now guarantees a second rewrite.

## Void numbers currently in the Abstract

| Claim | Status |
|---|---|
| global cooling reduction up to 0.809 °C | Void — Option B. Also conflicts with the Conclusion's "0.80 °C max, 0.11 °C mean". |
| SECPI scores ranged from 3.02 to 4.39 | Void — generated under the superseded self-normalizing scheme |
| configurations lacking Akleng-parang and Narra scored 28% lower | **Unreproducible** — Flag #43 |
| functional diversity offered negligible improvement (0.03%) | **Unreproducible** — Flag #43 |

## Open flags

- **#5** — SECPI range stated with no defined scale. Closes when D-02 fixes the goalposts.
- **#9** — land-use ratio source unclear. With Deriver.
- **#6** — 28% / 0.03% presented without indicating whether a test was run. Resolved as raw percentage differences, not significance tests; the rewrite must say so explicitly.
- **#10 / #11 / #3** — "Mapping" implies literal georeferencing; the study is synthetic and non-georeferenced. See D-04.

## Locked content

- SECPI = **Synergistic and Equitable Cooling Performance Index** (Flag #1).
- *Pterocarpus indicus* (Narra), *Albizia lebbeck* (Akleng-parang) — author-corrected, supersedes an external *A. procera* verification (Flags #2, #18).
- Cooling values are **modeled only**, with no field or remote-sensing validation (Flag #8). The Abstract must not imply otherwise.
- Cellular automata is genuinely used, for grid generation (Flag #4) — the keyword is earned, but the Abstract's methods summary should mention it.

---

---

## ORIGINAL MANUSCRIPT TEXT — verbatim

> **Provenance.** Extracted 2026-07-25 from `manuscript/MCS02_SECPI_original.pdf` (source lines 1–27).
> Content: Title, authors, affiliation, abstract, keywords
> **Verbatim — no edits, no corrections applied.** Known extraction artifacts retained deliberately:
> repeated page footers (`Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025) <page>`, 48 occurrences
> document-wide), and equations/subscripts that flattened during PDF text extraction — these need visual
> comparison against the PDF before any equation is trusted. Figures and tables are not present in this text layer.
> The editor works below this line; everything above it is editorial notes, not manuscript content.

---

Mapping Synergistic and Equitable Urban Cooling (SECPI) of Philippine Tree
Functional Types: A Discrete Grid Optimization Grounded in Integer Lattice
Theory
Gabriel Clark C. Lacuanan¹, Jian R. Valenzuela¹, Zane Jean G. De Leon¹, Euvherline Jewel S. J.
Villadolid¹, Lourdes Marie V. Valdes¹, Guiller Jobert H. Suarez¹
1Caloocan City Science High School
P. Sevilla Street cor. 10
th Avenue Grace Park Caloocan City, Metro Manila
*Corresponding Author: gablacuanan@gmail.com
ABSTRACT
Recent mathematical advancements are being integrated into urban sprawl and metaheuristic optimization
studies addressing urban heat islands (UHI) and cooling effects of trees, with optimal placement of trees being
promising in addressing microclimate solutions to the UHI effect. However, relevant studies have incorporated
costly and data-demanding software and also largely overlooked the spatial equity dimensions of urban cooling,
with optimization frameworks not accounting for the disproportionate heat exposure experienced by vulnerable
populations. This study employs integrated mathematical modeling, combining discrete optimization on an integer
lattice with spatially explicit biophysical proxy functions. Tree placement is operationalized as a binary integer
program solved via Ant Colony Optimization (ACO), while cooling effects are modeled using distance-decay
equations with tropical forestry allometrics. The framework incorporates equity-weighting through an objective
function (SECPI) and is validated through scenario analysis and sensitivity testing. The best configuration achieved
a global cooling reduction of up to 0.809 °C. SECPI scores ranged from 3.02 to 4.39, revealing a distinct
performance cliff: configurations lacking large-crowned species (Akleng-parang and Narra) scored 28% lower.
Notably, functional diversity offered negligible improvement (0.03%) over well-chosen mono-species solutions,
confirming that under the Gaussian decay model, shading area dominates evapotranspiration in cooling
effectiveness. This approach provides urban planners a realistic and scalable optimization framework given equity
constraints, allowing incorporation of various empirical validations to further increase its scalability.
Keywords: Tree functional types, cooling index, urban heat island, integrative perspective, lattice grid, optimization, equity weights, cellular automata
