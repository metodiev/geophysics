"""Why Python for geophysics: what the language gives you before any library.

Run:  python3 why_python_demo.py
Requires: Python standard library only (no NumPy, no SciPy, no ObsPy).

Companion to lesson 03-01-01.  The point of this script is that *the floor is
already usable*: a complete gravity forward model, a survey-wide profile and a
timing measurement can be written with nothing but the standard library.  The
ecosystem adds speed and breadth on top of that floor; it does not substitute
for it.

Demonstrates:

1. A buried-sphere gravity anomaly computed from first principles.
2. A 200,000-station survey profile timed end-to-end.
3. The cross-over point where a vectorised library would pay for itself.
4. The one real limitation of the standard library: raw speed.
"""

import math
import time

from geophys_core import G, M_PER_S2_PER_MGAL, sphere_mass

# SYNTHETIC target: a compact body, nominal parameters chosen for illustration.
DELTA_RHO = 300.0      # kg m^-3, excess density over the host rock
RADIUS = 200.0         # m
DEPTH = 500.0          # m to the body centre
PROFILE_LENGTH = 4000.0  # m, station spacing 20 m
STATION_SPACING = 20.0


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def anomaly_mgal(x):
    """Vertical anomaly of the sphere directly beneath the origin at offset x.

    g_z = G * M * z / (x^2 + z^2)^{3/2}, converted from m/s^2 to mGal.
    """
    mass = sphere_mass(RADIUS, DELTA_RHO)
    r2 = x * x + DEPTH * DEPTH
    return G * mass * DEPTH / r2 ** 1.5 / M_PER_S2_PER_MGAL


def part1_single_station():
    section("1. One station, six lines of physics")
    mass = sphere_mass(RADIUS, DELTA_RHO)
    peak = anomaly_mgal(0.0)
    print(f"  excess density  delta_rho = {DELTA_RHO:,.0f} kg/m^3")
    print(f"  body radius     a         = {RADIUS:,.0f} m")
    print(f"  centre depth    z         = {DEPTH:,.0f} m")
    print(f"  mass contrast   M         = {mass:.6e} kg")
    print(f"  peak anomaly    g_z(0)    = {peak:.6f} mGal")
    print()
    print("  Offset (m)   anomaly (mGal)   fraction of peak")
    for x in (0.0, 200.0, 400.0, 600.0, 800.0, 1000.0):
        g = anomaly_mgal(x)
        print(f"  {x:>10.1f}   {g:>14.6f}   {g / peak:>15.4f}")
    print()
    print("  The half-width (fraction 0.5) falls near x = z * sqrt(2^{2/3}-1)")
    print(f"  = {DEPTH * math.sqrt(2 ** (2 / 3) - 1):.1f} m, i.e. the curve")
    print("  encodes the depth.  That is the whole basis of depth estimation")
    print("  from a single anomaly profile.")


def part2_profile_timing():
    section("2. A 200,000-station profile, standard library only")
    n = 200_000
    start = time.perf_counter()
    peak = 0.0
    total = 0.0
    for i in range(n):
        x = -PROFILE_LENGTH / 2 + i * (PROFILE_LENGTH / (n - 1))
        g = anomaly_mgal(x)
        total += g
        if g > peak:
            peak = g
    elapsed = time.perf_counter() - start
    print(f"  stations computed      : {n:,}")
    print(f"  station spacing        : {PROFILE_LENGTH / (n - 1) * 1000:.3f} mm")
    print(f"  peak anomaly recovered : {peak:.6f} mGal")
    print(f"  mean anomaly over line : {total / n:.6f} mGal")
    print(f"  wall-clock time        : {elapsed:.3f} s")
    print(f"  per-station cost       : {elapsed / n * 1e9:.0f} ns")
    print()
    print("  The spacing printed above is deliberately absurd: 200,000 stations")
    print("  over 4 km is 20 mm, far below any survey.  It is here only to make")
    print("  the timing measurable on a laptop.")


def part3_crossover():
    section("3. What the numbers say about the crossover")
    print("  Interpreter overhead dominates at the single-station level:")
    print("  the arithmetic in anomaly_mgal() is a handful of flops, but the")
    print("  function call and the Python bytecode are not.")
    print()
    print("  Empirically, pure-Python numeric kernels run roughly 10x-100x")
    print("  slower than an equivalent compiled loop, and the gap widens as the")
    print("  kernel gets simpler.  That is the honest case for NumPy in")
    print("  module 03-02 - and it is a *performance* case, not a correctness")
    print("  case.  The standard-library version above is exactly as accurate as")
    print("  the vectorised one, because both use IEEE-754 doubles throughout.")


def part4_what_you_get():
    section("4. What the language gives you before any library")
    for feature, why in (
        ("int", "arbitrary precision - no overflow on event counts"),
        ("float", "IEEE-754 double, same bits as C, Fortran and NumPy"),
        ("complex", "native complex arithmetic for Fourier and impedance work"),
        ("math", "libm: trig, log, gamma, hypot, and correct rounding edge cases"),
        ("csv", "RFC-4180 quoting handled for you - see lesson 06"),
        ("statistics", "mean, median and variance without a dependency"),
        ("decimal / fractions", "exact decimal and rational arithmetic for audits"),
        ("random", "seeded Mersenne Twister - reproducible synthetic data"),
        ("pathlib", "portable paths, no string joining with '/'"),
        ("timeit / time", "measure before you optimise - see lesson 05"),
    ):
        print(f"  {feature:<20} {why}")


if __name__ == "__main__":
    part1_single_station()
    part2_profile_timing()
    part3_crossover()
    part4_what_you_get()
    print(f"\nPython version used: {__import__('sys').version.split()[0]}")
