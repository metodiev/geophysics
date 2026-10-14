#!/usr/bin/env python3
"""Cost, scaling and practical efficiency: where the money goes, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cost_and_scaling_demo.py

Everything here is SYNTHETIC.  Costs, rates and data volumes are chosen teaching
values in arbitrary units; no provider price list is quoted and no benchmark of a
real system is used.

Sections
--------
1. The cost of one model run: compute, storage and egress.
2. Weak scaling: cost per unit of work against problem size.
3. The break-even core count: when parallel speedup stops paying for itself.
4. Where the cost actually goes in a data-heavy project.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC cost model (chosen, not measured) ----------------------------
CORE_HOUR_COST = 0.05        # arbitrary units per core-hour
STORAGE_TB_MONTH = 20.0
EGRESS_TB = 90.0
SERIAL_FRACTION = 0.05


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def speedup(p, n):
    return 1.0 / (p + (1.0 - p) / n)


def main():
    section("1. The cost of one model run")
    cores = 64
    hours = 12.0
    output_tb = 2.0
    kept_months = 12
    compute = cores * hours * CORE_HOUR_COST
    storage = output_tb * kept_months * STORAGE_TB_MONTH
    egress = output_tb * EGRESS_TB
    print(f"SYNTHETIC run: {cores} cores for {hours:.0f} h, {output_tb:.0f} TB "
          f"output kept {kept_months} months (chosen)")
    print(f"  compute      = {compute:>10.1f} units")
    print(f"  storage      = {storage:>10.1f} units")
    print(f"  egress (once)= {egress:>10.1f} units")
    print(f"  total        = {compute + storage + egress:>10.1f} units")
    print(f"  storage and egress are "
          f"{100 * (storage + egress) / (compute + storage + egress):.0f} % of the "
          f"bill")
    print("  -> the compute is the visible cost and the data movement is often the")
    print("     larger one; both must be forecast, not assumed")

    section("2. Weak scaling: cost per unit of work")
    print(f"  model: 12 h at 64 cores, efficiency falling 2 % per doubling of "
          f"cores (chosen)")
    print("  problem size | cores | wall (h) | core-hours | cost | cost per unit")
    for scale, cores_used in ((1, 64), (8, 512), (64, 4096), (512, 32768)):
        doublings = np.log2(cores_used / 64.0)
        wall = 12.0 * (1.02 ** doublings)
        core_hours = cores_used * wall
        cost = core_hours * CORE_HOUR_COST
        print(f"  {scale:>12.0f} | {cores_used:>5d} | {wall:>8.2f} | "
              f"{core_hours:>10.0f} | {cost:>7.1f} | {cost / scale:>12.2f}")
    print("  -> a 2 % efficiency loss per doubling makes the same work cost about")
    print("     20 % more at 32 768 cores than at 64; doubling capacity is not")
    print("     free even when the wall time barely changes")

    section("3. The break-even core count")
    print("  model: T(n) = 12 h x (p + (1-p) x 64/n), p = 0.05, from a 64-core base")
    print("  deadline (h) | cores needed | wall (h) | core-hours | cost | feasible")
    floor_hours = 12.0 * SERIAL_FRACTION
    print(f"  serial floor: the minimum wall time on any number of cores is "
          f"{floor_hours:.2f} h (p = {SERIAL_FRACTION:.2f})")
    for deadline in (12.0, 6.0, 3.0, 1.5, 0.5):
        n = 64
        wall = 12.0 * (SERIAL_FRACTION + (1.0 - SERIAL_FRACTION) * 64.0 / n)
        while wall > deadline and n < 1_000_000:
            n *= 2
            wall = 12.0 * (SERIAL_FRACTION + (1.0 - SERIAL_FRACTION) * 64.0 / n)
        feasible = wall <= deadline
        core_hours = n * wall if feasible else float("nan")
        cores_text = f"{n:>12d}" if feasible else f"{'> 1000000':>12}"
        cost = core_hours * CORE_HOUR_COST
        print(f"  {deadline:>12.1f} | {cores_text} | {wall:>8.2f} | "
              f"{core_hours:>10.0f} | {cost:>5.1f} | {'yes' if feasible else 'no'}")
    print("  -> halving the deadline roughly doubles the requested cores, and the")
    print("     serial fraction makes the wall time fall more slowly each time:")
    print("     the cost of the last halving is the largest, and below the serial")
    print("     floor no number of cores can reach the deadline")

    section("4. Where the cost goes in a data-heavy project")
    items = {"compute for analysis": 35.0, "storage of raw data": 25.0,
             "storage of derived products": 10.0, "data egress": 20.0,
             "recomputation after failures": 10.0}
    total = sum(items.values())
    print("  item                          | share of annual cost")
    for k, v in items.items():
        print(f"  {k:<29} | {100 * v / total:>20.1f} %")
    print(f"  fraction that is not compute = "
          f"{100 * (1 - items['compute for analysis'] / total):.0f} %")
    print("  -> two thirds of a data-heavy budget can be storage, movement and")
    print("     failures; optimising the solver alone leaves most of the bill")
    print("     untouched")


if __name__ == "__main__":
    main()
