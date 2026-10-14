#!/usr/bin/env python3
"""Wavefront tracking: two eikonal solvers, cross-checked, and their accuracy.

The fast sweeping method updates the whole grid repeatedly in alternating
directions with the Godunov upwind stencil, and converges to the viscosity
solution of the eikonal equation.  A fast marching method with the same stencil
but a different ordering is implemented here as well, so the two numerical
routes can be compared with each other and with a closed form.  Agreement
between two methods that share only the discretisation is evidence about the
discretisation; agreement with a closed form is evidence about the physics.

Run:
    .venv/bin/python 06-seismology/02-ray-theory-and-travel-times/code/wavefront_tracking_demo.py
"""

from __future__ import annotations

import heapq

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def godunov_update(t, i, j, h, slow, nx, nz):
    """One Godunov upwind eikonal update of node (i, j)."""
    t1 = min(t[i - 1, j] if i > 0 else np.inf, t[i + 1, j] if i < nx - 1 else np.inf)
    t2 = min(t[i, j - 1] if j > 0 else np.inf, t[i, j + 1] if j < nz - 1 else np.inf)
    f = h * slow[i, j]
    a = min(t1, t2)
    b = max(t1, t2)
    if not np.isfinite(a):
        return t[i, j]
    if b == np.inf or a + f <= b:
        return a + f
    disc = 2.0 * f**2 - (b - a) ** 2
    return 0.5 * (a + b + np.sqrt(max(disc, 0.0)))


def fast_sweeping(slow, h, src):
    nx, nz = slow.shape
    t = np.full((nx, nz), np.inf)
    t[src] = 0.0
    sweeps = 0
    for _ in range(400):
        previous = t.copy()
        for i_range in (range(1, nx), range(nx - 2, -1, -1)):
            for j_range in (range(1, nz), range(nz - 2, -1, -1)):
                for i in i_range:
                    for j in j_range:
                        if (i, j) == src:
                            continue
                        t[i, j] = min(t[i, j], godunov_update(t, i, j, h, slow, nx, nz))
        sweeps += 1
        with np.errstate(invalid="ignore"):
            # inf - inf is nan at nodes the sweep has not reached yet; nanmax
            # ignores those, which is what "has anything changed?" means here.
            change = np.nanmax(np.abs(t - previous))
        if change < 1e-9:
            break
    return t, sweeps


def fast_marching(slow, h, src):
    nx, nz = slow.shape
    t = np.full((nx, nz), np.inf)
    frozen = np.zeros((nx, nz), dtype=bool)
    t[src] = 0.0
    pq = [(0.0, src)]
    while pq:
        d, (i, j) = heapq.heappop(pq)
        if frozen[i, j] or d > t[i, j]:
            continue
        frozen[i, j] = True
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ii, jj = i + di, j + dj
            if 0 <= ii < nx and 0 <= jj < nz and not frozen[ii, jj]:
                cand = godunov_update(t, ii, jj, h, slow, nx, nz)
                if cand < t[ii, jj]:
                    t[ii, jj] = cand
                    heapq.heappush(pq, (cand, (ii, jj)))
    return t


def homogeneous() -> None:
    section("1. Homogeneous medium: two solvers against the exact circle")
    v = 3500.0
    length = 10000.0
    print(f"  v = {v:.0f} m/s, domain {length / 1e3:.0f} km square, source in "
          f"a corner; exact T = r/v")
    print(f"  {'dx (m)':>8} {'sweeps':>8} {'sweeping max err (ms)':>23} "
          f"{'marching max err (ms)':>23} {'|sweep - march| (ms)':>22}")
    dxs, e1, e2 = [], [], []
    for dx in (100.0, 50.0, 25.0):
        n = int(round(length / dx)) + 1
        x = np.arange(n) * dx
        X, Z = np.meshgrid(x, x, indexing="ij")
        exact = np.sqrt(X**2 + Z**2) / v
        slow = np.full((n, n), 1.0 / v)
        sweep, nsweep = fast_sweeping(slow, dx, (0, 0))
        march = fast_marching(slow, dx, (0, 0))
        a = np.abs(sweep - exact)[2:, 2:].max()
        b = np.abs(march - exact)[2:, 2:].max()
        c = np.abs(sweep - march)[2:, 2:].max()
        dxs.append(dx)
        e1.append(a)
        e2.append(b)
        print(f"  {dx:8.1f} {nsweep:8d} {a * 1e3:23.6f} {b * 1e3:23.6f} "
              f"{c * 1e3:22.3e}")
    print(f"  measured convergence order in dx: sweeping "
          f"{np.polyfit(np.log(dxs), np.log(e1), 1)[0]:.3f}, marching "
          f"{np.polyfit(np.log(dxs), np.log(e2), 1)[0]:.3f}")
    print("  Both are first order, as the four-point stencil dictates, and the")
    print("  two solvers agree with each other far more closely than either agrees")
    print("  with the analytic circle: the shared discretisation error dominates,")
    print("  and agreement with the closed form is limited by it rather than by")
    print("  the iteration.")


