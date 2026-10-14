#!/usr/bin/env python3
"""Intermediate project 4: interpreting a shallow refraction survey, including
the layer that the survey cannot see.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python refraction_interpretation_demo.py

Everything here is SYNTHETIC.  The velocity models and the "picked" first-arrival
times are generated below with a chosen noise level; no field survey is used.

Sections
--------
1. A three-layer model and its first-arrival branches.
2. Inverting the branches for velocities and thicknesses.
3. A hidden layer: a real intermediate layer that never appears.
4. What the interpreter must report besides the numbers.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

PICK_SIGMA = 0.0015      # first-break pick uncertainty, s (1.5 ms)

# SYNTHETIC model A: soil / weathered rock / bedrock, km/s and metres
MODEL_A = {"v1": 0.40, "v2": 1.60, "v3": 4.00, "h1": 3.0, "h2": 8.0}
# SYNTHETIC model B: a hidden layer - v2 refracts but is never the first arrival
MODEL_B = {"v1": 1.00, "v2": 1.50, "v3": 5.00, "h1": 2.0, "h2": 2.0}


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def branch_times(x, m):
    """Travel times of the direct, first-refractor and second-refractor waves."""
    v1, v2, v3, h1, h2 = m["v1"], m["v2"], m["v3"], m["h1"], m["h2"]
    t1 = x / v1
    t2 = x / v2 + 2.0 * h1 * np.sqrt(v2 ** 2 - v1 ** 2) / (v1 * v2)
    ti3 = (2.0 * h1 * np.sqrt(v3 ** 2 - v1 ** 2) / (v1 * v3)
           + 2.0 * h2 * np.sqrt(v3 ** 2 - v2 ** 2) / (v2 * v3))
    return t1, t2, x / v3 + ti3, ti3


def crossover(x, ta, tb):
    """First offset at which tb becomes faster than ta."""
    idx = np.flatnonzero(tb < ta)
    return x[idx[0]] if idx.size else np.nan


def main():
    section("1. A three-layer model and its branches")
    x = np.arange(1.0, 60.0, 0.5)
    t1, t2, t3, ti3 = branch_times(x, MODEL_A)
    m = MODEL_A
    print(f"SYNTHETIC model A: v1 = {m['v1']:.2f}, v2 = {m['v2']:.2f}, "
          f"v3 = {m['v3']:.2f} km/s; h1 = {m['h1']:.1f} m, h2 = {m['h2']:.1f} m")
    print(f"  critical angles: to layer 2 = "
          f"{np.degrees(np.arcsin(m['v1'] / m['v2'])):.1f} deg, "
          f"to layer 3 = {np.degrees(np.arcsin(m['v1'] / m['v3'])):.1f} deg")
    print(f"  crossover 1->2 at {crossover(x, t1, t2):.1f} m, "
          f"2->3 at {crossover(x, t2, t3):.1f} m")
    first = np.minimum(np.minimum(t1, t2), t3)
    which = np.argmin(np.vstack([t1, t2, t3]), axis=0)
    print(f"{'X (m)':>7}{'t direct':>11}{'t refr 2':>11}{'t refr 3':>11}"
          f"{'first':>10}{'phase':>10}")
    for xa in (2.0, 6.0, 10.0, 20.0, 40.0, 55.0):
        k = int(np.argmin(np.abs(x - xa)))
        print(f"{x[k]:>7.1f}{t1[k]:>11.5f}{t2[k]:>11.5f}{t3[k]:>11.5f}"
              f"{first[k]:>10.5f}{('direct', 'refr2', 'refr3')[which[k]]:>10}")

    section("2. Inverting the branches")
    npick = np.arange(1.0, 60.0, 1.0)
    t_pick = (np.minimum(np.minimum(branch_times(npick, MODEL_A)[0],
                                    branch_times(npick, MODEL_A)[1]),
                         branch_times(npick, MODEL_A)[2])
              + PICK_SIGMA * RNG.standard_normal(npick.size))
    sel2 = (npick > 9.0) & (npick < 20.0)
    sel3 = npick > 25.0
    c2 = np.polyfit(npick[sel2], t_pick[sel2], 1)
    c3 = np.polyfit(npick[sel3], t_pick[sel3], 1)
    v2_est = 1.0 / c2[0]
    v3_est = 1.0 / c3[0]
    h1_est = c2[1] * m["v1"] * v2_est / (2.0 * np.sqrt(v2_est ** 2 - m["v1"] ** 2))
    ti3_est = c3[1]
    h2_est = ((ti3_est - 2.0 * h1_est * np.sqrt(v3_est ** 2 - m["v1"] ** 2)
               / (m["v1"] * v3_est))
              * v2_est * v3_est / (2.0 * np.sqrt(v3_est ** 2 - v2_est ** 2)))
    print(f"  {npick.size} first-break picks, Gaussian noise "
          f"sigma = {PICK_SIGMA * 1000:.1f} ms")
    print(f"  branch 2 ({sel2.sum()} picks): slope 1/v2 -> v2 = {v2_est:.3f} km/s, "
          f"intercept = {c2[1]:.6f} s")
    print(f"  branch 3 ({sel3.sum()} picks): slope 1/v3 -> v3 = {v3_est:.3f} km/s, "
          f"intercept = {c3[1]:.6f} s")
    print(f"  recovered h1 = {h1_est:.2f} m (true {m['h1']:.1f} m)")
    print(f"  recovered h2 = {h2_est:.2f} m (true {m['h2']:.1f} m)")
    print(f"  v1 is taken from the direct branch: {m['v1']:.2f} km/s "
          f"(measured, not inverted)")

    section("3. A hidden layer")
    mb = MODEL_B
    xb = np.arange(1.0, 60.0, 0.5)
    a1, a2, a3, tib = branch_times(xb, mb)
    print(f"SYNTHETIC model B: v1 = {mb['v1']:.2f}, v2 = {mb['v2']:.2f} "
          f"(hidden), v3 = {mb['v3']:.2f} km/s; h1 = {mb['h1']:.1f} m, "
          f"h2 = {mb['h2']:.1f} m")
    print(f"  crossover 1->2 would be at {crossover(xb, a1, a2):.1f} m")
    print(f"  crossover 2->3 is at {crossover(xb, a2, a3):.1f} m")
    firstB = np.minimum(np.minimum(a1, a2), a3)
    print(f"  branch 2 is the first arrival at "
          f"{int(np.sum((a2 < a1) & (a2 < a3)))} offsets; the v2 layer is masked")
    sel_b = xb > 15.0
    cb = np.polyfit(xb[sel_b], firstB[sel_b], 1)
    v3b = 1.0 / cb[0]
    h1b = cb[1] * mb["v1"] * v3b / (2.0 * np.sqrt(v3b ** 2 - mb["v1"] ** 2))
    print(f"  inverting the first arrivals alone gives v3 = {v3b:.3f} km/s and a")
    print(f"  single apparent depth of {h1b:.2f} m, whereas the true total cover")
    print(f"  is h1 + h2 = {mb['h1'] + mb['h2']:.1f} m: the interpreter sees one")
    print(f"  interface and attributes all of the delay to it.")

    section("4. What the report must contain")
    print("  1. the picked first breaks, with the picking method and its scatter;")
    print("  2. the velocity of each branch, with the offset range used;")
    print("  3. the thickness of each layer, with the assumption of constant")
    print("     velocity above it stated explicitly;")
    print("  4. a statement of whether a hidden or low-velocity layer is possible")
    print("     - it is not detectable from first arrivals alone;")
    print("  5. the maximum depth of investigation, set by the longest offset")
    print(f"     (here {xb.max():.0f} m) and the assumption of flat layering.")


if __name__ == "__main__":
    main()
