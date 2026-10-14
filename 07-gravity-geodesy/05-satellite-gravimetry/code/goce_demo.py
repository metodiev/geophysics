#!/usr/bin/env python3
"""Satellite gravimetry, part 2: the gravity-gradient tensor measured by a
satellite gradiometer -- what it is, how it scales with degree, and what
sampling it buys over a range link.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python goce_demo.py

Everything here is SYNTHETIC.  The orbit altitudes, the synthetic zonal
coefficients, the surface-gradient spectrum and the gradiometer noise are
teaching values chosen for this module; they are not the parameters of any real
mission and no measured gravity field is used.

Contents
--------
1. The gradient tensor of the monopole field at orbit altitude, in s^-2 and E.
2. Trace-free check: the Hessian of any potential in vacuum has zero trace.
3. The exact degree scaling d2/dr2 of a zonal term: (l+1)(l+2) r^-(l+3),
   verified by finite differences.
4. The transfer function T(l) = (l+1)(l+2)(R/a)^(l+2): where it peaks, and how
   the peak moves with altitude.
5. Signal-to-noise crossover degree for a stated synthetic spectrum and a stated
   gradiometer noise; two altitudes compared.
6. The trace as a free diagnostic on a noisy measured tensor.
"""

import numpy as np
from scipy.special import eval_legendre

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
G = 6.67430e-11             # m^3 kg^-1 s^-2
GM_EARTH = 3.986004418e14   # m^3 s^-2
R_EARTH = 6371.0e3          # m, rounded mean Earth radius
EOTVOS = 1.0e-9             # s^-2, definition of 1 E

# --- SYNTHETIC teaching parameters ------------------------------------------
ALT_LOW_KM = 250.0
ALT_HIGH_KM = 500.0
C20_SYN = 1.0e-4            # synthetic degree-2 zonal coefficient
SURF_SPECTRUM_2 = 1.0e-10   # s^-2, synthetic surface radial-gradient at l = 2
SPECTRUM_EXP = 1.5          # synthetic surface spectrum ~ l^-1.5
GRAD_NOISE_E = 0.10         # E, synthetic per-component gradiometer noise


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def monopole_hessian(x):
    """Hessian of U = GM/r in the 'gradient tensor' convention, G_ij = d2U/dx_i dx_j."""
    r = np.linalg.norm(x)
    n = x / r
    return GM_EARTH / r ** 3 * (3.0 * np.outer(n, n) - np.eye(3))


