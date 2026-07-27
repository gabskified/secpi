"""Regression test for Flag #96 / decision D-12 --- SensitivityAnalyzer state leak.

WHAT THIS GUARDS
----------------
`SensitivityAnalyzer._run_single_evaluation` perturbs species parameters in order
to measure their sensitivity. `TreeSpecies.SPECIES_DATA` is a CLASS attribute,
shared by every `TreeSpecies` instance in the process, so those perturbations are
writes to global state. If they are not restored, every subsequent evaluation ---
and every consumer of `TreeSpecies` anywhere else in the pipeline --- runs against
contaminated species data.

Three quantities must survive an evaluation unchanged, not one:

  1. `TreeSpecies.SPECIES_DATA`      --- the shared dict itself.
  2. `TreeSpecies.max_CPA`           --- cached as an INSTANCE attribute by
  3. `TreeSpecies.max_LAI`               `_calculate_cpa_and_normalize()`.

(2) and (3) matter because `get_normalized_cooling_potential()` divides by both:
they are live denominators in the cooling term. A restore that covers only the
dict looks correct at the dict level and stays wrong at the normalization level.

WHY A LONG-LIVED PROBE
----------------------
The probe `TreeSpecies` is constructed ONCE, before the contaminating evaluations,
and is asserted against afterwards. A freshly constructed instance would hide the
defect by construction: its `__init__` recomputes `max_CPA`/`max_LAI` from whatever
the dict currently holds, so it is self-consistent even when the dict is corrupt.
The interesting failure is a live object whose cached denominators no longer agree
with the shared dict they were derived from.

RUNNING
-------
    .venv/Scripts/python.exe tests/test_species_data_isolation.py

Point it at a different implementation file with the SECPI_IMPL environment
variable --- used to run this same test against the pre-fix baseline reconstructed
from commit 87d4528:

    SECPI_IMPL=/path/to/pre_fix_AuditedCode_1.py .venv/Scripts/python.exe \
        tests/test_species_data_isolation.py

Exit code 0 = pass, 1 = fail. No third-party test runner is required (pytest is
not installed in this project's .venv), but the `test_*` functions are named so a
runner can collect them if one is added later.
"""

from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_IMPL = os.path.join(REPO_ROOT, "legacy", "AuditedCode_1.py")
IMPL_PATH = os.environ.get("SECPI_IMPL", DEFAULT_IMPL)

# Production ACO configuration, copied verbatim from main_revised_validation()'s
# config['aco_params'] (AuditedCode_1.py:3327-3335). The optimizer itself is
# stubbed out below, so these values only have to be present and well-formed;
# they are kept faithful so the code path under test is the production one.
PRODUCTION_ACO_CONFIG = {
    "n_trees": 5,
    "n_ants": 20,
    "n_iterations": 40,
    "evaporation_rate": 0.5,
    "alpha": 1.0,
    "beta": 2.0,
    "q0": 0.7,
}


def load_impl(path: str):
    """Load the reference implementation as a module, read-only, by path."""
    spec = importlib.util.spec_from_file_location("secpi_impl_under_test", path)
    module = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(module)
    return module


class StubACO:
    """Stands in for `AntColonySystemACO` during the test.

    The species mutations under test happen at AuditedCode_1.py:859-888, strictly
    BEFORE the optimizer is constructed at :895, and none of them depends on the
    optimizer's output. Stubbing the ACO therefore leaves the code path under test
    completely intact while removing ~1.9 s of irrelevant compute per evaluation.
    The constant it returns is a control value, not a SECPI measurement.
    """

    STUB_SECPI = 1.0

    def __init__(self, *args, **kwargs):
        self.best_secpi = self.STUB_SECPI

    def run(self, verbose=False):
        return [], []


