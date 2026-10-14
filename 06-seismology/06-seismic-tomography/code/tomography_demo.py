#!/usr/bin/env python3
"""Seismic travel-time tomography as a linear inverse problem: five measurements.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tomography_demo.py

Requires: numpy.  Print-only; no figures, no network.

Companion to lessons 06-06-01 (the tomography principle: data as path
integrals), 06-06-02 (parametrisation and inversion) and 06-06-03 (resolution,
null space and model covariance).

SYNTHETIC setup.  A 10 x 10 cell grid over 10 km x 5 km; a cross-hole
acquisition with 12 sources in the left borehole and 12 receivers in the right
borehole (144 rays); straight-ray paths; a background velocity of 4000 m/s;
+/- 5 to 8 per cent Gaussian velocity anomalies; 0.02 s of Gaussian
travel-time noise unless stated otherwise.  No real survey, station or
published model appears anywhere in this file.

Contents
--------
1. The forward problem and its linearisation.  T = integral ds / v is a path
   integral; d = G m with m the slowness perturbation and G the ray length in
   each cell; the error of the first-order expansion is MEASURED against the
   exact travel time through the same model.
2. The null space, concretely: two models that fit noise-free data to machine
   precision while differing substantially.
3. Ray coverage and aperture: the same 144 rays at two different angular
   ranges, the same inversion, and the measured difference in recovery.
4. The resolution matrix R and the trade-off between resolution and variance.
5. Parameter choice: L-curve, generalised cross-validation and the discrepancy
   principle, each compared against the best achievable model error.
"""

import numpy as np

SEED = 20261014
RNG = np.random.default_rng(SEED)

NX, NZ = 10, 10              # cells across (x), cells down (z)
DX, DZ = 1.0e3, 0.5e3         # m
V_BG = 4000.0                # m/s, SYNTHETIC background
U_BG = 1.0 / V_BG            # s/m, background slowness
N_SRC, N_REC = 12, 12
SIGMA_T = 0.02               # s, travel-time noise

# Model vector convention: index = (z index) * NX + (x index), x fastest.


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def cell_lengths(p, q, n=2000):
    """Length of segment p-q inside each cell, by dense sampling.

    Returns metres per cell, ordered as the model vector (x fastest).
    """
    t = np.linspace(0.0, 1.0, n)
    xs = p[0] + (q[0] - p[0]) * t
    zs = p[1] + (q[1] - p[1]) * t
    col = np.clip((xs / DX).astype(int), 0, NX - 1)
    row = np.clip((zs / DZ).astype(int), 0, NZ - 1)
    seg = np.hypot(q[0] - p[0], q[1] - p[1]) / (n - 1)
    out = np.zeros(NX * NZ)
    np.add.at(out, row * NX + col, seg)
    return out


def geometry(kind="wide"):
    """Source/receiver positions of a cross-borehole survey.

    Both kinds use the same 12 sources in the left borehole (x = 2 km) and the
    same 12 receivers in the right borehole (x = 98 km) at 12 depths, so the RAY
    COUNT is 144 in both cases.  Only the depth range of the receivers differs,
    and therefore only the range of ray angles crossing the interior.
    """
    src = np.column_stack([np.full(N_SRC, 0.2e3),
                           np.linspace(0.2e3, 4.8e3, N_SRC)])
    if kind == "wide":
        rec = np.column_stack([np.full(N_REC, 9.8e3),
                               np.linspace(0.2e3, 4.8e3, N_REC)])
    else:                        # narrow aperture: receivers clustered at depth
        rec = np.column_stack([np.full(N_REC, 9.8e3),
                               np.linspace(1.9e3, 3.1e3, N_REC)])
    return [(s, r) for s in src for r in rec]


def build_g(rays):
    """Jacobian of the straight-ray problem: length in cell / background velocity.

    Units: m / (m/s) = s, so G m has the units of a travel-time perturbation.
    """
    return np.array([cell_lengths(s, r) for s, r in rays]) / V_BG


