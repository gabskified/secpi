# STATE.md — Live Ownership Board

Last synchronized with: **Project Log Entry 5 / Flag Archive v3 (truncated at #74)** — synced 2026-07-26.
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

> ⚠️ **SUPERSEDED 2026-07-26 (Entry 5) — do not quote this line.** It read: *"Current live total: 51 flags (41 original + #42–#51 added during migration)… Next free number: #52."* Both figures are stale. **The live total is 74 and the next free number is #75.** See the authoritative count block immediately below.

### 🔢 Authoritative flag counts — synced 2026-07-26 (Entry 5)

| Category | Count |
|---|---|
| RESOLVED — Cleared Up | **29** |
| RESOLVED — Deferred | **2** |
| PENDING VERIFICATION | **25** |
| POTENTIAL ROADBLOCK | **18** |
| ROADBLOCK (SEVERE) | **0** |
| **TOTAL LIVE FLAGS** | **74** |

**Next free flag number: #75.**

Derived by per-flag enumeration of `docs/FLAGS.md`, not by carrying forward any summary line. Basis: the 51-flag baseline (29 / 2 / 17 / 3 / 0), plus v3's escalations of **#39** and **#44** (PENDING → POTENTIAL ROADBLOCK), plus the 23 flags actually written in v3 (**#52–#74**: 13 POTENTIAL ROADBLOCK, 10 PENDING VERIFICATION).

> 🔴 **`docs/FLAGS.md` is truncated. Flags #75–#94 were announced but never written** — the v3 session terminated mid-write. Its Executive Summary claims **94 flags, 30 potential roadblocks and 1 ROADBLOCK (SEVERE)**; those describe a file that does not exist. **This project's severe count is 0.** The claimed severe item (#75, §3.5's category-level sensitivity means) survives only as a forward reference; the underlying arithmetic defect was spot-checked and looks real, but no flag registers it. Do not report a severe roadblock to the research lead on the strength of a forward reference. Full detail: Project Log Entry 5 §A.

> **Prior arithmetic defect, now closed.** The former summary line read *"28 cleared · 2 deferred · 19 pending · 3 potential roadblocks · 0 severe · 51 total"* — five categories summing to **52**, not 51. Flag Archive v3 identified this and correctly routed it to the orchestrator rather than editing it. Resolved 2026-07-26 in favour of the per-flag record.

**Added 2026-07-25 from the D-06 salvage** (see `DECISIONS.md` D-06):

| Flag | Section | Description | Class |
|---|---|---|---|
| #46 | Results §3.1, Abstract, Conclusion | `k` = species *available*, not *used*. ACO used the full palette in only 30.16% (WITH) / 19.05% (WITHOUT) of configurations; the rank-1 k=6 result planted just 2 species. The "diversity offers negligible benefit" claim is mis-stated. | **POTENTIAL ROADBLOCK** |
| #47 | Results §3.1 | WITHOUT_VULN produced only 3 distinct SECPI values (1.500/1.501/1.750) across 63 configurations — near-total loss of discrimination, likely saturation or clamping. | PENDING VERIFICATION |

**Flag #43 downgraded** — POTENTIAL ROADBLOCK → RESOLVED (Cleared Up). The combinatorial output was located at `legacy/archive/corrected_outputs/run_20260213_222844/combinatorial/` and matches §3.1 verbatim (4.3916 / rank 3 / 63 rows). Superseded by outcome (b), not missing.

**Flag #44 refined** — §3.1's `k` is now confirmed as *available palette size*, a third distinct meaning alongside subset size and tree count. Feeds D-07.

**Entry 3 recovered 2026-07-25 — Deriver flag batch resolved.** The provenance gap is closed; the entry is now in `PROJECT_LOG.md` with independent verification of every §1 numeric claim against raw field data.

| Flag | Movement | Basis |
|---|---|---|
| #19 | PENDING → ✅ **RESOLVED — error confirmed** | *Terminalia catappa* and *Lagerstroemia speciosa* are both documented **deciduous**. The blanket "evergreen tree types" claim is factually wrong. Correct to "predominantly evergreen, with Talisay and Banaba deciduous/semi-deciduous." |
| #26 | PENDING → ✅ **RESOLVED — direct precedent** | "Expander" is **DINAMICA** terminology, not author-coined and not originally Almeida's. Cite **Soares-Filho, Cerqueira & Pennachin (2002), *Ecological Modelling* 154(3), 217–235.** DINAMICA's expander is `P' = P × √(nⱼ/4)` — a neighbourhood factor on a weights-of-evidence potential, never a uniform constant, reinforcing that `p0 = 0.5` is the team's own simplification. |
| #30 | POTENTIAL ROADBLOCK → ◐ **PARTIAL — 3 of 6 species resolved** | Real refitted coefficients now exist for Narra, Talisay, Banaba from 211 NPDC field records, independently reproduced. **Duhat, Kabiki, Akleng-parang have no data** — no open paired (DBH, height) dataset located. Options: constrained pantropical/genus fit, fieldwork, or disclose as range-constrained author estimates. |
| #35 / #38 | Re-sourced | Confirmed as a single defect from a readable source: code and calibration are Gaussian (15% at d=C_D ✓, 62.2% at d=C_D/2 ✓); §2.3.2 dropped the square. Fix = restore the square. |
| #20 | PENDING → ◐ **PARTIAL — needs author input** | Directional claim well-supported (Chave et al. 2004; Mauya et al. 2015). **No source called "PTM-2" could be located**, and no source gives the manuscript's specific figures (~50% / ~10% / ~5%). Ask the author team what "PTM-2" refers to. |
| #21 | PENDING → ◐ **Likely resolved** | **No author named "Kunhle" exists** in the submodular-optimization literature. Correct source is almost certainly **Bian, Buhmann, Krause & Tschiatschek, ICML 2017** (manuscript cites "Bian et al., 2018" one section earlier — year off by one). Editor to confirm. |
| #22 | PENDING → ◐ **Diagnosed — citation-form error** | **NSF is a funding agency, not an author.** EPFL has attributable material (Discrete Optimization Chair; MATH-504). The team must name the actual paper/textbook intended (e.g. Rothvoss, *Integer Optimization and Lattices*, or Schrijver) rather than cite institutions. |
| #9 | Detail added | P 55–65% analogous (specify density context — Metro Manila core ~78% impervious); A 25–40% aligns with *aspirational* targets (UN-Habitat 30%+10–15%; C40 30%), not measured cover (~16% global avg); **V 5–10% has no precedent and is directionally contradicted** by Philippine heat-vulnerability data (Quezon City: 81% of barangays high-risk). **V is the highest-priority disclosure item.** |
| #14 | ◐ Spot-checked | Yigitcanlar verified real and active. **Scordato & Gulbrandsen and Abujder Ochoa et al. remain unchecked.** |

**New flags from Entry 3:**

| Flag | Section | Description | Class |
|---|---|---|---|
| #48 | §2.3 / Table 4 | Assumed species heights extrapolate beyond calibration — Narra 30 m implies DBH 244.5 cm vs. observed max 117.2 cm and species max ~200 cm. Independent of which H–D constants are used. See **D-08**. | **POTENTIAL ROADBLOCK** |
| #49 | §2.3.2 | λ = 1.897 attributed to Morakinyo & Lam (2016), which is an **ENVI-met thermal-comfort study, not a distance-decay calibration**. λ is arithmetically fixed by the author-chosen 15% anchor (−ln 0.15 = 1.897). Author construct requiring disclosure. | PENDING VERIFICATION |
| #50 | §2.3 | Cooling decay kernel `exp(−λ(d/C_D)²)` has **no direct literature precedent** — author construct requiring disclosure. | PENDING VERIFICATION |

**Added 2026-07-25 during Phase 1.5 manuscript extraction:**

| Flag | Section | Description | Class |
|---|---|---|---|
| #51 | Results §3.5 | **Subsection numbering error.** §3.5 Sensitivity Analysis contains `3.5.1`, then jumps to **`3.4.2`** and **`3.4.3`** — duplicate numbers already used under §3.4. Mechanical fix; renumber to 3.5.2 / 3.5.3. | RESOLVED — Cleared Up (fix is unambiguous) |

**⚠️ Flag #47 CORRECTED — my error, not the manuscript's.** I registered #47 claiming the WITHOUT_VULN degeneracy (3 distinct SECPI values across 63 configs) was "not explained by any existing flag." **That was wrong.** The manuscript documents it explicitly at §3.4.4: scores *"compress into two narrow bands centered at approximately 1.50 and 1.75, with the entire top 48 configurations falling within a range of only 0.0002,"* interpreted as the optimizer lacking spatial signal without equity weighting. The authors observed and wrote up the phenomenon; I flagged as undiscovered something already in their Results.

**Revised #47:** PENDING VERIFICATION → the *observation* is documented and correct. What still needs checking is whether the *interpretation* holds, and whether a near-degenerate WITHOUT_VULN arm is a sound comparison baseline. Reframed as an analytical question, not a discovery.

**Corroboration from the same extraction:** §3.4.4 states SECPI spans **"3.023 to 4.393... across the 63 configurations"** — matching the recovered `run_20260213_222844` CSV exactly (best 4.393, and a `k2_Tal_Ban_SECPI_3.023.png` file). Independent confirmation that D-06's located output is the source of the manuscript's Results.

~~Next free flag number: **#52**.~~ — **superseded 2026-07-26: the next free number is #75.** See the authoritative count block at the top of this file.

---

**Added 2026-07-25 by the `editorial-flagger` v3 pass over Results, Discussion and Conclusion — logged retroactively in Project Log Entry 5 (session was interrupted).**

**Flags #52–#74 (23 new)** — 13 POTENTIAL ROADBLOCK, 10 PENDING VERIFICATION. First editorial coverage §3.1–§3.4.4 has ever received. Registered in full in `docs/FLAGS.md`; not duplicated here.

| Class | Flags |
|---|---|
| **POTENTIAL ROADBLOCK** (13) | #52, #54, #55, #56, #57, #60, #62, #64, #67, #68, #69, #70, #72 |
| PENDING VERIFICATION (10) | #53, #58, #59, #61, #63, #65, #66, #71, #73, #74 |

The heaviest items: **#62** (a dimensionless 0–1 cooling proxy is relabelled °C with no calibration anywhere — this is the Abstract's headline 0.809 °C), **#69** (§3.4.4's central validation uses the objective function as its own outcome variable, so the result is algebraically guaranteed), **#64** (§3.4.1's per-`k` means are numerically incompatible with the same dataset's individual values — #44's `k` collision surfacing as an arithmetic error), **#72** (the equity-weight scheme, the paper's claimed novelty, is operationalized one way in Methods Table 2 and a different way in §3.4.4), and **#57** (the ACO configuration is published two mutually exclusive ways, differing 11× in function evaluations).

**Escalations in the same pass:** **#39** and **#44** both PENDING VERIFICATION → **POTENTIAL ROADBLOCK**. **#46, #30, #6, #10, #11, #8** refined or extended in scope, classes unchanged. No flag was downgraded or closed.

**⚠️ Verification status (orchestrator, Entry 5 §C).** All 23 were re-checked against `manuscript/sections/`. **Every manuscript quotation in #52–#74 is verbatim-accurate**, and 18 flags are confirmed in full. **Five carry defects in reasoning or sourcing and must be repaired before going to any downstream agent:**

| Flag | Defect | Fix |
|---|---|---|
| **#53** | Claims Akleng-parang outranks Narra under midpoint conventions — **not reproducible**; Narra leads under every convention tried. Also wrongly asserts Banaba is among the two highest-LAI species, and cites the 0.70/0.30 weighting to §2.3.1 (it is §2.3.2). | Drop both claims; re-cite. The maxima check (Akleng ≈0.72 vs reported 0.856) stands. |
| **#59** | Headline says the two convergence traces are "conflated"; the manuscript names them separately and is internally consistent on that point. | Reword to the Figure 11 labelling question. Objection (b) (no pheromone diagnostic) stands. |
| **#64** | Attests "hand arithmetic on the manuscript's own printed values" — but Kabiki 3.094 and Banaba 3.068 appear nowhere in §3; they come from the D-06 CSV. | Correct the attestation. The finding (k=1 mean 2.990 < the lowest printed k=1 value 3.0396) survives intact. |
| **#68** | Same sourcing defect: Δ = 0.0396 uses the CSV's Kabiki value. Manuscript-only margin is 0.094. | Re-source. Objection holds at either value. |
| **#70** | Asserts as fact that "[SUCCESS] HIGH EQUITY" is threshold-triggered. **No project record establishes this** — `STATE.md` documents a *different* function (`interpret_scenario_comparison()` → `"Difference: SIGNIFICANT"` on \|Δ\| > 0.1). | Demote to hypothesis pending `math-auditor`. Part (a) — unsupported "significantly" — is confirmed. |

---

Four flags added during migration (Project Log Entry 4 and dependency verification):

| Flag | Section | Proposed class |
|---|---|---|
| #42 | Methods §2.2.1 — V-zone buffer geometry (previously reserved, now assigned) | PENDING VERIFICATION |
| #43 | Results §3.1 — 63-subset combinatorial analysis has no code in `AuditedCode_1.py` | **POTENTIAL ROADBLOCK** |
| #44 | Results §3.1 / Methods — `k` denotes both species-subset size and tree count | PENDING VERIFICATION |
| #45 | Abstract / Methods §2.4.2 — stated software stack contradicts the implementation | PENDING VERIFICATION |

**Flag #45 detail.** The Abstract states ACO was implemented "via the scikit-opt Python library"; `AuditedCode_1.py` contains no `sko` import and hand-implements `AntColonySystemACO`. §2.4.2 credits "Matplotlib and Seaborn"; only matplotlib is imported. Verified dependencies are numpy, matplotlib, scipy (`cdist` only), tqdm, and pandas (soft, try/except-guarded). A reviewer attempting reproduction would install scikit-opt and find nothing uses it — this is a reproducibility defect, not a wording nit.

~~Revised counts: **28 cleared · 2 deferred · 19 pending · 3 potential roadblocks · 0 severe · 51 total.**~~ — ⚠️ **superseded 2026-07-26.** These five categories summed to **52**, not 51; the arithmetic defect is resolved in favour of the per-flag record. **Current counts: 29 cleared · 2 deferred · 25 pending · 18 potential roadblocks · 0 severe · 74 total** — see the authoritative block at the top of this file.

The **18** potential roadblocks: the original three — #46 (mis-stated diversity claim), #48 (assumed heights beyond calibration), #30 (pending its remaining 3 species without field data) — plus #39 and #44 escalated in the v3 pass, plus the 13 new ones from #52–#74 listed above.

---

## Open work by owner

### Research lead — 7 open decisions
D-02 (normalization ceiling), D-03 (statistical outcome metric), D-04 (final title), D-05 (Chebyshev terminology), D-07 (`k` notation — now a three-way collision), D-08 (assumed heights), D-10 (`p0 = 1.0` sign-off). D-01, D-09 decided; D-06 resolved (outcome b). See `DECISIONS.md`.

**D-02 and D-03 gate the Results rewrite.** D-06 is resolved — the combinatorial output was located and confirmed as outcome (b), so §3.1 regenerates rather than being reconstructed from scratch.

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

### Editorial-flagger — two-thirds done, resume at §3.5

~~Review has never reached **Results, Discussion, or Conclusion**.~~ — **partially discharged 2026-07-25** (Project Log Entry 5). The v3 pass covered **§3.1 through §3.4.4** and produced flags **#52–#74**. It confirmed the prediction: 13 of 23 are POTENTIAL ROADBLOCK, in a manuscript that had zero before this section was read.

**Still uninspected — resume here:**

1. **§3.5 Sensitivity Analysis** — `manuscript/sections/06_results_discussion.md:597–725`. **Highest priority.** A spot-check found §3.5.2 reporting a Species Morphology category mean SI of **1.3068** while the largest single SI anywhere in §3.5.1 is **0.4435**, with the other 39 parameters below 0.005 — a mean cannot exceed its own maximum. The same sentence lists **"Species Allometry" twice** (0.1857, 0.0727) where the following paragraph implies the second is *Cooling Model*. The v3 session intended to register this as the project's first **ROADBLOCK (SEVERE)** (#75) and never wrote it.
2. **Conclusion, Recommendations, back matter** — `manuscript/sections/07_conclusion.md`. Four findings were identified and left unwritten: **#79** (§3.5.3's "sourced from literature" is a false provenance claim, refining #30), **#90** ("successfully developed and validated" — no field or remote-sensing validation exists), **#91 / #92** (a real-world planting prescription for Philippine planners, and a transferability claim across "climate-vulnerable cities", both colliding with the synthetic non-georeferenced design). All four quotations were verified verbatim against the manuscript; only their flag entries are missing.

**Assign from #75.** Do not renumber #52–#74. Also owed: repair of the five defective flags (#53, #59, #64, #68, #70) per the table above.

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

## Provenance note — Project Log Entry 3 RECOVERED

Entry 3 (Deriver) was recovered 2026-07-25 and folded into `PROJECT_LOG.md` with independent verification of every numeric claim against raw field data (`docs/data/SECPI_HD_field_data.csv`). The gap flagged during migration is **closed**. The four flags that cited it (#20, #26, #35, #38) now have a readable source.
## Session-end checklist

- [ ] Appended a dated entry to `PROJECT_LOG.md` using the template
- [ ] Updated flag statuses in `FLAGS.md` (never renumber)
- [ ] Moved any new research-lead question into `DECISIONS.md` as a numbered `D-xx`
- [ ] Updated the "Open work by owner" table above
- [ ] Every numerical claim made this session was produced by execution, not inference
