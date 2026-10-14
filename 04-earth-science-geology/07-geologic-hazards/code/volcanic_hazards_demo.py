"""Volcanic hazards, monitoring and precursors: what a measurement can decide.

Run:  .venv/bin/python volcanic_hazards_demo.py
Requires: numpy.

Companion to lesson 04-07-02.

Four computations, chosen because each one supports a statement the lesson
makes:

1. Mogi point-source deformation.  The far-field decay is 1/r^3 in the
   numerator and the surface tilt peaks at half the source depth.  Both are
   derived, and the predicted deformation is compared with the precision of
   GNSS and InSAR.
2. Microgravity from an intrusion, from the attraction of a compact mass.
3. Plume height scaling from dimensional analysis: H proportional to the
   quarter power of the buoyancy flux.  The exponent is derived; the
   dimensionless constant is not, and is labelled empirical.
4. The precursor problem as a Bayesian statement.  This is the quantitative
   core of the lesson's honesty: with a realistic base rate, a sensitive
   precursor still gives a low probability of eruption, and the false-alarm
   rate needed for a reliable warning is computed rather than asserted.

Nothing here is a volcano, an eruption, or a monitoring record.  Every scenario
is synthetic and labelled.
"""

import math

import numpy as np

G = 6.67430e-11       # m^3 kg^-1 s^-2, exact-by-convention CODATA value
RHO_W = 1030.0        # kg/m^3, seawater-ish, NOMINAL


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# --------------------------------------------------------------------------
# 1. Mogi source
# --------------------------------------------------------------------------

def mogi_uz(r, d, strength):
    """Vertical surface displacement of a Mogi point pressure source.

    u_z(r) = C * d / (r^2 + d^2)^(3/2), with C = 3 a^3 dP / (4 mu) the source
    strength (units of volume).  The half-space Green's function behind this
    expression is Mogi's solution; the ampitude coefficient is quoted, the
    r- and d-dependence is what the script tests.
    """
    return strength * d / (r * r + d * d) ** 1.5


def mogi_ur(r, d, strength):
    return strength * r / (r * r + d * d) ** 1.5


def part1():
    section("1. Mogi point source: deformation and tilt")
    a = 1000.0        # m, source radius
    dP = 10.0e6       # Pa, pressure change
    mu = 30.0e9       # Pa, shear modulus (NOMINAL crustal)
    d = 3000.0        # m, source depth
    print("SYNTHETIC source (a, dP, mu, depth chosen for arithmetic)")
    print(f"  source radius a      = {a:.0f} m")
    print(f"  pressure change dP   = {dP/1e6:.1f} MPa")
    print(f"  shear modulus mu     = {mu/1e9:.1f} GPa  (NOMINAL)")
    print(f"  source depth d       = {d:.0f} m")

    # Pressurised spherical cavity in an infinite elastic medium:
    #   u_r(a) = a dP / (4 mu), so dV = 4 pi a^2 u_r(a) = pi a^3 dP / mu.
    u_wall = a * dP / (4.0 * mu)
    dV = 4.0 * math.pi * a * a * u_wall
    strength = 3.0 * a ** 3 * dP / (4.0 * mu)
    print()
    print("  Pressurised spherical cavity (derivable part):")
    print(f"    wall displacement u(a) = a dP/(4 mu) = {u_wall:.6f} m")
    print(f"    cavity volume change dV = pi a^3 dP/mu = {dV:.6e} m^3  (derived)")
    print(f"    Mogi strength C = 3a^3 dP/(4 mu)       = {strength:.6e} m^3")
    print(f"    C / dV = 3/(4 pi) = {strength/dV:.6f}")
    print()
    print(f"  maximum uplift u_z(0) = C/d^2 = {mogi_uz(0.0, d, strength):.6f} m"
          f"  ({mogi_uz(0.0, d, strength)*1e3:.2f} mm)")
    print()
    print("     r (km)   u_z (mm)   u_r (mm)   u_r/u_z   far-field r^3 u_z / C")
    for r_km in (0.0, 0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0):
        r = r_km * 1e3
        uz = mogi_uz(r, d, strength)
        ur = mogi_ur(r, d, strength)
        ratio = ur / uz if uz != 0 else float("nan")
        far = (r ** 3 * uz / strength) if r > 0 else float("nan")
        print(f"  {r_km:8.1f}   {uz*1e3:8.4f}   {ur*1e3:8.4f}   {ratio:8.4f}"
              f"   {far:10.6f}")
    print()
    print("  u_r = u_z exactly at r = d, and the far-field column tends to d,")
    print("  which is the statement that u_z ~ C d / r^3: the decay is a dipole")
    print("  (1/r^3), not a monopole (1/r^2).")
    print()
    r_scan = np.linspace(1.0, 20e3, 200001)
    tilt = np.abs(np.gradient(mogi_uz(r_scan, d, strength), r_scan))
    i = int(np.argmax(tilt))
    print(f"  tilt |du_z/dr| peaks at r = {r_scan[i]/1e3:.4f} km, "
          f"against d/2 = {d/2000:.4f} km")
    print(f"  peak tilt = {tilt[i]:.6e} rad = {tilt[i]*1e6:.3f} microrad")
    print("  (a borehole tiltmeter resolves ~0.01 microrad, a GNSS daily")
    print("  solution resolves ~1 mm of displacement: both see this source.)")


# --------------------------------------------------------------------------
# 2. Microgravity
# --------------------------------------------------------------------------

