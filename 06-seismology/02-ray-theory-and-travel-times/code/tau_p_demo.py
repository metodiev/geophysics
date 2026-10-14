#!/usr/bin/env python3
"""The tau-p transform: intercept time, Benndorf's relation, and sphericity.

Checks:
1. For a linear-gradient layer, X(p) and T(p) are computed by quadrature, and
   tau(p) = T - p X is formed.  Benndorf's relation d(tau)/dp = -X is then
   verified numerically.
2. ObsPy's TauP travel times are differentiated to verify p = dT/dDelta.
3. The spherical ray parameter identity p = r sin i / v is verified directly on
   TauP ray paths, by measuring the ray's local angle and the local velocity at
   every point of the path.

Run:
    .venv/bin/python 06-seismology/02-ray-theory-and-travel-times/code/tau_p_demo.py
"""

from __future__ import annotations

import numpy as np
from obspy.taup import TauPyModel

RNG = np.random.default_rng(20261014)


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ---- SYNTHETIC linear-gradient layer ---------------------------------------
V0 = 3000.0          # m/s at the surface
G = 0.40             # 1/s
H = 20.0e3           # m, base of the gradient layer
V_H = V0 + G * H
DV = 2.0             # m/s, quadrature step in velocity (~5 m in depth)


def branch(p: float, n: int = 2001):
    """X(p) and T(p) for a ray turning inside the gradient layer.

    The quadrature is carried out in the ray angle theta, which removes the
    integrable 1/sqrt(z_turn - z) singularity at the turning depth analytically:
    with v = sin(theta)/p and dz = cos(theta) d(theta)/(G p), the two integrals

        X = 2 int p/eta dz,   T = 2 int 1/(v^2 eta) dz

    become  X = (2/(G p)) int sin(theta) d(theta)  and
            T = (2/G) int d(theta)/sin(theta),

    both smooth on [theta_0, pi/2].  Integrating in z on a uniform grid instead
    puts a node arbitrarily close to the singularity, where the last trapezoid
    can dominate the whole sum; that failure mode is avoided here by
    construction rather than by a tolerance.
    """
    z_turn = (1.0 / p - V0) / G
    if not (0.0 < z_turn < H):
        return None
    theta0 = np.arcsin(p * V0)
    theta = np.linspace(theta0, 0.5 * np.pi, n)
    x = 2.0 * np.trapezoid(np.sin(theta), theta) / (G * p)
    t = 2.0 * np.trapezoid(1.0 / np.sin(theta), theta) / G
    return x, t


def benndorf() -> None:
    section("1. X(p), T(p) and Benndorf's relation d(tau)/dp = -X")
    print(f"  v(z) = {V0:.0f} + {G:.2f} z m/s for 0 < z < {H / 1e3:.0f} km, "
          f"v at the base = {V_H:.0f} m/s")
    p_all = np.linspace(1.0 / (V_H * 1.02), 1.0 / (V0 * 1.05), 60)
    ps, xs, ts = [], [], []
    for p in p_all:
        out = branch(p)
        if out is None:
            continue
        ps.append(p)
        xs.append(out[0])
        ts.append(out[1])
    ps = np.array(ps)
    xs = np.array(xs)
    ts = np.array(ts)
    taus = ts - ps * xs
    dtau = np.gradient(taus, ps)
    interior = slice(2, -2)
    rel = np.abs(dtau[interior] + xs[interior]) / xs[interior]
    print(f"  p range {ps[0]:.6e} to {ps[-1]:.6e} s/m, "
          f"{len(xs)} ray parameters")
    print(f"  {'p (s/m)':>13} {'X (km)':>10} {'T (s)':>10} {'tau (s)':>10} "
          f"{'-d(tau)/dp (km)':>17} {'X (km)':>10}")
    for k in range(0, len(xs), 12):
        print(f"  {ps[k]:13.6e} {xs[k] / 1e3:10.4f} {ts[k]:10.4f} "
              f"{taus[k]:10.4f} {-dtau[k] / 1e3:17.4f} {xs[k] / 1e3:10.4f}")
    print(f"  worst relative difference between -d(tau)/dp and X over the "
          f"interior: {rel.max():.3e}")
    print("  The two columns agree to finite-difference accuracy, so the")
    print("  intercept function is the Legendre transform of the travel-time")
    print("  curve and either one determines the other.")

    i = len(xs) // 2
    print(f"\n  dT/dX at the middle of the branch = "
          f"{(ts[i + 1] - ts[i - 1]) / (xs[i + 1] - xs[i - 1]):.9e} s/m")
    print(f"  the ray parameter there                = {ps[i]:.9e} s/m")
    print("  Benndorf's relation is the statement that these are equal.")


