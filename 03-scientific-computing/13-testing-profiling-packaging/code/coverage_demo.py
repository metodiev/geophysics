"""Line coverage, measured with sys.settrace, and three ways it misleads.

Run:  python coverage_demo.py
Requires: numpy (project virtual environment)

``coverage.py`` and ``pytest-cov`` are the tools you would use in practice; they
are not installed in this environment, so this script builds the same
measurement from the standard library.  The measurement is not an approximation
of what coverage means -- it is definitionally the same thing: the fraction of
executable lines that were executed.

The subject is ``survey_stats.py``, which contains two planted defects and one
branch that no test here reaches.  Three scenarios run against it:

  A. a smoke test: 100% line coverage, every assertion passes, output wrong by
     61.72 mGal;
  B. the same coverage with one correct assertion, which fails -- the defect was
     never invisible to *arithmetic*, only to coverage;
  C. the untested branch: coverage rises when the branch is exercised, and the
     branch turns out to contain the second defect.
"""

from __future__ import annotations

import dis
import inspect
import sys

import numpy as np

import survey_stats as ss


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# A minimal line-coverage instrument
# --------------------------------------------------------------------------

def _functions(module) -> dict[str, object]:
    return {
        name: obj
        for name, obj in vars(module).items()
        if inspect.isfunction(obj) and getattr(obj, "__module__", None) == module.__name__
    }


def executable_lines(module) -> dict[str, set[int]]:
    """Lines the interpreter could execute, per function, from bytecode.

    This is the denominator of a coverage percentage and it is derived from the
    compiled code, not from the source text, which is why a comment or a
    continuation line is not an "uncovered line".
    """
    result: dict[str, set[int]] = {}
    for name, fn in _functions(module).items():
        code = fn.__code__
        lines = {lineno for _offset, lineno in dis.findlinestarts(code)}
        result[name] = {ln for ln in lines if ln > code.co_firstlineno}
    return result


def run_covered(callable_) -> tuple[set[tuple[str, int]], BaseException | None]:
    """Run ``callable_``, returning the executed lines and any failure.

    The coverage is returned even when the callable raises: a failing test is
    exactly the test whose coverage you want to see.
    """
    hit: set[tuple[str, int]] = set()
    error: BaseException | None = None
    target_file = ss.__file__

    def tracer(frame, event, arg):
        if event == "call":
            return tracer
        if event == "line" and frame.f_code.co_filename == target_file:
            hit.add((frame.f_code.co_name, frame.f_lineno))
        return tracer

    sys.settrace(tracer)
    try:
        callable_()
    except BaseException as exc:          # noqa: BLE001 - reported, not swallowed
        error = exc
    finally:
        sys.settrace(None)
    return hit, error


def coverage_report(executable: dict[str, set[int]],
                    hit: set[tuple[str, int]]) -> float:
    total = covered = 0
    print(f"  {'function':>24} {'executable':>11} {'hit':>5} {'coverage':>9}  missed")
    for name in sorted(executable):
        lines = executable[name]
        got = {ln for fname, ln in hit if fname == name}
        missed = sorted(lines - got)
        pct = 100.0 * len(got & lines) / len(lines) if lines else 100.0
        total += len(lines)
        covered += len(got & lines)
        missed_text = ",".join(str(m) for m in missed) if missed else "-"
        print(f"  {name:>24} {len(lines):>11} {len(got & lines):>5} {pct:>8.1f}%  {missed_text}")
    overall = 100.0 * covered / total if total else 100.0
    print(f"  {'TOTAL':>24} {total:>11} {covered:>5} {overall:>8.1f}%")
    return overall


# --------------------------------------------------------------------------
# The three scenarios
# --------------------------------------------------------------------------

def base_calls(with_terrain: bool = False) -> None:
    """The four calls every scenario makes, so coverage is comparable."""
    _ = ss.free_air_anomaly(100.0, 979000.0)
    _ = ss.mean_elevation(np.array([100.0, 120.0, 140.0]))
    _ = ss.normal_gravity_mgal(45.0)
    if with_terrain:
        _ = ss.station_anomaly(100.0, 979000.0, terrain_correction_mgal=5.0)
    else:
        _ = ss.station_anomaly(100.0, 979000.0)


def smoke_test() -> int:
    """Calls every public entry point and asserts nothing at all."""
    base_calls()
    return 0                            # zero assertions


