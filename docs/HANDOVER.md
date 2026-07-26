# SECPI Project — Handover Package

**For:** the next chat, continuing as research collaborator + interpreter.
**From:** the migration/setup session (2026-07-24 → 07-26).
**Read this once, fully, before doing anything. It is designed to be the only context you need to start.**

---

## 0. Who you are and how to behave

You are a research collaborator and technical interpreter for a senior-high-school STEM manuscript being elevated to a citable EarthArXiv preprint, then an ISI/Scopus geoscience journal. The research lead is **Gab** (Gabriel Lacuanan), lead author.

The single most important behavioral rule, learned the hard way across this entire project:

> **Verify, do not assume. If you assert a number, you ran the code or read the file that produced it — this turn. Never inherit a claim from a summary, including your own earlier summaries.**

This discipline caught, in one session: a stale plugin ID, a self-contradicting state file, a false "compiles clean," a shadowed pip install, a mislabeled flag total (51 that summed to 52), and — most importantly — a manuscript flag the authors' own numbers confirm. Every one was found by checking, not trusting. Hold this line.

Other standing behaviors:
- Present decisions to Gab with premises stated first; **you do not make design decisions unilaterally.** Gab closes decisions; you investigate and recommend.
- When you spot-check a claim and it fails, say so plainly, including when the failed claim is your own.
- Be direct about bad news. The value you add is catching problems before a reviewer does.
- Don't over-format. Prose over bullet-walls. Gab reads on mobile sometimes.

---

## 1. What the project is

**Manuscript:** *A Generalizable Framework for Synergistic and Equitable Cooling Optimization of Philippine Tree Functional Types via Discrete Grid Modeling* (title still under decision — see D-04).

Authors: Lacuanan, Valenzuela, De Leon, Villadolid, Valdes, Suarez (2025), Caloocan City Science High School.

**What it does:** a theoretical computational framework placing urban trees on a synthetic grid to optimize cooling *and* equity, via Ant Colony Optimization, scored by a novel index (**SECPI** — Synergistic and Equitable Cooling Performance Index).

**Critical scope fact:** the study is **synthetic and non-georeferenced.** No real site, no field validation, no remote sensing. Any prose implying literal geographic mapping is a defect.

**Immediate goal:** publishable EarthArXiv preprint → citable DOI, urgently (another research group wants to cite it).
**Ultimate goal:** Q1/Q2 ISI/Scopus geoscience journal.

**Six species:** Narra (*Pterocarpus indicus*), Talisay (*Terminalia catappa*), Banaba (*Lagerstroemia speciosa*), Kabiki (*Mimusops elengi*), Duhat (*Syzygium cumini*), Akleng-parang (*Albizia lebbeck* — author-confirmed, supersedes an external *A. procera* correction; **author source data always wins over external verification**).

---

## 2. The repository (already built and on GitHub)

Private repo: `github.com/gabskified/secpi`, local at `C:\Users\Administrator\GabskifiedProjects\secpi`. Co-authors will get **Read-only** access.

```
secpi/
├── CLAUDE.md              ← auto-loads into every Claude Code session + subagent. THE rules file.
├── START_HERE.md          ← frozen setup runbook (PowerShell). Not live. Includes the PIM-Python trap (§2.4a).
├── MIGRATION.md           ← frozen master plan snapshot. Not live.
├── .claude/agents/        ← 5 subagent definitions (see §5)
├── docs/
│   ├── DECISIONS.md        ← LIVE. Research-lead decision queue (D-01…D-10)
│   ├── STATE.md            ← LIVE. Ownership board + authoritative flag counts
│   ├── PROJECT_LOG.md      ← LIVE, append-only. Entries 1–5.
│   ├── FLAGS.md            ← LIVE. The 74-flag register (v3, truncated at #74)
│   ├── SESSION_PROMPTS.md  ← copy-paste prompts for Sessions 1–6
│   ├── data/SECPI_HD_field_data.csv  ← 211 field records (Deriver's allometric refit source)
│   ├── proposals/          ← normalization/stats + p0 provenance
│   └── archive/FLAGS_v1.pdf
├── manuscript/
│   ├── MCS02_SECPI_original.pdf   ← FROZEN, never edited (provenance anchor)
│   └── sections/                  ← 9 section files, populated verbatim (byte-identical to source, verified)
├── legacy/
│   ├── AuditedCode_1.py           ← current reference implementation (~3,670 lines)
│   ├── LATEST_CODE.md, INITIALCODE.md
│   └── archive/                   ← D-06 salvage: 5 recovered scripts + run-output dirs + 2 stale venvs
├── src/secpi/             ← empty; target for the eventual refactor (Stage 7, not started)
├── results/               ← gitignored; regeneration output goes here
├── tests/                 ← empty
└── .venv/                 ← gitignored; WORKING (Python 3.14.6 classic installer)
```

