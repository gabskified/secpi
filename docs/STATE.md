# STATE.md — Live Ownership Board

Last synchronized with: Project Log Entry 3 / Flag Archive v2.
Update this file at the end of every session. It answers one question: *what is the next person supposed to do?*

---

## Flag register at a glance

| Category | v1 | v2 | Δ |
|---|---|---|---|
| RESOLVED — Cleared Up | 17 | **25** | +8 |
| RESOLVED — Deferred | 2 | 2 | — |
| PENDING VERIFICATION | 19 | **14** | −5 |
| POTENTIAL ROADBLOCK | 3 | **0** | −3 |
| ROADBLOCK (SEVERE) | 0 | **0** | — |
| **Total** | 41 | 41 | — |

Next free flag number: **#46**.

Four flags added during migration (Project Log Entry 4 and dependency verification):

| Flag | Section | Proposed class |
|---|---|---|
| #42 | Methods §2.2.1 — V-zone buffer geometry (previously reserved, now assigned) | PENDING VERIFICATION |
| #43 | Results §3.1 — 63-subset combinatorial analysis has no code in `AuditedCode_1.py` | **POTENTIAL ROADBLOCK** |
| #44 | Results §3.1 / Methods — `k` denotes both species-subset size and tree count | PENDING VERIFICATION |
| #45 | Abstract / Methods §2.4.2 — stated software stack contradicts the implementation | PENDING VERIFICATION |

**Flag #45 detail.** The Abstract states ACO was implemented "via the scikit-opt Python library"; `AuditedCode_1.py` contains no `sko` import and hand-implements `AntColonySystemACO`. §2.4.2 credits "Matplotlib and Seaborn"; only matplotlib is imported. Verified dependencies are numpy, matplotlib, scipy (`cdist` only), tqdm, and pandas (soft, try/except-guarded). A reviewer attempting reproduction would install scikit-opt and find nothing uses it — this is a reproducibility defect, not a wording nit.

Revised counts: 25 cleared · 2 deferred · 17 pending · **1 potential roadblock** · 0 severe · **45 total**.

The project's clean record ended this session: after three audit cycles with zero escalations, the first POTENTIAL ROADBLOCK since v1 was found — by structural grep, not by reading — in the one section nobody has reviewed.

---

## Open work by owner

### Research lead — 6 decisions
D-02 (normalization ceiling), D-03 (statistical outcome metric), D-04 (final title), D-05 (Chebyshev terminology), **D-06 (recover the combinatorial script — highest urgency)**, D-07 (`k` notation). See `DECISIONS.md`.

**D-06 outranks everything.** D-02 and D-03 gate how Results are *written*; D-06 determines whether §3.1, and the Abstract and Conclusion claims that depend on it, can exist at all.

### Deriver — 5 literature items, zero code dependency
| Item | Flag | Ask |
|---|---|---|
| Land-use ratios | #9 | Citable grounding for the 55–65 / 25–40 / 5–10 P/A/V split against Philippine urban land-use & zoning literature. Sent; **no response yet.** |
| AGB estimation error | #20 | Source the estimation-error percentages. Newly assigned, no progress. |
| "Expander heuristic" | #26 | Is the term from Almeida et al. (2002) or coined by the team? Bundle with the `p0` lookup. |
| H–D allometrics | #30 | **Highest priority.** Real literature H–D equations for the six species (or genus proxies). |
| `p0 = 0.5` provenance | — | Does Almeida et al. (2002) specify an initial-condition convention? If not, is uniform init citably conventional? Can `p0` collapse into the existing `p_init` to eliminate an undocumented parameter? Directive on file. |

**Flag #30 detail (confirmed twice, independently):** using the manuscript's own Table 4 constants, all six species yield `h < h0` (ratio 0.278–0.742), producing DBH of 0.17–0.66 m — physically implausible — and computed LAI 50–420× smaller than the LAI values the model actually uses. The DBH-from-height inversion runs opposite to typical FORMIND allometrics. **This is a real defect, not a suspicion.** Allometric sensitivity results are invalid until it closes.