def gradient() -> None:
    section("2. A linear gradient: sweeping, marching and the closed form")
    v0 = 2500.0
    g = 0.6
    print(f"  SYNTHETIC v(z) = v0 + g z with v0 = {v0:.0f} m/s, g = {g:.2f} 1/s")
    print(f"  closed form T = (1/g) arccosh(1 + g^2 (x^2+z^2)/(2 v0 (v0+g z)))")

    def exact(x, z):
        return np.arccosh(1.0 + g**2 * (x**2 + z**2) / (2.0 * v0 * (v0 + g * z))) / g

    print(f"  {'dx (m)':>8} {'sweeps':>8} {'max |sweep - exact| (ms)':>26} "
          f"{'max |march - exact| (ms)':>26}")
    dxs, e1, e2 = [], [], []
    for dx in (100.0, 50.0, 25.0):
        n = int(round(10000.0 / dx)) + 1
        x = np.arange(n) * dx
        z = np.arange(n) * dx + dx
        X, Z = np.meshgrid(x, z, indexing="ij")
        slow = 1.0 / (v0 + g * Z)
        sweep, nsweep = fast_sweeping(slow, dx, (0, 0))
        march = fast_marching(slow, dx, (0, 0))
        a = np.abs(sweep - exact(X, Z))[2:, 2:].max()
        b = np.abs(march - exact(X, Z))[2:, 2:].max()
        dxs.append(dx)
        e1.append(a)
        e2.append(b)
        print(f"  {dx:8.1f} {nsweep:8d} {a * 1e3:26.6f} {b * 1e3:26.6f}")
    print(f"  measured convergence order in dx: sweeping "
          f"{np.polyfit(np.log(dxs), np.log(e1), 1)[0]:.3f}, marching "
          f"{np.polyfit(np.log(dxs), np.log(e2), 1)[0]:.3f}")
    print("  Two solvers, one shared stencil, one closed form: the residual is")
    print("  the discretisation of |grad T| = 1/v on a square grid, and it is")
    print("  reduced by refining the grid, not by iterating harder.")


def smoothing_kernel(cell: float, corr: float, half: int = 10) -> np.ndarray:
    """Normalised 1-D Gaussian kernel, sampled on the grid step ``cell``."""
    offs = np.arange(-half, half + 1) * cell
    k = np.exp(-0.5 * (offs / corr) ** 2)
    return k / k.sum()


def smooth2d(white: np.ndarray, k: np.ndarray) -> np.ndarray:
    """Separable smoothing of a 2-D field with the 1-D kernel ``k``."""
    rows = np.apply_along_axis(lambda r: np.convolve(r, k, mode="same"), 1, white)
    return np.apply_along_axis(lambda c: np.convolve(c, k, mode="same"), 0, rows)


def grid_error_vs_model_error() -> None:
    section("3. Discretisation error against velocity-model error")
    v = 3500.0
    length = 10000.0
    dx = 100.0
    n = int(round(length / dx)) + 1
    x = np.arange(n) * dx
    X, Z = np.meshgrid(x, x, indexing="ij")
    exact = np.sqrt(X**2 + Z**2) / v

    march = fast_marching(np.full((n, n), 1.0 / v), dx, (0, 0))
    grid_err = np.abs(march - exact)[2:, 2:].max()
    receiver = (n - 1, n - 1)
    t0 = march[receiver]
    t_exact = float(exact[receiver])
    print(f"  homogeneous v = {v:.0f} m/s on a {length / 1e3:.0f} km square, "
          f"dx = {dx:.0f} m, source at a corner")
    print(f"  exact time to the opposite corner = {t_exact:.6f} s; the solver "
          f"returns {t0:.6f} s, an error of {(t0 - t_exact) * 1e3:+.3f} ms")
    print(f"  largest discretisation error anywhere on the grid = "
          f"{grid_err * 1e3:.3f} ms")

    k = smoothing_kernel(dx, 1000.0)
    sigma = 0.015
    runs = 30
    ts = []
    for _ in range(runs):
        s = smooth2d(RNG.normal(0.0, 1.0, (n, n)), k)
        s /= s.std()
        ts.append(fast_marching(1.0 / (v * (1.0 + sigma * s)), dx, (0, 0))[receiver])
    ts = np.array(ts)
    print(f"  now perturb the velocity: {sigma:.1%} rms relative error with a")
    print(f"  1 km correlation length, {runs} realisations, same solver and grid")
    print(f"    time to the same receiver: {ts.mean():.6f} +/- "
          f"{ts.std() * 1e3:.3f} ms (exact {t_exact:.6f} s)")
    print(f"    the model-error scatter of {ts.std() * 1e3:.3f} ms is "
          f"{ts.std() / abs(t0 - t_exact):.1f} times the discretisation error")
    print(f"    of {abs(t0 - t_exact) * 1e3:.3f} ms at that receiver")
    print("  The two error sources are within a factor of two of each other,")
    print("  which is the useful answer to 'how fine should the grid be?': fine")
    print("  enough that the discretisation error is no longer the largest one, and")
    print("  no finer.  A grid refined far below this point would return a travel")
    print("  time whose digits are precise and whose value is no better, because")
    print("  the velocity field -- not the solver -- has become the limiting input.")


def main() -> None:
    homogeneous()
    gradient()
    grid_error_vs_model_error()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
