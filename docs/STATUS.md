# STATUS — SECPI

**Generated:** 2026-07-26 by `interpreter` (regenerated from scratch; supersedes the 2026-07-26 initial run)
**Derived from:** `docs/FLAGS.md` (v4, complete #1–#95), `docs/STATE.md` (authoritative count block), `docs/DECISIONS.md`, `docs/PROJECT_LOG.md` Entry 6
**Count check:** per-flag enumeration gives **29 cleared · 2 deferred · 30 pending · 33 potential roadblock · 1 SEVERE = 95**. This agrees with the stated totals in `FLAGS.md`, `STATE.md` and Entry 6. No discrepancy this run. Next free flag: **#96**.

> This file is **derived**. If it disagrees with `FLAGS.md` or `DECISIONS.md`, those win.

---

## 1. Headline

The editorial register is now complete through the whole manuscript, and completing it produced the project's **first ROADBLOCK (SEVERE): Flag #82** — §3.5.2's four category-level mean sensitivity indices each exceed the maximum SI of their own member set, a desk-reject-class defect proved by hand arithmetic on the manuscript's own printed values. The preprint cannot be minted with §3.5.2 as written, and #82 is not editable — the aggregation must be regenerated, which puts it behind the same Option-B regeneration that D-02/D-03/D-07 already gate. **Next action (recommendation, not instruction): close D-02, D-03 and D-07 so one regeneration run can serve Results and §3.5 together, and in parallel send `math-auditor` the #85 allometric call-path trace, which is the cheapest high-leverage check on the board.**

---

## 2. Preprint readiness

Gates derived this run from the flag register and the open decision queue.

| Must be true before an EarthArXiv DOI is minted | True yet? | Blocked by |
|---|---|---|
| No ROADBLOCK (SEVERE) outstanding | 🔴 No | **#82** — regeneration only; no wording fixes it |
| Every manuscript section has had an editorial pass | ✅ Yes | — (`08_references_appendices.md` still unpassed, but it is back matter, not manuscript body) |
| Results numbers regenerated under Option B | 🔴 No | D-02, D-03, D-07 |
| §3.5 sensitivity analysis regenerated | 🔴 No | #82, plus the unanswered "which design was run" questions #75, #76, #77, #79 |
| Every "significant" claim has a test behind it | 🔴 No | #39, #69, #70, #87; D-03 open |
| Cooling figures carry a defensible unit | 🔴 No | #62 — °C attached to a dimensionless index with no calibration anywhere; `math-auditor` has not yet confirmed whether any calibration exists |
| Headline diversity claim matches the data | 🔴 No | #46, #91 — the data show palette convergence, not "diversity is negligible" |
| Conclusion claims stay inside the study's scope | 🔴 No | #87, #88, #91, #92, #93 |
| Author contributions complete and mappable | 🔴 No | **#94** — five contributor entries against six named authors; only the author team can fix |
| Funding / COI / data / code-availability statements exist | 🔴 No | #95 — none present anywhere in the manuscript |
| Title locked (DOI landing page is permanent) | ⬜ No | D-04 |

---

## 3. Decisions awaiting the research lead

Seven `D-xx` are open. Nothing below has been decided by any agent.

| ID | What | Blocks | Effort |
|---|---|---|---|
| **D-02** | Normalization ceiling (3.75 proposed) + framing | Writing any Results number; also gates the §3.5 regeneration #82 needs | Pick a number |
| **D-03** | Wilcoxon outcome metric — cooling-in-V **or** trees-near-V | The entire significance claim (#39, #69, #70, #87) | One of two |
| **D-07** | `k` notation — three-way collision | Results prose coherence; #64 cannot be regenerated coherently before it closes | Pick symbols |
| D-08 | Re-anchor assumed heights, or disclose extrapolation | Crown geometry → all cooling numbers (#48) | One of two |
| D-10 | Fix `p0 = 1.0`, absorb into γ | CA generation code | Yes/no, recommendation on file |
| D-04 | Final title | DOI minting (permanent) | One of two |
| D-05 | "Chebyshev space (ℤ²)" keep/delete | Nothing structural | Keep/delete |

**Critical path: D-02 + D-03 + D-07.** All three gate the Option-B regeneration, and #82's fix rides on that same run. Settling them first means regenerating once rather than twice.

### Not decisions — routing recommendations only

No `D-xx` has been opened for any of these. They are recorded here because they need the research lead and nobody else can supply the answer.

- **#94 — author contributions.** Five statements, six authors; three V-surnames with no initial key. Needs a session with the author team. Submission-blocking for the preprint, not just the journal.
- **#75 / #77 — which sensitivity design was actually run?** Methods names the Morris method; §3.5.1 describes a local two-level OAT from a single baseline. §3.5.1 says three ACO restarts; the implementation of record uses five. Both gate whether §3.5.1 is salvageable or must be regenerated wholesale.
- **#82 — regeneration scope for §3.5.** If a `D-11` is ever opened for this, **"relabel sum-vs-mean" must not be one of its options.** That remedy is arithmetically dead (see §4). No D-11 exists.

---

## 4. Key flags — grouped by root cause

### 🔴 ROADBLOCK (SEVERE) — #82. §3.5.2's category means are impossible as printed.

All **four** reported category-level mean sensitivity indices exceed the maximum SI of their own member set. The argument is **`mean ≤ max`** and it needs no assumptions.

| Category | n | Largest member (manuscript-printed) | Reported mean |
|---|---|---|---|
| Species Morphology | 12 | 0.4435 (Narra CD) | **1.3068** |
| Species Allometry | 24 | < 0.005 | **0.1857** |
| Cooling Model *(duplicate-labelled)* | 3 | 0.0032 (CCA threshold) | **0.0727** |
| Weighting | **1** | 0.0017 (shade_weight) | **0.0236** |

**The Weighting row refutes it in one line, with no bounding step:** the category has exactly one member by §3.5.1's own definition, and §3.5.2 prints that member's SI as 0.0017 thirteen lines below giving the category a mean of 0.0236. A one-element mean *is* that element.

**Two arguments that must not be used** — both were carried in the previous STATUS.md and both are wrong:
- **SI is not bounded to [0,1].** It is `|SECPI_high − SECPI_low| / SECPI_baseline`, a difference-to-baseline ratio that would legitimately exceed 1 if an effect exceeded baseline SECPI. Arguing from a bound hands the authors a valid rebuttal to a correct objection.
- **The values are not sums.** Weighting's sum equals its mean equals 0.0017 against a reported 0.0236; Cooling Model's sum is 0.0068 against 0.0727; Morphology's sum is at most 0.4938 against 1.3068. The overstatement factors (2.95 / 50.2 / 22.7 / 13.9) share no common factor, so no single mis-scaling explains them either.

**Status: verified**, by hand arithmetic on manuscript-printed values in Project Log Entry 6 §B. No execution required, nothing pending. **Mitigating diagnosis:** §3.5.1's parameter-level layer reproduces cleanly (1.356 / 3.0576 = 0.4435 ✓), so the defect localizes to the aggregation step and Figure 34 — which points at `SensitivityAnalyzer`, not at four transcription slips. §3.5.1 may survive; §3.5.2 will not. No number from §3.5.2 may be quoted anywhere, including the Conclusion's "SI = 0.46" (#89).

### Cluster A — one unmeasured quantity: the ACO's run-to-run noise floor (#65, #68, #77, #78; feeds #67, #89)

The manuscript never measures restart-to-restart SD, so it treats the same magnitude as noise where that helps and as a causal effect where that helps. §3.4.2 dismisses 0.0014 as stochastic; §3.4.3 attributes causation to 0.0669 and 0.094; §3.5.1 ranks effects of 0.009–0.014 and calls them "not negligible" — all against §3.3.1's own reported best-vs-average gap of 0.05–0.07. **Leverage: one noise-floor measurement across the production restart set resolves or hardens four flags and supplies the missing denominator for two more.** It is the single highest-yield execution item after #82's regeneration, and it does not depend on any open decision.

### Cluster B — §3.5.1 is not the analysis Methods describes (#75, #76, #79, #80)

Methods §2.5.3 names the Morris method; §3.5.1 executes a local two-level OAT from a single baseline — no trajectories, no elementary effects, no μ*/σ — which is weaker in exactly the dimension that matters, since the paper elsewhere asserts the objective is non-submodular and interaction-dominated (#75). The baseline SECPI 3.0576 matches no configuration reported anywhere and its parameter vector, experiment, arm, grid and seed are unstated, yet all 40 indices are ratios to it (#76). Morphology was swept over full trait ranges while allometrics got ±15%, a 3.19× wider relative span for the dominant parameter, so the ranking is not like-for-like (#79) — **stated fairly, crown diameter's dominance survives directionally; the magnitude and the "nearly two orders of magnitude" framing do not.** The one cross-reference offered in support points at §3.2, an empty subsection (#80).

### Cluster C — the allometric chain may be off the canonical path (#85; with #84, #30, #48)

D-09 makes hardcoded LAI canonical and the allometric chain sensitivity-only. If l0/l1/h0/h1 do not reach the objective, near-zero sensitivity is what a *disconnected* parameter produces — and §3.5.3 reads it as demonstrated robustness, describing #30's confirmed defect (all six species yield h < h₀; DBH 0.17–0.66 m; LAI 50–420× off) as "sufficient buffering." Separately §3.5.3 claims the constants were "sourced from literature," which D-09 and Entry 3 explicitly contradict (#84). **Leverage: a single call-path trace from `math-auditor` settles #85, gives #30 a second confirmation route, and determines whether §3.5.3's robustness conclusion is merely overstated or entirely vacuous.** Highest-value unexecuted check in the v4 batch, and cheap.

### Cluster D — claimed validation that was never performed (#87, #88, #69, #70, #39)

The Conclusion says the framework was "successfully developed and validated." Methods §2.5 specifies four validation stages: the greedy benchmark is absent from §3 entirely; the morphological-robustness stage has no reported result and its own pass criterion ("outperform random placements") has no random-placement baseline anywhere; the diversity stage's results are the subject of #64/#65/#46; the cross-scenario stage is circular by construction (#69) and its "significantly" carries no test (#70). The Conclusion additionally reports a morphological-robustness result **absent from §3**, says "six distinct land-use patterns" where Methods gives **three**, names an undefined preset ("Dense Organic," one occurrence in the whole manuscript), and attributes cooling to building shading — a mechanism §2.3 states is not modelled (#88).

### Cluster E — mechanism claims refuted by the paper's own tables (#83, #73, #88d)

§3.5.2 explains the weighting ratio's insensitivity by asserting Narra and Akleng-parang "rank highest on both CPA and LAI." **Table 3 shows Akleng-parang has the lowest LAI of the six** under both midpoint and maximum conventions; Narra is third. The same table refutes the paragraph's closing claim that the pool lacks a CPA–LAI trade-off — Kabiki is highest-LAI with a 10–12 m crown; Akleng-parang is second-largest CPA with the lowest LAI. The offered mechanism is unavailable, and the likelier explanation (the 0.30 LAI term does little work in the objective) compounds #54 and bears on #85.

### Cluster F — carried forward, unchanged in substance

- **Unit manufacture** (#62, #63, #90): a dimensionless 0–1 index reported in °C with no calibration; the Abstract's 0.809 °C exists only because of it, and the 42% equity cost recomputes to 31% on the manuscript's other printed mean.
- **Internal inconsistency about what was run** (#52, #57, #60, #61): crown diameters, ACO configuration (11× difference in function evaluations), best-solution composition (three different fifth species), and untraceable coordinates.
- **Real-world claims from a synthetic study** (#86, #91, #92, #93): now four instances across Results, Conclusion and Recommendations. #93 is the useful one — the Recommendations are *correct* and the Conclusion is what must move.
- **Mis-stated headline** (#46, #54, #65): the defensible claim is that a larger palette converges to the same small high-performing set.

---

## 5. Triage buckets

Re-derived this run.

**A — blocks the preprint.** #82 (SEVERE, regeneration). Cluster A's noise floor, because #65/#68/#78 currently make the paper self-contradicting on its own headline numbers. Cluster D's validation claims (#87, #88) — "validated" with no satisfied criterion is a desk-check failure. #62's °C. #46/#91's inverted diversity claim. #94 author contributions. #95's missing code-availability statement, for a study whose entire evidentiary basis is one script.

**B — fix before journal submission, not necessarily before the DOI.** Cluster B (#75, #76, #79, #80) if the research lead accepts §3.5 being scoped down or disclosed rather than fully regenerated. Cluster C (#85, #84, #30, #48). Cluster F's internal inconsistencies (#52, #57, #60, #61, #63). #83. #92, #93. The six confirmed Methods corrections (`CLAUDE.md` §7). #81's figure-citation audit. #66's submodularity demonstration.

**C — disclose or defer.** #45 software-stack misattribution. #49, #50 author-construct disclosures. #9's land-use band grounding (V is the priority disclosure). Citation-form errors (#20 "PTM-2", #21, #22). #51 subsection renumbering. #90's "100 x 100 m²" dimensional slip (applyable immediately). #71's plantability clarification.

---

## 6. Integrity warnings

- **The previous STATUS.md carried a refuted argument for the SEVERE flag.** It argued #82 from a `[0,1]` bound on SI and described the reported values as behaving like "a sum." Both are wrong (see §4), and the "relabel sum-vs-mean" remedy it proposed as a candidate D-11 would replace one wrong number with another. Corrected in this regeneration. `docs/HANDOVER.md` §A1 was corrected in place on 2026-07-26 and no longer carries the error.
- **The SEVERE flag is #82, not #75.** Older documents forward-reference it as #75. Also moved from their predicted numbers: §3.5.3 false provenance is **#84** (not #79); the Conclusion "validated" claim is **#87** (not #90). #75 is the Morris-vs-local-OAT contradiction. #91/#92 kept their predicted numbers by coincidence of content, not by deference.
- **The #74 truncation is discharged.** `FLAGS.md` is complete through #95, the `PLACEHOLDER` stub and truncation notice are gone, and no flag forward-references an entry that does not exist below it.
- **Five flags were repaired in place, not reclassified** (#53, #59, #64, #68, #70), as marked `v4 CORRECTION` blocks with original text preserved. Three consequences for anyone quoting them: #53's "Akleng-parang outranks Narra under midpoints" is withdrawn (not reproducible); #64's arithmetic is manuscript-internal only via the 2.990-below-3.0396 check — the 3.514 six-value mean is mixed-source; #68 should be quoted at **0.094**, not 0.0396, unless the D-06 CSV provenance is cited alongside. #70's self-validation claim is now a hypothesis pending `math-auditor`, not a finding.
- **Known-wrong, not yet fixed.** All Results numbers in the manuscript remain obsolete under Option B (`CLAUDE.md` §4) — including the Abstract's 3.02–4.39, 28%, 0.03% and 0.809 °C. Nothing has been regenerated.
- **Never inspected:** `manuscript/sections/08_references_appendices.md` — the reference list beyond spot-checks, and Appendices A–B including Figures A1–A28. #81 shows the unreferenced-figure problem is document-wide, which makes the appendix figures a live concern. Assign from #96.
- **Unrouted terminology conflict, raised in Entry 6 §E and not flagged:** §2.2 and §3.4.4 define **P as "Prohibited"**; `CLAUDE.md` §3 lists **P as "public."** This may be a `CLAUDE.md` error rather than a manuscript one. It belongs to the orchestrator; no agent has taken it.
- **D-06 is resolved as outcome (b) but retains an open sub-question** — which script generated `run_20260213_222844` is still unidentified. It is a provenance question, not an existence question, and it is not counted among the seven open `D-xx`.
- **Every execution obligation created by Entry 6 is undischarged.** No code has been run against any v4 flag.

---

## 7. What changed since last run

Previous run: 2026-07-26 (initial), derived from a `FLAGS.md` truncated at #74.

- **Register: 74 → 95 flags.** v4 added #75–#95 covering §3.5 Sensitivity Analysis and the Conclusion/Recommendations/back matter: 15 potential roadblock, 5 pending verification, 1 SEVERE.
- **Potential roadblocks: 18 → 33. Pending verification: 25 → 30. SEVERE: 0 → 1.** Cleared (29) and deferred (2) unchanged. No flag was downgraded or closed.
- **The project's first ROADBLOCK (SEVERE) now exists and is registered on evidence** (#82). The previous STATUS.md correctly refused to report a severe flag on the strength of a forward reference; that caution is now discharged.
- **The previous run's §4 SEVERE argument is retracted** — the `[0,1]` bound and the "sum" diagnosis are both wrong. Replaced with `mean ≤ max` and the one-line Weighting refutation.
- **The proposed "D-11 — relabel sum-vs-mean, or re-run" is withdrawn.** Relabelling is arithmetically dead; no D-11 has been opened, and any future one must be scoped to regeneration only.
- **Cluster A regrouped.** The previous run grouped #64/#65/#67/#68 as one variance problem. #64 is an arithmetic incompatibility, not a variance question, and belongs with the #44/D-07 `k` collision; #77 and #78 join the variance cluster from §3.5. The noise-floor measurement's leverage is unchanged and now spans two sections.
- **Three new clusters appear** that had no representation last run: §3.5.1's design mismatch (B), the allometric off-path hypothesis (C), and the never-performed validation protocol (D).
- **Two new submission-blocking non-scientific items:** #94 (author contributions) and #95 (missing funding/COI/data/code-availability statements). Neither was visible before the Conclusion pass.
- **Integrity items closed:** the #74 truncation, the "formal SEVERE count is 0" caution, and #64's attestation defect. `STATE.md`'s summing error (51 vs 52) is resolved in favour of the per-flag record.
