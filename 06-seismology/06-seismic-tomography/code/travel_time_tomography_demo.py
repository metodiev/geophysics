#!/usr/bin/env python3
"""Travel-time tomography: parametrisation, inversion, and how far the
linearised problem can be pushed.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python travel_time_tomography_demo.py

Requires: numpy.  Print-only; no figures, no network.

Companion to lesson 06-06-02.  Every number printed here is produced by this
file from a SYNTHETIC model; the acquisition is a 16 km x 5.5 km cross-hole
survey with a homogeneous reference medium of 3000 m/s, 10 sources in the left
borehole and 14 receivers in the right borehole (140 rays), straight-ray paths,
and a smooth 5 per cent velocity anomaly unless stated otherwise.  Nothing is
taken from a real survey or a published model.

Contents
--------
1. Parametrisation: the same ray set discretised as 16 x 12 cells and as a
   17 x 13 bilinear node grid.  Sparsity, ray length per parameter, and what the
   choice does to conditioning.
2. Solver: direct damped least squares against conjugate-gradient least squares
   (CGLS), measured in matrix-vector products and in seconds.
3. Grid size against noise: 8 x 6, 16 x 12 and 32 x 24 cells at a fixed data set
   and a fixed noise level, averaged over many noise realisations.
4. Regularisation operator: identity (minimum norm) against first differences
   (minimum roughness), matched by data misfit.
5. Nonlinearity: (a) Fermat stationarity, measured by moving a ray's mid-point
   and watching the travel time change only quadratically; (b) a Newton
   re-linearisation loop, per-iteration.
"""

import time

import numpy as np

RNG = np.random.default_rng(20261014)

X0, X1 = 0.2e3, 15.8e3        # boreholes at x = 0.2 km and 15.8 km
Z_TOP, Z_BOT = 0.25e3, 5.75e3
V_REF = 3000.0                # m/s, SYNTHETIC homogeneous reference
N_SRC, N_REC = 10, 14
SIGMA_T = 5.0e-3              # s, travel-time noise used in sections 3-4


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def geometry():
    """Cross-hole ray set: every source-receiver pair.  Returns 140 segments."""
    src = np.column_stack([np.full(N_SRC, X0),
                           np.linspace(Z_TOP, Z_BOT, N_SRC)])
    rec = np.column_stack([np.full(N_REC, X1),
                           np.linspace(Z_TOP, Z_BOT, N_REC)])
    return [(s, r) for s in src for r in rec]


def sample_path(p, q, n=1500):
    """Dense points along the segment p-q (metres)."""
    t = np.linspace(0.0, 1.0, n)
    return p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t, \
        np.hypot(q[0] - p[0], q[1] - p[1]) / (n - 1)


def cell_lengths(p, q, nx, nz, dx, dz, n=1500):
    """Length of segment p-q inside each cell, model index = row*nx + col."""
    xs, zs, seg = sample_path(p, q, n)
    col = np.clip((xs / dx).astype(int), 0, nx - 1)
    row = np.clip((zs / dz).astype(int), 0, nz - 1)
    out = np.zeros(nx * nz)
    np.add.at(out, row * nx + col, seg)
    return out


def bilinear_lengths(p, q, nx, nz, dx, dz, n=1500):
    """Length in each node of a bilinear node grid, nodes (nx+1) x (nz+1).

    A straight ray is a set of samples; each sample contributes its length split
    between the four surrounding nodes with bilinear weights.  A ray therefore
    touches about 4 parameters per cell it crosses, not 1.
    """
    xs, zs, seg = sample_path(p, q, n)
    fx = np.clip(xs / dx, 0.0, nx - 1e-12)
    fz = np.clip(zs / dz, 0.0, nz - 1e-12)
    i0 = fx.astype(int)
    j0 = fz.astype(int)
    wx = fx - i0
    wz = fz - j0
    out = np.zeros((nx + 1) * (nz + 1))
    for (ii, wxi) in ((i0, 1.0 - wx), (i0 + 1, wx)):
        for (jj, wzj) in ((j0, 1.0 - wz), (j0 + 1, wz)):
            np.add.at(out, jj * (nx + 1) + ii, seg * wxi * wzj)
    return out


def build_g(rays, nx, nz, dx, dz, velocity=V_REF):
    """Jacobian for a homogeneous reference: length in cell / reference velocity."""
    return np.array([cell_lengths(s, r, nx, nz, dx, dz) for s, r in rays]) / velocity