def snapshot_state(module, probe):
    """Capture the three protected quantities plus their observable consequence."""
    return {
        "species_data": copy.deepcopy(module.TreeSpecies.SPECIES_DATA),
        "max_CPA": probe.max_CPA,
        "max_LAI": probe.max_LAI,
        # Derived, and the reason (2) and (3) are in scope at all: this divides
        # the (possibly contaminated) dict by the (possibly stale) cached maxima.
        "normalized_cooling_potential": {
            species: probe.get_normalized_cooling_potential(species)
            for species in probe.species_list
        },
    }


def diff_species_data(before: dict, after: dict) -> list[str]:
    """Return one human-readable line per differing (species, field) pair."""
    differences = []
    for species in sorted(set(before) | set(after)):
        fields_before = before.get(species, {})
        fields_after = after.get(species, {})
        for field in sorted(set(fields_before) | set(fields_after)):
            value_before = fields_before.get(field, "<absent>")
            value_after = fields_after.get(field, "<absent>")
            if repr(value_before) != repr(value_after):
                differences.append(
                    f"    SPECIES_DATA[{species!r}][{field!r}]: "
                    f"{value_before!r} -> {value_after!r}"
                )
    return differences


def diff_snapshots(before: dict, after: dict) -> list[str]:
    """Return every bit-level difference between two snapshots."""
    differences = diff_species_data(before["species_data"], after["species_data"])

    for scalar in ("max_CPA", "max_LAI"):
        if repr(before[scalar]) != repr(after[scalar]):
            differences.append(
                f"    long-lived TreeSpecies.{scalar}: "
                f"{before[scalar]!r} -> {after[scalar]!r}"
            )

    ncp_before = before["normalized_cooling_potential"]
    ncp_after = after["normalized_cooling_potential"]
    for species in sorted(set(ncp_before) | set(ncp_after)):
        if repr(ncp_before.get(species)) != repr(ncp_after.get(species)):
            differences.append(
                f"    get_normalized_cooling_potential({species!r}): "
                f"{ncp_before.get(species)!r} -> {ncp_after.get(species)!r}"
            )

    return differences


# The contaminating evaluations, chosen to exercise all four write points named in
# D-12's implementation note: :880 (compounding LAI), :882 (direct field write),
# :885-886 (CPA recomputation on crown-diameter change), :888 (renormalization).
# Bounds are the code's own +/-20% sweep bounds, not invented values.
CONTAMINATION_SEQUENCE = [
    ("Narra", "crown_diameter_m", 27.6),          # 23.0 * 1.2  -> :882, :885-886, :888
    ("Talisay", "height_m", 42.0),                # 35.0 * 1.2  -> :882, :888
    ("Akleng-parang", "crown_diameter_m", 28.8),  # 24.0 * 1.2  -> shifts max_CPA
    ("Narra", "l0", 0.30),                        # 0.25 * 1.2  -> :880, compounding
    ("Narra", "l0", 0.30),
    ("Narra", "l0", 0.30),
    ("Narra", "l0", 0.30),
    ("Narra", "l0", 0.30),
    ("Narra", "l0", 0.30),
]


def run_isolation_check(module, verbose=True):
    """Run the contaminating evaluations and return (differences, evaluation_log)."""
    analyzer_stdout = io.StringIO()

    with contextlib.redirect_stdout(io.StringIO()):
        probe = module.TreeSpecies()          # long-lived; the subject of the assertions
        original_aco = module.AntColonySystemACO
        module.AntColonySystemACO = StubACO
        analyzer = module.SensitivityAnalyzer(
            base_grid=None,
            base_cooling_model=None,
            base_aco_config=PRODUCTION_ACO_CONFIG,
            output_dir=None,
            reference_cutoffs=None,
        )

    try:
        before = snapshot_state(module, probe)
        with contextlib.redirect_stdout(analyzer_stdout):
            for species, param_name, value in CONTAMINATION_SEQUENCE:
                analyzer._run_single_evaluation({}, [(species, param_name, value)])
        after = snapshot_state(module, probe)
    finally:
        module.AntColonySystemACO = original_aco

    evaluation_log = analyzer_stdout.getvalue()
    return diff_snapshots(before, after), evaluation_log, before, after


