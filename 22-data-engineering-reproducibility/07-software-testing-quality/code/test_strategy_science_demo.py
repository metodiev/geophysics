#!/usr/bin/env python3
"""Test strategy for numerical and data code, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python test_strategy_science_demo.py

Everything here is SYNTHETIC.  Cost multipliers, discovery fractions, coverage
and assertion strengths are chosen teaching values; no real test suite was
measured.  The floating-point section is deterministic arithmetic on the
platform's own IEEE-754 doubles and is reproducible there.

Sections
--------
1. Where a defect is found: the shift-left cost model.
2. Floating-point tolerance: what a derivative test can actually assert.
3. Coverage is an upper bound: mutation kill rates by operator class.
4. Diminishing returns: what the hundredth test buys.
"""

import math

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    print("SYNTHETIC teaching values; the arithmetic is this machine's IEEE-754 float64.")
    print("No real suite, benchmark or CI service was measured.")
    section("1. Where a defect is found: the shift-left cost model")
    stages = ["unit", "integration", "acceptance", "field"]
    # chosen discovery fractions and relative repair multipliers
    strategies = {
        "strong unit suite": ([0.55, 0.25, 0.12, 0.08], [1.0, 3.0, 10.0, 60.0]),
        "no unit tests": ([0.20, 0.30, 0.18, 0.32], [1.0, 3.0, 10.0, 60.0]),
    }
    print("  stage        | strong unit suite | no unit tests (chosen fractions)")
    for i, st in enumerate(stages):
        print(f"  {st:<12} | {100 * strategies['strong unit suite'][0][i]:>17.0f} % | "
              f"{100 * strategies['no unit tests'][0][i]:>6.0f} %")
    print("  repair multiplier relative to a unit-test fix: "
          f"{strategies['strong unit suite'][1]}")
    cost = {}
    for name, (disc, mult) in strategies.items():
        cost[name] = sum(d * m for d, m in zip(disc, mult))
        print(f"  expected cost per defect, {name:<18} = {cost[name]:>6.2f} units")
    ratio = cost["no unit tests"] / cost["strong unit suite"]
    print(f"  -> a suite that finds defects one stage later costs {ratio:.2f}x more "
          f"per defect")
    defects = 120
    print(f"  at {defects} defects a year that is "
          f"{(cost['no unit tests'] - cost['strong unit suite']) * defects:.0f} units")
    shift = 0.10
    print(f"  moving {100 * shift:.0f} % of the defects from field to unit saves "
          f"{shift * (60.0 - 1.0) * defects:.1f} units a year")

    section("2. Floating-point tolerance: what a derivative test can assert")
    x0 = 1.0
    exact = math.cos(x0)
    print(f"  exact f'(1) = cos(1) = {exact:.16f}")
    print("  h        | forward-difference value | abs error  | rel error")
    best = (None, None)
    for k in range(1, 17):
        h = 10.0 ** (-k)
        approx = (math.sin(x0 + h) - math.sin(x0)) / h
        err = abs(approx - exact)
        if best[0] is None or err < best[0]:
            best = (err, h)
        print(f"  1e-{k:<2d}    | {approx:>24.16f} | {err:>10.3e} | "
              f"{err / abs(exact):>9.3e}")
    print(f"  -> the smallest error is {best[0]:.3e} at h = {best[1]:.0e}, near "
          f"sqrt(eps) = {math.sqrt(np.finfo(float).eps):.2e}")
    print(f"  -> an atol of 1e-8 would pass at h = 1e-8 but fail at h = 1e-14, "
          f"where the error is {abs((math.sin(x0 + 1e-14) - math.sin(x0)) / 1e-14 - exact):.1e}")
    tiny = 9.0e-10
    print(f"  a value of {tiny:.1e} is {1e-8 / tiny:.0f}x smaller than an atol of 1e-8:")
    print("  an absolute tolerance cannot be used across scales; use a relative one")
    print(f"  with an absolute floor, e.g. atol = 1e-12, rtol = 1e-9")

    section("3. Coverage is an upper bound: mutation kill rates")
    # (line coverage, assertion strength) per mutation operator class, chosen
    operators = {
        "arithmetic operator": (0.98, 0.92, 0.35),
        "condition or boundary": (0.86, 0.74, 0.25),
        "constant or unit": (0.95, 0.88, 0.20),
        "statement deletion": (0.99, 0.55, 0.20),
    }
    mutants = 60000
    print("  operator class        | coverage | assertion | killed | c * a")
    weighted_c = 0.0
    weighted_a = 0.0
    for name, (c, a, w) in operators.items():
        u1 = RNG.random(mutants)
        u2 = RNG.random(mutants)
        killed = np.mean((u1 <= c) & (u2 <= a))
        weighted_c += w * c
        weighted_a += w * a
        print(f"  {name:<21} | {c:>8.2f} | {a:>9.2f} | {killed:>6.3f} | {c * a:>6.3f}")
    overall = 0.0
    for name, (c, a, w) in operators.items():
        overall += w * c * a
    print(f"  -> weighted line coverage {weighted_c:.3f} is an upper bound on the "
          f"kill rate, which is {overall:.3f}")
    print(f"  -> the suite looks 94.6 % complete and is {100 * (weighted_c - overall):.1f} "
          f"points weaker than that")
    weak = 0.60
    print(f"  -> a 100 % coverage suite whose assertions observe only {weak:.2f} of the "
          f"time scores {weak:.3f}, below every class above")
    print("  -> the weakest operator class says where to add assertions, which the "
          "aggregate number hides")

    section("4. Diminishing returns: what the hundredth test buys")
    lam = 0.06        # chosen: detection rate per additional test
    seconds = 4.0     # chosen: seconds per test
    print("  tests | detected fraction | suite time | marginal gain of the last block")
    previous = 0.0
    for n in (10, 25, 50, 100, 200):
        detected = 1.0 - math.exp(-lam * n)
        print(f"  {n:>5d} | {detected:>17.6f} | {n * seconds:>8.0f} s | "
              f"{detected - previous:>+10.4f}")
        previous = detected
    print("  -> 50 tests buy 0.9502 of the detectable defects; growing to 200 tests")
    print("     quadruples the runtime to buy the last 0.0498, so the fast suite and")
    print("     the full suite are different tools with different jobs")


if __name__ == "__main__":
    main()