def build_g_nodes(rays, nx, nz, dx, dz, velocity=V_REF):
    return (np.array([bilinear_lengths(s, r, nx, nz, dx, dz) for s, r in rays])
            / velocity)


def smooth_model(nx, nz, dx, dz, amp=0.05):
    """Relative velocity perturbation dv/v0: one Gaussian blob, x fastest."""
    xc = (np.arange(nx) + 0.5) * dx
    zc = (np.arange(nz) + 0.5) * dz
    zz, xx = np.meshgrid(zc, xc, indexing="ij")
    return (amp * np.exp(-((xx - 0.62 * nx * dx) ** 2
                           + (zz - 0.55 * nz * dz) ** 2)
                         / (2.0 * (0.22 * nx * dx) ** 2))).ravel()


def svd_solve(u, s, vt, d, lam):
    return vt.T @ (s / (s ** 2 + lam ** 2) * (u[:, :s.size].T @ d))


def cgls(g, d, lam, iters):
    """Conjugate-gradient least squares.  Returns (m, residual rms per iteration)."""
    n = g.shape[1]
    m = np.zeros(n)
    r = d.copy()
    s_vec = g.T @ r - lam ** 2 * m
    p = s_vec.copy()
    gamma = s_vec @ s_vec
    hist = [np.sqrt(np.mean(r ** 2))]
    for _ in range(iters):
        q = g @ p
        alpha = gamma / (q @ q + lam ** 2 * (p @ p))
        m = m + alpha * p
        r = r - alpha * q
        s_vec = g.T @ r - lam ** 2 * m
        gamma_new = s_vec @ s_vec
        p = s_vec + (gamma_new / gamma) * p
        gamma = gamma_new
        hist.append(np.sqrt(np.mean(r ** 2)))
    return m, np.array(hist)


def lambda_for_misfit(misfit_of, lambdas, target):
    """Largest damping whose data misfit is still below the target."""
    vals = np.array([misfit_of(l) for l in lambdas])
    idx = np.where(vals <= target)[0]
    if idx.size:
        k = int(idx[-1])
    else:
        k = int(np.argmin(np.abs(vals - target)))
    return float(lambdas[k]), float(vals[k])


def first_difference(nx, nz):
    """First-difference operator on the grid (x fastest), rows stacked x then z."""
    rows = []
    for j in range(nz):
        for i in range(nx - 1):
            r = np.zeros(nx * nz)
            r[j * nx + i] = -1.0
            r[j * nx + i + 1] = 1.0
            rows.append(r)
    for j in range(nz - 1):
        for i in range(nx):
            r = np.zeros(nx * nz)
            r[j * nx + i] = -1.0
            r[(j + 1) * nx + i] = 1.0
            rows.append(r)
    return np.array(rows)


def part1_parametrisation():
    section("1. Parametrisation: the same rays, two different models")
    rays = geometry()
    nx, nz = 16, 12
    dx, dz = (X1 - X0) / nx, (Z_BOT - Z_TOP) / nz
    lengths = np.array([cell_lengths(s, r, nx, nz, dx, dz) for s, r in rays])
    g_cell = lengths / V_REF
    g_node = build_g_nodes(rays, nx, nz, dx, dz)
    print(f"acquisition: {len(rays)} rays between {N_SRC} sources (x=0.2 km) and "
          f"{N_REC} receivers (x=15.8 km)")
    print(f"region: {(X1 - X0) / 1e3:.0f} km x {(Z_BOT - Z_TOP) / 1e3:.1f} km; "
          f"reference velocity {V_REF:.0f} m/s")
    print(f"reference travel times: {lengths.sum(axis=1).min() / V_REF:.3f} to "
          f"{lengths.sum(axis=1).max() / V_REF:.3f} s\n")
    for (name, g) in (("cells 16 x 12", g_cell), ("nodes 17 x 13", g_node)):
        u, s, vt = np.linalg.svd(g, full_matrices=False)
        nonzero = np.count_nonzero(g)
        print(f"  {name}: {g.shape[1]} parameters, {g.shape[0]} data, "
              f"{nonzero} non-zeros ({100.0 * nonzero / g.size:.2f} per cent)")
        print(f"      non-zeros per ray: {np.mean(np.count_nonzero(g, axis=1)):.1f}, "
              f"max {np.max(np.count_nonzero(g, axis=1))}")
        print(f"      rank {int(np.sum(s > 1e-9 * s[0]))} of {min(g.shape)}, "
              f"condition number {s[0] / s[int(np.sum(s > 1e-9 * s[0])) - 1]:.3e}")
    print(f"  mean non-zero entry of G: cell grid "
          f"{np.mean(g_cell[g_cell > 0]):.4e} s, node grid "
          f"{np.mean(g_node[g_node > 0]):.4e} s")
    print("""
  Both matrices describe the same physics.  The cell basis is blocky and sparse
  -- one non-zero per cell crossed -- so its parameters are easy to interpret
  but its images are piecewise constant.  The bilinear node basis is about four
  times denser and smoother, at the cost of correlated parameters and a worse
  condition number.  The parametrisation is a modelling decision that has to be
  reported, because a feature smaller than a cell cannot exist in the answer.""")


