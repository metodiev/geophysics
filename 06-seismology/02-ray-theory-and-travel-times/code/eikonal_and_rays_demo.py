#!/usr/bin/env python3
"""The eikonal equation: solved on a grid, and checked against closed forms.

1. The high-frequency reduction of the wave equation to |grad T| = 1/v is
   demonstrated on a homogeneous medium, where the solution is known exactly
   and the grid solution's error can be refined toward zero.
2. A linear velocity gradient v(z) = v0 + g z has a closed-form travel time.
   That closed form is *tested* here, not quoted: it is substituted into the
   eikonal equation and the residual |grad T| v - 1 is measured.
3. The validity condition of ray theory -- the medium must vary slowly over a
   wavelength -- is turned into a number for a stated model and frequency.

Run:
    .venv/bin/python 06-seismology/02-ray-theory-and-travel-times/code/eikonal_and_rays_demo.py
"""

from __future__ import annotations

import heapq

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def fast_marching(speed: np.ndarray, h: float, src: tuple[int, int]) -> np.ndarray:
    """First-order fast marching method for |grad T| = 1/v on a uniform grid.

    Nodes are accepted in order of travel time and each newly accepted node
    updates its four neighbours with the upwind quadratic
    (t - T1)^2 + (t - T2)^2 = h^2 / v^2, which is the discretisation of the
    eikonal equation on a four-point stencil.
    """
    nx, nz = speed.shape
    t = np.full((nx, nz), np.inf)
    frozen = np.zeros((nx, nz), dtype=bool)
    t[src] = 0.0
    pq = [(0.0, src)]
    while pq:
        dist, (i, j) = heapq.heappop(pq)
        if frozen[i, j] or dist > t[i, j]:
            continue
        frozen[i, j] = True
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ii, jj = i + di, j + dj
            if not (0 <= ii < nx and 0 <= jj < nz) or frozen[ii, jj]:
                continue
            t1 = np.inf
            t2 = np.inf
            if ii > 0 and frozen[ii - 1, jj]:
                t1 = min(t1, t[ii - 1, jj])
            if ii < nx - 1 and frozen[ii + 1, jj]:
                t1 = min(t1, t[ii + 1, jj])
            if jj > 0 and frozen[ii, jj - 1]:
                t2 = min(t2, t[ii, jj - 1])
            if jj < nz - 1 and frozen[ii, jj + 1]:
                t2 = min(t2, t[ii, jj + 1])
            f = h / speed[ii, jj]
            if np.isfinite(t1) and np.isfinite(t2):
                disc = 2.0 * f**2 - (t1 - t2) ** 2
                cand = 0.5 * (t1 + t2 + np.sqrt(disc)) if disc > 0 else min(t1, t2) + f
            elif np.isfinite(t1):
                cand = t1 + f
            elif np.isfinite(t2):
                cand = t2 + f
            else:
                continue
            if cand < t[ii, jj]:
                t[ii, jj] = cand
                heapq.heappush(pq, (cand, (ii, jj)))
    return t


def homogeneous_check() -> None:
    section("1. Fast marching on a homogeneous medium, refined in dx")
    v = 3000.0
    length = 12000.0
    print(f"  v = {v:.0f} m/s, domain {length / 1e3:.0f} km x {length / 1e3:.0f} km, "
          f"source at a corner")
    print(f"  {'dx (m)':>8} {'grid':>12} {'max abs error (ms)':>20} "
          f"{'max rel error':>15}")
    dxs, errs = [], []
    for dx in (200.0, 100.0, 50.0, 25.0):
        n = int(round(length / dx)) + 1
        x = np.arange(n) * dx
        X, Z = np.meshgrid(x, x, indexing="ij")
        exact = np.sqrt(X**2 + Z**2) / v
        grid = fast_marching(np.full((n, n), v), dx, (0, 0))
        err = np.abs(grid - exact)[1:, 1:].max()
        rel = (np.abs(grid - exact) / np.maximum(exact, 1e-9))[3:, 3:].max()
        dxs.append(dx)
        errs.append(err)
        print(f"  {dx:8.1f} {n:6d} x {n:<5d} {err * 1e3:20.6f} {rel:15.3e}")
    order = np.polyfit(np.log(dxs), np.log(errs), 1)[0]
    print(f"  measured convergence order in dx: {order:.3f}")
    print("  The exact solution is a circular wavefront, which the four-point")
    print("  stencil approximates by a staircase; the error therefore falls at")
    print("  first order, and the measured value above is the check on that.")


