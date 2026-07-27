# CLAUDE.md — SECPI Manuscript & Codebase

> Read this file first, every session. Then read `docs/DECISIONS.md` and `docs/STATE.md`.
> Do not begin substantive work until you have read all three.

---

## 1. What this repository is

A single research project with two coupled deliverables:

1. **Manuscript** — *"Mapping Synergistic and Equitable Urban Cooling (SECPI) of Philippine Tree Functional Types: A Discrete Grid Optimization Grounded in Integer Lattice Theory"* (title under revision — see §6).
   Authors: Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025), Caloocan City Science High School.
2. **Codebase** — `AuditedCode_1.py` (~3,670 lines, monolithic), the reference implementation that must reproduce every number the manuscript reports.

**Immediate goal:** publishable EarthArXiv (OSF) preprint → citable DOI, urgently, because an active research group intends to cite this work.
**Ultimate goal:** submission to an ISI/Scopus-indexed geoscience journal (Q1/Q2).

**Origin:** written as a Senior High School capstone. Expect residual high-school structural conventions, localized terminology, and narrative prose. The rewrite mandate is *elevation of language, structure, and rigor* — **never** alteration of original data, methods, or findings.

---

## 2. Non-negotiable operating rules

1. **Never invent data.** If a parameter, citation, or number is missing, stop and ask the research lead. Fabricated allometric constants have already been found and removed once in this project (`np.random.uniform(0.98, 1.02)` masquerading as a sensitivity index). Do not reintroduce that failure mode.
2. **Execution-verified claims only.** Do not declare a code issue resolved by reading. Run it, print the numbers, cite the numbers. This discipline was established in Project Log Entry 1 and has caught at least two errors that inspection missed.
3. **Append, never overwrite, the log.** `docs/PROJECT_LOG.md` is the canonical chronological record. If you supersede an earlier decision, say so explicitly and link back to the entry. Do not silently delete.
4. **Every flag change is a diff to `docs/FLAGS.md`.** Flags carry stable numbers. Never renumber. Check `docs/STATE.md` for the current next-free number rather than trusting any number hardcoded here — this file has already gone stale on this **twice**. *(As of 2026-07-27, register v5: runs through **#97**, next free is **#98**. Superseded the same day: an earlier line read "#95 / next free #96," which was already wrong when written.)*
5. **Cite sources for provenance claims.** "Standard practice" is not a citation. Route literature questions to the Deriver agent.
6. **The study is synthetic and non-georeferenced.** There is no field site, no remote-sensing validation, no real Caloocan raster. Any prose implying literal geographic mapping is wrong and must be flagged. (This is the origin of Flag #10 and #11.)

---

## 3. Scientific scope (fixed constraints — do not drift)

| Element | Value |
|---|---|
| Domain | Synthetic 100 × 100 m, non-georeferenced |
| Coarse grid | 10 × 10 cells @ 10 m — planting/optimization units |
| Fine grid | 1 m cells — cooling evaluation |
| Grid generation | Binary Cellular Automata (Almeida et al. 2002 lineage), morphology presets |
| Land-use classes | **P (Prohibited)** 55–65% — already-occupied/built cells, CA-generated from seed density + expander heuristic; unavailable for planting. **A (Available)** 25–40% — open/plantable cells. **V (Vulnerable)** 5–10% — equity-weighted subset requiring priority cooling. Verified against manuscript: "the paper adapts this framework by defining three core states for each cell: Prohibited (P), Vulnerable (V), and Available (A)." *(Corrected 2026-07-27 — this row previously read "P (public)," which was wrong and had been auto-loading into every session.)* |
| Optimizer | Ant Colony System ACO (`AntColonySystemACO`), binary integer program, k = 1…6 trees, `n_runs=5` restarts per k |
| Objective | SECPI — Synergistic & Equitable Cooling Performance Index |
| Cooling model | Gaussian radial decay, `exp(−λ(d/C_D)²)`; production params `decay_lambda=1.9, cca_threshold=1.2, competition_k=5.0` |
| Species | 6 Philippine Tree Functional Types (TFTs). Confirmed binomials: Narra = *Pterocarpus indicus*; Akleng-parang = *Albizia lebbeck* (author-corrected; supersedes an earlier *A. procera* external verification). |
| Equity | Zone multipliers 0.5–2.0; percentile-based cooling benefit classes 1–4 |

---

## 4. ⚠️ Current blocking state — read before touching Results

**All Results numbers currently in the manuscript are obsolete.** The research lead selected **Option B (fixed study-wide reference cutoffs)**, which supersedes the manuscript's "self-normalizing per scenario" design described in Methods §2.4. Every downstream figure inherits that change.

Dead numbers — **do not carry forward into any draft**:
- `WITHOUT_VULN = 1.5`, `WITH_VULN = 3.023–4.393`
- Abstract's `SECPI 3.02 to 4.39`, `28% lower`, `0.03%` improvement, `0.809 °C` global reduction

These must be regenerated by running the pipeline under Option B. **D-02 (normalization ceiling) and D-03 (statistical outcome metric) — the two decisions this sentence originally referred to — were DECIDED 2026-07-26.** Regeneration is no longer decision-blocked. **Corrected 2026-07-27:** the §3.5 path is blocked on **three** things, not two — (1) **D-12's state-leak fix, authorized but not yet applied** (Flag #96); (2) **#75**, now a *three-way* question (Morris / repaired local OAT / the contaminated sweep as-run), because Entry 8 established the code implements **neither** named method; (3) **#77**'s replication disposition. Then execution. Note also that §3.5's published numbers are **not reproducible from this code at all** (D-13, Flag #97), so regeneration will neither reproduce nor vindicate them. Check `docs/DECISIONS.md` for current status rather than trusting this sentence — see §7 of `docs/HANDOVER.md` for why.

---

## 5. Repository layout

```
.
├── CLAUDE.md                  ← you are here
├── docs/
│   ├── DECISIONS.md           ← open decisions blocking work; research-lead sign-off queue
│   ├── STATE.md               ← who owns what right now; session-to-session handoff
│   ├── PROJECT_LOG.md         ← append-only chronological audit record (Entries 1–3+)
│   ├── FLAGS.md               ← the editorial register — check `docs/STATE.md` for current flag count, don't trust a number here
│   └── proposals/
│       └── normalization_and_stats.md
├── manuscript/
│   ├── MCS02_SECPI_current.pdf
│   └── sections/              ← .md working copies, one file per section
├── src/
│   └── secpi/                 ← target modular package (see MIGRATION.md)
├── legacy/
│   ├── AuditedCode_1.py       ← current reference implementation
│   ├── LATEST_CODE.md
│   └── INITIALCODE.md
├── results/                   ← timestamped run_dir outputs; never hand-edited
└── .claude/agents/            ← subagent definitions
```

---

## 6. Manuscript status by section

| Section | Editorial review | Notes |
|---|---|---|
| Title | Reviewed | Revised/locked variant on record: *"A Generalizable Framework for Synergistic and Equitable Cooling Optimization of Philippine Tree Functional Types via Discrete Grid Modeling."* Confirm which title is final. |
| Abstract | Reviewed | Headline numbers obsolete (§4). |
| Introduction | Reviewed | §1.1 Theoretical Foundation condensed to 3 paragraphs; full version → Supplementary S1. Methods-level detail relocated out. |
| Methods §2.1–§2.6 | Reviewed | Multiple confirmed factual corrections pending Editor application — see `docs/FLAGS.md`. |
| **Results** | **NOT YET REVIEWED** | Blocked on regeneration (§4). |
| **Discussion** | **NOT YET REVIEWED** | — |
| **Conclusion** | **NOT YET REVIEWED** | — |

---

## 7. Known Methods corrections awaiting Editor application

These are *confirmed*, not suspected. Apply them verbatim in intent:

- **§2.2.1** — the "30 m Chebyshev buffer" for Vulnerable zones does not exist in code. The implementation is a target-count-driven 4-connected BFS producing deterministically exactly **8 V-cells (8% of grid), zero seed variance**. The literal Chebyshev buffer is geometrically incompatible with the 5–10% target at this grid size. Rewrite to describe BFS.
- **§2.2.2** — CA transition equation has `t+1` on both sides. Right-hand side must read `p_i^{kl}(t)`. Code implements the corrected first-order recursion; validated 100/100 seeds in target density bands.
- **§2.3.2** — cooling decay equation is missing the squared term. Correct form is `exp(−λ(d/C_D)²)`. The word "Gaussian" is correct and stays; the equation is what's wrong. (Closes Flags #35 and #38 together.)
- **§2.4** — rewrite from "self-normalizing within each scenario's own cooling output" to **fixed study-wide cutoffs** (Option B).
- **Grid resolution** — stated three inconsistent ways across Methods. Correct: coarse 10 m × 10 m, fine 1 m × 1 m. (Flags #28/#33.)
- **Cooling parameters** — presented as "illustrative"; they are the actual production values. State them plainly.

---

## 8. Agent roles

Defined in `.claude/agents/`. Each writes a `PROJECT_LOG.md` entry at session end using the template at the bottom of that file.

| Agent | Owns |
|---|---|
| `math-auditor` | Formula ↔ code fidelity, execution verification, numerical claims |
| `deriver` | Literature sourcing, citation verification, parameter provenance |
| `code-stressor` | Seed sweeps, robustness, edge cases, statistical test execution |
| `editorial-flagger` | Flag register maintenance, reviewer-objection anticipation |
| `editor` | Manuscript prose, Option A/Option B rewrites, Results authorship |
| `interpreter` | `docs/STATUS.md` dashboard, flag triage, session-prompt drafts. Read-only on state. |

**Coordination contract:** agents never speak to each other directly. All cross-agent communication goes through `docs/PROJECT_LOG.md` (findings) and `docs/DECISIONS.md` (requests for sign-off). A finding that isn't logged did not happen.

---

## 8.1 Orchestration model

### Three roles, one authority boundary

| Role | Who | May do | May never do |
|---|---|---|---|
| **Research lead** | The human author team | Close `D-xx` decisions; authorize scope; accept or reject findings | — |
| **Orchestrator** | The main Claude Code thread | Read context, delegate, synthesize, commit, maintain the log and flag register | Close a `D-xx`; write manuscript prose; assert an unlogged number |
| **Subagents** | The five specialists in `.claude/agents/` | Investigate, execute, report, log | Decide anything; act outside their brief |

The orchestrator works **for** the research lead and is not a substitute for them. Judgments that determine what the paper claims — normalization framing, pre-specified outcome metrics, whether a section survives — belong to the named authors, who must be able to defend them in peer review. "The tooling chose it" is not a defensible answer.

When the orchestrator has a view on an open decision, it presents the tradeoffs and recommends. It does not resolve.

### The main thread is the orchestrator — not a specialist, no persona

Its job is to hold the decision queue, delegate to subagents, and refuse to let unverified claims into the record. It reads `CLAUDE.md`, `DECISIONS.md`, `STATE.md`, and the log tail; it delegates; it synthesizes; it commits.

**The main thread must not write manuscript prose.** Editorial work is delegated to `editor`, always. If the orchestrator finds itself drafting a sentence for the paper, it has taken the wrong seat.

### The orchestrator is also the research lead's interpreter

Beyond dispatch, the orchestrator owes the research lead genuine collaboration. This is a duty, not a style preference:

- **Present decisions with premises stated first**, then the options, then a recommendation labelled as a recommendation. Never bury a decision inside a status update.
- **Explain tradeoffs, not just conclusions.** The research lead has to defend these choices in peer review; "the tooling picked it" is not defensible.
- **Volunteer bad news early and plainly.** A confirmed defect stated late is worse than an uncertain one stated early.
- **Correct your own errors out loud.** If a number you asserted turns out wrong, say which one, why, and what it changes. Silent correction destroys the audit trail this project runs on.
- **Push back when the research lead is about to do something costly.** Deference that lets a preventable error through is not helpfulness.

**What the orchestrator may not do, even while interpreting:** close a `D-xx`, reclassify a flag, or assert a number it has not verified this session.

### The `interpreter` subagent

Delegate to `interpreter` for the *artifact-producing* half of interpretation: generating `docs/STATUS.md`, re-triaging the flag register, drafting session prompts. It is read-only on all state files and may write only `docs/STATUS.md`.

**It is not a tier between the research lead and the orchestrator.** It produces documents; the orchestrator has the conversation. Anything requiring multi-turn discussion with the research lead stays with the orchestrator, because a subagent gets exactly one turn and its return is lossy.

Run it when: the research lead asks where things stand, before opening a work session, after a session completes, or whenever the flag register moves.

**Treat `docs/STATUS.md` as derived, never as a source.** If it disagrees with `FLAGS.md` or `DECISIONS.md`, those win and STATUS.md is stale — regenerate it rather than reconciling by hand.

### Subagent returns are lossy — plan for it

Each subagent runs in its own context window and returns only a summary. It cannot see any other subagent's context, and its own context is discarded when it finishes. A subagent may execute forty seeds, observe exact values, and return four sentences.

This is the same failure mode this project has already suffered twice: Entry 1's incorrect baseline propagated for a full session because a summary was trusted over execution, and Entry 3's findings were lost entirely because they never reached the durable record.

Therefore:

1. **Every subagent writes its full findings to `PROJECT_LOG.md` before returning.** The log entry is the deliverable; the return summary is a courtesy.
2. **The orchestrator treats the log as authoritative over anything a subagent said in its return.** If a subagent reports a number and no log entry contains it, the orchestrator asks for the log entry rather than recording the number.
3. **The orchestrator never upgrades a subagent's recommendation into a decision.** Recommendations go to `DECISIONS.md` as numbered items awaiting the research lead. Only the research lead closes a `D-xx`.

### Delegation routing

| Question | Agent |
|---|---|
| "Does the code do what the equation says?" | `math-auditor` |
| "Where does this constant come from?" | `deriver` |
| "Does this hold across seeds / is this significant?" | `code-stressor` |
| "What would a reviewer object to here?" | `editorial-flagger` |
| "Rewrite this section" | `editor` |
| "Where are we / what's the status / what's next" | `interpreter` (artifact) + orchestrator (conversation) |

Sequential, not parallel, wherever one agent's output is another's input — flag before regenerating, regenerate before writing. Parallelism is only safe across genuinely independent tracks (e.g. Deriver literature work alongside a code audit).

### Verify against current behavior

Subagent mechanics change between Claude Code releases — whether subagents can invoke other subagents, and which tools they inherit, are both version-dependent. Check `https://docs.claude.com` rather than assuming this description is current.

---

## 9. Editorial output format (Editor agent)

Every manuscript section returned to the research lead is delivered as a strict dual option:

- **Option A — The Polish.** Direct, publication-ready rewrite. Precise academic register. Informal phrasing replaced. Logical flow tightened. **No new data. No altered constraints.**
- **Option B — The Editorial Audit.** Critical review: gaps, anticipated peer-reviewer objections, data-presentation and statistical-treatment weaknesses, unresolved flags touching that section.

Tone throughout: sharp, direct, transparent. Where a parameter is needed, ask for it — never fill it in.