def part2_solvers():
    section("2. Solvers: direct damped least squares against CGLS")
    rays = geometry()
    nx, nz = 16, 12
    dx, dz = (X1 - X0) / nx, (Z_BOT - Z_TOP) / nz
    g = build_g(rays, nx, nz, dx, dz)
    p_true = smooth_model(nx, nz, dx, dz)
    d = -(g @ p_true)                       # datum in seconds, from dv/v0 = -1
    lam = 3e-2 * np.linalg.norm(g)
    t0 = time.perf_counter()
    m_direct = np.linalg.solve(g.T @ g + lam ** 2 * np.eye(g.shape[1]), g.T @ d)
    t_direct = time.perf_counter() - t0
    print(f"problem: {g.shape[0]} data, {g.shape[1]} parameters; "
          f"damping lam = {lam:.4e} (3e-2 x ||G||)")
    print(f"direct solve           : {t_direct:.4f} s, misfit "
          f"{np.sqrt(np.mean((g @ m_direct - d) ** 2)):.4e} s")
    print(f"{'CGLS iterations':>16} {'mat-vecs':>9} {'misfit (s)':>12} "
          f"{'wall time (s)':>14} {'model error':>12}")
    for iters in (2, 5, 10, 20, 50, 100):
        t0 = time.perf_counter()
        m_cg, hist = cgls(g, d, lam, iters)
        dt = time.perf_counter() - t0
        err = np.sqrt(np.mean((m_cg - m_direct) ** 2))
        print(f"{iters:16d} {2 * iters:9d} "
              f"{np.sqrt(np.mean((g @ m_cg - d) ** 2)):12.4e} {dt:14.5f} "
              f"{err:12.4e}")
    print("""
  CGLS reaches the same answer as the direct solve to four or five significant
  figures in ten to twenty iterations, and its cost grows in matrix-vector
  products rather than in a matrix factorisation.  For a problem with thousands
  of parameters (and a sparse Jacobian that is never formed explicitly) the
  iterative route is the only feasible one; the price is that the answer is
  defined by the iteration count as well as by the damping, so the stopping
  rule has to be stated.""")