def spherical_identity() -> None:
    section("2. p = dT/dDelta measured from TauP")
    model = TauPyModel(model="iasp91")
    print(f"  {'Delta (deg)':>12} {'T (s)':>10} {'dT/dDelta (s/deg)':>19} "
          f"{'TauP p (s/deg)':>16} {'relative diff':>14}")
    h = 0.01
    for dist in (20.0, 40.0, 60.0, 80.0, 95.0):
        a = model.get_travel_times(10.0, dist - h, phase_list=["P"])[0]
        b = model.get_travel_times(10.0, dist + h, phase_list=["P"])[0]
        mid = model.get_travel_times(10.0, dist, phase_list=["P"])[0]
        numeric = (b.time - a.time) / (2.0 * h)
        print(f"  {dist:12.2f} {mid.time:10.4f} {numeric:19.8f} "
              f"{mid.ray_param_sec_degree:16.8f} "
              f"{abs(numeric - mid.ray_param_sec_degree) / mid.ray_param_sec_degree:14.3e}")
    print("  The numerical derivative of the travel-time curve and the ray")
    print("  parameter TauP carries with each arrival agree to a few parts in")
    print("  1e-5, the truncation error of a 0.01 degree central difference.")

    section("3. the spherical identity p = r sin i / v, checked along a ray path")
    arrival = model.get_ray_paths(10.0, 60.0, phase_list=["P"])[0]
    path = arrival.path
    depth = np.array(path["depth"], dtype=float)
    dist_rad = np.array(path["dist"], dtype=float)
    radius = model.model.radius_of_planet - depth
    vmod = model.model.s_mod.v_mod
    d_grid = np.arange(1.0, model.model.radius_of_planet - 1.0, 1.0)
    vp_grid = np.array([float(np.asarray(vmod.evaluate_above(d, "p")).ravel()[0])
                        for d in d_grid])
    vp = np.interp(np.clip(depth, 1.0, d_grid[-1]), d_grid, vp_grid)

    # local ray angle from the path geometry, in the (r, r*Delta) plane
    dr = np.gradient(radius, dist_rad)
    dx = radius * np.ones_like(dist_rad)                  # d(r Delta)/d Delta
    angle = np.arctan2(np.abs(dx), np.abs(dr))            # from the vertical
    p_path = radius * np.sin(angle) / vp
    core = slice(3, -3)
    p_target = arrival.ray_param
    rel = np.abs(p_path[core] - p_target) / p_target
    print(f"  P at 60 deg, source depth 10 km: {len(depth)} path points, "
          f"shallowest point {depth.min():.2f} km, "
          f"turning depth {depth.max():.2f} km")
    print(f"  TauP ray parameter for this arrival         : {p_target:.6e} s/rad "
          f"({arrival.ray_param_sec_degree:.8f} s/deg)")
    print(f"  median of r sin i / v along the path        : "
          f"{np.median(p_path[core]):.6e} s/rad")
    print(f"  mean   |r sin i / v - p| / p                : {rel.mean():.3e}")
    print(f"  median |r sin i / v - p| / p                : "
          f"{np.median(rel):.3e}")
    print(f"  95th percentile of |r sin i / v - p| / p    : "
          f"{np.percentile(rel, 95):.3e}")
    print(f"  worst  |r sin i / v - p| / p                : {rel.max():.3e}")
    print("  The angle is read off the path geometry by differencing neighbouring")
    print("  path points, so the residual is the finite-difference error of that")
    print("  reading, and it is worst where the ray is nearly horizontal and the")
    print("  radial difference between adjacent samples goes to zero.  Over 95 per")
    print("  cent of the path the identity holds to better than the printed")
    print("  percentile, which is the sense in which p is a ray invariant.")

    print(f"\n  ray parameter converted between units: p = {p_target:.4f} s/rad")
    print(f"  = {p_target * np.pi / 180.0:.8f} s/deg, and TauP reports "
          f"{arrival.ray_param_sec_degree:.8f} s/deg.")


def noise_amplification() -> None:
    section("4. Differentiating tau: how a picking error becomes a slowness error")
    p_grid = np.linspace(1.50e-4, 3.00e-4, 121)
    xs, ts = [], []
    for p in p_grid:
        out = branch(p)
        xs.append(out[0])
        ts.append(out[1])
    xs = np.array(xs)
    ts = np.array(ts)
    sigma_t = 0.010                           # s, a stated pick uncertainty
    core = slice(3, -3)

    clean = -np.gradient(ts - p_grid * xs, p_grid)
    n = 300
    errs = np.empty((n, p_grid.size))
    for k in range(n):
        tau_noisy = (ts + RNG.normal(0.0, sigma_t, ts.size)) - p_grid * xs
        errs[k] = np.abs(-np.gradient(tau_noisy, p_grid) - xs)

    dp = p_grid[1] - p_grid[0]
    predicted = sigma_t / (np.sqrt(2.0) * dp)
    clean_worst = np.abs(clean - xs)[core].max()
    noisy_worst = errs.mean(axis=0)[core].max()
    print(f"  branch sampled at {p_grid.size} ray parameters from "
          f"{p_grid[0]:.3e} to {p_grid[-1]:.3e} s/m, spacing {dp:.3e} s/m")
    print(f"  X ranges from {xs[core].min() / 1e3:.2f} to "
          f"{xs[core].max() / 1e3:.2f} km over the sampled branch")
    print(f"  the same difference on noise-free data returns X to "
          f"{clean_worst:.3f} m worst case (truncation only)")
    print(f"  with sigma_T = {sigma_t * 1e3:.1f} ms, over {n} realisations:")
    print(f"    mean |X_recovered - X| = {errs.mean(axis=0)[core].mean():.3f} m, "
          f"worst {noisy_worst:.3f} m")
    print(f"    relative to the smallest X on the branch, that worst error is "
          f"{noisy_worst / xs[core].min():.3%}")
    print(f"    predicted by scaling the pick noise through the central")
    print(f"    difference, sigma_T / (sqrt(2) dp) = {predicted:.3f} m")
    print(f"  the noise term exceeds the truncation term by a factor "
          f"{noisy_worst / clean_worst:.1f}")
    print("  The intercept function is smooth and its derivative is well defined;")
    print("  the *data* are not, and a difference of two neighbouring tau values")
    print("  divides the pick noise by the p spacing.  Refining the p grid to gain")
    print("  resolution therefore buys slowness noise in inverse proportion -- the")
    print("  same trade a water level makes in deconvolution, in a different")
    print("  variable.  What the transform buys is not free resolution; it is a")
    print("  change of variable in which a curved travel-time branch becomes a")
    print("  straight line whose slope can be estimated by regression.")


def main() -> None:
    benndorf()
    spherical_identity()
    noise_amplification()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