def true_model(kind="blobs"):
    """Relative velocity perturbation dv/v0, as a flat model vector.

    m = dv/v0 is what a tomographer usually plots; the slowness perturbation
    used by the linear operator is -m to first order, which section 1 spells out.
    """
    xc = (np.arange(NX) + 0.5) * DX
    zc = (np.arange(NZ) + 0.5) * DZ
    zz, xx = np.meshgrid(zc, xc, indexing="ij")      # shape (NZ, NX), x fastest
    if kind == "blobs":
        out = np.zeros((NZ, NX))
        for (bx, bz, amp, w) in ((2.5e3, 1.2e3, 0.08, 1.2e3),
                                 (7.5e3, 3.5e3, 0.06, 1.5e3)):
            out += amp * np.exp(-((xx - bx) ** 2 + (zz - bz) ** 2) / (2.0 * w ** 2))
        return out.ravel()
    if kind == "checker":
        i = (xx / DX).astype(int)
        j = (zz / DZ).astype(int)
        return (0.05 * (-1.0) ** (i + j)).ravel()
    # a smooth long-wavelength pattern, one wavelength across the grid
    return (0.05 * np.cos(np.pi * xx / (NX * DX))
            * np.cos(np.pi * zz / (NZ * DZ))).ravel()


def svd_filtered_solve(u, s, vt, d, lam):
    """m(lam) = (G^T G + lam^2 I)^-1 G^T d, evaluated with a precomputed SVD."""
    filt = s / (s ** 2 + lam ** 2)
    return vt.T @ (filt * (u[:, :s.size].T @ d))


def coverage(g):
    """Number of rays that enter each cell."""
    return (g > 0).sum(axis=0)


def part1_forward_and_linearisation():
    section("1. The forward problem, and the error of its linearisation")
    print("Travel time along a ray is a path integral of slowness:")
    print("    T = integral_ray ds / v(x) = integral_ray u(x) ds.")
    print("Perturb the slowness, u = u0 + delta u, and keep the ray fixed:")
    print("    delta T = integral_ray delta u ds   ->   d = G m,")
    print("G_rc = length of ray r inside cell c, m = the slowness perturbation.\n")
    rays = geometry("wide")
    g = build_g(rays)
    t0 = np.array([np.hypot(r[0] - s[0], r[1] - s[1]) / V_BG for s, r in rays])
    print(f"rays                     : {g.shape[0]}")
    print(f"cells (parameters)       : {g.shape[1]}")
    print(f"non-zero G entries       : {int(np.count_nonzero(g))} "
          f"({100.0 * np.count_nonzero(g) / g.size:.2f} per cent of G)")
    print(f"mean reference travel time: {t0.mean():.3f} s "
          f"(range {t0.min():.3f} to {t0.max():.3f} s)")
    print(f"reference velocity       : {V_BG:.0f} m/s  "
          f"(slowness {U_BG:.3e} s/m)\n")
    print("Tomographers usually parametrise velocity, v = v0 (1 + p), not")
    print("slowness.  Then the datum is NONLINEAR in p:")
    print("    T - T0 = integral ds (1/v - 1/v0) = -integral (ds/v0) p/(1+p)")
    print("    linear part: -integral (ds/v0) p ;  remainder: +integral (ds/v0)"
          " p^2/(1+p).")
    print("The remainder is computed exactly below (it is the second-order term")
    print("of the expansion; ray bending, which is not modelled here, is of the")
    print("same order in p).\n")
    p = true_model("blobs")
    len_mat = np.array([cell_lengths(s, r) for s, r in rays])
    exact = len_mat @ (1.0 / (V_BG * (1.0 + p)))
    linear = -(len_mat @ p) / V_BG
    datum = exact - t0
    err = datum - linear
    print(f"datum dT range            : {datum.min():+.4f} to {datum.max():+.4f} s")
    print(f"rms datum                 : {np.sqrt(np.mean(datum ** 2)):.4e} s")
    print(f"max |exact - linear|      : {np.abs(err).max():.4e} s")
    print(f"rms |exact - linear|      : {np.sqrt(np.mean(err ** 2)):.4e} s")
    print(f"rms error / rms datum     : "
          f"{np.sqrt(np.mean(err ** 2)) / np.sqrt(np.mean(datum ** 2)):.4f} "
          f"({100.0 * np.sqrt(np.mean(err ** 2)) / np.sqrt(np.mean(datum ** 2)):.2f} per cent)")
    print(f"max |p| in the model      : {np.abs(p).max():.3f} "
          f"({100.0 * np.abs(p).max():.1f} per cent velocity perturbation)")
    print("""
  The remainder is about six per cent of the datum rms for 8 per cent
  anomalies, and it scales as p^2: halving the anomalies quarters it.  This is why travel-time
  tomography is run iteratively -- solve, retrace the rays in the updated model,
  rebuild G, solve again -- and why the first iteration is already a good
  answer.  It is ALSO why the answer depends on the reference model: a different
  v0 changes both the rays and the size of the neglected term.""")