def test_species_data_is_restored_after_evaluation():
    """SPECIES_DATA, max_CPA and max_LAI must be bit-identical across evaluations."""
    module = load_impl(IMPL_PATH)

    differences, evaluation_log, before, after = run_isolation_check(module)

    # Guard against a vacuous pass: _run_single_evaluation swallows exceptions and
    # prints "Evaluation error", so a broken evaluation would mutate nothing and
    # the identity assertions would hold for the wrong reason.
    assert "Evaluation error" not in evaluation_log, (
        "an evaluation raised and was swallowed; this test would pass vacuously.\n"
        + evaluation_log
    )

    # Independent check of the same invariant from the other side: a TreeSpecies
    # constructed AFTER the evaluations must agree with the long-lived probe. This
    # is the mechanism by which STEP 8 inherits STEP 7's contamination.
    with contextlib.redirect_stdout(io.StringIO()):
        fresh = module.TreeSpecies()
    fresh_disagreements = []
    for scalar in ("max_CPA", "max_LAI"):
        probe_value = after[scalar]
        fresh_value = getattr(fresh, scalar)
        if repr(probe_value) != repr(fresh_value):
            fresh_disagreements.append(
                f"    freshly-constructed TreeSpecies.{scalar} = {fresh_value!r}, "
                f"long-lived probe = {probe_value!r}"
            )

    all_differences = differences + fresh_disagreements

    if all_differences:
        header = (
            f"Species state was NOT restored after "
            f"{len(CONTAMINATION_SEQUENCE)} evaluations "
            f"({len(all_differences)} difference(s)):"
        )
        raise AssertionError(header + "\n" + "\n".join(all_differences))


def test_evaluation_is_idempotent():
    """Repeating an identical evaluation must not compound the model state.

    AuditedCode_1.py:879-880 reads the CURRENT LAI and writes `current * ratio`,
    so without a restore an identical input produces a different model each time.
    `n_samples=3` averages three repeats "to reduce stochastic noise"; if this
    test fails, those three repeats are three different models, not three samples
    of one.
    """
    module = load_impl(IMPL_PATH)

    with contextlib.redirect_stdout(io.StringIO()):
        original_aco = module.AntColonySystemACO
        module.AntColonySystemACO = StubACO
        analyzer = module.SensitivityAnalyzer(
            base_grid=None,
            base_cooling_model=None,
            base_aco_config=PRODUCTION_ACO_CONFIG,
            output_dir=None,
            reference_cutoffs=None,
        )

    try:
        observed_lai = []
        with contextlib.redirect_stdout(io.StringIO()):
            for _ in range(6):
                analyzer._run_single_evaluation({}, [("Narra", "l0", 0.30)])
                observed_lai.append(module.TreeSpecies.SPECIES_DATA["Narra"]["LAI"])
    finally:
        module.AntColonySystemACO = original_aco

    distinct = {repr(value) for value in observed_lai}
    if len(distinct) != 1:
        raise AssertionError(
            "identical evaluations produced "
            f"{len(distinct)} distinct Narra LAI values, expected 1:\n"
            + "\n".join(f"    repeat {i + 1}: {v!r}" for i, v in enumerate(observed_lai))
        )


TESTS = [
    test_species_data_is_restored_after_evaluation,
    test_evaluation_is_idempotent,
]


def main() -> int:
    print(f"implementation under test: {IMPL_PATH}")
    failures = 0
    for test in TESTS:
        try:
            test()
        except AssertionError as exc:
            failures += 1
            print(f"[FAIL] {test.__name__}")
            print(exc)
        except Exception as exc:  # noqa: BLE001 - surface any error, do not mask it
            failures += 1
            print(f"[ERROR] {test.__name__}: {type(exc).__name__}: {exc}")
        else:
            print(f"[PASS] {test.__name__}")

    print(f"\n{len(TESTS) - failures}/{len(TESTS)} passed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
