"""Conditionals, loops and loop-invariant reasoning on a survey line.

Run:  python3 control_flow_demo.py
Requires: Python standard library only.

Companion to lesson 03-01-03.  This script measures the cost of recomputing a
loop invariant inside the loop body, which is the practical face of the
question "which values change from iteration to iteration?".

Demonstrates:

1. if / elif / else, and the trap of comparing floats for equality.
2. A for-loop over survey stations with break, continue and for-else.
3. Range, enumerate and zip in the three idioms you actually need.
4. Loop-invariant hoisting, timed before and after.
5. A while loop: Newton iteration for the depth of a compact body.
6. Nested loops and the accumulator pattern.
"""

import math
import time

from geophys_core import (G, M_PER_S2_PER_MGAL, REFERENCE_DENSITY,
                          bouguer_slab_mgal, sphere_mass)

DELTA_RHO = 300.0
RADIUS = 200.0
DEPTH = 500.0
N_STATIONS = 100_000
STATION_SPACING = 10.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def part1_conditionals():
    section("1. Conditionals: classify an anomaly, not a float")
    def classify(peak_mgal):
        if peak_mgal < 0.05:
            return "at noise level"
        elif peak_mgal < 0.5:
            return "a weak target"
        elif peak_mgal < 5.0:
            return "a routine exploration target"
        else:
            return "a strong target or a regional gradient"

    for peak in (0.02, 0.2684, 1.5, 12.0):
        print(f"  peak = {peak:>7.4f} mGal  -> {classify(peak)}")
    print()
    print("  The comparison is against thresholds in mGal, never against")
    print("  0.268390 == 0.268390: rounded measurement values must be compared")
    print("  with math.isclose, because the two sides are different doubles.")


def part2_loops():
    section("2. Loops: break, continue, and a search that is allowed to fail")
    offsets = [0.0, 100.0, 250.0, 500.0, 900.0, 1500.0]

    def anomaly(x):
        mass = sphere_mass(RADIUS, DELTA_RHO)
        r2 = x * x + DEPTH * DEPTH
        return G * mass * DEPTH / r2 ** 1.5 / M_PER_S2_PER_MGAL

    print("  Looking for the first station where the anomaly drops below")
    print("  0.05 mGal (the 'edge' of the body):")
    for x in offsets:
        g = anomaly(x)
        if g < 0.05:
            print(f"    offset {x:>7.1f} m: {g:.6f} mGal -> first edge found")
            break
        print(f"    offset {x:>7.1f} m: {g:.6f} mGal -> still anomalous")
    else:
        print("    no edge within the line: the loop ran to completion")
    print()
    print("  The for-else clause is not decoration.  'for ... else' runs the")
    print("  else branch only if no break happened, which expresses 'search")
    print("  failed' without a sentinel flag - and a sentinel flag is where the")
    print("  off-by-one bugs live.")


def part3_idioms():
    section("3. The three loop idioms you need most")
    stations = ["STA01", "STA02", "STA03"]
    elevations = [112.4, 118.9, 121.7]
    print(f"  enumerate : {[(i, s) for i, s in enumerate(stations)]}")
    print(f"  zip       : {[(s, h) for s, h in zip(stations, elevations)]}")
    print(f"  sum/genexp: total lift = {sum(e - elevations[0] for e in elevations):.1f} m")
    print()
    print("  enumerate gives you the index without arithmetic; zip walks two")
    print("  sequences in lockstep without indexing either.  Both remove the")
    print("  chance of an index-bookkeeping error.")


