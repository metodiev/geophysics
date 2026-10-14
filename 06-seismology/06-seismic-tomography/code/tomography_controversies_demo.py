#!/usr/bin/env python3
"""Why two tomographic models of the same region disagree: resolution, damping
and the difference between a model and the Earth.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tomography_controversies_demo.py

Requires: numpy.  Print-only; no figures, no network.

Companion to lesson 06-06-07.  Everything is SYNTHETIC: a 16 km x 5.5 km
cross-hole region with a 16 x 12 cell grid (192 parameters), a homogeneous
3000 m/s reference, two acquisitions (a full crossing one and a one-sided one),
straight rays and a 5 ms travel-time noise level.  No published model, station
or data set is used.

Contents
--------
1. Two models from the same synthetic Earth, built from two different ray sets.
2. Where the two models agree and where they do not: resolution, cell by cell.
3. Amplitudes: the recovered anomaly is a fraction of the true one, and the
   fraction depends on the damping.
4. The same data inverted with two dampings: disagreement without any data
   difference at all.
5. Combining the two data sets: what agreement is worth.
6. A vote map: the fraction of models that agree on the sign, cell by cell.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

X0, X1 = 0.2e3, 15.8e3
Z_TOP, Z_BOT = 0.25e3, 5.75e3
V_REF = 3000.0
NX, NZ = 16, 12
DX, DZ = (X1 - X0) / NX, (Z_BOT - Z_TOP) / NZ
SIGMA_T = 5.0e-3


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def cell_lengths(p, q, n=1200):
    t = np.linspace(0.0, 1.0, n)
    xs = p[0] + (q[0] - p[0]) * t
    zs = p[1] + (q[1] - p[1]) * t
    col = np.clip((xs / DX).astype(int), 0, NX - 1)
    row = np.clip((zs / DZ).astype(int), 0, NZ - 1)
    seg = np.hypot(q[0] - p[0], q[1] - p[1]) / (n - 1)
    out = np.zeros(NX * NZ)
    np.add.at(out, row * NX + col, seg)
    return out


def rays_crossing():
    src = np.column_stack([np.full(12, X0), np.linspace(Z_TOP, Z_BOT, 12)])
    rec = np.column_stack([np.full(12, X1), np.linspace(Z_TOP, Z_BOT, 12)])
    return [(s, r) for s in src for r in rec]


def rays_onesided():
    src = np.column_stack([np.full(10, X0), np.linspace(Z_TOP, 0.5 * Z_BOT, 10)])
    rec = np.column_stack([np.full(10, X1), np.linspace(0.5 * Z_BOT, Z_BOT, 10)])
    return [(s, r) for s in src for r in rec]


def jacobian(rays):
    return np.array([cell_lengths(s, r) for s, r in rays]) / V_REF


def true_model():
    """Relative velocity perturbation dv/v0: one blob and one gradient."""
    xc = (np.arange(NX) + 0.5) * DX
    zc = (np.arange(NZ) + 0.5) * DZ
    zz, xx = np.meshgrid(zc, xc, indexing="ij")
    blob = 0.06 * np.exp(-((xx - 4.5e3) ** 2 + (zz - 1.5e3) ** 2)
                         / (2.0 * (2.4e3) ** 2))
    ramp = 0.02 * (zz - Z_TOP) / (Z_BOT - Z_TOP)
    return (blob + ramp).ravel()


def solve(g, d, lam):
    return np.linalg.lstsq(np.vstack([g, lam * np.eye(g.shape[1])]),
                           np.concatenate([d, np.zeros(g.shape[1])]),
                           rcond=None)[0]


def velocity_perturbation(m):
    """Convert a slowness perturbation to dv/v0 (first order)."""
    return -m


def corr(a, b):
    if np.std(a) == 0 or np.std(b) == 0:
        return float("nan")
    return float(np.corrcoef(a, b)[0, 1])


def part1_two_models():
    section("1. Two models of the same Earth")
    p_true = true_model()
    out = {}
    for name, rays in (("crossing", rays_crossing()),
                       ("one-sided", rays_onesided())):
        g = jacobian(rays)
        d = g @ (-p_true) + RNG.normal(0.0, SIGMA_T, len(rays))
        lam_rel = 3e-2 if name == "crossing" else 3e-2
        m = solve(g, d, lam_rel * np.linalg.norm(g))
        cover = (g > 0).sum(axis=0)
        out[name] = (velocity_perturbation(m), cover, len(rays))
        print(f"  {name:>10}: {len(rays):3d} rays, cells with no ray "
              f"{int(np.sum(cover == 0)):3d}, rms model "
              f"{np.sqrt(np.mean(m ** 2)):.4e} (dv/v0)")
    a, cover, _ = out["crossing"]
    b, _, _ = out["one-sided"]
    print(f"\n  correlation of the two models, all cells      : {corr(a, b):+.3f}")
    print(f"  rms difference between them                   : "
          f"{np.sqrt(np.mean((a - b) ** 2)):.4e} (dv/v0)")
    print(f"  rms of the true anomaly                       : "
          f"{np.sqrt(np.mean(p_true ** 2)):.4e} (dv/v0)")
    print(f"  rms of the difference as a fraction of the model: "
          f"{np.sqrt(np.mean((a - b) ** 2)) / np.sqrt(np.mean(p_true ** 2)):.3f}")
    print(f"  correlation of each model with the truth      : "
          f"{corr(a, p_true):+.3f} and {corr(b, p_true):+.3f}")
    print("""
  Two inversions of the SAME synthetic Earth with different rays are correlated
  but not equal, and the difference between them is a substantial fraction of
  the anomaly they both claim to have found.  Nothing here is an error in either
  inversion: the data are different, so the null spaces are different, and each
  model is the minimum-norm answer in its own null space.""")


def part2_where():
    section("2. Where the two models agree")
    p_true = true_model()
    a, cover, n_ray = None, None, 0
    models = {}
    for name, rays in (("crossing", rays_crossing()),
                       ("one-sided", rays_onesided())):
        g = jacobian(rays)
        d = g @ (-p_true) + RNG.normal(0.0, SIGMA_T, len(rays))
        models[name] = velocity_perturbation(solve(g, d, 3e-2 * np.linalg.norm(g)))
        if name == "crossing":
            cover = (g > 0).sum(axis=0)
    a, b = models["crossing"], models["one-sided"]
    lo = cover < np.percentile(cover, 25)
    hi = cover > np.percentile(cover, 75)
    print(f"  cells split by how many rays cross them: worst quarter "
          f"({cover[lo].min()}-{cover[lo].max()} rays) and best quarter "
          f"({cover[hi].min()}-{cover[hi].max()} rays)\n")
    print(f"{'subset':>28} {'correlation':>12} {'rms difference':>15} "
          f"{'cells':>7}")
    for name, sel in (("worst-covered quarter", lo),
                      ("best-covered quarter", hi),
                      ("all cells", np.ones(NX * NZ, dtype=bool))):
        print(f"{name:>28} {corr(a[sel], b[sel]):12.3f} "
              f"{np.sqrt(np.mean((a[sel] - b[sel]) ** 2)):15.4e} "
              f"{int(sel.sum()):7d}")
    print("""
  Model disagreement is not uniform: it concentrates where the ray coverage is
  poor.  This is the single most useful diagnostic for reading a discrepancy
  map, because it converts a vague question ("why do the models differ?") into a
  computable one ("is the difference larger than the resolution in that cell?").""")


def part3_amplitude():
    section("3. Amplitudes are a fraction of the truth, and the fraction is a choice")
    p_true = true_model()
    rays = rays_crossing()
    g = jacobian(rays)
    d = g @ (-p_true)
    print(f"  true anomaly: rms {np.sqrt(np.mean(p_true ** 2)):.4e} (dv/v0), "
          f"peak {p_true.max():.4f}")
    u, s, vt = np.linalg.svd(g, full_matrices=False)
    rank = int(np.sum(s > 1e-9 * s[0]))
    p_row = vt[:rank].T @ (vt[:rank] @ p_true)
    print(f"  the best any inversion of these rays could do: rank {rank} of "
          f"{g.shape[1]}")
    print(f"  row-space part of the anomaly correlates with the whole anomaly at")
    print(f"  only {corr(p_row, p_true):+.3f}\n")
    print(f"{'lam/||G||':>10} {'misfit (s)':>12} {'recovered rms':>14} "
          f"{'fraction of truth':>18} {'correlation':>12}")
    for lam_rel in (1e-3, 1e-2, 3e-2, 1e-1, 3e-1):
        m = solve(g, d, lam_rel * np.linalg.norm(g))
        p_est = velocity_perturbation(m)
        print(f"{lam_rel:10.1e} "
              f"{np.sqrt(np.mean((g @ m - d) ** 2)):12.3e} "
              f"{np.sqrt(np.mean(p_est ** 2)):14.4e} "
              f"{np.sqrt(np.mean(p_est ** 2)) / np.sqrt(np.mean(p_true ** 2)):18.3f} "
              f"{corr(p_est, p_true):12.3f}")
    print("""
  The recovered rms falls by a factor of two across these legitimate answers,
  and the correlation with the truth falls with it: no damping is more accurate
  in both senses at once.  Note the line above: the recoverable part of this
  anomaly is itself only weakly correlated with the whole anomaly, because most
  of it lies in the null space of this limited-angle geometry.  Amplitude and
  structure are both partly a choice of damping, and a paper that quotes an
  anomaly without its damping rule has quoted a number nobody can reproduce.""")


def part4_same_data():
    section("4. Disagreement with no difference in the data at all")
    p_true = true_model()
    rays = rays_crossing()
    g = jacobian(rays)
    d = g @ (-p_true) + RNG.normal(0.0, SIGMA_T, len(rays))
    m1 = velocity_perturbation(solve(g, d, 1e-2 * np.linalg.norm(g)))
    m2 = velocity_perturbation(solve(g, d, 3e-1 * np.linalg.norm(g)))
    print(f"  the same {len(rays)} travel times, the same code, two damping "
          f"values:")
    print(f"    lam = 1e-2 ||G|: rms model {np.sqrt(np.mean(m1 ** 2)):.4e}")
    print(f"    lam = 3e-1 ||G|: rms model {np.sqrt(np.mean(m2 ** 2)):.4e}")
    print(f"    correlation between the two          : {corr(m1, m2):+.3f}")
    print(f"    rms difference                       : "
          f"{np.sqrt(np.mean((m1 - m2) ** 2)):.4e} (dv/v0), "
          f"{100.0 * np.sqrt(np.mean((m1 - m2) ** 2)) / np.sqrt(np.mean(p_true ** 2)):.0f} "
          f"per cent of the true anomaly")
    print(f"    correlation with the truth           : "
          f"{corr(m1, p_true):+.3f} and {corr(m2, p_true):+.3f}")
    print("""
  The same data, the same rays, the same code, one different number -- and the
  two images differ by more than half the rms of the true anomaly.  A published
  disagreement of this size need not be evidence about the Earth at all: it is
  evidence about the two inversions first, and untangling the two is the work.""")


def part5_combine():
    section("5. What combining the data sets is worth")
    p_true = true_model()
    r1, r2 = rays_crossing(), rays_onesided()
    g1, g2 = jacobian(r1), jacobian(r2)
    d1 = g1 @ (-p_true) + RNG.normal(0.0, SIGMA_T, len(r1))
    d2 = g2 @ (-p_true) + RNG.normal(0.0, SIGMA_T, len(r2))
    m1 = velocity_perturbation(solve(g1, d1, 3e-2 * np.linalg.norm(g1)))
    m2 = velocity_perturbation(solve(g2, d2, 3e-2 * np.linalg.norm(g2)))
    g = np.vstack([g1, g2])
    d = np.concatenate([d1, d2])
    mj = velocity_perturbation(solve(g, d, 3e-2 * np.linalg.norm(g)))
    mc = velocity_perturbation(solve(g1, d1, 3e-2 * np.linalg.norm(g1)))
    print(f"  separate inversions : correlation {corr(m1, m2):+.3f}, "
          f"rms difference {np.sqrt(np.mean((m1 - m2) ** 2)):.4e}")
    print(f"  joint inversion     : correlation {corr(mj, mc):+.3f}, "
          f"rms difference {np.sqrt(np.mean((mj - mc) ** 2)):.4e}")
    print(f"  each single model against the truth: "
          f"{corr(m1, p_true):+.3f} and {corr(m2, p_true):+.3f}")
    print(f"  joint model against the truth      : {corr(mj, p_true):+.3f}")
    print(f"  rms error, crossing alone  : "
          f"{np.sqrt(np.mean((m1 - p_true) ** 2)):.4e}")
    print(f"  rms error, one-sided alone : "
          f"{np.sqrt(np.mean((m2 - p_true) ** 2)):.4e}")
    print(f"  rms error, joint           : "
          f"{np.sqrt(np.mean((mj - p_true) ** 2)):.4e}")
    print("""
  Combining the two data sets collapses the DISAGREEMENT while barely changing
  the error against the truth.  That is the most useful thing to understand
  about a joint inversion: it does not conjure up the missing angular coverage,
  but it does remove the part of the model that was unconstrained in one
  geometry and arbitrary in the other.  Agreement and accuracy are different
  quantities, and combining data improves one of them.""")


def part6_vote_map():
    section("6. A vote map: how many models agree on the sign")
    p_true = true_model()
    rays = rays_crossing()
    g = jacobian(rays)
    d0 = g @ (-p_true)
    lam_grid = np.array([3e-3, 1e-2, 3e-2, 1e-1, 3e-1])
    signs = []
    for lam_rel in lam_grid:
        for trial in range(6):
            d = d0 + RNG.normal(0.0, SIGMA_T, len(rays))
            m = velocity_perturbation(solve(g, d, lam_rel * np.linalg.norm(g)))
            signs.append(np.sign(m))
    signs = np.array(signs)
    frac = np.abs(signs.mean(axis=0))
    cover = (g > 0).sum(axis=0)
    print(f"  {len(signs)} models = {len(lam_grid)} damping values x 6 noise "
          f"realisations, same rays and same true Earth\n")
    print(f"{'subset':>34} {'mean agreement':>15} {'worst cell':>12} "
          f"{'cells':>7}")
    for name, sel in (("best-covered quarter of cells",
                       cover > np.percentile(cover, 75)),
                      ("worst-covered quarter of cells",
                       cover < np.percentile(cover, 25)),
                      ("all cells", np.ones(NX * NZ, dtype=bool))):
        print(f"{name:>34} {frac[sel].mean():15.3f} {frac[sel].min():12.3f} "
              f"{int(sel.sum()):7d}")
    print("""
  The sign is the robust part of a tomographic image: over 30 models that differ
  in damping and in noise realisation the sign of the anomaly is agreed on
  almost everywhere, and only slightly less often in the worst-covered cells,
  while the amplitudes of the same models differ by factors of two.  A vote map
  is therefore a cheap honest summary of an ensemble: quote the sign where
  everything agrees, and quote the ensemble, with its amplitudes, where it does
  not.""")


def main():
    print("SYNTHETIC two-dimensional experiment:")
    print(f"  region {(X1 - X0) / 1e3:.0f} km x {(Z_BOT - Z_TOP) / 1e3:.1f} km, "
          f"grid {NX} x {NZ} = {NX * NZ} cells, reference {V_REF:.0f} m/s")
    print(f"  two acquisitions, straight rays, travel-time noise "
          f"{SIGMA_T * 1e3:.1f} ms")
    part1_two_models()
    part2_where()
    part3_amplitude()
    part4_same_data()
    part5_combine()
    part6_vote_map()
    print("\nAll models and data in this file are SYNTHETIC (see the module")
    print("docstring for every parameter).  Done.")


if __name__ == "__main__":
    main()
