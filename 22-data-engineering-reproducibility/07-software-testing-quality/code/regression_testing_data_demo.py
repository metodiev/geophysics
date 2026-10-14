#!/usr/bin/env python3
"""Regression testing against known results, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python regression_testing_data_demo.py

Everything here is SYNTHETIC except the floating-point arithmetic, which is
measured on this platform's IEEE-754 numbers: the sums, the two variance
formulas and the dtype breakdown are computed and printed here.  The workflow in
section 3 is a chosen teaching DAG.

Sections
--------
1. Two orderings of the same sum: the round-off floor and the tolerance above it.
2. Catastrophic cancellation: the golden value that must not be computed.
3. What one code change invalidates: fan-out over a workflow.
4. Bitwise versus numerical comparison: alarms and blind spots.
"""

import math

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def sequential_sum(values):
    total = 0.0
    for v in values:
        total += v
    return total


def main():
    print("SYNTHETIC teaching values; the arithmetic is this machine's IEEE-754 float64.")
    print("No real suite, benchmark or CI service was measured.")
    section("1. Two orderings of the same sum: the round-off floor")
    n = 1_000_000
    values = 1.0e6 + RNG.normal(0.0, 1.0, n)
    reference = math.fsum(values)          # exactly rounded: the reference value
    sequential = sequential_sum(values)
    pairwise = float(np.sum(values))       # numpy's pairwise summation
    spread = abs(sequential - pairwise) / abs(reference)
    print(f"  {n} values near 1e6, exactly rounded sum = {reference:.4f}")
    print(f"  sequential accumulation : {sequential:.4f}  "
          f"rel error {abs(sequential - reference) / abs(reference):.3e}")
    print(f"  pairwise accumulation   : {pairwise:.4f}  "
          f"rel error {abs(pairwise - reference) / abs(reference):.3e}")
    print(f"  -> two legal orderings differ by {spread:.1e} relative: that is this "
          f"computation's round-off floor")
    for rtol, bug in ((1e-12, 1e-3), (1e-9, 1e-3), (1e-6, 1e-4)):
        print(f"  -> rtol {rtol:.0e}: sits {rtol / spread:>10.0f}x above the floor and "
              f"{bug / rtol:>8.0f}x below a real {bug:.0e} error")
    print("  -> a tolerance must be placed between the floor and the smallest error")
    print("     worth catching, and both numbers have to be measured, not guessed")

    section("2. Catastrophic cancellation: the golden value that must not be computed")
    mean = 1.0e8
    data = mean + RNG.normal(0.0, 1.0, 1_000_000)
    two_pass = float(np.var(data))                       # subtract the mean first
    naive64 = float(np.mean(data * data)) - float(np.mean(data)) ** 2
    data32 = data.astype(np.float32)
    naive32 = (float(np.mean(data32 * data32, dtype=np.float32))
               - float(np.mean(data32, dtype=np.float32)) ** 2)
    print(f"  {len(data)} values with mean {mean:.0e} and standard deviation 1")
    print(f"  two-pass variance        : {two_pass:.9f}")
    print(f"  E[x^2] - E[x]^2 float64  : {naive64:.9f}  "
          f"rel error {abs(naive64 - two_pass) / two_pass:.3e}")
    print(f"  E[x^2] - E[x]^2 float32  : {naive32:.1f}  (a negative variance)")
    print(f"  -> the naive formula is wrong by {100 * abs(naive64 - two_pass) / two_pass:.0f} % "
          f"in float64 and is meaningless in float32")
    print(f"  -> float32 resolution is {np.finfo(np.float32).eps:.1e}, and the squares "
          f"here reach {mean ** 2:.0e}: the terms cannot be represented")
    print("  -> a golden value recorded from the naive formula would reject the")
    print("     correct answer and accept the wrong one, so the test must pin an")
    print("     independent implementation plus a property (variance >= 0)")

    section("3. What one code change invalidates: fan-out over a workflow")
    stages = {
        "load": (0.2, []),
        "qc": (0.5, ["load"]),
        "grid": (1.0, ["qc"]),
        "invert": (6.0, ["grid"]),
        "migrate": (4.0, ["invert"]),
        "attributes": (1.5, ["grid"]),
        "figures": (0.4, ["attributes", "migrate"]),
        "report": (0.1, ["figures"]),
        "export": (0.6, ["migrate"]),
        "archive": (0.2, ["export"]),
        "training_set": (0.8, ["attributes"]),
        "metrics": (0.3, ["training_set", "report"]),
    }
    successors = {name: [] for name in stages}
    for name, (_, needs) in stages.items():
        for parent in needs:
            successors[parent].append(name)

    def descendants(name):
        seen, stack = set(), list(successors[name])
        while stack:
            cur = stack.pop()
            if cur not in seen:
                seen.add(cur)
                stack.extend(successors[cur])
        return seen

    everything = sum(hours for hours, _ in stages.values())
    print("  changed stage | stages to recompute | hours | share of the pipeline")
    for name, (hours, _) in stages.items():
        affected = descendants(name)
        work = hours + sum(stages[s][0] for s in affected)
        print(f"  {name:<13} | {len(affected):>2d} of {len(stages)} stages "
              f"{'':>6} | {work:>5.1f} | {100 * work / everything:>19.1f} %")
    print(f"  -> the whole pipeline costs {everything:.1f} h, which is also what")
    print("     'invalidate everything on any edit' costs every time")
    print("  -> content-addressed keys recompute only the descendants; a change to")
    print("     'load' or 'qc' is still almost the whole pipeline, because the")
    print("     fan-out, not the size of the edit, is what the key has to capture")

    section("4. Bitwise versus numerical comparison: alarms and blind spots")
    trials = 200_000
    legitimate = 1.0 + RNG.normal(0.0, spread, trials)
    print(f"  {trials} legitimate refactors, each shifting the result by about the")
    print(f"  round-off floor measured in section 1 ({spread:.1e})")
    print("  rtol     | false alarms | share of refactors")
    for rtol in (1e-14, 1e-13, 1e-12, 1e-9):
        alarms = int(np.sum(np.abs(legitimate - 1.0) > rtol))
        print(f"  {rtol:.0e} | {alarms:>12d} | {100 * alarms / trials:>19.3f} %")
    print("  -> bitwise comparison sits at the top of that table: every refactor that")
    print("     reorders a sum alarms, and the test is switched off within a month")
    print("  rtol     | smallest error still caught")
    for rtol, note in ((1e-11, "round-off noise only"),
                       (1e-9, "units, formula and layout bugs"),
                       (1e-6, "large formula and layout bugs"),
                       (1e-3, "structural changes only")):
        print(f"  {rtol:.0e} | {note}")
    print("  -> tolerances near the floor alarm on noise and loose ones pass a wrong")
    print("     formula, so a suite needs both: exact assertions on counts, indices and")
    print("     flags, and loose numerical assertions on floating-point arrays")


if __name__ == "__main__":
    main()
