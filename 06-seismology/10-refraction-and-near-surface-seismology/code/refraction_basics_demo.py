"""Refraction seismology: Snell, critical refraction, head waves, and the blind zone.

Run:  .venv/bin/python refraction_basics_demo.py
Requires: numpy, scipy.

Companion to lesson 06-10-01.

Five computations in the order the lesson derives them:

1. Snell's law and the critical angle for two stated velocities.
2. The head-wave travel-time equation, the intercept time and the crossover
   distance -- the crossover obtained three ways, two algebraic and one a
   numerical root find of the crossing of two curves, so that they must agree.
3. Verification of the head-wave equation against two independent computations:
   (a) numerical minimisation of the Fermat travel-time functional over the two
       ray knee points (the closed form is never used, the ray is found);
   (b) a discretised eikonal (shortest-path, scipy.sparse.csgraph) solver on a
       2-D velocity grid whose edge weights are exact straight-segment times
       through the layered model.  Its error is angular quantisation, so the
       refinement parameter is the *number of directions*, not the grid.
4. The blind zone, the honesty point of the module: a three-layer model with a
   250 m/s layer between two faster layers, whose exact first-arrival times are
   reproduced by a two-layer model that contains no low-velocity layer at all.
   The fit residual is measured, and so is the depth error of the inversion.
5. The two-layer inversion applied to its own travel-time curve (exact round
   trip), which sets the baseline that lesson 02 perturbs with picking error.

Every model parameter is SYNTHETIC and printed.  No field survey, no site and no
catalogue are referred to.
"""

from __future__ import annotations

import numpy as np
from scipy.optimize import minimize
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import dijkstra

# --------------------------------------------------------------------------
# SYNTHETIC two-layer model (values chosen for arithmetic clarity)
# --------------------------------------------------------------------------
V1 = 500.0     # m/s  weathered / unsaturated near-surface layer
V2 = 1800.0    # m/s  saturated or consolidated refractor
H = 10.0       # m    depth to the top of layer 2 (flat surface, flat interface)


def banner(title: str) -> None:
    print()
    print("=" * 74)
    print(title)
    print("=" * 74)


def layered_velocity(z, interfaces, velocities):
    """Right-continuous stack: v = velocities[k] at or below interface k."""
    z = np.asarray(z, dtype=float)
    v = np.full(z.shape, velocities[0], dtype=float)
    for depth, vk in zip(interfaces, velocities[1:]):
        v = np.where(z >= depth, vk, v)
    return v


# --------------------------------------------------------------------------
# 1. Snell's law and the critical angle
# --------------------------------------------------------------------------

def critical_angle(v1: float, v2: float) -> float:
    """Critical angle in radians for incidence from v1 into the faster v2."""
    return float(np.arcsin(v1 / v2))


def part1() -> None:
    banner("1. Snell's law and critical refraction")
    ic = critical_angle(V1, V2)
    print(f"  v1 (upper layer)            = {V1:.1f} m/s")
    print(f"  v2 (lower layer)            = {V2:.1f} m/s")
    print(f"  sin(i_c) = v1/v2            = {V1 / V2:.6f}   (dimensionless)")
    print(f"  i_c                         = {np.degrees(ic):.4f} deg"
          f" = {ic:.6f} rad")
    print(f"  cos(i_c)                    = {np.cos(ic):.6f}")
    print(f"  tan(i_c)                    = {np.tan(ic):.6f}")
    p = np.sin(ic) / V1
    print(f"  ray parameter p=sin(i_c)/v1 = {p:.9f} s/m"
          f"  (= 1/v2 = {1.0 / V2:.9f} s/m)")
    print("  -> the critically refracted ray has p exactly 1/v2: the slowest")
    print("     horizontal slowness the lower layer can carry.")


# --------------------------------------------------------------------------
# 2. Head-wave travel time, intercept time, crossover distance
# --------------------------------------------------------------------------

def head_wave_time(x, v1: float, v2: float, h: float):
    """t = x/v2 + 2h sqrt(v2^2-v1^2)/(v1 v2)."""
    x = np.asarray(x, dtype=float)
    return x / v2 + 2.0 * h * np.sqrt(v2 ** 2 - v1 ** 2) / (v1 * v2)


def intercept_time(v1: float, v2: float, h: float) -> float:
    """t_i = 2h sqrt(v2^2-v1^2)/(v1 v2) = 2h cos(i_c)/v1."""
    return 2.0 * h * np.sqrt(v2 ** 2 - v1 ** 2) / (v1 * v2)


