#!/usr/bin/env python3
"""The geocentric dipole, and what a spherical-harmonic field model is.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python dipole_and_igrf_demo.py

Everything here is SYNTHETIC.  The Gauss coefficients below are invented
teaching values; they are NOT the IGRF or WMM coefficients and no published
field model is reproduced.  Only mu0, the Earth radius 6371 km and the 11.5 deg
dipole tilt are standard values.

Contents
--------
1. Axial dipole: field components and the tan(I) = 2 tan(lat) relation.
2. Radial attenuation (a/r)^3 and the potential-field decay.
3. Tilted dipole: geomagnetic latitude under an 11.5 deg tilt.
4. Recovering Gauss coefficients by least squares on a synthetic field.
5. What a degree-1 truncation of a degree-2 field leaves behind.
6. Coefficient count, and the temporal validity window of a model.
"""

import numpy as np
from scipy.special import lpmv

RNG = np.random.default_rng(20261014)

A_EARTH_KM = 6371.0        # standard mean Earth radius, km
DIPOLE_TILT_DEG = 11.5     # standard value of the Earth's dipole tilt

# --- SYNTHETIC teaching coefficients (nT), invented, NOT IGRF ---------------
COEF = {
    (1, 0, "g"): -30000.0,
    (1, 1, "g"): -1800.0,
    (1, 1, "h"): 4800.0,
    (2, 0, "g"): 1200.0,
    (2, 1, "g"): -600.0,
    (2, 1, "h"): 900.0,
    (2, 2, "g"): 1500.0,
    (2, 2, "h"): -700.0,
}


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def legendre(n, m, theta):
    """Schmidt semi-normalised P_n^m(cos theta), Condon-Shortley phase removed.

    P_1^0 = cos(theta) and P_1^1 = sin(theta), the convention in which the
    degree-1 potential reads
    V = a (a/r)^2 [g10 cos t + (g11 cos p + h11 sin p) sin t]
    and the Gauss coefficients are directly comparable to the field in nT.
    """
    import math
    norm = math.sqrt((2.0 if m > 0 else 1.0) * math.factorial(n - m)
                     / math.factorial(n + m))
    return norm * (-1) ** m * lpmv(m, n, np.cos(theta))


def _S(coefs, n, theta, phi):
    """S_n(theta, phi) and its theta and phi derivatives for one degree."""
    S = dSdth = dSdph = 0.0
    h = 1.0e-6
    for (nn, m, kind) in coefs:
        if nn != n:
            continue
        g = coefs[(nn, m, kind)]
        if kind == "g":
            c, dcp = np.cos(m * phi), -m * np.sin(m * phi)
        else:
            c, dcp = np.sin(m * phi), m * np.cos(m * phi)
        P = legendre(n, m, theta)
        dP = (legendre(n, m, theta + h) - legendre(n, m, theta - h)) / (2.0 * h)
        S += g * c * P
        dSdth += g * c * dP
        dSdph += g * dcp * P
    return S, dSdth, dSdph


def field(coefs, theta, phi, r_km, max_degree=None):
    """Field (X north, Y east, Z down) in nT from Gauss coefficients.

    V = sum_n (a^{n+2} / r^{n+1}) S_n, so
    B_r = sum_n (n+1)(a/r)^{n+2} S_n,
    B_theta = -sum_n (a/r)^{n+2} dS_n/dtheta,
    B_phi = -(1/(r sin theta)) sum_n (a/r)^{n+2} dS_n/dphi.
    """
    Br = Bt = Bp = 0.0
    for n in sorted({k[0] for k in coefs}):
        if max_degree is not None and n > max_degree:
            continue
        S, dSdth, dSdph = _S(coefs, n, theta, phi)
        att = (A_EARTH_KM / r_km) ** (n + 2)
        Br += (n + 1) * att * S
        Bt += -att * dSdth
        Bp += -att * dSdph / np.sin(theta)
    return -Bt, Bp, -Br