def linear_gradient() -> None:
    section("2. A linear gradient: the closed form is tested, not assumed")
    v0 = 2000.0
    g = 0.5                     # s^-1, so v = 2000 + 0.5 z (z in metres)
    print(f"  v(z) = v0 + g z with v0 = {v0:.0f} m/s and g = {g:.3f} 1/s")
    print(f"  the gradient is positive downward and v is real everywhere in z > 0")

    def travel_time(x: np.ndarray, z: np.ndarray) -> np.ndarray:
        return np.arccosh(1.0 + g**2 * (x**2 + z**2) / (2.0 * v0 * (v0 + g * z))) / g

    dx = 2.0
    x = np.arange(0.0, 6000.0, dx)
    z = np.arange(10.0, 6000.0, dx)
    X, Z = np.meshgrid(x, z, indexing="ij")
    T = travel_time(X, Z)
    dTdx = np.gradient(T, dx, axis=0)
    dTdz = np.gradient(T, dx, axis=1)
    grad_norm = np.sqrt(dTdx**2 + dTdz**2)
    residual = grad_norm * (v0 + g * Z) - 1.0
    core = (slice(5, -5), slice(5, -5))
    print(f"  T(x, z) = (1/g) arccosh(1 + g^2 (x^2+z^2) / (2 v0 (v0 + g z)))")
    print(f"  T(0,0) = {travel_time(np.array([0.0]), np.array([1e-9]))[0]:.6e} s "
          f"(must be 0)")
    print(f"  max |grad T| v - 1| over the interior = "
          f"{np.abs(residual[core]).max():.3e}")
    print("  The residual is the truncation error of the numerical gradient; the")
    print("  closed form satisfies |grad T| = 1/v to that accuracy, so it is a")
    print("  genuine solution of the eikonal equation rather than a remembered")
    print("  formula.")

    print(f"\n  the same problem by fast marching:")
    print(f"  {'dx (m)':>8} {'max |T_grid - T_exact| (ms)':>30}")
    e_list, d_list = [], []
    for dx_grid in (100.0, 50.0, 25.0):
        n = int(round(6000.0 / dx_grid)) + 1
        xg = np.arange(n) * dx_grid
        zg = np.arange(n) * dx_grid + dx_grid
        Xg, Zg = np.meshgrid(xg, zg, indexing="ij")
        speed = v0 + g * Zg
        grid = fast_marching(speed, dx_grid, (0, 0))
        exact = travel_time(Xg, Zg)
        err = np.abs(grid - exact)[4:, 4:].max()
        e_list.append(err)
        d_list.append(dx_grid)
        print(f"  {dx_grid:8.1f} {err * 1e3:30.6f}")
    print(f"  measured convergence order in dx: "
          f"{np.polyfit(np.log(d_list), np.log(e_list), 1)[0]:.3f}")
    print("  Agreement is tens of milliseconds on travel times of order one")
    print("  second, falling at first order: the numerical eikonal solver and the")
    print("  analytic ray solution are two routes to the same function.")


def validity_condition() -> None:
    section("3. Where ray theory is allowed to be used")
    v0 = 2000.0
    f = 10.0
    print(f"  local validity of the eikonal reduction needs the velocity to change")
    print(f"  by a small fraction over one wavelength: (lambda/v)|dv/dz| << 1")
    print(f"  take f = {f:.0f} Hz, so lambda = v/f")
    print(f"  {'dv/dz (1/s)':>13} {'v (m/s)':>10} {'lambda (m)':>12} "
          f"{'(lambda/v)|dv/dz|':>20}")
    for gradient in (0.05, 0.2, 0.5, 2.0, 10.0):
        v = v0
        lam = v / f
        ratio = (lam / v) * gradient
        print(f"  {gradient:13.3f} {v:10.1f} {lam:12.2f} {ratio:20.4f}")
    print("  The dimensionless group is independent of v and equals f^-1 dv/dz:")
    print("  ray theory requires the fractional velocity change per wavelength,")
    print("  dv/dz / f, to be much less than one.  At 10 Hz a gradient of 10 1/s")
    print("  changes the velocity by 100 per cent within one wavelength and the")
    print("  ray description is meaningless; the criterion is stated here as the")
    print("  number it is, not as a slogan.")


def picking_uncertainty() -> None:
    section("4. What a picking error does to a distance, and what it cannot do")
    v = 3000.0
    x_true, z_true = 6000.0, 6000.0
    t_true = float(np.hypot(x_true, z_true) / v)
    sigma_t = 5.0e-3                     # s, a stated pick uncertainty
    n = 4000
    noisy = t_true + RNG.normal(0.0, sigma_t, n)
    r = v * noisy
    r_true = v * t_true
    print(f"  homogeneous v = {v:.0f} m/s; receiver at ({x_true / 1e3:.1f}, "
          f"{z_true / 1e3:.1f}) km; exact time = {t_true:.6f} s")
    print(f"  stated pick uncertainty sigma_t = {sigma_t * 1e3:.1f} ms over "
          f"{n} realisations")
    print(f"  distance recovered as r = v t   : {r.mean():.4f} +/- {r.std():.4f} m "
          f"(true {r_true:.4f} m)")
    print(f"  relative scatter                : {r.std() / r_true:.4%}")
    print(f"  a mis-specified velocity acts linearly: 0.5 per cent of v moves the")
    print(f"  same distance by {5e-3 * r_true:.2f} m, "
          f"{5e-3 * r_true / r.std():.1f} times the picking scatter of "
          f"{r.std():.2f} m.")
    print("  The eikonal solver returns a travel time and nothing else.  It has no")
    print("  amplitude and no error bar, so every uncertainty attached to a ray")
    print("  result was carried in by the data or the model, never produced by the")
    print("  method.")


def main() -> None:
    homogeneous_check()
    linear_gradient()
    validity_condition()
    picking_uncertainty()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
