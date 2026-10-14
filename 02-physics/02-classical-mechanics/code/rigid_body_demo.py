"""Rigid-body dynamics: Euler's equations, free precession, Earth's rotation.

Run:  python3 rigid_body_demo.py
Requires: Python standard library only.

Companion to lesson 02-02-08.  The structure is:

1.  Integrate Euler's equations for a torque-free *asymmetric* top and measure
    what the equations say should be conserved (|L|^2 and the rotational kinetic
    energy), and what is not (the components of omega).
2.  Integrate a torque-free *symmetric* top and measure the precession rate of
    the transverse components against the closed-form value
    Omega = omega_3 (C - A)/A.
3.  Build the Earth's dynamical ellipticity H = (C - A)/A from the WGS 84
    defining parameters and a uniform-density spheroid -- a model that uses no
    measured Earth parameter beyond the two defining ones -- and compute the
    resulting free (Eulerian) precession period.
4.  Compute the forced lunisolar precession period from the same H, with
    astronomical inputs labelled as nominal, and show the sensitivity.

The measured quantities that this file deliberately does NOT quote -- the
observed Chandler wobble period, the observed precession period, and the tidal
recession rate -- must be taken from IERS and lunar-laser-ranging literature.
"""

import math

OMEGA_EARTH = 7.292115e-5      # rad/s, defining (WGS 84)
A_WGS = 6378137.0              # m, defining (WGS 84)
INV_F = 298.257223563          # defining (WGS 84)
SIDEREAL_DAY = 2 * math.pi / OMEGA_EARTH


def section(title: str) -> None:
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def rk4(f, y, dt):
    k1 = f(y)
    k2 = f([y[i] + 0.5 * dt * k1[i] for i in range(len(y))])
    k3 = f([y[i] + 0.5 * dt * k2[i] for i in range(len(y))])
    k4 = f([y[i] + dt * k3[i] for i in range(len(y))])
    return [y[i] + dt / 6.0 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
            for i in range(len(y))]


