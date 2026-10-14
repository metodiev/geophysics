#!/usr/bin/env python3
"""Cloud computing for research: scaling, efficiency and interruption risk.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cloud_computing_research_demo.py

Everything here is SYNTHETIC.  Parallel fractions, instance costs and interruption
rates are chosen teaching values; no cloud provider was used and no price is quoted.

Sections
--------
1. Strong scaling: speedup under a serial fraction (Amdahl).
2. Efficiency and the practical worker count.
3. Interruption risk for preemptible capacity, and the checkpoint interval it implies.
4. What the cloud changes and what it does not.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC model (chosen, not measured) ---------------------------------
SERIAL_FRACTION = 0.05       # fraction of the runtime that cannot be parallelised
WORKERS = [1, 4, 16, 64, 256, 1024]
INTERRUPTION_PER_HOUR = 0.02  # chance per instance-hour, chosen
CHECKPOINT_MINUTES = [60, 30, 10, 5]


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def speedup(p, n):
    """Amdahl speedup with serial fraction p."""
    return 1.0 / (p + (1.0 - p) / n)


def main():
    section("1. Strong scaling under a serial fraction")
    print(f"  Amdahl:  S(n) = 1 / (p + (1-p)/n), p = {SERIAL_FRACTION:.2f} "
          f"(chosen)")
    print("  workers | speedup | ideal | efficiency")
    for n in WORKERS:
        s = speedup(SERIAL_FRACTION, n)
        print(f"  {n:>7d} | {s:>7.2f} | {n:>5d} | {100 * s / n:>9.1f} %")
    ceiling = 1.0 / SERIAL_FRACTION
    print(f"  asymptote with p = {SERIAL_FRACTION:.2f} is {ceiling:.0f}x: no")
    print("  number of instances beats the serial fraction")

    section("2. Efficiency and the practical worker count")
    print("  workers | wall time (h) | instance-hours | cost (units)")
    base_hours = 24.0
    cost_per_hour = 1.0
    for n in (1, 16, 64, 256):
        wall = base_hours / speedup(SERIAL_FRACTION, n)
        inst_hours = wall * n
        print(f"  {n:>7d} | {wall:>13.2f} | {inst_hours:>14.1f} | "
              f"{inst_hours * cost_per_hour:>12.1f}")
    print("  -> cost rises monotonically while wall time falls: the useful")
    print("     question is the deadline, not the maximum worker count")

    section("3. Interruption risk and the checkpoint interval")
    print(f"  preemptible capacity: {INTERRUPTION_PER_HOUR:.2f} per instance-hour "
          f"(chosen)")
    print("  checkpoint every (min) | P(interrupted in an interval) | expected")
    print("                         |                             | work lost (h)")
    for minutes in CHECKPOINT_MINUTES:
        p_int = 1.0 - np.exp(-INTERRUPTION_PER_HOUR * minutes / 60.0)
        lost = (minutes / 60.0) * p_int / 2.0
        print(f"  {minutes:>22d} | {p_int:>27.4f} | {lost:>15.3f}")
    for n in (64, 256):
        p_any = 1.0 - np.exp(-INTERRUPTION_PER_HOUR * (24.0 / speedup(
            SERIAL_FRACTION, n)) * n)
        print(f"  with {n} instances over a run, "
              f"P(at least one interruption) = {p_any:.3f}")
    print("  -> at fleet scale an interruption is certain, so the design question")
    print("     is not whether but how much work a restart costs")

    section("4. What the cloud changes, and what it does not")
    rows = [
        ("changes", "capacity is elastic and billed by the hour"),
        ("changes", "you can obtain a different machine type per task"),
        ("changes", "storage and compute are separate services, with a network "
                    "between them"),
        ("does not change", "the serial fraction of the algorithm"),
        ("does not change", "the licence of your dependencies or of the data"),
        ("does not change", "whether the result is correct"),
    ]
    for kind, item in rows:
        print(f"  {kind:<15} | {item}")
    print("  -> the cloud changes the cost curve of capacity, not the physics or")
    print("     the statistics; a result that is wrong on a cluster is wrong in a")
    print("     cloud region, faster and with a larger bill")


if __name__ == "__main__":
    main()
