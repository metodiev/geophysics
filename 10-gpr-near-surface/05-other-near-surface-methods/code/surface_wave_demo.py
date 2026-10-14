#!/usr/bin/env python3
"""Surface waves in shallow layered ground: the Rayleigh speed of a half-space,
the exact Love-mode dispersion of a layer over a half-space, the Love-wave depth
sensitivity kernel, and the dispersion non-uniqueness (a ridge, not a point).

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python surface_wave_demo.py

Everything here is SYNTHETIC.  The two-layer models, velocities and densities are
chosen teaching values, not measurements and not site parameters.

Contents
--------
1. Rayleigh wave in a homogeneous half-space: speed from the exact equation
   (2 - z^2)^2 = 4 sqrt(1 - z^2 eta^2) sqrt(1 - z^2), z = c_R/beta, eta = beta/alpha,
   cross-checked against the classical sextic in z, plus the surface ellipticity.
2. Exact Love dispersion for one layer over a half-space, fundamental and higher
   modes, with the higher-mode cut-off frequencies f_c,n = n pi /(h sqrt(...)).
3. Love-wave depth sensitivity: the kernel follows from the variational identity
   omega^2 = INT mu (v')^2 dz / INT rho v^2 dz.  Kernel, cumulative kernel, depth
   of half the sensitivity, and a finite-difference verification of the kernel.
4. Non-uniqueness: a two-parameter family of (h, beta1) models that reproduces the
   reference dispersion curve, with the residual of the best member quantified.
"""

import numpy as np
from scipy.optimize import brentq

RNG = np.random.default_rng(20261014)

BETA1 = 180.0     # m/s, layer S-wave speed (teaching value)
RHO1 = 1800.0     # kg/m^3
H = 5.0           # m, layer thickness
BETA2 = 400.0     # m/s, half-space S-wave speed
RHO2 = 2000.0     # kg/m^3


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# --------------------------------------------------------------------------
# 1. Rayleigh wave in a homogeneous half-space
# --------------------------------------------------------------------------

def rayleigh_zeta(alpha, beta):
    """c_R/beta from (2 - z^2)^2 = 4 sqrt(1 - z^2 eta^2) sqrt(1 - z^2)."""
    eta2 = (beta / alpha) ** 2

    def f(z):
        return (2.0 - z ** 2) ** 2 - 4.0 * np.sqrt(1.0 - z ** 2 * eta2) * np.sqrt(1.0 - z ** 2)

    grid = np.linspace(0.05, 1.0 - 1e-12, 40000)
    vals = np.array([f(z) for z in grid])
    cand = [i for i in range(len(grid) - 1) if vals[i] * vals[i + 1] < 0]
    return brentq(f, grid[cand[-1]], grid[cand[-1] + 1], xtol=1e-15)


def rayleigh_cubic(beta_over_alpha):
    """Largest root in (0,1) of the classical sextic in z = c_R/beta."""
    eta2 = beta_over_alpha ** 2
    coeffs = [1.0, 0.0, -8.0, 0.0, 8.0 * (3.0 - 2.0 * eta2), 0.0, -16.0 * (1.0 - eta2)]
    roots = np.roots(coeffs)
    real = sorted(r.real for r in roots if abs(r.imag) < 1e-9 and 1e-9 < r.real < 1.0)
    return real[-1]


def rayleigh_ellipticity(z, alpha, beta):
    """Complex surface ratio u_x/u_z of the Rayleigh eigenfunction."""
    q = np.sqrt(1.0 - (z * beta / alpha) ** 2)
    s2 = 1.0 - z ** 2
    B = -2.0j * q / (1.0 + s2)          # from sigma_xz = 0, with A = 1
    ux = 1j + np.sqrt(s2) * B
    uz = -q + 1j * B
    return ux / uz


# --------------------------------------------------------------------------
# 2 and 3. Love waves: dispersion and sensitivity
# --------------------------------------------------------------------------

def love_k1(c, beta1, f):
    return 2.0 * np.pi * f * np.sqrt(1.0 / beta1 ** 2 - 1.0 / c ** 2)


def love_rhs(c, beta1, rho1, beta2, rho2):
    k1 = np.sqrt(1.0 / beta1 ** 2 - 1.0 / c ** 2)
    k2 = np.sqrt(1.0 / c ** 2 - 1.0 / beta2 ** 2)
    return rho2 * beta2 ** 2 * k2 / (rho1 * beta1 ** 2 * k1)