def part2_nullspace():
    section("2. Underdetermined and non-unique, made concrete")
    rays = geometry("wide")
    g = build_g(rays)
    n_cell = g.shape[1]
    u, s, vt = np.linalg.svd(g, full_matrices=True)
    tol = 1e-9 * s[0]
    rank = int(np.sum(s > tol))
    print(f"G is {g.shape[0]} x {g.shape[1]} (data x parameters)")
    print("largest 8 singular values (s):")
    print("  " + "  ".join(f"{v:.3e}" for v in s[:8]))
    print(f"rank at a 1e-9 relative tolerance : {rank} of {n_cell}")
    print(f"null-space dimension              : {n_cell - rank}")
    print(f"condition number of G             : {s[0] / s[rank - 1]:.3e}\n")
    m_true = -true_model("blobs")          # the slowness perturbation seen by G
    d = g @ m_true
    m_ls = np.linalg.lstsq(g, d, rcond=None)[0]
    v_null = vt[n_cell - 1]                # highest-index right singular vector
    amp = 0.5 * np.linalg.norm(m_true) / np.linalg.norm(v_null)
    m_alt = m_ls + amp * v_null
    cover = coverage(g)
    peak = int(np.argmax(np.abs(v_null)))
    print("Two models fitted to the SAME noise-free data:")
    print(f"  ||G m_1 - d||            = {np.linalg.norm(g @ m_ls - d):.3e}"
          f"   (data scale ||d|| = {np.linalg.norm(d):.3e})")
    print(f"  ||G m_2 - d||            = {np.linalg.norm(g @ m_alt - d):.3e}")
    print(f"  ||G m_2 - G m_1|| / ||d||= "
          f"{np.linalg.norm(g @ m_alt - g @ m_ls) / np.linalg.norm(d):.3e}")
    print(f"  ||m_2 - m_1||            = {np.linalg.norm(m_alt - m_ls):.4e} s/m")
    print(f"  ||m_1||                  = {np.linalg.norm(m_ls):.4e} s/m")
    print(f"  rms(m_2 - m_1) / rms(m_true) = "
          f"{np.sqrt(np.mean((m_alt - m_ls) ** 2)) / np.sqrt(np.mean(m_true ** 2)):.4f}")
    print(f"  the added vector is a right singular vector with s = "
          f"{s[n_cell - 1]:.2e} s")
    print(f"  its largest component sits in cell (x = "
          f"{(peak % NX) * DX / 1e3 + 0.5 * DX / 1e3:.1f} km, z = "
          f"{(peak // NX) * DZ / 1e3 + 0.5 * DZ / 1e3:.1f} km), crossed by "
          f"{cover[peak]} rays")
    print(f"  mean ray count per cell: {cover.mean():.1f}; cells with 0 rays: "
          f"{int(np.sum(cover == 0))}")
    print("""
  The two models are indistinguishable in the data to machine precision while
  differing by a substantial fraction of the model norm.  The difference is
  built from a right singular vector of G with a numerically zero singular
  value, i.e. from a direction in which G is exactly zero: the data CANNOT
  contain information about it.  Only a prior, a regularisation term or a
  different acquisition can choose between the two, and that choice is a
  scientific decision, not a mathematical one.""")


