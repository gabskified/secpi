# SECPI Normalization Fix (Item 2) & Statistical Test Recommendation (Item 4)

**From:** Mathematical Auditor #2
**Prepared for:** Research lead decision + Editor implementation
**Basis:** Web-searched precedent (UN HDI methodology, OECD/JRC composite-indicator handbook) + execution against `AuditedCode_1.py`

---

## ITEM 2 — Replace the theoretical-bounds normalization with the "goalposts" method

### The problem being solved

The current `normalize_secpi()` maps raw SECPI onto 0–5 using the formula's *theoretical* extremes (min = −1.0, max = 7.5). Those extremes are mathematically real but practically unreachable, which produces two defects:

- The no-intervention baseline (raw SECPI = 0) maps to **0.588**, not 0 — so the scale's zero point is meaningless.
- The best result achievable in the actual study (raw SECPI ≈ 3.5, measured across 500 random valid placements) maps to only **≈ 2.6/5.0** — so the entire study occupies the bottom half of the scale and the top ~48% is dead space.

### The fix: goalposts normalization (a.k.a. distance-to-frontier)

This is the standard, citable solution for exactly this problem. The UN Human Development Index uses it, and it is the recommended approach in the OECD/JRC *Handbook on Constructing Composite Indicators* for indices with fixed interpretable bounds. The method sets two policy-meaningful reference points — a **"natural zero"** (lower goalpost) and an **"aspirational target"** (upper goalpost) — rather than the formula's raw extremes:

$$SECPI_{norm} = 5 \times \frac{SECPI_{raw} - SECPI_{floor}}{SECPI_{ceiling} - SECPI_{floor}}$$

clamped to [0, 5] so that values at or below the floor read 0 and values at or above the ceiling read 5.

### Proposed goalpost values for SECPI

| Goalpost | Proposed value | Justification |
|---|---|---|
| **Floor (natural zero)** | `SECPI_raw = 0.0` | This is the no-intervention baseline — zero trees. It is the meaningful "natural zero" of the index: any real intervention should score above it. Setting the floor here means the normalized scale reads **0 = do nothing**, which is exactly the interpretable anchor the manuscript's 0–5 presentation implies. |
| **Ceiling (aspirational target)** | `SECPI_raw = 3.75` | Set slightly above the best value observed across 500 random valid placements (measured max = 3.52) and above the ACO-optimizer's practical reach. This makes 5.0 a genuine "aspirational frontier" — reachable only by near-optimal placement — while keeping realistic strong results in the upper-middle of the scale rather than the bottom. Round to 3.75 for a clean, pre-registered constant. |

**Note:** the ceiling is a *design decision*, not a measured constant. I measured the empirical max (3.52 across 500 random trials) so you can set it defensibly, but you should confirm 3.75 against the ACO's optimized best once Results are regenerated under Option B. If the optimizer routinely exceeds 3.75, raise the ceiling so that near-optimal solutions don't all pin at 5.0 (which would lose discrimination at the top). The HDI literature frames this exact choice as "satiation point vs. highest achievable" — either framing is defensible as long as it's stated.

### What this produces (using floor=0.0, ceiling=3.75)

| Scenario | raw SECPI | normalized (goalposts) | normalized (old, theoretical bounds) |
|---|---|---|---|
| No intervention (baseline) | 0.000 | **0.00** | 0.588 |
| Weak (1 tree, worst species) | 1.919 | **2.56** | 1.717 |
| Strong (6 trees, best species) | 2.969 | **3.96** | 2.335 |
| Best observed (500 random) | 3.519 | **4.69** | 2.658 |

The goalposts version uses the full 0–5 range, anchors 0 to "do nothing," and reserves 5 for near-optimal — which is what a reader expects from a 0–5 index.

### Citable precedent (for the Methods section)

- UNDP Human Development Report Technical Notes — goalposts as "natural zeros and aspirational targets."
- OECD/JRC (2008), *Handbook on Constructing Composite Indicators: Methodology and User Guide* — the standard reference for min-max and goalposts normalization in composite indices.
- The "distance-to-frontier" framing is also used by the World Bank Doing Business index and the European Skills Index — additional precedent if a reviewer questions the choice.

### Code change required