def main():
    section("1. The gradient tensor of the monopole field at orbit altitude")
    for alt_km in (ALT_LOW_KM, ALT_HIGH_KM):
        a = R_EARTH + alt_km * 1e3
        g = GM_EARTH / a ** 3
        x = np.array([a, 0.0, 0.0])
        H = monopole_hessian(x)
        vals = [H[0, 0], H[1, 1], H[2, 2]]
        print(f"altitude {alt_km:.0f} km  (r = {a/1e3:.1f} km):")
        print(f"  GM/r^3 = {g:.6e} s^-2 = {g/EOTVOS:.4e} E")
        print(f"  G_rr (radial)   = {vals[0]:+.6e} s^-2 = {vals[0]/EOTVOS:+.6e} E")
        print(f"  G_tt (tangential) = {vals[1]:+.6e} s^-2 = {vals[1]/EOTVOS:+.6e} E")
        print(f"  G_cc (tangential) = {vals[2]:+.6e} s^-2 = {vals[2]/EOTVOS:+.6e} E")
        print(f"  trace = {np.trace(H):+.3e} s^-2  (sum of eigenvalues = 0)")
    print("  The diagonal components are of order 10^5-10^6 E, while useful")
    print("  anomaly information in the gradient tensor is of order 1-100 E:")
    print("  the dynamic-range problem is five to six orders of magnitude.")

    section("2. Trace-free check on a synthetic zonal field at altitude")
    a = R_EARTH + ALT_LOW_KM * 1e3
    th = np.deg2rad(40.0)

    def U_zonal(x, c20):
        r = np.linalg.norm(x)
        ct = x[2] / r
        return GM_EARTH / r * ((R_EARTH / r) ** 2) * c20 * eval_legendre(2, ct)

    h = 100.0
    x0 = a * np.array([np.sin(th), 0.0, np.cos(th)])
    H = np.zeros((3, 3))
    ex = np.eye(3)
    for i in range(3):
        for j in range(3):
            H[i, j] = (U_zonal(x0 + h * ex[i] + h * ex[j], C20_SYN)
                       - U_zonal(x0 + h * ex[i] - h * ex[j], C20_SYN)
                       - U_zonal(x0 - h * ex[i] + h * ex[j], C20_SYN)
                       + U_zonal(x0 - h * ex[i] - h * ex[j], C20_SYN)) / (4.0 * h * h)
    print(f"  synthetic zonal C_20 = {C20_SYN:.1e}, altitude {ALT_LOW_KM:.0f} km, "
          f"co-latitude {np.rad2deg(th):.1f} deg")
    print(f"  numerical Hessian diagonal: {np.diag(H)[0]:+.6e}, "
          f"{np.diag(H)[1]:+.6e}, {np.diag(H)[2]:+.6e} s^-2")
    print(f"  off-diagonal G_xy = {H[0,1]:+.4e}, G_xz = {H[0,2]:+.4e} s^-2")
    print(f"  trace of the anomalous Hessian = {np.trace(H):+.4e} s^-2 "
          f"({np.trace(H)/EOTVOS:+.4e} E)")
    print(f"  largest component = {np.max(np.abs(H))/EOTVOS:.4f} E")
    print(f"  trace / largest component = {abs(np.trace(H))/np.max(np.abs(H)):.4e}")
    print("  Laplace's equation makes the trace zero in vacuum: the tensor has 5")
    print("  independent components, not 6, and the trace is a checkable zero.")

    section("3. Exact degree scaling of d2U/dr2 for a zonal term")
    print("  U_l = (GM/r)(R/r)^l C_l0 P_l(cos th), so")
    print("      d2U_l/dr2 = (l+1)(l+2) GM R^l C_l0 P_l(cos th) / r^(l+3).")
    print("   l    finite-difference d2U/dr2 (s^-2)   closed form (s^-2)   rel. diff")
    r0 = R_EARTH + ALT_LOW_KM * 1e3
    c_l = 1.0e-6
    for l in (2, 5, 10, 20, 40, 60, 80, 120):
        pl = float(eval_legendre(l, np.cos(th)))
        def f(r):
            return GM_EARTH / r * (R_EARTH / r) ** l * c_l * pl
        hr = 100.0
        fd = (f(r0 + hr) - 2.0 * f(r0) + f(r0 - hr)) / hr ** 2
        # written as (R/r)^l to avoid overflowing R^l for large l
        closed = ((l + 1) * (l + 2) * GM_EARTH * c_l * pl
                  * (R_EARTH / r0) ** l / r0 ** 3)
        print(f"  {l:3d} {fd:28.6e} {closed:24.6e} {abs((fd-closed)/closed):12.2e}")
    print("  The (l+1)(l+2) factor is exact for the radial second derivative: a")
    print("  gradiometer does not measure the potential, it measures its")
    print("  curvature, and higher degrees curve more sharply.")

    section("4. Transfer function T(l) = (l+1)(l+2)(R/a)^(l+2)")
    print("   l    T(l), a = 250 km    T(l), a = 500 km")
    lmax = 200
    ls = np.arange(1, lmax + 1)
    T_low = (ls + 1) * (ls + 2) * (R_EARTH / (R_EARTH + ALT_LOW_KM * 1e3)) ** (ls + 2)
    T_high = (ls + 1) * (ls + 2) * (R_EARTH / (R_EARTH + ALT_HIGH_KM * 1e3)) ** (ls + 2)
    for l in (5, 10, 20, 40, 60, 80, 100, 150, 200):
        print(f"  {l:3d} {T_low[l-1]:18.3f} {T_high[l-1]:18.3f}")
    i_low, i_high = int(np.argmax(T_low)), int(np.argmax(T_high))
    print(f"  peak at degree {i_low+1} for h = {ALT_LOW_KM:.0f} km, "
          f"degree {i_high+1} for h = {ALT_HIGH_KM:.0f} km")
    print("  The exact continuous peak solves 1/(l+1) + 1/(l+2) = ln(a/R):")
    for alt_km in (ALT_LOW_KM, ALT_HIGH_KM):
        ratio = (R_EARTH + alt_km * 1e3) / R_EARTH
        c = np.log(ratio)
        # 2l + 3 = c (l^2 + 3l + 2) -> c l^2 + (3c - 2) l + (2c - 3) = 0
        roots = np.roots([c, 3.0 * c - 2.0, 2.0 * c - 3.0])
        l_exact = float(np.max(roots.real))
        print(f"    h = {alt_km:.0f} km: a/R = {ratio:.5f}, "
              f"exact l* = {l_exact:.2f}, crude 2/ln(a/R) = {2.0/c:.1f}, "
              f"integer peak = {int(np.argmax(T_low if alt_km == ALT_LOW_KM else T_high))+1}")
    print("  T(l) rises as l^2 (higher degrees have more curvature) and falls as")
    print("  (R/a)^(l+2) (they attenuate faster).  The peak is where the two")
    print("  balance; a gradiometer at altitude h is most sensitive to that")
    print("  degree relative to the same coefficient at the surface.")

    section("5. Signal-to-noise crossover degree")
    print(f"  SYNTHETIC surface radial-gradient spectrum: A_s(l) = "
          f"{SURF_SPECTRUM_2:.0e} * (2/l)^{SPECTRUM_EXP:.1f} s^-2")
    print(f"  SYNTHETIC gradiometer noise: {GRAD_NOISE_E:.2f} E per component,")
    print("  propagated to a degree-l estimate as noise/sqrt(2l+1):")
    print("   altitude   S/N at l=10   S/N at l=50   l_max(S/N>1)   "
          "half-wavelength")
    for alt_km in (ALT_LOW_KM, 300.0, ALT_HIGH_KM):
        T = (ls + 1) * (ls + 2) * (R_EARTH / (R_EARTH + alt_km * 1e3)) ** (ls + 2)
        a_s = SURF_SPECTRUM_2 * (ls / 2.0) ** (-SPECTRUM_EXP)
        sig = a_s * T / EOTVOS * 1e3                                   # mE
        noi = GRAD_NOISE_E * 1e3 / np.sqrt(2 * ls + 1)                 # mE
        snr = sig / noi
        ok = ls[snr > 1.0]
        lmax_ok = int(ok.max()) if ok.size else 0
        print(f"   {alt_km:6.0f} km {snr[9]:12.2f} {snr[49]:14.2f} "
              f"{lmax_ok:10d}   "
              + (f"{np.pi*R_EARTH/lmax_ok/1e3:.0f} km" if lmax_ok else "none"))
        print(f"               signal at l=10: {sig[9]:8.3f} mE, noise "
              f"{noi[9]:7.3f} mE;  signal at l=100: {sig[99]:8.5f} mE, noise "
              f"{noi[99]:7.3f} mE")
    print("  Lower altitude is better at every degree, but the usable degree is")
    print("  finite: beyond the peak of T(l) the (R/a)^(l+2) attenuation beats the")
    print("  l^2 growth, and no amount of extra mission lifetime recovers it.")

    section("6. The trace as a free diagnostic on a noisy tensor")
    a = R_EARTH + ALT_LOW_KM * 1e3
    g_rr = 2.0 * GM_EARTH / a ** 3
    print("  A measured tensor is a 3x3 symmetric matrix whose true diagonal sum is")
    print("  zero in vacuum.  First, with consistent SYNTHETIC noise only:")
    print("   noise (E)   rms off-diagonal (E)   rms trace (E)   trace / offdiag")
    od_rms_ref = None
    for noise_e in (0.01, 0.1, 1.0):
        n = noise_e * EOTVOS
        tr_list, od_list = [], []
        for _ in range(4000):
            A = RNG.standard_normal((3, 3)) * n
            A = 0.5 * (A + A.T)
            tr_list.append(abs(np.trace(A)))
            od_list.append(np.sqrt(A[0, 1] ** 2 + A[0, 2] ** 2 + A[1, 2] ** 2))
        tr_rms = np.sqrt(np.mean(np.square(tr_list)))
        od_rms = np.sqrt(np.mean(np.square(od_list)))
        if od_rms_ref is None:
            od_rms_ref = od_rms
        print(f"   {noise_e:9.2f} {od_rms/EOTVOS:22.4f} {tr_rms/EOTVOS:16.4f}"
              f" {tr_rms/od_rms:16.4f}")
    print("  A trace of the same size as the noise is the signature of noise alone.")
    print("  For symmetrised noise the trace rms is sqrt(3) times a component and")
    print("  the off-diagonal norm rms is sqrt(3/2) times a component, so the ratio")
    print("  is sqrt(2) = 1.414, independent of the noise level.  A trace much")
    print("  larger than 1.4x the off-diagonal norm is an inconsistency.")
    print("  Now a CALIBRATION error: scale the radial component by (1+eps).")
    print(f"  the true radial component at {ALT_LOW_KM:.0f} km is "
          f"{g_rr/EOTVOS:.1f} E, so the trace picks up eps x that:")
    print("     eps      induced trace (E)   S/N against the stated component noise")
    for eps in (1e-5, 1e-4, 1e-3, 1e-2):
        induced = eps * g_rr / EOTVOS
        print(f"   {eps:8.0e} {induced:18.4f} {induced/GRAD_NOISE_E:23.1f}")
    print("  A one-part-in-a-thousand scale error is already 27 sigma against the")
    print("  stated noise, and one part in ten thousand is still 2.7 sigma.  The")
    print("  trace is a zero that the physics guarantees and the inversion cannot")
    print("  check; a nonzero trace mixes instrument error with mis-modelled")
    print("  non-gravitational accelerations, and the check flags the problem")
    print("  without separating the two causes.")


if __name__ == "__main__":
    main()
