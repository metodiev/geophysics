#!/usr/bin/env python3
"""Satellite gravimetry, part 3: spherical-harmonic solutions -- normalisation,
the geoid and gravity anomaly as coefficient sums, degree variance, and where
the signal runs into the noise.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python spherical_harmonic_solutions_demo.py

Everything here is SYNTHETIC: the coefficient set is drawn from a stated
synthetic spectrum with a fixed seed.  No measured gravity model is used, and
no published coefficient value is quoted.

Contents
--------
1. Normalisation of the associated Legendre functions, verified by quadrature.
2. A synthetic coefficient set from a stated degree-amplitude law.
3. Geoid undulation and gravity anomaly from the same coefficients: the (l-1)
   and 1/gamma factors, verified against finite differences of the potential.
4. Degree variance: measuring the exponent of the synthetic spectrum, with a
   white-noise control.
5. The information budget: (L+1)^2 coefficients, half-wavelength pi R / L.
6. Signal-to-noise crossover degree for a stated synthetic error spectrum.
"""

import numpy as np
from scipy.special import gammaln, lpmv, roots_legendre

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
GM_EARTH = 3.986004418e14   # m^3 s^-2
R_EARTH = 6371.0e3          # m, rounded mean Earth radius
GAMMA = 9.80665             # m s^-2, standard gravity (conventional value)

# --- SYNTHETIC model parameters ---------------------------------------------
L_MAX = 40                  # maximum degree of the synthetic model
AMP_LAW = 1.0e-5            # degree amplitude A at l = 2 in A * (2/l)^P
AMP_POW = 2.0               # exponent P of the synthetic degree-amplitude law
NOISE_LAW = 1.0e-9          # synthetic per-coefficient error = NOISE_LAW * l


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def pbar(l, m, x):
    """4pi-normalised associated Legendre function, Condon-Shortley phase removed.

    int_{-1}^{1} pbar^2 dx * (pi for m>0, 2pi for m=0) = 4 pi.
    """
    norm = np.sqrt((2.0 - (m == 0)) * (2 * l + 1)
                   * np.exp(gammaln(l - m + 1) - gammaln(l + m + 1)))
    return norm * (-1.0) ** m * lpmv(m, l, x)


def synth_T(r, th, ph, C, S, L):
    """Disturbing potential T = (GM/r) sum_l (R/r)^l sum_m [...] pbar, l >= 2.

    r, th, ph may be arrays of the same shape.  Returns an array.
    """
    ct = np.cos(th)
    out = np.zeros_like(np.asarray(ct, dtype=float))
    for l in range(2, L + 1):
        fl = np.zeros_like(out)
        for m in range(0, l + 1):
            fl = fl + (C[l, m] * np.cos(m * ph) + S[l, m] * np.sin(m * ph)) \
                * pbar(l, m, ct)
        out = out + (R_EARTH / r) ** l * fl
    return GM_EARTH / r * out