def crossover_closed(v1: float, v2: float, h: float) -> float:
    """x_c = 2h sqrt((v2+v1)/(v2-v1))."""
    return 2.0 * h * np.sqrt((v2 + v1) / (v2 - v1))


def first_arrival(x, v1: float, v2: float, h: float):
    """min(direct, refracted) -- the observed first-arrival curve."""
    x = np.asarray(x, dtype=float)
    return np.minimum(x / v1, head_wave_time(x, v1, v2, h))


def part2() -> None:
    banner("2. Head wave, intercept time and crossover distance")
    ti = intercept_time(V1, V2, H)
    xc = crossover_closed(V1, V2, H)
    print(f"  intercept time t_i = 2h cos(i_c)/v1          = {ti * 1e3:.6f} ms")
    print(f"                     = 2h sqrt(v2^2-v1^2)/(v1 v2) = {ti * 1e3:.6f} ms")
    print(f"  crossover distance x_c (closed form)         = {xc:.6f} m")
    xc_root = ti / (1.0 / V1 - 1.0 / V2)
    print(f"  crossover from x(1/v1-1/v2) = t_i            = {xc_root:.6f} m")
    print(f"  two algebraic routes agree to "
          f"{abs(xc - xc_root) / xc:.2e} (relative)")

    xg = np.linspace(0.0, 60.0, 600001)
    diff = head_wave_time(xg, V1, V2, H) - xg / V1
    change = np.nonzero(np.diff(np.sign(diff)))[0]
    xc_num = float(xg[change[0]])
    print("  crossover from a sign change of t_head-t_direct on a 0.1 mm grid"
          f" = {xc_num:.6f} m")
    print(f"  closed form vs grid search: relative difference "
          f"{abs(xc - xc_num) / xc:.2e}")

    print()
    print("  travel-time curve of the SYNTHETIC two-layer model:")
    print("      x (m)  t_direct (ms)  t_head (ms)  first arrival")
    for x in (5.0, 10.0, 20.0, 26.6, 40.0, 60.0, 100.0, 150.0):
        td = x / V1 * 1e3
        th = float(head_wave_time(x, V1, V2, H)) * 1e3
        print(f"    {x:6.1f}  {td:12.4f}  {th:11.4f}  "
              f"{'direct' if td <= th else 'head'}")


# --------------------------------------------------------------------------
# 3a. Verification by numerical Fermat minimisation (ray tracing)
# --------------------------------------------------------------------------

def fermat_two_layer(p, x, v1: float, v2: float, h: float) -> float:
    """Travel time along S(0,0) -> P1(p1,h) -> P2(p2,h) -> R(x,0)."""
    p1, p2 = p
    return float(np.hypot(p1, h) / v1 + (p2 - p1) / v2
                 + np.hypot(x - p2, h) / v1)


def fermat_first_arrival(x, v1: float, v2: float, h: float) -> float:
    """First arrival from ray tracing: min(direct, refracted), the refracted
    branch found by numerical minimisation of the Fermat functional."""
    direct = x / v1
    best = np.inf
    for frac in (0.1, 0.3, 0.5, 0.7, 0.9):
        res = minimize(
            fermat_two_layer, np.array([frac * x, frac * x]),
            args=(x, v1, v2, h), method="L-BFGS-B",
            bounds=[(0.0, x), (0.0, x)],
            options={"ftol": 1e-15, "gtol": 1e-12, "maxiter": 5000},
        )
        if res.fun < best:
            best = float(res.fun)
    return min(direct, best)


def part3a() -> None:
    banner("3a. Verification: numerical Fermat minimisation (ray tracing)")
    worst = 0.0
    print("      x (m)  t_head closed (ms)  t_ray traced (ms)  rel. diff")
    for x in (30.0, 50.0, 80.0, 120.0, 160.0):
        closed = float(head_wave_time(x, V1, V2, H))
        traced = fermat_first_arrival(x, V1, V2, H)
        rel = abs(closed - traced) / closed
        worst = max(worst, rel)
        print(f"    {x:6.1f}  {closed * 1e3:17.9f}  {traced * 1e3:17.9f}"
              f"  {rel:.3e}")
    print(f"  worst relative difference over 5 offsets = {worst:.3e}")
    print("  -> the closed form and the numerically minimised ray agree to")
    print("     about 1e-14 in relative terms.  That residual is floating point")
    print("     stopping tolerance, not a physical discrepancy, so the check")
    print("     validates the algebra.  It does not test the choice of ray")
    print("     family, which is the same in both computations; the solver in")
    print("     section 3b is the check that does not assume it.")


