SECPI Manuscript — Comprehensive Editorial Flag Archive (v2 — Updated)

**Sections reviewed:** Title, Abstract, Introduction, Methods (§2.1–§2.6)
**Update source:** Cross-referenced against SECPI Project Log Entries 1–3 (Mathematical Auditor sessions, code-execution-verified against `AuditedCode_1.py`)
**Session pause point (unchanged from v1):** end of Methods, prior to Results and Discussion. Sections pending: Results and Discussion, Conclusion.

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

| Category | Count (v1) | Count (v2) | Change |
|---|---|---|---|
| RESOLVED — Cleared Up | 17 | **25** | +8 |
| RESOLVED — Deferred | 2 | 2 | — |
| PENDING VERIFICATION | 19 | **14** | −5 |
| POTENTIAL ROADBLOCK | 3 | **0** | −3 |
| ROADBLOCK (SEVERE) | 0 | 0 | — |
| **TOTAL FLAGS IDENTIFIED** | 41 | 41 | — |

**What moved and why:** all 3 POTENTIAL ROADBLOCK flags (#25, #28, #33) closed via direct code execution against `AuditedCode_1.py`. 5 PENDING VERIFICATION flags (#31, #34, #35, #38, #41) closed the same way. No flag escalated in severity. Full detail below.

---

## Full Flag Register (All 41 Flags, by Classification)

### RESOLVED — Cleared Up (25 flags)

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

### PENDING VERIFICATION (14 flags)

*Flags #13, #14, #19, #21, #22, #29, #36 are unchanged from v1 — no update this session, not reproduced here.*

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

### POTENTIAL ROADBLOCK (0 flags)

*All 3 flags previously in this category (#25, #28, #33) have moved to RESOLVED — Cleared Up this update — see above. No flags currently classified at this severity.*

---

### ROADBLOCK (SEVERE) (0 flags)

None currently confirmed at this stage of review — unchanged.

---

## New item surfaced by code audit (not part of the original 41-flag count — recommend numbering as Flag #42 when the Editor next updates this archive)

**V-zone "30-meter Chebyshev buffer" description (§2.2.1) is factually incompatible with the code and, independently, appears geometrically incompatible with the manuscript's own 5–10% Vulnerable-area target on this grid size.** The coarse grid is confirmed 10 m/cell (10×10 = 100 cells total); a 30 m Chebyshev buffer is a 7×7 = 49-cell square — a single such buffer already covers 49% of the entire grid, far exceeding the stated 5–10% target before any overlap is considered. The current code does not implement a Chebyshev buffer at all — it uses target-count-driven BFS growth from seed points, which reliably and deterministically hits the 5–10% target (produces exactly 8% coverage, zero run-to-run variance) but does not correspond to the literal procedure described in §2.2.1. **This is an Editor task**: rewrite §2.2.1 to describe the actual BFS method, not a code task — the geometric incompatibility means the originally-described procedure likely cannot be made to work as literally written on this grid size regardless of implementation. Source: Project Log Entry 1 §3.1, Entry 2 handoff note 6.

---

## Resuming This Review

- Send Results and Discussion / Conclusion pages when ready; flag numbering continues from #42 (recommend #42 be assigned to the V-zone buffer item above when this archive is next formally updated by the Editor).
- **Highest-priority open items now**: Flag #5 (normalization ceiling confirmation) and Flag #39 (statistical test outcome-metric confirmation) — both are one-decision-away from being fully actionable, and both block final Results numbers from being reported with confidence.
- Flags #9, #20, #26, #30 all currently sit with the Deriver chat awaiting literature sourcing — no code-side work remains on any of them.
- If any PENDING VERIFICATION item is confirmed, resolved, or escalates, flag it explicitly so this archive can be updated again — same convention as v1.
