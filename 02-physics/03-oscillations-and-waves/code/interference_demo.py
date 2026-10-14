"""Superposition, interference and standing waves, quantified.

Run:  python3 interference_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-06. The script:

1. Sums the exact fields of two monochromatic line sources, measures the fringe
   spacing, and compares it with both the exact interference condition
   r1 - r2 = m lambda and the small-angle formula lambda L/d, which differs from
   it by a measurable amount at L/d = 20.
2. Shows that interference redistributes energy rather than creating it: the
   average intensity over a fringe period is exactly the sum of the two
   intensities.
3. Measures the node positions of a standing wave and verifies the profile
   <u^2>_t = 2 A^2 cos^2(kx).
4. Shifts the pattern with a source phase offset, showing that the shift is
   delta lambda L/(2 pi d) on the screen - the phased-array result.

Every number printed below was produced by this script.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def path_difference(x, d, L):
    return math.hypot(x + d / 2.0, L) - math.hypot(x - d / 2.0, L)


def solve_fringe(m, wavelength, d, L, lo=0.0, hi=None):
    """Solve r1 - r2 = m lambda for x > 0 by bisection."""
    if hi is None:
        hi = 2.0 * m * wavelength * L / d + d
    target = m * wavelength

    def f(x):
        return path_difference(x, d, L) - target

    if f(lo) > 0.0:
        return lo
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0.0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def part1_two_sources():
    section("1. Two sources: measuring the fringe spacing")
    wavelength, d, L = 0.5, 2.0, 40.0
    k = 2.0 * math.pi / wavelength
    print(f"wavelength {wavelength} m, source separation d = {d} m, "
          f"screen distance L = {L} m, d/L = {d / L}")
    xs = [-30.0 + 0.001 * i for i in range(60001)]
    intensity = []
    for x in xs:
        r1 = math.hypot(x + d / 2.0, L)
        r2 = math.hypot(x - d / 2.0, L)
        u = (cmath.exp(1j * k * r1) / math.sqrt(r1)
             + cmath.exp(1j * k * r2) / math.sqrt(r2))
        intensity.append(abs(u) ** 2)
    maxima = [xs[i] for i in range(1, len(xs) - 1)
              if intensity[i] > intensity[i - 1] and intensity[i] >= intensity[i + 1]]
    ordered = sorted(maxima, key=abs)[:5]
    # spacing between the two maxima that straddle the axis
    straddle = sorted([m for m in ordered if abs(m) <= 12.0])
    measured = 0.5 * (straddle[-1] - straddle[0])
    small_angle = wavelength * L / d
    exact = solve_fringe(1, wavelength, d, L)
    print(f"maxima nearest the axis (m): "
          f"{', '.join(f'{m:+.4f}' for m in sorted(ordered))}")
    print(f"measured half-spacing of the central pair = {measured:.6f} m")
    print(f"exact condition r1 - r2 = lambda          = {exact:.6f} m "
          f"({(measured - exact) / exact * 100:+.3f} per cent)")
    print(f"small-angle lambda L/d                    = {small_angle:.6f} m "
          f"({(small_angle - exact) / exact * 100:+.3f} per cent)")
    print()
    print("  The exact fringe position solves r1 - r2 = m lambda with the full")
    print("  obliquity; it reduces to x = m lambda L/d only when x << L. At")
    print("  L/d = 20 the small-angle formula is 3.2 per cent below the exact")
    print("  position, while the measured maximum sits 0.36 per cent below the")
    print("  exact one because the 1/sqrt(r) amplitude weighting tilts it. The")
    print("  approximation must be checked, not assumed.")


def part2_energy_conservation():
    section("2. Interference redistributes energy, it does not create it")
    n = 720
    total = 0.0
    for i in range(n):
        c = i / n                       # phase difference in cycles, one full period
        total += abs(1.0 + cmath.exp(2j * math.pi * c)) ** 2
    mean_intensity = total / n
    print(f"mean of |1 + exp(i 2 pi c)|^2 over one full period of c = "
          f"{mean_intensity:.12f}")
    print(f"sum of the two separate intensities (1 + 1)           = 2.000000000000")
    print(f"difference = {mean_intensity - 2.0:+.3e}")
    print()
    print("  Bright fringes are four times brighter than one source alone and dark")
    print("  fringes are dark, but the average is exactly the sum: the interference")
    print("  term integrates to zero over a period. This bookkeeping is the")
    print("  test that a claimed interference effect is physically possible.")


def part3_standing_wave():
    section("3. Standing waves: nodes, antinodes and the energy profile")
    wavelength, amplitude = 1.0, 1.0
    k = 2.0 * math.pi / wavelength
    omega = 2.0 * math.pi                  # period exactly 1 s
    n, steps = 1200, 1000
    xs = [4.0 * i / (n - 1) for i in range(n)]
    times = [i / steps for i in range(steps)]      # exactly one full period
    rows = [[2.0 * amplitude * math.cos(k * x) * math.cos(omega * t) for t in times]
            for x in xs]
    mean_sq = [sum(v * v for v in row) / len(times) for row in rows]
    predicted = [2.0 * amplitude ** 2 * math.cos(k * x) ** 2 for x in xs]
    err = max(abs(mean_sq[i] - predicted[i]) for i in range(n))
    print(f"u(x,t) = 2A cos(kx) cos(omega t), wavelength {wavelength} m, A = 1 m,")
    print(f"averaged over exactly one period")
    print(f"max |<u^2>_t - 2 A^2 cos^2(kx)| over the grid = {err:.3e} m^2")
    nodes = [xs[i] for i in range(1, n - 1)
             if mean_sq[i] < mean_sq[i - 1] and mean_sq[i] <= mean_sq[i + 1]]
    print(f"predicted nodes at odd multiples of lambda/4: "
          f"{', '.join(f'{v:.2f}' for v in [(2 * m + 1) * wavelength / 4.0 for m in range(5)])} m")
    print(f"measured nodes from <u^2>_t:                   "
          f"{', '.join(f'{v:.2f}' for v in nodes[:5])} m")
    print(f"max |u| over the whole field = "
          f"{max(abs(v) for row in rows for v in row):.6f} (predicted 2A = 2.000000)")
    print()
    print("  A standing wave has fixed nodes in space and a single phase everywhere:")
    print("  the two travelling components carry equal and opposite energy fluxes,")
    print("  so the net flux is zero and the resonance stores energy instead of")
    print("  radiating it. That is why a resonant cavity has a high quality factor.")


def part4_phase_offset():
    section("4. A source phase offset steers the pattern")
    wavelength, d, L = 0.5, 2.0, 40.0
    k = 2.0 * math.pi / wavelength
    print(f"predicted screen shift delta lambda L/(2 pi d), exact by bisection on")
    print(f"  k (r1 - r2) = delta")
    print(f"{'delta (rad)':>12} {'measured max x (m)':>20} {'small-angle (m)':>17} "
          f"{'exact (m)':>12}")
    for delta in (0.0, math.pi / 2.0, math.pi):
        best_x, best_i = 0.0, -1.0
        for i in range(0, 50001):           # positive screen half only
            x = 0.0005 * i
            r1 = math.hypot(x + d / 2.0, L)
            r2 = math.hypot(x - d / 2.0, L)
            value = abs(cmath.exp(1j * k * r1) + cmath.exp(1j * (k * r2 + delta))) ** 2
            if value > best_i:
                best_i, best_x = value, x
        small_angle = delta * wavelength * L / (2.0 * math.pi * d)
        # exact: solve path difference = delta / k by bisection
        target = delta / k
        lo, hi = 0.0, 40.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if path_difference(mid, d, L) < target:
                lo = mid
            else:
                hi = mid
        exact = 0.5 * (lo + hi)
        print(f"{delta:12.4f} {best_x:20.5f} {small_angle:17.5f} {exact:12.5f}")
    print()
    print("  A source phase offset shifts the pattern - equivalently, steers the")
    print("  beam. The same statement in the other direction is that a measured")
    print("  phase difference between two receivers locates a source; and the")
    print("  obliquity correction of part 1 applies here too.")


if __name__ == "__main__":
    part1_two_sources()
    part2_energy_conservation()
    part3_standing_wave()
    part4_phase_offset()
