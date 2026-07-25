# SESSION_PROMPTS.md

Copy-pasteable prompts, in order. Each assumes you are in the repo root with Claude Code open.

Run them in sequence. Do not skip Session 1 — it is the cheapest possible check that the migration worked, and the most expensive thing to discover late.

---

## Setting up ECC first

**Everything Claude Code** (`affaan-m/everything-claude-code`, MIT, Anthropic hackathon winner) ships 48 agents, 182 skills, and 68 legacy command shims. Requires Claude Code CLI **v2.1.0+** — check with `claude --version`.

```
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install ecc@ecc
```

Then rules, which the plugin system **cannot** distribute — copy them by hand:

```bash
git clone https://github.com/affaan-m/everything-claude-code.git /tmp/ecc
mkdir -p ~/.claude/rules/ecc
cp -R /tmp/ecc/rules/common ~/.claude/rules/ecc/
cp -R /tmp/ecc/rules/python ~/.claude/rules/ecc/
```

### Three warnings that apply specifically to this project

**1. Do not stack install methods.** The repo names this as the most common broken setup: `/plugin install` followed by `install.sh --profile full`. Pick the plugin path and stop. If things look duplicated, use `node scripts/uninstall.js --dry-run` from the cloned repo rather than reinstalling on top.

**2. Install narrowly.** ECC is built for software engineering — React, Django, Spring Boot, Laravel, deployment, E2E testing. Almost none of that touches a geoscience manuscript. Every MCP server and skill description consumes context: the repo warns that too many MCPs can shrink a 200k window to ~70k. **Your project's core problem is state and context management.** Bloating the window with irrelevant tooling makes the exact thing you migrated to fix worse. Copy `rules/common` and `rules/python`; skip the rest until you want something specific.

**3. Consider disabling continuous learning for this repo.** ECC's `continuous-learning-v2` extracts "instincts" from sessions with confidence scores and stores them at `~/.claude/skills/learned/` — **cross-project, not scoped to this repo**. For a manuscript with strict provenance requirements, having auto-generated heuristics from unrelated coding work silently shape an editorial session is a real risk. If you keep it on, never let an instinct justify a manuscript claim; only the log and executable code do that.

If hooks feel too global, the minimal profile excludes the hook runtime entirely:
```bash
./install.sh --profile minimal --target claude
```

### What's actually worth using here

| ECC surface | Use for |
|---|---|
| `deep-research`, `search-first`, `exa-search` skills | Deriver literature work — Flags #9, #20, #26, #30 |
| `documentation-lookup` skill | Verifying library behavior during the refactor |
| `verification-loop`, `eval-harness` skills | Code-stressor regeneration and reproducibility gates |
| `strategic-compact` skill | Long audit sessions — suggests `/compact` at breakpoints instead of auto-compacting at 95% |
| `iterative-retrieval` skill | Subagent context refinement |
| `python-reviewer` agent | Reviewing the modular refactor |
| `/plan` (namespaced: `/ecc:plan`) | Planning the `src/secpi/` refactor |
| `/checkpoint`, `/quality-gate` | Saving verification state between sessions |

Note the namespacing: plugin installs use `/ecc:plan "..."`, manual installs use `/plan "..."`.

**Model routing:** default to Sonnet, switch with `/model opus` for the math audit and the Results rewrite — those are the two places deep reasoning earns its cost. ECC recommends `MAX_THINKING_TOKENS: 10000` and `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: 50` in `~/.claude/settings.json`.

---

## Session 1 — Verify the migration

> Read `CLAUDE.md`, `docs/DECISIONS.md`, and `docs/STATE.md`. Do not read anything else yet, and do not use any tools beyond reading those three files.
>
> Then tell me, in your own words:
> 1. What this project is and what the immediate deliverable is
> 2. The six decisions currently waiting on me, and which ones block which downstream work
> 3. Which manuscript sections have never been reviewed
> 4. Why every Results number currently in the manuscript is void
>
> If you cannot answer any of these from those three files alone, say exactly what is missing. Do not fill gaps by inference.

**Why this first.** If it can't reconstruct the situation from those three files, the context is wrong and you fix it now — before it costs you a real session. This is the whole thesis of the migration, tested in five minutes.

---

## Session 2 — Editorial flagging of Results, Discussion, Conclusion

> Use the `editorial-flagger` agent.
>
> Read `CLAUDE.md`, `docs/STATE.md`, `docs/FLAGS.md`, and the tail of `docs/PROJECT_LOG.md` (Entries 3 and 4 especially). Then review `manuscript/sections/06_results_discussion.md` and `07_conclusion.md`.
>
> These sections have never been editorially reviewed. Flags #43 and #44 were already found there by structural inspection alone, so assume more. Flag numbering continues from #45.
>
> For each flag: section, description, proposed classification, and what evidence would close it. Read as the harshest plausible Q1 geoscience reviewer. Do not soften findings to be encouraging.
>
> Update `docs/FLAGS.md` and append a log entry using the template. Do not renumber existing flags.

Use `/model opus` for this one.

---

## Session 3 — Close the Entry 3 provenance gap

> Use the `math-auditor` agent.
>
> `docs/FLAGS.md` cites "Project Log Entry 3" as the sole source for Flags #20, #26, #35, and #38 — but the log ends at Entry 2. See the Entry 3 placeholder in `docs/PROJECT_LOG.md`.
>
> Flags #35 and #38 concern the cooling decay function and are independently verifiable. Execute against `legacy/AuditedCode_1.py`:
> 1. Confirm the implemented decay is quadratic in distance, `exp(−λ(d/C_D)²)`, not linear
> 2. Re-derive the two calibration points (62% at crown edge, 15% at full crown diameter) and report the actual numbers you get
> 3. Confirm production parameters `decay_lambda=1.9, cca_threshold=1.2, competition_k=5.0`
>
> Report what you ran and what it printed. Do not assert anything you did not execute. Then re-source #35 and #38 to your new entry and mark the Entry 3 placeholder RETIRED — do not delete it.
>
> #20 and #26 are queue assignments with no analytical content; note them for re-issue to the Deriver.

