# STATUS — SECPI

**Generated:** 2026-07-27 by `interpreter`. Supersedes the 2026-07-26 run in full.
**Derived from (read this session):** `CLAUDE.md`, `docs/DECISIONS.md` (D-01…D-13), `docs/STATE.md`, `docs/FLAGS.md` (v5 content, #1–#97), `docs/PROJECT_LOG.md` Entries 8/9/10, previous `docs/STATUS.md`.
**Working-tree note:** the D-12/D-13/D-11-amendment/v5-register changes are on disk and uncommitted. This file reflects disk, not `git log`.

> This file is **derived**. If it disagrees with `FLAGS.md`, `DECISIONS.md` or `PROJECT_LOG.md`, those win — regenerate, do not reconcile by hand.

### Count check — enumerated, not copied

Walked every per-flag record in `FLAGS.md` (two formats: the #1–#51 summary/movement tables, and the `**#N — …** · CLASS` headers from #52 on; #77's struck-through old class and #96's parenthetical "SEVERE" annotation excluded by hand).

| | cleared | deferred | pending | potential roadblock | SEVERE | total |
|---|---|---|---|---|---|---|
| #1–#41 (after v3 movements) | 27 | 2 | 10 | 2 | 0 | 41 |
| #42–#51 | 2 | — | 5 | 3 | 0 | 10 |
| #52–#74 | — | — | 10 | 13 | 0 | 23 |
| #75–#95 | — | — | 4 | 16 | 1 | 21 |
| #96–#97 | — | — | — | 2 | 0 | 2 |
| **Derived total** | **29** | **2** | **29** | **36** | **1** | **97** |

**Next free flag number: #98.** Derived total **agrees** with `FLAGS.md:1114–1123`, `STATE.md:23–32`, Entry 9 and Entry 10 §5. **No live-total discrepancy this run.** Stale *historical* totals elsewhere are listed in §6.

**Decision queue, enumerated from `## D-xx` headings:** 13 decisions. DECIDED: D-01, D-02, D-03, D-07, D-09, D-11 (amended 2026-07-27), D-12. Resolved-with-residuals: D-06. `OPEN`: D-04, D-05, D-08, D-13. "Recommendation ready, needs sign-off": D-10. **Awaiting the research lead = 5** (D-04, D-05, D-08, D-10, D-13), matching `STATE.md:149`. ⚠️ **But 5 understates the ask** — see §3.

---

## 1. Headline

Bad news first: the §3.5 path moved from *decision-blocked* to *authorized-but-unapplied*, which is progress on paper and zero progress in the file — **D-12 was authorized 2026-07-27 and no line of `legacy/AuditedCode_1.py` has changed**, and Entry 8 additionally established that §3.5's published numbers did not come from this codebase at all, so the regeneration D-11 ordered will neither reproduce nor vindicate §3.5. The single biggest obstacle is not the SEVERE flag: it is that the three prerequisites now standing in front of D-11's regeneration are one unapplied code fix and **two research-lead questions (#75, #77) that exist nowhere in the decision queue**. Recommended next action, labelled as a recommendation: apply D-12's fix (including the `max_CPA`/`max_LAI` restoration Entry 10 §3 identified), and in the same sitting put #75 and #77 to the research lead as numbered decisions.

---

## 2. Preprint readiness

Re-derived this run from the register and the live decision queue. Nothing carried forward from the previous STATUS.md.

| Must be true before an EarthArXiv DOI is minted | True? | Blocked by |
|---|---|---|
| No ROADBLOCK (SEVERE) outstanding | 🔴 No | **#82**. Remedy = D-11 regeneration, which is itself blocked (three rows below) |
| D-12's state-leak fix applied to `legacy/AuditedCode_1.py` | 🔴 No | **Authorized 2026-07-27, not applied.** `code-stressor`. Must also restore `max_CPA`/`max_LAI`, not just `SPECIES_DATA` (Entry 10 §3) |
| #75's sensitivity-design question answered | 🔴 No | Three-way (Morris / repaired local OAT / as-run). **Not a numbered decision** |
| #77's replication count decided + `n`/`SD` emitted | 🔴 No | **Not a numbered decision.** The code stores no dispersion at all — capability must be *added*, not run |
| §3.5 regenerated under Option B | 🔴 No | The three rows above, in that order, then execution |
| §3.1–§3.4 regenerated under Option B | 🔴 No | Not decision-blocked. Blocked on execution only |
| Ceiling 3.75 re-checked against the optimizer | 🔴 No | D-02's standing obligation; 3.75 sits just above 3.52, a *random*-placement max |
| Every "significant" claim has a test behind it | 🔴 No | H1/H2 design decided, unexecuted. `editor` must pre-specify in §2.5.2 **before** execution. #70's manuscript-wide sweep is not discharged by D-03 |
| Cooling figures carry a defensible unit | 🔴 No | #62/#63/#90 — °C on a dimensionless 0–1 proxy. **No owner, no D-xx** |
| Diversity claim matches the data | 🔴 No | #46/#91. D-06 residual sub-decision 2 |
| Conclusion claims stay inside scope | 🔴 No | #87, #88, #91, #92, #93 |
| Author contributions complete; funding/COI/data/code statements exist | 🔴 No | #94, #95. **Author team only** — no agent can discharge these |
| References + appendices have had one editorial pass | 🔴 No | `08_references_appendices.md` never inspected. Assign from **#98** |
| Title locked (DOI landing page is permanent) | ⬜ No | **D-04** |

---

## 3. Decisions awaiting the research lead

**Five numbered** — plus six unnumbered asks that the "5 open" figure hides. The hidden six are where work stops silently.

| ID | What | Blocks | Effort | Critical path |
|---|---|---|---|---|
| **D-04** | Final title: current vs. Flag #10 revision | DOI minting. Landing-page title is permanent | One of two | **Yes** (DOI only) |
| **D-13** | Where §3.5's published numbers came from | Nothing. But until answered no §3.5 number has a known origin; it is #97's escalation trigger **in both directions** | Needs a session (time-boxed) | No — **unassigned** |
| D-08 | Re-anchor assumed heights, or disclose extrapolation | Crown geometry → every cooling number (#48, #30) | One of two, real cost either way | No, propagates widely |
| D-10 | Fix `p0 = 1.0`, let γ absorb calibration | CA generation code | Yes/no; recommendation on file | No |
| D-05 | "Chebyshev space (ℤ²)": convention or error | §2.2.1 prose only | Keep/delete | No — **no agent can answer this** |

**Not numbered, but owed by the research lead:**

1. **#75** — Morris / repaired local OAT / contaminated sweep as-run. **Prerequisite to D-11.** Recommended for numbering by Entry 9 and Entry 10; not opened.
2. **#77** — should the sensitivity analysis replicate at the optimizer's `n_runs = 5`? A design choice, not a typo (`n_samples ≠ n_runs`). **Prerequisite to D-11.**
3–5. **D-06's three residuals** — confirm §3.1 regenerates under Option B; **confirm the #46 diversity reframing** (this changes what the paper argues, not clerical); decide whether `species_actually_used` becomes a reported variable.
6. **D-02's standing re-check** — 3.75 is decided as a decision, provisional as a value.

**Carve-outs that are easy to lose:** D-07 does **not** close #64 or auto-downgrade #44. D-03 does **not** discharge #70. D-11's amendment **discharges `math-auditor`'s aggregation assignment — do not re-run it.**

---

## 4. Key flags — by root cause

### 🔴 The only SEVERE: #82 — §3.5.2's four category means each exceed the max SI of their own member set

Weighting has exactly one member (SI 0.0017) and is printed with a mean of 0.0236. A one-element mean *is* that element. **Status: verified** by hand arithmetic on manuscript-printed values; no execution needed. **Do not** argue it from a `[0,1]` bound, do not call the values sums, and "relabel sum-vs-mean" is not an available remedy.

**Strengthened, not weakened, by Entry 8 (executed):** the aggregation code is innocent — `groupby().agg` computes a true mean, 0 violations of `mean ≤ max` in 2,000 randomized trials. The published means therefore did not come from this code. #82's own note that "§3.5.1 may be salvageable" is **superseded by #97**.

### Causal clusters

| Cluster | Members | One action that collapses it | Owner | State |
|---|---|---|---|---|
| **A. `SensitivityAnalyzer` leaks class-level state** | **#96**; blocks #75, #77, #78, #79, #82's remedy, #85, #97, D-11 | Apply D-12's fix **plus** `max_CPA`/`max_LAI` restoration; re-run the idempotency and drift probes | `code-stressor` | **Authorized, not applied** |
| **B. §3.5's numbers came from outside this repository** | #82 (SEVERE), #97, #76, #84, #89, #80, #81 | D-13's forensic search of `legacy/archive/` — regeneration does *not* answer provenance | ⚠️ **NOBODY — D-13 is unassigned** | Open |
| **C. The sensitivity design is undecided and under-replicated** | #75, #77, #78 | Research lead answers #75 (three-way) and #77; `code-stressor` adds `n`/`SD` emission | ⚠️ **No D-xx exists for either** | Blocked |
| **D. ACO run-to-run variance is never measured** | #65, #67, #68, #78 (#77(b) supplies the capability) | One replicated noise-floor measurement across the production restart set, reported beside every effect | `code-stressor` | Rides the regeneration |
| **E. A dimensionless 0–1 proxy is reported in °C** | #62, #63, #90 | Supply a sourced calibration, or strip °C manuscript-wide | ⚠️ **No owner, no decision** | Untouched |
| **F. Synthetic/non-georeferenced study written as geographic** | #86, #91, #92, #93 (+ D-04) | One `editor` scope-limiting pass over Results §3.5.3, Conclusion and Recommendations | `editor` + lead (D-04) | Ready when Results settle |
| **G. `k` carried three meanings** | #44, #64, #46, #80 | Regenerate §3.1 and §3.4.1 under Option B with D-07's `s`/`k`; confirm D-06's reframing | `code-stressor` → `editor` | Execution-blocked |
| **H. Validation claimed but never performed** | #39, #69, #70, #87, #88 | Execute H1/H2 (after `editor` pre-specifies), and supply or withdraw the three missing validation stages | `editor` → `code-stressor` | Sequenced |
| **I. Allometric chain has no source and is off-path** | #30, #48, #84, #85 (+ D-08, D-09) | D-08 decision + #85's call-path trace (**must run after cluster A**) | lead + `math-auditor` + `deriver` | Partly blocked |
| **J. What was actually run is stated inconsistently** | #45, #52, #57, #58, #60, #61, #71 | One machine-emitted "configuration of record" from a named `results/` run; Methods states it once | ⚠️ **No single owner** | Untouched |
| **K. Back matter / submission hygiene** | #94, #95, #51, uninspected references + appendices | Author team supplies; schedule the references pass **from #98** | Author team | Untouched |

**Flags appearing in more than one cluster:** #78 (C and D); #82 (A's remedy and B); #84 (B and I); #85 (A and I); #46 (B-adjacent via D-06, and G); #80 (B and G); #57/#58 (J, and C via the ACO config).

**Clusters with no owner or no action attached — this is where work stops silently:** **B** (D-13 unassigned), **C** (two research-lead questions with no D-number), **E** (no owner at all), **J** (no single owner). Recommend the orchestrator route all four.

### Known but deliberately **unregistered** — do not lose it

`main_revised_validation()` runs STEP 7 (sensitivity, line 3522) then STEP 8 (morphological robustness, line 3540) **in one process**, and STEP 8 builds a fresh `TreeSpecies` that Entry 8 §D2 proved sees contaminated class state. So STEP 8 plausibly begins with every species at high crown diameter and height, feeding the Conclusion claim #88 already flags. **Step ordering verified by reading; contamination mechanism verified by execution; the joint claim is INFERRED and has NOT been executed.** It carries no flag number by design (Entry 10 §4). Owner: `code-stressor`, as a before/after check in the D-12 pass; flag it **from #98** afterwards, on evidence.

---

## 5. Triage buckets

Re-derived this run.

**A — blocks the preprint.** #96 (gate on everything in §3.5). #82 (SEVERE). #75, #77 (D-11's other two prerequisites). #97. Cluster D's noise floor (#65, #67, #68, #78). Cluster E's °C (#62, #63, #90). #46/#91's inverted diversity claim. Cluster H (#69, #70, #87, #88). #94, #95. D-04.

**B — fix before journal submission, not necessarily before the DOI.** #76, #79, #80, #81, #89 (falls out of regeneration). Cluster I (#30, #48, #84, #85). Cluster J (#45, #52, #57, #58, #60, #61, #71). #83. #64, #44 (regenerate, do not reword). #92, #93. The six confirmed Methods corrections in `CLAUDE.md` §7. #66.

**C — disclose or defer.** #49, #50 (author-construct disclosures). #9's land-use grounding — **V 5–10% is the priority disclosure**, it has no precedent and is directionally contradicted. Citation-form errors (#20 "PTM-2", #21, #22). #51 renumbering. #90's dimensional slip (applyable now). #47's interpretation question. #53, #59, #61, #63, #71, #73, #74.

**Movement since last run:** #77 promoted B→A (escalated to POTENTIAL ROADBLOCK). #96, #97 enter A on creation. #85 moves B→"blocked until A clears" — its call-path trace must not run before the leak fix.

---

## 6. Integrity warnings

**Stale numbers that will auto-load into future sessions:**

- 🔴 **`CLAUDE.md` line 28** states *"(As of 2026-07-27: register runs through #95, next free is #96.)"* — **derived value is #97 / next free #98** (`FLAGS.md:1123`, `STATE.md:32`). This is the highest-risk stale figure in the tree because `CLAUDE.md` loads every session. The surrounding rule ("check `STATE.md`, not this file") is correct and `STATE.md` is current — but the wrong parenthetical still loads. Orchestrator's to fix.
- ⚠️ **`CLAUDE.md` line 59** says regeneration is *"blocked on Flags #75 and #77, then execution."* There are now **three** prerequisites — D-12's fix (#96) was added by D-11's 2026-07-27 amendment.
- ⚠️ **`STATE.md` line 3** header reads *"Last synchronized with … Flag Archive v4 (complete, #1–#95) — synced 2026-07-26"*, contradicting its own authoritative block 18 lines below (Entry 9 / v5 / 97 / 2026-07-27). Header stale, block current.
- ⚠️ **`STATE.md` line 135** carries an un-struck *"Current counts: 29 · 2 · 30 · 33 · 1 · 95 total"*, and line 19 says *"the live total is 95 and the next free number is #96."* Both are superseded by the block at lines 23–32. Reported side by side per instruction; **not adopted**.
- ⚠️ **`FLAGS.md` line 1148 and `PROJECT_LOG.md` Entry 9 (lines 1459, 1500)** assert that *"`docs/STATE.md` and `docs/STATUS.md` both still record 'next free: #96'."* **That is now false as to `STATE.md`** — Entry 10 updated it to #98 after Entry 9 was written. It was true of the previous `STATUS.md`, which this run supersedes.
- ⚠️ **`FLAGS.md` line 1** still titles the file *"(v4 …)"* though it carries v5 content through #97; **line 100** still says *"Flags #42–#94 are registered in the v3 blocks."*
- ⚠️ **`STATE.md` line 173** says *"D-11 now gates the Results rewrite alone"* — D-11 is decided; contradicted by line 158 of the same file.

**Known-wrong, not yet fixed:**

- **All manuscript Results numbers remain obsolete** under Option B — including the Abstract's 3.02–4.39, 28%, 0.03%, 0.809 °C. Nothing has been regenerated.
- **D-12 authorized, zero lines changed.** The pre-fix behaviour is the evidentiary artefact behind every existing `results/` run; anchor at commit `87d4528`.
- **Entry 8's fix recipe is incomplete** (Entry 10 §3, found by reading): a plain `SPECIES_DATA` restore leaves `max_CPA`/`max_LAI` — live denominators cached as instance attributes at `:1615–1616` and divided by at `:1630–1631` — computed from contaminated data. Verify both scalars explicitly or the fix is correct at the dict level and wrong at the normalization level.
- **D-02's ceiling is provisional as a value.** Treat any normalized SECPI produced before the re-check as unconfirmed.

**Provenance discipline — do not upgrade these:**

- Every magnitude from Entry 8 carries a binding scope caveat: **one grid, one morphology, one seed, `n_samples = 3`, no D-02 ceiling applied, `normalize_secpi()` not exercised — diagnostic, not the D-11 regeneration, and no number in it may be quoted as a manuscript value.** This binds the 1.84×/0.63× leak cost, the ≈0.0098 noise floor, the 3.2593 baseline, the 28/40 rank and the sign inversion. **Structural** claims (evaluation counts, sweep bounds, category membership, aggregation semantics, the state leak, the ACO kwargs) are deterministic and carry no caveat.
- **Do not publish 0.0098.** Use it to justify the requirement that every SI carry an interval, not as the interval.
- **#96 was argued down from a recommended SEVERE, not overlooked.** `editorial-flagger` tested it against #82's three conditions and it failed condition 2 (unresolvable): #96 has a known, small, local remedy that Entry 8's Phase H harness already executed successfully, and its harm is *prospective* — it corrupts the regeneration, it did not produce what is printed. Recording two SEVEREs would have told the lead there are two unresolvable manuscript defects; the true position is **one unresolvable manuscript defect (#82) plus one fixable code defect blocking its remedy (#96)**. Three explicit escalation triggers are written into #96.
- **Five flags were repaired in place, not reclassified** (#53, #59, #64, #68, #70). When quoting: #53's "Akleng-parang outranks Narra" is withdrawn; #64's decisive check is manuscript-internal (2.990 < 3.0396); #68 quotes at 0.094; #70's self-validation claim is a hypothesis, not a finding. **#79's premise is dead, its conclusion is not** — all 36 species parameters are ±20%; quote the corrected version only.
- **Historic defect, closed, recorded for continuity:** the five-category summary that summed to 52 against a stated 51 was resolved 2026-07-26 in favour of the per-flag record.

---

## 7. Ranked next actions — by leverage, not severity

Leverage = *how much this unblocks*. Reasoning is stated so the research lead can disagree with it.

**1. Apply D-12's state-leak fix. — ACTIONABLE NOW.**
*Unblocks:* #96 closes; #75's remedy path; #77's fix pass (repoint `n_samples`); #78's noise floor; #85's call-path trace; #97's replication; D-11's regeneration and through it #82's remedy, #89, Figure 34, §3.5.1–§3.5.3. Also produces the evidence to flag the STEP 7 → STEP 8 contamination from #98.
*Cost:* one `try/finally` plus the `max_CPA`/`max_LAI` restoration; verification sweep 243 evaluations ≈ 7.8 min per arm at the measured 1.92 s/evaluation.
*Owner:* `code-stressor`.
*Leverage reasoning:* it is the cheapest item on the board and a prerequisite of the most other work, and it is **the only §3.5 prerequisite that needs nothing further from the research lead**. Disagree if you intend to answer #75 with option (3) — then the fix is moot, but #96's escalation trigger 2 fires and it becomes SEVERE.

**2. Number and answer #75 and #77. — BLOCKED on the research lead, and on nobody having opened the D-xx.**
*Unblocks:* D-11's remaining two prerequisites; #75, #77, #78's remedies; §2.5.3 and §3.5.1 prose.
*Cost:* two decisions. If Morris is chosen, ≈410 ACO runs ≈ 13 min/arm — cost is not the constraint.
*Owner:* research lead to decide; `code-stressor` to execute; `editor` to reconcile.
*Leverage reasoning:* these cost minutes and gate the entire §3.5 path, yet **they are not in `DECISIONS.md`** — which is precisely the condition under which an item is quietly forgotten. Disagree if you would rather batch them into a single session with D-08 and D-10.

**3. Confirm D-06's diversity reframing (#46). — ACTIONABLE NOW.**
*Unblocks:* §3.1's argument, the Abstract, the Conclusion, #46, #91, and the framing half of cluster G. The structural claim — *"given a larger palette the optimizer converges to the same small set of high-performing species"* — survives Option-B renormalization, so it can be settled **before** any number regenerates.
*Cost:* one confirmation.
*Owner:* research lead, then `editor`.
*Leverage reasoning:* it is the only item that lets editorial work start ahead of the regeneration, and it changes what the paper argues rather than what it reports. Disagree if you would rather see regenerated §3.1 numbers first — defensible, but it idles the `editor` for the whole blocked period.

**4. Lock D-04 (title). — ACTIONABLE NOW.** One of two; the only DOI-blocking decision. *Leverage reasoning, stated so you can reject it:* D-04 unblocks exactly one thing, so by pure leverage it ranks below the three above — it is here because it is free, irreversible once minted, and nothing else in the queue can substitute for it later.

**5. Route D-13 to a time-boxed `code-stressor` session over `legacy/archive/`**, searching for §3.1's and §3.5's generator together. Gates nothing, but it is #97's escalation trigger in *both* directions: a pre-audit source makes §3.5 obsolete-not-impossible; no source makes it numbers of no known provenance, which is stronger than #82.

**Why #82, the only SEVERE, is not ranked 1–5.** Its remedy is already decided (D-11 option b) and that remedy is blocked behind items 1 and 2. There is no action available on #82 today that is not an action on #96, #75 or #77. Severity is an input to leverage, not a synonym for it. **Disagree here if you believe #82 warrants scoping §3.5 out of the preprint entirely** (D-11 option (c) was offered and not taken) — that is the one move that acts on #82 without waiting for anything, and it is the research lead's to make, not mine.

---

## 8. What changed since the last STATUS.md

Previous run: 2026-07-26, generated before Entries 8, 9 and 10. **The following statements in it are now false:**

- ❌ *"29 cleared · 2 deferred · 30 pending · 33 potential roadblock · 1 SEVERE = 95. Next free flag: #96."* → **97, next free #98.** #77 escalated PENDING → POTENTIAL ROADBLOCK; #96 and #97 created.
- ❌ *"Assign from #96"* (its §6, and the same instruction still in `FLAGS.md`) → **superseded. The references-and-appendices pass assigns from #98.** Left uncorrected, a future pass would collide with #96/#97.
- ❌ *"Four open [decisions]"* → **five**: D-12 authorized, D-13 opened.
- ❌ *"`math-auditor` should still report what `SensitivityAnalyzer` actually computes"* → **executed and DISCHARGED.** The aggregation is arithmetically correct; the working hypothesis that four uncorrelated overstatements implied a code defect is **overturned**. Do not re-run it.
- ❌ *"§3.5.1's parameter-level layer reproduces cleanly … the defect localizes to the aggregation step"* → superseded by #97: **§3.5.1 does not survive either.** Rank-1 becomes 28/40, executed rank-1 is `decay_lambda` (the parameter §3.5.2 dismisses), the category hierarchy inverts, and the headline effect's **sign** inverts. The manuscript's 12→34 m sweep bounds are not in the code (uniform ±20%).
- ❌ *"#75 … in flight to `math-auditor`"* → landed. Verdict is **(c)**: the code implements **neither** Morris nor a valid local OAT, so the old two-way question has no true answer.
- ❌ *"#77 (`n_runs` 3 vs 5)"* → reframed. `n_samples = 3` ≠ `n_runs = 5`; §3.5.1 is **accurate to the code**. What survives is a design inconsistency plus a confirmed capability gap (no dispersion is computed or storable).
- ❌ *"Cluster A … §3.5 is not the analysis Methods describes … #75 and #77"* → cluster A is now **#96, the state leak**, which outranks both in urgency and is different in kind (a code change, not a decision).
- ❌ *"Unrouted terminology conflict … `CLAUDE.md` §3 lists P as 'public'"* → **fixed** 2026-07-27 (commit `87d4528`); `CLAUDE.md` §3 now reads P = Prohibited.
- ❌ *"`CLAUDE.md` §2 rule 4 … state '#1–#41 assigned; next free number is #42'"* → that text is gone; rule 4 now says **#95 / next free #96**, which is still wrong by two. Re-flagged in §6.
- ⚠️ Its *"D-11 set [#82's] remedy, it did not apply it"* — **still true**, and now the amended expectation is that the remedy will **not** vindicate §3.5 either.

**New this run:** D-12 (authorized, unapplied), D-13 (open, unassigned), D-11's amendment, flags #96/#97, the discharge of `math-auditor`'s aggregation assignment, and one deliberately unregistered finding (STEP 7 → STEP 8 contamination, inferred not executed).