**Provenance zones (which files you may touch how):**
- 🔒 **Frozen:** `manuscript/*.pdf`, `legacy/`, `docs/archive/` — never edit, they're evidence.
- 📝 **Workspace:** `manuscript/sections/`, `src/`, `tests/` — freely edited.
- 📓 **State:** `docs/*.md` — append/update per rules; `PROJECT_LOG.md` append-only; flags never renumbered.
- ⚙️ **Generated:** `results/` — execution only, never hand-edited (a hand-edited result is indistinguishable from a fabricated one).

---

## 3. How the workflow actually operates

**Three roles, one authority boundary:**
| Role | Who | May | May never |
|---|---|---|---|
| Research lead | Gab | close decisions, authorize scope | — |
| Orchestrator | the main Claude Code thread | delegate, synthesize, commit | close a decision, write manuscript prose, assert an unlogged number |
| Subagents | the 5 specialists | investigate, execute, report, log | decide anything |

**Sessions ≠ windows.** "Session 1–6" in `SESSION_PROMPTS.md` are *tasks* you copy-paste, one at a time, into a single Claude Code window. Subagent delegation happens automatically inside that window when a prompt says "Use the X agent." **You never need more than 2 windows** (one Claude Code, one raw PowerShell for filesystem work). `/clear` or fresh window between different sessions.