---

## Session 4 — D-06 salvage triage

**Updated with concrete findings from the actual salvage** — the recovered directory is far larger than anticipated: 5 `.py` files (`CA.py`, `CODE020526.py`, `GEMINI.py`, `dashboard.py`, `secpi_main.py`) and dozens of run-output directories under three naming conventions (`corrected_outputs/`, `secpi_outputs/`, loose `run_*`), spanning two date clusters (mid-Feb 2026, and July 19 — the same day as Entry 2's audit).

> Use the `math-auditor` agent. Read `docs/DECISIONS.md` D-06 in full first.
>
> `legacy/archive/` contains recovered material already committed unmodified: 5 Python scripts and dozens of run-output directories.
>
> **Priority 1 — inspect `corrected_outputs/run_20260213_222844/combinatorial/` first.** It contains `all_combos_with_vuln.csv`, `all_combos_without_vuln.csv`, `combinatorial_summary.json`. Check row counts (looking for ~63), column structure, and whether any values match the published Results §3.1 numbers: SECPI 4.3916 (rank 3/63), 4.3856 (rank 27/63), marginal deltas 0.6291/0.6283, threshold 3.13. This may be stored *output* of the missing combinatorial sweep, not just a candidate script — treat it as the highest-value lead.
>
> **Priority 2 — inventory all 5 `.py` files by signature:** for each, check for a combinatorial/subset-sweep class, `itertools` used (not just imported), 63-subset or six-species references, and whether any of them could have produced the `combinatorial/` output above.
>
> **Priority 3 — note the `1_species` through `5_species` folder pattern** (in `run_20260219_004451`, `_005059`, `_010340`). This may represent a species-*count* sweep distinct from both subset-size and tree-count meanings of `k` — flag as a possible third D-07 variable, don't resolve it yourself.
>
> **Priority 4 — use directory naming and dates as forensic signal, not proof.** `corrected_outputs/` vs `secpi_outputs/` vs loose `run_*` likely indicates different script versions or sessions. The July 19 runs share a date with Entry 2's audit — note this, but confirm audit-boundary status per Step C below rather than inferring from the date alone. A folder called "corrected" is not evidence of correctness; that's exactly what verification is for.
>
> **Step: date the winning candidate against the audit boundary.** For whichever script/output combination best matches §3.1, check individually: the tie-inversion fix, `SensitivityAnalyzer` reading `base_aco_config` rather than hardcoded 10 ants/15 iterations, absence of the fabricated `np.random.uniform(0.98, 1.02)` allometric sensitivity, the corrected CA transition formula, and which SECPI normalization scheme is in use.
>
> **State the outcome** as (a) post-audit, (b) pre-audit — numbers reproducible but wrong — or (c) no reproduction, per the D-06 table. Do not modify any file in `legacy/archive/`. Expand `legacy/archive/MANIFEST.md` to cover the run-output directories, not just the `.py` files. Append a full `PROJECT_LOG.md` entry.

Use `/model opus`.

---

## Session 5 — Regenerate Results (blocked until D-02, D-03, D-07 are settled)

> Use the `code-stressor` agent.
>
> Prerequisites — confirm all three are recorded as DECIDED in `docs/DECISIONS.md` before starting, and stop if any is not: D-02 (normalization ceiling), D-03 (Wilcoxon outcome metric), D-07 (`k` notation).
>
> Then:
> 1. Apply the goalposts change to `normalize_secpi()` using the confirmed ceiling. Reporting layer only — the ACO continues to optimize on raw SECPI.
> 2. Run the full pipeline under Option B fixed cutoffs. Write to a timestamped `results/` directory. Record the seed.
> 3. Run the paired Wilcoxon signed-rank test on the pre-specified metric only. n=30, paired on grid and k. Report statistic, n, two-sided p, and matched-pairs rank-biserial effect size.
> 4. Re-check the goalpost ceiling against the optimizer's actual best. If solutions pin at 5.0, say so — do not silently adjust.
>
> Report distributions, not single runs. Zero variance is a finding. Never tune a parameter to improve a result.

---

## Session 6 — Editor, first substantive pass

Run only after Session 2 has flagged Results and you have decided what survives.

> Use the `editor` agent. Read your scope-of-authority section carefully first — the research lead has authorized unrestricted structural and rhetorical change, but no change to data.
>
> Start with `manuscript/sections/02_methods_2.1_2.2_grid.md`. The six confirmed corrections there are unblocked.
>
> Deliver **Option A** (publication-ready rewrite) and **Option B** (editorial audit) together. In Option B, name every structural decision you made and why.

Sections in order of readiness: `02` → `05` → `04` (after D-02) → `03` (after Flag #30) → `01` → `06`/`07` (after regeneration) → `00` last.

---

## Standing session hygiene

Open every session by reading `CLAUDE.md`, `docs/DECISIONS.md`, `docs/STATE.md`, and the tail of `docs/PROJECT_LOG.md`.

Close every session by appending a log entry, updating flag statuses, moving any new question into `DECISIONS.md` as a numbered `D-xx`, and committing.

Use `/compact` at logical breakpoints — after an audit completes, before writing prose. Not mid-task; you'll lose file paths and partial state. Use `/clear` between genuinely unrelated sessions.

**The rule that makes all of this work:** if you assert a number, you ran the code that produced it in this session, or you cite the log entry where someone else did. Nothing else counts.
