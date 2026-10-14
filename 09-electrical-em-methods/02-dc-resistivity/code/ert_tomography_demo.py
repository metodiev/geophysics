#!/usr/bin/env python3
"""ERT acquisition design: signal, depth of investigation, and lateral resolution.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_tomography_demo.py

Everything is SYNTHETIC.  The electrode layout, the resistivities, the current
and the noise floor are chosen teaching values; no instrument, site or data set
is used.

Contents
--------
1. Survey geometry and the number of four-electrode measurements.
2. Signal and depth of investigation as a function of the dipole-dipole
   separation n, computed with the exact layered forward model.
3. The usable range of n for a stated noise floor.
4. Depth coverage at the centre of the line.
5. Lateral resolution at depth, from the analytic half-space kernel.
6. A design table: target depth and size versus array choice.
"""

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

RNG = np.random.default_rng(20261014)

N_ELECTRODES = 48
SPACING = 2.0           # m
I_INJECT = 0.1          # A
NOISE_FLOOR_MV = 0.5    # mV, synthetic receiver noise floor
RHO_LEVELS = (100.0, 1000.0)


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def k_general(A, B, M, N):
    bracket = (1.0 / abs(A - M) - 1.0 / abs(A - N)
               - 1.0 / abs(B - M) + 1.0 / abs(B - N))
    return 2.0 * np.pi / bracket


def kernel_R(rhos, hs, lam):
    R = 0.0
    for i in range(len(hs) - 1, -1, -1):
        k = (rhos[i + 1] - rhos[i]) / (rhos[i + 1] + rhos[i])
        R = (k + R) * np.exp(-2.0 * lam * hs[i]) / (1.0 + k * R)
    return R


def layered_potential(rhos, hs, r, I=1.0):
    lam_max = 30.0 / min(hs)
    integrand = (lambda lam: (1.0 / (1.0 - kernel_R(rhos, hs, lam)) - 1.0)
                 * j0(lam * r))
    value, _ = quad(integrand, 0.0, lam_max, limit=600)
    return rhos[0] * I / (2.0 * np.pi) * (1.0 / abs(r) + value)


def dV(rhos, hs, A, B, M, N, I=1.0):
    return (layered_potential(rhos, hs, M - A, I)
            - layered_potential(rhos, hs, N - A, I)
            - layered_potential(rhos, hs, M - B, I)
            + layered_potential(rhos, hs, N - B, I))


def fd_profile(A, B, M, N, grid, rho=100.0, eps=1e-3):
    """Cumulative sensitivity F(z) and its derivative, exactly as in 09-02-02."""
    ref = dV([rho, rho], [1.0e6], A, B, M, N, I_INJECT)
    F = np.array([
        (dV([rho * (1.0 + eps), rho, rho], [z, 1.0e6], A, B, M, N, I_INJECT) - ref)
        / (eps * ref) for z in grid])
    return np.gradient(F, grid)


