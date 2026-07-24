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

<!-- PASTE CURRENT §2.5–§2.6 BELOW -->
