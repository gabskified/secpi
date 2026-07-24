---
section: References, Glossary, Appendices A–B, Supplementary
status: NOT REVIEWED
owner: deriver (references), editor (appendices)
---

# References, Glossary & Appendices

## References — Deriver task, not yet started

No systematic reference audit has been performed. Before preprint:

- Every in-text citation resolves to the reference list, and vice versa
- Every reference is real and says what it is cited for — verify **Almeida et al. (2002)** and **Shaamala (2024)** directly, as both are load-bearing (CA formulation and objective-function form respectively) and both have open provenance questions (`p0`, "expander heuristic")
- Consistent style throughout; APA appears to be the current convention
- DOIs present where they exist — EarthArXiv readers expect them

## Glossary

Strong and worth keeping — unusual for a preprint but genuinely useful given the paper spans lattice theory, ACO, and tropical forestry. Two entries need updating after Methods corrections:

- **Gaussian Decay Model** — must match the corrected quadratic form (§2.3.2)
- Any Chebyshev-related entry — pending D-05

## Appendices

- **Appendix A** — Morphology Combinatorial Gallery, Figures A1–A28. Confirm all 28 are referenced in the main text; unreferenced figures draw comments. Confirm the gallery matches the current morphology presets rather than a superseded run.
- **Appendix B** — Documentation: consultation screenshots, ClickUp date plotting, QGIS rasterization of Caloocan People's Park, connectedpapers screenshots, initial 70 × 70 m heatmaps.

## ⚠️ Appendix B does not belong in a journal submission

Process documentation — advisor consultation photos, project-management screenshots, literature-search tooling — is standard for a school capstone and reads as unprofessional in a Q1 geoscience venue. It also creates two specific problems:

1. The **QGIS rasterization of Caloocan People's Park** implies a real georeferenced study site. The manuscript's central scope claim is that it is synthetic and non-georeferenced (Flags #3, #10, #11). A reviewer who sees this will question the scope statement.
2. The **70 × 70 m initial heatmaps** are from the superseded `INITIALCODE` pipeline and do not correspond to the 100 × 100 m two-level grid described in Methods.

Recommend removing Appendix B entirely, or retaining only genuinely scientific content. Consultation records can be acknowledged in the Acknowledgements.

## Supplementary S1

Destination for the full §1.1 Theoretical Foundation (Flag #15). Create when the Introduction is condensed.

## Preprint-specific additions

- Data & code availability statement — required in practice for EarthArXiv; must name a repository. Cannot be honestly written until Flag #43 resolves.
- Author contributions (CRediT)
- Competing interests, funding
- Acknowledgements — advisor, institution