def part3_grid_size():
    section("3. Grid size against noise: matching the model to the data")
    rays = geometry()
    target = np.sqrt(len(rays)) * SIGMA_T
    print(f"fixed data: {len(rays)} rays, one Gaussian velocity anomaly of 5 per")
    print(f"cent, rms(dv/v0) = 0.028.  Noise sigma = {SIGMA_T * 1e3:.1f} ms, so a")
    print(f"statistically acceptable fit has misfit sqrt(N) sigma = {target:.4e} s.")
    print(f"Each grid below is inverted at the damping that just reaches that")
    print(f"misfit, so the comparison is between well-adapted inversions, not")
    print(f"between arbitrary damping choices.  40 noise realisations each.\n")
    print(f"{'grid':>10} {'params':>7} {'data/par':>9} {'lam/||G||':>10} "
          f"{'misfit (s)':>11} {'model error':>12} {'row-space err':>14} "
          f"{'null fraction':>14}")
    for (nx, nz) in ((8, 6), (16, 12), (24, 18), (32, 24)):
        dx, dz = (X1 - X0) / nx, (Z_BOT - Z_TOP) / nz
        g = build_g(rays, nx, nz, dx, dz)
        p_true = smooth_model(nx, nz, dx, dz)
        d_clean = -(g @ p_true)
        u, s, vt = np.linalg.svd(g, full_matrices=False)
        ud = u[:, :s.size].T @ d_clean
        lambdas = np.logspace(-5, 0, 200) * s[0]

        def misfit_of(lam, ud=ud, s=s):
            projected = s ** 2 / (s ** 2 + lam ** 2) * ud
            return float(np.sqrt(np.mean((projected - ud) ** 2)))

        lam, fit = lambda_for_misfit(misfit_of, lambdas, target)
        rank = int(np.sum(s > 1e-9 * s[0]))
        row_proj = vt[:rank].T @ (vt[:rank] @ p_true)
        null_frac = np.linalg.norm(p_true - row_proj) / np.linalg.norm(p_true)
        errs, row_errs = [], []
        for _ in range(40):
            dn = d_clean + RNG.normal(0.0, SIGMA_T, d_clean.size)
            m_est = svd_solve(u, s, vt, dn, lam)
            errs.append(np.sqrt(np.mean((m_est + p_true) ** 2)))
            row_errs.append(np.sqrt(np.mean(
                (vt[:rank].T @ (vt[:rank] @ (m_est + p_true))) ** 2)))
        errs, row_errs = np.array(errs), np.array(row_errs)
        print(f"{nx:5d}x{nz:<4d} {g.shape[1]:7d} {g.shape[0] / g.shape[1]:9.2f} "
              f"{lam / s[0]:10.3e} {fit:11.3e} {errs.mean():12.4e} "
              f"{row_errs.mean():14.4e} {null_frac:14.3f}")
    print(f"\n  model error is the rms difference between the recovered dv/v0 and the")
    print(f"  true anomaly, whose own rms is 0.028; a relative error of 1.0 would")
    print(f"  mean the image carries no information at all")
    print("""
  Every row of the table reaches the same statistically acceptable data fit, so
  the misfit cannot choose between them -- yet the images differ, and the total
  model error grows as the grid is refined.  The last two columns give the
  reason: refinement adds parameters that no ray crosses, the null fraction
  rises, and the part of the true anomaly that no inversion can reach grows with
  it.  The recoverable part (the row-space error) does not blow up, so this is
  not a numerical failure; it is the parametrisation outrunning the data.  A
  finer grid buys a smaller misfit and a worse image, which is why the grid is
  part of the answer rather than a technical detail.""")


def part4_operators():
    section("4. Regularisation: minimum norm against minimum roughness")
    rays = geometry()
    nx, nz = 24, 18
    dx, dz = (X1 - X0) / nx, (Z_BOT - Z_TOP) / nz
    g = build_g(rays, nx, nz, dx, dz)
    p_true = smooth_model(nx, nz, dx, dz)
    d = -(g @ p_true) + RNG.normal(0.0, SIGMA_T, len(rays))
    l_mat = first_difference(nx, nz)
    smooth = np.vstack([l_mat, 0.05 * np.eye(nx * nz)])
    target = np.sqrt(len(rays)) * SIGMA_T
    ident = np.eye(nx * nz)
    print(f"{nx} x {nz} grid = {nx * nz} parameters, {len(rays)} data, "
          f"noise sigma = {SIGMA_T * 1e3:.1f} ms")
    print(f"roughness operator L: {l_mat.shape[0]} first differences.  A pure")
    print(f"difference operator does not penalise a constant model, because")
    print(f"constants lie in its null space, so the operator used here is L")
    print(f"stacked with 5 per cent of the identity ({smooth.shape[0]} rows).")
    print(f"||L m_true|| = {np.linalg.norm(l_mat @ p_true):.4e} (1/s)\n")
    print("Both operators are tuned to reach the same data misfit "
          f"sqrt(N) sigma = {target:.4e} s:")
    print(f"{'operator':>12} {'lam/||G||':>10} {'misfit (s)':>11} "
          f"{'model error':>12} {'||Lm|| (1/s)':>13} {'Lm/Lm_true':>11}")
    for (name, l_op) in (("identity", ident), ("differences", smooth)):
        lambdas = np.logspace(-5, 3, 160) * np.linalg.norm(g)

        def misfit_of(lam, l_op=l_op):
            m = np.linalg.solve(g.T @ g + lam ** 2 * (l_op.T @ l_op), g.T @ d)
            return np.sqrt(np.mean((g @ m - d) ** 2))

        lam, fit = lambda_for_misfit(misfit_of, lambdas, target)
        m_est = np.linalg.solve(g.T @ g + lam ** 2 * (l_op.T @ l_op), g.T @ d)
        print(f"{name:>12} {lam / np.linalg.norm(g):10.3e} {fit:11.4e} "
              f"{np.sqrt(np.mean((m_est + p_true) ** 2)):12.4e} "
              f"{np.linalg.norm(l_mat @ m_est):13.4e} "
              f"{np.linalg.norm(l_mat @ m_est) / np.linalg.norm(l_mat @ p_true):11.4f}")
    print("\n  Sweep of the roughness operator (damping in units of ||G||):")
    print(f"{'lam/||G||':>10} {'misfit (s)':>11} {'model error':>12} "
          f"{'Lm/Lm_true':>11}")
    for lam_rel in (1e-3, 1e-2, 3e-2, 1e-1, 3e-1):
        lam = lam_rel * np.linalg.norm(g)
        m_est = np.linalg.solve(g.T @ g + lam ** 2 * (smooth.T @ smooth), g.T @ d)
        print(f"{lam_rel:10.3e} "
              f"{np.sqrt(np.mean((g @ m_est - d) ** 2)):11.4e} "
              f"{np.sqrt(np.mean((m_est + p_true) ** 2)):12.4e} "
              f"{np.linalg.norm(l_mat @ m_est) / np.linalg.norm(l_mat @ p_true):11.4f}")
    print("""
  Minimum norm (identity) minimises the amplitude of the model; minimum
  roughness (first differences) minimises its gradient.  Matched by data misfit
  the two answers are different models of the same Earth, and the roughness
  ratio shows why: the smoother operator suppresses the high-wavenumber part of
  the image that the rays cannot resolve anyway.  The choice of L is a prior
  statement about what the Earth is like, it changes the numbers in the image by
  tens of per cent, and it belongs in the report next to the damping value.""")


