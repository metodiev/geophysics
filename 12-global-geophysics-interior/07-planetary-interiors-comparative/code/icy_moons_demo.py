#!/usr/bin/env python3
"""Induction in a conducting shell, and what a magnetic measurement can say about
a subsurface ocean.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python icy_moons_demo.py

Everything is SYNTHETIC.  The body, its shell thickness, its conductivity and the
"measured" responses are teaching values chosen for this lesson; the body is not
any real moon and no number below is a measurement.  The externally quoted
constants are mu0 and the definition of the skin depth.

Physics: a time-varying external field of degree n induces currents in a
spherical conducting shell.  Writing the poloidal field through a radial
function h(r) with  B_r = n(n+1) h P_n / r^2  and  B_theta = (h'/r) dP_n/dtheta,
the field obeys  h'' - n(n+1)h/r^2 = i omega mu0 sigma h  inside the conductor and
h'' - n(n+1)h/r^2 = 0 outside it.  We solve that boundary-value problem and check
it against the analytic spherical-Bessel solution, against the insulating limit
and against the perfect-conductor limit.

Sections
--------
1  skin depth and the induction parameter
2  the shell response, verified three ways
3  the observable, and the conductance collapse: sigma and d are not separately
   measurable
4  sensitivity and inversion of a synthetic single-frequency measurement
5  saturation: when a bigger signal carries no more information
"""

import numpy as np
from scipy.special import spherical_in, spherical_kn

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi   # exact SI constant, H/m


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def skin_depth(omega, sigma):
    """delta = sqrt(2/(omega mu0 sigma)), in metres."""
    return np.sqrt(2.0 / (omega * MU0 * sigma))


def shell_response(n, sigma, r1, r2, omega, n_steps=2000):
    """Complex response Q of a conducting shell to a degree-n external field.

    The external field is V_ext = E r^n + Q a^{2n+1} r^-(n+1) with a = r2 and
    E = 1, so |Q| is the ratio of the induced to the primary potential
    coefficient.  Inside (r < r1) the field is regular: V_in = I r^n.
    Returns (I, Q).
    """
    a = r2
    k2 = 1j * omega * MU0 * sigma

    def rhs(r, y):
        S, Sp = y
        return np.array([Sp, n * (n + 1) * S / r ** 2 + k2 * S])

    # start at r1 with the regular interior branch, amplitude 1
    y = np.array([-1.0 * r1 ** (n + 1) / (n + 1), -1.0 * r1 ** n], dtype=complex)
    h = (r2 - r1) / n_steps
    r = r1
    for _ in range(n_steps):
        k1 = rhs(r, y)
        k2a = rhs(r + h / 2, y + h / 2 * k1)
        k3 = rhs(r + h / 2, y + h / 2 * k2a)
        k4 = rhs(r + h, y + h * k3)
        y = y + h / 6.0 * (k1 + 2 * k2a + 2 * k3 + k4)
        r += h
    S1, Sp1 = y
    # continuity of S and S' at r2 with the exterior expansion
    A = np.array([[S1, -a ** (2 * n + 1) * r2 ** (-n) / n],
                  [Sp1, a ** (2 * n + 1) * r2 ** (-n - 1)]], dtype=complex)
    b = np.array([-r2 ** (n + 1) / (n + 1), -r2 ** n], dtype=complex)
    I, Q = np.linalg.solve(A, b)
    return I, Q


def shell_response_analytic(n, sigma, r1, r2, omega):
    """The same response using the exact spherical-Bessel solutions."""
    a = r2
    k = np.sqrt(1j * omega * MU0 * sigma)

    def basis(r):
        return np.array([spherical_in(n, k * r) * r, spherical_kn(n, k * r) * r])

    def S(r, c):
        b = basis(r)
        return c[0] * b[0] + c[1] * b[1]

    def Sp(r, c):
        hh = 1e-4
        return (S(r + hh, c) - S(r - hh, c)) / (2 * hh)

    M = np.array([[S(r1, [1, 0]), S(r1, [0, 1])],
                  [Sp(r1, [1, 0]), Sp(r1, [0, 1])]], dtype=complex)
    c = np.linalg.solve(M, np.array([-1.0 * r1 ** (n + 1) / (n + 1), -1.0 * r1 ** n]))
    S1, Sp1 = S(r2, c), Sp(r2, c)
    A = np.array([[S1, -a ** (2 * n + 1) * r2 ** (-n) / n],
                  [Sp1, a ** (2 * n + 1) * r2 ** (-n - 1)]], dtype=complex)
    b = np.array([-r2 ** (n + 1) / (n + 1), -r2 ** n], dtype=complex)
    return np.linalg.solve(A, b)


