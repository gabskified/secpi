# DECISIONS.md — Research-Lead Sign-Off Queue

Everything below is a decision only the **research lead** can make. No agent may guess, default, or proceed past a blocked item. When a decision is made, record it here with a date, then append the corresponding entry to `PROJECT_LOG.md`.

Status vocabulary: `OPEN` · `DECIDED` · `SUPERSEDED`

---

## D-01 — SECPI classification scheme — **DECIDED**

**Decision:** Option B — fixed study-wide reference cutoffs.
**Date:** Project Log Entry 2 session (2026-07-19).
**Consequences:** (a) Methods §2.4 must be rewritten away from "self-normalizing per scenario"; (b) all existing Results numbers are void and must be regenerated; (c) the Editor authors the new Results. Code already implements this — no code change required.

---

## D-02 — Normalization goalpost ceiling — **DECIDED**

> ### ✅ DECIDED 2026-07-26 by the research lead
>
> **Ceiling = 3.75.** Floor = 0.0. `SECPI_norm = 5 × (SECPI_raw − 0) / (3.75 − 0)`, clamped to [0, 5].
>
> **Framing:** present the ceiling as a **pre-specified design constant**, consistent with every verified precedent (UNDP HDI fixed goalposts; OECD/JRC 2008; Cedefop European Skills Index). **Do not cite World Bank "distance to frontier"** — Doing Business was discontinued in September 2021 following a data-integrity investigation.
>
> **⚠️ Standing re-check obligation.** 3.75 was set just above the empirical max of **3.52** from 500 *random* valid placements. The ACO optimizes harder than random sampling, so 3.52 is a weak lower bound. **After the Option-B regeneration, compare the optimizer's best raw SECPI against 3.75.** If solutions routinely approach or exceed it, near-optimal configurations all pin at 5.0 and discrimination is lost exactly where the headline results live — raise the ceiling before the Editor writes any Results prose. Owner: `code-stressor` to report the max; the research lead to re-confirm or raise.
>
> **Code impact:** `normalize_secpi()` only — reporting layer. The ACO continues to optimize on raw SECPI. **Not yet applied.**

**Question (original, for the record):** Confirm the upper goalpost for the 0–5 SECPI presentation scale.

**Context.** The original scheme normalized against *theoretical* extrema (raw min −1.0, max 7.5). This is mathematically valid but practically useless: the no-intervention baseline maps to **0.588**, not 0, and realistic study outcomes occupy only the bottom ~35% of the scale.

> Correction of record: Project Log Entry 1 stated this baseline as **2.94**. That is wrong — it double-applied the 5× factor. The correct value is **0.5882**, confirmed by arithmetic, by the code's own docstring, and by direct execution of `AntColonySystemACO.normalize_secpi(0.0)`. Do not propagate 2.94 anywhere.

**Proposal on the table:** goalposts / distance-to-frontier normalization.

> **⚠️ Citation list corrected 2026-07-25 (Entry 3, Deriver).** All four candidate precedents were independently verified:
> - **UNDP HDI goalposts** — ✅ verified. Fixed-goalpost method introduced HDR 2010; cite the specific HDR edition whose values are used.
> - **OECD/JRC (2008) Handbook** — ✅ verified complete. ISBN 978-92-64-04345-9, DOI 10.1787/9789264043466-en. Authors: Nardo, Saisana, Saltelli, Tarantola, Hoffman & Giovannini.
> - **World Bank "distance to frontier"** — ⚠️ **DO NOT CITE.** Real and methodologically sound, but Doing Business was **discontinued in September 2021 following a data-integrity investigation**. Citing a discredited index as precedent for your normalization scheme invites the exact scrutiny you want to avoid.
> - **Cedefop European Skills Index** — ✅ verified, **preferred substitute**. Min-max 0–100, "distance to the ideal," still active, never discredited.
>
> Also recommended: Klugman, Rodríguez & Choi (2011), *J. Economic Inequality* 9(2), 249–288 — **DOI/pages not independently verified, needs a 10-second check.**
>
> Method-fit note: in all verified precedents the frontier is a **fixed, pre-registered goalpost**. Present the ceiling explicitly as a pre-specified design constant.

`SECPI_norm = 5 × (SECPI_raw − floor) / (ceiling − floor)`, clamped to [0, 5].

- **Floor = 0.0** (no-intervention baseline → normalized 0). Recommended, uncontroversial.
- **Ceiling = 3.75** *(proposed)*. Set just above the empirical max of **3.52** measured across 500 random valid placements.

| Scenario | raw | goalposts (0→3.75) | old theoretical (−1→7.5) |
|---|---|---|---|
| No intervention | 0.000 | 0.00 | 0.588 |
| Weak (1 tree, worst species) | 1.919 | 2.56 | 1.717 |
| Strong (6 trees, best species) | 2.969 | 3.96 | 2.335 |
| Best observed (500 random) | 3.519 | 4.69 | 2.658 |

**What the lead must confirm:** the ceiling value, and the *framing* (empirical frontier vs. theoretical satiation point) so Methods prose is internally consistent. Re-check against the ACO's optimized best once Option-B Results are regenerated — if the optimizer routinely exceeds the ceiling, raise it or near-optimal solutions all pin at 5.0 and discrimination is lost at the top.

**Code impact:** one method (`normalize_secpi()`), reporting layer only — the ACO continues to optimize on raw SECPI. **Not yet applied.**

---

## D-03 — Statistical test outcome metric — **DECIDED**