`normalize_secpi()` currently divides by the theoretical range (`−1.0` to `7.5`). It would be changed to divide by the goalpost range (`0.0` to `3.75`) with a clamp to [0, 5]. This is a one-method change, still a pure reporting-layer transform (the ACO continues to optimize on raw SECPI). **I have not made this change yet** — it should be applied only after you confirm the ceiling value, ideally against the regenerated Option-B optimizer results.

### One decision I need from you

Confirm the **ceiling value**. My recommendation is 3.75 (just above observed random max), to be re-checked against the ACO's optimized best once Results are regenerated. If you'd prefer to anchor the ceiling to the theoretical satiation point instead of an empirical frontier, that's also defensible — but tell me which framing you want so the Methods text is internally consistent.

---

## ITEM 4 — Statistical test for the "redirection of resources" claim

### The problem being solved

The manuscript (§2.5.2) claims a "statistically significant redirection of resources" toward high-vulnerability zones when vulnerable cells are included, but specifies no test, no sample size, and no p-value. A reviewer cannot evaluate or reproduce this. It must either be backed by a real test or softened to a descriptive claim.

### Recommended test

The natural comparison is **WITH-vulnerable vs. WITHOUT-vulnerable** on a per-run outcome, across the study's existing replicate structure. The cleanest framing:

**Primary test — Wilcoxon signed-rank test (paired, non-parametric):**

- **Pairing:** for each configuration (each of k=1…6, run on the *same* underlying grid), compute the outcome metric under WITH-vulnerable and under WITHOUT-vulnerable. These are naturally paired because they share the grid and k.
- **Outcome metric:** the proportion of delivered cooling (or trees) that lands in high-vulnerability zones — this is the quantity the "redirection" claim is actually about. Do **not** use SECPI itself as the outcome, because SECPI is *defined* to reward vulnerability weighting, so testing SECPI would be circular. Use a placement-based metric that is independent of the objective function.
- **Why Wilcoxon signed-rank rather than paired t-test:** SECPI-derived proportions across a small number of configurations are unlikely to be normally distributed, and n is small. The signed-rank test is the standard non-parametric paired test and is defensible for n in this range.

### Sample size

You have two independent sources of replication; use whichever gives adequate n, or combine:

1. **The k-sweep:** k = 1…6 gives **6 paired observations**. This is the minimum defensible n for a Wilcoxon signed-rank test (the test can technically run at n=6, but power is low and the smallest possible two-sided p-value at n=6 is ~0.03, so a null result would be uninformative).

2. **The existing per-k replication:** the code already runs `n_runs=5` optimization restarts per k (see `run_optimization_for_k(..., n_runs=5)`). Using each restart as a replicate gives **6 × 5 = 30 paired observations**, which is comfortably adequate for the signed-rank test and gives real power.

**Recommendation:** use the **30-observation version** (6 k-values × 5 restarts), pairing each WITH run against the corresponding WITHOUT run on the same grid/seed. Report: test name, n = 30, the test statistic, the two-sided p-value, and an effect-size measure (matched-pairs rank-biserial correlation, which is the standard effect size for Wilcoxon signed-rank).

### If the test comes back non-significant

Then the manuscript claim must be **softened to descriptive**, e.g.: *"A greater share of cooling benefit was allocated to high-vulnerability zones under the vulnerability-weighted objective (median X% vs. Y%),"* with no significance language. Do not report "statistically significant" unless the test actually supports it.

### One decision I need from you

Confirm the **outcome metric**. My recommendation is "proportion of delivered cooling in V-zones" (independent of SECPI, avoids circularity). If you'd rather test "proportion of *trees* placed adjacent to V-zones," that's also valid and arguably more direct — but pick one, pre-specify it, and don't test both and report the better one (that's p-hacking a reviewer will catch).

---

## Summary of what's now pending

| Item | My output | What I still need from you |
|---|---|---|
| 2 — Normalization | Goalposts method, floor=0.0, ceiling≈3.75, with HDI/OECD precedent | Confirm ceiling value (re-check vs. optimized Results) |
| 4 — Statistical test | Wilcoxon signed-rank, paired, n=30, on a non-SECPI placement metric | Confirm the outcome metric (cooling-in-V vs. trees-near-V) |
| 3 — `p0` provenance | Deriver directive written (separate file) | Nothing — routed to Deriver |