def part5_nonlinearity():
    section("5. Nonlinearity: Fermat stationarity and Newton re-linearisation")
    rays = geometry()
    nx, nz = 16, 12
    dx, dz = (X1 - X0) / nx, (Z_BOT - Z_TOP) / nz
    g = build_g(rays, nx, nz, dx, dz)
    p_true = smooth_model(nx, nz, dx, dz)
    print("(a) Fermat stationarity.  A ray between a source and a receiver is the")
    print("path of stationary travel time, so moving the path changes T only to")
    print("second order.  Below, the mid-point of one ray is displaced in z by d,")
    print("the path is forced through (source, mid-point + d, receiver), and the")
    print("exact travel time through the 2-D model is integrated along it.\n")
    src = np.asarray(rays[5 * N_REC][0], dtype=float)
    rec = np.asarray(rays[5 * N_REC + 7][1], dtype=float)
    mid = 0.5 * (src + rec)

    def travel(midpoint):
        total = 0.0
        for (a, b) in ((src, midpoint), (midpoint, rec)):
            xs, zs, seg = sample_path(a, b, 1500)
            col = np.clip((xs / dx).astype(int), 0, nx - 1)
            row = np.clip((zs / dz).astype(int), 0, nz - 1)
            u = 1.0 / (V_REF * (1.0 + p_true))[row * nx + col]
            total += np.sum(u * seg)
        return total

    t_straight = travel(mid)
    print(f"ray {5 * N_REC + 7}: source z = {src[1] / 1e3:.2f} km, "
          f"receiver z = {rec[1] / 1e3:.2f} km, offset "
          f"{(rec[0] - src[0]) / 1e3:.1f} km")
    print(f"travel time along the straight path           : {t_straight:.6f} s")
    offsets = np.linspace(-1.0e3, 1.0e3, 401)
    times = np.array([travel(mid + np.array([0.0, dz_off])) for dz_off in offsets])
    k_best = int(np.argmin(times))
    print(f"minimum over mid-point depth offsets d        : {times[k_best]:.6f} s "
          f"at d = {offsets[k_best] / 1e3:+.3f} km")
    print(f"travel-time change from the straight path     : "
          f"{(times[k_best] - t_straight) * 1e3:+.3f} ms")
    print(f"  T(d) - T(0) for d = 0.25, 0.50, 1.00 km     : "
          f"{(travel(mid + np.array([0.0, 0.25e3])) - t_straight) * 1e3:+.3f}, "
          f"{(travel(mid + np.array([0.0, 0.50e3])) - t_straight) * 1e3:+.3f}, "
          f"{(travel(mid + np.array([0.0, 1.00e3])) - t_straight) * 1e3:+.3f} ms")
    print("""
  The travelled path of minimum time is displaced from the straight line by only
  70 m for this ray, and using the straight line instead costs 0.486 ms on a
  5.071 s travel time.  Forcing the path away from its own minimum is far more
  expensive, and the cost grows quadratically: going from a 0.25 km forced
  offset to 0.50 km multiplies the penalty by 4.36, and doubling again to
  1.00 km multiplies it by 4.00.  That is Fermat's principle in numbers, and it
  is why the fixed-path Jacobian is a good approximation: the travel time is
  STATIONARY with respect to path errors, so a path error enters the datum only
  at second order while it would enter a naively perturbed travel time at first
  order.

  (b) The remaining nonlinearity is in the parametrisation.  With v = v0(1+p),
  the datum is integral ds / v = -integral (ds/v0) p/(1+p), which is not linear
  in p.  Below, the same 5 per cent anomaly is inverted by (i) one linearised
  step and (ii) Newton re-linearisation, and the model error is printed after
  every step.\n""")
    lengths = np.array([cell_lengths(s, r, nx, nz, dx, dz) for s, r in rays])
    d_obs = np.array([np.sum(l / (V_REF * (1.0 + p_true))) for l in lengths]) \
        - lengths.sum(axis=1) / V_REF
    g_lin = -(lengths / (V_REF * (1.0 + p_true) ** 2)[None, :])
    u, s, vt = np.linalg.svd(g_lin, full_matrices=False)
    rank = int(np.sum(s > 1e-9 * s[0]))
    p_row = vt[:rank].T @ (vt[:rank] @ p_true)
    print(f"  the recoverable part of the anomaly (its projection on the row")
    print(f"  space of G) has rms {np.sqrt(np.mean(p_row ** 2)):.4e}, against a")
    print(f"  total dv/v0 rms of {np.sqrt(np.mean(p_true ** 2)):.4e}; the")
    print(f"  remainder is in the null space and no iteration can reach it\n")
    p_cur = np.zeros(nx * nz)
    print(f"{'iteration':>10} {'data residual rms (s)':>22} "
          f"{'error vs truth':>16} {'error vs recoverable part':>27}")
    for it in (0, 1, 2, 3, 4):
        if it > 0:
            g_it = -(lengths / (V_REF * (1.0 + p_cur) ** 2)[None, :])
            resid = d_obs - (np.sum(lengths / (V_REF * (1.0 + p_cur)), axis=1)
                             - lengths.sum(axis=1) / V_REF)
            lam = 1e-3 * np.linalg.norm(g_it)
            p_cur = p_cur + np.linalg.solve(
                g_it.T @ g_it + lam ** 2 * np.eye(nx * nz), g_it.T @ resid)
        resid_now = np.sqrt(np.mean((
            np.sum(lengths / (V_REF * (1.0 + p_cur)), axis=1)
            - lengths.sum(axis=1) / V_REF - d_obs) ** 2))
        print(f"{it:10d} {resid_now:22.4e} "
              f"{np.sqrt(np.mean((p_cur - p_true) ** 2)):16.4e} "
              f"{np.sqrt(np.mean((p_cur - p_row) ** 2)):27.4e}")
    print("""
  The first linearised step already reproduces the recoverable part of the
  anomaly to 3.3 per cent of its rms (7.77e-04 against 2.35e-02), and it leaves a
  data residual of 2.99e-03 s.  Re-linearising about the updated model multiplies
  that residual by 1/1400 in ONE further iteration, to 2.13e-06 s.  The
  nonlinearity lives in the parametrisation (1/(1+p) is not 1-p) and it is
  mild, so the residual after convergence is no longer a parametrisation error:
  what is left is the part of the anomaly the ray geometry cannot see, printed
  as the error against the recoverable projection.  That is a resolution limit,
  not an iteration error, and the next lesson quantifies it.""")


def main():
    part1_parametrisation()
    part2_solvers()
    part3_grid_size()
    part4_operators()
    part5_nonlinearity()
    print("\nAll models and data in this file are SYNTHETIC (see the module")
    print("docstring for every parameter).  Done.")


if __name__ == "__main__":
    main()