def main():
    section("1. Normalisation of the 4pi-normalised Legendre functions")
    print("  convention: int_{-1}^{1} [pbar_lm]^2 dx = 2(2-delta_m0), so that")
    print("  int_{sphere} [pbar_lm]^2 dOmega = 4 pi (with the phi integral).")
    x, w = roots_legendre(200)
    print("   l   m   quadrature int(pbar^2 dx)   2(2-delta_m0)   rel. error")
    for (l, m) in ((2, 0), (2, 1), (2, 2), (5, 3), (10, 0), (10, 7), (20, 5)):
        val = np.sum(w * pbar(l, m, x) ** 2)
        want = 2.0 * (2.0 - (m == 0))
        print(f"  {l:3d} {m:3d} {val:22.10f} {want:16.1f} {abs(val-want)/want:12.2e}")
    print("  Multiplying by (pi for m>0, 2 pi for m=0) makes every value 4 pi.")
    print("  A model is only interpretable if its normalisation convention is")
    print("  stated: the same numbers mean different fields under another one.")

    section("2. A synthetic coefficient set from a stated amplitude law")
    C = np.zeros((L_MAX + 1, L_MAX + 1))
    S = np.zeros((L_MAX + 1, L_MAX + 1))
    for l in range(2, L_MAX + 1):
        amp = AMP_LAW * (2.0 / l) ** AMP_POW
        for m in range(0, l + 1):
            C[l, m] = amp * RNG.standard_normal()
            S[l, m] = amp * RNG.standard_normal()
    n_coef = sum(2 * l + 1 for l in range(2, L_MAX + 1))
    print(f"  SYNTHETIC amplitude law: sigma_l = {AMP_LAW:.1e} * (2/l)^{AMP_POW:.1f}")
    print(f"  degrees l = 2..{L_MAX}, coefficients (l>=2): {n_coef}")
    print(f"  sigma_2 = {AMP_LAW:.2e}, sigma_10 = "
          f"{AMP_LAW*(2/10)**AMP_POW:.2e}, sigma_40 = "
          f"{AMP_LAW*(2/40)**AMP_POW:.2e}")
    print("  (each coefficient is a draw from N(0, sigma_l^2); the field is a")
    print("   random realisation, so the printed extremes are not universal)")

    section("3. Geoid and gravity anomaly from the same coefficients")
    print("  Bruns: N = T/gamma.  Fundamental equation of physical geodesy:")
    print("         dg = -dT/dr - 2T/r = (GM/r^2) sum_l (l-1)(R/r)^l sum_m [...]")
    lats = np.array([0.0, 30.0, 45.0, 60.0, 89.0])
    phs = np.array([0.0, 25.0, 70.0, 130.0, 200.0])
    print("  lat(deg)  lon(deg)      T (m^2/s^2)      N (m)     dg analytic   "
          "dg finite-diff   rel. diff")
    for la, ph in zip(lats, phs):
        th = np.deg2rad(90.0 - la)
        ph = np.deg2rad(ph)
        T0 = float(synth_T(R_EARTH, th, ph, C, S, L_MAX))
        N = T0 / GAMMA
        # analytic gravity anomaly
        ct = np.cos(th)
        ssum = 0.0
        for l in range(2, L_MAX + 1):
            fl = 0.0
            for m in range(0, l + 1):
                fl += (C[l, m] * np.cos(m * ph) + S[l, m] * np.sin(m * ph)) \
                    * float(pbar(l, m, ct))
            ssum += (l - 1) * fl
        dg = GM_EARTH / R_EARTH ** 2 * ssum * 1e5      # m/s^2 -> mGal
        # finite-difference route: -dT/dr - 2T/r at r = R
        h = 100.0
        dTdr = (float(synth_T(R_EARTH + h, th, ph, C, S, L_MAX))
                - float(synth_T(R_EARTH - h, th, ph, C, S, L_MAX))) / (2 * h)
        dg_fd = (-dTdr - 2.0 * T0 / R_EARTH) * 1e5
        print(f"  {la:8.1f} {np.rad2deg(ph):9.1f} {T0:16.4f} {N:9.3f} "
              f"{dg:14.4f} {dg_fd:16.4f} {abs((dg-dg_fd)/dg):12.2e}")
    print("  1 mGal = 1e-5 m/s^2.  The two routes agree to round-off: the")
    print("  (l-1) factor and the 1/gamma factor are not conventions to be")
    print("  looked up but consequences of Bruns' formula and Laplace's equation.")

    section("4. Degree variance: measuring the spectrum exponent")
    for name, cset, sset in (("synthetic signal", C, S),
                             ("white-noise control",
                              RNG.standard_normal((L_MAX + 1, L_MAX + 1)) * AMP_LAW,
                              RNG.standard_normal((L_MAX + 1, L_MAX + 1)) * AMP_LAW)):
        deg = np.arange(2, L_MAX + 1)
        var = np.array([np.sum(cset[l, :l + 1] ** 2) + np.sum(sset[l, :l + 1] ** 2)
                        for l in deg])
        degvar = var / (2.0 * deg + 1.0)
        slope, intercept = np.polyfit(np.log(deg), np.log(degvar), 1)
        print(f"  {name}: fitted log-log slope of the degree variance = "
              f"{slope:.3f}")
        for l in (2, 4, 8, 16, 32, 40):
            print(f"     l = {l:3d}   degree variance = {degvar[l-2]:.6e}   "
                  f"amplitude = {np.sqrt(degvar[l-2]):.6e}")
    print(f"  The input law sigma_l ~ l^-{AMP_POW:.0f} has degree variance")
    print(f"  ~ l^-{2*AMP_POW:.0f}, so the fitted slope should be about "
          f"{-2*AMP_POW:.1f} for the signal and 0 for the control.")

    section("5. The information budget and the resolution a degree implies")
    print("   L   coefficients (L+1)^2   half-wavelength pi R / L (km)")
    for L in (10, 20, 40, 60, 100, 200):
        print(f"  {L:3d} {((L+1)**2):22d} {np.pi*R_EARTH/L/1e3:31.1f}")
    print("  Coefficients grow as L^2 while resolution grows only as 1/L:")
    print("  every doubling of resolution costs four times as many parameters,")
    print("  and the data must determine all of them.")

    section("6. Signal-to-noise crossover degree")
    deg = np.arange(2, L_MAX + 1)
    sig = AMP_LAW * (2.0 / deg) ** AMP_POW
    noi = NOISE_LAW * deg
    print(f"  SYNTHETIC signal amplitude:  sigma_l = {AMP_LAW:.1e} (2/l)^{AMP_POW:.1f}")
    print(f"  SYNTHETIC error amplitude:   eps_l   = {NOISE_LAW:.1e} l")
    print("   l    sigma_l      eps_l      ratio   above noise?")
    for l in (2, 5, 10, 15, 20, 25, 30, 40):
        print(f"  {l:3d} {sig[l-2]:.4e} {noi[l-2]:.4e} {sig[l-2]/noi[l-2]:8.3f} "
              f"{'yes' if sig[l-2] > noi[l-2] else 'no'}")
    above = deg[sig > noi]
    l_star = int(above.max()) if above.size else 0
    print(f"  highest degree with signal above noise: {l_star} "
          f"-> half-wavelength {np.pi*R_EARTH/l_star/1e3:.0f} km")
    print("  A coefficient above the crossover is a statement about the model")
    print("  space, not about the Earth: it is determined by the regularisation")
    print("  and the a priori spectrum, both of which are assumptions.")


if __name__ == "__main__":
    main()
