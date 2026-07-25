# START HERE — SECPI Migration Plan (Windows / PowerShell)

> **📌 One-time setup runbook — not a live document.** Its job is done once Phase 0–2 are complete. No Claude Code session reads this file. If you set up on a second machine or onboard a co-author later, it's an accurate historical record of what worked — but don't expect it to reflect the project's current state; check `docs/STATE.md` for that instead.
>
> **One exception, 2026-07-25:** §2.4a was added after the freeze to document a real, confirmed environment trap (Python Install Manager runtimes) that cost significant debugging time and will recur for any co-author whose machine has the same setup. Worth breaking the freeze for; nothing else in this file has been touched since.

Everything you need, in order. All commands are PowerShell-native.

**Assumed present:** Claude Code (v2.1.0+), git, GitHub, ECC installed from prior work.
**Assumed unverified:** Python environment, ECC rule coverage for this stack.

---

## Phase 0 — Verify what you already have

### 0.1 Know which PowerShell you're on

```powershell
$PSVersionTable.PSVersion
claude --version
```

**This matters.** Windows PowerShell 5.1 (the built-in one) does **not** support the `&&` chaining operator — that arrived in PowerShell 7 (`pwsh`). Everything below is written to work on both: separate lines, no chaining. If you see `&&` in ECC's docs or my earlier messages, split it into two lines.

ECC requires Claude Code **v2.1.0 or later**.

### 0.2 ECC — verify, do not reinstall

**You almost certainly do not need to reinstall.** The plugin install is user-level, recorded in `$env:USERPROFILE\.claude\settings.json` under `enabledPlugins`, and applies to every project on the machine. Installing it for another project already installed it here.

```
/plugin list ecc@ecc
```

> **Naming note:** the canonical plugin identifier is `ecc@ecc`. Older documentation (including earlier drafts of this bundle) references the longer `everything-claude-code@everything-claude-code` — that form is a legacy alias only and may not resolve. If you already confirmed `ecc@ecc` is installed and enabled, you're done with this step; skip to 0.3.

If that lists agents, skills, and commands, skip to 0.3.

> **Windows note from ECC's own docs:** the Claude config directory is `%USERPROFILE%\.claude`, not `~/.claude`. PowerShell resolves `$HOME` correctly, but any instruction telling you to `cd ~/.claude` was written for Unix.

**⚠️ Do not run `.\install.ps1 --profile full` now.** If you originally used `/plugin install`, layering the full installer on top is the most common way to break ECC — it duplicates skills and runtime behavior. If anything looks duplicated from your prior project:

```powershell
Set-Location C:\path\to\everything-claude-code
node scripts/ecc.js list-installed
node scripts/ecc.js doctor
node scripts/ecc.js repair
```

Repair before reinstalling. ECC only touches files recorded in its own install-state.

### 0.3 ECC rules — confirmed working setup for this machine

**This section reflects what was actually verified on this install, not the generic docs.** The rules location and mechanism below were confirmed empirically, not assumed.

**Node.js requirement, confirmed.** ECC's hook runtime (`PreToolUse`/`PostToolUse`/`Stop` hooks, including a gating hook called **GateGuard**) runs through a Node-based subprocess. If Node isn't installed, hooks fail with `node: command not found` on every tool call — non-blocking, so the session still works, but the hook layer is dead.

```powershell
node --version
```

If missing:
```powershell
winget install OpenJS.NodeJS.LTS
```

**Then fully quit and relaunch Claude Code — do not `--resume` or `--continue`.** A new PowerShell window is not enough. The hook runner is a subprocess spawned at session start; it inherits PATH at that moment, so an already-running session (or one resumed from it) keeps the stale PATH even after Node is installed and even in a brand-new terminal. Only a genuine relaunch spawns a fresh subprocess that sees the update. Confirm with a cold command in the new session — not one recalling prior conversation:

```
Run node --version yourself, to confirm the hook runner sees it.
```

**Real rules location (confirmed, not `~/.claude/rules/ecc/`):**

