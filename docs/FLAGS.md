SECPI Manuscript — Comprehensive Editorial Flag Archive (v4 — Results/Discussion/Conclusion pass **completed**)

**Sections reviewed:** Title, Abstract, Introduction, Methods (§2.1–§2.6), **Results and Discussion (§3.1–§3.5)**, **Conclusion / Recommendations / Individual Author's Contributions / Acknowledgment**
**Update source (v2):** Cross-referenced against SECPI Project Log Entries 1–3 (Mathematical Auditor sessions, code-execution-verified against `AuditedCode_1.py`)
**Update source (v3):** Project Log Entry 4 + `docs/STATE.md` (movement blocks for #42–#51, reconciled into this file verbatim in substance), plus the first editorial read of `manuscript/sections/06_results_discussion.md` §3.1–§3.4.4 (Project Log Entry 5 — session interrupted, register truncated at #74).
**Update source (v4):** Project Log Entry 6 — completion of Entry 5's unfinished scope. `06_results_discussion.md` **§3.5** (lines 597–725) and `07_conclusion.md` **in full**. Flags **#75–#95** assigned. The five defective flags identified in Entry 5 §C (#53, #59, #64, #68, #70) repaired in place.
**Update source (v5):** Project Log Entry 8 — the `math-auditor` execution audit of `SensitivityAnalyzer` (2026-07-27, commit `0e912d1`). Flags **#96–#97** assigned; **#77** escalated; `v5 UPDATE` / `v5 CORRECTION` blocks appended in place to #57, #58, #75, #76, #78, #79, #82, #85, #95. **The first flag movements in this register grounded in executed code rather than in reading.**
**Session pause point:** none. ~~**Next free flag number: #95.**~~ ~~**superseded: … next free number is #75**~~ ~~**superseded again 2026-07-26 (v4): #75–#95 are now assigned. The next free flag number is #96.**~~ — **superseded again 2026-07-27 (v5): #96 and #97 are now assigned. The next free flag number is #98.**

> ⚠️ **v3 and v4 were both read-only editorial passes. No code was executed in either.** Every finding below that depends on program behavior is registered as PENDING VERIFICATION or POTENTIAL ROADBLOCK with a named owning agent and a named artefact. Arithmetic checks performed by hand on the manuscript's own reported values are labelled as such, with the working shown inline.

## Classification Legend

**RESOLVED — Cleared Up**
The flag was directly answered, verified, or fixed. No further action required beyond applying the confirmed answer to manuscript prose.

**RESOLVED — Deferred**
An editorial observation (e.g., redundancy, minor phrasing/formatting) rather than a factual or methodological risk. The author team has consciously chosen not to act on it now; it carries no risk to submission readiness on its own.

**PENDING VERIFICATION**
The author team is still checking a fact, citation, dataset, or parameter. Not yet a risk, but not yet closed.

**POTENTIAL ROADBLOCK**
A pending item where, if verification fails or the underlying issue can't be reconciled with the actual implementation/data, the affected section would need to be substantively reworked rather than simply re-worded.

**ROADBLOCK (SEVERE)**
A potential roadblock confirmed as unresolved/unresolvable — the section requires substantive rework before it can proceed.

---

## Executive Summary

| Category | Count (v1) | Count (v2) | Count (v3 — *claimed*) | Count (v4 — actual, per-flag) | Count (v5 — **actual, per-flag**) | Δ v4 → v5 |
|---|---|---|---|---|---|---|
| RESOLVED — Cleared Up | 17 | **25** | 29 | 29 | **29** | — |
| RESOLVED — Deferred | 2 | 2 | 2 | 2 | **2** | — |
| PENDING VERIFICATION | 19 | **14** | 32 | 30 | **29** | −1 (#77 escalated) |
| POTENTIAL ROADBLOCK | 3 | **0** | 30 | 33 | **36** | +3 (#77 in, #96 and #97 new) |
| ROADBLOCK (SEVERE) | 0 | 0 | 1 | 1 | **1** | — (still #82 alone) |
| **TOTAL FLAGS IDENTIFIED** | 41 | 41 | 94 | 95 | **97** | +2 |

> ### v5 — Project Log Entry 8 applied (2026-07-27, `editorial-flagger`)
>
> **Update source (v5):** Project Log Entry 8 — the `math-auditor` execution audit of `SensitivityAnalyzer` (commit `0e912d1`), which created, closed and reclassified nothing by design and routed all of its evidence here. This is the **first flag movement in this register grounded in executed code rather than in reading.**
>
> **Two flags created: #96** (`SensitivityAnalyzer` mutates global `TreeSpecies.SPECIES_DATA` and never restores it) and **#97** (§3.5's qualitative findings do not survive execution against the reference implementation). Both **POTENTIAL ROADBLOCK**. **#96 and #97 were the next two free numbers; nothing was renumbered.**
>
> **⚠️ Instruction superseded.** The v4 Register-status block and `docs/STATUS.md` both direct a future references-and-appendices pass to *"assign from #96."* **That instruction is now void — #96 and #97 are taken. The references-and-appendices pass assigns from #98.**
>
> **The project still carries exactly one ROADBLOCK (SEVERE): #82.** A second severe flag was recommended by Entry 8 for the state leak and is **declined, with reasons stated in the body of #96.** The register's risk posture is unchanged in category, materially worse in content.
>
> **Nine existing flags moved or were updated:** #75, #76, #77, #78, #79, #82, #85 (Entry 8's routing table), plus #57, #58 and #95 (collateral advances the flagger identified in the same evidence). One class changed: **#77 PENDING VERIFICATION → POTENTIAL ROADBLOCK.**
>
> **Binding scope limit inherited from Entry 8 and carried into every v5 block below.** Entry 8's runs are **one grid, one morphology, one seed, `n_samples=3`, with no D-02 ceiling applied and no output written to `results/`.** Entry 8 states plainly that **no number in it may be quoted as a manuscript value.** Accordingly, every v5 block distinguishes:
> - **Structural claims** — evaluation counts, sweep bounds, category membership, aggregation semantics, the state leak, the ACO kwargs. These are deterministic, reproducible, and asserted without qualification.
> - **Magnitude claims** — which parameter ranks where, category hierarchies, sign of an effect, measured index values. These are **single-run diagnostics** carrying a measured SI noise floor of ≈ 0.0098, and are labelled as such at every point of use. `code-stressor` owns their formal replication.

> ### ✅ TRUNCATION CLOSED — the register is complete and self-consistent as of v4 (2026-07-26)
>
> **This block replaces the 🔴 THIS FILE IS TRUNCATED notice added by the orchestrator on 2026-07-25 (Project Log Entry 5 §A). That notice is now discharged, not deleted — its substance is preserved below for the audit trail.**
>
> **What it said:** the v3 session terminated mid-write; the register ended at **#74** followed by a bare `## Resuming This Review — PLACEHOLDER` stub; **flags #75–#94 were never written**; four items were forward-referenced elsewhere in this file as though on record when they were not (**#75** the claimed first SEVERE, **#79**, **#90**, **#91 / #92**); and the v3 Executive Summary column described a 94-flag file that did not exist. All of that was correct.
>
> **What v4 did:** re-derived the missing scope from the manuscript directly — `06_results_discussion.md` §3.5 (lines 597–725) and `07_conclusion.md` in full — and assigned **#75–#95 (21 flags)**. `#52–#74` were **not** renumbered and their findings were not re-derived. See "v4 — New flags #75–#95" below.
>
> **Forward references resolved.** The numbers the v3 file predicted are *not* the numbers v4 assigned, because v4 derived its findings in document order rather than reserving slots. The mapping:
>
> | v3 forward reference | Actually assigned in v4 | Note |
> |---|---|---|
> | **#75** — SEVERE, §3.5 category-level sensitivity means | **#82** | Confirmed **ROADBLOCK (SEVERE)**. The defect is *larger* than the forward reference described: **all four** reported category means are impossible, not just Species Morphology. **#75** is instead the §2.5.3-Morris-vs-§3.5.1-local-OAT method contradiction. |
> | **#79** — §3.5.3 "sourced from literature" false provenance | **#84** | Confirmed. **#79** is instead the unequal-sweep-width defect. |
> | **#90** — Conclusion "successfully developed and validated" | **#87** | Confirmed and widened to all three of §2.5's validation stages. **#90** is instead the Conclusion's inheritance surface for #62/#63/#67. |
> | **#91 / #92** — Conclusion prescription and transferability | **#91 / #92** | Numbers coincide; the split is by remediation (prescription vs transferability), which happens to land on the same two slots. Coincidence, not deference to the prediction. |
>
> **Class split actually derived for #75–#95: 15 POTENTIAL ROADBLOCK / 5 PENDING VERIFICATION / 1 ROADBLOCK (SEVERE) = 21.** The v3 preamble predicted 14 / 5 / 1 = 20 for this range. Close, but **not the same set** — the counts were derived independently in document order and then compared, per the resumption brief's instruction not to force a match.
>
> **v4 count basis:** the #1–#74 per-flag record (29 cleared / 2 deferred / 25 pending / 18 PR / 0 severe = 74), plus #75–#95 (0 / 0 / 5 / 15 / 1 = 21) → **29 / 2 / 30 / 33 / 1 = 95**. Derived by enumerating every `**#N —` heading in this file, not by carrying forward any summary line.
>
> **The project now carries one ROADBLOCK (SEVERE): #82.** This is the first in the project's history and it is registered on evidence, not on a forward reference. ~~**Next free flag number: #96.**~~ — **superseded 2026-07-27 (v5): #96 and #97 are assigned; the next free number is #98.** #82 is **still the only** ROADBLOCK (SEVERE) — a second was recommended by Project Log Entry 8 for the `SensitivityAnalyzer` state leak and was **declined with an argument recorded in the body of #96.**

**What moved and why (v1 → v2):** all 3 POTENTIAL ROADBLOCK flags (#25, #28, #33) closed via direct code execution against `AuditedCode_1.py`. 5 PENDING VERIFICATION flags (#31, #34, #35, #38, #41) closed the same way. No flag escalated in severity. Full detail below.

**What moved and why (v2 → v3):**

1. **#42–#51 formally registered into this file** (they existed only in `docs/STATE.md`). Transcribed verbatim in substance; no status re-derived, no wording of a finding changed.
2. ~~**#52–#94 added** — 43 new flags from the first editorial pass over Results and Discussion (§3.1–§3.5) and the Conclusion. 27 are POTENTIAL ROADBLOCK, 15 PENDING VERIFICATION, **1 is the project's first ROADBLOCK (SEVERE)** — #75, §3.5's category-level sensitivity table, whose reported means are arithmetically impossible against the SI definition given one subsection earlier.~~
   ⚠️ **Corrected in v4.** v3 actually wrote **#52–#74 only** (23 flags: 13 POTENTIAL ROADBLOCK, 10 PENDING VERIFICATION), covering **§3.1–§3.4.4 only**. §3.5 and the Conclusion were completed in v4 as **#75–#95**. The SEVERE finding is real but is registered as **#82**, not #75, and it is broader than described here — all four category means are impossible, not one.
3. **#39, #44, #46, #30, #6, #10, #11 escalated or refined** — see the "Escalations and refinements of existing flags" block below. No existing flag was downgraded in v3 or v4.

> ### ⚠️ Count reconciliation note — read before quoting any total
>
> `docs/STATE.md` line 79 records **"28 cleared · 2 deferred · 19 pending · 3 potential roadblocks · 0 severe · 51 total."** Those five categories sum to **52**, not 51. The per-flag movement record in the same file sums cleanly to **51** (29 cleared / 2 deferred / 17 pending / 3 potential roadblocks / 0 severe), because #19, #26, #43 and #51 all moved into RESOLVED — Cleared Up while #30 moved back out of PENDING into POTENTIAL ROADBLOCK.
>
> **This file treats the per-flag record as authoritative** and builds the v3 column on the 51-flag reconstruction. `docs/STATE.md` was **not** edited — resolving that summary line is the orchestrator's or research lead's call, not the flagger's. Flag this to whoever next syncs `STATE.md`.

---

## Full Flag Register

> **Scope of the classification sections immediately below: Flags #1–#41 only** (the v2 register). Flags #42–#94 are registered in the v3 blocks further down, each carrying its own classification. Do not read the "(25 flags)" / "(0 flags)" counts in the headings below as file-wide totals — they describe #1–#41 as of v2.

### RESOLVED — Cleared Up (25 flags — of #1–#41, as of v2)

*Flags #1–4, 6–8, 10–12, 15–18, 23, 32, 40 are unchanged from v1 — see original archive for their descriptions/resolutions, not reproduced here since nothing about them changed.*

**Newly closed this update (8 flags):**

| # | Section | Original flag | Resolution (this update) |
|---|---|---|---|
| **25** | Methods | CA transition-probability equation showed the same time index (t+1) on both sides. | **Confirmed real** — verified verbatim against the manuscript PDF, not a transcription artifact. Fix: right-hand side should read $p_i^{kl}(t)$, consistent with a standard first-order recursive Markov formulation. Code has been corrected to implement this form; the recursion is now genuinely computable and was empirically validated (100/100 seeds land in target density bands across both morphologies). Manuscript equation in §2.2.2 needs the same correction. Source: Project Log Entry 1 §1.5. |
| **28** | Methods | Coarse and fine grids described with identical/conflicting dimensions across the text. | **Confirmed via code inspection**: coarse cells are 100 m² (10 m × 10 m), fine cells are 1 m² (1 m × 1 m), 100×100 = 10,000 fine cells total, matching Figure 4. All conflicting statements in the current manuscript text should be corrected to these values. Source: Project Log Entry 1 §1.4/§3.2. |
| **31** | Methods | Species-specific allometric parameters (h₀, h₁, l₀, l₁) referenced but not tabulated. | **Data confirmed to exist and is exact** — all values are present in `AuditedCode_1.py`'s `TreeSpecies.SPECIES_DATA` for all six species. No further research needed; Editor should pull these directly into a Methods table or Appendix. Note: running these values through the manuscript's own DBH formula produces implausible results — see Flag #30, still open, which is a separate question about the *formula's* validity, not the *table's* existence. Source: Project Log Entry 1 §1.2, Entry 3. |
| **33** | Methods | Fine grid cell size restated a third, conflicting way in §2.4.2. | Same resolution as Flag #28 (extends it) — 1 m² fine cells confirmed. Source: Project Log Entry 1 §1.4/§3.2. |
| **34** | Methods | §2.4 says "minimize" SECPI while §2.4.2 says "Maximize," with SECPI framed as an improvement metric throughout. | **Confirmed via code**: the ACO objective function is genuinely `Maximize f(x) = SECPI`. §2.4's "minimize" is the wording error; correct it to match §2.4.2 and the actual implementation. Source: Project Log Entry 3. |
| **35** | Methods | Stated 62% cooling at crown edge doesn't match recalculation using λ=1.897 (recalculation gives ~38.7%). | **Arithmetic confirmed correct — under a corrected decay formula.** $\exp(-\lambda(d/C_D)^2)$ at $d/C_D=0.5$ gives exactly 0.622, matching the manuscript's stated 62%. The recalculation that produced 38.7% assumed a linear (exponential-only) decay term; the actual/intended function is quadratic in distance (see Flag #38). No arithmetic error — the formula transcribed in §2.3.2 is missing a squared term. Source: Project Log Entry 3 (originally verified early in the audit conversation, retroactively logged). |
| **38** | Abstract/Methods | Decay function called "Gaussian" but the written formula (§2.3.2) is linear-in-distance (exponential), not Gaussian. | **"Gaussian" is the correct term.** The actual/intended cooling function is $\exp(-\lambda(d/C_D)^2)$ — genuinely Gaussian-shaped (quadratic in distance), matching the code and correctly reproducing both the 62%-at-crown-edge and 15%-at-full-crown-diameter calibration points. The manuscript's written equation in §2.3.2 needs the squared term restored; the terminology itself does not need to change. Closes together with Flag #35 via the same fix. Source: Project Log Entry 3. |
| **41** | Methods | CCA_threshold and steepness parameter k given only as "illustrative" examples. | **Confirmed as the actual production values, not illustrative placeholders**: `decay_lambda=1.9, cca_threshold=1.2, competition_k=5.0`, verified directly in the model's production configuration. Manuscript should state these plainly as the fixed values used, not as examples. Source: Project Log Entry 1 §3.2, Entry 2 (independently reconfirmed). |

---

### RESOLVED — Deferred (2 flags) — unchanged from v1

Flags #24, #27 — no change; not reproduced here, see original archive.

---

### PENDING VERIFICATION (14 flags — of #1–#41, as of v2)

*Flags #13, #14, #19, #21, #22, #29, #36 are unchanged from v1 — no update this session, not reproduced here.*

> v3 note: #19 and #26 have since moved to RESOLVED, and #30 has since moved to POTENTIAL ROADBLOCK. Those movements are recorded in the v3 blocks below, not applied to the v2 body above — same append-don't-overwrite convention as `PROJECT_LOG.md`.

**Flags with meaningful progress this update (7 flags — still open, but status has changed):**

| # | Section | Original flag | Updated status |
|---|---|---|---|
| **5** | Abstract | SECPI score range given with no defined scale. | Author team's original instinct (0–5 scale) confirmed directionally correct, but the *first* proposed normalization (pure theoretical min/max bounds) was superseded — it made the no-intervention baseline map to a non-zero, uninterpretable value. **Current proposal: "goalposts" (distance-to-frontier) normalization**, precedented by the UN Human Development Index methodology and the OECD/JRC (2008) *Handbook on Constructing Composite Indicators*. Floor = raw SECPI 0.0 (baseline → normalized 0), ceiling ≈ raw SECPI 3.75 (near-optimal → normalized 5), **pending research-lead confirmation of the exact ceiling value** before the code change is applied. Source: Project Log Entry 2, `SECPI_normalization_and_stats_proposals.md`. |
| **9** | Abstract | Land-use ratio source unclear. | Unchanged in substance — a literature-sourcing addendum has been sent to the Deriver chat requesting grounding for the 55–65% / 25–40% / 5–10% P/A/V split against Philippine urban land-use/zoning literature. No response received yet. Source: Project Log Entry 1 addendum. |
| **20** | Methods | AGB estimation-error percentages given with no citation. | Not previously assigned to anyone in the current audit workflow; now added to the Deriver chat's task queue. No progress yet beyond assignment. Source: Project Log Entry 3. |
| **26** | Methods | "Expander heuristic" terminology — unclear if from Almeida et al. (2002) or coined by the author team. | Not previously assigned; now bundled into the Deriver chat's existing task of sourcing Almeida et al. (2002) directly (for the separate `p0`-provenance question, see Flag-adjacent note below) — checking for this term is a low-cost addition to that same literature lookup. No answer yet. Source: Project Log Entry 3. |
| **30** | Methods | DBH-from-height formula runs opposite to typical FORMIND allometrics. | **Confirmed numerically implausible**, independently verified twice (Project Log Entry 1 and Entry 2): using the manuscript's own Table 4 constants, all six species yield $h < h_0$, producing DBH values of 0.17–0.66 (physically implausible) and computed LAI 50–420× smaller than the values actually used in the model. This is confirmed as a real problem, not just a suspected one — still blocked on the Deriver chat sourcing genuine literature-based H-D allometric equations before it can close. Source: Project Log Entry 1 §1.2, Entry 2 Finding F. |
| **37** | Methods | "Chebyshev space (ℤ²)" used for the placement lattice while cooling decay uses Euclidean distance. | **Partially clarified, not fully closed.** Confirmed: the cooling decay function genuinely uses Euclidean distance throughout, consistent with that part of the manuscript. Separately, the *original* Vulnerable-zone buffer implementation used Manhattan distance (mismatched with the "Chebyshev" description) — this specific sub-issue is now moot, because the V-zone generation method has been rewritten entirely (target-count-driven BFS growth, using neither Manhattan nor Chebyshev distance). What remains genuinely open: whether "Chebyshev space (ℤ²)" is meant as a general indexing/lattice convention distinct from any specific physical-distance calculation, or whether it's simply an error that should be removed. Needs author/Editor clarification, not further code work. Source: Project Log Entry 1 §1.4, Entry 2. |
| **39** | Methods | "Statistically significant redirection of resources" claimed without specifying test/n/threshold. | **A specific test has been recommended, not yet run.** Paired Wilcoxon signed-rank test, WITH-vulnerable vs. WITHOUT-vulnerable, n=30 (6 k-values × 5 existing per-k restarts), on a placement-based outcome metric independent of SECPI itself (recommended: proportion of delivered cooling landing in Vulnerable zones, to avoid circularity with SECPI's own definition). **Pending research-lead confirmation of the exact outcome metric**, then execution (Stressor) and write-up (Editor). If the test is non-significant, the manuscript claim must be softened to descriptive language — do not report "statistically significant" unless the test actually supports it. Source: Project Log Entry 2, `SECPI_normalization_and_stats_proposals.md`. |

---

### POTENTIAL ROADBLOCK (0 flags — of #1–#41, as of v2)

*All 3 flags previously in this category (#25, #28, #33) have moved to RESOLVED — Cleared Up this update — see above. No flags currently classified at this severity.*

> ~~v3 note: #30 has since moved back into this category, and 27 new flags (#52–#94) enter it. The file-wide POTENTIAL ROADBLOCK count is **30**. See the v3 blocks below.~~
>
> ⚠️ **v4 correction.** #30 did move back into this category, but the "27 new flags (#52–#94)" figure was aspirational. The actual file-wide POTENTIAL ROADBLOCK roster is **33**:
>
> - **5 from #1–#51:** #30, #39, #44, #46, #48
> - **13 from v3 (#52–#74):** #52, #54, #55, #56, #57, #60, #62, #64, #67, #68, #69, #70, #72
> - **15 from v4 (#75–#95):** #75, #78, #79, #80, #83, #84, #85, #86, #87, #88, #90, #91, #92, #93, #94
>
> 5 + 13 + 15 = **33**, not 30. See the v3 and v4 blocks below.
>
> ⚠️ **v5 update (2026-07-27) — the roster is now 36.** Add **#77** (escalated from PENDING VERIFICATION on executed evidence that no dispersion statistic is computed or storable), **#96** (the `SensitivityAnalyzer` state leak) and **#97** (§3.5's qualitative findings do not survive execution). 33 + 3 = **36**. The complete roster is written out in the v5 Totals block at the end of this file.

---

### ROADBLOCK (SEVERE) (0 flags — of #1–#41, as of v2)

None currently confirmed at this stage of review — unchanged.

> ~~v3 note: the file-wide SEVERE count is now **1** — Flag **#75** (§3.5 category-level sensitivity means are arithmetically impossible). This is the project's first. See the v3 blocks below.~~
>
> ⚠️ **v4 correction — the finding is confirmed, the number is wrong.** v3 never wrote the flag; between 2026-07-25 and 2026-07-26 the project's severe count was genuinely **0** and `docs/STATE.md` was right to say so. v4 re-derived the finding from the manuscript and registered it as **#82**, not #75. **File-wide SEVERE count is now 1 — Flag #82** (§3.5.2: *all four* reported category-level mean sensitivity indices exceed the maximum SI of their own member sets). This is the project's first ROADBLOCK (SEVERE) and it is now on record rather than forward-referenced. See the v4 block below.
>
> ✅ **v5 confirmation (2026-07-27) — the file-wide SEVERE count is STILL 1, and still #82.** Project Log Entry 8 recommended a second severe flag for the `SensitivityAnalyzer` state leak; the recommendation was weighed and **declined**, and the argument is recorded in the body of **#96**. Entry 8 also **discharged #82's `math-auditor` diagnostic and overturned its working hypothesis** — the aggregation function is arithmetically correct, and the published category means are not reproducible from `AuditedCode_1.py` at all. **#82 stays SEVERE and is strengthened by that finding, not weakened.** See the `v5 UPDATE to #82` block.

---

## Flag #42 — formally registered (v3)

*Previously carried in this file as an unnumbered "new item surfaced by code audit." `docs/STATE.md` and Project Log Entry 4 assign it **#42**; that assignment is adopted here. Class: **PENDING VERIFICATION** (Methods §2.2.1 — V-zone buffer geometry). Description below is the original text, unaltered.*

**V-zone "30-meter Chebyshev buffer" description (§2.2.1) is factually incompatible with the code and, independently, appears geometrically incompatible with the manuscript's own 5–10% Vulnerable-area target on this grid size.** The coarse grid is confirmed 10 m/cell (10×10 = 100 cells total); a 30 m Chebyshev buffer is a 7×7 = 49-cell square — a single such buffer already covers 49% of the entire grid, far exceeding the stated 5–10% target before any overlap is considered. The current code does not implement a Chebyshev buffer at all — it uses target-count-driven BFS growth from seed points, which reliably and deterministically hits the 5–10% target (produces exactly 8% coverage, zero run-to-run variance) but does not correspond to the literal procedure described in §2.2.1. **This is an Editor task**: rewrite §2.2.1 to describe the actual BFS method, not a code task — the geometric incompatibility means the originally-described procedure likely cannot be made to work as literally written on this grid size regardless of implementation. Source: Project Log Entry 1 §3.1, Entry 2 handoff note 6.

---

## v3 — Flags #43–#51 reconciled in from `docs/STATE.md`

> **Transcription only.** These flags were raised in Project Log Entry 4, the D-06 salvage, Entry 3, and the Phase 1.5 manuscript extraction, and were recorded only in `docs/STATE.md`. They are registered here so that `FLAGS.md` is once again the complete register. Descriptions, sections and statuses are carried over verbatim in substance from `STATE.md`; nothing was re-derived, re-worded in its findings, or reclassified.

### Added during migration (Project Log Entry 4 and dependency verification)

| Flag | Section | Description | Class |
|---|---|---|---|
| **#43** | Results §3.1 | 63-subset combinatorial analysis has no code in `AuditedCode_1.py` | **POTENTIAL ROADBLOCK** → since **DOWNGRADED**, see below |
| **#44** | Results §3.1 / Methods | `k` denotes both species-subset size and tree count | PENDING VERIFICATION |
| **#45** | Abstract / Methods §2.4.2 | Stated software stack contradicts the implementation | PENDING VERIFICATION |

**Flag #43 downgraded** — POTENTIAL ROADBLOCK → **RESOLVED (Cleared Up)**. The combinatorial output was located at `legacy/archive/corrected_outputs/run_20260213_222844/combinatorial/` and matches §3.1 verbatim (4.3916 / rank 3 / 63 rows). Superseded by outcome (b), not missing. *Evidence and log citation: D-06 update 2026-07-25 in `docs/DECISIONS.md`; recorded in `docs/STATE.md`.*

**Flag #44 refined** — §3.1's `k` is now confirmed as *available palette size*, a third distinct meaning alongside subset size and tree count. Feeds D-07.

**Flag #45 detail.** The Abstract states ACO was implemented "via the scikit-opt Python library"; `AuditedCode_1.py` contains no `sko` import and hand-implements `AntColonySystemACO`. §2.4.2 credits "Matplotlib and Seaborn"; only matplotlib is imported. Verified dependencies are numpy, matplotlib, scipy (`cdist` only), tqdm, and pandas (soft, try/except-guarded). A reviewer attempting reproduction would install scikit-opt and find nothing uses it — this is a reproducibility defect, not a wording nit.

### Added from the D-06 salvage

| Flag | Section | Description | Class |
|---|---|---|---|
| **#46** | Results §3.1, Abstract, Conclusion | `k` = species *available*, not *used*. ACO used the full palette in only 30.16% (WITH) / 19.05% (WITHOUT) of configurations; the rank-1 k=6 result planted just 2 species. The "diversity offers negligible benefit" claim is mis-stated. | **POTENTIAL ROADBLOCK** |
| **#47** | Results §3.1 | WITHOUT_VULN produced only 3 distinct SECPI values (1.500/1.501/1.750) across 63 configurations — near-total loss of discrimination, likely saturation or clamping. | PENDING VERIFICATION |

**⚠️ Flag #47 CORRECTED (carried over from `STATE.md`, verbatim in substance).** #47 was registered claiming the WITHOUT_VULN degeneracy was "not explained by any existing flag." **That was wrong.** The manuscript documents it explicitly at §3.4.4: scores *"compress into two narrow bands centered at approximately 1.50 and 1.75, with the entire top 48 configurations falling within a range of only 0.0002,"* interpreted as the optimizer lacking spatial signal without equity weighting. The authors observed and wrote up the phenomenon; it was flagged as undiscovered something already in their Results.

**Revised #47:** PENDING VERIFICATION → the *observation* is documented and correct. What still needs checking is whether the *interpretation* holds, and whether a near-degenerate WITHOUT_VULN arm is a sound comparison baseline. Reframed as an analytical question, not a discovery.

### Added from Entry 3 (Deriver)

| Flag | Section | Description | Class |
|---|---|---|---|
| **#48** | §2.3 / Table 4 | Assumed species heights extrapolate beyond calibration — Narra 30 m implies DBH 244.5 cm vs. observed max 117.2 cm and species max ~200 cm. Independent of which H–D constants are used. See **D-08**. | **POTENTIAL ROADBLOCK** |
| **#49** | §2.3.2 | λ = 1.897 attributed to Morakinyo & Lam (2016), which is an **ENVI-met thermal-comfort study, not a distance-decay calibration**. λ is arithmetically fixed by the author-chosen 15% anchor (−ln 0.15 = 1.897). Author construct requiring disclosure. | PENDING VERIFICATION |
| **#50** | §2.3 | Cooling decay kernel `exp(−λ(d/C_D)²)` has **no direct literature precedent** — author construct requiring disclosure. | PENDING VERIFICATION |

### Added during Phase 1.5 manuscript extraction

| Flag | Section | Description | Class |
|---|---|---|---|
| **#51** | Results §3.5 | **Subsection numbering error.** §3.5 Sensitivity Analysis contains `3.5.1`, then jumps to **`3.4.2`** and **`3.4.3`** — duplicate numbers already used under §3.4. Mechanical fix; renumber to 3.5.2 / 3.5.3. | RESOLVED — Cleared Up (fix is unambiguous) |

### Movements on existing flags recorded in `STATE.md` (Entry 3 recovery)

| Flag | Movement | Basis |
|---|---|---|
| #19 | PENDING → ✅ **RESOLVED — error confirmed** | *Terminalia catappa* and *Lagerstroemia speciosa* are both documented **deciduous**. The blanket "evergreen tree types" claim is factually wrong. Correct to "predominantly evergreen, with Talisay and Banaba deciduous/semi-deciduous." |
| #26 | PENDING → ✅ **RESOLVED — direct precedent** | "Expander" is **DINAMICA** terminology, not author-coined and not originally Almeida's. Cite **Soares-Filho, Cerqueira & Pennachin (2002), *Ecological Modelling* 154(3), 217–235.** DINAMICA's expander is `P' = P × √(nⱼ/4)` — a neighbourhood factor on a weights-of-evidence potential, never a uniform constant, reinforcing that `p0 = 0.5` is the team's own simplification. |
| #30 | POTENTIAL ROADBLOCK → ◐ **PARTIAL — 3 of 6 species resolved** (and retained in POTENTIAL ROADBLOCK pending the remaining 3) | Real refitted coefficients now exist for Narra, Talisay, Banaba from 211 NPDC field records, independently reproduced. **Duhat, Kabiki, Akleng-parang have no data.** Options: constrained pantropical/genus fit, fieldwork, or disclose as range-constrained author estimates. |
| #35 / #38 | Re-sourced | Confirmed as a single defect from a readable source: code and calibration are Gaussian (15% at d=C_D ✓, 62.2% at d=C_D/2 ✓); §2.3.2 dropped the square. Fix = restore the square. |
| #20 | PENDING → ◐ **PARTIAL — needs author input** | Directional claim well-supported (Chave et al. 2004; Mauya et al. 2015). **No source called "PTM-2" could be located**, and no source gives the manuscript's specific figures (~50% / ~10% / ~5%). Ask the author team what "PTM-2" refers to. |
| #21 | PENDING → ◐ **Likely resolved** | **No author named "Kunhle" exists** in the submodular-optimization literature. Correct source is almost certainly **Bian, Buhmann, Krause & Tschiatschek, ICML 2017** (manuscript cites "Bian et al., 2018" one section earlier — year off by one). Editor to confirm. |
| #22 | PENDING → ◐ **Diagnosed — citation-form error** | **NSF is a funding agency, not an author.** EPFL has attributable material (Discrete Optimization Chair; MATH-504). The team must name the actual paper/textbook intended (e.g. Rothvoss, *Integer Optimization and Lattices*, or Schrijver) rather than cite institutions. |
| #9 | Detail added | P 55–65% analogous (specify density context — Metro Manila core ~78% impervious); A 25–40% aligns with *aspirational* targets (UN-Habitat 30%+10–15%; C40 30%), not measured cover (~16% global avg); **V 5–10% has no precedent and is directionally contradicted** by Philippine heat-vulnerability data (Quezon City: 81% of barangays high-risk). **V is the highest-priority disclosure item.** |
| #14 | ◐ Spot-checked | Yigitcanlar verified real and active. **Scordato & Gulbrandsen and Abujder Ochoa et al. remain unchecked.** |

**Corroboration from the Phase 1.5 extraction (carried over):** §3.4.4 states SECPI spans **"3.023 to 4.393... across the 63 configurations"** — matching the recovered `run_20260213_222844` CSV exactly (best 4.393, and a `k2_Tal_Ban_SECPI_3.023.png` file). Independent confirmation that D-06's located output is the source of the manuscript's Results.

---

## v3 — Escalations and refinements of existing flags

*No existing flag was downgraded in v3. The following are escalations or refinements, each with the evidence that caused it.*

| Flag | Movement | Evidence from the Results/Conclusion read |
|---|---|---|
| **#39** | PENDING VERIFICATION → **POTENTIAL ROADBLOCK** | #39 was scoped to Methods §2.5.2's "statistically significant redirection of resources." Results §3.4.4 contains a **second, independent** significance assertion — *"the equity-weighted scenario produced a significantly higher mean SECPI of 3.08"* — and additionally quotes the software's own hardcoded verdict string *"[SUCCESS] HIGH EQUITY"* as confirmation. The defect is therefore not one sentence in Methods; it is the evidentiary spine of §3.4.4. Registered in detail as #69, #70. |
| **#44** | PENDING VERIFICATION → **POTENTIAL ROADBLOCK** | The `k` collision is not merely notational. §3.4.1 reports per-`k` mean SECPI of 2.990–3.017, which is **arithmetically incompatible** with the individual configuration values reported from the same 63-configuration dataset in §3.1.4/§3.4.2/§3.4.3 (k=1 monocultures 4.392, 4.386, 3.106, 3.094, 3.068, 3.040 → mean 3.514, not 2.990). Two incommensurable experiments are interleaved in one Results narrative. Registered as #64. |
| **#46** | Refined (class unchanged: POTENTIAL ROADBLOCK) | #46 states that the CSV's `species_actually_used` column is something "the manuscript never reports." **The manuscript does report it in part**: §3.4.2 states *"Among the top 10 configurations, the ACO used all available species in only 3 out of 10 cases"* and that the rank-1 k=6 result *"allocated trees to only Narra and Talisay."* What is genuinely unreported is the dataset-wide figure (30.16% / 19.05%) and — more damagingly — the manuscript draws the *opposite* conclusion from data it has already disclosed. The objection stands and strengthens; the premise needed correcting. |
| **#30** | Refined (class unchanged: POTENTIAL ROADBLOCK) | Results §3.5.3 states the allometric constants were *"sourced from literature."* Entry 3 established they have no literature source and are 22–77× off an empirical refit; D-09 records them as author estimates. #30 was a Methods-scoped defect; it is also a **false provenance claim in Results**. ~~Registered as #79.~~ → **v4: registered as #84.** v4 additionally registers **#85** — the near-zero allometric sensitivity indices are the *expected signature* of parameters that D-09 places off the canonical path, so §3.5.3 reads #30's defect as evidence of robustness. |
| **#6** | Refined (class unchanged: RESOLVED) | #6 resolved the Abstract's 28% / 0.03% as raw percentage differences rather than tests. v3 finds §3.4.2 goes further: it states the 0.03% margin *"falls well within the stochastic variation inherent to the ACO metaheuristic across independent runs"* — i.e. the manuscript's own Results declares its own headline number to be noise. Registered as #65. |
| **#10 / #11** | Extended in scope | The synthetic/non-georeferenced objection was raised against the Title and Abstract. The Conclusion reoffends independently and more seriously: a real-world planting prescription for Philippine planners, and a transferability claim across "climate-vulnerable cities." Registered as #91, #92. **v4: confirmed verbatim and registered at those numbers.** v4 also finds a *third* instance inside Results — §3.5.3's field-measurement prescription *"For planning applications…"* — registered as **#86**. |
| **#8** | Extended in scope | "No field or remote-sensing validation" was an Abstract-scoped lock. The Conclusion asserts the framework was *"successfully developed and validated"* and that results *"confirm the model's ability to deliver targeted thermal relief."* ~~Registered as #90.~~ → **v4: registered as #87**, and widened — none of the three validation stages Methods §2.5.2 specifies has a reported result or a met pass criterion, and §2.5.2's own criterion (*"outperform random placements"*) has no random-placement baseline anywhere in §3. |

---

## v3 — New flags #52–#74 (Results and Discussion, §3.1–§3.4.4)

> ~~**First editorial pass over §3.1–§3.5 and §Conclusion.** Registered in document order. 43 flags: 27 POTENTIAL ROADBLOCK, 15 PENDING VERIFICATION, 1 ROADBLOCK (SEVERE).~~
>
> ⚠️ **v4 correction to this heading.** v3 covered **§3.1 through §3.4.4 only** and wrote **23 flags (#52–#74): 13 POTENTIAL ROADBLOCK, 10 PENDING VERIFICATION, 0 SEVERE.** §3.5, the Conclusion, the Recommendations and the back matter are covered in the **v4** block further below (#75–#95).
>
> **Attestation:** this pass was **read-only**. No script was run, no seed was set, no number was regenerated. Where a finding turns on program behavior it is assigned to `math-auditor` or `code-stressor` with a named run. ~~Two findings (#75, #74)~~ → **one finding in this range (#74)** rests on arithmetic performed by hand **on the manuscript's own printed values**; that arithmetic requires no execution and is labelled accordingly. (The other, the §3.5 category-mean defect, is in the v4 range and is registered as **#82**.)
>
> **Five flags in this range carry repairs applied in v4** — #53, #59, #64, #68, #70. Each repair is appended directly beneath the original flag as a marked **v4 CORRECTION** block; **no original finding text was deleted or rewritten.** See Project Log Entry 6.

---

### §3.1 — Species Performance of Selected TFTs

**#52 — §3.1.1 / §3.3.2 vs §3.1.4 / §3.4.4 — Narra's and Akleng-parang's crown diameters are each reported as two different numbers.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.1.1 — *"They exhibit expansive crown diameters of 34 meters and 30 meters respectively."* §3.3.2 — *"three large Narra trees (CD = 34.0m)."* Against §3.1.4 — *"These two species share the largest crown diameters in the TFT pool (24.0 m and 23.0 m, respectively)"* and §3.4.4 — *"(λ=1.9, CD=23.0 m for Narra)."*
- **Objection:** the manuscript silently alternates between Table 3's range **maxima** (Narra 34, Akleng-parang 30) and its range **midpoints** (Narra 23, Akleng-parang 24) for the same parameter, in adjacent subsections, with no statement of which summary statistic is in force. Crown diameter is the paper's single dominant parameter (§3.5.1, SI = 0.4435) and the entire "performance cliff" argument is built on it. A reviewer cannot determine what value the model actually used, and therefore cannot check a single downstream number. This is the same failure mode as the grid-resolution defect (#28/#33), in the parameter that matters most.
- **Closes when:** `math-auditor` reports the production `TreeSpecies.SPECIES_DATA` crown-diameter value used per species, states whether ranges are sampled or a point value is taken, and the Editor propagates one convention through §3.1, §3.3, §3.4 and §3.5 with the convention named explicitly.

**#53 — §3.1.2 — the six normalized cooling-potential scores have no shown derivation, and only four of six are reported.** · PENDING VERIFICATION

- **Where:** *"Narra achieves the highest score of 0.943. This is followed closely by Akleng-parang at 0.856… Talisay scores only 0.392 and Duhat scores the lowest at 0.284."*
- **Objection:** (a) Kabiki and Banaba are never given a score — four of six species are reported, and the two omitted are precisely the ones whose LAI is highest (Kabiki 4.5–6.0), which is the omission least favourable to the paper's shading-dominance thesis. (b) The four reported values are not reproducible from Table 3 via §2.3.1's formula `0.70·(CPA/CPA_max) + 0.30·(LAI/LAI_max)` under either summary convention. Hand check (not executed): using range maxima, Narra ≈ 0.95 (reported 0.943 ✓) but Akleng-parang ≈ 0.72 against a reported 0.856; using midpoints, Akleng-parang **outranks** Narra, contradicting the text. No derivation, no intermediate values, and no table of normalized CPA/LAI are given.
- **Closes when:** `math-auditor` prints the six normalized cooling-potential values and their normalized CPA/LAI inputs from the production model and confirms which CD/LAI point values feed them; Editor reports all six in a table with the normalization denominators stated.

> **⚠️ v4 CORRECTION to #53 — applied 2026-07-26 by `editorial-flagger`, per Project Log Entry 5 §C and Entry 6.**
> The original finding text above is preserved unaltered. Three of its supporting claims are withdrawn or corrected; the flag itself stands and its class is unchanged (**PENDING VERIFICATION**).
>
> 1. **WITHDRAWN — *"using midpoints, Akleng-parang outranks Narra, contradicting the text."*** Not reproducible under any midpoint convention tried. Using Table 3 CPA midpoints (Narra 510.5, Akleng-parang 480.5): Narra 0.957 vs Akleng-parang 0.830. Using CPA recomputed from CD midpoints (Narra π/4·23² = 415.5, Akleng-parang π/4·24² = 452.4): Narra 0.900 vs Akleng-parang 0.871. **Narra leads under both.** The claim is deleted from the objection.
> 2. **WITHDRAWN — *"the two omitted are precisely the ones whose LAI is highest."*** False for Banaba. Table 3 LAI: Kabiki 4.5–6.0, Talisay 4.0–5.5, Narra 4.0–5.0, **Banaba 3.5–4.5 (fourth of six by midpoint)**, Duhat 2.5–4.0, Akleng-parang 2.5–3.5. Only Kabiki supports the claim. Reduce the objection to: *the highest-LAI species in the pool (Kabiki) is among the two never scored.*
> 3. **RE-CITED.** The 0.70 / 0.30 weighting is stated in **§2.3.2** (`03_methods_2.3_cooling.md:213–215`, α₁ = 0.70, α₂ = 0.30), **not §2.3.1**. §2.3.1 defines only normalized CPA = CPA/CPA_max.
> 4. **STANDS UNCHANGED.** Objection (a) — Kabiki and Banaba are never scored, four of six species reported — is confirmed. And the maxima check stands and is the flag's load-bearing half: under Table 3 range maxima, Akleng-parang computes to **≈ 0.72** against a reported **0.856**, while Narra computes to ≈ 0.95 against a reported 0.943. One of the two reported values is reproducible and the other is not.
>
> *Basis: hand arithmetic on Table 3 (`06_results_discussion.md:85–104`) and §2.3.2; independently reproduced by the orchestrator in Entry 5 §C. No code executed.*

**#54 — §3.1.2 / §3.1.4 / §3.4.3 and Abstract — "shading area dominates evapotranspiration" is a property of the objective function's construction, not an empirical finding.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.1.4 — *"within the current biophysical proxy, where normalized cooling potential weights CPA at 0.7 and LAI at 0.3, shading area dominates the optimizer's selection logic."* Abstract — *"confirming that under the Gaussian decay model, shading area dominates evapotranspiration in cooling effectiveness."* §3.1.2 — *"the algorithm will mathematically favor the larger species."*
- **Objection:** crown diameter enters the objective **twice and multiplicatively** — once through `CPA = (π/4)·C_D²` in the amplitude, and again as the length scale in `exp(−λ(d/C_D)²)`. Shading is additionally assigned a fixed a-priori weight of 0.70. The conclusion that shading area dominates is therefore entailed by the specification, and the word "confirming" in the Abstract asserts empirical support the design cannot provide. §3.1.4 half-concedes this ("within the current biophysical proxy") and the Abstract then drops the qualifier entirely. This is the single most likely reviewer objection in the paper.
- **Closes when:** the claim is reframed as a structural property of the specified objective, not a result; **and** either (a) the two `C_D` pathways are decomposed so the marginal contribution of each is reported separately (`math-auditor`), or (b) the claim is deleted. The Abstract's "confirming" must go regardless. Owner: `editor` after `math-auditor`.

**#55 — §3.1.3 / §3.3.2 / §3.3.3 — claims about what the optimizer does, with no supporting analysis, no ablation, and one self-contradiction.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.1.3 — *"the results show that the ACO avoids placing trees closer than their combined radii would allow. The algorithm seeks configurations where the 'cooling footprints' of adjacent trees touch but do not excessively overlap"*; *"In the absence of this competition factor, the algorithm would simply stack the highest-performing trees (Narra) on top of the most vulnerable grid cells."* §3.3.3 — *"the ACO distributed the five trees to cover the widest possible surface area of the Vulnerable zone."*
- **Objection:** four separate problems. (a) *No metric is reported* — no nearest-neighbour distance distribution, no CCA occupancy histogram, no overlap fraction. (b) The counterfactual "in the absence of this competition factor" describes an **ablation run that is never reported anywhere in §3**. (c) The "combined radii" claim is contradicted by the manuscript's own coordinates: §3.4.4 lists placements at (25,45) and (45,45) — 20 m apart — for a species whose crown diameter is reported as 23–34 m, i.e. substantially *closer* than combined radii. (d) "widest possible" asserts optimality for a metaheuristic that the paper itself says plateaued in the first few iterations, with no optimality gap, no exhaustive baseline, and no random or clustered comparator reported.
- **Closes when:** `code-stressor` runs a CCA-on/off ablation and reports nearest-neighbour spacing statistics and overlap fractions for the retained solutions; `editor` replaces optimality language with heuristic language throughout, or deletes the claims.

---

### §3.2 — Urban Grid Generation and Equity Zone Classification

**#56 — §3.2.1 and §3.2.2 contain no prose at all, and the canonical grid is never characterized.** · **POTENTIAL ROADBLOCK**

- **Where:** the entirety of §3.2 is four lines: two subsection headings and two figure captions (*"Figure 9. Canonical Output of Coarse Grid"*, *"Figure 10. Equity Weights Spatialization Across Coarse Grid"*).
- **Objection:** every downstream result in §3.3, §3.4 and §3.5 is conditional on one grid, and that grid is never described numerically. Not reported anywhere in Results: the P/A/V cell counts for the canonical grid, the V-cell count (which the code fixes deterministically at **8 cells = 8%**, zero seed variance — a striking and highly relevant fact), which morphology preset generated it, the seed, whether it is representative or hand-picked, the distribution of equity weights across cells, or the number of plantable A cells (which bounds the search space the paper invokes in §3.3.1 to explain the plateau). A Results subsection consisting of a figure caption is not reviewable, and a reviewer will read the omission of the V-cell count as concealment once they learn V is deterministic.
- **Closes when:** `code-stressor` emits the canonical grid's composition (P/A/V counts, V-cell count and %, plantable-A count, morphology preset, seed); `editor` writes §3.2 around those numbers and discloses the determinism.

---

### §3.3 — ACO Search Dynamics and Convergence

**#57 — §3.3.1 / §3.4 vs Methods §2.4.1 — the ACO configuration is stated two incompatible ways.** · **POTENTIAL ROADBLOCK**

- **Where:** Methods §2.4.1 — *"The algorithm was configured with a colony size of 50 artificial ants over 100 iterations."* Results §3.4 — *"a best SECPI score of 3.067 over 30 iterations with 15 ants per iteration."* §3.3.1 — *"This gap did not close over 30 iterations."*
- **Objection:** 50 ants × 100 iterations and 15 ants × 30 iterations differ by a factor of **11 in function evaluations** (5,000 vs 450). Every convergence claim in §3.3.1 — the plateau, the persistent best–average gap, the "flat landscape near the optimum" reading — depends on which is true, and the paper's own explanation for the plateau (small effective search space) is far more plausible at 450 evaluations than at 5,000. This is not a typo-class defect: it is an irreproducible method with two mutually exclusive published configurations. Compounds #45 (stated software stack contradicts implementation).
- **Closes when:** `math-auditor` reports `base_aco_config` verbatim from `AuditedCode_1.py` and confirms the values used at each of the five ACO instantiation sites; `editor` corrects §2.4.1 and §3.3/§3.4 to the single true configuration.

> **⚠️ v5 UPDATE to #57 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §E1. Flagger-initiated: Entry 8 did not route this flag to me, but its executed evidence bears on it directly.**
> The original finding text above is preserved unaltered. **The objection is strengthened from "two incompatible ways" to "three"; the class is unchanged (POTENTIAL ROADBLOCK).**
>
> - **STRENGTHENED — the published configurations are not merely incompatible with each other, they are both incompatible with the code.** Entry 8 §E1 spied on the `AntColonySystemACO` constructor during a live evaluation and recorded the production configuration by execution: **`n_ants = 20, n_iterations = 40`**, `n_trees = 5`, `alpha = 1.0`, `beta = 2.0`, `evaporation_rate = 0.5`, `q0 = 0.7`, all read from `base_aco_config`. So the manuscript publishes **50 × 100** (Methods §2.4.1) and **15 × 30** (Results §3.4), and the reference implementation runs **20 × 40**. Three configurations, none matching another: 5,000 vs 450 vs **800** function evaluations. This is the same failure mode as the grid-resolution defect (#28/#33) — a parameter stated three incompatible ways — now confirmed against executed code rather than inferred from prose.
> - **PARTIAL DISCHARGE of the `math-auditor` half of "closes when".** `base_aco_config` is now reported verbatim. **What is still owed:** confirmation of the values used at each of the **five** ACO instantiation sites. Entry 8 verified **one** site — `SensitivityAnalyzer._run_single_evaluation` — and confirmed it inherits `base_aco_config` correctly. The other four are unverified.
> - **Class unchanged.** The editor half is untouched and the defect is now larger, not smaller.
>
> *Basis: Project Log Entry 8 §E1 (Phase C), executed under `.venv` Python 3.14.6. Structural claim — deterministic, not subject to Entry 8's magnitude caveat.*

**#58 — §3.3.1 — ACO hyperparameters appear for the first time in Results and are never specified in Methods.** · PENDING VERIFICATION

- **Where:** *"The exploration parameter q0, set at 0.7, allocates 30% of decisions to random exploration… This is by design: a q0 closer to 1.0 would accelerate convergence but risk premature exploitation."*
- **Objection:** `q0` is introduced in Results with a post-hoc justification and is absent from Methods §2.4.1, which specifies only colony size and iteration count. Also never specified anywhere in the manuscript: the pheromone evaporation/decay rate, the local and global update rules, α and β (heuristic vs. pheromone exponents), τ₀ initialization, and the restart count. Since the implementation is a hand-written Ant Colony **System** (not the generic ACO of §2.4.1, and not scikit-opt per #45), the ACS-specific parameters are exactly what a reader needs to reproduce it. "This is by design" is a rationalization of a value the reader was never given.
- **Closes when:** `math-auditor` enumerates the production `AntColonySystemACO` parameter set; `editor` moves the complete set into a Methods table and deletes the Results-side justification.

> **⚠️ v5 UPDATE to #58 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §E1. Flagger-initiated.**
> The original finding text above is preserved unaltered. **The `math-auditor` half of "closes when" is DISCHARGED; the `editor` half is untouched; the class is unchanged (PENDING VERIFICATION).**
>
> - **DISCHARGED — the production `AntColonySystemACO` parameter set is now enumerated by execution.** Entry 8 §E1: `alpha = 1.0`, `beta = 2.0`, `evaporation_rate = 0.5`, `q0 = 0.7`, `n_ants = 20`, `n_iterations = 40`, `n_trees = 5`, `reference_cutoffs` supplied per call site. `q0 = 0.7` is confirmed — the Results-side value is correct, it is simply in the wrong section.
> - **STILL MISSING FROM THE ENUMERATION, and still absent from the manuscript:** the **local** and **global** pheromone update rules and **τ₀ initialization**. Entry 8 recorded the constructor kwargs, not the update rules. An Ant Colony *System* is distinguished from generic ACO precisely by its local pheromone update, so this is not a cosmetic omission — a reader cannot reimplement ACS from α, β, ρ and q₀ alone.
> - **`n_samples` is not in this set.** See the v5 block on #77: the sensitivity routine's replication count is a hardcoded literal at the call site (`AuditedCode_1.py:3527`) and appears nowhere in `base_aco_config`.
> - **Class unchanged.** The editor deliverable — a complete Methods-side ACS parameter table, and deletion of the Results-side post-hoc justification — has not been done.
>
> *Basis: Project Log Entry 8 §E1 (Phase C), §E2. Structural claim — deterministic.*

**#59 — §3.3.1 — iteration-best and global-best traces are conflated, and the pheromone explanation has no diagnostic behind it.** · PENDING VERIFICATION

- **Where:** *"The best-per-iteration SECPI trace fluctuated between approximately 3.02 and 3.07 across the full run, with no clear monotonic convergence trend. The global best was reached early (within the first few iterations) and was never substantially improved upon."* And: *"indicating that the pheromone reinforcement mechanism did not fully drive the ant colony toward consensus on a single dominant solution."*
- **Objection:** (a) a best-so-far (global-best) trace is monotonically non-decreasing by construction — it cannot "fluctuate" and cannot lack a monotonic trend; either the trace plotted in Figure 11 is the per-iteration best (in which case "no monotonic trend" is expected and uninformative) or the axis is mislabelled. "Never substantially improved upon" is a hedge that hides which quantity is being described. (b) The best–average gap is attributed to pheromone dynamics with **no pheromone-concentration measurement, no solution-diversity or entropy statistic, and no comparison against a q0 sweep**. A mechanistic attribution to a named internal mechanism requires a diagnostic on that mechanism.
- **Closes when:** `editor` defines both traces precisely and matches them to Figure 11's actual series; `code-stressor` either supplies a diversity/pheromone-entropy diagnostic or the attribution is deleted and replaced with a descriptive statement.

> **⚠️ v4 CORRECTION to #59 — applied 2026-07-26 by `editorial-flagger`, per Project Log Entry 5 §C and Entry 6.**
> The original finding text above is preserved unaltered. The **headline is withdrawn and replaced**; the class is unchanged (**PENDING VERIFICATION**).
>
> - **WITHDRAWN — the headline *"iteration-best and global-best traces are conflated."*** The manuscript **names the two traces separately** and is internally consistent on that point: *"The best-per-iteration SECPI trace fluctuated…"* and, as a distinct sentence, *"The global best was reached early."* A per-iteration best legitimately fluctuates. There is no conflation in the prose.
> - **REPLACEMENT HEADLINE:** *§3.3.1 — it cannot be determined which series Figure 11 actually plots, and the pheromone explanation has no diagnostic behind it.* The manuscript describes two traces; Figure 11 is captioned only *"ACO Convergence Line Graph"* and is never cited in the text. Whether the plotted series is the per-iteration best, the global best, the colony average, or some combination is unrecoverable from the manuscript, and objection (a)'s force is now the **figure-to-text mapping**, not a prose defect. Compounds **#81** (no figure in §3 is cited in text).
> - **STANDS UNCHANGED — objection (b).** The best–average gap is attributed to pheromone dynamics with no pheromone-concentration measurement, no solution-diversity or entropy statistic, and no q0 sweep. A mechanistic attribution to a named internal mechanism still requires a diagnostic on that mechanism.
>
> *Basis: re-read of `06_results_discussion.md:220–250` and the Figure 11 caption at :222. No code executed.*

**#60 — §3.3.2 / §3.4.4 — the best configuration's species composition is stated three incompatible ways.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.3.2 opening — *"The best solution selected 3 Narra trees, 1 Talisay, and 1 Kabiki."* §3.3.2 closing, two paragraphs later — *"The inclusion of a smaller-crowned species (Duhat, CD = 11.0m) alongside three large Narra trees."* §3.4.4 — *"utilizing three Narra trees, one Terminalia catappa (Talisay), and one Lagerstroemia speciosa (Banaba)."*
- **Objection:** the fifth species of the headline configuration is Kabiki, then Duhat, then Banaba — within one section, one of them inside a single subsection. This is not a rounding or notation issue; the manuscript does not know what its own best solution is. Everything §3.3.2 and §3.4.4 then infer about complementary spatial niches and species mixing is built on a composition that is not fixed.
- **Closes when:** `code-stressor` regenerates under Option B and emits the best configuration's species vector, coordinates, seed and run ID as a single machine-written table; `editor` writes §3.3.2/§3.4.4 from that table only. Per Entry 4 handoff note 5, no composition claim survives without a named script and fixed seed.

**#61 — §3.3.2 vs §3.4.4 — placement coordinates are mutually inconsistent and none is attributed to a run.** · PENDING VERIFICATION

- **Where:** §3.3.2 — *"The five placements span x-coordinates from 25 to 75 meters and y-coordinates from 5 to 75 meters."* §3.4.4 — *"placements such as (45.0, 85.0) and (75.0, 95.0)"*; and *"trees are positioned at coordinates including (25, 95), (25, 45), and (45, 45)"* for the WITH arm versus *"(25, 15), (15, 15), and (25, 55)"* for WITHOUT.
- **Objection:** (45,85) and (75,95) lie outside §3.3.2's stated y-range of 5–75, so at least two different solutions are being described as though they were one, and the text never says which configuration, k value, arm, restart or seed each coordinate set belongs to. §3.4.4 also refers to *"the JSON placement data"* and *"the Automated Cooling Interpretation Report"* as sources without identifying the files or runs. No coordinate in §3 is traceable.
- **Closes when:** every reported coordinate set is labelled with arm, k, restart index and seed, sourced from a named artefact in `results/`. Owner: `code-stressor` to emit, `editor` to label.

---

### Units and magnitude of the cooling field (§3.3.2, §3.4.4, Conclusion, Abstract)

**#62 — A dimensionless cooling proxy is relabelled as degrees Celsius, with no conversion stated anywhere.** · **POTENTIAL ROADBLOCK**

- **Where:** §2.3.1 defines the proxy on *"a common, dimensionless scale from 0 to 1"*; §2.3.2 calls the total *"a spatially explicit, relative measure of cooling effectiveness"*; §3.1.2 calls it *"a single scalar value between 0 and 1"*; §3.3.2 reports *"a mean intensity of 0.131… a maximum of 0.809… a standard deviation of 0.160"* with **no units**. Then §3.4.4 — *"a global maximum cooling intensity of 1.15 °C and a mean intensity of 0.19 °C… decreased to a maximum of 0.80 °C and a mean of 0.11 °C"*; Conclusion — *"a maximum localized cooling reduction of 0.80 °C and a mean reduction of 0.11 °C"*; Abstract — *"a global cooling reduction of up to 0.809 °C."*
- **Objection:** the same quantity is unitless in §3.3.2 and carries °C in §3.4.4, the Conclusion and the Abstract. **No calibration from proxy units to kelvin is presented anywhere in the manuscript** — no reference ΔT, no scaling constant, no anchoring measurement. Attaching °C to a normalized index manufactures a physical unit. Two aggravating details: (a) §3.4.4's 1.15 °C **exceeds the 0–1 bound** the model's own definition asserts, so the field is not bounded as described and its scale is undefined; (b) the paper's single most quotable claim — the Abstract's 0.809 °C — exists only because of this unstated relabelling. A geoscience reviewer will treat an unconverted index reported in °C as disqualifying.
- **Closes when:** `math-auditor` states whether any °C calibration exists in `AuditedCode_1.py` (I did not execute; expectation unverified) and reports the actual range of the summed cooling field. If no calibration exists, **every °C in the manuscript must be removed** and the quantity reported as a dimensionless cooling index — which eliminates the Abstract's headline number and requires the Abstract, §3.3.2, §3.4.4 and the Conclusion to be rewritten. Substantive rework, not a units edit.

**#63 — §3.3.2 vs §3.4.4 vs Conclusion vs Abstract — the cooling-field statistics are mutually inconsistent, and the "42% cost of equity" depends on which inconsistent value is used.** · PENDING VERIFICATION

- **Where:** mean cooling intensity under the WITH arm is **0.131** (§3.3.2), **0.1305** (§3.4.4 equity paragraph — *"a global average of 0.1305"*) and **0.11** (§3.4.4 efficiency paragraph and Conclusion). Maximum is **0.809** (§3.3.2), **0.80** (§3.4.4, Conclusion) and **0.809 °C** (Abstract).
- **Objection:** (a) 0.131 → 0.11 is not rounding. (b) The headline equity-cost figure is derived from the smaller value: (0.19 − 0.11)/0.19 = 42.1%, matching *"a reduction of approximately 42%"* — but recomputed against the mean reported two paragraphs earlier, (0.19 − 0.131)/0.19 = **31%**. The manuscript's most rhetorically important trade-off number moves by 11 percentage points depending on which of its own two means is used, and the Conclusion repeats 42% without noting the alternative. (c) The Abstract describes 0.809 as a *"global cooling reduction"* when §3.3.2 identifies it as the maximum **directly beneath a canopy**, against a grid mean of 0.131 — a local peak presented as a global effect. This error mode will survive regeneration unless corrected explicitly. Arithmetic above is by hand on the manuscript's printed values; nothing executed.
- **Closes when:** `code-stressor` regenerates under Option B and emits one mean, one max, one SD per arm from a single named run; `editor` reports identical statistics in §3.3.2, §3.4.4, Conclusion and Abstract, derives the equity-cost percentage in-text from the stated means, and never labels a local maximum "global."

---

### §3.4 — SECPI Framework Outcomes

**#64 — §3.4.1 — the reported per-`k` mean SECPI values are arithmetically incompatible with the individual configuration values from the same dataset; two incommensurable experiments are interleaved.** · **POTENTIAL ROADBLOCK** *(escalation of #44)*

- **Where:** §3.4.1 — *"Mean SECPI rises from k=1 (approximately 2.990) through k=4 (approximately 3.017)… drops to approximately 2.999… recovering slightly at k=6 (approximately 3.009)… The overall range of mean SECPI across all k values spans only about 0.027."* Against §3.4.2/§3.4.3, from the same 63-configuration dataset: mono-species 4.3916 (Akleng-parang), 4.3856 (Narra), 3.1065 (Talisay), 3.094 (Kabiki), 3.068 (Banaba), 3.0396 (Duhat).
- **Objection:** hand arithmetic on the manuscript's own printed values (no execution required): the six k=1 configurations have mean **3.514**, not 2.990. §3.4.1's stated k=1 mean is **below the lowest single k=1 value the manuscript itself reports** (3.0396). The same subsection then explains its own impossible number in terms of the correct data — *"At k=1, the mean is dragged down by the four small-crowned mono-species configurations… all of which score below 3.11"* — so the narrative is written against the 63-subset data while the numbers are not. The values 2.99–3.02 match the *tree-count* experiment's scale (§3.4's best 3.067; §3.3.1's trace 3.02–3.07; §3.5.1's baseline 3.0576), not the palette-size experiment's (3.02–4.39). §3.4.1 therefore appears to report the tree-count experiment's means as palette-size means. This is #44's `k` collision manifesting as a numerical error, not a notation preference, and it invalidates §3.4.1's entire diversity-trend argument including the "dip at k=5" explanation.
- **Closes when:** `code-stressor` recomputes per-`k` means, SDs and n from `legacy/archive/corrected_outputs/run_20260213_222844/combinatorial/all_combos_with_vuln.csv` and from the regenerated Option-B sweep, reporting them separately from the tree-count experiment. D-07 must close first so the two axes carry distinct symbols. **Until then §3.4.1 must not be rewritten — it must be regenerated.**

> **⚠️ v4 CORRECTION to #64 — applied 2026-07-26 by `editorial-flagger`, per Project Log Entry 5 §C and Entry 6.**
> The original finding text above is preserved unaltered. **The attestation is corrected; the finding survives intact and the class is unchanged (POTENTIAL ROADBLOCK).**
>
> - **CORRECTED ATTESTATION.** The flag states its arithmetic was performed *"on the manuscript's own printed values (no execution required)"* and cites §3.1.4 / §3.4.2 / §3.4.3 as the source of all six mono-species values. **Two of the six — Kabiki 3.094 and Banaba 3.068 — appear nowhere in §3.** They originate in the recovered `run_20260213_222844` combinatorial CSV, reached via `docs/DECISIONS.md` D-06. The six-value mean of **3.514** is therefore *mixed-source* arithmetic — four manuscript values plus two CSV values — not manuscript-internal arithmetic. Label it as such.
> - **THE FINDING IS UNAFFECTED AND IS MANUSCRIPT-INTERNAL.** The decisive comparison needs none of the CSV values: §3.4.1's stated k=1 mean of **2.990** is **below 3.0396**, the *lowest single k=1 value the manuscript itself prints* (mono-species Duhat, §3.4.3). A mean below its own printed minimum is impossible from that dataset regardless of what the other five values are. That check is entirely manuscript-internal and requires no execution.
> - **Class unchanged: POTENTIAL ROADBLOCK.** Nothing in this correction reduces severity; it narrows the evidentiary base to the half that needs no external source, which strengthens it.
>
> *Basis: `06_results_discussion.md` §3.4.1–§3.4.3; `docs/DECISIONS.md` D-06. No code executed.*

**#65 — §3.4.2 vs Abstract — the manuscript's own Results declare the Abstract's headline 0.03% to be stochastic noise.** · PENDING VERIFICATION *(refines #6, #46)*

- **Where:** §3.4.2 — *"The spread between the best configuration (4.3930) and the best mono-species result (4.3916) is only 0.0014, representing a difference of approximately 0.03% in SECPI. **This margin falls well within the stochastic variation inherent to the ACO metaheuristic across independent runs.**"* Abstract — *"functional diversity offered negligible improvement (0.03%) over well-chosen mono-species solutions."*
- **Objection:** the Abstract advances as a finding a quantity the Results explicitly classify as unresolvable against run-to-run noise. Either the number means something — in which case §3.4.2's caveat must be replaced by a quantified noise floor — or it does not, in which case it cannot be an Abstract headline. The "stochastic variation inherent to the ACO" is itself never quantified: no SD across restarts, no repeated-run distribution, no n. The manuscript uses an unmeasured noise level to dismiss a difference here and to *not* dismiss smaller differences in §3.4.3 (see #68).
- **Closes when:** `code-stressor` reports SD and range of best-SECPI across the 5 restarts per configuration, establishing an explicit noise floor; `editor` removes from Abstract and Results every difference below it. Interacts with #46 — the claim must also be reframed from "diversity" to "palette size."

**#66 — §3.4.2 — non-submodularity is used as the explanatory mechanism for species underutilization but is never demonstrated.** · PENDING VERIFICATION

- **Where:** §3.4.2 — *"This underutilization is consistent with the non-submodular structure of the cooling objective."* Methods §2.1 states only an expectation: *"the cooling function is **expected to be** non-submodular."*
- **Objection:** non-submodularity is load-bearing twice — it justifies choosing a metaheuristic over a greedy algorithm with approximation guarantees (§2.1, §2.5.1), and it is invoked in Results as a causal explanation. It is never tested. Demonstrating it is cheap and decisive: exhibit sets A ⊂ B and an element x with `f(A ∪ {x}) − f(A) < f(B ∪ {x}) − f(B)`. Its absence means the paper's central mathematical framing rests on an assumption while Results presents it as an established property. A discrete-optimization reviewer will ask for the counterexample immediately.
- **Closes when:** `math-auditor` exhibits a numerical violation of submodularity from the production cooling model (sets, element, and all four function values printed), or the claim and the ACO justification depending on it are both softened to "assumed."

**#67 — §3.4.3 and Abstract — the "28% performance cliff" is the gap between two adjacent ranks, presented as a between-group effect.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.4.3 — *"the transition occurs between rank 48 (Narra + Kabiki + Duhat, SECPI = 4.3651) and rank 49 (Banaba + Kabiki + Duhat, SECPI = 3.1336), a drop of approximately 1.23 SECPI units or 28%."* Abstract — *"configurations lacking large-crowned species (Akleng-parang and Narra) scored 28% lower."*
- **Objection:** the arithmetic is internally traceable (1.2315 / 4.3651 = 28.2%), but it describes a single adjacent pair in a rank-ordered list of 63 values, and the Abstract restates it as a **group-level** difference. No group means, no dispersion, no n per group, no rank-based test. Separately, `docs/DECISIONS.md` D-06 derives the same "28%" a *different* way — (4.3916 − 3.13)/4.3916 = 28.73% — so two incompatible derivations of the manuscript's second-most-quoted number are already on the project record. The largest gap in any sorted list is guaranteed to exist; quantifying a between-group effect from it is not licensed.
- **Closes when:** `code-stressor` computes, from the regenerated sweep, group means ± SD and n for subsets containing vs. lacking a large-crowned species, plus a rank-based test (Mann–Whitney U) with effect size; `editor` reports the group contrast rather than the adjacent-rank gap, and states which single derivation is used.

**#68 — §3.4.3 — differences of similar or larger magnitude are dismissed as noise in one paragraph and treated as causal effects in the next.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.4.2 dismisses **0.0014** as *"well within the stochastic variation."* §3.4.3 then asserts *"Mono-species Talisay (SECPI = 3.1065) outperforms mono-species Duhat (3.0396) despite comparable LAI, **because** Talisay's slightly larger crown diameter (12.0 m vs. 9.5 m) provides a broader decay radius"* (Δ = **0.067**), and *"Banaba + Kabiki + Duhat (SECPI = 3.1336) marginally outperforms any of its constituent mono-species configurations, indicating that… functional mixing does provide a slight additive benefit"* (Δ = **0.0396** over the best constituent, Kabiki at 3.094).
- **Objection:** §3.3.1 reports the ACO's best-versus-average gap as **0.05 to 0.07 SECPI units**. Both effects claimed in §3.4.3 sit at or below that scale, from **n = 1 versus n = 1**, with no dispersion and no repeated runs — yet one receives a causal mechanism ("because") and the other is generalized into a statement about functional mixing. The evidentiary standard is inconsistent within one section and is applied in whichever direction supports the surrounding narrative. This is the clearest selective-reporting pattern in the manuscript and is the sort of passage a hostile reviewer quotes verbatim.
- **Closes when:** `code-stressor` establishes a quantified noise floor from the 5 restarts per configuration; every §3.4.3 claim below it is deleted, and survivors are reported with SD and n. Owner: `code-stressor` then `editor`.

> **⚠️ v4 CORRECTION to #68 — applied 2026-07-26 by `editorial-flagger`, per Project Log Entry 5 §C and Entry 6.**
> The original finding text above is preserved unaltered. **One number is re-sourced; the objection is unchanged and the class is unchanged (POTENTIAL ROADBLOCK).**
>
> - **RE-SOURCED.** The second effect is quantified in the flag as **Δ = 0.0396**, the margin of Banaba + Kabiki + Duhat (3.1336) over *Kabiki at 3.094*. **Kabiki 3.094 is a D-06 CSV value, not a manuscript value** — the same sourcing defect as #64. Using only what §3 prints, the mixture's margin over its one reported constituent (mono-species Duhat, **3.0396**) is **3.1336 − 3.0396 = 0.094**.
> - **THE OBJECTION HOLDS AT EITHER VALUE**, and slightly more strongly at the corrected one. §3.3.1 reports the ACO's best-versus-average gap as **0.05–0.07 SECPI units**; §3.4.2 dismisses **0.0014** as *"well within the stochastic variation."* Both §3.4.3 effects — Talisay − Duhat = 3.1065 − 3.0396 = **0.0669** (manuscript-internal, unaffected) and the mixture margin of **0.094** — sit at or just above the same unmeasured noise scale, from n = 1 versus n = 1, with no dispersion. The inconsistent evidentiary standard within one section is the finding, and it is untouched.
> - **Quote the manuscript-only figure (0.094) going forward.** Cite 0.0396 only alongside its D-06 CSV provenance.
>
> *Basis: `06_results_discussion.md` §3.4.2–§3.4.3; `docs/DECISIONS.md` D-06. No code executed.*

---

### §3.4.4 — Cross-Scenario Validation

**#69 — The framework's central validation uses the framework's own objective function as the outcome variable. The result is guaranteed by construction.** · **POTENTIAL ROADBLOCK** *(escalation of #39)*

- **Where:** §3.4.4 — *"The framework's central claim is that embedding spatial equity into the optimization objective produces meaningfully different, and more just, cooling outcomes than efficiency-only optimization. To test this…"* and the result: *"In the baseline scenario… a low SECPI score of 1.5… In contrast, the equity-weighted scenario produced a significantly higher mean SECPI of 3.08."*
- **Objection:** SECPI multiplies each weighted class shift by the mean equity weight `W_e,k`. The WITHOUT arm sets all equity weights to unity (§3.4.4: *"all equity weights were set to unity"*), the WITH arm carries weights up to 2.0. **SECPI_WITH > SECPI_WITHOUT is therefore an algebraic consequence of the manipulation, not a finding.** Optimizing an objective and then reporting that the objective is higher is circular; it establishes nothing about cooling delivered, about equity of outcome, or about justice. The two arms also optimize different functions, so the two SECPI values are not on a common scale and their difference has no interpretation. D-03 exists precisely to specify a SECPI-independent outcome metric; §3.4.4 as written does not use one, and the Conclusion inherits the circularity (*"The equity-weighting component of SECPI proved effective"*).
- **Closes when:** D-03 closes on a SECPI-independent metric (recommended: proportion of delivered cooling landing in V-zones); `code-stressor` executes the paired Wilcoxon design (n = 30, paired on grid and k) and reports test, n, statistic, two-sided p and rank-biserial effect size; `editor` rebuilds §3.4.4 around that metric. **The SECPI-vs-SECPI comparison must not remain the validation, in any wording.**

**#70 — §3.4.4 — a second unsupported significance claim, plus the software's own hardcoded verdict string quoted as confirmation.** · **POTENTIAL ROADBLOCK** *(escalation of #39)*

- **Where:** *"the equity-weighted scenario produced a **significantly** higher mean SECPI of 3.08"*; *"The Automated Cooling Interpretation Report provides a direct answer… The report classified this outcome as **'[SUCCESS] HIGH EQUITY,'** confirming that the algorithm prioritized vulnerable zones above the global baseline"*; *"The quantitative results confirm that the SECPI framework successfully redirects the optimization search process."*
- **Objection:** two distinct defects. (a) "Significantly" appears with no test, no n, no p, no dispersion — a second instance beyond the §2.5.2 sentence #39 covers, making the defect systemic rather than local. (b) Worse, the manuscript cites **its own program's hardcoded label** as evidence. Per `docs/STATE.md`, `AutomatedInterpreter` emits verdict strings from fixed magnitude thresholds (`interpret_scenario_comparison()` prints `"Difference: SIGNIFICANT"` whenever `|Δ| > 0.1`). Quoting a threshold-triggered string as a classification "confirming" a scientific claim is self-validation: the software was told when to print SUCCESS and it printed SUCCESS. A reviewer who reads the code will find this, and it contaminates trust in every other reported outcome.
- **Closes when:** every instance of "significant/significantly" not backed by the D-03 test is removed (`editor`, manuscript-wide sweep); every quotation of an interpreter verdict string is removed and replaced by the underlying numbers; `math-auditor` enumerates which thresholds emit which strings so the Editor can confirm none survive.

> **⚠️ v4 CORRECTION to #70 — applied 2026-07-26 by `editorial-flagger`, per Project Log Entry 5 §C and Entry 6.**
> The original finding text above is preserved unaltered. **Objection (b) is demoted from assertion to hypothesis; objection (a) stands; the class is unchanged (POTENTIAL ROADBLOCK).**
>
> - **DEMOTED TO HYPOTHESIS — objection (b).** The flag asserts as established fact that *"the software was told when to print SUCCESS and it printed SUCCESS,"* i.e. that `"[SUCCESS] HIGH EQUITY"` is emitted by a hardcoded magnitude threshold. **No project record establishes this for that string.** `docs/STATE.md` documents a *different* function — `AutomatedInterpreter.interpret_scenario_comparison()`, which prints `"Difference: SIGNIFICANT"` on a hardcoded `|Δ| > 0.1`. Extending that behaviour to `"[SUCCESS] HIGH EQUITY"` is **inference by analogy from a different code path**. Read the objection as: *the manuscript quotes a verdict string produced by its own interpretation layer as external confirmation, and the project has already documented at least one such string as threshold-triggered rather than test-backed. Whether this particular string is threshold-triggered is unverified.*
> - **The quotation itself is verbatim-accurate** — §3.4.4 does print `"[SUCCESS] HIGH EQUITY"` and does describe it as *"confirming that the algorithm prioritized vulnerable zones above the global baseline."*
> - **OWNER FOR THE OPEN HALF:** `math-auditor`. **Named artefact:** an enumeration, from `legacy/AuditedCode_1.py`, of every verdict string `AutomatedInterpreter` can emit, the condition that emits it, and whether any is backed by a statistical test. Until that exists, the flag may not be quoted as showing self-validation — only as showing an *unattributed* verdict string used as evidence.
> - **STANDS UNCHANGED — objection (a).** *"the equity-weighted scenario produced a significantly higher mean SECPI of 3.08"* carries no test, no n, no p and no dispersion. Confirmed, and it is a second instance beyond the §2.5.2 sentence #39 was scoped to, which makes the defect systemic. This half alone sustains the POTENTIAL ROADBLOCK class.
>
> *Basis: `06_results_discussion.md` §3.4.4; `docs/STATE.md` "Interpretation-layer hazard". No code executed — that is precisely why (b) is a hypothesis.*

**#71 — §3.4.4 — the claim that the two arms differ in one variable only is false as described, and the plantability of V cells is stated inconsistently.** · PENDING VERIFICATION

- **Where:** §3.4.4 — *"a benchmark scenario where vulnerability zones were **reclassified as Prohibited cells** and all equity weights were set to unity… Both scenarios used identical CA-generated urban morphologies, the same ACO hyperparameters, and the same five-tree budget, **isolating the equity mechanism as the sole experimental variable**."* Against Methods §2.2.4 — *"tree placement is permitted only in cells where S(cell) = A."*
- **Objection:** two things change at once — the weight field **and** the cell-state map. Whether that confounds the comparison turns on a fact the manuscript states two ways. If planting is permitted only in A cells (§2.2.4), V cells were never plantable, reclassifying them to P is a pure weight manipulation, and §3.4.4's rationale (*"the optimizer has no mechanism to distinguish socially sensitive areas"*) describes something the weight reset already accomplishes — making the reclassification language misleading. If V cells *were* plantable, the feasible region shrank, the "sole experimental variable" claim is false, and the arms are not comparable. A reader cannot tell which. Note also that #47 records the WITHOUT arm as near-degenerate (3 distinct SECPI values across 63 configurations); §3.4.4 presents that degeneracy as evidence *in favour of* the equity mechanism (*"the equity mechanism… enriches the fitness landscape"*) rather than as a caveat on using a discrimination-free arm as a baseline.
- **Closes when:** `math-auditor` reports whether V ∈ plantable set in each arm and whether anything besides `W_e` differs between the two ACO instantiations; `editor` states the manipulation exactly. If the feasible set changes, D-03's design must be revisited before the test is run.

**#72 — Methods Table 2 vs §3.4.4 — the equity-weight scheme, the paper's central contribution, is operationalized two incompatible ways.** · **POTENTIAL ROADBLOCK**

- **Where:** Methods Table 2 assigns weights by **zone type** — *"Near schools/health centers 2.0 · High-density residential 1.5 · Commercial/industrial 1.0 · Parks/empty lots 0.5"* — each with a paragraph of published justification. Results §3.4.4 describes weights as **distance bands from V cells**: *"fine-grid cells within or near vulnerable zones carry weights of 2.0 (within 10 m) or 1.5 (within 20 m), compared to a baseline weight of 1.0 elsewhere."*
- **Objection:** these are different mechanisms with different spatial footprints and different justifications. Under Table 2 the weight is a property of land use; under §3.4.4 it is a step function of distance to a V cell. The **0.5 class disappears entirely from Results** — the only sub-unity weight, the only one that could penalize a placement, is never mentioned again, so the manuscript never establishes whether it was implemented at all. Methods spends four justification paragraphs defending a table Results does not appear to use. Since equity weighting is the paper's claimed novelty, an unspecified weight field is fatal to §3.4.4.
- **Closes when:** `math-auditor` reports the implemented weight assignment from code (including whether the 10 m / 20 m bands and the 0.5 class exist), and `editor` corrects whichever of Table 2 or §3.4.4 is wrong along with the justification paragraphs. If the implemented scheme is distance-banded, Table 2's zone-type citations no longer support it and `deriver` must source new grounding.

**#73 — §3.4.4 — an uncited empirical claim, attributed to physical processes the model does not represent.** · PENDING VERIFICATION

- **Where:** *"…produces a cooling footprint that extends well beyond the physical crown boundary, consistent with the empirical finding that tree cooling effects propagate 2 to 3 crown radii into the surrounding environment through **advective and radiative** processes."*
- **Objection:** (a) "the empirical finding" carries **no citation** — the only bare appeal to empirical literature inside Results. (b) It attributes the modelled envelope to advection, which the model explicitly does not implement: §2.3 states wind modulation is only *"indirectly considered through crown geometry and spacing"* and §2.6 lists absent wind dynamics as a stated limitation. Explaining a purely geometric distance-decay kernel by naming transport processes the model omits is post-hoc physical dressing, and it contradicts the manuscript's own limitations section. Compounds #50 (kernel has no literature precedent) and #49 (λ's attribution is mismatched): an author-constructed envelope is being retrofitted with borrowed physics.
- **Closes when:** `deriver` either sources the 2–3 crown-radii claim to a real study (and states whether that study's mechanism is compatible with a geometric Gaussian kernel) or the sentence is deleted; `editor` removes the process attribution regardless, since no advective term exists.

**#74 — §3.4.4 — the 4.80% coverage interpretation rests on a per-tree footprint that does not follow from the model's own parameters, and its denominator is never reported.** · PENDING VERIFICATION

- **Where:** *"Under WITH VULN, 4.80% of vulnerable fine-grid cells received cooling intensity above 0.5… Each Narra tree's high-intensity zone (above 0.5) extends roughly 15 m from its trunk, covering approximately 707 m² per tree, or 3,535 m² for five trees. Against a total grid area of 10,000 m², this corresponds to theoretical maximum high-intensity coverage of about 35%."*
- **Objection:** hand arithmetic on the manuscript's own parameters (**not executed** — `math-auditor` to confirm): using the same subsection's stated peak 0.85, λ = 1.9 and C_D = 23.0 m, the 0.5 isopleth solves `0.85·exp(−1.9·(d/23)²) = 0.5` → d ≈ **12.2 m**, i.e. ≈ **470 m²** per tree, not 15 m and 707 m². The 707 figure is exactly `π·15²` and also exactly Table 3's maximum CPA for Akleng-parang, which suggests transposition rather than derivation. Three further defects: the 35% "theoretical maximum" ignores the crown overlap the same section insists is avoided; the calculation is performed for Narra and applied to a mixed-species five-tree configuration; and the **denominator is never given** — the number of vulnerable fine-grid cells appears nowhere in §3 (per `STATE.md` the code fixes V at 8 coarse cells = 800 fine cells), so 4.80% cannot be checked or interpreted. A percentage whose denominator is withheld is not reportable.
- **Closes when:** `math-auditor` derives the 0.5-isopleth radius from the production model and reports the per-tree high-intensity area; `code-stressor` reports the V fine-cell count and the raw counts behind 4.80%; `editor` rewrites from those numbers or deletes the coverage argument.

---

## v4 — New flags #75–#95 (§3.5 Sensitivity Analysis, Conclusion, Recommendations, back matter)

> **This block discharges the `## Resuming This Review — PLACEHOLDER` stub that stood here from 2026-07-25 to 2026-07-26.** The stub's substance is preserved in the "TRUNCATION CLOSED" notice in the Executive Summary and in Project Log Entry 5 §A; it is not reproduced again.
>
> **Scope:** `manuscript/sections/06_results_discussion.md` **§3.5 only** (lines 597–725) and `manuscript/sections/07_conclusion.md` **in full** (Conclusion, Recommendations, Individual Author's Contributions, Acknowledgment). §3.1–§3.4.4 were **not** re-read or re-flagged — that work is #52–#74 and was independently verified in Entry 5 §C. Where a v4 finding compounds one of those, it cites it rather than restating it.
>
> **21 flags: 15 POTENTIAL ROADBLOCK, 5 PENDING VERIFICATION, 1 ROADBLOCK (SEVERE).** Registered in document order. The v3 preamble predicted 14 / 5 / 1 for this range; the true split was derived independently and then compared. It is close but the *sets* differ — see the forward-reference mapping in the Executive Summary.
>
> **Attestation:** read-only. **No code was executed.** Every number asserted below is (i) a verbatim manuscript value cited by file and line, (ii) hand arithmetic on such values with the working shown inline, or (iii) a value cited from a named log entry or `DECISIONS.md` and labelled as such. Where a finding turns on program behavior it is assigned to `math-auditor`, `code-stressor` or `deriver` with a named artefact.

---

### §3.5.1 — Parameter-Specific Level Sensitivity

**#75 — Methods §2.5.3 names the Morris method; §3.5.1 executes a local two-level OAT, and §2.5.3's stated parameter scope excludes the parameter that produces the headline result.** · **POTENTIAL ROADBLOCK**

- **Where:** Methods §2.5.3 (`05_methods_2.5_2.6_vv.md:117–121`) — *"Parameter uncertainty—specifically regarding allometric coefficients for Leaf Area Index (LAI) and cooling decay constants, is propagated through the model via a **Morris-method One-at-a-Time (OAT) screening approach**."* Against Results §3.5.1 (`06_results_discussion.md:608–612`) — *"Each parameter was evaluated at its low and high bounds while all others were held at baseline values, and the resulting SECPI was averaged over three independent ACO runs per configuration… **The baseline SECPI was 3.0576.**"*
- **Objection:** two defects, both consequential.
  **(a) The method executed is not the method named.** The Morris method is a *global* screening design: randomized trajectories from multiple dispersed base points, yielding elementary-effect statistics μ, μ\* and σ, where σ is specifically what diagnoses non-linearity and interaction. What §3.5.1 describes is a *local* two-level OAT from a **single** baseline — one base point, no trajectories, no elementary effects, and no μ\*/σ reported anywhere. That is strictly weaker, and it is weaker in exactly the dimension that matters here: §3.4.2 and §2.1 both assert the objective is **non-submodular**, i.e. interaction-dominated, and a single-base-point OAT cannot see interactions at all. The manuscript names the right method and reports the wrong one.
  **(b) The headline parameter is outside Methods' stated uncertainty scope.** §2.5.3 scopes uncertainty quantification to *"allometric coefficients for LAI and cooling decay constants"* — by §3.5.1's own category definitions that is 24 + 3 = **27 of 40** parameters. Crown diameter and height (12 parameters) and the weighting ratio (1) are outside it. The single dominant result of the entire sensitivity analysis — Narra crown diameter, SI 0.4435 — comes from a parameter the Methods' uncertainty protocol does not cover.
  This is not a wording mismatch. §3.5.3's robustness conclusion, the Conclusion's *"Sensitivity Index = 0.46"* claim, and the field-measurement prescription all rest on a design the Methods section does not describe.
- **Closes when:** the research lead states which design was actually run. If Morris was run, `code-stressor` reports the trajectory count, Δ, and μ\*/σ per parameter and §3.5.1 is rewritten from them. If a local OAT was run, **§2.5.3 must stop claiming Morris** and §3.5.3's robustness inference must be requalified as local-only, since a single-base-point OAT licenses no statement about a non-submodular response surface. Owner: `code-stressor` to characterize, `editor` to reconcile §2.5.3 with §3.5.

> **⚠️ v5 UPDATE to #75 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §A, §B and §D.**
> The original finding text above is preserved unaltered. **The flag is RESOLVED AS TO ITS QUESTION and remains OPEN AS TO ITS REMEDY. Class unchanged: POTENTIAL ROADBLOCK.** The "closes when" clause below **replaces** the one above.
>
> **VERDICT: (c) — the code implements something that is neither Morris nor a valid local OAT.** Both §2.5.3 and §3.5.1 misdescribe what runs, for different reasons, and the second was not anticipated by this flag.
>
> **(a) CONFIRMED — it is not Morris.** Entry 8 wrapped `SensitivityAnalyzer._run_single_evaluation` with a recorder and ran `run_oat_analysis(n_samples=3)`. Executed:
>
> | #75's question | Executed answer |
> |---|---|
> | Sampling design | Two-level factorial-by-coordinate: each factor at `{low, high}`, all others nominal. 40 factors. |
> | Base points | **One**, hardcoded at `run_oat_analysis` lines 927–932. Every one of the 9 non-empty cooling vectors differs from the nominal in **exactly one** coordinate. |
> | Evaluations per parameter | **6** (3 low + 3 high). Plus 3 baseline. **243 total** = 3 + 40 × 2 × 3, matching the prediction exactly. |
> | Trajectories | **None.** No trajectory construction, no randomized start, no step size Δ, no `r` parameter anywhere in the class. |
> | Statistic per parameter | **One:** `sensitivity_index = \|mean(high) − mean(low)\| / baseline_secpi` (line 1000). **No μ, no μ\*, no σ, no SD, no n.** |
>
> Morris requires all five of the things absent here. **"Morris-method OAT screening" is not implemented anywhere in `AuditedCode_1.py`.**
>
> **(b) CONFIRMED AGAINST CODE, not merely against prose.** Executed `_define_parameters()`: `TOTAL PARAMETERS SWEPT = 40`, `{'Cooling_Model': 3, 'Weighting': 1, 'Species_Morphology': 12, 'Species_Allometry': 24}`. §3.5.1's "40 parameters" is confirmed and **#82's forced membership (12 + 24 + 3 + 1) is confirmed against the implementation.** §2.5.3's stated scope — *"allometric coefficients for LAI and cooling decay constants"* — therefore covers **27 of 40** parameters, excluding the 12 morphology parameters that carry the headline result and the 1 weighting parameter. Objection (b) stands exactly as written.
>
> **(c) NEW — and this is why the verdict is (c) rather than (b): the evaluator leaks state, so it is not a valid local OAT either.** §3.5.1's *"all others were held at baseline values"* — which **is** the definition of a local OAT — **is false in the implementation.** `_run_single_evaluation` writes into the class-level `TreeSpecies.SPECIES_DATA` and never restores it. Because `_define_parameters()` iterates `Cooling_Model → Weighting → Species_Morphology → Species_Allometry`, only the 3 baseline plus 24 Cooling_Model/Weighting evaluations run against pristine species data; from the first `Species_Morphology` evaluation onward, contamination accumulates monotonically. **The executed design is a sequentially contaminated, order-dependent two-level sweep that matches neither named method.** Registered separately and in full as **#96** — this flag depends on it and cannot close before it.
>
> **REVISED "Closes when" — the research-lead question is now THREE-WAY, not two-way.** The old clause offered "Morris or local OAT." That framing is obsolete because neither was run. The research lead must choose among:
> 1. **Implement true Morris.** Requires a new routine: trajectory sampling, a Δ grid, μ\*/σ per factor. Entry 8's cost sketch, offered as information and not as a recommendation: at r = 10 trajectories × 41 evaluations ≈ 410 ACO runs ≈ 13 min per arm at the measured 1.92 s/evaluation. Affordable.
> 2. **Repair to a clean local OAT.** The **#96** state-leak fix plus an `n_samples` raise. One `try/finally` plus run time. §2.5.3 must then stop claiming Morris, and §3.5.3's robustness inference must be requalified as local-only.
> 3. **Report the contaminated sweep as-run.** Recorded here for completeness because it is formally available; it requires disclosing the order-dependence and the geometric LAI compounding in Methods, and no defensible sensitivity claim survives it. **Not recommended by this register.**
>
> **This flag no longer closes on characterization — it closes on a decision plus a re-run.** `code-stressor` cannot "characterize" the design further; it has been characterized. **Owner: research lead to choose (1), (2) or (3); this belongs in `docs/DECISIONS.md` as a numbered item — the flagger does not open `D-xx` entries.** Then `code-stressor` executes, `editor` reconciles §2.5.3 with §3.5.
>
> *Basis: Project Log Entry 8 §A1, §A3, §D4 (Phases A, B, G). All claims in this block are structural and deterministic; none depends on a magnitude and none is subject to Entry 8's single-run caveat.*

**#76 — §3.5.1 — the sensitivity baseline (SECPI = 3.0576) matches no configuration reported anywhere in the manuscript, and its parameter vector is never stated.** · PENDING VERIFICATION

- **Where:** `06_results_discussion.md:612` — *"The baseline SECPI was 3.0576."* Against every other SECPI value in §3: §3.4's best **3.067**; §3.4.1's per-k means **2.990 / 3.017 / 2.999 / 3.009**; §3.4.4's equity-arm mean **3.08**; §3.3.1's convergence trace **3.02–3.07**; the combinatorial range **3.023–4.393**.
- **Objection:** 3.0576 appears exactly once in the manuscript and corresponds to nothing else in it. The reader is never told which experiment the baseline belongs to (tree-count or palette-size — the #44/#64 collision), which k, which grid, which morphology preset, which seed, which arm (WITH or WITHOUT VULN), or which parameter values constitute "baseline" for the 40 swept parameters. **Every one of the 40 SI values is a ratio to this number**, so an unattributed baseline makes the entire sensitivity analysis unreproducible in principle, not merely unverified.
  A second, sharper problem sits inside the same subsection. Hand arithmetic on the manuscript's printed values: the low-bound sweep gives SECPI **3.024**, i.e. **3.0576 − 3.024 = 0.0336** below baseline; the high-bound sweep gives **4.380**, i.e. **4.380 − 3.0576 = 1.3224** above it. The baseline therefore sits **39× closer to the low bound (12.0 m) than to the high bound (34.0 m)**, which is what one would expect if the baseline crown diameter were near 12 m — **not** the 23.0 m midpoint §3.1.4 uses (#52). Either the response is extremely convex or the baseline does not use the midpoint convention. The manuscript does not say, and #52 already documents that the paper alternates between maxima and midpoints for this exact parameter without declaring which is in force.
- **Closes when:** `math-auditor` reports the baseline parameter vector used by `SensitivityAnalyzer` — in particular the baseline crown diameter per species — together with the experiment, k, arm, grid and seed that produced SECPI 3.0576, from a named run in `results/`. `editor` states all of it in §3.5.1. Compounds **#52** and **#64**.

> **⚠️ v5 UPDATE to #76 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §A1, §B and §D6. PARTIALLY ADVANCED, NOT CLOSED. Class unchanged: PENDING VERIFICATION.**
> The original finding text above is preserved unaltered.
>
> - **ADVANCED — the baseline parameter *vector* is now known.** Entry 8 §A1: the base point is hardcoded at `run_oat_analysis` lines 927–932 (`decay_lambda 1.9, cca_threshold 1.2, competition_k 5.0, shade_weight 0.7`) plus each species' current `SPECIES_DATA` values, evaluated at `n_trees = 5`. **Narra's baseline crown diameter is 23.0 m** — the Table 3 midpoint, not the maximum. That answers the *"which crown-diameter convention"* half of this flag and of **#52** for the sensitivity routine specifically.
> - **NOT CLOSED — 3.0576 remains unmatched.** Entry 8's executed baseline is **3.2593** (leak-repaired) on one grid + one seed. The manuscript's 3.0576 is not reproduced. No experiment, k, arm, grid or seed producing 3.0576 has been identified, and **no run in `results/` has been named.** Both halves of the "closes when" clause remain owed.
> - **The flag's own arithmetic is now partly explained and partly deepened.** #76 observed that the baseline sits 39× closer to the low bound than to the high bound and inferred the baseline crown diameter might be near 12 m. Entry 8 refutes that inference for the *code*: the baseline is 23.0 m and the code's Narra crown-diameter bounds are **18.4 → 27.6 m**, symmetric about it. The manuscript's 12 → 34 m sweep is absent from the code entirely. So the asymmetry #76 detected is not a baseline-convention artefact — it is a property of numbers whose source is unknown. **This escalates the question from "which convention?" to "where did these numbers come from at all?"** — see **#97**.
> - **⚠️ Magnitude caveat, binding.** 3.2593 is a **single-run diagnostic**: one grid, one morphology, one seed, `n_samples = 3`, **no D-02 ceiling applied**, not written to `results/`. Entry 8 states it must not be quoted as a manuscript value. It is recorded here as evidence that 3.0576 was **not** matched, not as a replacement for it.
> - **Compounds #97.** #76 asks where one number came from; #97 asks where the whole of §3.5 came from. They close together or not at all.
>
> *Basis: Project Log Entry 8 §A1, §B, §D6 (Phases A, F2, H).*

**#77 — §3.5.1 — "three independent ACO runs" contradicts the project's `n_runs = 5` restart count, and no dispersion is reported for any of the 40 sensitivity indices.** · ~~PENDING VERIFICATION~~ → **POTENTIAL ROADBLOCK** *(escalated v5 — see the update block beneath this flag)*

- **Where:** `06_results_discussion.md:610–612` — *"the resulting SECPI was **averaged over three independent ACO runs** per configuration to reduce stochastic noise."*
- **Objection:** (a) **A third restart count enters the manuscript here.** `CLAUDE.md` §3 fixes the optimizer at `n_runs = 5` restarts per k, and the D-03 Wilcoxon design on file (`05_methods_2.5_2.6_vv.md:20`, editorial note) is built on *"n = 30 — k = 1…6 × 5 existing restarts per k."* §3.5.1 says three. The manuscript states the production restart count **nowhere else** — grep across `02`–`07` returns only this sentence and §3.4.2's bare *"across independent runs"* — so the only restart count the paper ever publishes is one that disagrees with the implementation of record. Whether the sensitivity sweep genuinely used a reduced restart count, or the sentence is wrong, changes the noise floor under every SI. Compounds **#57** (the ACO configuration is already published two mutually exclusive ways) and **#58** (the ACS parameter set is absent from Methods).
  (b) **No dispersion is reported for any SI.** Forty indices are computed as differences of run-averaged stochastic outputs and are then rank-ordered to ten places, with no SD, no standard error, no confidence interval and no n stated per index. Averaging three runs reduces the standard error of each endpoint by only √3 ≈ 1.73. A ranking of quantities whose uncertainty is never estimated is not a ranking. This is what makes **#78** possible.
- **Closes when:** `math-auditor` reports the restart count `SensitivityAnalyzer` actually uses and whether it inherits `base_aco_config` (per `docs/STATE.md`, `SensitivityAnalyzer` previously carried a **hardcoded 10 ants / 15 iterations** that has since been repointed at `base_aco_config` — so the published §3.5 numbers may predate that fix and may not have been produced by the production optimizer at all). `code-stressor` supplies per-index SD from the restart set. `editor` reports n and dispersion with every SI or removes the ranking.

> **⚠️ v5 UPDATE to #77 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §E1–§E3.**
> The original finding text above is preserved unaltered. **Objection (a) is REFRAMED — it is not the manuscript error this flag assumed. Objection (b) is CONFIRMED BY EXECUTION. The flag is ESCALATED: PENDING VERIFICATION → POTENTIAL ROADBLOCK.** The "closes when" clause below **replaces** the one above.
>
> **(a) REFRAMED — the manuscript sentence is ACCURATE TO THE CODE. This is a downgrade of one half of the objection and the evidence for it is stated here in full, per register discipline.** `n_samples` and `n_runs` are **different quantities**, and this flag conflated them:
> - **`n_runs = 5`** — `SuboptimalScenariosGenerator.run_optimization_for_k`, `AuditedCode_1.py:2753`. Independent ACO **restarts per k**, from which the **best** is taken.
> - **`n_samples = 3`** — `SensitivityAnalyzer.run_oat_analysis`. Repeat evaluations **averaged** per swept configuration.
>
> Best-of-5-restarts and mean-of-3-repeats are not the same statistic and are not interchangeable. §3.5.1's *"averaged over three independent ACO runs per configuration"* is therefore a **faithful description of what the code does**, and the "third restart count" framing above is withdrawn. *(Evidence: Project Log Entry 8 §E3, executed.)*
>
> **(a′) WHAT SURVIVES, AND IT IS NOT SMALLER.** The inconsistency is real; it is a **design** inconsistency, not a transcription error. **The sensitivity analysis runs at lower replication than the headline optimization, and the manuscript never states this, never justifies it, and never states either count in Methods.** A reviewer who notices that the paper's robustness evidence is built on 3 repeats while its headline result is built on best-of-5 will ask why — and the manuscript has no answer on the page. Compounded by **#78**: at `n_samples = 3` the measured SI noise floor is ≈ 0.0098, which 38 of the 40 indices fail to clear. The replication count is not a detail here; it is the reason the analysis cannot resolve its own effects.
>
> **(a″) A SECOND INSTANCE OF THE DEFECT CLASS ENTRY 2 FIXED — while the Entry 2 fix itself is confirmed live.** Two findings that must be read together:
> - **The Entry 2 fix is present and working.** Entry 8 §E1 spied the `AntColonySystemACO` constructor during a live `SensitivityAnalyzer` evaluation: **all seven ACO parameters are read from `base_aco_config`** — `n_ants = 20, n_iterations = 40, n_trees = 5, alpha = 1.0, beta = 2.0, evaporation_rate = 0.5, q0 = 0.7`. The historical hardcoded **10 ants / 15 iterations is gone.** `docs/STATE.md`'s "Code health" claim is confirmed **by execution**, not by grep. **The parenthetical worry in the original "closes when" clause — that the published §3.5 numbers may not have come from the production optimizer — is not supported by this code.** It is superseded by a larger finding: per **#97**, the published numbers cannot have come from this code for an entirely different reason.
> - **But `n_samples` escaped that fix.** It appears **nowhere in `base_aco_config`**. It is a signature default and a hardcoded literal at the production call site, `AuditedCode_1.py:3527`: `sensitivity_df = sensitivity_analyzer.run_oat_analysis(n_samples=3)`. This is the **same defect class Entry 2 repaired — a fidelity parameter hardcoded inside `SensitivityAnalyzer` instead of inherited from the study configuration — in a parameter Entry 2 did not cover.** It should be repointed at the study configuration in the same pass as the **#96** fix.
>
> **(b) CONFIRMED BY EXECUTION, and it is worse than "not reported".** Entry 8 §E3: **no dispersion statistic is computed or stored anywhere in the sensitivity path.** The results row (`AuditedCode_1.py:1002–1009`) carries `parameter, category, secpi_low, secpi_high, absolute_effect, sensitivity_index` — **no SD, no SE, no n field.** `low_scores` / `high_scores` are collapsed by `np.mean` at lines 997–998 and **discarded**. The per-index SD is therefore **not recoverable from the current CSV** and cannot be back-computed from any stored artefact; `code-stressor` must **add the capability**, not merely run the analysis.
>
> **WHY THIS ESCALATES TO POTENTIAL ROADBLOCK.** Three conditions, all now confirmed rather than pending:
> 1. **D-11 requires a per-index `SD` column. The reference implementation cannot produce one.** That is a capability gap in the code, confirmed by execution, standing between a decided decision and its execution.
> 2. **#78 is already POTENTIAL ROADBLOCK and this is its enabling defect.** #78's remedy — report every SI with an interval, mark as *unresolved* every index whose interval spans the noise floor — is **impossible in the current implementation.** A flag whose remedy is blocked by an unbuilt capability is not "pending verification"; the verification is done and the answer is that the capability is absent.
> 3. **The remedy is substantive, not editorial.** §3.5.1's rank-ordered list either acquires dispersion (code change + re-run) or is deleted. Rewording cannot produce it.
>
> **REVISED "Closes when":** `code-stressor` extends `SensitivityAnalyzer` to record and emit per-index `n` and `SD` (D-11's required table columns), applies it in the same pass as the **#96** state-leak fix and the `n_samples` repointing, and re-runs; the **research lead** decides and Methods discloses the replication count the sensitivity analysis will use and **why it may legitimately differ from the optimizer's `n_runs = 5`**; `editor` reports `n` and dispersion beside every SI, or removes the ranking entirely per **#78**. **No part of this closes by rewording §3.5.1.**
>
> *Basis: Project Log Entry 8 §E1, §E2, §E3 (Phase C, plus direct source reading of `AuditedCode_1.py:997–1009`, `:2753`, `:3527`). All claims in this block are structural and deterministic. The only magnitude cited — the ≈ 0.0098 noise floor — is carried from **#78** with its single-run caveat attached.*

**#78 — §3.5.1 — sensitivity indices 2 through 40 sit at or below the noise level the manuscript itself declares elsewhere, yet are ranked, interpreted, and used to found the robustness claim.** · **POTENTIAL ROADBLOCK**

- **Where:** `06_results_discussion.md:640–655` — *"All remaining 39 parameters exhibit sensitivity indices below 0.005, indicating that **the framework is robust** to moderate uncertainty in these inputs. The second through tenth most sensitive parameters, in descending order, are Talisay.h1 (SI = 0.0045), Talisay crown diameter (0.0043), Akleng-parang.l0 (0.0037), Duhat crown diameter (0.0033), Banaba.l0 (0.0032), CCA threshold (0.0032), Narra.h1 (0.0030), Narra.l0 (0.0030), and Duhat.h0 (0.0028). These parameters produce **absolute SECPI effects ranging from 0.009 to 0.014, which are small relative to the baseline but not negligible**."*
- **Objection:** hand arithmetic on the manuscript's own printed values, no execution required. SI × baseline recovers the stated absolute effects — 0.0045 × 3.0576 = **0.0138** ≈ 0.014 ✓, 0.0028 × 3.0576 = **0.0086** ≈ 0.009 ✓ — so the conversion is sound and the effects really are 0.009–0.014 SECPI units. Now compare against the manuscript's own two statements of its noise scale:
  - §3.3.1 reports the ACO's best-versus-average gap as **0.05–0.07 SECPI units** — five to eight times larger than every effect in the top-ten list.
  - §3.4.2 dismisses a difference of **0.0014** as *"well within the stochastic variation inherent to the ACO metaheuristic across independent runs."*
  The manuscript therefore declares 0.0014 to be noise, reports run-to-run structure at 0.05–0.07, and then calls effects of 0.009–0.014 **"not negligible"** and ranks them to four decimal places. All three statements cannot hold. Two consequences follow and both are load-bearing: the entire rank ordering below position 1 may be an ordering of noise, and §3.5.3's *"the framework is robust to moderate uncertainty"* is not an inference from small effects — it is what an under-powered design returns when it cannot resolve any effect at all. **Absence of measured sensitivity is being reported as demonstrated insensitivity.** This is the same selective-standard pattern **#65** and **#68** document in §3.4, now appearing in §3.5 as the foundation of the robustness conclusion rather than as an isolated sentence.
- **Closes when:** `code-stressor` establishes a quantified noise floor for SECPI across restarts at the sensitivity analysis's own restart count (see #77), and reports each SI with an interval. Every index whose interval spans the noise floor is reported as *unresolved*, not ranked. `editor` deletes the rank-2-to-10 list and the *"not negligible"* characterization unless the indices survive that test, and restates the robustness claim as *"no effect resolvable above run-to-run variation"* — which is a weaker and different claim. Owner: `code-stressor` then `editor`.

> **⚠️ v5 UPDATE to #78 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §D6.**
> The original finding text above is preserved unaltered. **CONFIRMED BY EXECUTION AND MATERIALLY STRENGTHENED. Class unchanged: POTENTIAL ROADBLOCK** — because its remedy remains achievable inside D-11's regeneration, not because its evidence is weak.
>
> **The noise floor is now measured, not inferred.** This flag was originally argued by cross-referencing three of the manuscript's own statements about its noise scale. That argument stands, and it is now backed by direct measurement. Entry 8 Phase F1 ran **10 fresh baseline evaluations** at production configuration:
>
> ```
> values: [3.2238, 3.2725, 3.2815, 3.1944, 3.1595, 3.1948, 3.2144, 3.1777, 3.2064, 3.2298]
> mean = 3.2155   sd = 0.0386   range = 0.1220
> SD of a 3-sample mean = 0.0223
> implied SI noise floor  |diff of two 3-means| / baseline  ≈ 0.0098
> ```
>
> **The measured SI noise floor at `n_samples = 3` is ≈ 0.0098.** In the leak-repaired 40-parameter sweep, **only two of forty indices clear it**: `decay_lambda` (0.1697) and `Akleng-parang.crown_diameter_m` (0.0444). **The other 38 sit at or below the noise floor.**
>
> **What this converts.** #78 previously read: *"the entire rank ordering below position 1 **may be** an ordering of noise."* On measurement, for the executed sweep, it **is** — and the boundary is at position **2**, not position 1. §3.5.3's *"the framework is robust to moderate uncertainty"* is confirmed as this flag characterized it: not an inference from small effects, but what an under-powered design returns when it cannot resolve any effect at all. **Absence of measured sensitivity reported as demonstrated insensitivity.**
>
> **A second, independent instability worth recording.** `Narra.crown_diameter_m` ranked **31/40** in Entry 8's Phase E sweep and **28/40** in its Phase H sweep. The two runs differ **both** by the #96 leak repair **and** by ACO stochasticity, so the rank change is **not attributable to either alone** and must not be quoted as a noise measurement. It is recorded here only as a caution: **the rank ordering is not stable between two runs of the same sweep**, which is exactly what a floor of 0.0098 predicts for indices below it.
>
> **⚠️ Magnitude caveat, binding and load-bearing here.** The 0.0098 floor derives from **one grid, one morphology, one seed, n = 10 baseline evaluations, no D-02 ceiling applied.** Entry 8 states its order of magnitude is measured but that `code-stressor` still owns the formal, replicated noise-floor deliverable. **Do not publish 0.0098.** Use it to justify the design requirement — every SI reported with an interval — not as the interval.
>
> **The "closes when" clause above is unchanged and now has a hard dependency:** it cannot be executed until **#77**'s capability gap is closed, because the current implementation stores no dispersion at all and the required interval cannot be computed from its CSV.
>
> *Basis: Project Log Entry 8 §D6 (Phases F1, E, H).*

**#79 — §3.5.1 vs §3.5.3 — parameters are swept over two incomparable perturbation widths, and the sensitivity index is not normalized by perturbation size, so the reported ranking is not a valid cross-parameter comparison.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.5.1 (`:609–610`) — *"Each parameter was evaluated at its **low and high bounds**"*; and (`:626–628`) — *"Sweeping Narra's crown diameter from its manuscript low of **12.0 m** to its high of **34.0 m**."* Against §3.5.3 (`:700–703`) — *"The allometric constants… (l0, l1, h0, h1) were swept across a **15% uncertainty band**."*
- **Objection:** the two sentences describe two different perturbation conventions inside one analysis, and only one of them is disclosed as a band. Morphological parameters are swept across their **full Table 3 trait ranges**; allometric constants across **±15%**. Hand arithmetic on the manuscript's printed values, taking Table 3's Narra crown-diameter midpoint (23.0 m) as the reference: the sweep 12→34 m is a span of 22 m, i.e. **0.957 of baseline (±47.8%)**, against the allometric span of **0.30 of baseline (±15%)** — the dominant parameter received a perturbation **3.19× wider in relative terms** than the parameters it is being ranked against.
  The sensitivity index as defined — |SECPI_high − SECPI_low| / SECPI_baseline — normalizes by the **output** baseline and not by the **input** perturbation. It is therefore an effect size, not an elasticity, and effect sizes measured over unequal input spans are not comparable. Correcting crudely for span: Narra CD 0.4435 / 0.957 = **0.464**; Talisay.h1 0.0045 / 0.30 = **0.0150**; ratio **30.9×** against the raw ratio of 0.4435 / 0.0045 = **98.6×**, which §3.5.1 reports as *"nearly two orders of magnitude."*
  **Stated fairly: crown diameter's dominance survives directionally — this objection does not overturn the paper's central sensitivity finding.** What it overturns is the reported *magnitude* (inflated roughly threefold), the claim that this is a like-for-like ranking, and — through §3.5.3 — the inference that allometric uncertainty is unimportant *relative to* crown diameter, which is precisely the comparison the unequal spans invalidate. A sweep across a species' full morphological trait range is also not an uncertainty analysis in the same sense as a ±15% error band: it asks what happens if the tree is a different size, not what happens if the measurement is wrong. §3.5.3 and the Conclusion then treat it as the latter (see #86).
- **Closes when:** `math-auditor` reports the actual low/high bound used for **each** of the 40 parameters from `SensitivityAnalyzer`, and whether heights and the weighting ratio used trait ranges or a fixed band. `editor` either (a) tabulates every sweep bound alongside every SI so the reader can see the spans, or (b) reports an elasticity-normalized index for the cross-parameter ranking and keeps the raw SI only within a category. The phrase *"nearly two orders of magnitude"* must not survive unqualified.

> **⚠️ v5 CORRECTION to #79 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §B.**
> The original finding text above is preserved unaltered. **The FACTUAL PREMISE IS REFUTED. The CONCLUSION SURVIVES. The class is unchanged (POTENTIAL ROADBLOCK) but the load-bearing objection is REPLACED** — see below for why the class does not fall with the premise.
>
> **REFUTED — there is no perturbation-width asymmetry in the code.** The `math-auditor` half of the "closes when" clause is **discharged**: Entry 8 dumped `parameter_definitions` for all 40 swept parameters. **Every one of the 36 species parameters — morphology *and* allometry — is swept at a uniform ±20% of its base value, `rel_span = 0.4000` for all of them.**
>
> ```
> Narra.crown_diameter_m          base=23    low=18.4   high=27.6   rel_span=0.4000
> Talisay.crown_diameter_m        base=12    low=9.6    high=14.4   rel_span=0.4000
> Banaba.crown_diameter_m         base=11    low=8.8    high=13.2   rel_span=0.4000
> Kabiki.crown_diameter_m         base=11    low=8.8    high=13.2   rel_span=0.4000
> Duhat.crown_diameter_m          base=9.5   low=7.6    high=11.4   rel_span=0.4000
> Akleng-parang.crown_diameter_m  base=24    low=19.2   high=28.8   rel_span=0.4000
> Narra.l0                        base=0.25  low=0.2    high=0.3    rel_span=0.4000
> Talisay.h1                      base=0.71  low=0.568  high=0.852  rel_span=0.4000
>    … every one of the 36 species parameters: rel_span = 0.4000
> ```
>
> Therefore, withdrawn from this flag as statements about the executed design:
> 1. **WITHDRAWN — *"Morphological parameters are swept across their full Table 3 trait ranges; allometric constants across ±15%."*** Neither convention is in the code. Both are ±20%.
> 2. **WITHDRAWN — the 3.19× relative-span asymmetry**, and with it the derived correction arithmetic (Narra CD 0.4435 / 0.957 = 0.464; Talisay.h1 0.0045 / 0.30 = 0.0150; ratio 30.9× against a raw 98.6×). **All of that arithmetic is sound but is performed on spans that do not exist in the implementation.** Do not quote it.
> 3. **WITHDRAWN — *"the reported magnitude is inflated roughly threefold"* by span inequality.** There is no span inequality to inflate it. (The reported magnitude **is** wrong, but for the unrelated reason registered as **#97**.)
>
> **WHAT SURVIVES, AND IT IS THE FLAG'S REAL CONTENT.**
> - **The methodological objection stands and is untouched by execution.** The sensitivity index as defined — `|SECPI_high − SECPI_low| / SECPI_baseline` — normalizes by the **output** baseline and not by the **input** perturbation. **It is an effect size, not an elasticity.** Cross-parameter comparison of effect sizes is only valid over equal relative input spans. The code happens to satisfy that condition for the 36 species parameters — but **by accident of a uniform ±20% default, not by design, and the manuscript nowhere states the condition, the span, or why it matters.** A reviewer is entitled to the sweep bounds beside every index; the manuscript supplies none.
> - **The condition is NOT satisfied across all 40 parameters.** The 4 non-species parameters do not share the ±20% convention. Entry 8's executed cooling vectors give `decay_lambda` **0.5 → 3.0** about a base of **1.9** (a span of 2.5, ≈ 132% of base), `cca_threshold` **0.5 → 2.0** about 1.2, `competition_k` **1.0 → 10.0** about 5.0, `shade_weight` **0.5 → 0.9** about 0.7. **The executed rank-1 parameter, `decay_lambda`, is swept over a relative span several times wider than every species parameter it is ranked against.** The asymmetry this flag correctly suspected is real — it simply sits between the **Cooling_Model** and **species** blocks, not between morphology and allometry. **The objection is preserved, relocated, and now points at the parameter that actually tops the executed ranking.**
> - **A NEW defect surfaces from the same evidence:** §3.5.1's *"12.0 m to 34.0 m"* and §3.5.3's *"15% uncertainty band"* are **both absent from the reference implementation.** The manuscript states two sweep conventions and the code implements a third. That is registered in full as **#97**, not duplicated here.
>
> **WHY THE CLASS DOES NOT FALL.** The premise was one route to the objection; it was not the objection. What remains is confirmed rather than suspected: an effect-size index presented as a cross-parameter ranking, over spans the manuscript never discloses, at least one of which (`decay_lambda`) is materially wider than the rest. The remedy is unchanged and is still substantive — tabulate the bounds, or report an elasticity-normalized index. **The phrase *"nearly two orders of magnitude"* must still not survive unqualified.**
>
> **REVISED "Closes when":** the `math-auditor` half is **discharged** (bounds reported for all 40). `editor` tabulates every sweep bound beside every SI in the regenerated §3.5, **including the four non-species parameters whose spans differ**, or reports an elasticity-normalized index for the cross-parameter ranking and keeps the raw SI only within a category. The research lead should be told plainly that the ±20% default is undocumented and unjustified in the manuscript — see **#84** for the related false-provenance defect on the same constants.
>
> *Basis: Project Log Entry 8 §B (Phase A parameter dump), §A1 (executed cooling vectors). Structural claims — deterministic.*

**#80 — §3.5.1 — the cross-reference supporting the headline finding points to the wrong section, and the comparison it draws crosses the two incommensurable experiments #64 identifies.** · **POTENTIAL ROADBLOCK**

- **Where:** `06_results_discussion.md:629–631` — *"This finding is consistent with the combinatorial results reported in **Section 3.2**, which identified a sharp performance cliff between configurations containing large-crowned species and those without."* And `:635–639` — *"When set to its upper bound (34.0 m)… producing SECPI scores **comparable to the top-ranked combinatorial configurations**."*
- **Objection:** two problems, one mechanical and one substantive.
  **(a) The cross-reference is wrong.** §3.2 is *"Urban Grid Generation and Equity Zone Classification"* (`:210`) and contains no combinatorial results, no performance cliff, and in fact **no prose at all** — it is two headings and two figure captions (**#56**). The performance cliff is in **§3.4.3**, *"The Performance Cliff and the Role of…"* (`:364`). The single citation the manuscript offers in support of its dominant sensitivity finding points at an empty subsection. Mechanically trivial to fix, but it means the corroboration §3.5.1 claims has never actually been checked by anyone in the drafting chain.
  **(b) The comparison crosses two experiments that #64 establishes are not on a common scale.** §3.5's baseline is **3.0576** and its sweep endpoints are 3.024 and 4.380; §3.4's tree-count experiment lives at 2.99–3.08 and the palette-size combinatorial experiment at 3.023–4.393. §3.5.1 takes a value produced by perturbing **one species' crown diameter within the sensitivity experiment** and declares it *"comparable to the top-ranked combinatorial configurations"* — configurations that differ by **species palette**, not by crown diameter. The two 4.38-ish numbers arrive by different routes and mean different things; their proximity is presented as convergent evidence. Until D-07 closes and the two axes carry distinct symbols, this sentence reads as mutual corroboration between an experiment and itself.
- **Closes when:** `editor` repoints the cross-reference to §3.4.3 **and** deletes or requalifies the "comparable to the top-ranked combinatorial configurations" claim; `code-stressor` states which experiment the sensitivity sweep was run inside (see #76) so the comparability question can be settled rather than assumed. D-07 must close first. Compounds **#44**, **#56**, **#64**.

**#81 — §3.5 — Figures 33 and 34 are never cited in the text; document-wide, §3 carries 28 figure captions and not one valid in-text reference.** · PENDING VERIFICATION

- **Where:** `06_results_discussion.md:615` — *"Figure 33. Sensitivity Index Tornado Diagram"* — and `:657` — *"Figure 34. Parameter Category Sensitivity Summary."* Neither string "Figure 33" nor "Figure 34" occurs anywhere else in the section.
- **Objection:** both §3.5 figures are orphaned. The defect is not local: enumerating every `Figure` occurrence in `06_results_discussion.md` returns **Figures 7 through 34 — 28 captions — and exactly one in-text reference**, at `:549`, which is itself broken: *"profile for Narra (**Figure [Single Tree Radial Decay: Narra]**)"* — an unresolved placeholder naming no figure number. So no figure in the entire Results and Discussion is called out from the text. Journals in this field desk-check for this; unreferenced figures are queried or cut, and a reader cannot tell which claim each figure supports. Two specific consequences for §3.5: Figure 33 is the only presentation of the full 40-parameter result set, so the 30 parameters never named in prose exist **only** in an uncited figure and cannot be checked at all; and Figure 34 plots the four category means that **#82** shows to be impossible, so the figure is presumptively wrong and must be regenerated rather than merely cited. Separately, a tornado diagram in which one bar is 0.4435 and the other 39 are below 0.005 is at ~1% of the axis — the figure cannot legibly convey the secondary tier it is the sole source for.
- **Closes when:** `editor` performs a manuscript-wide figure-and-table audit — every figure cited at least once at the point of the claim it supports, the `:549` placeholder resolved to a numbered figure, and any figure that survives regeneration but supports no claim removed. **Named artefact:** a figure inventory listing, for each of Figures 7–34, the section and line of its in-text call-out. Interacts with `08_references_appendices.md:27` (the same check is already owed for Appendix A's Figures A1–A28). Figure 34 is blocked behind **#82**.

---

### §3.5.2 — Category-Level Sensitivity

**#82 — 🔴 All four reported category-level mean sensitivity indices exceed the maximum sensitivity index of their own member sets. The category-level analysis is arithmetically impossible as printed and cannot be repaired by rewording.** · **ROADBLOCK (SEVERE)** — *the project's first*

- **Where:** `06_results_discussion.md:658–665` — *"Aggregating sensitivity indices by category reveals a clear hierarchy. **Species Morphology dominates with a mean SI of 1.3068**, driven almost entirely by the Narra crown diameter outlier. Removing that single parameter would reduce the category mean to approximately 0.002, placing it on par with the other categories. **Species Allometry parameters rank second with a mean SI of 0.1857, followed by Species Allometry (0.0727) and Weighting (0.0236)**."* Supporting values, all printed in §3.5 itself: SI definition and baseline (`:616–622`, `:612`); Narra CD SI **0.4435** and *"All remaining 39 parameters exhibit sensitivity indices below 0.005"* (`:623–624`, `:640–641`); ranks 2–10 (`:642–647`); CCA threshold **0.0032**, competition steepness **0.0021** (`:667–668`), decay lambda **0.0015** (`:674–675`), shade_weight **0.0017** (`:678–679`).
- **Objection:** four independent impossibilities, one duplicate label, and one internal self-contradiction. All of it is derivable from values the manuscript prints, by hand, with no execution and no external data.

  **Category membership is fixed by §3.5.1's own definition** (`:604–608`): *"species morphological traits (crown diameter, height), species allometric constants (l0, l1, h0, h1), cooling model parameters (decay lambda, CCA threshold, competition steepness), and the shade-evapotranspiration weighting ratio."* With six species that gives Morphology **2 × 6 = 12**, Allometry **4 × 6 = 24**, Cooling Model **3**, Weighting **1**. **12 + 24 + 3 + 1 = 40**, matching §3.5.1's own *"swept 40 parameters."* The membership counts are therefore not an assumption — they are forced by the manuscript.

  **The argument is `mean ≤ max`, not a [0,1] bound.** SI = |SECPI_high − SECPI_low| / SECPI_baseline is a ratio of a difference to a baseline and is **not** bounded above by 1; it would legitimately exceed 1 if a parameter's effect exceeded the baseline SECPI. Any objection resting on a normalized-index bound is refutable and must not be used. `mean ≤ max` needs no assumption at all.

  | Category | n | Largest SI among its members (manuscript-printed) | Maximum possible mean | **Reported mean** | Overstatement |
  |---|---|---|---|---|---|
  | Species Morphology | 12 | 0.4435 (Narra CD) | (0.4435 + 0.0043 + 0.0033 + 0.0027 + 8 × 0.005) / 12 = 0.4938 / 12 = **0.0412** | **1.3068** | ≥ **31.7×** the ceiling; **2.95×** its own largest member |
  | Species Allometry | 24 | 0.0037 (Akleng-parang.l0) | all members < 0.005 ⇒ mean < **0.005** | **0.1857** | ≥ **37×** the ceiling; **50.2×** its largest named member |
  | Cooling Model *(the duplicate-labelled entry)* | 3 | 0.0032 (CCA threshold) | (0.0032 + 0.0021 + 0.0015) / 3 = 0.0068 / 3 = **0.002267** — an exact value, not a bound | **0.0727** | **32.1×**; **22.7×** its largest member |
  | Weighting | **1** | 0.0017 (shade_weight) | a one-element mean **equals** its element: **0.0017** — exact | **0.0236** | **13.9×** |

  **The Weighting row alone is decisive and needs no bounding step.** §3.5.1 defines the category as *"the shade-evapotranspiration weighting ratio"* — singular — and §3.5.2 itself prints that parameter's SI as **0.0017** thirteen lines below the sentence that gives the category a mean of **0.0236**. The mean of a one-element set is that element. **No definition of "mean" reconciles 0.0236 with 0.0017.**

  **(b) The label set is wrong.** *"Species Allometry"* is named **twice**, at 0.1857 and 0.0727. **Cooling Model is never named in the aggregation at all**, yet the very next paragraph opens *"The relatively low sensitivity of the **Cooling Model** category is noteworthy"* and discusses its three members. One of the four hierarchy entries is mislabelled and the reader must reverse-engineer which. This is distinct from **#51** (which covers only the `3.4.2` / `3.4.3` heading-number duplication) and is not fixed by renumbering headings.

  **(c) The sentence contradicts itself.** It states that removing Narra CD *"would reduce the category mean to approximately 0.002."* If the 11 remaining Morphology members average 0.002 — entirely consistent with §3.5.1's *"all remaining 39 below 0.005"* — then the full 12-member mean is (0.4435 + 11 × 0.002) / 12 = 0.4655 / 12 = **0.0388**. The sentence's second half implies a starting mean of ≈0.039; its first half asserts **1.3068**. The two halves disagree by a factor of **33.7**, and the second half is the one consistent with §3.5.1.

  **(d) It is not a units error, a scaling error, or a mislabelled sum — the three benign explanations are all excluded.** The overstatement factors are **2.95 / 50.2 / 22.7 / 13.9** against largest members and **31.7 / ≥37 / 32.1 / 13.9** against the true ceilings: **no common factor**, so no single mis-scaling produces them. And the "labelled a mean but is really a sum" reading fails outright: Weighting's sum **is** 0.0017 (n = 1) ≠ 0.0236; Cooling Model's sum is **0.0068** ≠ 0.0727; Morphology's sum is at most **0.4938** ≠ 1.3068. *(⚠️ This refutes the diagnosis currently carried in `docs/STATUS.md:48` and `docs/HANDOVER.md:171–172`, both of which state the values "behave like a sum" and additionally argue from a [0,1] bound. **Both arguments are wrong and the proposed "relabel sum-vs-mean" remedy would not fix anything.** Those files are derived artefacts owned elsewhere; v4 did not edit them — see Project Log Entry 6, "Still open".)*

  **What is *not* wrong, and why it matters.** The **parameter-level** results in §3.5.1 are internally consistent and reproduce cleanly: 4.380 − 3.024 = **1.356** ✓ as stated; 1.356 / 3.0576 = **0.44348** ≈ 0.4435 ✓; 0.0045 × 3.0576 = **0.0138** ≈ the stated 0.014 ✓; 0.0028 × 3.0576 = **0.0086** ≈ the stated 0.009 ✓; and shade_weight 0.0017 × 3.0576 = **0.0052** ≈ §3.5.2's own *"a SECPI difference of only 0.005"* ✓. **The defect is localized to the aggregation step and to Figure 34.** That is a diagnosis, not a mitigation — it tells the team where to look, and it means §3.5.1 may be salvageable while §3.5.2 is not.

- **Why SEVERE rather than POTENTIAL ROADBLOCK.** The register reserves SEVERE for a finding *confirmed unresolvable as written*, where the section must be reworked rather than reworded. All three conditions hold and none is contingent:
  1. **Confirmed, not pending.** The proof is closed over values the manuscript itself prints. Nothing needs to be executed, sourced, or decided for the impossibility to hold. The Weighting row is a single-line refutation.
  2. **Unresolvable as written.** The correct values are **not recoverable from the manuscript** — only upper bounds are derivable. There is no common factor to undo, no relabelling that repairs the arithmetic, and one of the four category labels is itself wrong. An editor cannot fix this sentence; the aggregation must be recomputed from the raw sensitivity output, and per `CLAUDE.md` §4 that output is itself obsolete under Option B and must be regenerated first.
  3. **The section must be reworked.** §3.5.2's entire hierarchy claim, Figure 34, and the Conclusion's *"Sensitivity Index = 0.46"* (**#89**) all fall with it.
  A reviewer who performs the one-element-mean check — which takes seconds and is the first check a numerate referee makes on a category table — finds a printed result that cannot be true. **This is a desk-reject-class defect, and it must not reach a preprint with a DOI.**
- **Closes when:** the sensitivity analysis is **regenerated** under Option B (blocked on D-02, and on #75's method question and #77's restart question), and `code-stressor` emits a machine-written per-parameter table — parameter, category, low bound, high bound, SECPI_low, SECPI_high, SI, n, SD — plus category aggregates computed from that table, from a single named run in `results/`. `math-auditor` confirms the aggregation function in `SensitivityAnalyzer` and reports what it actually computes, since a defect that produces four uncorrelated overstatements is more likely a code defect than four transcription slips. `editor` writes §3.5.2 and Figure 34 from that table only. **Until then §3.5.2 must not be rewritten — it must be regenerated, and no number from it may be quoted anywhere in the manuscript, the Abstract, or the Conclusion.**

> **⚠️ v5 UPDATE to #82 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §C.**
> The original finding text above is preserved unaltered. **The flag REMAINS ROADBLOCK (SEVERE). Its `math-auditor` diagnostic is DISCHARGED and its working hypothesis is OVERTURNED. Nobody should re-run that diagnostic; the answer is below.** The "closes when" clause is revised at the end of this block.
>
> **⛔ DO NOT RE-RUN THE AGGREGATION DIAGNOSTIC. THE AGGREGATION IS INNOCENT.**
>
> The original clause asked `math-auditor` to report what the aggregation function computes, on the reasoning that *"a defect that produces four uncorrelated overstatements is more likely a code defect than four transcription slips."* **That reasoning was wrong, and it has been tested to destruction.** Entry 8 §C, three independent probes:
>
> 1. **Known-truth vector (Phase D1).** `SensitivityAnalyzer.save_results()` (`:1033`) and `AutomatedInterpreter.interpret_sensitivity_analysis()` (`:538`) both compute a **true arithmetic mean**. The one plausible code-level mechanism for a mean/max/sum/count label swap was tested specifically — that pandas 3.0.0 might return `.agg([...])` columns in an order different from the hardcoded rename at `:1036`. **It does not.** The order is `mean, max, sum, count`, exactly as the rename assumes.
> 2. **2,000 randomized trials (Phase D2)** over category sizes 1–29 and magnitude scales 0.001 / 1 / 100, driving the identical `groupby().agg()` + rename expression: `cases where reported mean > reported max: 0`. **The reported mean is structurally incapable of exceeding the reported max.**
> 3. **A real 243-evaluation sweep at production configuration (Phase E).** `mean ≤ max` holds in **all four** categories.
>
> **THE DECISIVE FINDING — the published category means are not reproducible from this code at all.** Executed against published, side by side:
>
> | Category | n | **Published mean** | Executed mean | Executed max | Executed sum |
> |---|---|---|---|---|---|
> | Species_Morphology | 12 | **1.3068** | 0.006593 | 0.016320 | 0.079119 |
> | Species_Allometry | 24 | **0.1857** | 0.012433 | 0.040818 | 0.298385 |
> | Cooling_Model | 3 | **0.0727** | 0.059809 | 0.169702 | 0.179427 |
> | Weighting | **1** | **0.0236** | 0.001385 | 0.001385 | 0.001385 |
>
> **The Weighting row closes the question by execution as well as by arithmetic.** With n = 1, mean = max = sum = **0.001385**, and **none of the three equals the published 0.0236.** The "it is really a sum" reading — already excluded by hand in the original flag — is now excluded by execution too.
>
> **Therefore: the four published category means did not come from `AuditedCode_1.py`'s aggregation step.** They came from somewhere this repository does not contain — an earlier code version, a spreadsheet, or manual entry. **This is the same forensic question D-06 asked about §3.1, now asked about §3.5.** It is unassigned and, per Entry 8, warrants routing to `docs/DECISIONS.md` by the orchestrator. **Until it is answered, no §3.5 number has a known provenance.**
>
> **WHAT THIS CHANGES ABOUT D-11 — read before regenerating.** The note carried into D-11 — *"if the defect is in code, regeneration alone reproduces it"* — is answered: **it is not in this code, so regeneration will not reproduce the defect.** A clean regeneration will emit `mean ≤ max` rows. **But that is far weaker reassurance than it sounds, and it must not be read as vindication.** Regeneration will **neither reproduce nor vindicate §3.5**: the per-parameter table feeding the aggregation is itself invalid, for two separate reasons registered as **#96** (the state leak contaminates every row from the first morphology evaluation onward) and **#97** (the code's sweep bounds are not the manuscript's, and the qualitative findings invert). **Correct arithmetic over an invalid input table is still an invalid table.**
>
> **ONE SECONDARY OBSERVATION, recorded so it is not rediscovered as a lead.** `plot_sensitivity_results()` (`:1066`) computes `df.groupby('category')['sensitivity_index'].sum()`, labels the axis *"Total Sensitivity Index"* and titles the panel *"Sensitivity by Parameter Category."* **Figure 34 therefore plots SUMS while the CSV reports MEANS.** That is a genuine mean/sum ambiguity between two artefacts and a plausible seed for a transcription error — **but it does not explain the published numbers**, as the table above shows. Fix it in regeneration for consistency; do not pursue it as the cause.
>
> **WHY THE CLASS DOES NOT MOVE — SEVERE is confirmed, not weakened.** All three of the original SEVERE conditions hold **more strongly** than when they were written:
> 1. **Confirmed, not pending** — the impossibility was already closed over the manuscript's own printed values. Execution has now added that the correct values are not merely unrecoverable from the manuscript, they are **unrecoverable from the codebase**.
> 2. **Unresolvable as written** — strengthened. Not only can no editor repair the sentence; **no run of the reference implementation reproduces it**, so there is no artefact against which to check a repair.
> 3. **The section must be reworked** — strengthened, and widened. #82 previously noted that *"§3.5.1 may be salvageable while §3.5.2 is not."* **That note is SUPERSEDED by #97: §3.5.1 is not salvageable either.** The whole of §3.5 regenerates.
>
> **REVISED "Closes when":** the `math-auditor` half is **DISCHARGED — do not re-issue it.** What remains: (i) the **#96** state leak is fixed and authorized, (ii) **#75**'s three-way design question is settled by the research lead, (iii) **#77**'s dispersion capability is added, (iv) `code-stressor` regenerates the full sweep and aggregation under Option B into a single named run in `results/`, emitting the D-11 per-parameter table, and (v) the provenance of the published §3.5 numbers is either established or formally recorded as unrecoverable. `editor` writes §3.5 and Figure 34 from the emitted table only. **The standing prohibition is unchanged and now extends to all of §3.5, not just §3.5.2: it must not be rewritten, it must be regenerated, and no number from it may be quoted anywhere in the manuscript, the Abstract, or the Conclusion.**
>
> *Basis: Project Log Entry 8 §C1–§C4 (Phases D1, D2, E). The aggregation semantics and the 0/2000 violation count are structural and deterministic. The executed category means in the table above are **single-run diagnostics** — one grid, one seed, `n_samples = 3`, no D-02 ceiling — and are cited **solely to demonstrate non-reproduction of the published values**, never as replacements for them.*

**#83 — §3.5.2 — the stated causal explanation for the weighting ratio's insensitivity is refuted by the manuscript's own Table 3, which shows the exact trade-off the paragraph claims the species pool lacks.** · **POTENTIAL ROADBLOCK**

- **Where:** `06_results_discussion.md:683–694` — *"This insensitivity arises because **the two dominant species (Narra and Akleng-parang) rank highest on both CPA and LAI dimensions**, so altering the relative weight between these components does not change the optimizer's species preference or spatial strategy. The weighting ratio would become more consequential in scenarios where **the species pool contained trees with high LAI but small crowns, or vice versa**, creating a genuine trade-off between shading and evapotranspiration that **the current TFT set does not strongly exhibit**."*
- **Objection:** the claim is false against Table 3 (`:85–104`), printed in the same section. Table 3 LAI ranges, ranked by midpoint: **Kabiki 4.5–6.0 (5.25) > Talisay 4.0–5.5 (4.75) > Narra 4.0–5.0 (4.50) > Banaba 3.5–4.5 (4.00) > Duhat 2.5–4.0 (3.25) > Akleng-parang 2.5–3.5 (3.00)**. The ranking is identical under range maxima. So:
  - **Akleng-parang has the lowest LAI of all six species**, not the highest. Narra is **third**. The premise *"rank highest on both CPA and LAI dimensions"* is true only for CPA (Narra CPA 113–908, Akleng-parang 254–707 — the two largest under both midpoint and maximum conventions) and is **false for LAI under every convention**.
  - The final sentence is refuted by the same table. *"Trees with high LAI but small crowns, or vice versa"* describes **Kabiki** (highest LAI 4.5–6.0, crown 10–12 m, CPA 78.5–113 — near the bottom) and **Akleng-parang** (second-largest CPA, **lowest** LAI). The current TFT set exhibits the CPA–LAI trade-off about as starkly as a six-species pool can. The paragraph asserts the opposite of what its own Table 3 shows.
  This matters beyond a wrong sentence. §3.5.2's shade_weight result is one of the manuscript's two claimed robustness findings, and the offered mechanism for it is now unavailable. If the pool *does* contain a genuine CPA–LAI trade-off and the weighting ratio still barely moves SECPI, the correct inference is not "the trade-off is absent" but something the paper has not considered — most likely that the 0.30 LAI term is doing very little work in the objective at all, which would compound **#54** (shading dominance is entailed by the specification, not observed) and bear directly on **#85**. Note also that Table 3 is arithmetically sound and can be relied on here: CPA reproduces from CD for all six species (π/4 · 12² = 113.1 ✓, π/4 · 34² = 907.9 ✓, π/4 · 18² = 254.5 ✓, π/4 · 30² = 706.9 ✓).
- **Closes when:** `math-auditor` reports the marginal contribution of the normalized-LAI term to the objective across the sweep 0.5 → 0.9 of `shade_weight`, per species, so the real mechanism can be named. `editor` deletes the "rank highest on both dimensions" premise and the "does not strongly exhibit" conclusion, and rewrites the explanation from that output. Compounds **#53** (whose own Banaba-LAI claim was withdrawn in the v4 correction above — this is a distinct and opposite finding, about Akleng-parang) and **#54**.

---

### §3.5.3 — Implications for Model Robustness and Data Collection

**#84 — §3.5.3 states the allometric constants were "sourced from literature." They were not, and the project has already decided so.** · **POTENTIAL ROADBLOCK** *(refines #30 into Results scope; supersedes the forward reference "#79")*

- **Where:** `06_results_discussion.md:700–703` — *"The **allometric constants sourced from literature** (l0, l1, h0, h1) were swept across a 15% uncertainty band, and none produced SECPI effects exceeding 0.014."*
- **Objection:** this is a provenance claim, stated as fact in Results, that the project record already contradicts. Per `docs/DECISIONS.md` **D-09 — DECIDED**: *"Hardcoded LAI values remain canonical for all results. The allometric chain stays sensitivity-only, **disclosed as author-estimated**,"* and *"**No species-specific source exists**; §2.2's DENR-ERDB / UPLB-CFNR / Abino et al. (2014) citation covers **morphology, not LAI** — **do not present it as sourcing LAI**."* Project Log Entry 3 established, after two dedicated search rounds, that no direct or genus-level precedent exists for an `LAI = l0 · DBH^l1` power law, that the constants are **22–77× off an empirical refit** against 211 NPDC field records, and that the concept is mismatched (urban-forestry standards predict leaf *area*, extensive, from DBH; LAI is intensive). §3.5.3 is doing exactly what D-09 prohibits.
  Three aggravating features. (i) It is stated in **Results**, where a reader takes provenance as established rather than argued — #30 was scoped to Methods, so a Methods-only fix leaves this standing. (ii) The sentence uses the false provenance to *license* the robustness inference: literature-sourced constants with a 15% error band is a coherent uncertainty story, author estimates with no source and a 22–77× discrepancy is not, and the 15% band is then unmotivated (see #79). (iii) A `deriver` has already spent two search rounds establishing the absence; publishing "sourced from literature" would put a claim into the permanent record that the project's own audit trail refutes.
- **Closes when:** `editor` replaces the phrase with an explicit statement that l0, l1, h0, h1 are **author estimates**, per D-09, with the sensitivity-only status of the allometric chain stated in the same sentence; and the corresponding Methods disclosure lands at the same time so the two sections agree. `deriver` confirms no source has appeared since Entry 3 before the phrase is finalized. **Blocked jointly with #30**; both must move together or the manuscript will disclose in one section and assert the opposite in another.

**#85 — §3.5.3 — near-zero allometric sensitivity is the expected signature of parameters that D-09 places off the canonical path; it is reported as demonstrated robustness, and #30's documented defect is read as a design feature.** · **POTENTIAL ROADBLOCK**

- **Where:** `06_results_discussion.md:697–707` — *"the framework's outputs are **robust to the typical uncertainties associated with allometric estimation in tropical forestry**… even if the species-specific constants carry estimation errors of this magnitude, the optimization recommendations, particularly species ranking and spatial placement logic, **remain stable**."* And `:720–725` — *"Height measurements, by contrast, showed minimal sensitivity across all species (the highest being Duhat height at SI = 0.0027), **confirming that the allometric pathway from height to DBH to LAI introduces sufficient buffering** to dampen the effect of height uncertainty on final cooling estimates."*
- **Objection:** §3.5.3 offers one interpretation of near-zero allometric sensitivity — robustness — without considering the alternative the project has already documented, which fits the same data at least as well and is far more damaging.
  Per **D-09 (DECIDED)**, *"Hardcoded LAI values remain canonical for all results. **The allometric chain stays sensitivity-only.**"* If the canonical objective consumes hardcoded LAI, then l0, l1, h0 and h1 do not reach it, and **an SI indistinguishable from zero is exactly what a disconnected parameter produces**. The 24 allometric indices — every one below 0.005, i.e. absolute SECPI effects at or under 0.015 against a run-to-run gap of 0.05–0.07 (**#78**) — are consistent with *no effect at all*. The manuscript cannot distinguish "this parameter barely matters" from "this parameter is not on the active code path," and it reports the first without testing for the second.
  The height sentence makes the same move on a defect that is already confirmed. Flag **#30**, verified independently twice (Entries 1 and 2), records that using the manuscript's own Table 4 constants **all six species yield h < h₀**, producing DBH of **0.17–0.66 m** and computed LAI **50–420× smaller** than the LAI the model uses, with the inversion running opposite to typical FORMIND allometrics. §3.5.3 observes that perturbing inputs to this pathway changes nothing and names the cause *"sufficient buffering."* A pathway whose output is 50–420× wrong and unresponsive to its own inputs is not buffered; that is the signature of a broken or bypassed transform. **The manuscript reports a confirmed defect as a robustness property.** If that reading survives to publication it is worse than the defect, because it converts a bug into a stated finding.
  Whichever way this resolves, §3.5.3's central conclusion does not stand as written: if the constants are off-path, the robustness claim is vacuous and must be withdrawn; if they are on-path, #30's implausible DBH values are live inside the sensitivity results and the SIs are computed from a broken transform.
- **Closes when:** `math-auditor` reports, from `AuditedCode_1.py`, (i) whether l0, l1, h0, h1 influence the SECPI objective on the canonical path or only within `SensitivityAnalyzer`, (ii) whether `SensitivityAnalyzer` evaluates the same objective the ACO optimizes, and (iii) the computed vs. hardcoded LAI actually used at each call site — with values printed, not inferred. `editor` then either withdraws the robustness claim as vacuous or reports it alongside #30's disclosure. **Named artefact:** a call-path trace for the four allometric constants. Compounds **#30**, **#31**, **#78**; depends on **D-09**.

> **⚠️ v5 UPDATE to #85 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8 §C4 and §D5. ADVANCED BY A SECOND INDEPENDENT ROUTE. NOT CLOSED. Class unchanged: POTENTIAL ROADBLOCK.**
> The original finding text above is preserved unaltered.
>
> **THE ADVANCE — the allometric sensitivity indices are corrupted, and this no longer waits on #85's own call-path question.** This flag framed a binary: either the allometric constants are **off-path** (robustness claim vacuous) or **on-path** (SIs computed through #30's broken transform). Entry 8 supplies a **third, independently sufficient** reason the allometric SIs cannot be read as sensitivity, which holds under **either** branch:
>
> - Entry 8 §D5 re-ran the identical sweep with `TreeSpecies.SPECIES_DATA` snapshotted and restored around every evaluation — repaired **in the harness only**, `AuditedCode_1.py` untouched. `Cooling_Model` and `Weighting` came out **bit-identical** across the leaked and repaired runs, exactly as predicted, because they are evaluated before any species mutation and consume the same RNG stream. **That bit-identity is the internal control**: it confirms the harness is sound and that the divergence in the other two categories is caused by the state leak and nothing else.
> - Measured against that control: **the leak inflates apparent allometric sensitivity by 1.84× and deflates morphological sensitivity by 0.63×.** The allometry arm was substantially measuring **accumulated species drift**, not parameter sensitivity.
>
> **Why this matters to #85 specifically.** The 24 near-zero allometric indices are the observation this flag interprets. Entry 8 shows those indices are **not a clean measurement of anything** — they are inflated by a defect (**#96**) that is orthogonal to the on-path/off-path question. So the flag's central diagnosis — *the manuscript cannot distinguish "this parameter barely matters" from "this parameter is not on the active code path"* — now has a **third** indistinguishable candidate: *"this index is contaminated by state that leaked out of a previous evaluation."* The interpretive gap the flag identifies is wider, not narrower.
>
> **WHAT IS NOT ADVANCED, and why this does not close.**
> - **The call-path question is still open.** Entry 8 §C4 established only that the allometry branch *inside `SensitivityAnalyzer`* genuinely routes through `get_computed_lai()` with a real `l0/l1/h0/h1` override — i.e. **Entry 2's fabrication fix is present and live**, and the `np.random.uniform(0.98, 1.02)` failure mode named in `CLAUDE.md` §2 rule 1 does **not** recur in the sensitivity path. Entry 8 states plainly that this branch *"is broken in a different and equally invalidating way"* (**#96**). **None of #85's three lettered deliverables is discharged:** whether l0/l1/h0/h1 reach the **canonical** SECPI objective, whether `SensitivityAnalyzer` evaluates the **same** objective the ACO optimizes, and the computed-vs-hardcoded LAI **at each call site**, all remain unreported. Entry 8 lists #85's call-path trace among the items it still owes.
> - **#30 is untouched** and still blocks the physical-plausibility half.
>
> **⚠️ Magnitude caveat, binding.** The 1.84× and 0.63× factors are **single-run** — one grid, one morphology, one seed, `n_samples = 3`, no D-02 ceiling. They are strong evidence of **direction and rough scale** because of the `Cooling_Model`/`Weighting` bit-identity control, but they are **not publishable values** and must not be quoted as such.
>
> **"Closes when" is unchanged, with one addition:** the call-path trace must be produced **after** the **#96** fix lands, not before — a trace run against the leaking implementation would attribute to the call path effects that belong to accumulated drift.
>
> *Basis: Project Log Entry 8 §C4, §D5 (Phases E, G, H).*

**#86 — §3.5.3 — a trait-range sweep is recast as measurement error, and a real-world field-measurement prescription is issued from it inside a synthetic, non-georeferenced study.** · **POTENTIAL ROADBLOCK** *(third instance of #10/#11, first inside Results)*

- **Where:** `06_results_discussion.md:708–719` — *"the outsized influence of crown diameter identifies it as **the single most critical field measurement for future empirical calibration**. The manuscript's reported range for Narra crown diameter (12 to 34 m) spans nearly a three-fold difference, reflecting the species' **high morphological plasticity across growth stages and site conditions**. Narrowing this range through **site-specific crown surveys** would disproportionately reduce the uncertainty envelope around SECPI predictions. **For planning applications, this suggests that investing in crown diameter measurements for the dominant candidate species yields a far greater return in model precision than refining any other input parameter.**"*
- **Objection:** three defects stacked on one another.
  **(a) The quantity swept is not measurement error.** The sentence concedes it itself: 12–34 m *"reflect[s] the species' high morphological plasticity across growth stages and site conditions"* — that is genuine biological variation in what tree you plant, not uncertainty in measuring a given tree. The analysis asks *what if the Narra is small rather than large*, and §3.5.3 answers *therefore measure Narra crowns more precisely*. Those are different questions and the second does not follow from the first. A site survey cannot narrow a range that is real variation across growth stages; only specifying a planting age or size class can.
  **(b) The comparative claim it rests on is not valid as measured.** *"Greater return… than refining any other input parameter"* is a direct cross-parameter comparison of sensitivity indices measured over unequal perturbation spans (**#79**, 3.19× wider for crown diameter), against a secondary tier that may be entirely noise (**#78**), with an allometric arm that may be off-path (**#85**). If #79 or #85 resolves against the manuscript, the recommendation is not merely overstated — it is void, and a reader who acted on it would have misallocated real survey budget.
  **(c) It is a real-world prescription inside a study with no site.** `CLAUDE.md` §2 rule 6: the study is synthetic and non-georeferenced — no field site, no remote-sensing validation, no real raster. *"Site-specific crown surveys"* and *"planning applications"* address practitioners about measurements to take in a real city. **#10 / #11** were raised against the Title and Abstract, and **#91 / #92** cover the Conclusion; this is the first instance located inside **Results**, which is where such a claim is least defensible, and it means the objection is systemic across four sections rather than confined to framing text.
- **Closes when:** #79 and #85 resolve, establishing whether crown diameter's dominance survives an equal-span comparison and whether the allometric arm is live. Only then may a prioritization statement be made, and it must be scoped explicitly to model inputs within the synthetic framework (*"SECPI outputs in this framework are most responsive to assumed crown diameter"*), with any practitioner-facing recommendation moved to Recommendations as future work and marked as untested against any real site. Owner: `editor` after `math-auditor` and `code-stressor`.

---

### Conclusion

**#87 — "Successfully developed and validated" — none of the three validation stages Methods §2.5.2 specifies has a reported result, and §2.5.2's own pass criterion has no baseline anywhere in the manuscript.** · **POTENTIAL ROADBLOCK** *(extends #8; supersedes the forward reference "#90")*

- **Where:** `07_conclusion.md:55` — *"This study **successfully developed and validated** the Equitable Integer Lattice Optimization Paradigm."* And `:66–69` — *"achieved a maximum localized cooling reduction of 0.80 °C and a mean reduction of 0.11 °C across the grid, **confirming the model's ability to deliver targeted thermal relief**."*
- **Objection:** "validated" is unsupported in the ordinary external sense and also in the manuscript's own internal sense, and the second failure is the one that cannot be argued away.
  **(a) No external validation exists, and the manuscript says so.** §2.6 (`05_methods_2.5_2.6_vv.md:133–136`) states *"The absence of empirical field validation means that model results rely entirely on literature-derived and database parameters."* There is no field site, no remote-sensing comparison, no observed land-surface-temperature data. Verification against an internal specification is not validation against reality, and a geoscience reviewer draws that line immediately. This is **#8**, now asserted in the strongest possible form in the Conclusion's opening sentence.
  **(b) The manuscript's own internal validation protocol is never executed or reported.** Methods §2.5 specifies four things; §3 reports one and a half:
  | §2.5 specifies | Reported in §3? |
  |---|---|
  | §2.5.1 — ACO benchmarked against a **greedy algorithm on a submodular proxy**; *"the ACO must match or closely approximate this benchmark"* (`05:75–81`) | **Nowhere.** No greedy comparator appears anywhere in Results. |
  | §2.5.2 — **Morphological robustness**: *"considered validated if the ACO-SECPI logic consistently produces intelligible configurations that **outperform random placements** across all morphologies"* (`05:85–92`) | **Nowhere** — see **#88**. And **no random-placement baseline is reported anywhere in §3**, so the stated pass criterion has never been evaluated. |
  | §2.5.2 — **Functional diversity** validation (`05:93–100`) | Partially, in §3.4.1–§3.4.3 — but those results are the subject of **#64** (arithmetically incompatible per-k means), **#65** and **#46** (the conclusion drawn is the opposite of what the data show). |
  | §2.5.2 — **Cross-scenario**: *"A successful validation is marked by a **statistically significant** redirection of resources"* (`05:107–108`) | §3.4.4 — but **#69** shows the comparison is circular by construction and **#70** shows "significantly" carries no test, n or p. D-03 exists to specify the metric and is still open. |
  So the Conclusion declares a validation successful against a four-part protocol of which one part is unreported, one part's criterion has no baseline, one part reports a contested result, and one part is circular. **"Validated" is not an overstatement here; it is a claim with no satisfied criterion behind it.**
  **(c) "Confirming"** attaches empirical confirmation to °C figures that **#62** shows are a dimensionless index relabelled with a physical unit, with no calibration anywhere in the manuscript.
- **Closes when:** `editor` replaces *"developed and validated"* with *"developed and internally verified,"* names external validation explicitly as future work, and removes *"confirming."* Separately — and this is the substantive half — either `code-stressor` executes the §2.5 protocol and §3 reports all four stages against their stated criteria (including a **random-placement baseline**, which is cheap and is the paper's own chosen benchmark), or **§2.5 is rewritten to describe what was actually done.** A Methods section specifying a validation protocol that Results does not execute is a reproducibility defect in its own right. Owner: `code-stressor` then `editor`.

**#88 — The Conclusion reports a morphological-robustness result that appears nowhere in Results, contradicts Methods on the number of morphologies, names an undefined preset, and attributes the outcome to a mechanism the model does not implement.** · **POTENTIAL ROADBLOCK**

- **Where:** `07_conclusion.md:100–109` — *"The robustness of the framework was established through its consistent performance across diverse urban morphologies. The algorithm achieved **stable convergence across six distinct land-use patterns** generated by Cellular Automata, **performing best in "Dense Organic" environments where building clusters create synergistic shading opportunities**. This design choice supports the generalizability of the approach."*
- **Objection:** four defects in one paragraph, each independently disqualifying.
  **(a) The result is not in Results.** §3 comprises §3.1 species performance, §3.2 grid generation, §3.3 ACO search dynamics, §3.4 SECPI outcomes, §3.5 sensitivity. **There is no morphological-robustness subsection**, no per-morphology SECPI comparison, no convergence statistics across morphologies, and no ranking of morphologies. The Conclusion states an outcome — *which* morphology performed best — that the paper never reports, never tabulates, and never plots. A conclusion may summarize Results; it may not introduce them.
  **(b) "Six distinct land-use patterns" contradicts Methods.** §2.2's *"Generating Morphological Archetypes"* (`02_methods_2.1_2.2_grid.md:341–360`) defines **three**: Organic/Clustered, Sparse/Suburban, Linear/Corridor. The number six appears in no Methods section. *(`docs/STATE.md` records **6 morphology presets** in `AuditedCode_1.py` — cited from the project record, not verified here — which would make this a **three-way** split: Methods says 3, the code has 6, the Conclusion says 6. The manuscript is internally contradictory regardless of which is right.)*
  **(c) "Dense Organic" is not a defined term.** The string occurs exactly once in the entire manuscript — this sentence. It is not one of §2.2's three archetype names. A named experimental condition that the paper never defines cannot be a result.
  **(d) The mechanism is not in the model.** *"Building clusters create synergistic shading opportunities"* attributes cooling to shade cast by buildings. §2.3 (`03_methods_2.3_cooling.md:112–118`) states plainly that *"the simplified model does not explicitly model three-dimensional solar geometry"*; height only *"constrains placement in proximity to buildings and infrastructure."* The cooling field is generated by tree crowns through a geometric Gaussian kernel and by nothing else. Buildings occupy cells; they do not shade. **This is the same failure mode as #73** — explaining a purely geometric kernel by naming physical processes the model omits — recurring in the Conclusion, where it is least likely to be caught before submission.
- **Closes when:** `code-stressor` either runs the morphological-robustness experiment §2.5.2 specifies and emits per-morphology results (preset name, n runs, SECPI mean ± SD, convergence statistics, and the **random-placement comparator** §2.5.2 names as the pass criterion) for a new Results subsection, **or** the entire paragraph is deleted from the Conclusion. `math-auditor` states the number and names of morphology presets in the production code so §2.2, §3 and the Conclusion can be reconciled to one figure. The building-shading clause must be deleted regardless — no experiment will make it true. Compounds **#8**, **#73**, **#87**.

**#89 — Conclusion "Sensitivity Index = 0.46" contradicts §3.5.1's 0.4435, and inherits #82.** · PENDING VERIFICATION

- **Where:** `07_conclusion.md:78–80` — *"identifying crown diameter as the single most dominant variable (**Sensitivity Index = 0.46**), far outweighing allometric or shading coefficients."* Against `06_results_discussion.md:623–624` — *"**With an SI of 0.4435**, it exceeds the second-ranked parameter."*
- **Objection:** 0.4435 does not round to 0.46 at any precision — to two places it is **0.44**. The discrepancy is 0.017, roughly four times the second-ranked parameter's entire sensitivity index. Two readings, both bad: either the Conclusion was written against a different sensitivity run than §3.5.1 (in which case the paper reports two sensitivity analyses and identifies neither), or the number was transcribed loosely into the Conclusion (in which case the manuscript's own headline sensitivity figure was not checked against its source). `docs/HANDOVER.md` separately notes 0.46 as *"may be recoverable from `SensitivityAnalyzer` output"* — so a third possibility is that 0.46 is the true production value and §3.5.1's 0.4435 is the stale one. The direction of the fix is unknown, which is why this cannot be closed as a typo.
  The claim also inherits **#82**: no number from the §3.5 sensitivity analysis may be quoted anywhere until the analysis is regenerated. And *"far outweighing allometric or shading coefficients"* inherits **#79** (unequal sweep spans) and **#85** (the allometric arm may be off-path), so even the qualitative comparison is unsettled.
- **Closes when:** `code-stressor` regenerates the sensitivity analysis under Option B and reports the crown-diameter SI once, from a named run; `editor` propagates that single value to §3.5.1, the Conclusion, and anywhere else it appears. Blocked behind **#82**.

**#90 — The Conclusion is the terminal propagation point for the manuscript's three most-quoted defective numbers, and carries a dimensional error of its own. It cannot be edited independently of #62, #63 and #67.** · **POTENTIAL ROADBLOCK**

- **Where:** `07_conclusion.md:64` — *"within a simulated **100 x 100 m²** urban grid."* `:66–68` — *"a maximum localized cooling reduction of **0.80 °C** and a mean reduction of **0.11 °C** across the grid."* `:75–77` — *"fell below a SECPI threshold of **3.13**, representing a performance drop of approximately **28%**."* `:91–95` — *"the efficiency-focused scenario produced a higher mean cooling intensity of **0.19 °C** using a monoculture strategy, the equity-weighted scenario accepted a **42% reduction** in global mean cooling."* `:87–89` — *"The equity-weighting component of SECPI **proved effective**."*
- **Objection:** registered so the Editor cannot treat the Conclusion as a standalone polish job. Every quantitative claim it makes is already flagged upstream, and the Conclusion is where each of them is stated in its most quotable and least qualified form:
  - **°C on all four cooling figures → #62.** The quantity is defined as *"a common, dimensionless scale from 0 to 1"* (§2.3.1) and reported unitless in §3.3.2 (0.131 / 0.809 / 0.160); no proxy-to-kelvin calibration exists anywhere in the manuscript. If #62 resolves as expected, **every °C in this paragraph is deleted** and the Conclusion's quantitative content largely disappears.
  - **0.19 / 0.11 and the 42% → #63.** §3.4.4 prints the efficiency-arm mean as **0.192 unitless** at `06:426` and as **0.19 °C** at `06:514` — the same number, two lines apart in the same subsection, once with a unit and once without. And the 42% recomputes to **31%** if §3.3.2's mean of 0.131 is used instead of §3.4.4's 0.11: (0.19 − 0.11)/0.19 = **42.1%** versus (0.19 − 0.131)/0.19 = **31.0%**. The Conclusion repeats 42% with no indication that the manuscript contains a second mean giving a materially different answer.
  - **3.13 and 28% → #67.** Both are read off a single adjacent rank pair (rank 48 = 4.3651, rank 49 = 3.1336) and restated here as a group-level threshold and a group-level drop, with no group means, no dispersion, no n and no test. `DECISIONS.md` D-06 derives the same 28% a *different* way ((4.3916 − 3.13)/4.3916 = 28.73% vs the manuscript's 1.2315/4.3651 = 28.21%), so two incompatible derivations are already on the project record.
  - ***"Proved effective"* → #69.** The equity component's effectiveness is established by comparing SECPI under two arms that optimize different SECPI functions — circular by construction.
  - **Independently: *"100 x 100 m²"* is dimensionally wrong.** The domain is 100 m × 100 m = 10,000 m². As written it reads as 100 × 100 square metres. `CLAUDE.md` §3 fixes the domain as 100 × 100 m. Mechanical, but it is in the Conclusion's second sentence and is the kind of error that colours a referee's reading of everything after it.
- **Closes when:** #62, #63 and #67 all close, and `editor` rewrites the Conclusion in the same pass as the Abstract and §3.3.2/§3.4.4 so that one mean, one maximum, one percentage and one threshold appear across all four locations. The `m²` fix may be applied immediately. **The Conclusion must not be sent for an Option A polish before those three flags move** — polishing it now would harden numbers that are scheduled for deletion.

**#91 — The Conclusion issues a real-world planting prescription addressed to Philippine urban planners, from a synthetic non-georeferenced study, resting on a finding #46 shows is mis-stated.** · **POTENTIAL ROADBLOCK** *(extends #10 / #11)*

- **Where:** `07_conclusion.md:81–86` — *"This finding carries **significant practical weight for Philippine urban planners**. It suggests that **in resource-constrained settings, prioritizing a few high-performing species with large crown coverage yields cooling outcomes superior to complex mixed-species strategies that rely on smaller trees**."*
- **Objection:** three layers.
  **(a) Scope violation.** `CLAUDE.md` §2 rule 6: the study is synthetic and non-georeferenced — no field site, no real Caloocan raster, no remote-sensing validation. This sentence tells named real-world decision-makers in a named real country what to plant. It is the most direct instance in the manuscript of the objection **#10 / #11** raise against the Title and Abstract, and it is materially worse than those because it is *actionable*: a planner following it would reduce species diversity in real plantings on the strength of a simulation whose cooling field has never been compared to a measurement.
  **(b) The underlying finding is mis-stated.** **#46** establishes that `k` in the combinatorial experiment is the **available palette size**, not the number of species planted: the ACO used the full palette in only 30.16% (WITH) / 19.05% (WITHOUT) of configurations, and the rank-1 k=6 result planted **two** species. The data therefore do not show "few species beat many"; they show *a larger palette converges to the same small high-performing set* — which is a statement about the optimizer, not about planting strategy. The prescription inverts the finding's meaning. **#65** adds that the margin involved (0.0014, 0.03%) is one the Results section itself calls stochastic noise.
  **(c) Ecological one-sidedness.** A recommendation to reduce urban planting diversity carries pest, pathogen and windthrow risk that this model — which optimizes cooling alone — cannot see and never mentions. Recommending monoculture-leaning strategy from a single-objective cooling model, in a Conclusion, without naming that trade-off, is the kind of claim that attracts a hostile referee report rather than a revision request.
  Note that `07_conclusion.md`'s own editorial header already calls this paragraph *"the manuscript's strongest contribution"* which *"should survive intact."* On the evidence in #46, #65 and #67 it should not survive as written; that header note predates the Results pass and should be treated as superseded.
- **Closes when:** #46 and #67 resolve, and `editor` either restates the claim as a property of the optimizer within the synthetic framework (*"a larger available palette did not improve SECPI in this model"*) or moves it to Recommendations as an explicitly untested hypothesis for future empirical work. **The addressee — "Philippine urban planners" — must be removed** unless and until the model is applied to a real site with real data. Any surviving version must name the diversity/resilience trade-off it does not model.

**#92 — The Conclusion claims transferability "across climate-vulnerable cities" and "actionable" outputs, on generalizability evidence that #88 shows does not exist.** · **POTENTIAL ROADBLOCK** *(extends #10 / #11)*

- **Where:** `07_conclusion.md:120–128` — *"the study demonstrates that a discrete lattice optimization approach… produces **actionable and spatially just tree placement strategies**. The framework contributes a **transferable methodology** that bridges computational optimization and urban ecological planning, providing a rigorous foundation for future empirical validation and **scaled implementation across climate-vulnerable cities**."* And `:105–109` — *"This design choice supports the **generalizability** of the approach, making it **adaptable to the varied and often informal urban layouts found in Philippine cities**."*
- **Objection:** transferability is an empirical claim and requires evidence of performance outside the conditions tested. Here it rests entirely on the morphological-robustness paragraph that **#88** shows reports a result absent from §3, contradicts Methods on the number of morphologies, and names an undefined preset. Strip that paragraph and no generalizability evidence remains: **every result in the manuscript comes from a single synthetic 100 × 100 m grid** whose composition §3.2 never even characterizes (**#56**) — the P/A/V cell counts, the seed and the morphology preset for the canonical grid are all unreported. A framework demonstrated on one uncharacterized synthetic instance cannot be described as transferable across a class of real cities.
  *"Actionable"* compounds **#91**: outputs are actionable only if they have been checked against something actionable, and §2.6 concedes there is no empirical thermal measurement anywhere in the study. *"Adaptable to… informal urban layouts found in Philippine cities"* is a claim about real morphologies that the CA presets were never calibrated against — no Philippine land-use raster, no built-density comparison, no goodness-of-fit statistic appears in the manuscript. **#9** separately records that the P/A/V land-use bands themselves lack citable grounding, with the **V 5–10% band having no precedent and being directionally contradicted** by Philippine heat-vulnerability data (Quezon City: 81% of barangays high-risk) — so the synthetic city is not established as resembling a Philippine one even in its land-use proportions.
  *"Climate-vulnerable cities"* additionally imports a policy framing the study never operationalizes: no climate projection, no heat-exposure data, no vulnerability index beyond the model's own author-set zone multipliers.
- **Closes when:** #88 resolves — if the morphological-robustness experiment is run and reported with a random-placement comparator across all presets, a **bounded** generalizability statement becomes available (*"performance was stable across the N synthetic morphologies tested"*). Absent that, `editor` deletes *"transferable,"* *"actionable,"* *"scaled implementation across climate-vulnerable cities"* and the *"adaptable to… Philippine cities"* clause, and reframes the contribution as methodological. `deriver` input on #9 is required before any claim that the synthetic morphologies represent Philippine urban form. Compounds **#9**, **#10**, **#11**, **#56**, **#88**.

---

### Recommendations and back matter

**#93 — The Recommendations disclose the framework's "theoretical nature" in direct contradiction of the Conclusion's prescriptive register three paragraphs earlier, and propose as future work an analysis §3.3.3 already claims to report.** · **POTENTIAL ROADBLOCK**

- **Where:** `07_conclusion.md:131–147` — *"**Due to the theoretical nature of the framework**, future studies can incorporate Geographic Information Systems (GIS) to enhance spatial accuracy, empirical verification, and analytical depth… **Applying the model to a specific city would allow validation against observed land surface temperature data**… **Exploration between the concepts of cooling coverage, cooling intensity and their trade-offs can also be explored** to further advance the rigor of a justifiable cooling for zones."*
- **Objection:** **(a)** The Recommendations are the most honest passage in the manuscript and they contradict the section immediately above them. They concede the framework is *theoretical*, that empirical verification has not occurred, and that *"applying the model to a specific city"* remains future work — i.e. exactly what **#87**, **#91** and **#92** object to the Conclusion for having already claimed. Within roughly 45 lines the manuscript asserts it *"successfully developed and **validated**"* the framework (`:55`), that its findings carry *"**significant practical weight for Philippine urban planners**"* (`:81–82`), and that it produces *"**actionable**… strategies"* transferable to *"climate-vulnerable cities"* (`:123–128`) — and then that the framework is *theoretical* and validation against real land-surface-temperature data has yet to be done (`:132`, `:140–142`). A referee will quote these two passages side by side; they cannot both be defended.
  **This is not resolvable by editing the Recommendations.** The Recommendations are correct. Aligning the two sections means **removing the Conclusion's claims** — substantive rework of the Conclusion, not rewording of the Recommendations. That is the whole content of this flag: the fix has a direction, and the direction is not the obvious one.
  **(b)** *"Exploration between the concepts of cooling coverage, cooling intensity and their trade-offs can also be explored"* proposes as future work a topic **§3.3.3 already has a subsection on** — *"Cooling Coverage-Intensity Trade-Off"* (`06_results_discussion.md:287`). Either §3.3.3 does not deliver what its title claims (which would need registering against §3.3.3, outside this pass's scope but flagged here for whoever revisits it), or the Recommendation is redundant with the paper's own Results. The sentence is also tautological as written (*"Exploration… can also be explored"*) and its closing phrase, *"the rigor of a justifiable cooling for zones,"* is not parseable — narrative-register residue of the capstone origin, in the last substantive paragraph a referee reads.
- **Closes when:** `editor` reconciles the two sections **in the direction the evidence supports** — the Recommendations' disclosure is accurate and stands; the Conclusion's validation, prescription and transferability claims are the ones that move (#87, #91, #92) — and rewrites the coverage/intensity sentence either as a genuine extension of §3.3.3 that states what §3.3.3 did not do, or deletes it. The GIS paragraph should be retained; it is the correct future-work framing and it is what makes the synthetic scope defensible.

**#94 — Individual Author's Contributions lists five contributor entries against six named authors, with initials that do not disambiguate three same-surname authors.** · **POTENTIAL ROADBLOCK**

- **Where:** `07_conclusion.md:148–157` — *"INDIVIDUAL AUTHOR'S CONTRIBUTIONS — **L.G.**; Contributed to research design, code debugging, and in supervising the research manuscript. **V.J.**; Contributed to research methodology, code co-debugging, and in completing the research manuscript. **D.L.Z.**; Performed manuscript revisions, involved in mathematical framework of research. **V.L.**; Completed manuscript revisions, suggested revisions in research design. **V.E.**; Performed manuscript revisions, suggested revisions in research methodology. All contributed to completing the final version of the manuscript."*
- **Objection:** **(a) Five entries, six authors.** The byline is **Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez** (`CLAUDE.md` §1, and the page footer repeated 48 times through the manuscript). Five contributor statements are given. **One named author — on the evidence of the initials, Suarez — has no contribution statement.** The closing *"All contributed to completing the final version"* is a blanket clause, not a contribution, and most journals will not accept it as one. An author on the byline with no attributed contribution is an editorial-office query at submission and, at journals enforcing ICMJE-style authorship criteria, a hold.
  **(b) The initials do not disambiguate.** Three surnames begin with V — **V**alenzuela, **V**illadolid, **V**aldes — and three entries are **V.J.**, **V.L.**, **V.E.** No key is provided anywhere in the manuscript. The scheme also appears inconsistent: **D.L.Z.** carries three letters where the others carry two, presumably for *De Leon*, which makes the surname/given-name ordering unrecoverable for the rest. A reader cannot map any statement to any author with confidence — which defeats the entire purpose of a contributions section.
  **(c) No recognized taxonomy.** The statements use ad-hoc phrasing (*"code co-debugging"*, *"involved in mathematical framework"*). Most Q1 geoscience journals and several preprint servers now require **CRediT** roles. Four of five entries are dominated by *"manuscript revisions"*, which under CRediT is *Writing – review & editing* only; the statements as written do not establish that anyone performed *Software*, *Formal analysis*, *Investigation* or *Data curation*, despite the study being entirely computational.
  This is registered as POTENTIAL ROADBLOCK on the register's own definition — if verification confirms the sixth author has no attributable contribution, the section needs substantive rework (and possibly an authorship discussion), not rewording. **It cannot be fixed by any agent**: only the author team knows who did what.
- **Closes when:** the **research lead** supplies (i) the full name and initials of every author in byline order, (ii) a contribution statement for the missing sixth author or a decision on the byline, and (iii) the mapping of each existing statement to a named author. `editor` then rewrites the section in **CRediT** roles. **This is a submission-blocking item for the preprint, not just the journal** — record it as an open question for the research lead (see Project Log Entry 6).

**#95 — Acknowledgment credits a code editor as a contributor, and the manuscript carries no funding, competing-interests, data-availability or code-availability statement.** · PENDING VERIFICATION

- **Where:** `07_conclusion.md:158–165` — *"ACKNOWLEDGMENT — The researchers acknowledge the contribution of the following: **Visual Studio Code for the hosting of Python and its libraries**, Sir Alyson L. Yap for guidance in the research process, members of the Science Research Committee for the continuous guidance; and school head Dr. Warren A. Ramos for his support in research projects in Caloocan City Science High School."*
- **Objection:** **(a)** Acknowledging an **IDE** as a contributor is a category error — Visual Studio Code neither hosts Python nor its libraries, and a text editor is not an entity that contributes to research. What belongs in a scientific paper is a **software citation**: the interpreter version and the versioned libraries the results depend on. Per **#45** the manuscript's stated stack is already wrong in the other direction — the Abstract credits *scikit-opt*, which `AuditedCode_1.py` never imports, and §2.4.2 credits *Seaborn*, which is not imported either, while the verified dependencies are numpy, matplotlib, scipy (`cdist`), tqdm and pandas (soft). So the manuscript acknowledges an editor it did not depend on and cites two libraries it does not use, while naming none of the five it does. For a computational paper offered for reproduction, that is the reproducibility surface.
  **(b)** Four statements standard at Q1 geoscience journals — and expected on EarthArXiv/OSF — are absent from the manuscript entirely: **Funding**, **Competing interests / Conflict of interest**, **Data availability**, and **Code availability**. Code availability is the pointed one: this is a purely computational study whose entire evidentiary basis is one ~3,670-line script, and the manuscript never states where that script can be obtained. `08_references_appendices.md:482` refers to *"facilitat[ing] reproducibility"* for the framework, which suggests intent, but no statement, repository or DOI appears. A preprint minted without a code-availability statement, for a paper whose results cannot be checked any other way, invites exactly the reproducibility challenge this project has been trying to pre-empt.
- **Closes when:** `math-auditor` supplies the verified dependency list with versions (partly on record from Entry 4 — numpy, matplotlib, scipy, tqdm, pandas — but versions are not) so #45 and this flag can be fixed in one pass; the **research lead** decides the code-deposit target (repository, archive, DOI) and supplies funding and competing-interest declarations; `editor` writes the four statements and converts the software acknowledgment into a citation. **Named artefact:** a submission-readiness checklist for EarthArXiv covering the four statements plus author contributions (**#94**). Compounds **#45**.

> **⚠️ v5 UPDATE to #95 — applied 2026-07-27 by `editorial-flagger`, from Project Log Entry 8's reproducibility attestation. Flagger-initiated. PARTIALLY ADVANCED. Class unchanged: PENDING VERIFICATION.**
> The original finding text above is preserved unaltered.
>
> - **PARTIAL — versions now exist on the record, but for the WRONG environment, and this distinction is load-bearing.** Entry 8 recorded, by execution: **Python 3.14.6** (tags/v3.14.6:c63aec6), **numpy 2.4.2, scipy 1.17.0, pandas 3.0.0, matplotlib 3.10.8**. **`tqdm`'s version was not recorded.**
> - **⚠️ These are the versions of the 2026-07-27 AUDIT environment (`.venv`), not the versions that produced any published result.** Per **#82** v5 and **#97**, the published §3.5 numbers were not produced by this code at all, and per D-06 outcome (b) the published §3.1 numbers came from a 2026-02-13 pre-audit run. **A software-availability statement built on these versions would assert a provenance the project cannot support.** They are usable for the *forthcoming* regeneration, not retroactively.
> - **STILL OWED:** `tqdm`'s version; a decision on whether the manuscript reports the **audit/regeneration** environment (correct, once regeneration lands) or attempts to reconstruct the original one (probably impossible); and everything in objection (b) — the four missing Funding / Competing-interests / Data-availability / Code-availability statements, which need the **research lead**, not an agent.
> - **Practical consequence for #45:** the environment is now pinned well enough to write a correct dependency list *after* regeneration. Doing it before would put a third wrong stack in the manuscript.
>
> *Basis: Project Log Entry 8, "Reproducibility attestation".*

---

## v5 — New flags #96–#97 (from executed code, Project Log Entry 8)

> **Scope:** Project Log Entry 8, the `math-auditor` execution audit of `SensitivityAnalyzer` (2026-07-27, commit `0e912d1`). Entry 8 created, closed and reclassified nothing by design and routed all of its evidence to this register.
>
> **These are the first flags in this register raised from executed code rather than from reading.** Every preceding pass (v1–v4) was read-only. That changes the evidentiary character of what follows: the structural claims below were **observed**, not inferred, and are reproducible from the harness Entry 8 documents.
>
> **2 flags: 2 POTENTIAL ROADBLOCK, 0 PENDING VERIFICATION, 0 ROADBLOCK (SEVERE).** **#96 and #97 were the next two free numbers** per the v4 Register-status block, `docs/STATE.md`'s authoritative count block, and Entry 8's own recommendation. **Nothing was renumbered.**
>
> **A second ROADBLOCK (SEVERE) was recommended and is declined.** Entry 8 wrote of the state leak: *"it warrants a flag and, on its face, a severe one — it invalidates the executed §3.5 parameter table wholesale, not merely its aggregation."* That is a recommendation from another agent, not a decision, and this register weighs it and declines it. **The reasons are argued in full inside #96 and #97 and must be read there** — they are not assumed, and they are not a judgement that the defects are minor. **#82 remains the project's only ROADBLOCK (SEVERE).**
>
> **Attestation:** every number below is quoted from Project Log Entry 8, cited to its section and execution phase. **Nothing in this block was computed, interpolated or estimated by the flagger.** Entry 8's binding scope limits — one grid, one morphology, one seed, `n_samples = 3`, no D-02 ceiling applied, no output written to `results/`, and *"no number in this entry should be quoted as a manuscript value"* — are carried forward and re-stated at every point where a magnitude is used.

---

### The reference implementation (`legacy/AuditedCode_1.py`)

**#96 — 🔴 `SensitivityAnalyzer._run_single_evaluation` permanently mutates the class-level `TreeSpecies.SPECIES_DATA` and never restores it. Every sensitivity evaluation after the first species perturbation runs against corrupted species data, the LAI path compounds geometrically, and the function is not idempotent. §3.5.1's "all others were held at baseline values" is false in the implementation.** · **POTENTIAL ROADBLOCK** *(argued down from a recommended SEVERE — see "Why not SEVERE" below)*

- **Where:** `legacy/AuditedCode_1.py` — `SensitivityAnalyzer._run_single_evaluation`, **lines 879, 880 and 882**. Against Results §3.5.1 (`06_results_discussion.md:608–612`) — *"Each parameter was evaluated at its low and high bounds while **all others were held at baseline values**."*

- **Objection.** Five findings, each executed, in ascending order of consequence.

  **(a) The target of the mutation is shared global state.** `TreeSpecies.SPECIES_DATA` is a **class attribute**, not an instance attribute. Entry 8 §D1:

  ```
  TreeSpecies.SPECIES_DATA is a CLASS attribute:              True
  instance a.SPECIES_DATA is instance b.SPECIES_DATA:         True
  instance a.SPECIES_DATA is TreeSpecies.SPECIES_DATA:        True
  ```

  `_run_single_evaluation` writes into it at line 880 (`ts.SPECIES_DATA[species][param_name] = value`) and line 882 (`ts.SPECIES_DATA[species]['LAI'] = hardcoded_lai * ratio`). **There is no copy, no context manager, and no `finally`.** Nothing restores it.

  **(b) The mutation escapes the evaluation entirely.** Entry 8 §D2 — the defect surfaced when a freshly-constructed `SensitivityAnalyzer` reported Narra's crown-diameter *base* as 34.0 m after an unrelated evaluation had set it there:

  ```
  after evaluating Narra CD at its HIGH bound 27.6:
    TreeSpecies.SPECIES_DATA['Narra']['crown_diameter_m'] = 27.6  (was 23.0)
    a BRAND-NEW TreeSpecies() sees                        = 27.6
    a BRAND-NEW CorrectedCoolingModel sees                = 27.6
    a BRAND-NEW SensitivityAnalyzer's declared base       = 27.6
    -> the perturbation is NEVER restored.
  ```

  A perturbation applied for one evaluation is observed by every subsequently constructed object in the process. **Constructing a fresh analyzer does not reset anything**, which is why this survived every prior read-only pass: nothing about the source suggests that a new object inherits a previous run's perturbations.

  **(c) The LAI path compounds geometrically, so the function is not idempotent.** Line 879 reads the **current** LAI; line 880 writes `current × ratio`. Repeating an identical input keeps multiplying. Entry 8 §D3, six identical `Narra.l0 = 0.30` evaluations from a clean reset:

  ```
  Narra LAI reset to: 6.07
    after identical Narra.l0=0.30 evaluation #1: 7.284000
    after identical Narra.l0=0.30 evaluation #2: 8.740800
    after identical Narra.l0=0.30 evaluation #3: 10.488960
    after identical Narra.l0=0.30 evaluation #4: 12.586752
    after identical Narra.l0=0.30 evaluation #5: 15.104102
    after identical Narra.l0=0.30 evaluation #6: 18.124923
    -> an IDENTICAL input produces a DIFFERENT model each time.
  ```

  **This destroys the stated purpose of `n_samples`.** §3.5.1 says the three repeats are averaged *"to reduce stochastic noise"* — i.e. three samples of one model. **They are three different models.** Averaging them is not variance reduction; it is averaging across a systematic drift. Note also that 6.07 → 18.12 is a **~3× excursion** that carries Narra's LAI far outside the 3–6.5 band D-09 relies on for physical plausibility, so some evaluations are performed on a physically implausible tree.

  **(d) After one full 40-parameter sweep, every species has drifted, and the drift is systematic rather than random.** Entry 8 §D4, ACO stubbed so only the state trajectory is measured:

  ```
  state AFTER a full 40-parameter sweep (CD, height, LAI):
      Narra          before=(23.0, 30.0, 6.07)  after=(27.6, 36.0, 5.8595)  <-- CHANGED
      Talisay        before=(12.0, 35.0, 4.4 )  after=(14.4, 42.0, 4.9315)  <-- CHANGED
      Banaba         before=(11.0, 13.5, 3.87)  after=(13.2, 16.2, 2.4288)  <-- CHANGED
      Kabiki         before=(11.0, 13.5, 4.12)  after=(13.2, 16.2, 2.4819)  <-- CHANGED
      Duhat          before=( 9.5, 22.0, 3.52)  after=(11.4, 26.4, 3.1504)  <-- CHANGED
      Akleng-parang  before=(24.0, 24.0, 3.15)  after=(28.8, 28.8, 2.82  )  <-- CHANGED
  ```

  **Every species ends at its HIGH crown diameter and its HIGH height** — last-write-wins, because the high bound is evaluated after the low bound for each parameter — **and LAI has drifted by up to −37%** (Banaba 3.87 → 2.43). This is not noise; it is a deterministic, order-dependent bias with a known direction.

  **(e) The contamination has a precise boundary, which tells the team exactly which rows are clean.** `_define_parameters()` iterates `Cooling_Model → Weighting → Species_Morphology → Species_Allometry`. Therefore:
  - The **3 baseline evaluations** and all **24 `Cooling_Model` / `Weighting` evaluations** run against **pristine** species data. **These are the only clean rows in the entire table.**
  - From the **first `Species_Morphology` evaluation** onward, contamination accumulates monotonically. By the time the 24 `Species_Allometry` parameters are swept, all six species sit at high CD, high height and drifted LAI.

  So the executed §3.5 table is **27 valid rows and 36 invalid ones**, and the invalid ones include every parameter the manuscript's §3.5.1 and §3.5.3 arguments are built on.

- **Measured cost, with an internal control.** Entry 8 §D5 re-ran the identical sweep with `SPECIES_DATA` snapshotted and restored around every evaluation — repaired **in the harness only; `legacy/AuditedCode_1.py` was not modified**:

  | Category | n | mean (leaked) | mean (repaired) | max (repaired) |
  |---|---|---|---|---|
  | Cooling_Model | 3 | 0.059809 | **0.059809** | 0.169702 |
  | Species_Allometry | 24 | 0.012433 | **0.006749** | 0.021910 |
  | Species_Morphology | 12 | 0.006593 | **0.010466** | 0.044368 |
  | Weighting | 1 | 0.001385 | **0.001385** | 0.001385 |

  **`Cooling_Model` and `Weighting` are bit-identical across the two runs** — exactly as (e) predicts, since they are evaluated before any species mutation and consume the same RNG stream. **That bit-identity is the internal control**: it establishes that the harness is sound and that the divergence in the other two categories is attributable to the leak and to nothing else. On that control, **the leak inflates apparent allometric sensitivity by 1.84× and deflates morphological sensitivity by 0.63×.**

  > **⚠️ Magnitude caveat, binding.** 1.84× and 0.63× are **single-run diagnostics** — one grid, one morphology, one seed, `n_samples = 3`, no D-02 ceiling applied, nothing written to `results/`. They establish **direction and rough scale** with unusual confidence because of the bit-identity control, but they are **not publishable values.** The claims in (a)–(e) above are structural and deterministic and carry no such caveat.

- **Why this is decisive for #75, and why it was invisible to four editorial passes.** §3.5.1's *"all others were held at baseline values"* **is the definition of a local OAT.** The implementation does not satisfy it. Combined with the confirmed finding that the code is also not Morris, **the executed design is a sequentially contaminated, order-dependent two-level sweep matching neither named method** — which is why **#75**'s verdict is **(c)** and not (b). No read-only pass could have found this: the source of `_run_single_evaluation` looks like a normal parameter override, and the defect is visible only in the *identity* of `SPECIES_DATA` and in the *history* of successive calls.

- **⛔ Why NOT ROADBLOCK (SEVERE) — argued, not assumed.** Entry 8 recommended severe *"on its face."* This register declines, and #82 remains the only SEVERE. The register reserves SEVERE for a finding **confirmed unresolvable as written**, where the section must be reworked rather than reworded. Testing #96 against the three conditions #82 satisfies:
  1. **Confirmed, not pending — ✅ SATISFIED.** Deterministic, reproducible, observed by execution. No dispute.
  2. **Unresolvable — ❌ NOT SATISFIED, and this is the decisive one.** #82 is severe because *the correct values are not recoverable from anything* — not from the manuscript, and (per #82 v5) not from the codebase either. **#96 has a known, small, local remedy that has already been executed successfully:** snapshot `TreeSpecies.SPECIES_DATA` at the top of `_run_single_evaluation` and restore it in a `finally`. Entry 8's Phase H harness did exactly this and verified the post-sweep state pristine. A defect with a proven fix on the table is not "unresolvable."
  3. **The section must be reworked — ✅ SATISFIED, but adds nothing.** §3.5 is **already** under a standing regenerate-don't-rewrite injunction from **#82** and **D-11**. Escalating #96 would not change what anyone does next.

  **Two further reasons, both about not misleading the research lead.** *First*, #96 does **not** invalidate the manuscript's published §3.5 — **#82** v5 and **#97** establish that those numbers did not come from this code at all. #96's harm is **prospective**: it corrupts the regeneration D-11 has ordered, if that regeneration runs unfixed. *Second*, the register's severe count is a triage signal. Recording two SEVERE flags would tell the research lead there are two independent unresolvable manuscript defects, when the true position is **one unresolvable manuscript defect (#82) plus one fixable code defect that blocks its remedy.** Overstating that would be as damaging as understating it.

  **This is not a downgrade of any existing flag and no flag's class is reduced by it.** It is a first classification, made against the register's own definitions, that declines another agent's recommendation. *(Log citation: Project Log Entry 8, "Flags touched" and "Still open / unresolved" item 2.)*

- **⚠️ Escalate to ROADBLOCK (SEVERE) if any of the following becomes true:**
  1. The **research lead declines to authorize the fix**, or authorizes proceeding with the leak in place. Condition 2 then flips: a defect the project has chosen not to remedy is unresolvable in the sense that matters.
  2. **#75** is settled in favour of option (3) — reporting the contaminated sweep as-run.
  3. Evidence emerges that the leak was **present in whatever code produced the published §3.5 numbers**, in which case it becomes a defect in the published record rather than only in the forward path.

- **🔴 This flag blocks D-11 and outranks its two named prerequisites in urgency.** D-11 currently names **#75** and **#77** as its only prerequisites. **#96 is a third, and it is different in kind:** #75 and #77 need a decision, whereas #96 needs a **semantic change to the reference implementation**, which per `CLAUDE.md` §8.1 requires the research lead's authorization. Entry 8 states the position plainly: *"Do not run D-11's regeneration before it lands — you would burn ~8 minutes producing a fourth invalid table."* **The orchestrator should route this into `docs/DECISIONS.md`; the flagger does not open `D-xx` entries.**

- **Closes when:** the **research lead** authorizes a semantic fix to `legacy/AuditedCode_1.py` (or to the `src/secpi/` port); `code-stressor` applies it — snapshot `TreeSpecies.SPECIES_DATA` on entry to `_run_single_evaluation`, restore in a `finally`, using Entry 8's Phase H harness as the template — **and repoints the hardcoded `n_samples` at the study configuration in the same pass** (see **#77**); `math-auditor` re-verifies by executing the idempotency probe (§D3) and the post-sweep drift probe (§D4) against the fixed implementation and confirming **zero** drift and **bit-identical** repeated evaluations; and the D-11 regeneration is then run against the fixed code. **Until all of that lands, no sweep output from `SensitivityAnalyzer` may be used for any purpose, and no §3.5 number may be regenerated.** Cross-links: **#75** (cannot close before this), **#77** (same fix pass), **#78** (the noise floor was measured on the repaired sweep), **#79** (bounds evidence from the same audit), **#82** (this is one of the two reasons regeneration will not vindicate §3.5), **#85** (its call-path trace must be run *after* this fix), **#97** (the second reason).

---

### Results §3.5 — survival of the findings, not just the numbers

**#97 — 🔴 §3.5's qualitative findings do not survive execution against the reference implementation. The manuscript's rank-1 parameter ranks 28th of 40, the executed rank-1 is the parameter §3.5.2 explicitly dismisses, the category hierarchy is inverted, and the headline effect points in the opposite direction. The sweep bounds the manuscript reports are not in the code.** · **POTENTIAL ROADBLOCK**

- **Where:** §3.5.1 (`06_results_discussion.md:626–639`) — *"Sweeping Narra's crown diameter from its manuscript low of **12.0 m** to its high of **34.0 m**… When set to its upper bound (34.0 m)… the expanded decay envelope amplifies both direct cooling coverage and the vulnerability-weighted reward, producing SECPI scores comparable to the top-ranked combinatorial configurations"* (3.024 → 4.380, effect 1.356, SI 0.4435). §3.5.2 (`:674–675`) — decay lambda *"limited impact (0.0015)"* — and (`:667`) — *"The relatively low sensitivity of the **Cooling Model** category is noteworthy."* §3.5.3 (`:700–703`) — *"swept across a **15% uncertainty band**."*

- **Objection.** This flag is separate from **#82** and must not be folded into it. #82 establishes that §3.5.**2**'s category means are arithmetically impossible, and explicitly preserved the possibility that *"§3.5.1 may be salvageable while §3.5.2 is not."* **This flag removes that possibility.** It is also separate from **#75** (which is about the *method named* vs the *method run*) and from **#79** (which is about *comparability between* parameters). #97 is about whether §3.5's **findings** survive at all.

  **(a) STRUCTURAL, DETERMINISTIC — the manuscript's sweep bounds do not exist in the code.** Entry 8 §B dumped `parameter_definitions` for all 40 swept parameters. Every one of the 36 species parameters is swept at a uniform **±20% of base** (`rel_span = 0.4000`). Consequently:
  - **§3.5.1's headline sweep, Narra crown diameter 12.0 → 34.0 m, is not in this code.** The code sweeps **18.4 → 27.6 m** about a base of **23.0 m**.
  - **§3.5.3's *"15% uncertainty band"* for the allometric constants is not in this code either.** It is ±20%, i.e. a 40% span.
  - The manuscript therefore states **two** perturbation conventions, and the reference implementation implements a **third** that matches neither. This is the same class of defect as the grid resolution stated three ways (#28/#33) and the ACO configuration stated three ways (#57 v5), now in the sensitivity design.

  This half requires no execution beyond reading the executed parameter table, is deterministic, and is **not subject to Entry 8's single-run caveat.** On its own it is already sufficient to forbid rewriting §3.5.1: **the numbers 3.024, 4.380, 1.356 and 0.4435 have no known provenance in the reference implementation.**

  **(b) The manuscript's own bounds, forced through the same code path, give the OPPOSITE SIGN.** Entry 8 Phase F2 ran the manuscript's own 12.0 / 34.0 m endpoints through the identical code path, `n = 3` each:

  ```
  CD=12.0 -> [3.2067, 3.2504, 3.1825]  mean=3.2132   (manuscript: 3.024)
  CD=34.0 -> [2.7408, 2.8752, 2.9491]  mean=2.8550   (manuscript: 4.380)
  absolute effect = 0.3582                           (manuscript: 1.356)
  SI vs executed baseline 3.2155 = 0.1114            (manuscript: 0.4435)
  SI vs manuscript baseline 3.0576 = 0.1171
  ```

  **The manuscript reports that enlarging Narra's crown from 12 m to 34 m *raises* SECPI. Execution gives a *fall*.** The magnitude is also ~3.8× smaller. §3.5.1's causal narrative — *"the expanded decay envelope amplifies both direct cooling coverage and the vulnerability-weighted reward"* — **describes a response the implementation does not exhibit, in either magnitude or direction.** Entry 8 declines to assign a mechanism without a dedicated run, and so does this flag; a plausible but **unverified** candidate is that at 34 m the CCA/competition penalty and CPA renormalization dominate.

  **(c) The rank ordering collapses and the category hierarchy inverts.** From Entry 8's leak-repaired sweep (§D6):
  - **`Narra.crown_diameter_m` ranks 28 of 40, at SI 0.002245** — against the manuscript's **rank 1, SI 0.4435**.
  - The executed **rank 1 is `decay_lambda` at SI 0.1697** — *the parameter §3.5.2 explicitly dismisses as having "limited impact (0.0015)"* — and it is **larger than the next index by 3.8×**.
  - The dominant category by mean is **`Cooling_Model`**, which §3.5.2 calls *"relatively low sensitivity."* **§3.5.2's stated hierarchy is inverted.**

  **(d) What falls with this.** §3.5.1's headline finding and its causal narrative; §3.5.2's category hierarchy and its dismissal of the Cooling Model category; §3.5.3's robustness inference (already independently attacked by **#78** and **#85**); the Conclusion's *"Sensitivity Index = 0.46"* (**#89**); Figure 33 and Figure 34 (**#81**); and **#86**'s field-measurement prescription, which exists **only** because crown diameter is claimed to dominate. If crown diameter ranks 28th, *"the single most critical field measurement for future empirical calibration"* has no basis at all. **The Abstract and Conclusion must be checked for inherited §3.5 claims before either is redrafted.**

  **(e) Why this is not a numbers-refresh.** D-11 orders regeneration under Option B, which the project has framed as changing *magnitudes*. **This flag establishes that regeneration will change the *findings*.** Anyone approaching §3.5 expecting renormalized versions of the same conclusions will be wrong. Combined with **#82** v5, the position is: **regeneration will neither reproduce nor vindicate §3.5.**

- **⚠️ Magnitude caveat, binding and consequential for this flag's class.** Objections **(b)** and **(c)** rest on **single-run diagnostics** — one grid, one morphology, one seed, `n_samples = 3`, no D-02 ceiling applied, nothing written to `results/`. Entry 8 states that **no number in it may be quoted as a manuscript value** and that `code-stressor` owns their formal replication. Two specific cautions:
  - The measured SI noise floor is **≈ 0.0098** (**#78**), and `Narra.crown_diameter_m`'s executed SI of **0.002245 sits below it** — so *"ranks 28/40"* should be read as *"is not resolvable above noise,"* which is the weaker but sounder statement. Consistent with this, the same parameter ranked **31/40** in Entry 8's Phase E run and **28/40** in its Phase H run.
  - The sign inversion in (b) is a **0.358 separation between two non-overlapping triplets**, an order of magnitude above the 0.0386 baseline SD, so it is unlikely to be noise — **but it is still one grid and one seed**, and it must be replicated before it is asserted in prose.

- **Why POTENTIAL ROADBLOCK and not ROADBLOCK (SEVERE) — argued, not assumed.** Testing against the three conditions #82 satisfies:
  1. **Confirmed, not pending — ◐ PARTLY.** Objection (a) is confirmed and deterministic. Objections (b) and (c) are single-run and Entry 8's own binding scope limits forbid asserting them as established. **A SEVERE classification resting on a caveated single-run magnitude would violate the scope limit this register agreed to carry, and would be the exact failure mode `CLAUDE.md` §8.1 warns about.**
  2. **Unresolvable — ❌ NOT ESTABLISHED, and there is a live benign path.** #82 is severe because its defect is impossible **on the manuscript's own printed values, regardless of which code produced them.** #97's defect is *non-reproduction from the current code*, which has a known and precedented alternative explanation: **the published §3.5 numbers may come from a pre-audit code iteration, exactly as D-06 established for §3.1** (outcome (b) — *"reproducible AND superseded"*). Under that explanation §3.5 is **obsolete**, not impossible — a materially different finding. **The project has precedent for downgrading on exactly this basis: #43 went POTENTIAL ROADBLOCK → RESOLVED when its output was located in `legacy/archive/`.** Until the forensic question is answered, "unresolvable" is not established.
  3. **The section must be reworked — ✅ SATISFIED**, and §3.5 is already under that injunction via #82 and D-11.

  **The distinction is real, not a hedge.** #82 says *"this cannot be true."* #97 says *"this is not what the reference implementation does, and we do not yet know what produced it."* Those warrant different classes, and conflating them would weaken #82 — the register's one unassailable finding — by association with a claim that has an open benign explanation.

- **⚠️ Escalate to ROADBLOCK (SEVERE) if either becomes true:**
  1. `code-stressor`'s replicated, multi-seed regeneration under D-11 **confirms the sign inversion and the rank collapse.** §3.5 then falls in its entirety and the Abstract, §3.5.1, §3.5.2, §3.5.3, the Conclusion and **#86**'s prescription all require substantive rework rather than renumbering.
  2. The forensic search returns **no source** for the published §3.5 numbers — i.e. they are neither reproducible from current code nor traceable to an archived pre-audit run. §3.5 would then carry numbers of **no known provenance whatsoever**, which is a stronger defect than #82's.

- **🔴 A forensic question this flag depends on, and which currently belongs to nobody.** **Where did §3.5's published numbers come from?** Not from `AuditedCode_1.py` — established twice over, by the bounds mismatch in (a) and by the category-mean non-reproduction in **#82** v5. This is **structurally identical to the question D-06 asked about §3.1**, and `legacy/archive/` holds pre-audit iterations that have already answered one such question once. Entry 8 raises it and recommends the orchestrator route it. **It may warrant its own `D-xx`; the flagger does not open `D-xx` entries.** Until it is answered, **no §3.5 number has a known provenance.**

- **Closes when:** (i) the **#96** state leak is fixed and **#75**'s three-way design question is settled, so a valid sweep can be run at all; (ii) `code-stressor` regenerates §3.5 under Option B **across multiple seeds and grids**, with the per-index `n` and `SD` that **#77** shows the implementation cannot currently produce, into a single named run in `results/`; (iii) the resulting ranking is reported **with every index below the measured noise floor marked unresolved rather than ranked** (**#78**); (iv) the forensic provenance question above is either answered or formally recorded as unrecoverable; and (v) `editor` rewrites §3.5.1, §3.5.2 and §3.5.3 **from the emitted table only**, and audits the Abstract, the Conclusion and **#86** for inherited claims. **Until then §3.5 must not be rewritten in any part — it must be regenerated — and no number from it may be quoted in the manuscript, the Abstract, or the Conclusion.** Cross-links: **#75**, **#76**, **#78**, **#79**, **#80**, **#81**, **#82** (supersedes its *"§3.5.1 may be salvageable"* note), **#84**, **#85**, **#86**, **#89**, **#96**.

---

## Register status

**The register is complete through the whole manuscript.** Every section — Title, Abstract, Introduction, Methods §2.1–§2.6, Results and Discussion §3.1–§3.5, Conclusion, Recommendations, Individual Author's Contributions, Acknowledgment — has now had at least one editorial pass. Nothing in this file forward-references a flag that does not exist below it.

~~**Totals (per-flag enumeration, v4):** 29 · 2 · 30 · 33 · 1 · **95 total.** **Next free flag number: #96.**~~ — **superseded 2026-07-27 (v5).**

### 🔢 Totals — v5, re-derived by per-flag enumeration (2026-07-27)

**Derived by enumerating every flag number from #1 to #97 individually and assigning it to exactly one class. The v4 total was NOT incremented.** Each roster below is written out in full so the next reader can check the arithmetic without re-reading the file.

| Category | Count |
|---|---|
| RESOLVED — Cleared Up | **29** |
| RESOLVED — Deferred | **2** |
| PENDING VERIFICATION | **29** |
| POTENTIAL ROADBLOCK | **36** |
| **ROADBLOCK (SEVERE)** | **1** |
| **TOTAL LIVE FLAGS** | **97** |

**Next free flag number: #98.**

**RESOLVED — Cleared Up (29):** #1, #2, #3, #4, #6, #7, #8, #10, #11, #12, #15, #16, #17, #18, #19, #23, #25, #26, #28, #31, #32, #33, #34, #35, #38, #40, #41, #43, #51.

**RESOLVED — Deferred (2):** #24, #27.

**PENDING VERIFICATION (29):** #5, #9, #13, #14, #20, #21, #22, #29, #36, #37, #42, #45, #47, #49, #50, #53, #58, #59, #61, #63, #65, #66, #71, #73, #74, #76, #81, #89, #95.

**POTENTIAL ROADBLOCK (36):** #30, #39, #44, #46, #48, #52, #54, #55, #56, #57, #60, #62, #64, #67, #68, #69, #70, #72, #75, **#77**, #78, #79, #80, #83, #84, #85, #86, #87, #88, #90, #91, #92, #93, #94, **#96**, **#97**.

**ROADBLOCK (SEVERE) (1):** **#82** — and #82 alone. See #96's *"Why NOT ROADBLOCK (SEVERE)"* block for the argument declining a second.

29 + 2 + 29 + 36 + 1 = **97** ✓, and the four rosters plus #82 enumerate #1–#97 with no gaps and no flag counted twice ✓.

**Δ from v4 (95):** three movements, no renumbering.
| Flag | v4 | v5 | Cause |
|---|---|---|---|
| **#77** | PENDING VERIFICATION | **POTENTIAL ROADBLOCK** | Objection (b) confirmed by execution — no dispersion is computed or storable, so D-11's required per-index SD cannot be produced by the current implementation. Objection (a) reframed, not dropped. *(Project Log Entry 8 §E3.)* |
| **#96** | — | **POTENTIAL ROADBLOCK** (new) | `SensitivityAnalyzer` state leak. *(Project Log Entry 8 §D.)* |
| **#97** | — | **POTENTIAL ROADBLOCK** (new) | §3.5's qualitative findings do not survive execution. *(Project Log Entry 8 §B, §D6.)* |

**Updated in place, class unchanged:** #57, #58, #75, #76, #78, #79, #82, #85, #95.

> **⚠️ SUPERSEDED INSTRUCTION — read before scheduling the next pass.**
>
> The v4 text of this block, and `docs/STATUS.md`, both directed a future references-and-appendices pass to *"assign from #96."* **That instruction is void: #96 and #97 were assigned on 2026-07-27 from Project Log Entry 8's executed evidence.** **The references-and-appendices pass assigns from #98.** `docs/STATE.md` and `docs/STATUS.md` both still record "next free: #96" and are now stale on this point; they are owned elsewhere and were not edited by this pass. Whoever next syncs them should take **#98** from here.

**Not covered by any pass, and therefore still uninspected:** `manuscript/sections/08_references_appendices.md` — the reference list itself (individual citation verification beyond the spot-checks in #14, #20, #21, #22, #26, #49) and Appendices A–B. That file's own editorial header already flags Appendix A's Figures A1–A28 as requiring a referenced-in-text check, which **#81** now shows is a document-wide problem. **A references-and-appendices pass should be scheduled; assign from #98.**