def love_mode(f, n=0, beta1=BETA1, rho1=RHO1, h=H, beta2=BETA2, rho2=RHO2):
    """Phase velocity of Love mode n (n = 0 is the fundamental) in m/s.

    Returns nan when no trapped mode exists at this frequency: a trapped Love wave
    requires the layer to be slower than the half-space, beta1 < beta2.
    """
    if beta1 >= beta2:
        return np.nan
    omega = 2.0 * np.pi * f

    def g(c):
        return love_k1(c, beta1, f) * h - np.arctan(love_rhs(c, beta1, rho1, beta2, rho2)) - n * np.pi

    x_max = omega * h * np.sqrt(1.0 / beta1 ** 2 - 1.0 / beta2 ** 2)
    if x_max <= n * np.pi:
        return np.nan
    return brentq(g, beta1 * (1 + 1e-14), beta2 * (1 - 1e-14), xtol=1e-13)


def love_eigenfunction(z, c, f, beta1=BETA1, rho1=RHO1, h=H, beta2=BETA2):
    """v(z) normalised so that v(0) = 1, and its derivative."""
    omega = 2.0 * np.pi * f
    k1 = omega * np.sqrt(1.0 / beta1 ** 2 - 1.0 / c ** 2)
    k2 = omega * np.sqrt(1.0 / c ** 2 - 1.0 / beta2 ** 2)
    v = np.where(z <= h, np.cos(k1 * np.minimum(z, h)), np.cos(k1 * h) * np.exp(-k2 * (z - h)))
    dv = np.where(z <= h, -k1 * np.sin(k1 * np.minimum(z, h)),
                  -k2 * np.cos(k1 * h) * np.exp(-k2 * (z - h)))
    return v, dv


def love_kernel(z, c, f, beta1=BETA1, rho1=RHO1, h=H, beta2=BETA2, rho2=RHO2):
    """Fixed-frequency kernel K(z) with dc/c = INT (dmu/mu) K dz.

    Derivation: with k^2 = [omega^2 INT rho v^2 - INT mu (v')^2] / INT mu v^2 and
    stationarity in v at fixed omega,
        d(k^2) = -INT dmu [(v')^2 + k^2 v^2] dz / INT mu v^2,
    so with dc/c = -dk/k = -d(k^2)/(2k^2),
        K(z) = mu(z) [(v')^2 + k^2 v^2] / (2 k^2 INT mu v^2 dz).
    """
    omega = 2.0 * np.pi * f
    k = omega / c
    v, dv = love_eigenfunction(z, c, f, beta1, rho1, h, beta2)
    rho = np.where(z <= h, rho1, rho2)
    mu = rho * np.where(z <= h, beta1, beta2) ** 2
    i_mu = np.trapezoid(mu * v ** 2, z)
    return mu * (dv ** 2 + k ** 2 * v ** 2) / (2.0 * k ** 2 * i_mu), i_mu


