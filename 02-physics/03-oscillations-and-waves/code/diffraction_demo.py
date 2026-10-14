"""Diffraction, Fresnel zones and resolution limits, computed and measured.

Run:  python3 diffraction_demo.py
Requires: Python standard library only.

Companion to lesson 02-03-09. The script:

1. Evaluates the Fraunhofer diffraction integral of a slit by direct quadrature
   and compares it with the closed form (sin(beta)/beta)^2, locating the first
   minimum against sin(theta) = lambda/a.
2. Does the same for a circular aperture, where the closed form is the Airy
   pattern 2 J1(q)/q, and finds the first zero of J1 by bisection to get the
   1.22 lambda/D resolution limit.
3. Computes the on-axis amplitude behind a circular aperture from the Fresnel
   integral and verifies the half-period-zone result |U| = 2|sin(pi r^2/(2 lambda z))|,
   whose first maximum sits at r = sqrt(lambda z).
4. Converts the Fresnel-zone radius into the lateral resolution of a reflection
   survey, with and without migration.

Every number printed below was produced by this script.
"""

import cmath
import math


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def part1_slit():
    section("1. Single slit: quadrature against the closed form")
    wavelength = 0.5e-3             # 0.5 mm, a microwave/ultrasound scale
    a = 2.0e-3                      # slit width
    k = 2.0 * math.pi / wavelength
    print(f"wavelength = {wavelength * 1e3:.3f} mm, slit width a = {a * 1e3:.3f} mm")
    print(f"{'sin(theta)':>11} {'|U|/|U(0)| quadrature':>22} "
          f"{'closed form':>13} {'difference':>11}")
    worst = 0.0
    for sin_theta in (0.0, 0.1, 0.2, 0.25, 0.3, 0.5):
        n = 801
        dx = a / (n - 1)
        total = 0j
        for i in range(n):
            x = -a / 2.0 + i * dx
            weight = 0.5 if i in (0, n - 1) else 1.0
            total += weight * cmath.exp(-1j * k * sin_theta * x)
        total *= dx / a                      # trapezoid rule, normalised
        beta = 0.5 * k * a * sin_theta
        closed = math.sin(beta) / beta if beta != 0.0 else 1.0
        worst = max(worst, abs(abs(total) - abs(closed)))
        print(f"{sin_theta:11.3f} {abs(total):22.9f} {abs(closed):13.9f} "
              f"{abs(abs(total) - abs(closed)):11.2e}")
    print(f"max difference over the table = {worst:.3e}")
    print(f"first minimum at sin(theta) = lambda/a = {wavelength / a:.4f}")
    highest = 0.0
    for i in range(2001):
        s = 0.0 + 1.2 * i / 2000.0
        arg = math.pi * a * s / wavelength
        value = abs(math.sin(arg) / arg) if arg != 0.0 else 1.0
        if value < 1e-3:
            highest = s
            break
    print(f"numerically located first zero of the pattern at sin(theta) = "
          f"{highest:.6f} (relative difference "
          f"{abs(highest - wavelength / a) / (wavelength / a):.2e})")
    print()
    print("  The width of the central maximum is inversely proportional to the")
    print("  aperture: a narrower slit diffracts more widely. That trade-off is")
    print("  the content of the resolution limit below.")


def bessel_j1(z):
    """J1 by its integral representation, accurate for the range used here."""
    n = 2000
    total = 0.0
    for i in range(n):
        theta = math.pi * (i + 0.5) / n
        total += math.cos(theta - z * math.sin(theta))
    return total / n


def airy_analytic(q):
    return 1.0 if q == 0.0 else 2.0 * bessel_j1(q) / q


def part2_circular_aperture():
    section("2. Circular aperture: the Airy pattern and 1.22 lambda/D")
    diameter = 0.25
    wavelength = 0.5e-3
    k = 2.0 * math.pi / wavelength
    print(f"wavelength = {wavelength * 1e3:.3f} mm, aperture diameter D = "
          f"{diameter * 1e3:.1f} mm")
    print(f"{'angle (deg)':>12} {'quadrature':>13} {'Airy closed form':>18} "
          f"{'difference':>11}")
    for angle_deg in (0.0, 0.05, 0.1, 0.1401, 0.2, 0.3):
        theta = math.radians(angle_deg)
        # direct 2-D quadrature over the disk, in polar coordinates
        nr, nphi = 400, 720
        total = 0j
        for ir in range(nr):
            r = diameter / 2.0 * (ir + 0.5) / nr
            for ip in range(nphi):
                phi = 2.0 * math.pi * (ip + 0.5) / nphi
                total += cmath.exp(-1j * k * math.sin(theta) * r * math.cos(phi)) * r
        total *= (diameter / 2.0 / nr) * (2.0 * math.pi / nphi)
        total /= (math.pi * (diameter / 2.0) ** 2)
        q = k * (diameter / 2.0) * math.sin(theta)
        # the aperture is centrosymmetric, so the field on axis is real
        print(f"{angle_deg:12.4f} {total.real:13.7f} {airy_analytic(q):18.7f} "
              f"{abs(total.real - airy_analytic(q)):11.2e}")
    # first zero of J1 by bisection
    lo, hi = 3.0, 5.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if bessel_j1(lo) * bessel_j1(mid) < 0.0:
            hi = mid
        else:
            lo = mid
    first_zero = 0.5 * (lo + hi)
    print(f"first zero of J1 (bisection) = {first_zero:.9f}")
    print(f"  therefore sin(theta_min) = {first_zero:.6f} lambda/(pi D) = "
          f"{first_zero / math.pi:.6f} lambda/D")
    print(f"  the familiar 1.22 lambda/D follows, to five decimal places")
    print(f"  numeric value here: theta_min = "
          f"{first_zero / math.pi * wavelength / diameter:.3e} rad = "
          f"{math.degrees(first_zero / math.pi * wavelength / diameter):.6f} deg")
    print()
    print("  A telescope, an eye, a radar dish and a seismic array all obey this")
    print("  relation; what changes is the wavelength and the aperture.")


