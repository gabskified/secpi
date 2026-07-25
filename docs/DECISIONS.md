# DECISIONS.md — Research-Lead Sign-Off Queue

Everything below is a decision only the **research lead** can make. No agent may guess, default, or proceed past a blocked item. When a decision is made, record it here with a date, then append the corresponding entry to `PROJECT_LOG.md`.

Status vocabulary: `OPEN` · `DECIDED` · `SUPERSEDED`

---

## D-01 — SECPI classification scheme — **DECIDED**

**Decision:** Option B — fixed study-wide reference cutoffs.
**Date:** Project Log Entry 2 session (2026-07-19).
**Consequences:** (a) Methods §2.4 must be rewritten away from "self-normalizing per scenario"; (b) all existing Results numbers are void and must be regenerated; (c) the Editor authors the new Results. Code already implements this — no code change required.

---

## D-02 — Normalization goalpost ceiling — **OPEN — BLOCKING**

**Question:** Confirm the upper goalpost for the 0–5 SECPI presentation scale.

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

## D-03 — Statistical test outcome metric — **OPEN — BLOCKING**

**Question:** Pre-specify the single outcome metric for the "statistically significant redirection of resources" claim in §2.5.2.

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

## D-07 — Meaning of `k` — **OPEN**

`k` denotes species subset size in §3.1 (k=1 mono-species → k=6 full palette, trees fixed at five) and number of trees placed in the code, in `SuboptimalScenariosGenerator`, and in the D-03 Wilcoxon pairing design. Two orthogonal experimental axes, one symbol.

Pick distinct notation — e.g. `s` for subset size, `k` for tree count — and apply it consistently across Methods, Results, and the statistical design. **Settle before any Results prose is written**, or D-03's test will be misread as testing something it does not test.

---

## Decision dependency chain

```
D-06 (recover §3.1 code) ──→ §3.1 survives? ──→ Abstract & Conclusion headline claims survive?
                                 │
D-02 (ceiling) ─┐                │
                ├─→ regenerate Results under Option B ─→ Editor writes Results ─→ Abstract rewrite ─→ preprint
D-03 (metric) ──┤                │
D-07 (k notation) ───────────────┘
D-01 ✔ ─────────┘
D-04 ────────────────────────────────────────────────────────────────────────────→ DOI minting
```

**Neither D-02 nor D-03 blocks *running* the pipeline.** Both block *writing the numbers up*. Settle them first so normalized scores and the significance test are final on the first pass rather than requiring a second regeneration.

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