### Code-stressor — blocked on D-03, then execute
1. Run the Wilcoxon signed-rank test once D-03 fixes the metric. n = 30, paired on grid + k.
2. Regenerate Results under Option B (code is ready as-is).
3. **Note for V-density stress testing:** the BFS produces exactly **8 V-cells every run, zero seed variance**. Vary `v_target_range` midpoint explicitly — seed variation will *not* explore the 5–10% band.

### Editor — 6 Methods corrections ready to apply now
All confirmed; none blocked. See `CLAUDE.md` §7. Closes Flags #25, #28, #33, #35, #38, #41, plus the §2.2.1 BFS rewrite.
Then: author the new Results section once regeneration completes.

### Editorial-flagger — resume at Results
Review has never reached **Results, Discussion, or Conclusion**. Those three sections have zero editorial coverage. This is the largest uninspected surface in the project and the most likely source of new severe flags.

---

## Code health — verified, not assumed

`AuditedCode_1.py` (3,670 lines) at `/legacy/AuditedCode_1.py`. `py_compile` passes clean. All Entry 1 fixes confirmed present in Entry 2 by grep + execution; **no regressions detected.**

Confirmed working:
- Grid density compliance: 40/40 seeds in band (20 organic + 20 linear)
- SECPI magnitude ordering: 0-tree = 0.000 · 1-tree-worst = 1.919 · 6-tree-best = 2.969
- Fixed reference cutoffs applied consistently at all 5 ACO instantiation sites
- Tie-inversion bug fixed (degenerate all-zero → class 1, boundary `<= q1`)
- ACO fidelity restored — `SensitivityAnalyzer` and `MorphologicalRobustnessValidator` now read from `base_aco_config` instead of hardcoded 10 ants / 15 iterations
- Almeida CA formula: `p(t+1) = γ · ω · p(t)`, clipped to [0,1]
- 6 morphology presets with distinct `p_target_range` / `v_target_range`
- Fabricated allometric sensitivity removed; `get_dbh()` / `get_computed_lai()` added

**Known architectural debt:** monolithic single file; `AutomatedInterpreter.interpret_k_scenarios` is monkey-patched onto the class after definition; `main_revised_validation()` carries the full config inline. See `MIGRATION.md`.

**Missing capability (Flag #43):** no combinatorial species-subset sweep exists. `itertools` is imported at line 11 and never called; `AntColonySystemACO.species_subset` is accepted at line 1781 and never passed by any caller. Both read as fossils of a routine that was removed or never ported. See D-06.

**Interpretation-layer hazard:** `AutomatedInterpreter.interpret_scenario_comparison()` prints `"Difference: SIGNIFICANT"` on a hardcoded `|Δ| > 0.1` threshold. This is a magnitude label, not a statistical test. No output from that function may be described as significance in the manuscript — and it must not be confused with the D-03 Wilcoxon result once that exists.

---

## Provenance gap — Project Log Entry 3 is missing

`FLAGS.md` (v2) cites "Project Log Entry 3" as the sole source for four flag resolutions (#20, #26, #35, #38), but the log carried over from the Claude Project ends at Entry 2. See the placeholder in `PROJECT_LOG.md`.

`math-auditor` should re-verify #35 and #38 by execution — both are independently checkable against the code — and re-source them to a new entry. #20 and #26 are queue assignments with no analytical content; re-issue to the Deriver.

---

## Session-end checklist

- [ ] Appended a dated entry to `PROJECT_LOG.md` using the template
- [ ] Updated flag statuses in `FLAGS.md` (never renumber)
- [ ] Moved any new research-lead question into `DECISIONS.md` as a numbered `D-xx`
- [ ] Updated the "Open work by owner" table above
- [ ] Every numerical claim made this session was produced by execution, not inference
