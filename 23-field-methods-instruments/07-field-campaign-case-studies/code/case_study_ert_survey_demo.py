"""Case study: an ERT survey from design to report - synthetic walk-through.

Every number is a chosen teaching value combined with the standard relations
quoted in the accompanying lesson (depth of investigation against electrode
separation, configuration counts and coverage, contact resistance with a
voltage-limited transmitter, Ohm's law on the potential pair, a linear
reciprocal-error model).  No real survey, instrument, vendor figure or measured
dataset is reproduced.
"""

import math
import numpy as np

RNG_SEED = 20261014


def banner(n, text):
    print("=" * 72)
    print(f"{n}. {text}")
    print("=" * 72)


def section_1():
    banner(1, "Geometry from the target depth")
    target = 20.0
    print(f"  target depth {target:.0f} m; modelling choice DOI ~ L_max / 5,")
    print(f"  so the largest spread must be at least {5*target:.0f} m")
    print(f"  {'electrodes':>11}{'spacing (m)':>13}{'line (m)':>10}"
          f"{'L_max (m)':>11}{'DOI (m)':>9}{'lateral sample (m)':>19}")
    for n_elec, sp in ((21, 5.0), (48, 5.0), (48, 2.5), (64, 5.0), (64, 2.0)):
        line = (n_elec - 1) * sp
        print(f"  {n_elec:11d}{sp:13.1f}{line:10.1f}{line:11.1f}{line/5.0:9.1f}"
              f"{sp:19.1f}")
    print("  -> the largest spread sets the depth and the electrode spacing sets")
    print("     the lateral sampling. A 21-electrode line at 5 m just reaches the")
    print("     target depth; the 64-electrode line at 2 m reaches 25 m with 2.5x")
    print("     finer lateral sampling. Depth is bought with length, resolution")
    print("     with electrode count.")
    return 64, 2.0


def section_2(n_elec, s):
    banner(2, "Configurations: how much of the space is used")
    total = math.comb(n_elec, 4)
    n_max = (n_elec - 1) // 3
    used = 0
    for n in range(1, n_max + 1):
        used += 3 * (n_elec - 3 * n)          # alpha, beta, gamma skip-1 patterns
    print(f"  possible 4-electrode configurations C({n_elec},4) = {total:,}")
    print(f"  skip levels used: n = 1..{n_max} at {s:.1f} m spacing")
    print(f"  configurations in a standard protocol = {used:,} "
          f"({100*used/total:.2f} % of the space)")
    print(f"  {'n':>4}{'a (m)':>8}{'spread (m)':>12}{'DOI (m)':>9}{'count':>8}")
    for n in (1, 3, 6, 9, 12, n_max):
        a = n * s
        print(f"  {n:4d}{a:8.1f}{3*a:12.1f}{3*a/5.0:9.1f}{3*(n_elec-3*n):8d}")
    print("  -> the deepest levels cost the fewest configurations and carry the")
    print("     least resolution: the protocol concentrates data near the surface,")
    print("     which is where the inversion's ability to resolve is greatest.")


def section_3(n_elec, s):
    banner(3, "Contact resistance, injected current and the voltage we get back")
    rho, a = 50.0, 10.0
    v_tx = 100.0
    print(f"  transmitter {v_tx:.0f} V, half-space rho = {rho:.1f} ohm m, "
          f"Wenner a = {a:.0f} m")
    print(f"  {'contact each (ohm)':>20}{'I (mA)':>10}{"V_pair (mV)":>13}"
          f"{'V/noise':>18}")
    v_noise = 0.2e-3
    for rc in (500.0, 2000.0, 5000.0, 20000.0):
        i_tx = v_tx / (2.0 * rc + 1000.0)
        v_pair = i_tx * rho / (2.0 * math.pi * a)
        print(f"  {rc:20.1f}{i_tx*1e3:10.2f}{v_pair*1e3:13.3f}"
              f"{v_pair/v_noise:18.1f}")
    print("  -> a 20 kohm contact drops the signal to a few millivolts: the")
    print("     stack count, not the transmitter, then decides whether the data")
    print("     are usable, and the deepest levels suffer most.")


def section_4(n_elec):
    banner(4, "Acquisition time and the cost of stacking")
    per_stack, n_stack = 0.6, 4
    n_meas = 1080
    t_one = per_stack * n_stack
    print(f"  {n_meas} measurements (a subset of the 1953 protocol configurations,")
    print(f"  chosen for depth coverage) at {per_stack:.1f} s per stack x {n_stack} stacks")
    print(f"  {'stacks':>8}{'s per meas':>13}{'time (min)':>13}{'relative noise':>16}")
    for st in (1, 4, 16, 64):
        print(f"  {st:8d}{per_stack*st:13.2f}{n_meas*per_stack*st/60:13.1f}"
              f"{1.0/math.sqrt(st):16.4f}")
    print(f"  one line at 4 stacks = {n_meas*t_one/60:.1f} min of acquisition,")
    print("  plus electrode moves: a realistic 0.6-1.0 day per line and crew")
    print("  -> stacking buys sqrt(N) in noise for N times the time; 4 stacks")
    print("     costs 45 min and buys a factor 2, 64 stacks costs 12 h and buys 8x.")


def section_5(n_elec, s):
    banner(5, "What the inversion can and cannot resolve")
    n_data = 1080
    print(f"  {'model cells':>13}{'data':>8}{'cells/data':>12}{'status':>22}")
    for n_cells in (100, 500, 1080, 2000, 10000):
        status = "over-determined" if n_cells < n_data else "under-determined"
        print(f"  {n_cells:13d}{n_data:8d}{n_cells/n_data:12.2f}{status:>22}")
    print("  -> the model must have fewer cells than the data can constrain; the")
    print("     standard practice is a coarse mesh with smoothing, and the reported")
    print("     resolution is then a property of the mesh as much as of the data.")
    rng = np.random.default_rng(RNG_SEED)
    r = rng.normal(0.0, 0.008, 1080)
    print(f"  synthetic reciprocal errors: mean {r.mean()*100:+.3f} %, "
          f"sd {r.std()*100:.3f} %")
    keep = np.abs(r) < 0.05
    print(f"  data outside a 5 % reciprocal tolerance: {int((~keep).sum())} "
          f"({100*(~keep).mean():.2f} %)")
    print(f"  as a data-weight model: epsilon = 0.005 |V| + 0.2 mV")
    print("  -> the error model, not the inversion algorithm, sets how much")
    print("     structure the model can contain without fitting noise.")


def main():
    print()
    banner(0, "CASE STUDY: AN ERT SURVEY: SYNTHETIC WALK-THROUGH")
    n_elec, s = section_1()
    section_2(n_elec, s)
    section_3(n_elec, s)
    section_4(n_elec)
    section_5(n_elec, s)
    print()
    print("SYNTHETIC: every number above is a chosen parameter in this file combined")
    print("with the standard relations quoted in the lesson; no real survey,")
    print("instrument or measured dataset is reproduced.")


if __name__ == "__main__":
    main()
