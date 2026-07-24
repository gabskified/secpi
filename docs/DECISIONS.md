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

**Proposal on the table:** goalposts / distance-to-frontier normalization (precedent: UNDP Human Development Index technical notes; OECD/JRC 2008 *Handbook on Constructing Composite Indicators*; also World Bank Doing Business, European Skills Index).

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

## D-06 — Recover or retire the combinatorial species analysis — **PARTIALLY ANSWERED — TRIAGE REQUIRED**

> **Update 2026-07-24:** Multiple Python iterations located in the old file directory. Recovery is plausible. The question is no longer *does it exist* but **which iteration produced §3.1, and was that iteration correct?**

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