def main():
    section("1. The axial dipole: tan(I) = 2 tan(latitude)")
    g10 = COEF[(1, 0, "g")]
    axial = {(1, 0, "g"): g10}
    print(f"teaching coefficient g10 = {g10:.1f} nT (SYNTHETIC, not IGRF)")
    print("  latitude (deg)     X (nT)      Z (nT)    I (deg)  tan I/(2 tan lat)")
    for lat in (0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 85.0):
        th = np.radians(90.0 - lat)
        X, Y, Z = field(axial, th, 0.0, A_EARTH_KM)
        inc = np.degrees(np.arctan2(Z, X))
        tl = 2.0 * np.tan(np.radians(lat))
        chk = np.tan(np.radians(inc)) / tl if tl != 0.0 else float("nan")
        print(f"  {lat:12.1f}  {X:10.1f}  {Z:10.1f}  {inc:9.4f}  {chk:16.6f}")
    Xeq = field(axial, np.pi / 2, 0.0, A_EARTH_KM)[0]
    Xpo = field(axial, 1.0e-9, 0.0, A_EARTH_KM)[0]
    print(f"  H at the dipole equator = {Xeq:.1f} nT")
    print(f"  H approaching the dipole pole = {Xpo:.3e} nT")

    section("2. Radial attenuation and the potential-field decay")
    print("  r (km)  altitude (km)   (a/r)^3    F (nT) at the dipole equator")
    for r in (A_EARTH_KM, A_EARTH_KM + 100.0, A_EARTH_KM + 400.0,
              A_EARTH_KM + 1000.0):
        X, Y, Z = field(axial, np.pi / 2, 0.0, r)
        print(f"  {r:8.1f}  {r - A_EARTH_KM:12.1f}  {(A_EARTH_KM/r)**3:8.5f}  "
              f"{np.hypot(X, Z):10.2f}")
    fac = (A_EARTH_KM / (A_EARTH_KM + 400.0)) ** 3
    print(f"  400 km of altitude multiplies the dipole field by (a/r)^3 = "
          f"{fac:.5f}, removing {100*(1-fac):.2f}% of the amplitude")

    section("3. Tilted dipole: geomagnetic latitude and dipole tilt")
    print(f"dipole tilt = {DIPOLE_TILT_DEG:.1f} deg (standard value)")
    print("  site lat (deg)  site lon (deg)  geomagnetic lat (deg)   difference")
    tilt = np.radians(DIPOLE_TILT_DEG)
    for lat, lon in ((45.0, 0.0), (45.0, 90.0), (45.0, 180.0), (60.0, 90.0),
                     (0.0, 0.0), (-30.0, 90.0)):
        th, ph = np.radians(90.0 - lat), np.radians(lon)
        cos_gm = np.cos(th) * np.cos(tilt) + np.sin(th) * np.sin(tilt) * np.cos(ph)
        gm_lat = 90.0 - np.degrees(np.arccos(np.clip(cos_gm, -1.0, 1.0)))
        print(f"  {lat:14.1f}  {lon:14.1f}  {gm_lat:21.4f}  {gm_lat - lat:+9.4f}")
    print("  the difference never exceeds the tilt itself, and is zero only on")
    print("  the great circle containing both axes.")

    section("4. Recovering Gauss coefficients from a synthetic field")
    # Gauss-Legendre nodes in colatitude and a uniform longitude grid make the
    # spherical harmonics orthogonal, so least squares recovers coefficients.
    x, _ = np.polynomial.legendre.leggauss(8)
    ths = np.arccos(x)
    phs = np.linspace(0.0, 2.0 * np.pi, 16, endpoint=False)
    keys1 = [(1, 0, "g"), (1, 1, "g"), (1, 1, "h")]
    keys2 = keys1 + [(2, 0, "g"), (2, 1, "g"), (2, 1, "h"), (2, 2, "g"), (2, 2, "h")]

    def solve(keys):
        A, b = [], []
        for th in ths:
            for ph in phs:
                A.append(design_row(th, ph, keys))
                b.append(np.array(field(COEF, th, ph, A_EARTH_KM)))
        A = np.vstack(A)
        b = np.concatenate(b)
        s, *_ = np.linalg.lstsq(A, b, rcond=None)
        rms = float(np.sqrt(np.mean((b - A @ s) ** 2)))
        return s, rms

    s1, rms1 = solve(keys1)
    print("fit of a DEGREE-1 model to a field that also contains degree 2:")
    for k, key in enumerate(keys1):
        print(f"  {key[2]}{key[0]}{key[1]}: true {COEF[key]:9.2f}  "
              f"fitted {s1[k]:9.2f}  error {s1[k]-COEF[key]:+9.2f} nT")
    print(f"  a residual of {100*rms1/np.sqrt(np.mean([np.sum(np.array(field(COEF,th,ph,A_EARTH_KM))**2) for th in ths for ph in phs])):.2f}% of the rms field is what a degree-1 model cannot describe")
    s2, rms2 = solve(keys2)
    print("fit of a DEGREE-1+2 model to the same field:")
    for k, key in enumerate(keys2):
        print(f"  {key[2]}{key[0]}{key[1]}: true {COEF[key]:9.2f}  "
              f"fitted {s2[k]:9.2f}  error {s2[k]-COEF[key]:+9.1e} nT")
    print(f"  rms residual of the degree-2 fit = {rms2:.3e} nT (machine precision)")
    print("  lesson: over a complete sphere the basis is orthogonal, so truncation")
    print("  does NOT bias the coefficients you keep - it appears entirely as a")
    print("  residual field.  Bias appears only when a truncated model is fitted")
    print("  to a limited, non-global set of points.")

    section("5. What a degree-1 truncation leaves behind, in field space")
    print("  site lat  site lon   degree-1 F (nT)  full F (nT)  |resid| (nT)  % of F")
    for lat, lon in ((20.0, 30.0), (45.0, 120.0), (-60.0, 250.0), (10.0, 300.0)):
        th, ph = np.radians(90.0 - lat), np.radians(lon)
        Xf, Yf, Zf = field(COEF, th, ph, A_EARTH_KM)
        X1, Y1, Z1 = field(COEF, th, ph, A_EARTH_KM, max_degree=1)
        F = np.sqrt(Xf**2 + Yf**2 + Zf**2)
        r = np.sqrt((Xf - X1) ** 2 + (Yf - Y1) ** 2 + (Zf - Z1) ** 2)
        print(f"  {lat:8.0f} {lon:9.0f}  {np.sqrt(X1**2+Y1**2+Z1**2):15.2f}  "
              f"{F:11.2f}  {r:12.2f}  {100*r/F:7.2f}")

    section("6. Coefficient count and the validity window")
    for N in (1, 2, 3, 10, 13):
        count = int(sum(2 * n + 1 for n in range(1, N + 1)))
        print(f"  maximum degree N = {N:2d} -> {count:3d} Gauss coefficients "
              "(g and h together)")
    sv = -40.0     # nT/yr, SYNTHETIC secular variation of g10
    print(f"SYNTHETIC secular variation of g10 = {sv:+.1f} nT/yr")
    for years in (0.0, 2.0, 5.0, 10.0):
        print(f"  after {years:4.1f} yr: g10 = {g10 + sv*years:10.2f} nT "
              f"(change {sv*years:+7.1f} nT = {100*sv*years/g10:+.2f}%)")


def design_row(theta, phi, keys):
    """Design row: the (X, Y, Z) response to unit coefficients in ``keys``."""
    out = []
    for key in keys:
        unit = {k: 0.0 for k in keys}
        unit[key] = 1.0
        out.append(np.array(field(unit, theta, phi, A_EARTH_KM)))
    return np.array(out).T          # 3 x len(keys)


if __name__ == "__main__":
    main()
