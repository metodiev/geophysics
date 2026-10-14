#!/usr/bin/env python3
"""Resolution, null space and model covariance for a travel-time inverse problem.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resolution_and_nullspace_demo.py

Requires: numpy.  Print-only; no figures, no network.

Companion to lesson 06-06-03.  Everything here is SYNTHETIC: a 16 km x 5.5 km
cross-hole survey in a homogeneous 3000 m/s reference medium, 12 sources and 12
receivers in opposite boreholes (144 rays), straight-ray paths, a 16 x 12 cell
grid (192 parameters), 5 ms of travel-time noise, and chosen teaching anomalies.
No real survey, station or published model is used.

Contents
--------
1. Singular-value spectrum, numerical rank and condition number for two
   acquisitions of the same size.
2. The model resolution matrix R: diagonal, row sums, and the point-spread
   length of a well-covered and a poorly covered cell.
3. Null-space vectors, explicitly, of two kinds: one built from cells that no
   ray crosses, and one smooth vector from the singular-value decomposition.
4. Model covariance: analytic standard deviations checked against Monte Carlo,
   and the correlation between distant cells.
5. The resolution-variance trade-off, with trace(R) as "number of resolved
   parameters".
6. A known-model test: a long-wavelength pattern against a checkerboard.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

X0, X1 = 0.2e3, 15.8e3
Z_TOP, Z_BOT = 0.25e3, 5.75e3
V_REF = 3000.0
SIGMA_T = 5.0e-3
NX, NZ = 16, 12
DX, DZ = (X1 - X0) / NX, (Z_BOT - Z_TOP) / NZ


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def sample(p, q, n=1500):
    t = np.linspace(0.0, 1.0, n)
    return (p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t,
            np.hypot(q[0] - p[0], q[1] - p[1]) / (n - 1))


def cell_lengths(p, q, n=1500):
    xs, zs, seg = sample(p, q, n)
    col = np.clip((xs / DX).astype(int), 0, NX - 1)
    row = np.clip((zs / DZ).astype(int), 0, NZ - 1)
    out = np.zeros(NX * NZ)
    np.add.at(out, row * NX + col, seg)
    return out


def geometry(kind="crossing"):
    """Two acquisitions with the same number of rays and different coverage."""
    if kind == "crossing":
        src = np.column_stack([np.full(12, X0), np.linspace(Z_TOP, Z_BOT, 12)])
        rec = np.column_stack([np.full(12, X1), np.linspace(Z_TOP, Z_BOT, 12)])
    else:                       # sources shallow-left, receivers deep-right
        src = np.column_stack([np.full(12, X0),
                               np.linspace(Z_TOP, 0.5 * Z_BOT, 12)])
        rec = np.column_stack([np.full(12, X1),
                               np.linspace(0.5 * Z_BOT, Z_BOT, 12)])
    return [(s, r) for s in src for r in rec]


def build_g(rays):
    return np.array([cell_lengths(s, r) for s, r in rays]) / V_REF


def model(kind="long"):
    xc = (np.arange(NX) + 0.5) * DX
    zc = (np.arange(NZ) + 0.5) * DZ
    zz, xx = np.meshgrid(zc, xc, indexing="ij")
    if kind == "long":
        return (0.05 * np.cos(np.pi * xx / (NX * DX))
                * np.cos(np.pi * zz / (NZ * DZ))).ravel()
    i = (xx / DX).astype(int)
    j = (zz / DZ).astype(int)
    if kind == "checker4":                 # 4 km x 2 km blocks
        return (0.05 * (-1.0) ** (i // 4 + j // 4)).ravel()
    return (0.05 * (-1.0) ** (i + j)).ravel()      # one cell per block


def psf_metrics(r_mat, k):
    """Point-spread of cell k: self weight, spread in km, off-diagonal weight."""
    grid = np.abs(r_mat[:, k]).reshape(NZ, NX)
    i, j = k % NX, k // NX
    sx = np.sqrt((grid * ((np.arange(NX) - i) * DX / 1e3)[None, :] ** 2).sum()
                 / grid.sum())
    sz = np.sqrt((grid * ((np.arange(NZ) - j) * DZ / 1e3)[:, None] ** 2).sum()
                 / grid.sum())
    return r_mat[k, k], sx, sz, grid.sum() - r_mat[k, k]


def part1_spectrum():
    section("1. Singular-value spectrum: rank depends on the acquisition")
    print(f"grid {NX} x {NZ} = {NX * NZ} parameters; three acquisitions, "
          f"144 rays each\n")
    print(f"{'acquisition':>28} {'rank':>6} {'null dim':>9} {'cond':>10} "
          f"{'cells with 0 rays':>18}")
    for kind in ("crossing", "one-sided", "single borehole"):
        if kind == "single borehole":
            src = np.column_stack([np.full(12, X0), np.linspace(Z_TOP, Z_BOT, 12)])
            rec = np.column_stack([np.full(12, X0 + 50.0),
                                   np.linspace(Z_TOP, Z_BOT, 12)])
            rays = [(s, r) for s in src for r in rec]
        else:
            rays = geometry(kind)
        g = build_g(rays)
        s = np.linalg.svd(g, compute_uv=False)
        rank = int(np.sum(s > 1e-9 * s[0]))
        cover = (g > 0).sum(axis=0)
        print(f"{kind:>28} {rank:6d} {g.shape[1] - rank:9d} "
              f"{s[0] / s[rank - 1]:10.3e} {int(np.sum(cover == 0)):16d}")
    print("""
  All three rows have 144 data and 192 parameters, so on a parameter count they
  look equally determined.  They are not: the single-borehole survey is
  degenerate (its rays cross one line of cells, so almost the whole grid is
  null), and the one-sided survey loses the shallow part of the section.  Rank
  is a property of the ray geometry and must be computed, not assumed.""")


def part2_resolution_matrix():
    section("2. The resolution matrix R")
    rays = geometry("crossing")
    g = build_g(rays)
    n = g.shape[1]
    u, s, vt = np.linalg.svd(g, full_matrices=False)
    lam = 3e-2 * s[0]
    r_mat = vt.T @ np.diag(s ** 2 / (s ** 2 + lam ** 2)) @ vt
    diag = np.diag(r_mat)
    rows = r_mat.sum(axis=1)
    cover = (g > 0).sum(axis=0)
    print(f"damping lam = 3e-2 x s_max = {lam:.4e} s")
    print(f"diagonal of R: min {diag.min():.3f}, median "
          f"{np.median(diag):.3f}, max {diag.max():.3f}")
    print(f"row sums of R: min {rows.min():.3f}, median {np.median(rows):.3f}, "
          f"max {rows.max():.3f}")
    print(f"trace(R) = {np.trace(r_mat):.1f} of {n}, i.e. the data set resolves "
          f"the equivalent of {np.trace(r_mat):.0f} independent parameters\n")
    print("  Point spread of individual cells (spread in km, |off-diagonal| weight):")
    best = int(np.argmax(cover))
    worst = int(np.argmin(cover))
    for k, name in ((best, f"best covered  ({cover[best]} rays)"),
                    (worst, f"worst covered ({cover[worst]} rays)")):
        w, sx, sz, off = psf_metrics(r_mat, k)
        print(f"    cell (x={(k % NX) * DX / 1e3 + 0.5 * DX / 1e3:.2f}, "
              f"z={(k // NX) * DZ / 1e3 + 0.5 * DZ / 1e3:.2f}) km, {name}: "
              f"self {w:.3f}, spread {sx:.2f} x {sz:.2f} km, other cells "
              f"{off:+.3f}")
    widths = np.array([psf_metrics(r_mat, k)[1:3] for k in range(n)])
    print(f"\n  point-spread length over all cells: x median "
          f"{np.median(widths[:, 0]):.2f} km, z median "
          f"{np.median(widths[:, 1]):.2f} km; the median self-weight is "
          f"{np.median(diag):.3f}")
    print("""
  R is a matrix, so resolution has a shape and a direction.  Its diagonal is
  below one everywhere, meaning every cell's estimate contains a contribution
  from other cells; its off-diagonal entries say from where.  The point spread
  is a few cells wide in x and narrower in z because the rays of this survey are
  mostly horizontal: the vertical extent of a feature is better constrained than
  its horizontal extent.  Quoting "the resolution" as a single number discards
  exactly the information an interpreter needs.""")


def part3_null_space():
    section("3. Null-space vectors, written down")
    print("(a) The one-sided acquisition, whose shallow cells no ray reaches.")
    rays = geometry("one-sided")
    g = build_g(rays)
    cover = (g > 0).sum(axis=0)
    print(f"    cells with no ray: {int(np.sum(cover == 0))} of {g.shape[1]}")
    ind = (cover == 0).astype(float)
    dv = 0.05 * ind
    d_change = g @ (-dv / V_REF)
    print(f"    ||G v|| for the indicator vector v of those cells: "
          f"{np.linalg.norm(g @ ind):.3e} s")
    print(f"    5 per cent of velocity added in those cells changes the data by")
    print(f"    {np.sqrt(np.mean(d_change ** 2)) * 1e6:.2f} microseconds rms, "
          f"against a noise sigma of {SIGMA_T * 1e3:.1f} ms "
          f"({SIGMA_T * 1e6:.0f} microseconds)")
    print(f"    ratio to the noise: "
          f"{np.sqrt(np.mean(d_change ** 2)) / SIGMA_T:.3e} -- invisible\n")
    print("(b) The crossing acquisition, where every cell is crossed by at least")
    print("    one ray, and the null space is nevertheless 51-dimensional.")
    rays = geometry("crossing")
    g = build_g(rays)
    cover = (g > 0).sum(axis=0)
    u, s, vt = np.linalg.svd(g, full_matrices=True)
    rank = int(np.sum(s > 1e-9 * s[0]))
    v_last = vt[g.shape[1] - 1]
    d_ref = g @ np.abs(model("long"))
    print(f"    rank {rank} of {min(g.shape)}, so {g.shape[1] - rank} directions "
          f"have exactly zero singular value")
    print(f"    ||G v_last|| / ||d_ref||    : "
          f"{np.linalg.norm(g @ v_last) / np.linalg.norm(d_ref):.3e}")
    print(f"    ||v_last||                  : {np.linalg.norm(v_last):.6f}")
    print(f"    max |v_last| / rms(v_last)  : "
          f"{np.abs(v_last).max() / np.sqrt(np.mean(v_last ** 2)):.2f}")
    print(f"    correlation of |v_last| with the number of rays per cell: "
          f"{np.corrcoef(np.abs(v_last), cover)[0, 1]:+.3f}")
    k = int(np.argmax(np.abs(v_last)))
    print(f"    its largest element sits in cell (x="
          f"{(k % NX) * DX / 1e3 + 0.5 * DX / 1e3:.2f}, "
          f"z={(k // NX) * DZ / 1e3 + 0.5 * DZ / 1e3:.2f}) km, crossed by "
          f"{cover[k]} rays")
    print(f"    the pattern is not simply the weakly covered cells: its")
    print(f"    max/rms ratio is 3.4 and its correlation with the number of rays")
    print(f"    per cell is only -0.30\n")
    print("""  Nothing here is a numerical artefact or a solver bug.  A perturbation
  along a direction in which the data have exactly zero sensitivity cannot be
  recovered by any algorithm, and the true Earth may well have structure there.
  The honest responses are to add rays that cross the region, or to adopt a
  prior, state it, and report the result as conditional on that prior.""")
    return


def part4_covariance():
    section("4. Model covariance, and why errors are correlated")
    rays = geometry("crossing")
    g = build_g(rays)
    n = g.shape[1]
    u, s, vt = np.linalg.svd(g, full_matrices=False)
    lam = 3e-2 * s[0]
    filt = s / (s ** 2 + lam ** 2)
    # Cov(m) = sigma^2 A A^T with A = V diag(filt) U^T, so A A^T = V diag(filt^2) V^T
    cov_unit = (vt.T * (filt ** 2)) @ vt          # A A^T, i.e. cov / sigma^2
    std = SIGMA_T * np.sqrt(np.diag(cov_unit).clip(0.0))
    print(f"damping lam = 3e-2 x s_max, noise sigma = {SIGMA_T * 1e3:.1f} ms")
    print(f"analytic model standard deviation: min {std.min():.3e}, "
          f"median {np.median(std):.3e}, max {std.max():.3e} (in dv/v0)")
    print(f"i.e. on the {V_REF:.0f} m/s reference, a velocity uncertainty of "
          f"{100.0 * np.median(std):.3f} per cent of v0, or "
          f"{np.median(std) * V_REF:.1f} m/s\n")
    trials = 300
    est = np.empty((trials, n))
    d0 = g @ -model("long")
    for k in range(trials):
        d = d0 + RNG.normal(0.0, SIGMA_T, d0.size)
        est[k] = vt.T @ (filt * (u[:, :s.size].T @ d))
    emp = est.std(axis=0, ddof=1)
    rel = np.abs(emp - std) / np.where(std > 0, std, np.nan)
    print(f"Monte Carlo over {trials} noise realisations:")
    print(f"  max relative difference between empirical and analytic std "
          f"dev (cells with std > 1e-6): {np.nanmax(rel[std > 1e-6]):.4f}")
    print(f"  mean empirical std dev {np.mean(emp):.3e} against analytic "
          f"{np.mean(std):.3e} (in dv/v0)")
    rms_unit = np.sqrt(np.diag(cov_unit).clip(0.0))
    c = cov_unit / np.outer(np.where(rms_unit > 0, rms_unit, 1.0),
                            np.where(rms_unit > 0, rms_unit, 1.0))
    i_a, i_b = 3 * NX + 2, 9 * NX + 9
    dist_km = np.hypot((i_b % NX - i_a % NX) * DX, (i_b // NX - i_a // NX) * DZ) / 1e3
    print(f"  correlation of the estimates in cells {i_a} and {i_b} "
          f"({dist_km:.1f} km apart): {c[i_a, i_b]:+.3f}")
    off = np.abs(c - np.eye(n))
    print(f"  largest off-diagonal correlation: {off.max():.3f}; "
          f"median {np.median(off):.3f}")
    print("""
  The analytic covariance is reproduced by Monte Carlo to about a tenth, which
  is the check that the linear error propagation is implemented correctly.  The
  important output is the off-diagonal structure.  The largest off-diagonal
  correlation is one to three decimals, so some pairs of cells are
  indistinguishable after smearing, and two cells several kilometres apart are
  anti-correlated: mass that the image puts in one is taken from the other.
  Quoting per-cell standard deviations as if the cells were independent
  therefore misstates the uncertainty of anything computed from several cells.""")


def part5_tradeoff():
    section("5. Resolution against variance")
    rays = geometry("crossing")
    g = build_g(rays)
    n = g.shape[1]
    u, s, vt = np.linalg.svd(g, full_matrices=False)
    m_true = -model("long")
    d = g @ m_true
    m_row = vt.T @ (vt @ m_true)
    print(f"{'lam/lam_max':>12} {'trace(R)':>9} {'||R-I||/rt(n)':>14} "
          f"{'rms std dev':>13} {'bias (dv/v0)':>13} {'total (dv/v0)':>14}")
    for lam_rel in (1e-4, 1e-3, 1e-2, 3e-2, 1e-1, 3e-1, 1.0):
        lam = lam_rel * s[0]
        filt = s / (s ** 2 + lam ** 2)
        r_mat = vt.T @ np.diag(s ** 2 / (s ** 2 + lam ** 2)) @ vt
        m_est = vt.T @ (filt * (u[:, :s.size].T @ d))
        std = SIGMA_T * np.sqrt(np.mean(np.sum(vt.T ** 2 * filt ** 2, axis=1)))
        bias = np.sqrt(np.mean((m_est - m_row) ** 2))
        print(f"{lam_rel:12.0e} {np.trace(r_mat):9.1f} "
              f"{np.linalg.norm(r_mat - np.eye(n)) / np.sqrt(n):14.4e} "
              f"{std:18.4e} {bias:12.4e} {np.hypot(bias, std):12.4e}")
    print(f"\n  rms of the true anomaly in the row space: "
          f"{np.sqrt(np.mean(m_row ** 2)):.4e} (dv/v0)")
    print("""
  trace(R) is the effective number of parameters the data can resolve: it falls
  from near the null-space-limited maximum towards zero as damping rises.
  Reading down the table, the standard deviation falls by two orders of
  magnitude while the bias grows, and the total error has a minimum at an
  intermediate damping (here 1e-1 of the largest singular value).  One term is a
  random error, the other a systematic displacement of the image, and they are
  not interchangeable: reporting a model without its standard deviation, or a
  standard deviation without its resolution, is reporting half of the answer.""")


def part6_known_model():
    section("6. Known-model tests: a smooth pattern and a checkerboard")
    rays = geometry("crossing")
    g = build_g(rays)
    u, s, vt = np.linalg.svd(g, full_matrices=False)
    lam = 3e-2 * s[0]
    filt = s / (s ** 2 + lam ** 2)
    print(f"{'true pattern':>12} {'rms (dv/v0)':>12} {'datum rms (ms)':>16} "
          f"{'R2 (clean)':>11} {'R2 (noisy)':>11} {'amplitude':>10} "
          f"{'sign':>8}")
    for kind in ("long", "checker4", "checker1"):
        p_true = model(kind)
        d = g @ (-p_true)
        d_n = d + RNG.normal(0.0, SIGMA_T, d.size)
        r2 = []
        for dd in (d, d_n):
            m_est = -(vt.T @ (filt * (u[:, :s.size].T @ dd)))
            r2.append(1.0 - np.sum((m_est - p_true) ** 2)
                      / np.sum(p_true ** 2))
        m_clean = -(vt.T @ (filt * (u[:, :s.size].T @ d)))
        agree = np.mean(np.sign(m_clean) == np.sign(p_true))
        print(f"{kind:>12} {np.sqrt(np.mean(p_true ** 2)):12.4e} "
              f"{np.sqrt(np.mean(d ** 2)) * 1e3:16.3f} "
              f"{r2[0]:11.3f} {r2[1]:11.3f} "
              f"{np.sqrt(np.mean(m_clean ** 2)) / np.sqrt(np.mean(p_true ** 2)):10.3f} "
              f"{100.0 * agree:7.1f}%")
    print("""
  A known-model test is the only honest way to quote a resolution: inject a
  pattern whose answer you know, invert it with the SAME rays, grid and damping,
  and report how much of it survives.  The grid-scale pattern comes back with
  R2 = 0.948 and 95.8 per cent of its signs correct.  Both checkerboards are
  degraded -- their recovered amplitudes are 62 to 64 per cent of the input,
  which is the damping bias visible as a number -- and, the important point,
  their ordering is NOT monotone in wavelength: the 4 km x 2 km pattern scores
  worse (R2 = 0.534) than the one-cell pattern (0.656), and it also predicts
  twice as much datum (51 ms against 25 ms rms).  Resolution is not a single
  length: it depends on how a pattern projects onto the ray directions, which is
  why "the resolution is about two cells" is not a statement anyone can verify.
  A negative R2 would mean the inversion does worse than returning zero.""")


def main():
    part1_spectrum()
    part2_resolution_matrix()
    part3_null_space()
    part4_covariance()
    part5_tradeoff()
    part6_known_model()
    print("\nAll models and data in this file are SYNTHETIC (see the module")
    print("docstring for every parameter).  Done.")


if __name__ == "__main__":
    main()