def part3_coverage_and_aperture():
    section("3. Ray coverage and aperture: same rays, different angles")
    print("Both acquisitions below use the same 144 rays between the same 12")
    print("sources and 12 receivers and the same true model.  Only the spread of")
    print("receiver depths changes, hence only the angular range of the rays.\n")
    m_true = -true_model("blobs")
    p_true = true_model("blobs")
    for kind, label in (("wide", "wide aperture   (receivers over 0.2-4.8 km)"),
                        ("narrow", "narrow aperture (receivers over 1.9-3.1 km)")):
        rays = geometry(kind)
        g = build_g(rays)
        uu, ss, vvt = np.linalg.svd(g, full_matrices=False)
        lam = 2e-2 * ss[0]
        m_est = svd_filtered_solve(uu, ss, vvt, g @ m_true, lam)
        cov = coverage(g)
        p_est = -m_est
        print(f"{label}")
        print(f"  rays per cell: min {cov.min()}, median {int(np.median(cov))}, "
              f"max {cov.max()}; cells with no ray: {int(np.sum(cov == 0))}")
        print(f"  data misfit  : {np.sqrt(np.mean((g @ m_est - g @ m_true) ** 2)):.3e} s "
              f"(noise level {SIGMA_T:.2f} s)")
        for (bx, bz, name) in ((2.5e3, 1.2e3, "shallow blob (x= 2.5, z=1.2 km)"),
                               (7.5e3, 3.5e3, "deep blob    (x= 7.5, z=3.5 km)")):
            i = int(bx / DX)
            j = int(bz / DZ)
            k = j * NX + i
            got = p_est[k] / p_true[k] if p_true[k] != 0.0 else np.nan
            print(f"  {name}: input {p_true[k]:+.4f}, recovered "
                  f"{p_est[k]:+.4f} (dv/v0), {100.0 * got:+.1f} per cent")
        r2 = 1.0 - np.sum((p_est - p_true) ** 2) / np.sum(p_true ** 2)
        print(f"  rms model error: {np.sqrt(np.mean((p_est - p_true) ** 2)):.4e} "
              f"(dv/v0); variance explained R2 = {r2:.3f}")
        r_mat = vvt.T @ np.diag(ss ** 2 / (ss ** 2 + lam ** 2)) @ vvt
        i0, j0 = int(7.5e3 / DX), int(3.5e3 / DZ)
        psf = np.abs(r_mat[:, j0 * NX + i0]).reshape(NZ, NX)
        sx = np.sqrt((psf * ((np.arange(NX) - i0) * DX / 1e3)[None, :] ** 2).sum()
                     / psf.sum())
        sz = np.sqrt((psf * ((np.arange(NZ) - j0) * DZ / 1e3)[:, None] ** 2).sum()
                     / psf.sum())
        print(f"  point spread of the deep-blob cell: {sx:.2f} km in x, "
              f"{sz:.2f} km in z (x/z ratio {sx / sz:.2f}), "
              f"self-weight |R_kk| = {r_mat[j0 * NX + i0, j0 * NX + i0]:.3f}")
    print("""
  Resolution is a property of the GEOMETRY.  Both blocks have the same 144
  rays, the same true model and an essentially zero misfit on these noise-free
  data, so an image can be produced in either case -- yet the narrow-aperture
  image contains far less of the true anomaly (compare the recovered
  percentages, R2 and the x/z ratio of the point spread of the same cell), and
  it leaves a third of the cells with no ray at all.  Comparing the two blocks
  is the resolution test: same data quantity, different answer, and the
  difference is decided entirely by the angular range of the rays.  Run this
  test before interpreting any image, and report it with the image.""")