# --------------------------------------------------------------------------
# 3b. Verification by a discretised eikonal solver
# --------------------------------------------------------------------------

def _directions(max_step: int):
    """Primitive integer directions (a,b), |a|,|b| <= max_step, one per
    undirected direction."""
    dirs = []
    for a in range(0, max_step + 1):
        for b in range(-max_step, max_step + 1):
            if a == 0 and b <= 0:
                continue
            if abs(a) > max_step or abs(b) > max_step:
                continue
            if np.gcd(abs(a), abs(b)) != 1:
                continue
            dirs.append((a, b))
    return dirs


def edge_times(xa, za, xb, zb, interfaces, velocities):
    """Exact straight-segment travel time through a stack of horizontal layers.

    Each segment is split at every interface it crosses and each sub-segment is
    timed with the velocity at its midpoint, so the only error is that the
    shortest path is built from a finite set of directions.
    """
    xa = np.asarray(xa, dtype=float).ravel()
    za = np.asarray(za, dtype=float).ravel()
    xb = np.asarray(xb, dtype=float).ravel()
    zb = np.asarray(zb, dtype=float).ravel()
    dz = zb - za
    k = 2 + len(interfaces)
    t = np.ones((xa.size, k))
    t[:, 0] = 0.0
    for m, depth in enumerate(interfaces):
        denom = np.where(dz == 0.0, 1.0, dz)
        tk = (depth - za) / denom
        t[:, 1 + m] = np.where((tk > 0.0) & (tk < 1.0), tk, 1.0)
    t = np.sort(t, axis=1)
    total = np.zeros(xa.size)
    for m in range(k - 1):
        t0, t1 = t[:, m], t[:, m + 1]
        frac = t1 - t0
        zm = za + 0.5 * (t0 + t1) * dz
        seg = np.hypot(frac * (xb - xa), frac * dz)
        total += seg / layered_velocity(zm, interfaces, velocities)
    return total


def eikonal_times(dx: float, x_max: float, z_max: float, interfaces,
                  velocities, source_x: float = 0.0, max_step: int = 3):
    """First-arrival times on a grid from a surface source (shortest path).

    The solver is told only the velocity as a function of depth; it is never
    told a travel-time equation, so it is an independent check on the closed
    form.
    """
    nx = int(round(x_max / dx)) + 1
    nz = int(round(z_max / dx)) + 1
    n = nx * nz
    rows, cols, data = [], [], []
    for a, b in _directions(max_step):
        jj = np.arange(max(0, -b), nz - max(0, b))
        ii = np.arange(0, nx - a)
        if ii.size == 0 or jj.size == 0:
            continue
        i0, j0 = np.meshgrid(ii, jj, indexing="ij")
        i1, j1 = i0 + a, j0 + b
        tt = edge_times(i0 * dx, j0 * dx, i1 * dx, j1 * dx,
                        interfaces, velocities)
        rows.append((i0 * nz + j0).ravel())
        cols.append((i1 * nz + j1).ravel())
        data.append(tt)
    graph = coo_matrix(
        (np.concatenate(data), (np.concatenate(rows), np.concatenate(cols))),
        shape=(n, n),
    ).tocsr()
    src = int(round(source_x / dx)) * nz
    dist = dijkstra(graph, directed=False, indices=src, min_only=True)
    return np.asarray(dist).reshape(nx, nz)


def part3b() -> None:
    banner("3b. Verification: discretised eikonal (shortest-path) solver")
    offsets = np.array([10.0, 20.0, 40.0, 60.0, 80.0, 100.0])
    exact = first_arrival(offsets, V1, V2, H)
    dx = 0.5
    print(f"  grid spacing dx = {dx:.2f} m; domain 120 m x 30 m; the only")
    print("  refinement parameter is the number of ray directions.")
    print()
    print("  directions  max |dt| (ms)  max relative diff  RMS (ms)")
    for max_step in (2, 3, 4, 6, 7, 8):
        ndir = 2 * len(_directions(max_step))
        tt = eikonal_times(dx, 120.0, 30.0, [H], [V1, V2], max_step=max_step)
        num = np.array([tt[int(round(x / dx)), 0] for x in offsets])
        d = num - exact
        print(f"  {ndir:10d}  {np.abs(d).max() * 1e3:13.4f}"
              f"  {np.abs(d / exact).max():17.3e}  "
              f"{np.sqrt(np.mean(d ** 2)) * 1e3:7.4f}")
    print()
    print("  -> the residual is angular quantisation: the path may use only the")
    print("     available directions, so a ray at 73.87 deg to the horizontal is")
    print("     built from 71.57 deg and 75.96 deg steps.  The error falls as the")
    print("     direction set is enriched -- by a factor of about 3 per step here")
    print("     -- and not as dx is reduced, which is why a shortest-path solver")
    print("     must be refined in directions.  Note the plateau at 48-96")
    print("     directions: the same two neighbouring directions bound the ray")
    print("     until (2,7) becomes available at 144 directions.")