```
~/.claude/rules/
├── everything-claude-code-guardrails.md
├── node.md
├── python.md            ← consolidated from the 6-file python/ library, matching node.md's flat pattern
└── common/               ← copied wholesale, 10 files, 17,347 bytes, byte-identical to source
    ├── agents.md  code-review.md  coding-style.md  development-workflow.md
    ├── git-workflow.md  hooks.md  patterns.md  performance.md
    ├── security.md  testing.md
```

Confirmed both flat files **and** the nested `common/` subfolder are read: a cold, out-of-context question in a fresh session ("what's our required test coverage minimum, and what test-naming convention do we follow?") returned the correct 80% threshold and AAA/behavior-naming convention sourced from `common/testing.md`, without being told where to look.

**Do not use `~/.claude/rules/ecc/`** — that path doesn't exist on a plugin install; it does not match how this system actually resolves rules.

A mirror also exists at `~/.claude/plugins/cache/ecc/ecc/2.0.0/.claude/rules/`, kept in sync as a byproduct of setup. **Treat that copy as disposable.** It sits inside a version-numbered plugin cache directory and can be silently wiped by an ECC update or reinstall. `~/.claude/rules/` is the durable copy; if the two ever diverge, `~/.claude/rules/` is authoritative.

> **On the consolidation itself:** `python.md` was built by merging six library files (coding-style, patterns, testing, security, hooks, fastapi) into one flat file, stripping their `../common/...` cross-links per file to match `node.md`'s existing flat pattern. Those links pointed at real content beyond the guardrails baseline — general engineering rules also used by every other language, now restored by the `common/` copy above. If you add another stack's rules later (e.g. `typescript/` for a future tooling need), the same two-step applies: consolidate the stack file into the flat directory, then confirm `common/` covers what its cross-links pointed to — don't assume it's already there.

**GateGuard, and shell commands generally.** Expect a hook named GateGuard to intercept and pause on shell commands throughout Stage 1 (`git init`, directory creation) and Stage 2 (`pip install`, venv activation) — asking for the command's purpose before allowing it. This is a working safety gate, not a malfunction; answer its prompt and it proceeds. It's unrelated to the `node: command not found` errors, which will stop appearing now that Node is installed and the session has been relaunched.

### 0.4 What to exclude — confirmed state for this install