def part2():
    section("2. Microgravity from a compact mass change")
    r_body = 1000.0      # m
    drho = 300.0         # kg/m^3
    d = 3000.0
    vol = 4.0 / 3.0 * math.pi * r_body ** 3
    dg = G * vol * drho / d ** 2
    print("SYNTHETIC intrusion (a sphere, so the attraction is exact)")
    print(f"  body radius     = {r_body:.0f} m")
    print(f"  density change  = {drho:.0f} kg/m^3")
    print(f"  centre depth    = {d:.0f} m")
    print(f"  volume          = {vol:.6e} m^3")
    print(f"  dg = G dV drho / d^2 = {dg:.6e} m/s^2 = {dg/1e-5:.4f} mGal")
    print()
    print("  For comparison, a modern relative gravimeter repeatability is")
    print("  a few microgal and a survey is usually repeatable to 5-10 microgal:")
    print(f"  this signal is {dg/1e-8:.1f} microgal, so it is detectable, and")
    print("  the depth is what makes it hard: dg scales as 1/d^2, so the same")
    print("  body at 10 km depth would give "
          f"{G*vol*drho/(10000.0**2)/1e-8:.2f} microgal.")
    print()
    print("  dg vs depth for the same body:")
    for dd in (1000.0, 2000.0, 5000.0, 10000.0):
        print(f"    depth {dd/1000:5.1f} km -> {G*vol*drho/dd**2/1e-8:10.4f} microgal")


# --------------------------------------------------------------------------
# 3. Plume height scaling
# --------------------------------------------------------------------------

def part3():
    section("3. Plume height: the 1/4-power law, from dimensions")
    print("Dimensional analysis.  A buoyant plume in a stratified atmosphere has")
    print("  buoyancy flux F [L^4 T^-3],  buoyancy frequency N [T^-1],")
    print("  height H [L].  The only combination giving a length is")
    print("  H = C (F / N^3)^(1/4), so H scales as the QUARTER power of F.")
    print()
    f_ref = 1.0e6      # m^4/s^3, an arbitrary reference
    n_air = 0.012      # s^-1, NOMINAL tropospheric buoyancy frequency
    print(f"  reference buoyancy flux F = {f_ref:.3e} m^4/s^3")
    print(f"  buoyancy frequency N      = {n_air:.3f} s^-1  (NOMINAL)")
    print(f"  (F/N^3)^(1/4)            = {(f_ref/n_air**3)**0.25:.1f} m")
    print()
    print("   F ratio   H ratio  = (F2/F1)^(1/4)")
    for ratio in (0.5, 2.0, 4.0, 16.0):
        print(f"  {ratio:8.2f}   {ratio**0.25:14.4f}")
    print()
    print("  Consequence: a factor of 16 in eruption rate is only a factor of 2")
    print("  in column height.  The constant C is empirical (of order 1.7-2.5")
    print("  in the literature) and is NOT derived here, so no absolute height")
    print("  is quoted.")


# --------------------------------------------------------------------------
# 4. The precursor problem
# --------------------------------------------------------------------------

def posterior(p_erupt, sensitivity, false_alarm):
    """P(eruption | precursor) from Bayes, with a stated base rate."""
    a = sensitivity * p_erupt
    return a / (a + false_alarm * (1.0 - p_erupt))


def part4():
    section("4. Precursors are ambiguous: a Bayesian statement of why")
    print("Assume one monitoring interval (say one year) per volcano, an annual")
    print("eruption probability p, a precursor sensitivity s, and a")
    print("false-positive rate f (a precursor without an eruption).")
    print()
    print("  p(erupt)   sensitivity   false alarm   P(erupt | precursor)")
    rows = [
        (0.01, 0.90, 0.20),
        (0.01, 0.90, 0.05),
        (0.01, 0.90, 0.01),
        (0.01, 0.99, 0.05),
        (0.10, 0.90, 0.05),
        (0.30, 0.90, 0.05),
    ]
    for p, s, f in rows:
        print(f"  {p:9.2f}   {s:11.2f}   {f:11.2f}   {posterior(p, s, f):18.4f}")
    print()
    print("  With a 1 per cent base rate, a 90 per cent sensitivity and a 5 per")
    print("  cent false-alarm rate, a precursor raises the probability from 1 per")
    print("  cent to 15 per cent.  That is a real gain and it is nowhere near a")
    print("  prediction.")
    print()
    p, s = 0.01, 0.90
    print("  False-alarm rate needed for a given posterior, at p = 0.01, s = 0.90:")
    for target in (0.5, 0.8, 0.9, 0.99):
        f = s * p * (1.0 - target) / (target * (1.0 - p))
        print(f"    P = {target:4.2f} requires f = {f:.5f}"
              f"  (1 false alarm per {1.0/f:8.1f} quiet intervals)")
    print()
    print("  The rate of false alarms, not the sensitivity, is what a forecast")
    print("  needs, and it is the quantity that is hardest to measure, because")
    print("  it requires a long record of quiet intervals that were monitored")
    print("  as carefully as the restless ones.")


def main():
    print("Volcanic hazards and monitoring -- computed quantities")
    print(f"numpy {np.__version__}")
    part1()
    part2()
    part3()
    part4()
    print()
    print("=" * 72)
    print("No volcanic eruption, date, volume or monitoring record is quoted")
    print("anywhere in this script.  All scenarios are synthetic.")
    print("=" * 72)


if __name__ == "__main__":
    main()