# --------------------------------------------------------------------------
# 4. The blind zone: a low-velocity layer that no first arrival sees
# --------------------------------------------------------------------------

H1 = 8.0        # m   thickness of the V1 layer
H2 = 8.0        # m   thickness of the low-velocity layer
V_LVL = 250.0   # m/s deliberately slower than V1
V3 = 1800.0     # m/s basal refractor


def stack_intercept_time(velocities, thicknesses, target_v: float) -> float:
    """Intercept time of the head wave carried by the layer of speed target_v.

    t_i = 2 sum_k h_k cos(theta_k)/v_k  with  sin(theta_k) = v_k/target_v.
    """
    total = 0.0
    for vk, hk in zip(velocities, thicknesses):
        if target_v <= vk:
            continue
        theta = np.arcsin(vk / target_v)
        total += 2.0 * hk * np.cos(theta) / vk
    return float(total)


def stack_head_wave(x, velocities, thicknesses, target_v: float):
    x = np.asarray(x, dtype=float)
    return x / target_v + stack_intercept_time(velocities, thicknesses, target_v)


def two_layer_invert(v1: float, v2: float, ti: float) -> float:
    """Depth from an intercept time under the assumption of one layer of v1."""
    return ti * v1 * v2 / (2.0 * np.sqrt(v2 ** 2 - v1 ** 2))