def smoke_test_with_one_assertion() -> int:
    """The same calls, plus the one physical fact the first test omitted."""
    base_calls()
    got = ss.free_air_anomaly(100.0, 979000.0)
    expected = 979000.0 + ss.FREE_AIR_GRADIENT_MGAL_PER_M * 100.0
    assert abs(got - expected) < 1e-9, f"free-air sign: got {got}, expected {expected}"
    return 1


def characterisation_test() -> int:
    """A test whose expected value was copied from a previous run of the code.

    This is what a 'regression test' decays into when nobody checks the
    reference value. It pins the defect in place. Coverage: unchanged.
    """
    base_calls()
    got = ss.free_air_anomaly(100.0, 979000.0)
    reference = 978969.14            # captured from the buggy implementation
    assert abs(got - reference) < 1e-9
    return 1


def branch_test() -> int:
    """Now exercise the optional terrain-correction branch -- but assert nothing."""
    base_calls(with_terrain=True)
    return 0


def branch_test_with_assertion() -> int:
    """Exercise the branch AND state what the terrain correction must do."""
    base_calls(with_terrain=True)
    free_air = 979000.0 + ss.FREE_AIR_GRADIENT_MGAL_PER_M * 100.0
    got = ss.station_anomaly(100.0, 979000.0, terrain_correction_mgal=5.0)
    expected = free_air + 5.0            # the terrain correction is added, always
    assert abs(got - expected) < 1e-9, (
        f"terrain branch sign: got {got}, expected {expected}"
    )
    return 1


def scenario(label: str, fn, assertions: int) -> None:
    section(label)
    executable = executable_lines(ss)
    hit, error = run_covered(fn)
    outcome = "PASSED" if error is None else f"FAILED: {error}"
    print(f"  assertions executed: {assertions}   test outcome: {outcome}\n")
    pct = coverage_report(executable, hit)
    quality_gate_summary(pct, outcome)
    print()


def quality_gate_summary(coverage_pct: float, outcome: str) -> None:
    verdict = ("passes a 90% line-coverage gate"
               if coverage_pct >= 90 else "fails a 90% line-coverage gate")
    print(f"  gate verdict: coverage {coverage_pct:.1f}% -> {verdict}; "
          f"tests {'pass' if outcome == 'PASSED' else 'fail'}")


def compare_wrongness() -> None:
    section("Why the smoke test's pass is not evidence of anything")
    got = ss.free_air_anomaly(100.0, 979000.0)
    correct = 979000.0 + ss.FREE_AIR_GRADIENT_MGAL_PER_M * 100.0
    print(f"  free_air_anomaly(100 m, 979000 mGal) = {got:.2f} mGal")
    print(f"  free-air correction as defined       = {correct:.2f} mGal")
    print(f"  discrepancy                          = {abs(got - correct):.2f} mGal")
    print(f"  = 2 * {ss.FREE_AIR_GRADIENT_MGAL_PER_M} * 100 m -- a pure sign error")
    print("\n  A gravity anomaly wrong by 62 mGal is wrong by more than the total")
    print("  signal of most targets. The smoke test reported 100% line coverage")
    print("  and 'all tests passed'.")


def main() -> int:
    print("Line coverage is a *necessary* condition on a test suite: every line")
    print("should be executed by some test. It is not a sufficient one, and the")
    print("scenarios below show four different ways it falls short.")
    scenario("Scenario A: zero assertions -- tests pass, the defect ships",
             smoke_test, assertions=0)
    scenario("Scenario B: one correct assertion -- same calls, defect caught",
             smoke_test_with_one_assertion, assertions=1)
    scenario("Scenario C: expected value copied from the code -- 'regression'",
             characterisation_test, assertions=1)
    scenario("Scenario D: the untested branch, exercised but not checked",
             branch_test, assertions=0)
    scenario("Scenario E: the branch exercised AND checked -- defect 2 caught",
             branch_test_with_assertion, assertions=1)
    compare_wrongness()
    section("Summary")
    print("A. Coverage measures execution, never correctness. Four calls and zero")
    print("   assertions bought 90.9% line coverage and passed.")
    print("B. One assertion at the same coverage was enough to catch the sign")
    print("   error. Coverage is not useless -- it counts lines, not claims, and")
    print("   the claim is what finds the bug.")
    print("C. A test can pin a bug in place when its expected value came from the")
    print("   code itself. No coverage gate can detect that. Only an independent")
    print("   reference -- a formula, an instrument, an analytic solution -- can.")
    print("D/E. Coverage rose only when the branch was exercised, and the newly")
    print("   covered branch contained the second defect. That is the real value")
    print("   of the signal: it names the behaviour nothing tests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
