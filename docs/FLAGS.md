SECPI Manuscript — Comprehensive Editorial Flag Archive (v3 — Results/Discussion/Conclusion first pass)

**Sections reviewed:** Title, Abstract, Introduction, Methods (§2.1–§2.6), **Results and Discussion (§3.1–§3.5)**, **Conclusion / Recommendations / back matter**
**Update source (v2):** Cross-referenced against SECPI Project Log Entries 1–3 (Mathematical Auditor sessions, code-execution-verified against `AuditedCode_1.py`)
**Update source (v3):** Project Log Entry 4 + `docs/STATE.md` (movement blocks for #42–#51, reconciled into this file verbatim in substance), plus the first-ever editorial read of `manuscript/sections/06_results_discussion.md` and `manuscript/sections/07_conclusion.md` (Project Log Entry 5).
**Session pause point:** none remaining. Every section of the manuscript has now had at least one editorial pass. ~~**Next free flag number: #95.**~~ — ⚠️ **superseded: the register is truncated at #74 and the next free number is #75.** See the truncation notice in the Executive Summary below.

> ⚠️ **v3 was a read-only editorial pass. No code was executed.** Every finding below that depends on program behavior is registered as PENDING VERIFICATION or POTENTIAL ROADBLOCK with a named owning agent and a named run. Arithmetic checks performed by hand on the manuscript's own reported values are labelled as such.

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

| Category | Count (v1) | Count (v2) | Count (v3) | Δ v2→v3 |
|---|---|---|---|---|
| RESOLVED — Cleared Up | 17 | **25** | **29** | +4 |
| RESOLVED — Deferred | 2 | 2 | 2 | — |
| PENDING VERIFICATION | 19 | **14** | **32** | +18 |
| POTENTIAL ROADBLOCK | 3 | **0** | **30** | +30 |
| ROADBLOCK (SEVERE) | 0 | 0 | **1** | +1 |
| **TOTAL FLAGS IDENTIFIED** | 41 | 41 | **94** | +53 |

> ### 🔴 THIS FILE IS TRUNCATED — the v3 column above is aspirational, not actual
>
> **Added by the orchestrator, 2026-07-25 (Project Log Entry 5).** The v3 session terminated mid-write. The register ends at **#74**, followed by the stub `## Resuming This Review — PLACEHOLDER`. **Flags #75–#94 were never written to this file.** That includes:
>
> - **#75** — the claimed first ROADBLOCK (SEVERE), §3.5's category-level sensitivity means. Forward-referenced twice above (v3 note under ROADBLOCK (SEVERE), and item 2 of "What moved and why"). **It does not exist below.**
> - **#79** (§3.5.3 false provenance, refines #30), **#90** (Conclusion "successfully developed and validated", extends #8), **#91 / #92** (Conclusion georeferencing and transferability, extend #10/#11) — all four forward-referenced in the "Escalations and refinements" table below. **None exists below.**
>
> **Counts for the register as it actually stands (#1–#74), derived per-flag:**
>
> | Category | As written (#1–#74) | v3 column claims | Gap |
> |---|---|---|---|
> | RESOLVED — Cleared Up | **29** | 29 | — |
> | RESOLVED — Deferred | **2** | 2 | — |
> | PENDING VERIFICATION | **25** | 32 | −7 |
> | POTENTIAL ROADBLOCK | **18** | 30 | −12 |
> | ROADBLOCK (SEVERE) | **0** | 1 | −1 |
> | **TOTAL** | **74** | 94 | −20 |
>
> Basis: the 51-flag per-flag reconstruction this file already adopts (29/2/17/3/0), plus v3's escalations of **#39** and **#44** (PENDING → POTENTIAL ROADBLOCK, −2 pending / +2 PR), plus the 23 flags actually written (**#52–#74**: 13 POTENTIAL ROADBLOCK, 10 PENDING VERIFICATION). No flag content, wording, or classification was altered by this note.
>
> **Next free flag number is #75, not #95** — nothing has been assigned above #74. Do not quote the v3 column or the "#95" in the header until #75–#94 are written or the numbering is formally released.

**What moved and why (v1 → v2):** all 3 POTENTIAL ROADBLOCK flags (#25, #28, #33) closed via direct code execution against `AuditedCode_1.py`. 5 PENDING VERIFICATION flags (#31, #34, #35, #38, #41) closed the same way. No flag escalated in severity. Full detail below.

**What moved and why (v2 → v3):**

1. **#42–#51 formally registered into this file** (they existed only in `docs/STATE.md`). Transcribed verbatim in substance; no status re-derived, no wording of a finding changed.
2. **#52–#94 added** — 43 new flags from the first editorial pass over Results and Discussion (§3.1–§3.5) and the Conclusion. 27 are POTENTIAL ROADBLOCK, 15 PENDING VERIFICATION, **1 is the project's first ROADBLOCK (SEVERE)** — #75, §3.5's category-level sensitivity table, whose reported means are arithmetically impossible against the SI definition given one subsection earlier.
3. **#39, #44, #46, #30, #6, #10, #11 escalated or refined** — see the "Escalations and refinements of existing flags" block below. No existing flag was downgraded in v3.

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

> v3 note: #30 has since moved back into this category, and 27 new flags (#52–#94) enter it. The file-wide POTENTIAL ROADBLOCK count is **30**. See the v3 blocks below.

---

### ROADBLOCK (SEVERE) (0 flags — of #1–#41, as of v2)

None currently confirmed at this stage of review — unchanged.

> v3 note: the file-wide SEVERE count is now **1** — Flag **#75** (§3.5 category-level sensitivity means are arithmetically impossible). This is the project's first. See the v3 blocks below.

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
| **#30** | Refined (class unchanged: POTENTIAL ROADBLOCK) | Results §3.5.3 states the allometric constants were *"sourced from literature."* Entry 3 established they have no literature source and are 22–77× off an empirical refit; D-09 records them as author estimates. #30 was a Methods-scoped defect; it is also a **false provenance claim in Results**. Registered as #79. |
| **#6** | Refined (class unchanged: RESOLVED) | #6 resolved the Abstract's 28% / 0.03% as raw percentage differences rather than tests. v3 finds §3.4.2 goes further: it states the 0.03% margin *"falls well within the stochastic variation inherent to the ACO metaheuristic across independent runs"* — i.e. the manuscript's own Results declares its own headline number to be noise. Registered as #65. |
| **#10 / #11** | Extended in scope | The synthetic/non-georeferenced objection was raised against the Title and Abstract. The Conclusion reoffends independently and more seriously: a real-world planting prescription for Philippine planners, and a transferability claim across "climate-vulnerable cities." Registered as #91, #92. |
| **#8** | Extended in scope | "No field or remote-sensing validation" was an Abstract-scoped lock. The Conclusion asserts the framework was *"successfully developed and validated"* and that results *"confirm the model's ability to deliver targeted thermal relief."* Registered as #90. |

---

## v3 — New flags #52–#94 (Results and Discussion, Conclusion, back matter)

> **First editorial pass over §3.1–§3.5 and §Conclusion.** Registered in document order. 43 flags: 27 POTENTIAL ROADBLOCK, 15 PENDING VERIFICATION, 1 ROADBLOCK (SEVERE).
>
> **Attestation:** this pass was **read-only**. No script was run, no seed was set, no number was regenerated. Where a finding turns on program behavior it is assigned to `math-auditor` or `code-stressor` with a named run. Two findings (#75, #74) rest on arithmetic performed by hand **on the manuscript's own printed values**; that arithmetic requires no execution, and both are labelled accordingly.

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

**#58 — §3.3.1 — ACO hyperparameters appear for the first time in Results and are never specified in Methods.** · PENDING VERIFICATION

- **Where:** *"The exploration parameter q0, set at 0.7, allocates 30% of decisions to random exploration… This is by design: a q0 closer to 1.0 would accelerate convergence but risk premature exploitation."*
- **Objection:** `q0` is introduced in Results with a post-hoc justification and is absent from Methods §2.4.1, which specifies only colony size and iteration count. Also never specified anywhere in the manuscript: the pheromone evaporation/decay rate, the local and global update rules, α and β (heuristic vs. pheromone exponents), τ₀ initialization, and the restart count. Since the implementation is a hand-written Ant Colony **System** (not the generic ACO of §2.4.1, and not scikit-opt per #45), the ACS-specific parameters are exactly what a reader needs to reproduce it. "This is by design" is a rationalization of a value the reader was never given.
- **Closes when:** `math-auditor` enumerates the production `AntColonySystemACO` parameter set; `editor` moves the complete set into a Methods table and deletes the Results-side justification.

**#59 — §3.3.1 — iteration-best and global-best traces are conflated, and the pheromone explanation has no diagnostic behind it.** · PENDING VERIFICATION

- **Where:** *"The best-per-iteration SECPI trace fluctuated between approximately 3.02 and 3.07 across the full run, with no clear monotonic convergence trend. The global best was reached early (within the first few iterations) and was never substantially improved upon."* And: *"indicating that the pheromone reinforcement mechanism did not fully drive the ant colony toward consensus on a single dominant solution."*
- **Objection:** (a) a best-so-far (global-best) trace is monotonically non-decreasing by construction — it cannot "fluctuate" and cannot lack a monotonic trend; either the trace plotted in Figure 11 is the per-iteration best (in which case "no monotonic trend" is expected and uninformative) or the axis is mislabelled. "Never substantially improved upon" is a hedge that hides which quantity is being described. (b) The best–average gap is attributed to pheromone dynamics with **no pheromone-concentration measurement, no solution-diversity or entropy statistic, and no comparison against a q0 sweep**. A mechanistic attribution to a named internal mechanism requires a diagnostic on that mechanism.
- **Closes when:** `editor` defines both traces precisely and matches them to Figure 11's actual series; `code-stressor` either supplies a diversity/pheromone-entropy diagnostic or the attribution is deleted and replaced with a descriptive statement.

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

## Resuming This Review — PLACEHOLDER

> 🔴 **This is where the v3 session was interrupted.** Everything that belongs below this line was intended but never written.
>
> **Unwritten: flags #75–#94** (20 flags — 14 POTENTIAL ROADBLOCK, 5 PENDING VERIFICATION, 1 ROADBLOCK (SEVERE), per the v3 preamble's own accounting). Scope: §3.5 Sensitivity Analysis, the Conclusion, Recommendations, and back matter. Named in forward references elsewhere in this file: **#75** (SEVERE — §3.5's category-level sensitivity means), **#79** (§3.5.3 "sourced from literature" as a false provenance claim, refining #30), **#90** (Conclusion "successfully developed and validated", extending #8), **#91 / #92** (Conclusion real-world planting prescription and "climate-vulnerable cities" transferability, extending #10/#11).
>
> **The four named forward references were spot-checked against the manuscript by the orchestrator (Entry 5); every quoted string is verbatim-accurate.** `manuscript/sections/07_conclusion.md:55` — *"successfully developed and validated"*; `:128` — *"across climate-vulnerable cities"*; `:81–86` — the Philippine-urban-planner prescription. For #75, `manuscript/sections/06_results_discussion.md:658–665` does report a **Species Morphology category mean SI of 1.3068** while the largest single SI anywhere in §3.5.1 is **0.4435** (Narra crown diameter) with all 39 remaining parameters below 0.005 — a mean cannot exceed its own maximum, so the reported category mean is arithmetically impossible as described. The same sentence also lists **"Species Allometry" twice**, at 0.1857 and 0.0727, where the following paragraph's discussion implies the second should be *Cooling Model*. **The findings are real; only their flag entries are missing.**
>
> **Resuming agent:** re-derive #75–#94 from `manuscript/sections/06_results_discussion.md` (§3.5, lines 597–725) and `manuscript/sections/07_conclusion.md`. Assign from **#75**. Do not renumber #52–#74. Confirm whether the re-derived set matches the 14/5/1 split above — if it does not, report the true split rather than forcing it to match.