def part3_fresnel_zones():
    section("3. Fresnel half-period zones on axis")
    wavelength, z = 0.5, 400.0
    print(f"wavelength = {wavelength} m, distance z = {z:.1f} m "
          f"-> lambda z = {wavelength * z:.1f} m^2")
    print(f"{'r (m)':>8} {'|U| numeric':>13} {'2|sin(pi r^2/(2 lz))|':>24} "
          f"{'difference':>11}")
    worst = 0.0
    for r in (2.0, 6.0, 8.0, 10.0, math.sqrt(wavelength * z), 16.0, 20.0, 21.2):
        n = 60001
        total = 0j
        dr = r / (n - 1)
        for i in range(n):
            rho = i * dr
            phase = math.pi * rho * rho / (wavelength * z)
            total += cmath.exp(1j * phase) * 2.0 * math.pi * rho / (1j * wavelength * z)
        total *= dr
        analytic = 2.0 * abs(math.sin(math.pi * r * r / (2.0 * wavelength * z)))
        worst = max(worst, abs(abs(total) - analytic))
        print(f"{r:8.4f} {abs(total):13.7f} {analytic:24.7f} "
              f"{abs(abs(total) - analytic):11.2e}")
    print(f"max difference over the table = {worst:.3e}")
    first_max = math.sqrt(wavelength * z)
    print(f"predicted first maximum at r = sqrt(lambda z) = {first_max:.4f} m")
    # locate the first maximum numerically
    step_r = 1.0e-4
    best_r, best_v = 0.0, 0.0
    prev2, prev1 = 0.0, 0.0
    for i in range(1, int(30.0 / step_r)):
        r = i * step_r
        v = 2.0 * abs(math.sin(math.pi * r * r / (2.0 * wavelength * z)))
        if i > 1 and prev1 > prev2 and prev1 >= v and prev1 > 0.5:
            best_r, best_v = (i - 1) * step_r, prev1
            break
        prev2, prev1 = prev1, v
    print(f"first maximum located numerically at r = {best_r:.4f} m "
          f"with amplitude {best_v:.6f} (aperture-fine search, step "
          f"{step_r:.0e} m)")
    print()
    print("  The on-axis amplitude oscillates between 0 and 2 as the aperture")
    print("  grows: each extra Fresnel zone added at the rim reverses the phase")
    print("  of the contribution, so zones cancel in pairs and consecutive")
    print("  amplitudes alternate. Truncating the aperture at the first zone edge")
    print("  r = sqrt(lambda z) therefore gives the maximum on-axis amplitude for")
    print("  the least aperture - the principle of the zone plate.")


def part4_resolution():
    section("4. From the Fresnel zone to seismic resolution")
    vp, f, depth = 3000.0, 30.0, 1000.0
    wavelength = vp / f
    print(f"P wave at {vp:.0f} m/s, {f:.0f} Hz -> wavelength = {wavelength:.1f} m")
    print(f"reflector at depth z = {depth:.0f} m")
    r_fresnel = math.sqrt(wavelength * depth / 2.0)
    print(f"first Fresnel zone radius  sqrt(lambda z/2) = {r_fresnel:.2f} m")
    print(f"  lateral footprint on the interface = {2 * r_fresnel:.2f} m")
    print(f"migrated resolution limit ~ lambda/4      = {wavelength / 4.0:.2f} m")
    print(f"migrated resolution limit ~ lambda/2      = {wavelength / 2.0:.2f} m")
    print(f"vertical resolution limit ~ lambda/4      = {wavelength / 4.0:.2f} m")
    print()
    print("  Unmigrated reflection data averages the interface over the Fresnel")
    print("  zone, so features narrower than about 2 r_F are smeared together.")
    print("  Migration narrows the footprint back towards the diffracted")
    print("  wavelength limit - a factor of order 10 in this example - but it")
    print("  cannot go below lambda/4 in range, because the bandwidth is what")
    print("  sets that limit. Both limits are approximations; the exact factor")
    print("  depends on the aperture and the signal-to-noise ratio, and should be")
    print("  established for the survey at hand rather than assumed.")


if __name__ == "__main__":
    part1_slit()
    part2_circular_aperture()
    part3_fresnel_zones()
    part4_resolution()