def part4_hoisting():
    section("4a. Loop-invariant hoisting, measured")
    print("  We evaluate a synthetic profile twice with identical arithmetic.")
    print("  Version A recomputes the source mass inside the loop; version B")
    print("  hoists it out, because the mass does not depend on the station.")
    print()

    def version_a():
        total = 0.0
        for i in range(N_STATIONS):
            x = i * STATION_SPACING
            mass = sphere_mass(RADIUS, DELTA_RHO)
            r2 = x * x + DEPTH * DEPTH
            total += G * mass * DEPTH / r2 ** 1.5 / M_PER_S2_PER_MGAL
        return total

    def version_b():
        total = 0.0
        mass = sphere_mass(RADIUS, DELTA_RHO)
        for i in range(N_STATIONS):
            x = i * STATION_SPACING
            r2 = x * x + DEPTH * DEPTH
            total += G * mass * DEPTH / r2 ** 1.5 / M_PER_S2_PER_MGAL
        return total

    t0 = time.perf_counter()
    a = version_a()
    ta = time.perf_counter() - t0
    t0 = time.perf_counter()
    b = version_b()
    tb = time.perf_counter() - t0
    print(f"  A: mass recomputed inside loop  {ta:.3f} s   sum = {a:.6f}")
    print(f"  B: mass hoisted                 {tb:.3f} s   sum = {b:.6f}")
    print(f"  identical results               {(a == b)}")
    print(f"  speed-up                        {ta / tb:.2f}x")
    print()
    print("  Be honest about the size of the win: a factor of two here, because")
    print("  the hoisted quantity is two multiplications and a function call")
    print("  repeated over a loop body of about ten operations.  Hoisting is not")
    print("  where the big factors live - vectorisation is (module 03-02) - but")
    print("  the *reasoning* is compulsory, because the same judgement decides")
    print("  what may be moved out of the loop at all.")

    section("4b. The invariant test has teeth: hoisting a loop-variant is a bug")
    mean_h = 120.0
    print("  A Bouguer reduction needs the elevation of every station.  Below,")
    print("  elevations vary along the line by a synthetic sine with an 8 m")
    print("  amplitude, and the slab correction is 2*pi*G*rho*h =")
    print(f"  {2 * math.pi * 6.67430e-11 * REFERENCE_DENSITY / 1e-5:.4f} mGal per metre of elevation.")
    print()
    print(f"  {'station':>8}{'h (m)':>10}{'correct (mGal)':>16}"
          f"{'hoisted-mean (mGal)':>21}{'error (mGal)':>14}")
    worst = 0.0
    for i in (0, 125, 250, 500, 750, 875, 1000):
        h = mean_h + 8.0 * math.sin(2.0 * math.pi * i / 1000.0)
        correct = 2.0 * math.pi * G * REFERENCE_DENSITY * h / M_PER_S2_PER_MGAL
        wrong = 2.0 * math.pi * G * REFERENCE_DENSITY * mean_h / M_PER_S2_PER_MGAL
        worst = max(worst, abs(correct - wrong))
        print(f"  {i:>8}{h:>10.3f}{correct:>16.4f}{wrong:>21.4f}"
              f"{correct - wrong:>14.4f}")
    print()
    print(f"  Worst error from hoisting the mean elevation: {worst:.4f} mGal,")
    print("  which is larger than the 0.268 mGal target anomaly of lesson 01.")
    print("  Hoisting a genuinely invariant quantity is free; hoisting a")
    print("  variant one is a silent, plausible, survey-destroying bug.  The")
    print("  loop-invariance test is a *correctness* tool first and a speed")
    print("  tool second.")


def part5_newton():
    section("5. A while loop: inverting the anomaly for depth")
    target = 0.268390          # mGal, the peak from lesson 01
    mass = sphere_mass(RADIUS, DELTA_RHO)
    # g(z) = G*M/z^2 for a station directly over the centre.
    print(f"  target peak  = {target:.6f} mGal")
    print("  solve  G*M/z^2 = target  for z by Newton iteration")
    print(f"  initial guess z0 = 1000.0 m (a survey knows the depth to a factor)")
    print(f"  {'iteration':>9}  {'z (m)':>18}  {'|change| (m)':>14}")
    z = 1000.0
    for iteration in range(1, 21):
        f = G * mass / z ** 2 / M_PER_S2_PER_MGAL - target
        df = -2.0 * G * mass / z ** 3 / M_PER_S2_PER_MGAL
        # g depends on z^2 only, so both +z and -z solve the equation; the
        # first Newton step overshoots through zero to -500 m.  We keep the
        # physical branch by taking the magnitude after each step.
        z_next = abs(z - f / df)
        print(f"  {iteration:>9}  {z_next:>18.9f}  {abs(z_next - z):>14.2e}")
        if abs(z_next - z) < 1e-12:
            z = z_next
            break
        z = z_next
    print(f"  recovered depth = {z:.9f} m  (true value {DEPTH:.1f} m)")
    print(f"  iterations used = {iteration}")
    print()
    print("  Convergence is quadratic: the number of correct digits roughly")
    print("  doubles each step, which is why four iterations suffice from a")
    print("  guess 100 per cent too deep.  The residual 4.4e-4 m is not solver")
    print("  error: the target was the *rounded* value 0.268390 mGal from")
    print("  lesson 01, while the model peak is 0.26838953 mGal, and")
    print("  dz/dg = -z/(2g) = -931.5 m per mGal magnifies the 4.7e-7 mGal")
    print("  rounding to 4.4e-4 m.  Inversion amplifies input error; that is")
    print("  lesson one of module 18.")
    print()
    print("  A while loop with a tolerance is the right tool, and the iteration")
    print("  is only as good as its starting point: the same Newton step started")
    print("  from a nonsense guess of 0.27 m grows by a factor 1.5 each")
    print("  iteration and needs about 19 steps to come back.  Initial guesses")
    print("  are part of the algorithm, not a detail.")


def part6_accumulators():
    section("6. Nested loops and the accumulation pattern")
    lines = {"L1": [110.0, 240.0, 5.0], "L2": [95.0, 260.0, 12.0]}
    print("  A mini Bouguer reduction over two lines:")
    print(f"  {'line':<5}{'stations':>9}{'mean h (m)':>12}{'slab (mGal)':>13}")
    for name, heights in lines.items():
        count = 0
        total = 0.0
        for h in heights:
            count += 1
            total += h
        mean_h = total / count
        print(f"  {name:<5}{count:>9}{mean_h:>12.2f}"
              f"{bouguer_slab_mgal(mean_h, REFERENCE_DENSITY):>13.4f}")
    print()
    print("  The inner loop is the accumulator; the outer loop is the grouping.")
    print("  In lesson 05 the same pattern becomes a dict of lists, and in")
    print("  module 03-04 it becomes a one-line group-by.")


if __name__ == "__main__":
    part1_conditionals()
    part2_loops()
    part3_idioms()
    part4_hoisting()
    part5_newton()
    part6_accumulators()