def main():
    section("1. Survey geometry")
    xs = np.arange(N_ELECTRODES) * SPACING
    print(f"  SYNTHETIC ERT line: {N_ELECTRODES} electrodes, spacing "
          f"{SPACING:.1f} m")
    print(f"  line length = {(N_ELECTRODES - 1) * SPACING:.1f} m, "
          f"positions {xs[0]:.0f} to {xs[-1]:.0f} m")
    total = 0
    counts = {}
    for n in range(1, 7):
        block = 4 + n                      # C1 C2 P1 P2 span in spacings
        cnt = (N_ELECTRODES - block) + 1 if N_ELECTRODES >= block else 0
        counts[n] = cnt
        total += cnt
        print(f"  dipole-dipole n = {n}: {cnt:3d} measurements, array aperture "
              f"{block * SPACING:5.1f} m")
    print(f"  total measurements for n = 1..6: {total}")
    print("  the count is linear in the number of electrodes and roughly")
    print("  independent of n: the cost of depth is signal, not data volume.")

    section("2. Signal and depth of investigation versus n")
    # DC resistivity is scale invariant: an array scaled by a has the same
    # sensitivity profile in units of a.  So the DOI for spacing a is a times
    # the dimensionless DOI measured with a = 1 m.
    unit_grid = np.arange(0.05, 40.01, 0.25)
    print(f"  current I = {I_INJECT:.2f} A; sensitivity measured with a = 1 m and")
    print("  rescaled, because the DC response depends only on z/a")
    print("     n   |k|/a     dV (mV), rho=100   DOI/a     DOI at a=2 m (m)   "
          "peak depth/a")
    doi_unit = {}
    for n in range(1, 7):
        A, B, M, N = 0.0, 1.0, (n + 1) * 1.0, (n + 2) * 1.0
        s_unit = fd_profile(A, B, M, N, unit_grid)
        cum = np.concatenate([[0.0], np.cumsum(0.5 * (np.abs(s_unit[1:])
                                                     + np.abs(s_unit[:-1]))
                                               * np.diff(unit_grid))])
        cum = cum / cum[-1]
        doi_unit[n] = float(np.interp(0.5, cum, unit_grid))
        k = abs(k_general(0.0, SPACING, (n + 1) * SPACING, (n + 2) * SPACING))
        dv_r = 100.0 * I_INJECT / k
        print(f"  {n:4d} {abs(k_general(A, B, M, N)):8.4f} {dv_r * 1e3:21.4f} "
              f"{doi_unit[n]:9.3f} {doi_unit[n] * SPACING:17.2f} "
              f"{unit_grid[int(np.argmax(np.abs(s_unit)))]:12.3f}")
    # verify the scaling directly for one array
    A, B, M, N = 0.0, SPACING, 4 * SPACING, 5 * SPACING
    g2 = np.arange(0.1, 80.01, 0.5)
    s2 = fd_profile(A, B, M, N, g2)
    cum2 = np.concatenate([[0.0], np.cumsum(0.5 * (np.abs(s2[1:])
                                                  + np.abs(s2[:-1]))
                                           * np.diff(g2))])
    cum2 = cum2 / cum2[-1]
    doi_direct = float(np.interp(0.5, cum2, g2))
    print(f"\n  scaling check, n = 3, a = {SPACING:.1f} m: DOI computed directly "
          f"= {doi_direct:.3f} m,")
    print(f"    DOI from the unit profile = {doi_unit[3] * SPACING:.3f} m, "
          f"difference {abs(doi_direct - doi_unit[3] * SPACING) * 1e3:.2f} mm")
    print("  the depth of investigation is proportional to the electrode spacing,")
    print("  so it is the SPACING and not the number of measurements that sets")
    print("  how deep a line can see.")

    section("4. Depth coverage at the centre of the line")
    print("  sum |dF/dz| over the measurements whose centre lies within 20 m of")
    print("  the line centre, for two survey designs:")
    gcov = np.arange(0.1, 20.01, 0.2)
    for nmax, label in ((2, "shallow design n = 1..2"),
                        (6, "deep design n = 1..6")):
        profile = np.zeros_like(gcov)
        used = 0
        for n in range(1, nmax + 1):
            span = (2 + n) * SPACING
            centre_shift = span / 2.0
            for e0 in np.arange(0.0, (N_ELECTRODES - 4 - n) * SPACING
                                + 1e-9, SPACING):
                if abs(e0 + centre_shift - xs[-1] / 2.0) > 20.0:
                    continue
                A, B = e0, e0 + SPACING
                M, N = e0 + (n + 1) * SPACING, e0 + (n + 2) * SPACING
                profile += np.abs(fd_profile(A, B, M, N, gcov))
                used += 1
        cum = np.concatenate([[0.0], np.cumsum(0.5 * (profile[1:] + profile[:-1])
                                              * np.diff(gcov))])
        cum = cum / cum[-1]
        depth_half = float(np.interp(0.5, cum, gcov))
        depth_90 = float(np.interp(0.9, cum, gcov))
        print(f"    {label}: {used} measurements, half of the sensitivity above"
              f" {depth_half:.1f} m, 90% above {depth_90:.1f} m")
    print("  adding long-offset data deepens the coverage, but the marginal")
    print("  gain per measurement falls: that is why design is a choice.")

    section("5. Lateral resolution at depth")
    print("  footprint at depth z: w(x) = normalised integral of |S_rho| over")
    print("  y; the width is the distance between the 10% and 90% points of the")
    print("  cumulative footprint, i.e. the smearing of a sharp edge.")
    for n, z_frac in ((1, 1.0), (3, 1.0), (6, 1.0)):
        A, B = 0.0, SPACING
        M, N = (n + 1) * SPACING, (n + 2) * SPACING
        z = doi_unit[n] * SPACING * z_frac
        xg = np.arange(-60.0, 60.51, 0.5)

        def kernel_integrand(yy, xx):
            def grad(xe):
                dx, dy = xx - xe, yy
                r2 = dx * dx + dy * dy + z * z
                return np.array([-dx, -dy, -z]) / r2 ** 1.5
            return (grad(A) - grad(B)) @ (grad(M) - grad(N))

        w = np.abs(np.array([quad(lambda yy: kernel_integrand(yy, xx),
                                  -80.0, 80.0, limit=200)[0] for xx in xg]))
        w = w / np.trapezoid(w, xg)
        cw = np.concatenate([[0.0], np.cumsum(0.5 * (w[1:] + w[:-1])
                                             * np.diff(xg))])
        cw = cw / cw[-1]
        x10 = float(np.interp(0.1, cw, xg))
        x90 = float(np.interp(0.9, cw, xg))
        print(f"    n = {n}, z = {z:5.2f} m: 10-90% width = {x90 - x10:6.2f} m, "
              f"peak-to-width ratio {z / (x90 - x10):.2f}")
    print("  the footprint widens roughly in proportion to depth: resolution")
    print("  and depth trade one for one, and n buys depth without sharpening.")

    section("6. Design table: matching the spacing to the target")
    print("  using the scaling DOI = a * DOI/a, the required spacing for a")
    print("  target depth d is a = d / (DOI/a) for the deepest usable n.")
    n_deep = 6
    print("     target depth   required a (m)   aperture (m)   footprint width "
          "at target   electrodes for 100 m")
    xg_u = np.arange(-30.0, 30.01, 0.25)

    def footprint_width(a, z):
        """10-90% width of the |kernel| footprint for dipole-dipole n=6."""
        A, B = 0.0, a
        M, N = (n_deep + 1) * a, (n_deep + 2) * a

        def ki(yy, xx):
            def grad(xe):
                dx, dy = xx - xe, yy
                r2 = dx * dx + dy * dy + z * z
                return np.array([-dx, -dy, -z]) / r2 ** 1.5
            return (grad(A) - grad(B)) @ (grad(M) - grad(N))

        w = np.abs(np.array([quad(lambda yy: ki(yy, xx), -80.0, 80.0,
                                  limit=200)[0] for xx in xg_u * a]))
        w = w / np.trapezoid(w, xg_u * a)
        cw = np.concatenate([[0.0], np.cumsum(0.5 * (w[1:] + w[:-1])
                                             * np.diff(xg_u * a))])
        cw = cw / cw[-1]
        return float(np.interp(0.9, cw, xg_u * a) - np.interp(0.1, cw, xg_u * a))

    for d in (2.0, 5.0, 10.0, 20.0, 40.0):
        a_req = d / doi_unit[n_deep]
        aperture = (n_deep + 2) * a_req
        width = footprint_width(a_req, d)
        n_elec = int(np.ceil(100.0 / a_req)) + 1 + n_deep + 2
        print(f"  {d:12.1f} {a_req:16.2f} {aperture:14.1f} {width:28.1f} "
              f"{n_elec:19d}")
    print("  deeper targets need longer spacings, which need longer arrays:")
    print("  the number of electrodes grows as 1/a, so the cost of depth is")
    print("  paid in cable, in signal, and in the size of the footprint that")
    print("  sets the resolution.")


if __name__ == "__main__":
    main()