def part4() -> None:
    banner("4. The blind zone: a 250 m/s layer inside a 500 m/s layer")
    vels = [V1, V_LVL]
    thicks = [H1, H2]
    print("  SYNTHETIC three-layer model (every parameter stated):")
    print(f"    layer 1: v = {V1:6.0f} m/s, thickness {H1:4.1f} m")
    print(f"    layer 2: v = {V_LVL:6.0f} m/s, thickness {H2:4.1f} m   <- low"
          " velocity layer")
    print(f"    layer 3: v = {V3:6.0f} m/s, half-space")

    ti_true = stack_intercept_time(vels, thicks, V3)
    theta1 = np.arcsin(V1 / V3)
    theta2 = np.arcsin(V_LVL / V3)
    print()
    print("  exact first-arrival time from ray theory (delay-time sum):")
    print("    t_head(x) = x/v3 + 2[h1 cos(t1)/v1 + h2 cos(t2)/v2]")
    print(f"    t1 = arcsin(v1/v3) = {np.degrees(theta1):.4f} deg,"
          f"  t2 = arcsin(v2/v3) = {np.degrees(theta2):.4f} deg")
    print("    delay of layer 1 = h1 cos(t1)/v1 = "
          f"{H1 * np.cos(theta1) / V1 * 1e3:.6f} ms")
    print("    delay of layer 2 = h2 cos(t2)/v2 = "
          f"{H2 * np.cos(theta2) / V_LVL * 1e3:.6f} ms")
    print(f"    intercept time t_i = {ti_true * 1e3:.6f} ms")
    print(f"    far-branch slope = 1/v3 = {1e3 / V3:.6f} ms/m"
          f" -> apparent velocity {V3:.1f} m/s")
    print(f"    near-branch velocity = v1 = {V1:.1f} m/s")
    xc_direct = ti_true / (1.0 / V1 - 1.0 / V3)
    print(f"    crossover of the two branches = {xc_direct:.4f} m")

    h_inv = two_layer_invert(V1, V3, ti_true)
    print()
    print("  two-layer inversion of that travel-time curve:")
    print(f"    h = t_i v1 v3 / (2 sqrt(v3^2-v1^2)) = {h_inv:.6f} m")
    print(f"    inferred model: {V1:.0f} m/s over {V3:.0f} m/s"
          f" at {h_inv:.2f} m; nothing in between")
    print(f"    true depth to the top of the 1800 m/s layer = {H1 + H2:.1f} m")
    print(f"    depth error = {h_inv - (H1 + H2):+.3f} m"
          f" ({(h_inv - (H1 + H2)) / (H1 + H2) * 100:+.1f} %)")

    x = np.arange(20.0, 200.001, 2.0)
    t_true = np.minimum(x / V1, stack_head_wave(x, vels, thicks, V3))
    t_model = first_arrival(x, V1, V3, h_inv)
    resid = t_model - t_true
    print()
    print("  fit of the two-layer model to the true first arrivals over")
    print(f"  offsets {x[0]:.0f}-{x[-1]:.0f} m ({x.size} traces):")
    print(f"    max |residual| = {np.abs(resid).max():.3e} s"
          f" = {np.abs(resid).max() * 1e9:.3e} ns")
    print(f"    RMS |residual| = {np.sqrt(np.mean(resid ** 2)):.3e} s")
    print("    relative to t at the far end: "
          f"{np.abs(resid).max() / t_true[-1]:.3e}")
    print("    -> the observed curve is a two-layer curve to numerical")
    print("       precision.  No residual of any size can reveal the 250 m/s")
    print("       layer, because no first-arrival ray spends time in it.")

    dx = 0.25
    tt = eikonal_times(dx, 110.0, 40.0, [H1, H1 + H2], [V1, V_LVL, V3],
                       max_step=7)
    pick = np.array([20.0, 40.0, 60.0, 80.0, 100.0])
    num = np.array([tt[int(round(p / dx)), 0] for p in pick])
    exact = np.minimum(pick / V1, stack_head_wave(pick, vels, thicks, V3))
    print()
    print("  independent check with the eikonal solver, which is given the")
    print("  velocity stack but not the travel-time equation (dx = 0.25 m,")
    print("  144 directions):")
    print("      x (m)  eikonal (ms)  ray theory (ms)  difference (ms)   rel.")
    for p, n_, e in zip(pick, num, exact):
        print(f"    {p:6.1f}  {n_ * 1e3:12.5f}  {e * 1e3:15.5f}"
              f"  {(n_ - e) * 1e3:+14.5f}  {(n_ - e) / e:+.2e}")
    print(f"    max |difference| = {np.abs(num - exact).max() * 1e3:.5f} ms")

    spread = 100.0
    ti1_half = 0.5 * stack_intercept_time([V1], [H1], V3)
    budget = spread * (V3 - V1) / (2.0 * V1 * V3) - ti1_half
    h2_max = budget * V_LVL / np.cos(theta2)
    print()
    print(f"  with a {spread:.0f} m spread the basal refractor is detectable")
    print("  (its crossover lies inside the spread) only while the blind layer")
    print(f"  is thinner than h2_max = {h2_max:.3f} m.  Thicker than that, the")
    print("  1800 m/s layer also disappears and the record shows one layer at")
    print(f"  {V1:.0f} m/s.  Either way the 250 m/s layer is never inverted.")


# --------------------------------------------------------------------------
# 5. Two-layer inversion round trip
# --------------------------------------------------------------------------

def part5() -> None:
    banner("5. Two-layer inversion round trip (no low-velocity layer)")
    x = np.array([5.0, 10.0, 15.0, 20.0, 26.0, 40.0, 60.0, 90.0, 120.0])
    xc = crossover_closed(V1, V2, H)
    near = x < xc
    t = first_arrival(x, V1, V2, H)
    slope_near = float(np.polyfit(x[near], t[near], 1)[0])
    slope_far, icept_far = np.polyfit(x[~near], t[~near], 1)
    v1_fit = 1.0 / slope_near
    v2_fit = 1.0 / float(slope_far)
    h_fit = two_layer_invert(v1_fit, v2_fit, float(icept_far))
    print(f"  crossover used to split the branches: {xc:.4f} m")
    print(f"  true v1 = {V1:.1f} m/s   fitted v1 = {v1_fit:.6f} m/s")
    print(f"  true v2 = {V2:.1f} m/s   fitted v2 = {v2_fit:.6f} m/s")
    print(f"  true h  = {H:.4f} m      fitted h  = {h_fit:.6f} m")
    print(f"  relative errors: v1 {abs(v1_fit - V1) / V1:.2e},"
          f" v2 {abs(v2_fit - V2) / V2:.2e},"
          f" h {abs(h_fit - H) / H:.2e}")
    print("  -> with exact travel times the round trip closes to floating")
    print("     point.  All of the difficulty in lesson 02 comes from the")
    print("     picking error that this experiment has set to zero.")


if __name__ == "__main__":
    print("06-10-01 refraction basics -- SYNTHETIC models, no field data")
    part1()
    part2()
    part3a()
    part3b()
    part4()
    part5()
    print()
    print("done")