def part4_resolution_and_variance():
    section("4. The resolution matrix, and the resolution-variance trade-off")
    rays = geometry("wide")
    g = build_g(rays)
    n_cell = g.shape[1]
    u, s, vt = np.linalg.svd(g, full_matrices=True)
    print("Damped least squares with damping lam gives")
    print("    m(lam) = (G^T G + lam^2 I)^-1 G^T d = A(lam) d,")
    print("and its model-space resolution matrix is")
    print("    R(lam) = A(lam) G = (G^T G + lam^2 I)^-1 G^T G,")
    print("so that the noise-free estimate is R m_true.  R = I means perfect")
    print("recovery of every cell; R is a MATRIX, so resolution is a shape, not a")
    print("number.  Its rows show where each cell's estimate comes from.\n")
    m_true = -true_model("blobs")
    m_row = vt.T @ (vt @ m_true)        # component of m_true in the row space
    d = g @ m_true
    s_max = s[0]
    print(f"{'lam/lam_max':>12} {'||R-I||_F/rt(n)':>17} {'min row sum':>12} "
          f"{'misfit (s)':>11} {'rms bias':>10} {'rms std dev':>12} "
          f"{'total rms err':>14}")
    for lam_rel in (1e-4, 1e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0, 3.0):
        lam = lam_rel * s_max
        r_mat = vt.T @ np.diag(s ** 2 / (s ** 2 + lam ** 2)) @ vt
        m_est = svd_filtered_solve(u, s, vt, d, lam)
        std = SIGMA_T * np.sqrt(
            np.mean(np.sum(vt.T ** 2 * (s ** 2 / (s ** 2 + lam ** 2) ** 2), axis=1)))
        bias = np.sqrt(np.mean((m_est - m_row) ** 2))
        print(f"{lam_rel:12.0e} "
              f"{np.linalg.norm(r_mat - np.eye(n_cell)) / np.sqrt(n_cell):17.4e} "
              f"{np.min(r_mat.sum(axis=1)):12.4f} "
              f"{np.sqrt(np.mean((g @ m_est - d) ** 2)):11.3e} "
              f"{bias:10.3e} {std:12.4e} {np.hypot(bias, std):14.4e}")
    print(f"\n  rms of m_true in the row space = {np.sqrt(np.mean(m_row ** 2)):.4e} s/m")
    print("  rms model error is measured against the row-space part of the truth,")
    print("  because no method can recover the null-space part at all.")
    print("  rms std dev is the analytic noise-driven standard deviation of the")
    print("  estimate, sigma * sqrt(trace(A A^T)/n), with sigma = "
          f"{SIGMA_T} s.\n")
    r_fix = vt.T @ np.diag(s ** 2 / (s ** 2 + (1e-2 * s_max) ** 2)) @ vt
    print("\n  Point-spread of two cells at lam = 1e-2 lam_max, weighted over all")
    print("  cells (the diagonal is how much of a cell's estimate is its own):")
    for (i, j, name) in ((2, 2, "cell at x=2.5, z=1.2 km"),
                         (0, 0, "corner cell at x=0.5, z=0.2 km")):
        k = j * NX + i
        psf = np.abs(r_fix[:, k]).reshape(NZ, NX)
        sx = np.sqrt((psf * ((np.arange(NX) - i) * DX / 1e3)[None, :] ** 2).sum()
                     / psf.sum())
        sz = np.sqrt((psf * ((np.arange(NZ) - j) * DZ / 1e3)[:, None] ** 2).sum()
                     / psf.sum())
        print(f"    {name}: |R_kk| = {r_fix[k, k]:.3f}, row sum "
              f"{r_fix[k].sum():.3f}, spread {sx:.2f} km in x and {sz:.2f} km "
              f"in z, off-diagonal weight {r_fix[k].sum() - r_fix[k, k]:+.3f}")
    tot = []
    for lam_rel in (1e-4, 1e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0, 3.0):
        lam = lam_rel * s_max
        m_est = svd_filtered_solve(u, s, vt, d, lam)
        bias = np.sqrt(np.mean((m_est - m_row) ** 2))
        std = SIGMA_T * np.sqrt(
            np.mean(np.sum(vt.T ** 2 * (s ** 2 / (s ** 2 + lam ** 2) ** 2), axis=1)))
        tot.append(np.hypot(bias, std))
    print(f"  the total rms error of the last table is smallest at "
          f"lam/lam_max = "
          f"{(1e-4, 1e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0, 3.0)[int(np.argmin(tot))]:.1e}"
          f", with value {min(tot):.4e} s/m against a model rms of "
          f"{np.sqrt(np.mean(m_row ** 2)):.4e} s/m")
    print("""
  Reading the table: the noise-driven standard deviation falls by two orders of
  magnitude as damping increases, while the resolution (||R-I|| and the row
  sums) gets worse in the same direction.  The last column combines the two
  costs, sqrt(bias^2 + variance), and it has a minimum at an intermediate
  damping -- here 3e-1 of the largest singular value, where the total rms error
  is about half the model rms and both terms matter.  Above that damping the
  bias dominates, below it the variance does.  Damping is not a nuisance
  parameter: it selects a point on this trade-off, and the point belongs in the
  report.""")