> ### ✅ DECIDED 2026-07-26 by the research lead — **report BOTH metrics, pre-specified, with multiplicity correction**
>
> This **supersedes** the earlier "pre-specify one, do not test both" guidance in the body below. That guidance was aimed at the *test-both-report-the-winner* failure mode. The design adopted here forecloses that failure mode explicitly and is stronger than a single-metric design, because a divergence between the two metrics is itself an informative result.
>
> **Two pre-specified hypotheses**, both SECPI-independent (so both satisfy Flag #69's circularity objection):
>
> | | Hypothesis | Outcome metric |
> |---|---|---|
> | **H1** | Cooling delivered is redirected toward vulnerable zones | Proportion of **delivered cooling** landing in V-zones |
> | **H2** | Tree placement is redirected toward vulnerable zones | Proportion of **trees placed adjacent** to V-zones |
>
> **Test:** paired **Wilcoxon signed-rank**, WITH-vulnerable vs WITHOUT-vulnerable, paired on shared grid and tree count. **n = 30** (`k` = 1…6 tree counts × 5 restarts per `k`). *(Note: under D-07's notation this pairing axis remains `k` — tree count — so the design is unaffected by the rename.)*
>
> **Report for each:** test name, n, statistic, two-sided p, and matched-pairs rank-biserial correlation as effect size.
>
> **Four binding conditions, all set by the research lead:**
>
> 1. **Both results are reported regardless of outcome.** If H1 is significant and H2 is not, both go in the paper. Reporting only the one that "worked" is the exact practice this design exists to prevent.
> 2. **Both hypotheses are pre-specified in Methods before the test runs**, stated as two named hypotheses — not selected post-hoc after inspecting results.
> 3. **The "redirection of resources" claim is scoped to match the outcome.** Both significant → the claim may stay broad. Only one significant → the claim narrows to whichever held, e.g. *"a greater proportion of trees were redirected to V-zones, though the cooling delivered did not differ significantly"* (or the converse). Neither significant → descriptive language only, no significance wording, and this outcome **must not be reframed**.
> 4. **Multiplicity correction: Holm–Bonferroni, FWER = 0.05.** ~~Bonferroni, α = 0.025 per test.~~ — **amended 2026-07-26 by the research lead, same session.** Rationale: the two metrics are strongly correlated (trees adjacent to V-zones is largely *the mechanism by which* cooling reaches V-zones), which makes plain Bonferroni conservative and costs power unnecessarily. Holm is uniformly more powerful for two tests and equally standard.
>
> ### The Holm–Bonferroni procedure, written out — apply exactly this
>
> Step-down, two hypotheses, family-wise error rate 0.05. **This is a pre-specified procedure and must not be altered after seeing the p-values.**
>
> 1. Compute both raw two-sided p-values, `p_H1` and `p_H2`.
> 2. Order them ascending: `p_(1) ≤ p_(2)`.
> 3. **Compare `p_(1)` against α / 2 = 0.025.** If `p_(1) > 0.025`, **stop — neither hypothesis is rejected.** Do not test the second.
> 4. If `p_(1) ≤ 0.025`, reject that hypothesis, then **compare `p_(2)` against α / 1 = 0.05.** Reject if `p_(2) ≤ 0.05`.
>
> **Note the step-down gate in step 3:** if the *smaller* p-value fails at 0.025, the larger one is never tested, regardless of its value. This is what makes Holm a valid FWER procedure rather than two independent tests.
>
> **Report:** both **raw** p-values, the Holm-adjusted decision for each, and the effect size for each — whether or not either is rejected. Naming the procedure as "Holm–Bonferroni (m = 2, FWER = 0.05)" in Methods is required; "corrected for multiple comparisons" is not sufficient.
>
> **Owners:** `editor` writes the two hypotheses into Methods §2.5.2 **before** execution; `code-stressor` executes both tests once D-07's notation and the Option-B regeneration are in place; `editor` writes the result with the claim scoped per condition 3.
>
> **Flags this bears on:** #39, #69, #70. Note that #70's "significantly" sweep is **not** discharged by this decision — every instance of significance language not backed by these two tests must still be removed manuscript-wide.

**Question (original, for the record):** Pre-specify the single outcome metric for the "statistically significant redirection of resources" claim in §2.5.2.

**Context.** The manuscript asserts significance with no test, no n, no p-value. A reviewer will reject this on sight.

**Recommended design:** paired **Wilcoxon signed-rank** test, WITH-vulnerable vs. WITHOUT-vulnerable, paired on shared grid and k. **n = 30** (k = 1…6 × 5 existing restarts per k). Report: test name, n, statistic, two-sided p, and matched-pairs rank-biserial correlation as effect size.

**The choice:**
- (a) *proportion of delivered cooling landing in V-zones* — **recommended**, independent of SECPI, avoids circularity; or
- (b) *proportion of trees placed adjacent to V-zones* — also valid, arguably more direct.

**Do not test both and report the better one.** Pre-specify one. That is p-hacking and a reviewer will catch it.

**If non-significant:** the claim softens to descriptive ("a greater share of cooling benefit was allocated to high-vulnerability zones under the vulnerability-weighted objective, median X% vs. Y%"), with no significance language. This outcome is acceptable and must not be reframed.

---

## D-04 — Final title — **OPEN**

Two titles are on record. Confirm which is final before DOI minting, since the DOI landing page title is effectively permanent.

1. Current manuscript: *"Mapping Synergistic and Equitable Urban Cooling (SECPI) of Philippine Tree Functional Types: A Discrete Grid Optimization Grounded in Integer Lattice Theory"*
2. Flag #10 revision: *"A Generalizable Framework for Synergistic and Equitable Cooling Optimization of Philippine Tree Functional Types via Discrete Grid Modeling"*

Flag #10's objection stands: "Mapping" implies literal geographic mapping and conflicts with the synthetic, non-georeferenced design.

---

## D-05 — "Chebyshev space (ℤ²)" terminology — **OPEN**

Confirmed: cooling decay genuinely uses **Euclidean** distance. The old V-zone buffer used Manhattan distance — now moot, since V-zone generation was rewritten as BFS using neither.

**What's left:** is "Chebyshev space (ℤ²)" intended as a general lattice/indexing convention distinct from any physical distance calculation, or is it simply an error to delete? Author/Editor clarification only — no code work remains. (Flag #37.)

---

## D-06 — Recover or retire the combinatorial species analysis — **SOURCE LOCATED — OUTCOME (b) CONFIRMED**

> **Update 2026-07-25:** **The output data has been found and verified.**
> `legacy/archive/corrected_outputs/run_20260213_222844/combinatorial/` contains `all_combos_with_vuln.csv` (63 data rows + header), `all_combos_without_vuln.csv`, and `combinatorial_summary.json`.
>
> **Verbatim matches to the manuscript's §3.1:**
> - `combo_id 6, k=1, Akleng-parang, secpi 4.3916, rank 3` — the manuscript's "4.3916 (rank 3/63)"
> - `k1_Nar_SECPI_4.386.png` — the manuscript's mono-Narra 4.3856
> - 0.03% diversity figure = (4.393 − 4.3916)/4.3916 = **0.0319%** ✓
> - 28% cliff = (4.3916 − 3.13)/4.3916 = **28.73%** ✓
>
> **Classified outcome (b): reproducible AND superseded.** The run is dated 2026-02-13, five months before the Entry 1/Entry 2 audits (2026-07-19). Confirming evidence: every WITHOUT_VULN value is 1.500, 1.501, or 1.750 — the retired `WITHOUT_VULN = 1.5` constant of the self-normalizing scheme superseded by D-01. §3.1 must be regenerated under Option B; magnitudes will change.
>
> **Still unknown:** which script generated it. Candidates in `legacy/archive/`: `CA.py`, `CODE020526.py`, `GEMINI.py`, `dashboard.py`, `secpi_main.py`, plus `dashboard.ipynb` and `explore.ipynb`. Session 4 still owns this, but it is now a provenance question, not an existence question.

### 🔴 The finding that matters more than the recovery — Flag #46

The CSV carries three columns the manuscript never reports: **`species_available`**, **`species_actually_used`**, **`all_available_used`**.

| rank | k (available) | actually used | SECPI |
|---|---|---|---|
| 1 | 6 | **2** (Narra + Talisay) | 4.393 |
| 2 | 4 | **1** (Akleng-parang) | 4.3924 |
| 3 | 1 | 1 | 4.3916 |
| 4 | 5 | **3** | 4.3912 |

`aco_used_all_available_pct`: **30.16%** WITH vulnerability, **19.05%** WITHOUT. The optimizer declined to use the full palette in ~70% and ~81% of configurations respectively.

**Therefore `k` in §3.1 is the size of the offered palette, not the number of species planted.** The 0.03% comparison is "offered six vs offered one" — and when offered six, the optimizer planted two.

The manuscript's claim that functional diversity offers negligible benefit is **not what this data shows**. What it shows:

> Given a larger species palette, the optimizer converges to the same small set of high-performing species regardless of palette size.

This is a different claim, better supported, and currently unclaimed. The existing phrasing asserts something the data cannot carry. **Reframing §3.1, the Abstract, and the Conclusion is mandatory, not optional** — the `species_actually_used` column is the first thing a reviewer will notice.

### What survives intact

The **28% cliff is robust and now mechanistically explained.** At k=1 the six species split cleanly bimodal, gap of **1.280**:

Akleng-parang 4.392 · Narra 4.386 ‖ Talisay 3.106 · Kabiki 3.094 · Banaba 3.068 · Duhat 3.040

Two species carry the result. The 3.13 threshold sits just above the lower cluster. Magnitudes shift under Option B renormalization; the structure does not.

### Flag #47 — WITHOUT_VULN degeneracy

The without-vulnerability scenario produced **three distinct SECPI values across 63 configurations** (1.500, 1.501, 1.750) — near-total loss of discrimination, suggesting saturation or clamping. Combined with `aco_used_all_available_pct` = 19.05%, that arm of the analysis looks close to degenerate. Not explained by any existing flag. Needs investigation before the WITHOUT/WITH comparison can be reported.

### Revised research-lead decisions

1. Confirm §3.1 will be regenerated under Option B (outcome (b) requires it).
2. **Confirm the reframing of the diversity claim** per Flag #46 — this changes what the paper argues.
3. Decide whether `species_actually_used` becomes a reported variable in the new Results. Recommended: yes; it is the most interesting thing in the dataset.

### Original question, for the record

**Does the script that produced Results §3.1 still exist anywhere?** — Output: yes, verified. Script: pending Session 4.

### ⚠️ The trap: reproducing the numbers does not validate them

There are **three** outcomes here, not two, and the middle one is both the most likely and the easiest to miss.

| Outcome | Meaning | Consequence |
|---|---|---|
| **(a)** Script found, **post-audit** | Contains the Entry 1 + Entry 2 fixes | §3.1's numbers stand. Port to `src/secpi/analysis/combinatorial.py`. Best case. |
| **(b)** Script found, **pre-audit** | Reproduces the published numbers, but from code containing the bugs later fixed | **The numbers are reproducible and wrong.** §3.1 must be regenerated with the corrected implementation. Expect different values. |
| **(c)** No script reproduces §3.1 | — | Reconstruct from `species_subset`; numbers will differ; restate every dependent claim. |

**Outcome (b) is the likely one.** If the sweep had been run after the audits, it would live in `AuditedCode_1.py` — the auditors would have found it. Its absence suggests the sweep predates the audit cycle.

Bugs a pre-audit script would carry: the tie-inversion bug (degenerate all-zero cases misclassified), `SensitivityAnalyzer` hardcoded to 10 ants / 15 iterations instead of reading `base_aco_config`, the fabricated allometric sensitivity (`np.random.uniform(0.98, 1.02)`), the uncorrected CA transition formula, and the self-normalizing SECPI scheme superseded by D-01.

**Do not let "it reproduces the published numbers" be read as "the published numbers are correct."** Under (b) those two facts are perfectly compatible and both true.

### Triage protocol — follow in order

**Step 1 — Freeze before executing anything.**

Copy the entire old directory into `legacy/archive/` and record a manifest before running a single file. Chain of custody matters here; these files are evidence.

```powershell
New-Item -ItemType Directory -Force -Path "legacy\archive" | Out-Null
Copy-Item -Recurse "C:\path\to\old\directory\*" "legacy\archive\"

Get-ChildItem -Recurse "legacy\archive" -Filter *.py |
  Select-Object Name, Length, LastWriteTime,
    @{n='SHA256';e={(Get-FileHash $_.FullName -Algorithm SHA256).Hash}} |
  Format-Table -AutoSize |
  Out-File "legacy\archive\MANIFEST.md" -Encoding utf8

git add -A
git commit -m "D-06: archive recovered script iterations, unmodified"
```

Commit before running. If a script writes into its own directory on execution, you want the pristine state already in git.

**Step 2 — Inventory by signature, not by filename.** Filenames lie; imports don't. For each candidate record: does it import **and call** `itertools`? Is there a combinatorial class? Does it reference 63 subsets or six species? Grid dimensions? `n_trees`? Is a random seed set?

**Step 3 — Identify by target reproduction.** You have the published values, which makes this a solvable forensic problem. Run each candidate and compare against: **SECPI 4.3916** (rank 3/63), **4.3856** (rank 27/63), marginal deltas **0.6291** and **0.6283**, threshold **3.13**, the **~28%** cliff.

If no seed is set, exact reproduction may be impossible — compare distributions and rank orderings instead, and record that limitation.

**Step 4 — Date it against the audit boundary.** For the winning candidate, check for each Entry 1 and Entry 2 fix. Post-audit → outcome (a). Missing any → outcome (b), and §3.1 needs regeneration regardless of how cleanly it reproduces.

**Step 5 — Record the verdict** in `legacy/archive/MANIFEST.md` and a `PROJECT_LOG.md` entry, naming which file is canonical for §3.1 and which outcome applies.

### What the research lead must decide

1. Which recovered file is canonical for §3.1
2. If outcome (b): confirm §3.1 will be regenerated under the audited implementation, accepting that published values will change
3. If outcome (c): reconstruct, or scope §3.1 out of the preprint with a stated limitation

### Original question, for the record

**Does the script that produced Results §3.1 still exist anywhere?**

**Context.** §3.1 reports evaluation of all 63 unique subsets of the six TFTs, five trees per configuration. **No such code exists in `AuditedCode_1.py`** — no combinatorial class, `itertools` imported and never called, `species_subset` accepted but never passed, and no subset sweep among `main_revised_validation()`'s nine steps. The only combinatorial analyzer in project files is `ComprehensiveSpeciesAnalysis` in `INITIALCODE.md`, which is a different experiment entirely (31 combinations of five species, `n_trees=10`, 70 × 70 grid).

**What depends on this:** SECPI 4.3916 and 4.3856, ranks 3/63 and 27/63, marginal deltas 0.6291 and 0.6283, the 3.13 threshold, the ~28% performance cliff, the 0.03% diversity result. These appear in the Abstract, Results §3.1, and the Conclusion. They are the manuscript's headline findings.

**Where to look, in order:** local machines of any team member; Google Colab notebooks; earlier chats in the Claude Project; older commits or backups; email attachments. Check whether any team member ran the sweep as a one-off rather than as part of the main pipeline.

**Three outcomes:**

| Outcome | Consequence |
|---|---|
| Script recovered | Archive to `legacy/` immediately, verify it reproduces the published numbers from a fixed seed, then port to `src/secpi/analysis/combinatorial.py`. Best case. |
| Not recovered but reconstructible | `AntColonySystemACO` already accepts `species_subset`. A sweep is straightforward to write — but the regenerated numbers **will differ** from those published, and every dependent claim must be restated. |
| Not recoverable and not reconstructible in time | §3.1 and all dependent claims must be removed from the preprint. This would gut the paper's headline contribution. |

**Escalate to ROADBLOCK (SEVERE)** if the first two outcomes are exhausted. This would be the project's first.

**Answer this before spending any further effort on Results prose.** Nothing else in the Results pipeline matters if §3.1 cannot be sourced.

---

## D-07 — Meaning of `k` — **DECIDED**

> ### ✅ DECIDED 2026-07-26 by the research lead
>
> **`s` = species subset / available palette size. `k` = number of trees placed.**
>
> Apply consistently across Methods, Results, the figures, and the D-03 statistical design. The three-way collision (subset size / available palette size / tree count) collapses to two symbols on two orthogonal axes.
>
> **Consequences:**
> - **§3.1 becomes an `s`-axis experiment** (s = 1…6 palette sizes, trees fixed at five). Its `k` must be rewritten to `s` throughout, along with the Abstract and Conclusion references to it.
> - **D-03's pairing axis remains `k`** (tree count 1…6 × 5 restarts, n = 30). The rename does not alter the statistical design.
> - **Flag #64 is a numbering-independent defect and is NOT closed by this decision.** §3.4.1's per-`k` means (2.990–3.017) are arithmetically incompatible with the same dataset's individual values regardless of what the symbol is called. §3.4.1 must still be **regenerated, not rewritten**.
> - **Flag #44 downgrade is not automatic** — the notation fix removes the ambiguity, but the flag also covers the interleaving of two incommensurable experiments in one Results narrative. `editorial-flagger` to reassess after regeneration.
>
> **Owner:** `editor` applies the notation once Results regenerate; do not apply it to prose that is about to be regenerated anyway.

**Question (original, for the record):** disambiguate `k`.

`k` denotes species subset size in §3.1 (k=1 mono-species → k=6 full palette, trees fixed at five) and number of trees placed in the code, in `SuboptimalScenariosGenerator`, and in the D-03 Wilcoxon pairing design. Two orthogonal experimental axes, one symbol.

Pick distinct notation — e.g. `s` for subset size, `k` for tree count — and apply it consistently across Methods, Results, and the statistical design. **Settle before any Results prose is written**, or D-03's test will be misread as testing something it does not test.

---

## Decision dependency chain

```
D-06 (recover §3.1 code) ──→ §3.1 survives? ──→ Abstract & Conclusion headline claims survive?
                                 │
D-02 ✔ (ceiling) ─┐              │
                  ├─→ regenerate Results under Option B ─→ Editor writes Results ─→ Abstract rewrite ─→ preprint
D-03 ✔ (metric) ──┤              │
D-07 ✔ (k/s notation) ───────────┘
D-01 ✔ ───────────┘
D-04 ──────────────────────────────────────────────────────────────────────────→ DOI minting

§3.5 sub-path (D-11, amended 2026-07-27):

D-12 ✔ (state-leak fix) ──┐
#75 (three-way: Morris / repaired OAT / as-run) ──┤
#77 (n_samples design) ───┴──→ D-11 §3.5 regeneration ──→ Editor writes §3.5.2 + Fig 34
                                                     └──→ #82 remedy · #89 · Fig 34
D-13 (§3.5 provenance) ──→ can §3.5's published numbers be sourced at all?
```

**Neither D-02 nor D-03 blocks *running* the pipeline.** Both block *writing the numbers up*. All four Results-path decisions (D-01, D-02, D-03, D-07) are now settled.

**The §3.5 sub-path is the live bottleneck.** D-12 is authorized but **not yet applied**; #75 needs a research-lead answer that is now three-way; #77 needs a disposition. D-13 runs alongside and does not gate the regeneration — but until it is answered, no §3.5 number in the manuscript has a known provenance.

---

## D-08 — Assumed species heights are outside observed range — **OPEN — new, from Entry 3**

**Separate from Flag #30 and arguably more serious.** Independent of which H–D constants are used, the manuscript's *assumed heights* extrapolate far beyond any calibration range:

| Species | Manuscript assumes | Observed max (NPDC, n=211) | Inverted DBH at assumed height |
|---|---|---|---|
| Narra | 30 m | **21.58 m** | **244.5 cm** — above documented species max (~200 cm), and 2× the largest tree in a 161-tree inventory |
| Talisay | 35 m | **15.77 m** | far beyond range |
| Banaba | — | 11.77 m | — |

Entry 3 recommends re-anchoring to realistic urban values: **Narra ~18–21 m, Talisay ~13–15 m, Banaba ~10–12 m**. The current figures appear to be species *maxima* from profile literature, not urban open-grown typicals.

**Decision needed:** re-anchor assumed heights, or retain species-maxima and disclose that the H–D inversion extrapolates beyond calibration. Affects every downstream cooling calculation via crown geometry.

---

## D-09 — Path X (hardcoded LAI canonical) — **DECIDED (recorded in Entry 3)**

**Decision:** Hardcoded LAI values remain canonical for all results. The allometric chain stays **sensitivity-only**, disclosed as author-estimated.

**Rationale:** Path Y (computed-LAI canonical) was ruled out because no valid leaf-area constants exist for these six species. Entry 3 confirmed no direct or genus-level precedent for an `LAI = l0·DBH^l1` power law after two dedicated search rounds, and identified a conceptual mismatch — urban-forestry standards (Nowak 1996 / i-Tree Eco; Peper & McPherson) predict leaf *area* (m², extensive) from DBH, whereas LAI is leaf area per unit ground area (intensive).

The hardcoded values (3.15–6.07) are **physically plausible**, sitting inside measured tropical/urban canopy LAI (~3–6.5). No species-specific source exists; §2.2's DENR-ERDB / UPLB-CFNR / Abino et al. (2014) citation covers **morphology, not LAI** — do not present it as sourcing LAI.

**If revisited later (Path Y-prime):** predict leaf area or intra-crown LAI (*sensu* Nock et al. 2008) from **crown projection area**, which the model already computes — bypassing the height→DBH chain entirely. This is the methodologically defensible route.

---

## D-10 — `p0` disposition — **RECOMMENDATION READY, needs sign-off (Entry 3)**

Entry 3 settled the provenance question: **no Almeida initial-condition convention exists.** Almeida et al. (2002/2003) uses weights-of-evidence (Bayesian) transition probabilities computed from spatial evidence each iteration — not propagated recursively. The only initial condition is the observed land-use map. Uniform initialization is **not** a citable convention for this model class; it is defensible only as a generic non-informative default (principle of indifference), which is a statistical argument, not CA-methodology precedent.

**Key finding:** `p0` **cannot** collapse into `p_init` (seed density vs. per-cell probability — different quantities), **but is redundant with γ**. In the first update `p(1) = γ·ω·p0`, so both act as multiplicative scale factors and are not separately identifiable.

**Recommendation: fix `p0 = 1.0` and let γ absorb the calibration.** This removes the undocumented parameter and leaves exactly the two manuscript-named parameters. Needs research-lead sign-off; touches `grid.py` / CA generation.

**Citation hygiene:** "Almeida et al., 2002" is ambiguous — confirm whether CASA Working Paper 42 (UCL) or the Buenos Aires ISRSE proceedings. The full journal version is **de Almeida et al. (2003), *Computers, Environment and Urban Systems* 27(5), 481–509**. Cite Almeida for the *framework only*; present the multiplicative rule + p0/γ as the team's own adaptation.

---

## D-11 — §3.5 Sensitivity Analysis regeneration scope — **DECIDED**

> ### ✅ DECIDED 2026-07-26 by the research lead — **option (b), full §3.5 regeneration under Option B**
>
> Opened and decided the same day. Re-run the parameter sweep **and** the aggregation together — not the aggregation alone.
>
> **Why (b) and not (a):** the existing sweep predates Option B (D-01), so its SECPI values are void under the same reasoning that voided every other Results number. Aggregation-only regeneration would produce correct arithmetic over obsolete inputs — a second wrong table, arrived at more carefully.
>
> **⚠️ Prerequisite — #75 must settle first.** Methods §2.5.3 names the **Morris method**; §3.5.1 executes a **local two-level OAT** sweep from a single baseline. These are different methods. Regenerating before that is resolved reproduces the mismatch in fresh numbers and wastes the run. Settle whether the intended method is Morris (in which case the sweep design changes) or local OAT (in which case §2.5.3 is corrected).
>
> **Also settle before running — #77:** the sweep averaged over **three** ACO runs where the project standard is `n_runs = 5`. Fix the restart count in the same pass.
>
> **Required output — a machine-written per-parameter table**, one row per swept parameter: `parameter · category · low_bound · high_bound · SECPI_low · SECPI_high · SI · n · SD`. Category aggregates are computed **from that table**, never hand-entered. Emitted to a single named run directory in `results/`.
>
> **Owners:** `code-stressor` regenerates and emits the table; `math-auditor` reports what the aggregation function in `SensitivityAnalyzer` actually computes — four uncorrelated overstatements point at a code defect rather than four transcription slips, and that diagnosis should not be skipped just because the numbers are being replaced; `editor` writes §3.5.2 and Figure 34 from the emitted table only.
>
> **Falls with §3.5.2 and regenerates alongside it:** Figure 34, and the Conclusion's "Sensitivity Index = 0.46" (**#89** — 0.4435 does not round to 0.46 at any precision).
>
> **Until the regeneration lands:** §3.5.2 must not be rewritten, and **no number from it may be quoted in the manuscript, the Abstract, or the Conclusion.**

### 🔄 AMENDED 2026-07-27 by the research lead — third prerequisite added; the #82 diagnosis is overturned

**The decision itself stands: option (b), full §3.5 regeneration under Option B.** What changes is what must be true before it runs, and what it can be expected to achieve. Source: **Project Log Entry 8** (`math-auditor`, execution audit, commit `0e912d1`). Nothing above is deleted — read it, then read this.

**1. A third prerequisite, and it is now the binding one.**

D-11 as written names two prerequisites, #75 and #77. There is a third: **the `SensitivityAnalyzer` state leak registered by Entry 8 §D and authorized for repair under D-12.** `_run_single_evaluation` mutates the class-level `TreeSpecies.SPECIES_DATA` at `legacy/AuditedCode_1.py:880,882` and never restores it, so every evaluation after the first `Species_Morphology` parameter runs against contaminated species data. Measured cost: allometric sensitivity **inflated 1.84×**, morphological **deflated 0.63×**.

**Do not run the regeneration before D-12's fix lands.** Doing so burns the run producing a fourth invalid table. This prerequisite is unlike #75 and #77 in kind — those are description questions, this is a code defect — and it is the only one of the three that required a fresh authorization.

**2. The premise this decision was argued from is refuted. The conclusion survives anyway.**

D-11's body above, and Entry 7, both record the working hypothesis that *"four uncorrelated overstatements point at a code defect rather than four transcription slips"* in the aggregation step — and D-11 assigned `math-auditor` to diagnose it on exactly that reasoning. **Entry 8 executed it and the aggregation is innocent.** `groupby().agg(['mean','max','sum','count'])` computes a true arithmetic mean; the pandas 3.0.0 column order matches the hardcoded rename at line 1036; **0 violations of `mean ≤ max` across 2,000 randomized trials**; and a real 243-evaluation sweep produced `mean ≤ max` in all four categories.

That `math-auditor` assignment is therefore **discharged** — do not re-run it.

**3. What the regeneration will and will not do — corrected expectation.**

Executed against published, from a real 243-evaluation sweep at production config:

| Category | n | Executed mean | Published mean |
|---|---|---|---|
| Species_Morphology | 12 | 0.006593 | 1.3068 |
| Species_Allometry | 24 | 0.012433 | 0.1857 |
| Cooling_Model | 3 | 0.059809 | 0.0727 |
| Weighting | 1 | 0.001385 | 0.0236 |

Weighting settles it: n = 1, so mean = max = sum = 0.001385, and the published 0.0236 equals none of the three. **The published category means did not come from this code.** Consequently the regeneration will **neither reproduce nor vindicate §3.5** — it will emit a clean, internally consistent table that simply has no relationship to what is printed in the manuscript. That is a weaker reassurance than "the defect is fixed," and §3.5's prose must be regenerated on that understanding, not reconciled against the old numbers.

**4. §3.5 does not survive qualitatively either — expect a rewrite, not an adjustment.**

With the leak repaired, the manuscript's rank-1 parameter (Narra crown diameter) ranks **28 / 40** at SI 0.002245. The executed rank-1 is `decay_lambda` at SI **0.1697** — the parameter §3.5.2 dismisses as *"limited impact (0.0015)"* — larger than the next index by 3.8×. The category hierarchy is inverted. **And the sign is inverted:** forcing the manuscript's own 12 → 34 m bounds through the code gives SECPI 3.213 → 2.855, a *decrease* of effect 0.358, against the published 3.024 → 4.380, an *increase* of effect 1.356.

**5. A reporting requirement the current implementation cannot satisfy.**

D-11's required output table specifies `n` and `SD` columns. Entry 8 confirmed by execution that **no dispersion statistic is computed or stored anywhere** — `low_scores`/`high_scores` are collapsed by `np.mean` at lines 997–998 and discarded — so SD cannot be recovered from the existing CSV. `code-stressor` must add it. This matters because the measured **SI noise floor is ≈ 0.0098 at `n_samples=3`**, and only 2 of 40 indices clear it: without dispersion, the regenerated ranking is an ordering of noise.

**6. #75's prerequisite is now a three-way question, not a two-way one** — Morris, a repaired local OAT, or the contaminated sweep as-run. Entry 8 §A established that the code implements **neither** named method, so "which of the two did we mean" no longer has a true answer. This needs the research lead and is not yet a numbered decision.

**Owners, revised:** `code-stressor` applies D-12's fix, then regenerates and emits the table **including SD**; ~~`math-auditor` reports what the aggregation function computes~~ — **discharged, Entry 8 §C**; `editor` writes §3.5.2 and Figure 34 from the emitted table only.

**Scope caveat carried from Entry 8, binding on every magnitude quoted in this amendment:** those runs are one grid, one morphology, one seed, `n_samples=3`, with no D-02 ceiling applied and `normalize_secpi()` not exercised. They are **diagnostic, not the D-11 regeneration**, and **no number in this amendment may be quoted as a manuscript value.** The structural claims — evaluation counts, sweep bounds, category membership, aggregation semantics, the state leak — are deterministic and safe to assert; the magnitude and ranking claims are single-run observations that `code-stressor` owns replicating.

---

**Opened 2026-07-26 at the research lead's instruction, scoped to regeneration only.** Raised by the orchestrator. Source: **Flag #82 (ROADBLOCK — SEVERE)**, Project Log Entry 6.

**Question:** What is the regeneration scope for §3.5 — the aggregation layer alone, or the whole sensitivity analysis including the parameter sweep?

### ⚠️ Read this before considering any option

**"Relabel sum-vs-mean" is NOT an available remedy and must not be offered as one.** An earlier note in `docs/HANDOVER.md` proposed exactly that; it is arithmetically dead and has been withdrawn. Acting on it would replace one wrong number with another.

**Do not argue this defect from a `[0,1]` bound either.** SI is `|SECPI_high − SECPI_low| / SECPI_baseline` — a difference-to-baseline ratio, **not** bounded above by 1. It would legitimately exceed 1 if a parameter's effect exceeded the baseline SECPI. A bound-based objection is refutable and would let a reviewer dismiss a correct finding. **The sound argument is `mean ≤ max`.**

### The defect

All **four** of §3.5.2's category-level mean sensitivity indices exceed the maximum SI of their own member sets. Category membership is forced by §3.5.1's own definition (12 + 24 + 3 + 1 = 40, matching its stated "swept 40 parameters"):

| Category | n | Largest member (manuscript-printed) | Reported mean | Overstatement |
|---|---|---|---|---|
| Species Morphology | 12 | 0.4435 | **1.3068** | 2.95× its own largest member |
| Species Allometry | 24 | < 0.005 | **0.1857** | ≥ 37× the ceiling |
| Cooling Model *(duplicate-labelled)* | 3 | 0.0032 | **0.0727** | 22.7× |
| **Weighting** | **1** | **0.0017** | **0.0236** | **13.9×** |

**The Weighting row settles it in one line, with no assumptions:** the category has exactly one member — the shade–evapotranspiration weighting ratio — whose SI §3.5.2 itself prints as **0.0017** thirteen lines below giving the category a mean of **0.0236**. A one-element mean *is* that element.

The three benign explanations are all excluded: the overstatement factors (2.95 / 50.2 / 22.7 / 13.9) share **no common factor**, so no single mis-scaling produces them; and they are not sums (Weighting's sum is 0.0017; Cooling Model's is 0.0068 vs 0.0727). The sentence also contradicts itself — it says removing Narra CD would drop the category mean to "approximately 0.002," which implies a starting mean near 0.039, not 1.3068.

**Diagnosis, not mitigation:** §3.5.1's *parameter-level* values reproduce cleanly (1.356 / 3.0576 = 0.4435 ✓; 0.0045 × 3.0576 ≈ 0.014 ✓). The defect **localizes to the aggregation step and Figure 34**. Four uncorrelated overstatements are more consistent with a code defect in `SensitivityAnalyzer` than with four transcription slips.

### The options

- **(a) Aggregation-only regeneration.** Recompute category aggregates from the existing per-parameter sweep output. Cheapest. **Risk:** the existing sweep predates Option B (D-01), so its SECPI values are void under the same reasoning that voided all other Results numbers. This option produces correct arithmetic over obsolete inputs.
- **(b) Full §3.5 regeneration under Option B — *recommended*.** Re-run the parameter sweep and the aggregation together, emitting a machine-written per-parameter table (parameter, category, low/high bound, SECPI_low, SECPI_high, SI, n, SD) plus category aggregates computed from that table, from a single named run in `results/`. Consistent with how every other Results section must be handled.
- **(c) Scope §3.5 out of the preprint** with a stated limitation, and restore it for journal submission.

**Interacts with:** #75 (Methods §2.5.3 names the **Morris method**; §3.5.1 executes a local two-level OAT from one baseline — the stated and executed methods differ, and this must be settled *before* regenerating or the regeneration reproduces the mismatch) and #77 (the sweep averaged over **three** ACO runs where the project standard is `n_runs=5`).

**Also falls with §3.5.2:** Figure 34, and the Conclusion's "Sensitivity Index = 0.46" (**#89** — 0.4435 does not round to 0.46 at any precision).

**Owners once decided:** `code-stressor` regenerates; `math-auditor` reports what the aggregation function in `SensitivityAnalyzer` actually computes; `editor` writes §3.5.2 and Figure 34 from the emitted table only.

**Until this closes:** §3.5.2 must not be rewritten — it must be regenerated — and **no number from it may be quoted in the manuscript, the Abstract, or the Conclusion.**

---

## D-12 — Authorize the `SensitivityAnalyzer` state-leak fix — **DECIDED**

> ### ✅ AUTHORIZED 2026-07-27 by the research lead
>
> **Repair the leak. Snapshot `TreeSpecies.SPECIES_DATA` on entry to `SensitivityAnalyzer._run_single_evaluation` and restore it in a `finally`.**
>
> **Target — both, in the same pass** (research lead, 2026-07-27):
> 1. **`legacy/AuditedCode_1.py`** — the reference implementation. This is where the fix lands now and where D-11's regeneration will run.
> 2. **`src/secpi/`** — the modular port. ⚠️ **Stated plainly: `src/secpi/` is currently an empty directory — zero files** (verified this session). There is nothing to fix there today, so "both" resolves to a **binding carry-forward requirement**: the port must not be written without the snapshot/restore, and `MIGRATION.md` must carry that as an explicit acceptance criterion. Recorded here so the port cannot silently ship the defect the reference implementation just had removed.
>
> **This is the first authorized semantic change to `AuditedCode_1.py` in the project's history.** It is not a refactor and not a cleanup — it changes what the program computes.

**Question:** Entry 8 §D found that `_run_single_evaluation` mutates the class-level `TreeSpecies.SPECIES_DATA` and never restores it. The fix is small and local, but it is a semantic change to the reference implementation, so `math-auditor` declined to make it and routed it here.

### The defect, as verified by execution (Entry 8 §D1–D6)

- `TreeSpecies.SPECIES_DATA` is a **class attribute**, shared by every instance. `_run_single_evaluation` writes into it at `legacy/AuditedCode_1.py:880` and `:882` with no copy, no context manager, no `finally`.
- The mutation **escapes the evaluation.** After evaluating Narra's crown diameter at its high bound, a brand-new `TreeSpecies`, a brand-new `CorrectedCoolingModel` and a brand-new `SensitivityAnalyzer` all report 27.6 m against a base of 23.0 m.
- **The LAI path compounds geometrically** — line 879 reads current LAI, line 880 writes `current × ratio`. Six identical `Narra.l0 = 0.30` evaluations drove LAI **6.07 → 18.12**. The function is not idempotent, so the three repeats `n_samples=3` averages "to reduce stochastic noise" are three *different models*, not three samples of one.
- After a full 40-parameter sweep, **all six species** sit at high crown diameter and high height (last-write-wins), LAI drifted by up to **−37%** (Banaba 3.87 → 2.43).
- **Measured cost:** allometric sensitivity **inflated 1.84×**, morphological **deflated 0.63×**. The internal control is that `Cooling_Model` and `Weighting` are **bit-identical** between the leaked and repaired runs — they are evaluated before any species mutation — which is what isolates the divergence to the leak and nothing else.

### ⚠️ The blast radius is wider than §3.5, and Entry 8 did not state this

`main_revised_validation()` runs **STEP 7: Sensitivity Analysis** (call site line 3522–3529) and then **STEP 8: Morphological Robustness Validation** (line 3540) **in the same process**. STEP 8 constructs a fresh `MorphologicalRobustnessValidator` from `config`, which builds its own `TreeSpecies` — and Entry 8 §D2 proved by execution that a fresh `TreeSpecies` sees the contaminated class-level state.

**Therefore, in any single-process full pipeline run, STEP 8 begins with every species at its high crown diameter and high height.** That result feeds the Conclusion's morphological-robustness claim, which **#88** already flags as absent from §3 entirely.

**Provenance discipline on that claim:** the step ordering is verified **by reading** `AuditedCode_1.py:3517–3544`; the contamination mechanism is verified **by execution** in Entry 8 §D2. The *joint* conclusion — that STEP 8's outputs are contaminated in practice — is **inferred from those two, not executed**, and per `CLAUDE.md` §2 rule 2 it is not to be recorded as verified until someone runs it. **It needs its own flag number, to be assigned after the in-flight `editorial-flagger` pass lands** so it does not collide with #96/#97. Owner: `code-stressor`, as a before/after check in the same pass that applies this fix.

### ⚠️ Implementation note — a naive `SPECIES_DATA` restore is NOT sufficient

Verified this session by reading `legacy/AuditedCode_1.py:873–888` and `:1605–1632`. Entry 8 cites the mutation as "lines 880 and 882." There are in fact **four write points inside `_run_single_evaluation`**, and one of them has a consequence a dict-level restore does not reach:

| Line | Writes |
|---|---|
| 880 | `ts.SPECIES_DATA[species]['LAI'] = hardcoded_lai * ratio` — the compounding write |
| 882 | `ts.SPECIES_DATA[species][param_name] = value` |
| 885–886 | `ts.SPECIES_DATA[species]['CPA']` when `crown_diameter_m` changed |
| 888 | `ts._calculate_cpa_and_normalize()` |

Line 888 is the one that matters. `_calculate_cpa_and_normalize()` (line 1605) rewrites `data['CPA']` for **every** species in the shared dict, and then caches **`self.max_CPA` and `self.max_LAI` as instance attributes** (lines 1615–1616). `get_normalized_cooling_potential()` divides by both (lines 1630–1631), so those two cached scalars are live denominators in the cooling term.

**Restoring `SPECIES_DATA` does not restore `max_CPA` / `max_LAI`.** Any `TreeSpecies` instance that outlives the evaluation keeps denominators computed from contaminated data. The fix must therefore **either** call `_calculate_cpa_and_normalize()` on the affected instance after restoring the dict, **or** ensure no `TreeSpecies` instance survives the `finally`.

Entry 8's Phase H attested that post-sweep `SPECIES_DATA` was pristine and that `Cooling_Model`/`Weighting` were bit-identical. It did **not** state that it checked `max_CPA` / `max_LAI` on a long-lived instance. **`code-stressor` must verify both scalars explicitly**, or the fix will look correct at the dict level and still be wrong at the normalization level — the exact "fixed but still wrong" outcome this project has already hit twice.

### Scope of the authorization — what is and is not permitted

**Permitted:** snapshot and restore `SPECIES_DATA` around each evaluation, exactly as Entry 8's Phase H harness did (proven working; post-sweep state verified pristine) — **plus** the `max_CPA`/`max_LAI` restoration required by the implementation note above.

**Not permitted under D-12** — each of these is a separate decision and none is authorized here:
- Changing the sweep bounds (currently a uniform ±20% on all 36 species parameters).
- Changing `n_samples` from 3, or reconciling it with `n_runs = 5`. That is **#77**'s disposition and a design choice, not a typo fix.
- Adopting Morris, or restructuring the sampling design. That is **#75**'s three-way question and belongs to the research lead.
- Adding the SD/dispersion column D-11 requires. Necessary, but it is a D-11 deliverable for `code-stressor`, not part of this repair.

### Evidence preservation

The pre-fix behaviour is an evidentiary artefact — it is what produced every existing `results/` run. It is preserved in git history at **`87d4528`**, the HEAD immediately before this authorization. Record that SHA in the commit that applies the fix, so the contaminated behaviour remains recoverable without keeping a second copy of the file.

**Owners:** `code-stressor` applies the fix to `legacy/AuditedCode_1.py`, adds the carry-forward criterion to `MIGRATION.md`, and re-runs to confirm post-sweep state is pristine and that `Cooling_Model`/`Weighting` remain bit-identical. `math-auditor`'s work here is **discharged** — do not re-audit the aggregation.

**Gates:** D-11's regeneration. Does **not** gate #75 or #77, which are independent and still owed.

---

## D-13 — Provenance of §3.5's published numbers — **OPEN**

**Opened 2026-07-27 by the research lead.** Raised by `math-auditor` in Entry 8 §B/§C, item 6 of "Still open", and explicitly left to the orchestrator to route.

**Question:** Where did the numbers printed in Results §3.5 come from?

**Context — this is not a rounding or transcription question.** Entry 8 established by execution that §3.5's published values match `AuditedCode_1.py` on **none** of four independent axes:

| Axis | Manuscript | Code (executed) |
|---|---|---|
| Sweep bounds | Narra crown diameter 12.0 → 34.0 m; allometrics "±15% band" | 18.4 → 27.6 m about base 23.0; **uniform ±20% on all 36 species parameters** |
| Baseline SECPI | 3.0576 | 3.2593 (one grid, one seed) — unmatched |
| Headline effect | 3.024 → 4.380, effect 1.356, SI 0.4435, **rank 1** | at the manuscript's own bounds: 3.213 → 2.855, effect 0.358 — **sign inverted**; the parameter ranks **28 / 40** |
| Category aggregation | Morphology 1.3068 · Allometry 0.1857 · Cooling 0.0727 · Weighting 0.0236 | 0.006593 · 0.012433 · 0.059809 · 0.001385 |

The Weighting category closes the argument with no assumptions: **n = 1**, so mean = max = sum = 0.001385, and the published **0.0236** equals none of the three.

**Therefore §3.5's numbers were produced by something this repository does not contain** — an earlier code version, a spreadsheet, or manual entry.

### Structurally identical to D-06, with one decisive difference

D-06 asked the same question of §3.1 and resolved as **reproducible but superseded** — the output was located in `legacy/archive/corrected_outputs/run_20260213_222844/` and matched the manuscript verbatim. **This is not that.** §3.5 is **not reproducible at all** from the current implementation. D-06's happy path is not available here, and the search should be run without assuming it will be.

**Where to look first:** `legacy/archive/` holds pre-audit iterations (`CA.py`, `CODE020526.py`, `GEMINI.py`, `dashboard.py`, `secpi_main.py`, `dashboard.ipynb`, `explore.ipynb`) — the same candidate set D-06 named, still unresolved as to which produced §3.1. A single earlier script may account for both.

### What the research lead must decide

1. **Whether to spend session time on the search at all.** D-11 already commits to regenerating §3.5 from scratch, so provenance is **not** on the critical path to a correct §3.5. Its value is different and narrower: it tells you whether §3.5's numbers were *wrong* or *from a different study configuration*, which bears on how the limitation is disclosed and on whether any other section inherited the same untraced source.
2. **If unfound: what the manuscript says.** A Results section whose numbers cannot be traced to any code in the repository is a disclosure obligation, not merely an item to delete-and-replace.

**Recommendation (orchestrator, labelled as a recommendation):** **time-box it.** Route one `code-stressor` session at `legacy/archive/`, bounded, searching for both §3.1's and §3.5's generator together since they are likely the same artefact. Do **not** let it block D-12's fix or D-11's regeneration — those proceed regardless. If the search comes back empty, that is itself a finding worth recording, and it converts D-13 into a disclosure decision rather than a forensic one.

**Does not gate:** D-11, D-12, or the preprint's §3.5 regeneration.
