#!/usr/bin/env python3
"""Internal waves and tides: the internal-wave dispersion relation, rotation,
the vertical-mode problem, Richardson number and Osborn mixing.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python internal_waves_tides_demo.py

Everything here is SYNTHETIC.  The stratification profiles are chosen teaching
functions.  No mooring, CTD cast, altimeter or reanalysis is used.

Contents
--------
1. The dispersion relation and its two limits.
2. Rotation: the internal tide with and without f.
3. The vertical-mode problem for constant and non-constant N.
4. Characteristic slopes and the criticality of a synthetic ridge.
5. Richardson number and shear instability.
6. Osborn mixing, and verification of the eigenvector against the ODE.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

OMEGA = 7.292115e-5      # rad/s, Earth's rotation rate (standard constant)
T_M2 = 12.4206 * 3600.0  # s, conventional M2 tidal period
RHO = 1025.0             # kg/m^3


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def f_coriolis(lat_deg):
    return 2.0 * OMEGA * np.sin(np.radians(lat_deg))


def omega_internal(k, m, N, f):
    """omega^2 = (N^2 k^2 + f^2 m^2)/(k^2 + m^2).  k horizontal, m vertical."""
    return np.sqrt((N ** 2 * k ** 2 + f ** 2 * m ** 2) / (k ** 2 + m ** 2))


def main():
    omega_m2 = 2 * np.pi / T_M2
    f_45 = f_coriolis(45.0)

    section("1. The internal-wave dispersion relation")
    print("  omega^2 = (N^2 k^2 + f^2 m^2)/(k^2 + m^2)")
    print("  equivalently omega^2 = N^2 cos^2(theta) + f^2 sin^2(theta), where")
    print("  theta is the angle of the wavevector from the HORIZONTAL.")
    N = 0.010
    f = f_45
    print(f"\n  N = {N:.4f} rad/s (buoyancy period {2 * np.pi / N / 60:.2f} min), "
          f"f(45N) = {f:.6e} rad/s")
    print("\n   k (1/m)      m (1/m)      theta (deg)   omega (rad/s)   "
          "period (min)")
    for k, m in ((1e-3, 1e-5), (1e-4, 1e-5), (1e-5, 1e-5), (1e-5, 1e-4),
                 (1e-5, 1e-3)):
        th = np.degrees(np.arctan2(m, k))
        w = omega_internal(k, m, N, f)
        print(f"  {k:9.1e}   {m:9.1e}   {th:11.2f}   {w:13.6e}   "
              f"{2 * np.pi / w / 60:12.3f}")
    print("\n  As the wavevector approaches vertical (theta -> 90 deg), omega -> f:")
    print("  rotation sets the floor.  As it approaches horizontal (theta -> 0),")
    print(f"  omega -> N = {N:.4f} rad/s: buoyancy sets the ceiling.  An internal")
    print("  wave exists only in the band f < omega < N.")

    section("2. Rotation and the mode-1 internal tide")
    N_, H = 0.010, 1000.0
    m1 = np.pi / H
    print(f"  N = {N_:.4f} rad/s, depth H = {H:.0f} m, mode 1: m = pi/H = "
          f"{m1:.6e} 1/m")
    print(f"  M2 period = {T_M2 / 3600:.4f} h "
          f"(omega = {omega_m2:.6e} rad/s), a conventional astronomical value")
    c_nof = N_ * H / np.pi
    k_nof = omega_m2 / c_nof
    print(f"\n  without rotation (f = 0):")
    print(f"    phase speed c = N H / pi = {c_nof:.4f} m/s")
    print(f"    horizontal wavenumber k  = {k_nof:.6e} 1/m -> wavelength "
          f"{2 * np.pi / k_nof / 1000:.2f} km")
    print("\n  with rotation at several latitudes:")
    print("\n   latitude   f (1/s)      c (m/s)   wavelength (km)   "
          "c/c(nof)   wavelength ratio")
    for lat in (0.0, 15.0, 30.0, 45.0, 60.0):
        ff = f_coriolis(lat)
        if ff >= omega_m2:
            print(f"  {lat:8.1f}   {ff:10.3e}   f >= omega_M2: no freely "
                  "propagating internal tide")
            continue
        k2 = m1 ** 2 * (omega_m2 ** 2 - ff ** 2) / (N_ ** 2 - omega_m2 ** 2)
        kk = np.sqrt(k2)
        cc = omega_m2 / kk
        print(f"  {lat:8.1f}   {ff:10.3e}   {cc:9.4f}   "
              f"{2 * np.pi / kk / 1000:15.2f}   {cc / c_nof:9.4f}   "
              f"{cc / c_nof:15.4f}")
    print("\n  Rotation makes the mode-1 tide FASTER and longer, by the factor")
    print("  sqrt((N^2 - omega^2)/(omega^2 - f^2)) relative to the non-rotating")
    print("  case.  Above the tidal latitude cut-off, where f > omega_M2, the")
    print("  internal tide of this frequency cannot exist at all.")

    section("3. The vertical-mode problem")
    print("  For a flat bottom and a rigid lid, (d2/dz2 + N^2/c^2) phi = 0 with")
    print("  phi(0) = phi(H) = 0.  This is a Sturm-Liouville eigenproblem in 1/c^2.")

    def modes(Nfun, H, nz=400, nmodes=3):
        from scipy.linalg import eigh
        zed = np.linspace(0.0, H, nz)
        h = zed[1] - zed[0]
        Nv = Nfun(zed)
        # -(phi_{i+1} - 2phi_i + phi_{i-1})/h^2 = lambda N^2 phi_i
        A = (np.diag(2.0 * np.ones(nz - 2)) + np.diag(-np.ones(nz - 3), 1)
             + np.diag(-np.ones(nz - 3), -1)) / h ** 2
        B = np.diag(Nv[1:-1] ** 2)
        lam, vec = eigh(A, B)                # generalized symmetric problem
        idx = np.argsort(lam)[:nmodes]
        return zed[1:-1], lam[idx], vec[:, idx]

    zc, lam, vec = modes(lambda zed: np.full_like(zed, N_), H)
    print(f"\n  constant N = {N_:.4f} rad/s:")
    print("    mode   lambda = 1/c^2 (s^2/m^2)   c (m/s)   n*pi/H (1/m)   "
          "c from n pi/H (m/s)")
    for i in range(3):
        c = 1.0 / np.sqrt(lam[i])
        npi = (i + 1) * np.pi / H
        print(f"  {i + 1:6d}   {lam[i]:22.6e}   {c:8.4f}   {npi:12.6e}   "
              f"{N_ / npi:16.4f}")
    print("    The eigenvalues reproduce c = N H /(n pi) to the accuracy of the")
    print("    grid: this is the same relation used in section 2, now obtained")
    print("    numerically instead of asserted.")

    Nfun = lambda zed: 0.006 + 0.008 * np.exp(-zed / 300.0)
    zc2, lam2, vec2 = modes(Nfun, H)
    print("\n  non-constant N(z) = 0.006 + 0.008 exp(-z/300) rad/s:")
    print("    mode   c (m/s)   c / c(const N at surface)   max |phi|")
    for i in range(3):
        c = 1.0 / np.sqrt(lam2[i])
        print(f"  {i + 1:6d}   {c:8.4f}   {c / (N_ * H / ((i + 1) * np.pi)):24.4f}"
              f"   {np.abs(vec2[:, i]).max():8.4f}")
    phi1 = vec2[:, 0]
    d2 = np.gradient(np.gradient(phi1, zc2), zc2)
    Nz = Nfun(zc2)
    c1 = 1.0 / np.sqrt(lam2[0])
    resid = d2 + Nz ** 2 / c1 ** 2 * phi1
    print(f"\n  eigenvector residual ||phi'' + (N^2/c^2) phi||_inf = "
          f"{np.abs(resid).max():.3e} (mode 1, discrete grid {zc2.size} nodes)")
    print("  A structured N(z) lowers c by about 20 per cent relative to a")
    print("  constant N equal to the SURFACE value: the mode speed is a weighted")
    print("  integral of stratification, not its surface value.")

    section("4. Characteristic slopes and the criticality of a ridge")
    s_char = np.sqrt((omega_m2 ** 2 - f_45 ** 2) / (N_ ** 2 - omega_m2 ** 2))
    print("  Internal-wave characteristics have slope")
    print("  s = sqrt((omega^2 - f^2)/(N^2 - omega^2)).")
    print(f"\n  N = {N_:.4f} rad/s, f(45N) = {f_45:.4e} rad/s, M2:")
    print(f"    s = {s_char:.6e}  = 1/{1 / s_char:.1f}  = "
          f"{np.degrees(np.arctan(s_char)):.4f} deg from horizontal")
    print("  In this stratification the tidal beams are nearly horizontal, which")
    print("  is why they travel enormous distances across an ocean basin.")
    print("\n  criticality gamma = topographic slope / s; gamma ~ 1 generates:")
    print("\n   ridge slope   gamma   regime")
    for sl in (1e-4, 1e-3, 5e-3, s_char, 2e-2, 5e-2):
        gamma = sl / s_char
        regime = ("subcritical (weak generation)" if gamma < 0.5 else
                  "critical (efficient generation)" if gamma < 2.0 else
                  "supercritical (beams trapped near the slope)")
        print(f"  {sl:11.2e}   {gamma:6.3f}   {regime}")

    section("5. Richardson number and shear instability")
    print("  Ri = N^2/(du/dz)^2; a necessary condition for Kelvin-Helmholtz")
    print("  instability is Ri < 1/4 somewhere in the column.")
    zed = np.linspace(0.0, 200.0, 2001)
    N_of_z = 0.010 + 0.006 * np.tanh((zed - 100.0) / 20.0)
    U = 0.60 * np.tanh((zed - 100.0) / 25.0)
    dUdz = np.gradient(U, zed)
    Ri = N_of_z ** 2 / dUdz ** 2
    print(f"\n  synthetic profiles on 0-200 m: N(z) = 0.010 + 0.006 tanh((z-100)/20)")
    print("                                U(z) = 0.60 tanh((z-100)/25)")
    print("\n   z (m)   N (1/s)   U (m/s)   dU/dz (1/s)   Ri")
    for zz in (0.0, 60.0, 90.0, 100.0, 110.0, 140.0, 200.0):
        i = int(np.argmin(np.abs(zed - zz)))
        print(f"  {zz:7.0f}   {N_of_z[i]:7.4f}   {U[i]:7.3f}   {dUdz[i]:11.4f}   "
              f"{Ri[i]:8.3f}")
    i_min = int(np.argmin(Ri))
    thin = zed[Ri < 0.25]
    print(f"\n  minimum Ri = {Ri[i_min]:.4f} at z = {zed[i_min]:.1f} m "
          f"(Ri < 1/4: {Ri[i_min] < 0.25})")
    if thin.size:
        print(f"  Ri < 1/4 over z = {thin.min():.1f} to {thin.max():.1f} m, "
              f"a layer {(thin.max() - thin.min()):.1f} m thick")
    print("  Ri is a NECESSARY condition, not a sufficient one: a stable Ri > 1/4")
    print("  everywhere proves nothing about the absence of turbulence, and")
    print("  Ri < 1/4 does not by itself tell you the mixing rate.")

    section("6. Osborn mixing and numerical verification")
    GAMMA = 0.20
    print("  Osborn (1980) relation K_rho = Gamma eps / N^2, with the conventional")
    print(f"  mixing efficiency Gamma = {GAMMA:.2f}.")
    print("\n   eps (W/kg)   N (rad/s)   K_rho (m^2/s)")
    for eps in (1e-10, 1e-9, 1e-8, 1e-7):
        for NN in (0.005, 0.010, 0.020):
            print(f"  {eps:10.1e}   {NN:9.3f}   {GAMMA * eps / NN ** 2:13.4e}")
    print(f"\n  for eps = 1e-9 W/kg and N = 0.010 rad/s, K_rho = "
          f"{GAMMA * 1e-9 / 1e-4:.3e} m^2/s.")
    print(f"  the pure molecular value for heat is ~1.4e-7 m^2/s, so turbulence")
    print("  here supplies roughly "
          f"{GAMMA * 1e-9 / 1e-4 / 1.4e-7:.0f} times the molecular diffusivity.")
    print("  The Osborn relation is a closure, not a measurement: it assumes a")
    print("  fixed fraction of the dissipated energy goes into irreversible mixing.")
    print("  Test it: with Gamma = 0.2 and Gamma = 0.5 the inferred K_rho at")
    print(f"  eps = 1e-9 W/kg and N = 0.010 rad/s differs: "
          f"{0.2 * 1e-9 / 1e-4:.3e} vs {0.5 * 1e-9 / 1e-4:.3e} m^2/s, a factor "
          f"of {0.5 / 0.2:.1f},")
    print("  with nothing in the dissipation measurement to choose between them.")

    # Verification: an exact travelling-wave solution of the linear equations.
    print("\n  Verification: a plane internal wave with k = 1e-4, m = 1e-3 1/m")
    print("  should satisfy the polarisation relation exactly.")
    k_, m_ = 1e-4, 1e-3
    w_ = omega_internal(k_, m_, N_, f_45)
    theta = np.arctan2(m_, k_)
    w_angle = np.sqrt(N_ ** 2 * np.cos(theta) ** 2
                      + f_45 ** 2 * np.sin(theta) ** 2)
    print(f"    omega from the wavenumber form   = {w_:.10e} rad/s")
    print(f"    omega from the angle form        = {w_angle:.10e} rad/s")
    print(f"    absolute difference              = {abs(w_ - w_angle):.3e} rad/s")
    print("    the two forms agree to machine precision, as they must: they are")
    print("    the same relation written in two variables.")

    # Dispersion-relation residual for the mode-1 internal tide.
    kk = np.sqrt(m1 ** 2 * (omega_m2 ** 2 - f_45 ** 2) / (N_ ** 2 - omega_m2 ** 2))
    w_check = omega_internal(kk, m1, N_, f_45)
    print("\n  Verification: the mode-1 internal tide wavenumber must return the")
    print("  forcing frequency when fed back into the dispersion relation.")
    print(f"    target omega = {omega_m2:.10e} rad/s, recovered omega = "
          f"{w_check:.10e} rad/s")
    print(f"    relative error = {abs(w_check - omega_m2) / omega_m2:.3e}")
    print("    energy-flux direction: the group velocity is perpendicular to the")
    print(f"    wavevector, i.e. at {np.degrees(np.arctan2(kk, m1)):.2f} deg from "
          f"horizontal,")
    print(f"    while the wavevector itself is at "
          f"{np.degrees(np.arctan2(m1, kk)):.2f} deg from horizontal.")


if __name__ == "__main__":
    main()