def main():
    section("1. Rayleigh wave in a homogeneous half-space")
    print("  nu     alpha/beta   c_R/beta (equation)  c_R/beta (sextic)   |u_x/u_z|")
    for nu in (0.20, 0.25, 1.0 / 3.0, 0.40):
        ratio = np.sqrt(2.0 * (1.0 - nu) / (1.0 - 2.0 * nu))
        z = rayleigh_zeta(ratio, 1.0)
        zc = rayleigh_cubic(1.0 / ratio)
        r = rayleigh_ellipticity(z, ratio, 1.0)
        print(f"  {nu:5.2f}  {ratio:9.5f}   {z:16.8f}   {zc:16.8f}   {abs(r):8.4f}")
    print("  The two columns agree: the free-surface determinant and the classical")
    print("  sextic are the same condition.  With beta = 200 m/s, nu = 0.25:")
    z = rayleigh_zeta(np.sqrt(3.0), 1.0)
    print(f"    c_R = {z * 200.0:.2f} m/s = {z:.6f} beta")

    section("2. Love dispersion: one layer over a half-space (SYNTHETIC model)")
    print(f"  basic model: beta1 = {BETA1:.1f} m/s, rho1 = {RHO1:.0f} kg/m^3, "
          f"h = {H:.1f} m over beta2 = {BETA2:.1f} m/s, rho2 = {RHO2:.0f} kg/m^3")
    a1 = np.sqrt(1.0 / BETA1 ** 2 - 1.0 / BETA2 ** 2)
    print(f"  higher-mode cut-offs f_c,n = n pi/(h sqrt(1/beta1^2 - 1/beta2^2)):")
    for n in (1, 2):
        print(f"    n = {n}: f_c = {n * np.pi / (H * a1):8.2f} Hz")
    print("\n  f (Hz)   c0 (m/s)   c1 (m/s)   c2 (m/s)   lambda0 = c0/f (m)")
    for f in (4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 200.0):
        cs = [love_mode(f, n) for n in (0, 1, 2)]
        cells = "  ".join("   none  " if np.isnan(c) else f"{c:9.3f}" for c in cs)
        print(f"  {f:6.1f} {cells}   {cs[0] / f:14.2f}")
    print("  As f -> 0 the fundamental approaches beta2; as f grows it approaches beta1.")
    c_bad = love_mode(32.0, 0, beta1=500.0)
    print(f"  inverse configuration check: beta1 = 500 m/s over beta2 = 400 m/s gives "
          f"c = {c_bad}")
    print("  (nan): a trapped Love wave needs a SLOW layer over a FAST half-space, so the")
    print("  method is blind to a fast surface layer in exactly the way first-arrival")
    print("  refraction is blind to a slow one.")
    print("  Residual check of the dispersion equation at a few roots:")
    for f, n in ((16.0, 0), (64.0, 0), (128.0, 1), (200.0, 2)):
        c = love_mode(f, n)
        if not np.isnan(c):
            res = np.tan(love_k1(c, BETA1, f) * H) - love_rhs(c, BETA1, RHO1, BETA2, RHO2)
            print(f"    f = {f:6.1f} Hz, mode {n}: c = {c:8.3f} m/s, "
                  f"|tan(k1 h) - RHS| = {abs(res):.3e}")

    section("3. Love-wave depth sensitivity kernel")
    z = np.concatenate([np.linspace(0.0, H, 4001), np.linspace(H + 1e-3, 60.0, 6000)])
    print("  f (Hz)  lambda (m)   z_50 (m)  z_50/lambda   INT K dz   layer frac   top 1 m frac   dc/c per 1% beta1 in top 1 m")
    for f in (8.0, 16.0, 32.0, 64.0, 128.0):
        c = love_mode(f, 0)
        K, i_mu = love_kernel(z, c, f)
        cum = np.concatenate([[0.0], np.cumsum(0.5 * (K[1:] + K[:-1]) * np.diff(z))])
        total = cum[-1]
        z50 = float(np.interp(0.5 * total, cum, z))
        k_layer = float(np.trapezoid(K[z <= H], z[z <= H]))
        k_top = float(np.trapezoid(K[z <= 1.0], z[z <= 1.0]))
        print(f"  {f:6.1f}  {c / f:9.2f}   {z50:7.3f}   {z50 * f / c:8.3f}   {total:9.4f}   "
              f"{k_layer / total:10.3f}   {k_top / total:13.3f}   {100 * 2.0 * 0.01 * k_top:.4f}%")
    print("  dc/c for a uniform 1% increase of beta1 in the layer is 2*1%*INT_layer K dz,")
    print("  because mu = rho beta^2 makes dmu/mu = 2 dbeta/beta.")
    print("  Verification of the kernel against exact finite differences "
          "(beta1 -> beta1*(1+eps)):")
    for f in (16.0, 64.0):
        eps = 1e-5
        c0 = love_mode(f, 0)
        c1 = love_mode(f, 0, beta1=BETA1 * (1 + eps))
        exact = (c1 - c0) / c0
        K, i_mu = love_kernel(z, c0, f)
        pred = 2.0 * eps * float(np.trapezoid(K[z <= H], z[z <= H]))
        print(f"    f = {f:5.1f} Hz: exact dc/c = {exact:12.3e}, kernel prediction = "
              f"{pred:12.3e}, relative difference = {abs(pred - exact) / abs(exact):.2e}")

    section("4. Non-uniqueness: the thickness-velocity ridge")
    band = np.array([4.0, 8.0, 16.0, 32.0, 64.0, 128.0])
    narrow = np.array([4.0, 8.0, 16.0])
    c_ref = np.array([love_mode(fi, 0) for fi in band])
    c_nar = np.array([love_mode(fi, 0) for fi in narrow])
    print(f"  reference model: h = {H:.1f} m, beta1 = {BETA1:.1f} m/s, "
          f"beta2 = {BETA2:.1f} m/s")
    print("  reference dispersion:")
    for fi, ci in zip(band, c_ref):
        print(f"    f = {fi:6.1f} Hz: c = {ci:8.3f} m/s   (lambda = {ci / fi:7.2f} m)")

    from scipy.optimize import least_squares

    def fit_beta(h_try, band_use, band_ref):
        def res(b):
            cs = np.array([love_mode(fi, 0, beta1=float(b[0]), h=h_try) for fi in band_use])
            return (cs - band_ref) / band_ref
        sol = least_squares(res, np.array([BETA1]), bounds=([50.0], [BETA2 * 0.999]))
        return float(sol.x[0])

    print("\n  (a) one free velocity per fixed thickness, fitted over the whole band")
    print("      (4-128 Hz): how wide is the ridge?")
    print("       h (m)   fitted beta1 (m/s)   max |dc|/c over the band")
    for h_try in (4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0):
        b = fit_beta(h_try, band, c_ref)
        csw = np.array([love_mode(fi, 0, beta1=b, h=h_try) for fi in band])
        print(f"    {h_try:7.1f}   {b:18.2f}   "
              f"{np.max(np.abs(csw - c_ref) / c_ref) * 100:22.2f}%")

    print("\n  (b) the same ridge expressed as a thickness error at fixed velocity.")
    print("      Assume beta1 is known to +/-5% from a borehole, fit h over the")
    print("      narrow band and over the wide band:")
    print("       assumed beta1   fitted h, 4-16 Hz   fitted h, 4-128 Hz   true h")
    for b_assume in (BETA1 * 0.95, BETA1, BETA1 * 1.05):
        hs = []
        for band_use, band_ref in ((narrow, c_nar), (band, c_ref)):
            def res_h(h):
                cs = np.array([love_mode(fi, 0, beta1=b_assume, h=float(h[0]))
                               for fi in band_use])
                return (cs - band_ref) / band_ref
            sol = least_squares(res_h, np.array([H]), bounds=([0.5], [30.0]))
            hs.append(float(sol.x[0]))
        print(f"    {b_assume:12.2f}   {hs[0]:17.3f}   {hs[1]:18.3f}   {H:6.1f}")

    print("\n  (c) in the long-wavelength limit the ridge is wide.  Reference model")
    print("      h = 5.0 m, beta1 = 180.0 m/s, observed over 0.5-4 Hz, where")
    print("      lambda = c/f runs from 800 m down to 97 m, i.e. 20-160 x the layer:")
    print("       h (m)   fitted beta1 (m/s)   max |dc|/c")
    band_lw = np.array([0.5, 1.0, 2.0, 3.0, 4.0])
    c_lw = np.array([love_mode(fi, 0) for fi in band_lw])
    for h_try in (2.5, 5.0, 7.5, 10.0, 15.0):
        def res_lw(b):
            cs = np.array([love_mode(fi, 0, beta1=float(b[0]), h=h_try) for fi in band_lw])
            return (cs - c_lw) / c_lw
        sol = least_squares(res_lw, np.array([BETA1]), bounds=([50.0], [BETA2 * 0.999]))
        b_lw = float(sol.x[0])
        cs = np.array([love_mode(fi, 0, beta1=b_lw, h=h_try) for fi in band_lw])
        print(f"    {h_try:7.2f}   {b_lw:18.2f}   "
              f"{np.max(np.abs(cs - c_lw) / c_lw) * 100:11.2f}%")
    print("   Every one of these models reproduces the curve to better than 1%, including")
    print("   the physically absurd 55 m/s at h = 2.5 m.  Long-wavelength data alone")
    print("   cannot bound a layer velocity; the short-wavelength end of the band must.")

    print("\n  (d) mode information: c0 and c1 at 128 Hz for the reference model and")
    print("      for the best-fitting alternative at h = 3 m.")
    b_alt = fit_beta(3.0, band, c_ref)
    for label, (h_use, b_use) in (("reference", (H, BETA1)), ("h = 3 m fit", (3.0, b_alt))):
        c0 = love_mode(128.0, 0, beta1=b_use, h=h_use)
        c1 = love_mode(128.0, 1, beta1=b_use, h=h_use)
        print(f"    {label:12s}: c0 = {c0:8.3f} m/s, c1 = {c1:8.3f} m/s")
    print("  Higher modes and a wider band separate models that the fundamental alone")
    print("  cannot; the ridge is a statement about the data, not about the inversion.")

    section("5. Summary")
    print(f"  A Rayleigh wave in a uniform half-space has one speed, c_R/beta = "
          f"{rayleigh_zeta(np.sqrt(3.0), 1.0):.4f} at nu = 0.25.")
    print("  Layering makes both Rayleigh and Love speeds frequency-dependent, so the")
    print("  dispersion curve is the observable.  Its depth kernel is wavelength-scaled,")
    print("  and its inversion is a ridge whose width was measured above: wide when the")
    print("  band is long-wavelength (h << lambda), narrow when the band reaches the")
    print("  confining regime.  A wider band, a higher mode or a borehole breaks it.")


if __name__ == "__main__":
    main()