def main():
    section("1. Skin depth and the induction parameter")
    print("  delta = sqrt(2/(omega mu0 sigma));  the layer responds to a field whose")
    print("  period is comparable to the diffusion time across it.")
    print("   period        sigma (S/m)   delta (km)   delta/shell for d = 5 km")
    for period in (1.0e4, 1.0e5, 1.0e6):
        omega = 2.0 * np.pi / period
        for sigma in (0.01, 0.1, 1.0):
            d_km = skin_depth(omega, sigma) / 1e3
            print(f"   {period:8.1e} s   {sigma:9.2f}   {d_km:10.1f}   {d_km / 5.0:12.3f}")
    print("  At these periods a 1 S/m layer has a skin depth of 50-500 km, far larger")
    print("  than any plausible ocean: the layer is electromagnetically THIN, and what")
    print("  the field sees is the conductance sigma*d, not the conductivity.  For")
    print("  sigma*d below about 1e-4 S, the layer is transparent and no ocean can be")
    print("  detected at these periods regardless of how thick it is.")

    section("2. The shell response, verified three ways")
    n = 1
    r2 = 1.0e6
    r1 = 0.995e6
    omega = 2.0 * np.pi / 1.0e5
    print(f"  degree n = {n}, shell from r = {r1:.4e} m to {r2:.4e} m,"
          f" period {2 * np.pi / omega:.1e} s")
    print("   sigma (S/m)    delta (km)   |Q|      arg Q (deg)   |1+Q| interior")
    for sigma in (0.0, 1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0, 1e4):
        I, Q = shell_response(n, sigma, r1, r2, omega)
        d_km = skin_depth(omega, sigma) / 1e3 if sigma > 0 else np.inf
        print(f"   {sigma:10.3g}   {d_km:10.2f}   {abs(Q):7.4f}   "
              f"{np.degrees(np.angle(Q)):11.2f}   {abs(I):14.4f}")
    print("  Check 1 (insulating limit): sigma = 0 gives |Q| = 0 and |I| = 1 exactly:")
    I0, Q0 = shell_response(n, 0.0, r1, r2, omega)
    print(f"     |I| = {abs(I0):.10f}, |Q| = {abs(Q0):.2e}")
    print("  Check 2 (perfect conductor): a perfectly conducting shell expels the")
    print("  field from its interior, which requires |Q| -> n/(n+1) = "
          f"{n / (n + 1):.4f} with I -> 0:")
    I_hi, Q_hi = shell_response(n, 1e6, r1, r2, omega)
    print(f"     at sigma = 1e6 S/m: |Q| = {abs(Q_hi):.6f}, |I| = {abs(I_hi):.2e}")
    print("  Check 3 (independent route): the analytic spherical-Bessel solution")
    print("   sigma (S/m)   |Q| RK4      |Q| Bessel     |I| RK4      |I| Bessel")
    for sigma in (0.1, 1.0, 10.0):
        I1, Q1 = shell_response(n, sigma, r1, r2, omega)
        I2, Q2 = shell_response_analytic(n, sigma, r1, r2, omega)
        print(f"   {sigma:10.3g}   {abs(Q1):10.6f}   {abs(Q2):10.6f}   "
              f"{abs(I1):10.6f}   {abs(I2):10.6f}")

    section("3. The observable, and the collapse of sigma times thickness")
    print("  A real measurement returns the induced field: its amplitude |Q| and its")
    print("  phase lag.  Two shells with the same conductance C = sigma*d:")
    print("   sigma (S/m)   d (km)   C (S)     |Q|      arg Q (deg)")
    rows = []
    for sigma, d_km in ((1.0, 5.0), (0.5, 10.0), (0.2, 25.0), (0.1, 50.0)):
        r1_t = r2 - d_km * 1e3
        I, Q = shell_response(n, sigma, r1_t, r2, omega)
        rows.append((sigma, d_km, sigma * d_km * 1e3, abs(Q), np.degrees(np.angle(Q))))
        print(f"   {sigma:10.3g}   {d_km:7.1f}   {sigma * d_km * 1e3:8.1f}   "
              f"{abs(Q):7.4f}   {np.degrees(np.angle(Q)):11.2f}")
    print("  The four rows have the same conductance but different conductivity and")
    print("  thickness.  |Q| and the phase agree to about ten percent: the measurement")
    print("  constrains the CONDUCTANCE, not the conductivity and thickness separately.")
    print("  That is the central non-uniqueness of induction sounding; separating them")
    print("  requires an independent measurement of the layer's conductivity.")

    section("4. Sensitivity and a synthetic inversion")
    print("  Sensitivity of the response to the conductance, per frequency:")
    print("   period (s)   C (S)     |Q|      dln|Q|/dlnC")
    d_km, sigma0 = 5.0, 0.5
    for period in (1e3, 1e4, 1e5, 1e6, 1e7):
        omega_t = 2.0 * np.pi / period
        C0 = sigma0 * d_km * 1e3
        eps = 1e-3
        _, Q_a = shell_response(n, sigma0 * (1 - eps / 2), r2 - d_km * 1e3, r2, omega_t)
        _, Q_b = shell_response(n, sigma0 * (1 + eps / 2), r2 - d_km * 1e3, r2, omega_t)
        dlnQ = (np.log(abs(Q_b)) - np.log(abs(Q_a))) / eps
        print(f"   {period:8.1e}   {C0:7.1f}   {abs(Q_a):7.4f}   {dlnQ:14.4f}")
    print("  Read the ends of that table carefully.  Long periods give dln|Q|/dlnC =")
    print("  1.00, the best relative sensitivity, but the response itself is 0.03 or")
    print("  smaller.  Short periods give a large response that is already saturated")
    print("  and almost blind to C (0.02).  Neither end is useful by itself.")
    print("  Synthetic inversion of sigma for a 5.0 km layer, sigma = 0.5 S/m:")
    sigma_true = 0.5
    for period, tag in ((1e5, "sensitive band"), (1e3, "saturated")):
        omega_t = 2.0 * np.pi / period
        _, Q_true = shell_response(n, sigma_true, r2 - 5e3, r2, omega_t)
        measured = abs(Q_true)
        res = []
        for noise in (0.01, 0.05):
            bounds = []
            for sign in (+1, -1):
                lo, hi = 1e-3, 1e5
                for _ in range(60):
                    mid = np.sqrt(lo * hi)
                    _, Qm = shell_response(n, mid, r2 - 5e3, r2, omega_t)
                    if abs(Qm) < measured * (1 + sign * noise):
                        lo = mid
                    else:
                        hi = mid
                bounds.append(np.sqrt(lo * hi))
            res.append((noise, min(bounds), max(bounds)))
        print(f"     period {period:.0e} s ({tag}): |Q| = {measured:.4f}")
        for noise, lo_s, hi_s in res:
            print(f"        a {100 * noise:.0f}% error in |Q| admits sigma from"
                  f" {lo_s:.4f} to {hi_s:.4f} S/m")
    print("  In the sensitive band the admitted range is symmetric about the truth;")
    print("  in the saturated band it is open-ended upwards, so a layer orders of")
    print("  magnitude more conductive than assumed is consistent with the same signal.")

    section("5. Saturation: when a bigger signal carries no more information")
    omega_best = 2.0 * np.pi / 1e5
    print("  A thicker or more conductive layer does not keep increasing the signal.")
    print("   conductance C (S)    |Q|        information about C")
    for C in (1e2, 1e3, 1e4, 1e5, 1e6, 1e7):
        # hold d fixed at 10 km and vary sigma to change C
        d_t = 10e3
        sigma_t = C / d_t
        _, Q = shell_response(n, sigma_t, r2 - d_t, r2, omega_best)
        if abs(Q) < 0.05:
            info = "response too small to measure"
        elif abs(Q) > 0.45:
            info = "saturated against the 0.5 ceiling"
        else:
            info = "usable"
        print(f"   {C:16.0f}   {abs(Q):7.4f}   {info}")
    print("  The ceiling 0.5 is not a property of the body: it is the geometry of")
    print("  perfect screening.  Once a candidate ocean is thick and salty enough to")
    print("  reach it, its thickness is no longer recoverable from this measurement.")


if __name__ == "__main__":
    main()
