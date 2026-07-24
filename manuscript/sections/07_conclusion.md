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

<!-- PASTE CURRENT CONCLUSION BELOW -->
