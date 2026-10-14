#!/usr/bin/env python3
"""Spherical-harmonic analysis of the magnetic field: orthogonality, the
Mauersberger-Lowes power spectrum, and the non-uniqueness that surface data
cannot remove.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spherical_harmonic_magnetic_demo.py

Everything here is SYNTHETIC: the Gauss coefficients are invented teaching
values, and no observed or published model is used.  Only mu0, the Earth radius
6371 km and the 11.5 deg dipole tilt are standard values.

Contents
--------
1. Associated Legendre functions P_n^m and orthogonality of the harmonics.
2. Forward field from SYNTHETIC Gauss coefficients, degrees 1 to 4.
3. Degree power and the Mauersberger-Lowes spectrum R_n.
   A 2b section checks the degree-1 and degree-2 expressions by hand.
4. Truncation error versus maximum degree, measured.
5. Upward/downward continuation: the (a/r)^{n+2} amplification by degree.
6. Non-uniqueness: internal and external sources give the same surface field.
"""

import math

import numpy as np
from scipy.special import lpmv

RNG = np.random.default_rng(20261014)

A_EARTH_KM = 6371.0

# --- SYNTHETIC Gauss coefficients (nT).  Invented, NOT IGRF or WMM ----------
COEF = {}
for (n, m, val) in [
    (1, 0, -30000.0), (1, 1, -1800.0),
    (2, 0, 1200.0), (2, 1, -600.0), (2, 2, 1500.0),
    (3, 0, 900.0), (3, 1, -450.0), (3, 2, 700.0), (3, 3, -300.0),
    (4, 0, -400.0), (4, 1, 260.0), (4, 2, -180.0), (4, 3, 120.0), (4, 4, -90.0),
]:
    COEF[(n, m, "g")] = val
for (n, m, val) in [
    (1, 1, 4800.0),
    (2, 1, 900.0), (2, 2, -700.0),
    (3, 1, 380.0), (3, 2, -250.0), (3, 3, 410.0),
    (4, 1, -150.0), (4, 2, 210.0), (4, 3, -110.0), (4, 4, 80.0),
]:
    COEF[(n, m, "h")] = val


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def legendre(n, m, theta):
    """Schmidt semi-normalised P_n^m(cos theta), Condon-Shortley phase removed.

    P_1^0 = cos(theta), P_1^1 = sin(theta): the convention in which
    V = a (a/r)^2 [g10 cos t + (g11 cos p + h11 sin p) sin t] and in which the
    Gauss coefficients are directly comparable to the field in nT.
    """
    norm = np.sqrt((2.0 if m > 0 else 1.0) * math.factorial(n - m)
                   / math.factorial(n + m))
    return norm * (-1) ** m * lpmv(m, n, np.cos(theta))


def sph_potential(coefs, theta, phi, max_degree=4):
    """Scalar potential series S(theta, phi) = sum_n sum_m [g cos mp + h sin mp] P."""
    S = 0.0
    for n in range(1, max_degree + 1):
        for m in range(0, n + 1):
            P = legendre(n, m, theta)
            g = coefs.get((n, m, "g"), 0.0)
            h = coefs.get((n, m, "h"), 0.0)
            S += (g * np.cos(m * phi) + h * np.sin(m * phi)) * P
    return S


def field(coefs, theta, phi, r_km, max_degree=4):
    """X north, Y east, Z down in nT, from the potential V = sum (a^{n+2}/r^{n+1}) S_n."""
    h = 1.0e-6
    X = Y = Z = 0.0
    Br = Bt = Bp = 0.0
    for n in range(1, max_degree + 1):
        att = (A_EARTH_KM / r_km) ** (n + 2)
        Sn = 0.0
        dSdt = 0.0
        dSdp = 0.0
        for m in range(0, n + 1):
            g = coefs.get((n, m, "g"), 0.0)
            hh = coefs.get((n, m, "h"), 0.0)
            P = legendre(n, m, theta)
            dP = (legendre(n, m, theta + h) - legendre(n, m, theta - h)) / (2.0 * h)
            c = np.cos(m * phi)
            s = np.sin(m * phi)
            Sn += (g * c + hh * s) * P
            dSdt += (g * c + hh * s) * dP
            dSdp += (-g * m * s + hh * m * c) * P
        Br += (n + 1) * att * Sn
        Bt += -att * dSdt
        Bp += -att * dSdp / np.sin(theta)
    return -Bt, Bp, -Br