def part5_parameter_choice():
    section("5. Parameter choice: three rules, measured against the optimum")
    rays = geometry("wide")
    g = build_g(rays)
    u, s, vt = np.linalg.svd(g, full_matrices=False)
    m_true = -true_model("blobs")
    m_row = vt.T @ (vt @ m_true)
    d_clean = g @ m_true
    ud_clean = u.T @ d_clean
    lambdas = np.logspace(-6, 0, 400) * s[0]

    def m_of(lam, ud):
        return vt.T @ (s / (s ** 2 + lam ** 2) * ud)

    print("The same inversion, the same three automatic rules, at two noise")
    print("levels.  The rules see only the data and the assumed noise level;")
    print("the 'optimum' is the best achievable model error, known here because")
    print("the answer is known.  A ratio of 1.00x means the rule found it.\n")
    for sigma in (0.002, 0.02):
        d = d_clean + RNG.normal(0.0, sigma, d_clean.size)
        ud = u.T @ d
        m_err = np.array([np.linalg.norm(m_of(l, ud) - m_row) for l in lambdas])
        misfit = np.array([np.linalg.norm(g @ m_of(l, ud) - d) for l in lambdas])
        norm_m = np.array([np.linalg.norm(m_of(l, ud)) for l in lambdas])
        best_i = int(np.argmin(m_err))
        x, y = np.log(misfit), np.log(norm_m)
        dx, dy = np.gradient(x), np.gradient(y)
        kappa = np.abs(dx * np.gradient(dy) - dy * np.gradient(dx)) / \
            (dx ** 2 + dy ** 2) ** 1.5
        i_lc = int(np.argmax(kappa))
        gcv = np.empty(lambdas.size)
        for i, l in enumerate(lambdas):
            resid_sq = np.sum((l ** 2 / (s ** 2 + l ** 2)) ** 2 * ud ** 2)
            trace = np.sum(s ** 2 / (s ** 2 + l ** 2))
            gcv[i] = resid_sq / (d.size - trace) ** 2
        i_gcv = int(np.argmin(gcv))
        target = np.sqrt(d.size) * sigma
        ok = np.where(misfit <= target)[0]
        i_dp = int(ok[-1]) if ok.size else int(np.argmin(np.abs(misfit - target)))
        print(f"  sigma = {sigma:.4f} s  ({100.0 * sigma / np.sqrt(np.mean(d_clean ** 2)):.1f} "
              f"per cent of the datum rms),  ||d|| = {np.linalg.norm(d):.4e} s,  "
              f"expected misfit sqrt(N) sigma = {target:.4e} s")
        print(f"    best achievable model error: {m_err[best_i]:.4e} s/m "
              f"at lam = {lambdas[best_i]:.4e}")
        for (name, i) in (("L-curve    ", i_lc), ("GCV        ", i_gcv),
                          ("discrepancy", i_dp)):
            print(f"    {name}: lam = {lambdas[i]:.4e}, misfit "
                  f"{misfit[i]:.4e} s ({misfit[i] / target:.2f} x sqrt(N) sigma), "
                  f"model error {m_err[i]:.4e} s/m, ratio to best "
                  f"{m_err[i] / m_err[best_i]:.2f}x")
        print()
    print("""  The discrepancy principle picks the LARGEST damping whose misfit is still
  statistically acceptable, so it stops early and buys variance reduction at
  the cost of bias; the L-curve and GCV balance the two without knowing the
  noise level.  Which rule wins, and by how much, changes with the noise level
  and with the singular-value spectrum -- compare the two blocks above.  A
  tomographic image without a stated damping rule, a stated data misfit and a
  stated assumed noise level cannot be reproduced or compared with another,
  which is the practical reason this section exists.""")


def main():
    part1_forward_and_linearisation()
    part2_nullspace()
    part3_coverage_and_aperture()
    part4_resolution_and_variance()
    part5_parameter_choice()
    print("\nAll models and data in this file are SYNTHETIC (see the module")
    print("docstring for every parameter).  Done.")


if __name__ == "__main__":
    main()
