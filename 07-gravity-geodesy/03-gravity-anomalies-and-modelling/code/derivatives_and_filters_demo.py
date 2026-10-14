#!/usr/bin/env python3
"""Derivatives, upward and downward continuation, and Euler deconvolution on a
synthetic potential field, with every filter verified against an analytic field.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python derivatives_and_filters_demo.py

All models and data in this module are SYNTHETIC.  The harmonic field, the noise
level and the source are chosen teaching values.

Contents
--------
1. A harmonic field on a periodic grid, with analytic derivatives.
2. Fourier filters verified against the analytic derivatives: horizontal
   derivative, vertical derivative, upward continuation.
3. Noise amplification of the vertical derivative versus a low-pass cutoff.
4. Downward continuation: error growth with depth.
5. Euler deconvolution on a compact source: the structural index and the window.
6. Euler deconvolution with noise: depth error versus noise level.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_SI = 6.67430e-11
MGAL_TO_SI = 1.0e-5
NX = 101
DX = 100.0
L = NX * DX


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def mgal(g_si):
    return g_si / MGAL_TO_SI


def harmonic_field():
    """Sum of Laplace-satisfying harmonics, exactly periodic on the grid.

    g(x, y, z) = sum A cos(kx x) cos(ky y) exp(-k z), with z positive upward so
    the field decays with height.  Every mode sits on an FFT bin, so the discrete
    transform of the sampled field is exact and the filter check is a true test.
    """
    k1 = 2.0 * np.pi / L
    modes = [(3, 2, 5.0), (5, 0, 3.0), (2, 5, -2.0), (7, 4, 1.5)]
    x = np.arange(NX) * DX - L / 2.0
    X, Y = np.meshgrid(x, x, indexing="ij")
    g = np.zeros_like(X)
    for m, n, a in modes:
        g += a * np.cos(m * k1 * X) * np.cos(n * k1 * Y)
    return X, Y, g, modes, k1


def analytic(X, Y, modes, plane="value", shift=0.0):
    """Analytic field or derivative, at height z = shift (positive upward)."""
    k1 = 2.0 * np.pi / L
    out = np.zeros_like(X)
    for m, n, a in modes:
        kx, ky = m * k1, n * k1
        k = np.hypot(kx, ky)
        env = np.exp(-k * shift)
        if plane == "value":
            out += a * np.cos(kx * X) * np.cos(ky * Y) * env
        elif plane == "dx":
            out += -a * kx * np.sin(kx * X) * np.cos(ky * Y) * env
        elif plane == "dy":
            out += -a * ky * np.cos(kx * X) * np.sin(ky * Y) * env
        elif plane == "dz":
            out += -a * k * np.cos(kx * X) * np.cos(ky * Y) * env
    return out


def wavenumbers():
    f = np.fft.fftfreq(NX, d=DX) * 2.0 * np.pi
    KX, KY = np.meshgrid(f, f, indexing="ij")
    return KX, KY, np.hypot(KX, KY)


def main():
    section("1. A harmonic field and its analytic derivatives")
    X, Y, g, modes, k1 = harmonic_field()
    KX, KY, K = wavenumbers()
    print(f"grid {NX} x {NX}, spacing {DX:.0f} m, extent {L / 1000:.0f} km, "
          "periodic")
    print("SYNTHETIC modes (m, n, amplitude in mGal):", modes)
    print(f"fundamental wavenumber k1 = {k1:.6e} 1/m; Nyquist wavelength "
          f"2*dx = {2 * DX:.0f} m; Nyquist wavenumber {np.pi / DX:.4f} 1/m")
    print(f"field: min {g.min():.4f} mGal, max {g.max():.4f} mGal")

    section("2. Fourier filters verified against the analytic field")
    G = np.fft.fft2(g)
    print("     operator                          max |FFT - analytic|")
    for name, filt, plane, shift in (
        ("horizontal derivative d/dx (1/mGal)", 1j * KX, "dx", 0.0),
        ("horizontal derivative d/dy (1/mGal)", 1j * KY, "dy", 0.0),
        ("vertical derivative d/dz, z up", -K, "dz", 0.0),
        ("upward continuation to 1000 m", np.exp(-K * 1000.0), "value", 1000.0),
        ("upward continuation to 3000 m", np.exp(-K * 3000.0), "value", 3000.0),
    ):
        got = np.real(np.fft.ifft2(filt * G))
        want = analytic(X, Y, modes, plane, shift)
        print(f"  {name:34s}  {np.abs(got - want).max():.3e} mGal/m or mGal")
    print("  On a periodic grid the wavenumber filters are exact, not approximate;")
    print("  the small residuals are floating-point round-off.")

    section("3. Noise amplification of the vertical derivative")
    noise_mgal = 0.10
    noise_grid = noise_mgal * RNG.standard_normal(g.shape)
    Gn = np.fft.fft2(g + noise_grid)
    Gnoise = np.fft.fft2(noise_grid)
    truth_dz = analytic(X, Y, modes, "dz")
    print(f"added white noise rms = {noise_mgal:.2f} mGal; the field itself has "
          f"rms {np.std(g):.3f} mGal")
    print("   cutoff wavelength   total error   of which bias   of which noise")
    print("   (m)                 (mGal/m)      (mGal/m)        (mGal/m)")
    for lam_c in (np.inf, 2000.0, 1000.0, 500.0, 300.0):
        if np.isinf(lam_c):
            filt = -K
        else:
            kc = 2.0 * np.pi / lam_c
            filt = -K / (1.0 + (K / kc) ** 8)
        total = np.real(np.fft.ifft2(filt * Gn))
        bias = np.real(np.fft.ifft2(filt * G))
        noise_only = np.real(np.fft.ifft2(filt * Gnoise))
        err = np.sqrt(np.mean((total - truth_dz) ** 2))
        bia = np.sqrt(np.mean((bias - truth_dz) ** 2))
        noi = np.sqrt(np.mean(noise_only ** 2))
        label = "none" if np.isinf(lam_c) else f"{lam_c:.0f}"
        print(f"  {label:>17s}   {err:12.6f}   {bia:14.6f}   {noi:14.6f}")
    print("  The error splits cleanly into bias (cutting real short wavelengths)")
    print("  and variance (passing noise).  No cutoff removes both.")

    section("4. Downward continuation: error growth with depth")
    lam_c = 1000.0
    kc = 2.0 * np.pi / lam_c
    lp = 1.0 / (1.0 + (K / kc) ** 8)
    print(f"  continuing the noisy field down by dz; full band versus a low pass at "
          f"{lam_c:.0f} m")
    print("   depth (m)   full band: rms error   low pass: rms error   "
          "continued-field rms, full band")
    print("               (mGal)                 (mGal)                (mGal)")
    for dz in (200.0, 500.0, 1000.0, 2000.0):
        want = analytic(X, Y, modes, "value", -dz)
        cont_full = np.real(np.fft.ifft2(np.exp(+K * dz) * Gn))
        cont_lp = np.real(np.fft.ifft2(lp * np.exp(+K * dz) * Gn))
        print(f"  {dz:9.0f}   {np.sqrt(np.mean((cont_full - want) ** 2)):20.3e}   "
              f"{np.sqrt(np.mean((cont_lp - want) ** 2)):19.3e}   "
              f"{np.sqrt(np.mean(cont_full ** 2)):28.3e}")
    kn = np.pi / DX
    print(f"  exp(k dz) at the Nyquist wavenumber k = {kn:.4f} 1/m is "
          f"{np.exp(kn * 500.0):.2e} for 500 m and "
          f"{np.exp(kn * 1000.0):.2e} for 1000 m:")
    print("  At 200 m the low pass cuts the error from 8.6e1 mGal to 2.9e-1 mGal,")
    print("  a factor of 300; by 2 km even the low-passed error is enormous, because")
    print("  the cutoff wavelength (1000 m) is shorter than the continuation depth.")
    print("  Full-band downward continuation of noisy data is a noise amplifier, and")
    print("  the low pass that makes it stable also truncates the signal.")

    section("5. Euler deconvolution on a compact source")
    x0, y0, z0, mass = 200.0, -300.0, 800.0, 2.0e11
    x1, y1, z1, mass1 = -1400.0, 1400.0, 1200.0, 3.0e11
    xs = np.arange(-3000.0, 3000.0 + 1.0, 75.0)
    Xg, Yg = np.meshgrid(xs, xs, indexing="ij")

    def fields(xc, yc, zc, m):
        dxs, dys = Xg - xc, Yg - yc
        r = np.sqrt(dxs ** 2 + dys ** 2 + zc ** 2)
        return (G_SI * m * zc / r ** 3,
                -3.0 * G_SI * m * zc * dxs / r ** 5,
                -3.0 * G_SI * m * zc * dys / r ** 5,
                G_SI * m * (3.0 * zc ** 2 - r ** 2) / r ** 5)

    ga, gxa, gya, gza = fields(x0, y0, z0, mass)
    print(f"SYNTHETIC point mass: {mass:.1e} kg at "
          f"(x0, y0, z0) = ({x0:.0f}, {y0:.0f}, {z0:.0f}) m")
    print(f"  peak anomaly {mgal(ga.max()):.4f} mGal on an {xs.size} x {xs.size} "
          "grid at 75 m spacing")
    print("  Euler equation fitted in each window, unknowns (x0, y0, z0, B):")
    print("     x0 gx + y0 gy + z0 gz + N B = x gx + y gy + N g")
    print("  window centred on the source, radius 1200 m, single source:")
    print("     N   x0 (m)     y0 (m)     z0 (m)     B (mGal)    rms residual (mGal)")
    win = np.hypot(Xg - x0, Yg - y0) <= 1200.0
    for N in (0.0, 1.0, 2.0, 3.0):
        A = np.column_stack([gxa[win], gya[win], gza[win], N * np.ones(win.sum())])
        b = Xg[win] * gxa[win] + Yg[win] * gya[win] + N * ga[win]
        sol, *_ = np.linalg.lstsq(A, b, rcond=None)
        res = A @ sol - b
        print(f"  {N:5.0f}   {sol[0]:8.1f}   {sol[1]:9.1f}   {sol[2]:9.1f}   "
              f"{mgal(sol[3]):10.4f}   {mgal(np.sqrt(np.mean(res ** 2))):.2e}")
    print("  N = 2 is the structural index of a point mass for this gravity field,")
    print("  and it returns the true location; the other indices return a")
    print("  compromise that fits a wrong model of the source.  For an isolated")
    print("  exact source the equation holds pointwise, so window size is immaterial")
    print("  -- which is why the next table, with two sources, is the useful test.")

    gb, gxb, gyb, gzb = fields(x1, y1, z1, mass1)
    Gt, gxt, gyt, gzt = ga + gb, gxa + gxb, gya + gyb, gza + gzb
    print(f"  add a second mass {mass1:.1e} kg at "
          f"({x1:.0f}, {y1:.0f}, {z1:.0f}) m and slide the window (N = 2):")
    print("     window centre   radius (m)   recovered x0   recovered y0   "
          "recovered z0   rms residual (mGal)")
    for cx, cy, rad in ((x0, y0, 1000.0), (x1, y1, 1500.0), (-600.0, 500.0, 800.0)):
        w = np.hypot(Xg - cx, Yg - cy) <= rad
        A = np.column_stack([gxt[w], gyt[w], gzt[w], 2.0 * np.ones(w.sum())])
        b = Xg[w] * gxt[w] + Yg[w] * gyt[w] + 2.0 * Gt[w]
        sol, *_ = np.linalg.lstsq(A, b, rcond=None)
        res = A @ sol - b
        print(f"  ({cx:7.0f},{cy:7.0f})   {rad:10.0f}   {sol[0]:13.1f}   "
              f"{sol[1]:13.1f}   {sol[2]:13.1f}   "
              f"{mgal(np.sqrt(np.mean(res ** 2))):17.4f}")
    print("  With two sources no window returns either exactly: each estimate is")
    print("  pulled towards the other body, and the residual -- 0.2 mGal here against")
    print("  4.5e-11 mGal for the isolated source -- is the honest diagnostic that the")
    print("  single-source assumption has failed.  Euler deconvolution is a")
    print("  sliding-window estimator, and the window is an assumption.")

    section("6. Euler with noise: the depth error it buys")
    print("   noise rms (mGal)   mean z0 (m)   scatter of z0 (m)")
    for nl in (0.0, 0.02, 0.05, 0.10):
        z0s = []
        for _ in range(200):
            pert = nl * MGAL_TO_SI * RNG.standard_normal(ga.shape)
            A = np.column_stack([gxa[win], gya[win], gza[win],
                                 2.0 * np.ones(win.sum())])
            b = (Xg[win] * gxa[win] + Yg[win] * gya[win]
                 + 2.0 * (ga[win] + pert[win]))
            sol, *_ = np.linalg.lstsq(A, b, rcond=None)
            z0s.append(sol[2])
        print(f"  {nl:16.2f}   {np.mean(z0s):12.1f}   {np.std(z0s):16.2f}")
    print(f"  the true depth is {z0:.0f} m; with 0.05 mGal noise the recovered depth")
    print("  scatters by only a couple of metres here because the source is strong")
    print("  (2 mGal peak) and the window is wide.  A weaker anomaly, or a narrower")
    print("  window, gives a correspondingly larger scatter.")


if __name__ == "__main__":
    main()
