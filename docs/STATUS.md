# STATUS — SECPI

**Generated:** 2026-07-26 (initial, by the migration session — subsequent runs by `interpreter`)
**Derived from:** `docs/FLAGS.md` (v3, truncated at #74), `docs/STATE.md`, `docs/DECISIONS.md`, `docs/PROJECT_LOG.md` Entries 1–5

---

## 1. Headline

The first editorial pass over Results/Discussion/Conclusion is complete and it found serious, systemic problems — 18 potential roadblocks and the project's first SEVERE flag, in sections that had never been reviewed. The preprint cannot ship until the SEVERE arithmetic defect in §3.5 is resolved and the ACO's run-to-run variance is measured. **Next action: finish the interrupted flag derivation (#75–#94), then measure ACO restart variance — that single measurement resolves or hardens four separate flags.**

---

## 2. Preprint readiness

| Gate | Status |
|---|---|
| Repository, environment, manuscript sections | ✅ Done, verified |
| Every section has had an editorial pass | ⚠️ §3.5 tail + Conclusion still uncovered (register truncated at #74) |
| No SEVERE flags outstanding | 🔴 One confirmed (§3.5 category-mean SI) |
| Results numbers regenerated under Option B | 🔴 Not started — blocked on D-02, D-03, D-07 |
| Statistical claims have tests behind them | 🔴 No test has been run; §3.4.4's validation is circular |
| Headline claims match what the data shows | 🔴 Diversity claim mis-stated (#46) |
| Title locked | ⬜ D-04 open |

---

## 3. Decisions awaiting the research lead

| ID | What | Blocks | Effort |
|---|---|---|---|
| **D-02** | Normalization ceiling (~3.75?) + framing | Writing any Results number | Pick a number |
| **D-03** | Wilcoxon outcome metric — cooling-in-V **or** trees-near-V | The entire significance claim | One of two |
| **D-07** | `k` notation — three-way collision | Results prose coherence | Pick symbols |
| **D-08** | Re-anchor assumed heights, or disclose extrapolation | Crown geometry → all cooling numbers | One of two |
| **D-10** | `p0 = 1.0`, absorb into γ | CA generation code | Yes/no, recommendation ready |
| **D-11** *(proposed)* | §3.5 sensitivity table: relabel sum-vs-mean, or re-run | The SEVERE flag | Needs a session first |
| D-04 | Final title | DOI minting (permanent) | One of two |
| D-05 | "Chebyshev space (ℤ²)" keep/delete | Nothing structural | Keep/delete |

**Critical path: D-02 + D-03 + D-07** — all three gate the Results rewrite, and settling them before regeneration avoids running it twice.

---

## 4. Key flags — grouped by root cause, not by number

**🔴 SEVERE — §3.5 category-mean SI is arithmetically impossible.**
SI is defined as normalized (∈[0,1]); the largest single value is 0.4435 (Narra crown diameter); the reported Species Morphology "mean" is **1.3068**. A mean cannot exceed its largest member, and a normalized index cannot exceed 1.0. It is labelled a mean but behaves like a sum. *Independently verified against the manuscript 2026-07-26.* Formally unregistered — the flagger crashed before writing #75.

**Cluster A — unquantified ACO variance** (#64, #65, #67, #68).
Four flags, one root cause: the manuscript never measures run-to-run SD, so it treats a difference as a real effect when it supports the headline and as noise when it doesn't. §3.4.2 dismisses 0.0014 as noise; §3.4.3 attributes causation to 0.067 and 0.0396 — all below the 0.05–0.07 best-vs-average gap §3.3.1 itself reports. **One measurement collapses or hardens all four.**

**Cluster B — circular validation** (#69, escalating #39).
§3.4.4 validates the framework using the framework's own objective as the outcome variable. SECPI_WITH > SECPI_WITHOUT is algebraically guaranteed by the weight manipulation. Also quotes the software's own hardcoded verdict string as confirmation.

**Cluster C — internal inconsistency** (#52, #57, #60, #61, #62, #63).
Same quantities reported multiple incompatible ways: crown diameters (34 m vs 23 m), ACO config (50×100 vs 15×30 — an 11× difference in evaluations), best-solution species composition (stated three different ways), and a dimensionless index relabelled °C with no calibration anywhere.

**Cluster D — mis-stated headline claim** (#46, #54).
"Functional diversity offers negligible benefit" is not what the data shows. The optimizer used its full palette in only ~30% of configurations; offered six species, the rank-1 result planted two. The defensible claim is different and better: *a larger palette converges to the same small set of high performers.*

---

## 5. Triage buckets

**A — blocks the preprint:** the SEVERE flag; Cluster A (needs the variance measurement); Cluster B (needs D-03's independent metric); Cluster D (needs reframing).

**B — fix before submission, not before DOI:** Cluster C; the six confirmed Methods corrections; the allometric problems (D-08, #48, #30's three unsourced species); empty §3.2 subsections; ACO hyperparameters absent from Methods.

**C — disclose or defer:** software-stack misattribution (#45); citation-form errors (#21, #22, "PTM-2" in #20); §3.5 numbering error (#51).

---

## 6. Integrity warnings

- **`FLAGS.md` v3 is truncated.** Header announces #52–#94 and "next free #95"; the file ends at **#74**. Flags #75, #79, #90, #91, #92 are forward-referenced but never written. All four forward references were spot-checked and are verbatim-accurate — the findings are real, the entries are absent.
- **The project's formal SEVERE count is 0**, despite two places in `FLAGS.md` implying otherwise. Do not report a severe roadblock on the strength of a forward reference.
- **Flag #64's attestation is wrong; its finding is right.** It claims all six k=1 values come from §3; two (Kabiki 3.094, Banaba 3.068) come only from the D-06 CSV. The arithmetic conclusion is verified correct.
- **Five flags need repair before going downstream:** #53, #59, #64, #68, #70 (defective reasoning or sourcing; every *quotation* in all 23 new flags was verified verbatim-accurate).
- **A log gap exists:** Phase 1.5 and the STATE.md reconciliation produced flag #51 and the #47 correction with no log entry.

---

## 7. What changed since last run

First run — no prior STATUS.md.