**Verified counts (not the generic docs' figures):** `ecc@ecc v2.0.0` ships **67 agents, 278 skills**, measured directly from the installed plugin on disk. No official skill category taxonomy exists — the manifest stores skills as a flat array — but a thematic grouping shows roughly 18 clusters, the large majority irrelevant to this project: framework patterns (Django/Laravel/React/etc.), healthcare, Web3/trading, networking/homelab, business/logistics, content/marketing, media generation. None of that needs attention here; skills are not enabled/disabled individually the way MCP servers are, so there's nothing to trim on that front.

**MCP servers — confirmed and resolved.** `/mcp` showed exactly one: `plugin:ecc:chrome-devtools`, 29 tools, connected by default. Irrelevant to this project (browser/frontend debugging). Disabled via `/mcp` → select server → **`3. Disable`**.

**Confirmed scope of the disable:** project-only, persisted to `~/.claude.json` under the `secpi` project block (`disabledMcpServers: ["plugin:ecc:chrome-devtools"]`), verified by direct inspection of the config file — not a transient session toggle. Other projects using ECC on this machine are unaffected.

**Clusters actually worth knowing about for this project** (not disabling anything — just worth knowing they exist and what's in them):

| Cluster | Relevant to |
|---|---|
| Research / knowledge (`deep-research`, `scientific-db-*`, `scientific-thinking-*`, `iterative-retrieval`, `exa-search`) | Deriver's literature queue — Flags #9, #20, #26, #30 |
| Testing & TDD (`eval-harness`, `*-verification`) | code-stressor's regeneration and reproducibility gates |
| Code review & quality (`production-audit`, `coding-standards`) | math-auditor, the `src/secpi/` refactor |
| Learning / meta / instincts (`continuous-learning-v2`, `rules-distill`, `recursive-decision-ledger`, `growth-log`) | See §0.5 — the specific skill the continuous-learning caution below refers to |
| DevOps / harness / ECC-ops (`gateguard`, `safety-guard`) | The hook behavior you're already seeing on shell commands |

**Open question, not yet verified either way:** whether skill name+description metadata for all 278 skills sits in context by default for routing, or is genuinely zero-cost until a skill is invoked. If context starts feeling tight in later sessions, this is worth checking rather than assuming.

### 0.5 Continuous learning — confirmed mechanism, not just a caution

**Verified by reading the hook source directly (`evaluate-session.js`, one of six Stop hooks), not assumed from docs.**

`/ecc:instinct-status` confirmed the store was empty on first check. The mechanism explains why, and it's better than the general caution below originally assumed:

- **Six Stop hooks fire automatically** at the end of every session: JS/TS lint + console.log scan (irrelevant here, Python project), session persistence, `evaluate-session` (the continuous-learning touchpoint), cost tracking (the `~$8.48` notice), and a desktop popup.
- **`evaluate-session` does not extract or write anything.** It counts user messages; if the session is long enough (≥10 messages), it logs a signal that the session *might* be worth learning from, and exits. No model call, no file write, no homunculus store touched.
- **Actual extraction only happens via explicitly running `/ecc:learn` or `/ecc:evolve`.** Those are model-driven skills, not hooks — nothing runs them automatically.

**So the risk isn't passive background contamination — it's a specific pair of commands.** Practical rule: **don't run `/ecc:learn` or `/ecc:evolve` in this project.** Neither is needed for anything in the SECPI workflow, and it isn't yet confirmed what scope they'd operate over (this session only, vs. reaching across other projects' transcripts) — no need to find out.

**Separate scoping note, confirmed the same session:** instinct storage scope (project vs. global) depends on this directory being a git repo. Before `git init` (Phase 1.1), it resolves as **global** — shared with every other ECC project on the machine. After `git init`, it should scope to this project specifically. One more reason `.gitattributes` + `git init` happens first in Phase 1, before other setup continues.

**Regardless of mechanism, the standing rule holds:** an instinct — extracted deliberately or not — may never justify a manuscript claim. Only executed code and logged entries do that.

### 0.6 ECC surfaces worth using here — confirmed against this install

All four skills and both slash commands below were checked by exact name against the running install, not inherited from generic docs.

| Surface | Confirmed as | Use for |
|---|---|---|
| `deep-research`, `exa-search` | `ecc:deep-research`, `ecc:exa-search` | Deriver literature queue — Flags #9, #20, #26, #30 |
| `search-first` | `ecc:search-first` ✅ | Same |
| `documentation-lookup` | `ecc:documentation-lookup` ✅ | Library behavior during the refactor |
| `verification-loop` | `ecc:verification-loop` ✅ | Regeneration and reproducibility gates |
| `eval-harness` | confirmed in Testing & TDD cluster | Same |
| `strategic-compact` | `ecc:strategic-compact` ✅ | Long audit sessions |
| `iterative-retrieval` | confirmed in Research/knowledge cluster | Subagent context refinement |
| `/checkpoint` | real slash command, backed by `ecc:checkpoint` skill | Verification state between sessions |
| `/quality-gate` | real slash command, backed by `ecc:quality-gate` skill | Formatter/quality checks on a single file |
| `ecc:python-reviewer` | confirmed at agent #51 ✅ | Reviewing the modular refactor |

**Agent list confirmed: 67 real names, all `ecc:`-prefixed**, distinct from six built-in harness agents (`claude`, `Explore`, `general-purpose`, `Plan`, etc.) that aren't part of the ECC bundle.

Plugin installs use the namespaced form: `/ecc:plan "..."`.

**Model routing:** Sonnet by default; `/model opus` for the math audit and the Results rewrite.

---

## Phase 1 — Build the repo

### 1.1 Create and scaffold

If `secpi` doesn't exist yet:

```powershell
New-Item -ItemType Directory -Path secpi | Out-Null
Set-Location secpi
git init
```

**Scaffold the subdirectories** — run this whether or not the above already happened, it's idempotent:

```powershell
$dirs = @(
  "docs\proposals", "docs\citations", "docs\archive",
  "manuscript\sections", "legacy", "legacy\archive", "src\secpi",
  "results", "tests", ".claude\agents"
)
foreach ($d in $dirs) { New-Item -ItemType Directory -Force -Path $d | Out-Null }

Get-ChildItem -Recurse -Directory | Select-Object FullName
```

`New-Item -Force` is PowerShell's `mkdir -p` — creates intermediate directories, doesn't error if the path exists. The final `Get-ChildItem` is a self-check; confirm the tree actually matches Part 0.5 of `MIGRATION.md` before moving on rather than assuming the loop succeeded silently.

`legacy\archive` exists specifically for the **D-06 salvage triage** — it's where the recovered pre-audit script iterations get frozen and manifested, per `docs/DECISIONS.md`.

> **Running scaffolding in a second window, outside Claude Code:** fine, and often better for pure filesystem work like this. **GateGuard only intercepts commands run through the Claude Code session** — a separate raw PowerShell window bypasses it, which avoids friction on commands with zero judgment calls in them. Git doesn't care which window makes a commit; just make sure the second window's `Set-Location` lands in the same `secpi` directory already `git init`'d in the first, not a fresh duplicate.

### 1.2 Set line-ending policy before adding any files

**Do this now, not later.** `AuditedCode_1.py` already has CRLF line endings. If git's `autocrlf` converts them inconsistently, every diff fills with phantom whitespace changes — and your reproducibility gate ("does the modular version reproduce the legacy output?") gets buried in noise.

```powershell
@"
* text=auto eol=lf
*.py text eol=lf
*.md text eol=lf
*.pdf binary
*.png binary
"@ | Set-Content -Path .gitattributes -Encoding utf8

git config core.autocrlf false
```

Normalizing to LF in the repo keeps diffs clean. Python on Windows reads LF files without complaint.

### 1.3 Unpack the migration bundle

Drop in `CLAUDE.md`, `MIGRATION.md`, `START_HERE.md`, `docs\`, `manuscript\sections\`, `.claude\agents\`.

### 1.4 Place your existing files

```powershell
$src = "C:\path\to\your\downloads"   # adjust

Copy-Item "$src\MCS02_Pauling_Lacuanan_et_al_SECPI__1_.pdf" "manuscript\MCS02_SECPI_original.pdf"
Copy-Item "$src\AuditedCode_1.py" "legacy\"
Copy-Item "$src\LATEST_CODE.md"   "legacy\"
Copy-Item "$src\INITIALCODE.md"   "legacy\"
Copy-Item "$src\SECPI-Manuscript-Flag-Archive-v2.md" "docs\FLAGS.md"
Copy-Item "$src\SECPI-Manuscript-Flag-Archive.pdf"   "docs\archive\FLAGS_v1.pdf"
Copy-Item "$src\SECPI_normalization_and_stats_proposals.md" "docs\proposals\normalization_and_stats.md"
```

`docs\PROJECT_LOG.md` is already in the bundle — Entries 1–2 verbatim, the Entry 3 gap placeholder, Entry 4.

Preserve the v1 flag archive. Flag #2's history — external verification said *Albizia procera*, your own source data said *Albizia lebbeck*, and you were right — is provenance you may need to defend.

### 1.5 Populate the section files

Extract PDF text into `manuscript\sections\*.md` beneath each `<!-- PASTE ... BELOW -->` marker. Two-column academic PDFs extract badly and equations mangle. I can produce all nine populated files if you'd rather not do it by hand.

### 1.6 Layout check

```
secpi\
├── CLAUDE.md  START_HERE.md  MIGRATION.md  .gitattributes  .gitignore
├── .claude\agents\        5 subagent definitions
├── docs\                  DECISIONS · STATE · PROJECT_LOG · FLAGS · SESSION_PROMPTS
│   ├── proposals\  citations\  archive\
├── manuscript\
│   ├── MCS02_SECPI_original.pdf    🔒 frozen, never edited
│   └── sections\                   10 files — the editing workspace
├── legacy\                🔒 AuditedCode_1.py, LATEST_CODE.md, INITIALCODE.md
│   └── archive\           🔒 D-06 recovered iterations + MANIFEST.md
├── src\secpi\             target modular package (Stage 7)
├── results\               timestamped runs, never hand-edited
├── tests\                 test_reproducibility.py
└── .venv\                 gitignored
```

Full architecture, provenance zones, and file-placement conventions: `MIGRATION.md` Part 0.5.

---

## Phase 2 — Python environment

### 2.1 Verified dependencies

`legacy\AuditedCode_1.py` needs exactly:

| Package | Required? | Used for |
|---|---|---|
| `numpy` | **Hard** | Everything |
| `matplotlib` | **Hard** | All visualization |
| `scipy` | **Hard** | `scipy.spatial.distance.cdist` only — 5 call sites |
| `tqdm` | **Hard** | Progress bars |
| `pandas` | **Soft** | try/except-guarded; CSV features degrade, code still runs |

Stdlib: `itertools`, `warnings`, `os`, `datetime`, `json`, `copy`.

### 2.2 Create the environment

```powershell
python -m venv .venv
```

Note `python`, not `python3` — the `python3` alias generally doesn't exist on Windows.

**Activation may be blocked by execution policy.** This is the most common Windows Python snag:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

`RemoteSigned` at `CurrentUser` scope lets local scripts run without weakening machine-wide policy. If your school or organization locks execution policy, use the batch activator instead: `.\.venv\Scripts\activate.bat`.

```powershell
pip install numpy matplotlib scipy tqdm pandas
pip freeze | Out-File -FilePath requirements.txt -Encoding utf8
```

> **PowerShell 5.1 encoding trap:** plain `>` redirection writes **UTF-16LE**, which git treats as binary and pip can't read back. Always use `Out-File -Encoding utf8` or `Set-Content -Encoding utf8` when writing text files from 5.1. PowerShell 7 defaults to UTF-8 and doesn't have this problem.

```powershell
".venv/", "results/", "__pycache__/", "*.pyc" | Add-Content -Path .gitignore -Encoding utf8
```

### 2.3 Two defensive environment settings

```powershell
$env:PYTHONUTF8 = "1"
$env:MPLBACKEND = "Agg"
```

`PYTHONUTF8=1` forces UTF-8 for file I/O. Four `open()` calls in the code lack an explicit encoding; they write JSON, which `json.dump` escapes to ASCII by default, so they're probably safe — but Windows defaults to cp1252 rather than UTF-8, and this removes the risk for free.

`MPLBACKEND=Agg` selects the non-interactive matplotlib backend. The code has **zero** `plt.show()` calls and saves everything via `savefig`, so nothing will block — but Agg is faster and avoids GUI dependencies in batch runs.

Verified as safe on Windows: no hardcoded path separators anywhere, 29 uses of `os.path.join`.

### 2.4 🔴 Flag #45 — the stated software stack is wrong

Two Methods claims contradict the implementation:

| Manuscript says | Reality in `AuditedCode_1.py` |
|---|---|
| ACO implemented "via the **scikit-opt** Python library" (Abstract) | No `sko` import anywhere. Hand-implemented as `AntColonySystemACO`. |
| Heatmaps via "Matplotlib and **Seaborn**" (§2.4.2) | No `seaborn` import. matplotlib only. |

A reviewer attempting reproduction installs scikit-opt and finds nothing uses it. Reproducibility defect, not a wording nit.

Also: `itertools` is imported and never called — the fossil of the missing combinatorial analysis (Flag #43, D-06).

`geopandas`, `shapely`, `seaborn`, `scipy.stats` appear only in `INITIALCODE.md`, the superseded 70×70 pipeline. Don't install them.

**Register as #45, PENDING VERIFICATION.**

### 2.5 Smoke test

```powershell
python -m py_compile legacy\AuditedCode_1.py
if ($LASTEXITCODE -eq 0) { "compiles clean" } else { "COMPILE FAILED" }
```

Prior audits confirm this passes. `$LASTEXITCODE` is PowerShell's equivalent of checking `$?` in bash. **This only checks syntax — it never imports numpy, scipy, pandas, or matplotlib, so it will say "clean" even if package installation silently failed.** Run the import check in 2.4a below before trusting this line alone.

### 2.4a ⚠️ Known trap: Python Install Manager (PIM) runtimes are broken for this purpose

**Confirmed on this machine, 2026-07-25 — cost roughly a dozen debugging turns before being traced to the root cause.** If `python` resolves to a path containing `pythoncore-X.Y-64` (check with `python -c "import sys; print(sys.executable)"`), you are on a PIM-managed runtime, and venv creation will fail in a specific, escalating sequence:

1. **`python -m venv .venv` fails** with `No module named ensurepip` — the PIM runtime doesn't ship it.
2. **Workaround `--without-pip` + `get-pip.py` "succeeds"**, but silently doesn't — `-m pip` keeps resolving to a copy bundled directly in the base install's `Lib\pip` folder (not the normal `site-packages` location), which sits earlier on `sys.path` than the venv's own copy and permanently shadows it.
3. **Even after forcing pip to resolve correctly** (temporary `$env:PYTHONPATH` pointing at the venv's `site-packages`), package installs that happen to already exist in the base install's `Lib` (we hit this with `scipy` and `tqdm`) get skipped as "already satisfied" — landing outside the venv entirely, silently breaking isolation.
4. **Even past that**, `import pandas` fails with `No module named 'zoneinfo'` — a standard-library module missing from this base install, for reasons not fully diagnosed. This is where the runtime was abandoned as unfixable rather than patched further.

**Fix: do not use the PIM runtime at all. Install a conventional interpreter instead.**

```powershell
winget install Python.Python.3.14
```

**`py -0p` will *not* reliably show the new install** — it appeared to only enumerate PIM-registered runtimes on this machine, silently omitting the classic installer. Locate it directly on disk instead:

```powershell
Get-ChildItem "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python314\python.exe" -ErrorAction SilentlyContinue
```

If that's empty, broaden the sweep:

```powershell
Get-ChildItem -Path "C:\Users\$env:USERNAME\AppData\Local","C:\Program Files","C:\Program Files (x86)" -Recurse -Filter "python.exe" -ErrorAction SilentlyContinue -Depth 3 | Select-Object FullName
```

**Rebuild the venv using this path explicitly** — never bare `python` or `py`, both were shown to resolve unpredictably on a machine with multiple Python installs present:

```powershell
& "C:\Users\$env:USERNAME\AppData\Local\Programs\Python\Python314\python.exe" -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip --version          # should show a path INSIDE .venv\Lib\site-packages, not pythoncore-*
python -c "import zoneinfo; print('zoneinfo OK')"
```

Both must pass clean before proceeding to package installation. If either fails the same way, something more fundamental is wrong and this addendum's diagnosis doesn't apply — stop and reassess rather than keep patching.

**Do not uninstall the PIM runtime once this works.** Any salvaged environments in `legacy/archive/` (`*.venv`, `secpi_env`) declare it as their `home` in `pyvenv.cfg` — removing it would break those archived interpreters' ability to run at all, for no benefit.

### 2.4b Real import check (do this, not just the syntax smoke test)

```powershell
python -c "import numpy, scipy, pandas, matplotlib, tqdm; from scipy.spatial.distance import cdist; print('numpy', numpy.__version__); print('scipy', scipy.__version__); print('pandas', pandas.__version__); print('matplotlib', matplotlib.__version__); print('all imports OK')"
```

This is the actual Phase 2 finish line — confirms the packages are installed, importable, and specifically that `scipy.spatial.distance.cdist` (the one scipy symbol `AuditedCode_1.py` calls) resolves. `py_compile` passing without this does not mean the environment works.

### 2.6 Baseline commit

```powershell
git add -A
git commit -m "Migrate SECPI project from Claude Projects"
```

Everything after this is auditable.

---

## Phase 3 — Working model

**Three roles.** You are the **research lead** — you close decisions. The main Claude Code thread is the **orchestrator** — it delegates, synthesizes, commits, and may not close a decision or write manuscript prose. The five **subagents** investigate and report.

**Subagent returns are lossy.** Each runs in its own context and returns only a summary — precisely how Entry 3 was lost and the 2.94 error propagated. So: every subagent writes full findings to `PROJECT_LOG.md` *before* returning, and the orchestrator treats the log as authoritative over anything said in a return.

**Session hygiene.** Open by reading `CLAUDE.md`, `DECISIONS.md`, `STATE.md`, log tail. Close by appending a log entry, updating flags, moving new questions into `DECISIONS.md` as `D-xx`, and committing. `/compact` at breakpoints, never mid-task. `/clear` between unrelated sessions.

**The rule underneath everything:** if you assert a number, you ran the code that produced it this session, or you cite the log entry where someone else did.

---

## Phase 4 — Session sequence

Full prompts in `docs\SESSION_PROMPTS.md`.

| # | Session | Agent | Blocked by |
|---|---|---|---|
| 1 | Verify the migration | orchestrator | — |
| 2 | Flag Results/Discussion/Conclusion | `editorial-flagger` | — |
| 3 | Close the Entry 3 gap (#35, #38) | `math-auditor` | — |
| 4 | D-06 combinatorial recovery | orchestrator | — |
| 5 | Regenerate Results + Wilcoxon | `code-stressor` | D-02, D-03, D-07 |
| 6 | Editorial pass | `editor` | Session 2 |

Sessions 1–4 are unblocked now. Session 1 takes five minutes and is non-negotiable: if the orchestrator can't reconstruct the project from three context files, the migration failed and you want to know immediately.

---

## Phase 5 — Your decision queue

| ID | Decision | Effort |
|---|---|---|
| **D-06** | **Does the 63-subset script still exist?** | Phone call, not a repo task. **Start now.** |
| D-02 | Normalization ceiling (3.75?) + framing | One number, one framing choice |
| D-03 | Wilcoxon outcome metric — pre-specify one | One of two |
| D-07 | `k` notation — resolve the collision | One symbol |
| D-04 | Final title | One of two |
| D-05 | Keep or delete "Chebyshev space (ℤ²)" | Keep/delete |

**D-06 outranks everything.** D-02, D-03, D-07 gate how Results are *written*. D-06 determines whether §3.1 — and the Abstract and Conclusion claims resting on it — can exist at all. It needs no tooling: message your co-authors and ask **who ran the 63-subset sweep, and where is that script.**

---

## Critical path

```
D-06 answered ──→ §3.1 survives? ──→ Abstract & Conclusion headline claims survive?
                        │
D-02 ─┐                 │
D-03 ─┼──→ regenerate Results ──→ Editor writes Results ──→ Abstract rewrite ──→ EarthArXiv → DOI
D-07 ─┘                 │
D-04 ───────────────────┴──────────────────────────────────────────────────────→ DOI (title is permanent)
```

Deriver literature work (#9, #20, #26, #30) runs in parallel. **Flag #30 is the remaining schedule risk** — if no defensible H–D allometric equations exist for these six species, decide early whether to source a replacement or scope the allometric sensitivity out with a stated limitation.

---

## PowerShell quick-reference

For translating bash you encounter in ECC docs or anywhere else:

| bash | PowerShell |
|---|---|
| `mkdir -p a/b/c` | `New-Item -ItemType Directory -Force -Path a\b\c` |
| `cp -R src dst` | `Copy-Item -Recurse src dst` |
| `ls` | `Get-ChildItem` (`ls` is an alias) |
| `cat file` | `Get-Content file` |
| `grep pattern file` | `Select-String pattern file` |
| `export VAR=x` | `$env:VAR = "x"` |
| `source venv/bin/activate` | `.\.venv\Scripts\Activate.ps1` |
| `cmd1 && cmd2` | separate lines (PS 5.1) or `&&` (PS 7+) |
| `echo x > file` | `"x" \| Out-File file -Encoding utf8` |
| `$?` | `$LASTEXITCODE` |
| `/tmp` | `$env:TEMP` |
| `~/.claude` | `$HOME\.claude` or `$env:USERPROFILE\.claude` |
| `rm -rf dir` | `Remove-Item -Recurse -Force dir` |