**Subagent returns are lossy** — each runs in its own context and returns a summary. This is why every subagent must write full findings to `PROJECT_LOG.md` *before* returning, and why the orchestrator treats the log as authoritative over anything a subagent says in its return. (This is not theoretical: Entry 3 was lost this way once, and Session 2's flagger crashed mid-task — see §7.)

**Environment gotcha (already solved, documented in START_HERE §2.4a):** this machine has a Python Install Manager runtime that is broken for venvs (missing `ensurepip`, shadowed pip, missing `zoneinfo`). The working `.venv` was built from the *classic* installer at `C:\Users\Administrator\AppData\Local\Programs\Python\Python314\python.exe`. Always call venv Python by full path if anything Python-related misbehaves.

---

## 4. The migration timeline (what happened, compressed)

The project began as a Claude Projects setup with separate chats (Math Auditor, Deriver, Stressor, Editorial Flagger) coordinating through a shared log — which failed because nothing *enforced* reading the log. Migration to Claude Code fixed that: `CLAUDE.md` auto-loads, so state is unavoidable rather than advisory.

Phases completed this session:
- **Phase 0** — environment verified: PowerShell 5.1, Claude Code 2.1.218, ECC plugin `ecc@ecc` v2.0.0 (67 agents / 278 skills), rules at `~/.claude/rules/`, Node installed, continuous-learning confirmed opt-in only. Six doc corrections caught by verification.
- **Phase 1** — repo scaffolded, `.gitattributes`/line-endings set, all files placed, manuscript split verbatim (byte-identical, SHA-verified), pushed to private GitHub.
- **Phase 2** — working Python venv (after the PIM-runtime detour).
- **Session 1** — passed: an agent reconstructed the whole project from 3 files cold. Also caught a self-contradicting `STATE.md` (two different flag totals), since reconciled.
- **Session 2** — editorial flagging of Results/Discussion/Conclusion. **Crashed mid-task** (laptop freeze) after writing `FLAGS.md` but before the log/commit completed. Recovered by a follow-up orchestrator session. This is the session that found the big problems.

Entries 1–2 are the original auditors' work (verbatim). Entry 3 (Deriver) was recovered from a standalone file and independently re-verified against raw data. Entry 4 is the migration. Entry 5 is the interrupted-then-recovered Session 2.

---

## 5. The five subagents

Defined in `.claude/agents/`. Each writes a `PROJECT_LOG.md` entry at session end.

- **math-auditor** — formula↔code fidelity by *execution*, numerical plausibility.
- **deriver** — literature sourcing, citation verification, parameter provenance. (Strongest track record; self-corrected its own recommendation once.)
- **code-stressor** — seed sweeps, robustness, statistical tests, Results regeneration.
- **editorial-flagger** — the flag register, reviewer-objection anticipation.
- **editor** — manuscript prose; always returns Option A (polish) + Option B (audit). **Authorized for unrestricted structural change, but NEVER data change.**

Recommended models: Opus for math-auditor and editor and the flagging passes; Sonnet for stressor/deriver.

---

## 6. Decisions (7 open, need Gab)

Full detail in `docs/DECISIONS.md`. Summary:

| ID | Decision | Status |
|---|---|---|
| D-01 | Option B fixed study-wide SECPI cutoffs | ✅ DECIDED |
| D-02 | Normalization goalpost ceiling (~3.75) + framing | 🔴 OPEN, blocks Results |
| D-03 | Wilcoxon outcome metric — pre-specify ONE (cooling-in-V vs trees-near-V) | 🔴 OPEN, blocks Results |
| D-04 | Final title | OPEN |
| D-05 | "Chebyshev space (ℤ²)" — keep or delete | OPEN |
| D-06 | Combinatorial analysis | ✅ RESOLVED — output located, outcome (b): reproducible but superseded, must regenerate |
| D-07 | `k` notation — now a THREE-way collision (subset size / tree count / available-palette size) | 🔴 OPEN |
| D-08 | Assumed heights beyond observed range (Narra 30 m ⇒ DBH 244.5 cm vs 117.2 cm observed max) | OPEN |
| D-09 | Path X (hardcoded LAI canonical) | ✅ DECIDED |
| D-10 | `p0 = 1.0`, absorb into γ | OPEN, recommendation ready |

**Citation correction already logged (from D-02):** do NOT cite World Bank "distance to frontier" — Doing Business was discontinued 2021 for data-integrity reasons. Use Cedefop European Skills Index + OECD/JRC 2008 Handbook + UNDP HDI instead.

---

## 7. CURRENT STATE — the flag register

**74 live flags** (authoritative, per-flag enumerated in `STATE.md`):
- 29 Resolved-Cleared · 2 Resolved-Deferred · 25 Pending Verification · **18 Potential Roadblock** · **1 Roadblock (SEVERE)**
- Next free flag: **#75**

Session 2 added #52–#74 (23 flags) from the first-ever editorial read of Results/Discussion/Conclusion, and escalated #39 and #44. **Four were independently spot-checked against the manuscript this session and all four held** (#52, #64, #67, #75). That materially raises confidence in the batch — but the batch is not each-flag-verified.

**⚠️ Two integrity notes carried in the register:**
1. **Entry 5 / v3 is TRUNCATED at #74.** The flagger crashed before deriving #75–#94 (§3.5 tail + Conclusion). The SEVERE flag is *described* as #75 in the log narrative but the register formally stops at #74. **The first job in the next session is completing this derivation** — see §8 step 1.
2. **Flag #64's attestation is wrong (finding is right).** It claims all six k=1 monoculture values come from §3, but two (Kabiki 3.094, Banaba 3.068) come only from the recovered CSV via D-06. The arithmetic conclusion (mean 3.514 ≠ manuscript's 2.990) is verified correct; the *source citation* needs fixing. Don't let the wrong attestation discredit the right finding.

---

## 8. TRIAGE OF THE 74 — what the next chat should actually do

The register is a **map, not a to-do list to clear today.** Sorted into three buckets by urgency for the *preprint* (not the eventual journal):

### BUCKET A — Blocks the preprint. Must resolve before a DOI is minted.

**A1 — The SEVERE flag (#75): §3.5 category-mean SI of 1.3068 is arithmetically impossible.**
SI is defined as normalized (∈[0,1]); the largest single value is 0.4435; a "mean" of 1.3068 exceeds both its largest member and the [0,1] bound. It's labeled a mean but behaves like a sum. *Verified this session.* This is a desk-reject / retraction risk if it ships. Needs a research-lead decision (propose **D-11**): relabel sum-vs-mean, or re-run the sensitivity aggregation.

**A2 — The "noise-vs-effect" cluster (#64, #65, #67, #68).** The manuscript treats a difference as a real effect when it supports the headline and as noise when it doesn't. Root cause: **the run-to-run SD of the ACO is never quantified anywhere.** Half these flags dissolve or harden depending on that one unmeasured number. → This is a **code-stressor** job: measure the ACO's restart variance. It's also entangled with D-02/D-03. Nothing in Results can be honestly rewritten until this number exists.

**A3 — Circularity (#69, escalation of #39): the framework's validation uses its own objective function as the outcome variable.** The "significant" equity result is guaranteed by construction. Needs the Wilcoxon redesign (D-03) with an *independent* outcome metric (proportion of cooling delivered to V-zones, not SECPI itself).

**A4 — The mis-stated diversity claim (#46, #54, #65).** "Functional diversity offers negligible benefit" is not what the data shows — the optimizer used the full palette in only ~30% of configs; when offered six species it often planted two. The honest, better-supported claim: *a larger palette converges to the same small high-performing set.* Reframing is mandatory. (Gab has authorized unrestricted structural rewrite for exactly this kind of thing.)

### BUCKET B — Fix before submission, but doesn't block the DOI.

- **Internal-inconsistency flags** (#52, #57, #60, #61, #62, #63): the same quantity reported multiple incompatible ways (crown diameters, ACO config, species composition, cooling-field stats, °C vs dimensionless). Mechanical but numerous; each needs the manuscript reconciled to one authoritative value.
- **Empty/underspecified sections** (#56: §3.2.1/§3.2.2 have no prose; #58: ACO hyperparameters appear in Results but never in Methods).
- **The allometric problems** (D-08, Flag #48, #30's remaining 3 species): assumed heights beyond calibration; no field data for Duhat/Kabiki/Akleng-parang.
- **Methods corrections already confirmed** (6 of them, ready for the editor: BFS not Chebyshev buffer, CA equation `t+1` both sides, missing squared term in decay, grid resolution stated 3 ways, etc.).

### BUCKET C — Disclose as limitation, or defer to the journal version.

- Software-stack misattribution (#45: scikit-opt/Seaborn credited but unused).
- Terminology/provenance items (#26 expander heuristic, #21/#22 citation-form errors, "PTM-2" mystery source in #20).
- Numbering error (#51: §3.5's 3.4.2/3.4.3 reuse).

### The single most leveraged next action

**Measure the ACO's run-to-run variance (SD across restarts).** It's one code-stressor session, it needs the working venv (which exists), and it unblocks A2, informs A3, and is a prerequisite for D-02/D-03 and any honest Results rewrite. More flags collapse against this one number than any other single action.

---

## 9. Recommended sequence for the next chat

1. **Finish Entry 5's derivation (#75–#94).** Re-run the flagger against §3.5 (lines 597–725 of `06_results_discussion.md`) and the Conclusion, assigning from #75. Confirm the SEVERE flag formally. Then commit the completed register — it's currently uncommitted/interrupted.
2. **Fix Flag #64's attestation** (right finding, wrong source citation).
3. **Raise D-11** for the SEVERE sensitivity-table decision.
4. **Run the ACO variance measurement** (code-stressor). This is the keystone.
5. **Then** Gab tackles D-02/D-03/D-07 with a real noise floor in hand, and the editor can begin honest Results reconstruction.

Do NOT try to "fix all 74." Triage, sequence, and keep the research lead deciding.

---

## 10. What to ask Gab for at the start

- The current `docs/FLAGS.md`, `docs/STATE.md`, `docs/PROJECT_LOG.md` (he manages these; they're the live truth and may have moved past this handover).
- Confirmation of which sessions have run since this handover.
- Whether the interrupted Entry 5 register was ever committed.

Then read `CLAUDE.md` and `docs/DECISIONS.md` from the repo before doing anything substantive. **Verify against the files; don't trust this handover as current — it's a snapshot dated 2026-07-26, and this project's whole discipline is checking snapshots against reality.**
