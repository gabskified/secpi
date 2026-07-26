# STATUS — SECPI

**Generated:** 2026-07-26 by `interpreter` (third run today; supersedes the run that predated Project Log Entry 7)
**Derived from:** `docs/DECISIONS.md`, `docs/PROJECT_LOG.md` Entry 7 + same-session ADDENDUM, `docs/STATE.md` (authoritative count block, Entry 7-synced), `docs/FLAGS.md` (v4, #1–#95)
**Count check — derived, not copied.** Enumerating every `**#N —` heading in `FLAGS.md`: #52–#95 split **28 potential roadblock / 15 pending / 1 SEVERE = 44**; the #1–#51 per-flag record contributes **29 cleared / 2 deferred / 15 pending / 5 potential roadblock**. Totals: **29 cleared · 2 deferred · 30 pending · 33 potential roadblock · 1 SEVERE = 95.** This agrees with the stated totals in `FLAGS.md`, `STATE.md` and Entry 6. **No discrepancy this run.** Next free flag: **#96**.

> This file is **derived**. If it disagrees with `FLAGS.md`, `DECISIONS.md` or `PROJECT_LOG.md`, those win — regenerate rather than reconcile.

---

## 1. Headline

The decision queue moved for the first time since D-09: **D-02, D-03, D-07 and D-11 all closed on 2026-07-26**, which means every decision on the Results-regeneration critical path is now settled and that path is **no longer decision-blocked**. The binding constraint has shifted from the research lead to the register: the regeneration cannot start until **#75** (Methods names Morris, §3.5.1 executes a local two-level OAT) and **#77** (`n_runs` 3 vs 5) settle, and the project's only SEVERE flag, **#82**, is untouched by any of these decisions — D-11 set its remedy, it did not apply it. Next action (recommendation, not instruction): let the in-flight `math-auditor` #75 routing land, settle #77 in the same pass, then run once.

---

## 2. Preprint readiness

Gates re-derived this run from the register and the current decision queue. Nothing carried forward from the previous STATUS.md.

| Must be true before an EarthArXiv DOI is minted | True yet? | Blocked by |
|---|---|---|
| No ROADBLOCK (SEVERE) outstanding | 🔴 No | **#82** — remedy decided (D-11 option b), **not applied**. Regeneration only |
| §3.5 regenerated under Option B (sweep + aggregation) | 🔴 No | **#75** (method mismatch, `math-auditor` in flight) and **#77** (restart count) must settle first |
| Results numbers regenerated under Option B | 🔴 No | ✅ no longer decision-blocked. Blocked on #75/#77, then execution |
| Ceiling 3.75 confirmed against the optimizer, not random sampling | 🔴 No | D-02's **standing re-check** — 3.75 sits just above 3.52 (max of 500 *random* placements). `code-stressor` reports optimizer best raw SECPI post-regeneration |
| Every "significant" claim has a test behind it | 🔴 No | Design decided (H1/H2, Wilcoxon n=30, Holm–Bonferroni m=2). Unexecuted. **#70's manuscript-wide sweep is not discharged by D-03** |
| Cooling figures carry a defensible unit | 🔴 No | #62 — °C on a dimensionless 0–1 index, no calibration anywhere; #63, #90 inherit |
| Headline diversity claim matches the data | 🔴 No | #46, #91 — data show palette convergence, not "diversity is negligible". D-06 sub-decision open |
| Conclusion claims stay inside the study's scope | 🔴 No | #87, #88, #91, #92, #93 |
| Author contributions complete and mappable | 🔴 No | **#94** — five entries, six named authors. Only the author team can fix |
| Funding / COI / data / code-availability statements exist | 🔴 No | #95 — none present anywhere |
| Title locked (DOI landing page is permanent) | ⬜ No | **D-04 — the only DOI-blocking open decision** |

---

## 3. Decisions awaiting the research lead

**Four open**, down from seven. D-02, D-03, D-07 and D-11 are all **DECIDED 2026-07-26** (Entry 7 + addendum); D-11 was opened and closed the same day.

| ID | What | Blocks | Effort | Critical path? |
|---|---|---|---|---|
| **D-04** | Final title — current vs. Flag #10 revision | **DOI minting.** Landing-page title is effectively permanent | One of two | **Yes — the only DOI-blocking item** |
| D-05 | "Chebyshev space (ℤ²)" — lattice convention or error | Nothing structural; §2.2.1 prose only | Keep/delete | No |
| D-08 | Re-anchor assumed heights, or disclose extrapolation | Crown geometry → every cooling number (#48, #30) | One of two, real cost either way | No, but propagates widely |
| D-10 | Fix `p0 = 1.0`, let γ absorb calibration | CA generation code (`grid.py`) | Yes/no, recommendation on file | No |

**D-05 cannot be answered by any agent** — it turns on authorial intent. Do not route it.

**Plus D-06's three residual sub-decisions** (D-06 itself is resolved as outcome (b)): confirm §3.1 regenerates under Option B; confirm the Flag #46 diversity-claim reframing; decide whether `species_actually_used` becomes a reported variable. The second changes what the paper argues and should not be treated as clerical.

### Consequences of the four closures that are easy to lose

- **D-07 does not close #64 or #44.** §3.4.1's per-`k` means (2.990–3.017) are arithmetically incompatible with the same dataset's individual values regardless of the symbol used — the stated k=1 mean sits **below 3.0396**, the lowest k=1 value the manuscript itself prints. §3.4.1 must be **regenerated, not rewritten**. #44 additionally covers two incommensurable experiments interleaved in one narrative.
- **D-03 does not discharge #70.** Every "significant/significantly" not backed by H1/H2 must still be removed manuscript-wide.
- **Sequencing (D-03 condition 2):** `editor` writes H1 and H2 into Methods §2.5.2 **before** `code-stressor` executes. Running first voids the pre-specification and forfeits the whole point of the design.
- **D-02 carries a standing obligation, not a closed question.** The ceiling is provisional against the optimizer.

---

## 4. Key flags — grouped by root cause

### 🔴 ROADBLOCK (SEVERE) — #82. §3.5.2's four category means are impossible as printed.

Every reported category-level mean sensitivity index exceeds the maximum SI of its own member set. The argument is **`mean ≤ max`**.

| Category | n | Largest member (manuscript-printed) | Reported mean |
|---|---|---|---|
| Species Morphology | 12 | 0.4435 (Narra CD) | **1.3068** |
| Species Allometry | 24 | < 0.005 | **0.1857** |
| Cooling Model *(duplicate-labelled)* | 3 | 0.0032 (CCA threshold) | **0.0727** |
| Weighting | **1** | 0.0017 (shade_weight) | **0.0236** |

**The Weighting row refutes it in one line:** the category has exactly one member by §3.5.1's own definition, and §3.5.2 prints that member's SI as 0.0017 thirteen lines below giving the category a mean of 0.0236. A one-element mean *is* that element.

**Status: verified** by hand arithmetic on manuscript-printed values (Entry 6 §B, Flag #82). No execution required. **§3.5.1's parameter-level layer reproduces cleanly** (1.356 / 3.0576 = 0.4435 ✓), so the defect localizes to the aggregation step and Figure 34 — which is why `math-auditor` should still report what `SensitivityAnalyzer` actually computes even though the numbers are being replaced: if the defect is in code, regeneration alone reproduces it.

**Do not use these arguments** (both refuted, both previously in circulation): the `[0,1]` bound — SI is a difference-to-baseline ratio and is not bounded above by 1; and the "these values are sums" reading — Weighting's sum is 0.0017, Cooling Model's is 0.0068. **"Relabel sum-vs-mean" is not an available remedy**; D-11 explicitly excludes it.

### Cluster A — §3.5 is not the analysis Methods describes, and it is the gate on everything (#75, #77; with #76, #79, #80, #81)

**#75 is the immediate next action and is in flight to `math-auditor`.** Methods §2.5.3 names the **Morris method** — a global design with randomized trajectories and μ\*/σ statistics — while §3.5.1 executes a **local two-level OAT from a single baseline**. Regenerating before this resolves reproduces the mismatch in fresh numbers and wastes the run. **#77** must be fixed in the same pass: the sweep averaged over **three** ACO runs against the project standard `n_runs = 5`, and no dispersion is reported for any of the 40 indices. **Leverage: these two are the smallest items on the board and they gate the largest — D-11's regeneration, and through it #82, #89, Figure 34, and the salvageability of #78/#79/#86.** That is why they outrank everything else this week despite neither being SEVERE.

### Cluster B — one unmeasured quantity: the ACO's run-to-run noise floor (#65, #68, #78; supplies the denominator for #77, #67)

The manuscript never measures restart-to-restart SD, so the same magnitude is treated as noise where that helps and as a causal effect where that helps. §3.4.2 dismisses 0.0014 as stochastic; §3.4.3 attributes causation to 0.0669 and 0.094; §3.5.1 ranks effects of 0.009–0.014 and calls them "not negligible" — all against §3.3.1's own best-vs-average gap of **0.05–0.07**. **Leverage: one noise-floor measurement across the production restart set resolves or hardens three flags and supplies the missing denominator for two more.** It rides on the same regeneration run and depends on no open decision.

### Cluster C — the allometric chain may be off the canonical path (#85; with #84, #30, #48, D-08)

D-09 makes hardcoded LAI canonical and the allometric chain sensitivity-only. If l0/l1/h0/h1 do not reach the objective, near-zero sensitivity is what a **disconnected** parameter produces — and §3.5.3 reads it as demonstrated robustness, describing #30's confirmed defect (all six species yield h < h₀; DBH 0.17–0.66 m; LAI 50–420× off) as "sufficient buffering." §3.5.3 separately claims the constants were "sourced from literature," which D-09 and Entry 3 explicitly contradict (#84). **Leverage: one call-path trace from `math-auditor` settles #85, gives #30 a second confirmation route, and determines whether §3.5.3's robustness conclusion is overstated or vacuous.** Cheap, independent of the regeneration, runnable in parallel.

### Cluster D — claimed validation that was never performed (#87, #88, #69, #70, #39)

The Conclusion says the framework was "successfully developed and validated." Of §2.5's four validation stages: the greedy benchmark is absent from §3 entirely; morphological robustness has no reported result and its own pass criterion ("outperform random placements") has no baseline anywhere; the diversity stage is the subject of #64/#65/#46; the cross-scenario stage is circular by construction (#69) and its "significantly" carries no test (#70). D-03 now supplies a test design for the last of these — **the other three remain unaddressed by any decision.** #88 adds that the Conclusion reports a morphological-robustness result absent from §3, says "six distinct land-use patterns" where Methods gives three, and attributes cooling to building shading, a mechanism §2.3 states is not modelled.

### Cluster E — mechanism claims refuted by the paper's own tables (#83, #73, #88d)

§3.5.2 explains the weighting ratio's insensitivity by asserting Narra and Akleng-parang "rank highest on both CPA and LAI." **Table 3 shows Akleng-parang has the lowest LAI of the six**; Narra is third. The same table refutes the closing claim that the pool lacks a CPA–LAI trade-off. The likelier explanation — that the 0.30 LAI term does little work in the objective — compounds #54 and bears on #85.

### Cluster F — carried forward, unchanged in substance

Unit manufacture (#62, #63, #90); internal inconsistency about what was run (#52, #57, #60, #61); real-world claims from a synthetic study (#86, #91, #92, #93); mis-stated headline (#46, #54, #65).

### What moved since the last STATUS.md

**No flag was created, closed or reclassified** by the four decisions. Entry 7 states this explicitly. #39, #69 and #70 now have a decided test design behind them but remain open pending execution; #64 and #44 are recorded as expressly *not* closed by D-07.

---

## 5. Triage buckets

Re-derived this run.

**A — blocks the preprint.** #82 (SEVERE). **#75 and #77**, promoted into A this run — they are not severe in themselves but they are the gate on #82's remedy. Cluster B's noise floor (#65, #68, #78), because the paper is currently self-contradicting on its own headline numbers. Cluster D's validation claims (#87, #88). #62's °C. #46/#91's inverted diversity claim. #94 author contributions. #95's missing code-availability statement, for a study whose entire evidentiary basis is one script. D-04's title lock.

**B — fix before journal submission, not necessarily before the DOI.** #76, #79, #80, #81. Cluster C (#85, #84, #30, #48). Cluster F's internal inconsistencies (#52, #57, #60, #61, #63). #83. #92, #93. The six confirmed Methods corrections (`CLAUDE.md` §7). #66's submodularity demonstration. #89 (falls out of the §3.5 regeneration automatically).

**C — disclose or defer.** #45 software-stack misattribution. #49, #50 author-construct disclosures. #9's land-use band grounding (V is the priority disclosure). Citation-form errors (#20 "PTM-2", #21, #22). #51 subsection renumbering. #90's "100 x 100 m²" dimensional slip (applyable immediately). #71's plantability clarification.

---

## 6. Integrity warnings

- **The previous STATUS.md was materially wrong and has been overwritten.** It stated *"No D-11 exists"* — D-11 was **opened and decided** on 2026-07-26. It listed **seven** open decisions; there are **four**. It treated D-02, D-03 and D-07 as open; all three are decided. Anyone holding a copy of that version should discard it.
- **D-03's multiplicity correction was amended within the same session.** Entry 7's body records plain Bonferroni (α = 0.025 per test) and says it "stands as decided unless the lead says otherwise"; the ADDENDUM records the lead saying otherwise. **The binding version is Holm–Bonferroni, m = 2, FWER = 0.05**, with the step-down gate written out in `DECISIONS.md`. Do not implement from Entry 7's body alone.
- **Known-wrong, not yet fixed.** All Results numbers in the manuscript remain obsolete under Option B (`CLAUDE.md` §4) — including the Abstract's 3.02–4.39, 28%, 0.03% and 0.809 °C. Nothing has been regenerated. `CLAUDE.md` §4 also still says the regeneration awaits "the two open normalization/statistics decisions"; both are now closed, so that sentence is stale (orchestrator's to fix, not mine).
- **`CLAUDE.md` §2 rule 4 and §5 are stale on flag numbering** — they state "#1–#41 assigned; next free number is #42" and describe `FLAGS.md` as "the 41-flag editorial register (v2)". The register is complete through **#95**; next free is **#96**.
- **D-02's ceiling is provisional.** 3.75 is confirmed as a decision but not as a value: it was set against a max from 500 *random* placements, and the ACO optimizes harder than random. Treat any normalized SECPI produced before the re-check as unconfirmed.
- **Five flags were repaired in place, not reclassified** (#53, #59, #64, #68, #70). When quoting: #53's "Akleng-parang outranks Narra under midpoints" is withdrawn; #64's decisive check is manuscript-internal (2.990 < 3.0396) while its 3.514 six-value mean is mixed-source; #68 should be quoted at **0.094**, not 0.0396, unless the D-06 CSV provenance is cited alongside; #70's self-validation claim is a **hypothesis pending `math-auditor`**, not a finding.
- **Never inspected:** `manuscript/sections/08_references_appendices.md` — the reference list beyond spot-checks, and Appendices A–B including Figures A1–A28. #81 shows the unreferenced-figure problem is document-wide. Assign from #96.
- **Unrouted terminology conflict** (Entry 6 §E, still unflagged): §2.2 and §3.4.4 define **P as "Prohibited"**; `CLAUDE.md` §3 lists **P as "public."** This may be a `CLAUDE.md` error rather than a manuscript one. Orchestrator's; no agent has taken it.
- **D-06 retains an open sub-question** — which script generated `run_20260213_222844` is still unidentified. A provenance question, not an existence question; not counted among the four open `D-xx`.
- **Every execution obligation created by Entries 6 and 7 is undischarged.** No code has been run against any v4 flag, against D-02's ceiling re-check, or against D-03's two tests. Entry 7 and its addendum both attest that no code was executed.

---

## 7. What changed since last run

Previous run: 2026-07-26, generated **before** Project Log Entry 7. Register unchanged at 95 flags; the decision queue is what moved.

- **Four decisions closed: D-02, D-03, D-07, D-11.** D-11 was opened and closed the same day. Open decisions **7 → 4** (D-04, D-05, D-08, D-10).
- **The critical path changed owner.** Last run's headline recommendation was "close D-02, D-03 and D-07." All three are closed, plus D-11. The Results-regeneration path is **no longer decision-blocked**; it is blocked on **#75 and #77**, then execution.
- **#75 and #77 promoted from bucket B to bucket A.** They were previously filed as "which sensitivity design was actually run" routing questions. They are now the explicit prerequisites D-11 names, so they gate the SEVERE flag's remedy.
- **The false "no D-11 exists" statement is removed**, along with the seven-decision table and the treatment of D-02/D-03/D-07 as open.
- **Cluster A is now the §3.5 method mismatch** (#75/#77-led), and the noise-floor cluster moves to B. Last run had these in the reverse order; the regeneration prerequisite now outranks the measurement it enables.
- **Three new "not closed by the decision" carve-outs recorded** in §3: #64/#44 survive D-07, #70's sweep survives D-03, and D-02's ceiling carries a standing re-check.
- **D-03's Bonferroni → Holm–Bonferroni amendment** is now on record here as an integrity warning, because Entry 7's body and its addendum disagree and only the addendum binds.
- **Two stale-document notes added** against `CLAUDE.md` (§4's "two open decisions", §2/§5's #42 numbering). Neither is mine to fix.