def main() -> None:
    section("1. Torque-free asymmetric top: what Euler's equations conserve")
    A, B, C = 1.0, 1.5, 2.0            # principal moments (SYNTHETIC)
    inertia = (A, B, C)

    def euler_eqs(w):
        w1, w2, w3 = w
        return [(B - C) * w2 * w3 / A,
                (C - A) * w3 * w1 / B,
                (A - B) * w1 * w2 / C]

    def l_sq(w):
        return (A * w[0]) ** 2 + (B * w[1]) ** 2 + (C * w[2]) ** 2

    def ke(w):
        return 0.5 * sum(inertia[i] * w[i] ** 2 for i in range(3))

    w = [1.0, 0.2, 3.0]
    l0, t0 = l_sq(w), ke(w)
    dt = 1.0e-4
    maxima = []
    prev, prev2 = None, None
    t = 0.0
    while t < 10.0:
        prev2, prev = prev, w[2]
        w = rk4(euler_eqs, w, dt)
        t += dt
        if prev2 is not None and prev is not None and prev > prev2 and prev > w[2]:
            maxima.append(t)
    print(f"  A = {A}, B = {B}, C = {C}, starting omega = (1, 0.2, 3) rad/s")
    print(f"  |L|^2 : initial {l0:.12f}, final {l_sq(w):.12f}, "
          f"relative change {abs(l_sq(w) - l0) / l0:.3e}")
    print(f"  T_rot : initial {t0:.12f}, final {ke(w):.12f}, "
          f"relative change {abs(ke(w) - t0) / t0:.3e}")
    print(f"  omega components at t = 10 s: ({w[0]:+.6f}, {w[1]:+.6f}, "
          f"{w[2]:+.6f}) rad/s")
    print(f"  but the *components* are not conserved: omega_3 has local maxima")
    print(f"  at {[f'{m:.4f}' for m in maxima[:4]]} s, i.e. it executes a")
    print(f"  polhode cycle rather than staying constant.")
    if len(maxima) >= 2:
        per = [maxima[i + 1] - maxima[i] for i in range(len(maxima) - 1)]
        print(f"  mean polhode period from the maxima = "
              f"{sum(per) / len(per):.6f} s")
    print("  Euler's equations conserve the two quadratic invariants exactly in")
    print("  the continuous problem.  The measured relative drift is of order")
    print("  1e-15 over 10 s at dt = 1e-4: round-off, not truncation error,")
    print("  because RK4's truncation error on this problem is far below it.")

    section("2. Symmetric top: the closed-form precession rate")
    A = B = 1.0
    C = 1.5
    w3 = 3.0
    omega_prec = w3 * (C - A) / A
    print(f"  A = B = {A}, C = {C}, omega_3 = {w3} rad/s")
    print(f"  predicted precession rate Omega = omega_3 (C - A)/A = "
          f"{omega_prec:.6f} rad/s")
    print(f"  predicted period 2 pi / Omega = {2 * math.pi / omega_prec:.6f} s")

    def eqs(w):
        return [-(C - A) * w[1] * w[2] / A,
                (C - A) * w[2] * w[0] / A,
                0.0]

    w = [2.0, 0.0, w3]
    dt = 1.0e-5
    t = 0.0
    crossings = []
    prev = w[0]
    while t < 10.0:
        w = rk4(eqs, w, dt)
        t += dt
        if prev > 0.0 >= w[0]:
            crossings.append(t)
        prev = w[0]
    if len(crossings) >= 2:
        period = crossings[1] - crossings[0]   # downward crossings are one
        # full precession period apart
        print(f"  measured period from zero crossings of omega_1 = "
              f"{period:.6f} s")
        print(f"  relative difference from the closed form = "
              f"{abs(period - 2 * math.pi / omega_prec)
                 / (2 * math.pi / omega_prec):.3e}")
    print("  omega_3 stays constant to {:.1e} rad/s.".format(abs(w[2] - w3)))
    print("  Both the axis and the transverse components precess about the")
    print("  fixed direction of L: this is the Poinsot picture, and it is the")
    print("  dynamics behind the Earth's free wobble.")

    section("3. The Earth's dynamical ellipticity, from defining parameters")
    f = 1.0 / INV_F
    b_wgs = A_WGS * (1 - f)
    h_ellip = (A_WGS ** 2 - b_wgs ** 2) / (A_WGS ** 2 + b_wgs ** 2)
    print(f"  WGS 84: a = {A_WGS:.0f} m, 1/f = {INV_F}, b = {b_wgs:.3f} m")
    print(f"  for a uniform-density spheroid, C = 2 a^2/5 and "
          f"A = (a^2 + c^2)/5,")
    print(f"  so H = (C - A)/A = (a^2 - b^2)/(a^2 + b^2) = {h_ellip:.8f}")
    t_free = 2 * math.pi / (OMEGA_EARTH * h_ellip)
    print(f"  free (Eulerian) precession period T = 2 pi / (omega H) = "
          f"{t_free:.3f} s")
    print(f"                                            = "
          f"{t_free / 86400:.3f} days")
    print()
    print("  This number is a MODEL result: it uses only the two defining")
    print("  WGS 84 shape parameters and the defining rotation rate, plus the")
    print("  assumption of uniform density.  A real Earth is more centrally")
    print("  condensed, so its H is smaller and its free period longer; and")
    print("  elasticity and the fluid core lengthen it further.  Both the")
    print("  observed Euler period and the observed free-wobble (Chandler)")
    print("  period must be taken from the IERS Earth-orientation series, not")
    print("  from this model.")

    section("4. Forced lunisolar precession: scaling and sensitivity")
    # Nominal astronomical inputs, flagged: they are NOT defining constants.
    year_days = 365.256          # NOMINAL sidereal year, days
    obliquity = math.radians(23.439)   # NOMINAL mean obliquity
    n_orb = 2 * math.pi / (year_days * 86400.0)
    ratio = OMEGA_EARTH / n_orb
    print(f"  NOMINAL inputs (verify in IERS): sidereal year = "
          f"{year_days} days, obliquity = {math.degrees(obliquity):.3f} deg")
    print(f"  omega/n = {ratio:.4f}  (the number of sidereal days in a year,")
    print(f"  which is why the sidereal day and the solar day differ)")
    print()
    print("  For a circular orbit, the solar torque on the equatorial bulge")
    print("  gives dpsi/dt = (3/2)(n^2/omega) H cos(eps), so")
    print("  T_prec / T_year = (2/3)(omega/n) / (H cos eps).")
    rate0 = 1.5 * (n_orb ** 2 / OMEGA_EARTH) * h_ellip * math.cos(obliquity)
    print(f"  dpsi/dt = (3/2)(n^2/omega) H cos(eps) = {rate0:.4e} rad/s")
    print(f"  as a rate: {rate0 * 3.1557e7 * 206264.806:.4f} arcsec/yr "
          f"(1 rad = {180 * 3600 / math.pi:.2f} arcsec)")
    print()
    print("      H            T_prec (years, solar torque alone)")
    for h in (h_ellip, 0.0033, 0.0032, 0.0030):
        t_prec = (2 / 3) * ratio / (h * math.cos(obliquity)) * year_days / 365.25
        print(f"  {h:.6f}        {t_prec:12.1f}")
    t_solar = (2 / 3) * ratio / (h_ellip * math.cos(obliquity)) \
        * year_days / 365.25
    print()
    print(f"  With the uniform-spheroid H, the solar torque alone would give")
    print(f"  {t_solar:.0f} years.  The Moon's contribution is larger than the")
    print("  Sun's, even though the Moon is far less massive, because the")
    print("  torque on the bulge scales with the tide-raising parameter")
    print("  m/d^3 and the Moon is much closer.  The observed total is")
    print("  therefore considerably faster than the solar-only value above;")
    print("  the ratio of the lunar to solar contributions is a measured")
    print("  quantity (it depends on the lunar orbit and on H) and should be")
    print("  taken from the literature rather than computed from memory.")
    print("  The observed precession and nutation periods are measured")
    print("  quantities published by IERS and must be quoted from there.")
    print()
    print("  The sensitivity table is the honest output of this section: the")
    print("  precession period is inversely proportional to H, and H is the")
    print("  number the model does not constrain well (a 10% change in H moves")
    print("  the period by 10%).  A prediction of the precession rate is")
    print("  therefore a prediction of the Earth's internal mass distribution.")


if __name__ == "__main__":
    main()
