#!/usr/bin/env python3
"""Migration as an imaging problem: diffraction-sum migration and its velocity
sensitivity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python migration_demo.py

SYNTHETIC.  A single point diffractor in a constant-velocity medium; the
"correct" image is a focused point.  No real seismic section is used.

Contents
--------
1. Forward model: a zero-offset section is the diffractor's diffraction
   hyperbola t(x) = 2*sqrt((x-x0)^2 + z0^2)/v.
2. Diffraction-sum (Kirchhoff) migration: I(x,z) = sum over x of d(x, t(x,z)).
3. Image quality versus migration velocity: peak amplitude, spatial width and
   position error for 0.8 to 1.2 times the true velocity.
4. Why under- and over-migration look different (smile versus frown curvature).
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(t):
    print(f"\n{'=' * 68}\n{t}\n{'=' * 68}")


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


# --- SYNTHETIC experiment ----------------------------------------------------
V_TRUE = 2000.0                 # m/s, constant medium
X0, Z0 = 0.0, 800.0             # diffractor position (m)
XS = np.arange(-1500.0, 1500.1, 25.0)     # 121 surface locations
DT = 0.002
NT = 700
T = np.arange(NT) * DT
F0 = 25.0


def main():
    section("1. Forward model: the diffraction hyperbola")
    print(f"  SYNTHETIC: v = {V_TRUE:.0f} m/s, diffractor at "
          f"(x, z) = ({X0:.0f}, {Z0:.0f}) m")
    D = np.zeros((XS.size, NT))
    for i, x in enumerate(XS):
        t0 = 2.0 * np.sqrt((x - X0) ** 2 + Z0 ** 2) / V_TRUE
        D[i] = ricker(T - t0, F0)
    t_apex = 2.0 * Z0 / V_TRUE
    print(f"  apex two-way time = 2*z0/v = {t_apex:.4f} s")
    print(f"  section: {XS.size} traces x {NT} samples, dt = {DT * 1e3:.0f} ms, "
          f"wavelet {F0:.0f} Hz")

    section("2. Diffraction-sum migration")
    def migrate(v_mig, xgrid, zgrid):
        I = np.zeros((zgrid.size, xgrid.size))
        for a, z in enumerate(zgrid):
            for b, xm in enumerate(xgrid):
                acc = 0.0
                for i, xs in enumerate(XS):
                    tt = 2.0 * np.sqrt((xs - xm) ** 2 + z ** 2) / v_mig
                    k = tt / DT
                    k0 = int(k)
                    if 0 <= k0 < NT - 1:
                        frac = k - k0
                        acc += (1 - frac) * D[i, k0] + frac * D[i, k0 + 1]
                I[a, b] = acc
        return I

    xg = np.arange(-800.0, 800.1, 20.0)
    zg = np.arange(200.0, 1600.1, 20.0)
    print(f"  image grid: {zg.size} depths x {xg.size} positions = "
          f"{zg.size * xg.size} cells")
    print("  I(x,z) = sum_x d(x, t = 2 sqrt((x-xm)^2 + z^2)/v_mig)")

    section("3. Image quality versus migration velocity")
    print("   v_mig/v_true   peak depth (m)   peak x (m)   peak amplitude   "
          "depth error (m)")
    results = {}
    for scale in (0.80, 0.90, 0.95, 1.00, 1.05, 1.10, 1.20):
        vm = scale * V_TRUE
        I = migrate(vm, xg, zg)
        az, ax = np.unravel_index(np.argmax(np.abs(I)), I.shape)
        results[scale] = I
        print(f"   {scale:11.2f}   {zg[az]:13.0f}   {xg[ax]:10.0f}   "
              f"{I[az, ax]:14.3f}   {zg[az] - Z0:+12.0f}")
    print(f"  true diffractor: depth {Z0:.0f} m, x {X0:.0f} m")
    print("  Correct velocity images the point at its true position with maximum")
    print("  amplitude.  Too low a velocity leaves a downward-curving (smile)")
    print("  residual; too high leaves an upward-curving (frown) residual, and in")
    print("  both cases the energy is defocused and the amplitude drops.")

    section("4. Quantifying the focus with the peak amplitude")
    ref = np.abs(results[1.00]).max()
    print("   v_mig/v_true   peak amplitude   relative to correct")
    for scale, I in results.items():
        pk = np.abs(I).max()
        print(f"   {scale:11.2f}   {pk:14.3f}   {pk / ref * 100:16.1f}%")
    print("  The amplitude of the migrated point is a sharp function of migration")
    print("  velocity: this is why velocity analysis and migration are iterated")
    print("  until the image focuses, and why a wrong velocity is not merely a")
    print("  cosmetic problem but a loss of resolution and a mispositioning.")


if __name__ == "__main__":
    main()