def mauersberger_lowes(coefs, max_degree=4):
    """R_n = (n+1) sum_m (g^2 + h^2), in nT^2."""
    out = {}
    for n in range(1, max_degree + 1):
        s = 0.0
        for m in range(0, n + 1):
            g = coefs.get((n, m, "g"), 0.0)
            h = coefs.get((n, m, "h"), 0.0)
            s += g * g + h * h
        out[n] = (n + 1) * s
    return out


def main():
    section("1. Associated Legendre functions and orthogonality")
    print("  P_n^m(cos theta) at theta = 60 deg (Condon-Shortley phase removed)")
    for n in range(1, 4):
        row = "   ".join(f"P_{n}^{m} = {legendre(n, m, np.radians(60.0)):+.6f}"
                         for m in range(0, n + 1))
        print("  " + row)
    # Gauss-Legendre quadrature: sum over globe of P_n^m P_n'^m' vanishes unless
    # the indices match
    x, w = np.polynomial.legendre.leggauss(40)
    ths, wts = np.arccos(x), w
    norm = {}
    for n in range(1, 4):
        for m in range(0, n + 1):
            val = 0.0
            for th, wt in zip(ths, wts):
                val += legendre(n, m, th) ** 2 * wt
            norm[(n, m)] = val
    print("  quadrature integral of the Schmidt P_n^m squared, "
          "sin(theta) d(theta) d(phi) excluded:")
    for key in norm:
        expect = (4.0 if key[1] > 0 else 2.0) / (2 * key[0] + 1.0)
        print(f"    n = {key[0]}, m = {key[1]}: computed {norm[key]:.6f}   "
              f"2(2-delta_m0)/(2n+1) = {expect:.6f}")
    section("2. Forward field from SYNTHETIC Gauss coefficients (degrees 1-4)")
    print("  coefficients used (nT):")
    for n in range(1, 5):
        parts = []
        for m in range(0, n + 1):
            if (n, m, "g") in COEF:
                parts.append(f"g{n}{m}={COEF[(n,m,'g')]:+.0f}")
            if (n, m, "h") in COEF:
                parts.append(f"h{n}{m}={COEF[(n,m,'h')]:+.0f}")
        print(f"    degree {n}: " + ", ".join(parts))
    print("  site lat/lon       X (nT)      Y (nT)      Z (nT)     F (nT)   D (deg)  I (deg)")
    for lat, lon in ((60.0, 10.0), (30.0, 100.0), (0.0, 200.0), (-45.0, 300.0)):
        th, ph = np.radians(90.0 - lat), np.radians(lon)
        X, Y, Z = field(COEF, th, ph, A_EARTH_KM)
        print(f"  {lat:6.0f} {lon:5.0f}  {X:11.2f} {Y:11.2f} {Z:11.2f} "
              f"{np.hypot(np.hypot(X, Y), Z):9.2f} "
              f"{np.degrees(np.arctan2(Y, X)):8.3f} "
              f"{np.degrees(np.arctan2(Z, np.hypot(X, Y))):8.3f}")

    section("2b. Analytic checks of the degree-1 and degree-2 terms")
    print("  at (lat, lon) = (0, 0), i.e. colatitude 90 deg and zero longitude:")
    Xa, Ya, Za = field({(1, 0, "g"): -30000.0}, np.pi / 2, 0.0, A_EARTH_KM)
    print(f"    axial dipole only  : X = {Xa:9.4f} nT, Y = {Ya:.4f} nT, "
          f"Z = {Za:.4f} nT, I = {np.degrees(np.arctan2(Za, Xa)):.4f} deg")
    Xb, Yb, Zb = field({(1, 0, "g"): -30000.0, (2, 0, "g"): 1200.0},
                       np.pi / 2, 0.0, A_EARTH_KM)
    print(f"    + g20 = 1200 nT    : X = {Xb:9.4f} nT, Y = {Yb:.4f} nT, "
          f"Z = {Zb:.4f} nT, I = {np.degrees(np.arctan2(Zb, Xb)):.4f} deg")
    print("    hand check: Z = -(n+1) S_n with S_1 = g10 cos(90 deg) = 0 and")
    print(f"    S_2 = g20 P_2^0 = 1200 x (-0.5) = -600 nT, so Z = -3 x (-600) = "
          f"{3*600.0:.1f} nT")
    print(f"    and F = {np.hypot(Xb, Zb):.4f} nT")

    section("3. The Mauersberger-Lowes power spectrum R_n")
    R = mauersberger_lowes(COEF, 4)
    Rtot = sum(R.values())
    print("    n     R_n (nT^2)      share of total     R_n/R_1")
    for n in sorted(R):
        print(f"  {n:3d}  {R[n]:14.1f}  {100*R[n]/Rtot:14.3f}%  {R[n]/R[1]:14.2e}")
    print(f"  total power sum R_n = {Rtot:.1f} nT^2")
    print(f"  the dipole carries {100*R[1]/Rtot:.2f}% of the power in this SYNTHETIC")
    print("  spectrum; the non-dipole part is what the higher degrees describe.")

    section("4. Truncation error versus maximum degree (measured)")
    sites = [(60.0, 10.0), (30.0, 100.0), (0.0, 200.0), (-45.0, 300.0),
             (75.0, 45.0), (-20.0, 150.0)]
    full = [np.array(field(COEF, np.radians(90 - la), np.radians(lo), A_EARTH_KM))
            for la, lo in sites]
    print("  N     rms(X,Y,Z) residual (nT)   % of rms |F|")
    rmsF = np.sqrt(np.mean([np.sum(v ** 2) for v in full]))
    for N in (1, 2, 3, 4):
        res = [np.array(field(COEF, np.radians(90 - la), np.radians(lo),
                              A_EARTH_KM, max_degree=N)) for la, lo in sites]
        r = np.sqrt(np.mean([np.sum((a - b) ** 2) for a, b in zip(full, res)]))
        print(f"  {N}   {r:24.2f}   {100*r/rmsF:12.2f}%")

    section("5. Upward and downward continuation by degree")
    for alt in (100.0, 400.0):
        print(f"  altitude {alt:.0f} km: continuation factor (a/(a+alt))^(n+2)")
        for n in (1, 2, 4, 10, 13):
            fac = (A_EARTH_KM / (A_EARTH_KM + alt)) ** (n + 2)
            print(f"    n = {n:2d}: {fac:.6f}   (field at altitude is "
                  f"{100*(1-fac):.3f}% weaker than at the surface)")
    print("  downward continuation from 400 km to the surface multiplies degree")
    for n in (1, 13):
        fac = ((A_EARTH_KM + 400.0) / A_EARTH_KM) ** (n + 2)
        print(f"    n = {n:2d} by {fac:.4f}")
    print("  high-degree noise is amplified far more than the low-degree signal,")
    print("  which is why downward continuation must be truncated or damped.")

    section("6. Non-uniqueness: the same surface field from two models")
    # An internal source gives V ~ (a/r)^{n+1}; an external source gives (r/a)^n.
    # At r = a both reduce to the same S_n, so surface data cannot separate them.
    n = 2
    r_test = 0.95 * A_EARTH_KM
    fac_int = (A_EARTH_KM / r_test) ** (n + 2)
    fac_ext = (r_test / A_EARTH_KM) ** (n - 1)
    print(f"degree n = {n}; compare the field at r = {r_test:.0f} km "
          f"({100*r_test/A_EARTH_KM:.0f}% of a) for")
    print("two models that are IDENTICAL at the surface (r = a):")
    print(f"  internal-source model:  radial factor (a/r)^(n+2) = {fac_int:.5f}")
    print(f"  external-source model:  radial factor (r/a)^(n-1) = {fac_ext:.5f}")
    print(f"  ratio internal/external = {fac_int/fac_ext:.5f}: a "
          f"{100*abs(fac_int/fac_ext - 1):.2f}% difference,")
    print("  invisible in surface data and finite everywhere below it.")
    # and a genuinely null field: add a harmonic with the same value on r = a
    print("  the ambiguity is removed only by data at two radii (satellite plus")
    print("  surface, or a deep-penetrating measurement).")


def _fact(n):
    return float(math.factorial(n))


if __name__ == "__main__":
    main()
