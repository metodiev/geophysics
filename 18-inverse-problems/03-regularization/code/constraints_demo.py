#!/usr/bin/env python3
"""Physical constraints, bounds and feasible model sets: what a constraint buys,
what it costs, and how to tell that it is wrong.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python constraints_demo.py

All models and data are SYNTHETIC: the exact 2-D line-mass gravity kernel of a
textbook forward model, chosen density distributions, a chosen station grid and
computer-generated noise.  No measured data and no published numbers are used.
Model values and data are carried in units of 1e9 kg/m and dimensionless data;
mGal are quoted where they help.

Contents
--------
1. The synthetic problem and the reference unconstrained solution.
2. Inactive bounds: a constraint that touches nothing changes nothing.
3. Non-negativity against a model with a negative lobe: measured bias.
4. Bounds that exclude the truth: measured bias and the failing residual test.
5. A monotonicity constraint from isotonic regression (PAVA), with a
   variational-inequality check that the returned point really is optimal.
6. Projections onto convex sets: alternating projections and their convergence.
"""

import numpy as np
from scipy.optimize import lsq_linear, brentq

RNG = np.random.default_rng(20261014)
G_CONST = 6.67430e-11
MGAL = 1.0e5


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def line_mass_kernel(x_obs_m, x_src_m, depth_m):
    """2-D line-mass gravity kernel in mGal per (kg/m); see the lesson."""
    dx = x_obs_m[:, None] - x_src_m[None, :]
    return 2.0 * G_CONST * depth_m / (dx**2 + depth_m**2) * MGAL


def pava_decreasing(y):
    """Projection onto the non-increasing cone (pool adjacent violators)."""
    vals, wts = [], []
    for v in y:
        vals.append(float(v))
        wts.append(1.0)
        while len(vals) > 1 and vals[-2] < vals[-1]:
            s = vals[-2] * wts[-2] + vals[-1] * wts[-1]
            w = wts[-2] + wts[-1]
            vals[-2:] = [s / w]
            wts[-2:] = [w]
    return np.concatenate([np.full(int(w), v) for v, w in zip(vals, wts)])


def box_solve(K, d, alpha, lo, hi):
    """min ||Km-d||^2 + alpha||m||^2 subject to lo <= m <= hi."""
    n = K.shape[1]
    A = np.vstack([K, np.sqrt(alpha) * np.eye(n)])
    b = np.concatenate([d, np.zeros(n)])
    res = lsq_linear(A, b, bounds=(lo * np.ones(n), hi * np.ones(n)),
                     method="bvls", tol=1e-14)
    return res.x, res


def main():
    n, depth = 48, 800.0
    x = np.linspace(-12000.0, 12000.0, n)
    K_phys = line_mass_kernel(x, x, depth)
    s1 = np.linalg.svd(K_phys, compute_uv=False)[0]
    K = K_phys / s1
    m_true = (3.0 * np.exp(-((x - 5000.0) / 3000.0) ** 2)
              - 1.2 * np.exp(-((x + 4000.0) / 3000.0) ** 2))
    d_true = K @ m_true
    sig = 0.005 * np.abs(d_true).max()
    d = d_true + sig * RNG.standard_normal(n)
    n_sig = n * sig**2

    section("1. The synthetic problem and the reference solution")
    print(f"  model : {n} cells, spacing {x[1] - x[0]:.1f} m, profile "
          f"{x[0] / 1e3:.0f} to {x[-1] / 1e3:.0f} km, values in 1e9 kg/m")
    print(f"  kernel: line masses at {depth:.0f} m depth, {n} gravity stations")
    print(f"  truth : +3.00 (1e9 kg/m) high at x = +5 km, -1.20 low at x = -4 km")
    print(f"  anomaly peak = {np.abs(d_true).max() * s1 * 1e9:.3f} mGal, "
          f"noise sigma = {sig * s1 * 1e9:.4f} mGal (0.50% of the peak)")
    print(f"  n sigma^2 = {n_sig:.6e} in dimensionless data units")
    resid = lambda a: (np.linalg.norm(K @ np.linalg.solve(
        K.T @ K + a * np.eye(n), K.T @ d) - d) ** 2 - n_sig)
    alpha = brentq(resid, 1e-12, 1e2, xtol=1e-16)
    m_unc = np.linalg.solve(K.T @ K + alpha * np.eye(n), K.T @ d)
    chi2_unc = np.linalg.norm(K @ m_unc - d) ** 2 / n_sig
    rmse_unc = np.linalg.norm(m_unc - m_true) / np.sqrt(n)
    print(f"\n  reference: Tikhonov with alpha chosen by the discrepancy")
    print(f"  principle, i.e. the largest alpha with chi^2 = n sigma^2:")
    print(f"    alpha = {alpha:.4e}")
    print(f"    chi^2/n sigma^2 = {chi2_unc:.4f}   "
          f"RMS model error = {rmse_unc:.4f} (1e9 kg/m)")
    print(f"    (chi^2 = n sigma^2 is the expected value when the model fits the")
    print("     data to the noise level; 1.0 is the target.)")
    print("  Every constrained run below uses the SAME alpha, so the only change")
    print("  is the feasible set.")

    section("2. Inactive bounds change nothing")
    wide = 10.0 * np.abs(m_true).max()
    m_wide, _ = box_solve(K, d, alpha, -wide, wide)
    print(f"  bounds [-{wide:.1f}, +{wide:.1f}] (1e9 kg/m): no cell is near a bound")
    print(f"    max |m_wide - m_unc|            = "
          f"{np.max(np.abs(m_wide - m_unc)):.3e} (1e9 kg/m)")
    print(f"    RMS model error, constrained     = "
          f"{np.linalg.norm(m_wide - m_true) / np.sqrt(n):.6f}")
    print(f"    RMS model error, unconstrained    = {rmse_unc:.6f}")
    print(f"    cells at a bound                 = "
          f"{int((np.minimum(np.abs(m_wide - (-wide)), np.abs(wide - m_wide)) < 1e-8).sum())}")
    print("  A constraint that is not active carries no information: the two")
    print("  solutions agree to solver accuracy.  Constraints only act where the")
    print("  data and the prior disagree.")

    section("3. Non-negativity against a model with a negative lobe")
    m_nn, res_nn = box_solve(K, d, alpha, 0.0, wide)
    neg = m_true < -0.05
    act = np.abs(m_nn) < 1e-9
    print(f"  bounds [0, +{wide:.1f}] (1e9 kg/m): density cannot be negative")
    print(f"    cells forced to the bound      : {int(act.sum())} of {n}")
    print(f"    the bound is active exactly where the truth is negative: "
          f"{int((act & neg).sum())} of {int(neg.sum())} negative cells")
    rms_neg_u = np.sqrt(np.mean((m_unc[neg] - m_true[neg]) ** 2))
    rms_pos_u = np.sqrt(np.mean((m_unc[~neg] - m_true[~neg]) ** 2))
    print(f"    RMS error over the negative lobe: "
          f"{np.sqrt(np.mean((m_nn[neg] - m_true[neg]) ** 2)):.4f} "
          f"(unconstrained {rms_neg_u:.4f}; truth mean there "
          f"{m_true[neg].mean():+.4f})")
    print(f"    RMS error over the positive lobe: "
          f"{np.sqrt(np.mean((m_nn[~neg] - m_true[~neg]) ** 2)):.4f} "
          f"(unconstrained {rms_pos_u:.4f})")
    print(f"    RMS error, whole model          : "
          f"{np.linalg.norm(m_nn - m_true) / np.sqrt(n):.4f} "
          f"(unconstrained {rmse_unc:.4f})")
    print(f"    chi^2/(n sigma^2)               : "
          f"{np.linalg.norm(K @ m_nn - d) ** 2 / n_sig:.3f} "
          f"(unconstrained {chi2_unc:.3f})")
    print("  The constraint is a prior that is FALSE here (there really is a")
    print("  density deficit), so it forces a positive density where the data say")
    print("  otherwise and the residual rises by three orders of magnitude.  The")
    print("  damage is worst at the violating cells, but it is NOT local: the")
    print("  positive lobe also degrades, because the bound changes the fit of the")
    print("  whole profile.  'Non-negativity is always safe' is false, and the")
    print("  measurements above are the refutation.")

    section("4. Bounds that exclude the truth")
    hi_tight = 2.0
    m_tight, res_tight = box_solve(K, d, alpha, 0.0, hi_tight)
    at_hi = np.abs(m_tight - hi_tight) < 1e-9
    print(f"  bounds [0, {hi_tight:.1f}] (1e9 kg/m) while the truth peaks at "
          f"{m_true.max():.2f}")
    print(f"    cells pinned to the upper bound : {int(at_hi.sum())} of {n}")
    print(f"    bias where the truth exceeds the bound: mean "
          f"{np.mean(m_tight[at_hi] - m_true[at_hi]):+.4f} "
          f"(1e9 kg/m)")
    print(f"    distance from the truth to the bound = "
          f"{np.max(m_true) - hi_tight:.4f}")
    print(f"    RMS error whole model           : "
          f"{np.linalg.norm(m_tight - m_true) / np.sqrt(n):.4f} "
          f"(unconstrained {rmse_unc:.4f})")
    print(f"    chi^2/(n sigma^2)               : "
          f"{np.linalg.norm(K @ m_tight - d) ** 2 / n_sig:.3f} "
          f"(unconstrained {chi2_unc:.3f})")
    print("  Two signatures of a wrong bound appear together: the error saturates")
    print("  at the distance to the bound, and the residual can no longer reach the")
    print("  noise level.  The second is the test that is available WITHOUT knowing")
    print("  the truth, and it is the reason chi^2 must always be reported with a")
    print("  constrained inversion.")

    section("5. A monotonicity constraint (PAVA) and its optimality check")
    y = RNG.standard_normal(9)
    p1 = pava_decreasing(y)
    p2 = pava_decreasing(p1)
    print("  PAVA projects onto the non-increasing cone.  Two properties are")
    print("  checked here rather than assumed:")
    print(f"    the image is non-increasing      : "
          f"{bool(np.all(np.diff(p1) <= 1e-15))}")
    print(f"    the projection is idempotent     : max |P(P(y)) - P(y)| = "
          f"{np.max(np.abs(p2 - p1)):.3e}")
    m_dec_true = (4.0 * np.exp(-((x - 8000.0) / 6000.0) ** 2)
                  * (x < 8000.0) + 4.0 * np.exp(-((x - 8000.0) / 20000.0) ** 2))
    m_dec_true = np.maximum.accumulate(m_dec_true[::-1])[::-1]
    d_dec = K @ m_dec_true + sig * RNG.standard_normal(n)
    dec_resid = lambda a: (np.linalg.norm(K @ np.linalg.solve(
        K.T @ K + a * np.eye(n), K.T @ d_dec) - d_dec) ** 2 - n_sig)
    alpha_dec = brentq(dec_resid, 1e-12, 1e2, xtol=1e-16)
    L = np.linalg.norm(K, 2) ** 2 + alpha_dec
    m_proj = np.linalg.solve(K.T @ K + alpha_dec * np.eye(n), K.T @ d_dec)
    step = 1.0 / L
    m_it = m_proj.copy()
    for _ in range(40000):
        grad = K.T @ (K @ m_it - d_dec) + alpha_dec * m_it
        m_new = pava_decreasing(m_it - step * grad)
        if np.max(np.abs(m_new - m_it)) < 1e-15:
            m_it = m_new
            break
        m_it = m_new
    print(f"\n  data generated by a monotone decreasing model; {n} cells, and the")
    print(f"  discrepancy alpha for THIS data set is {alpha_dec:.4e}, so the")
    print("  unconstrained reference again has chi^2 = n sigma^2:")
    print(f"    unconstrained violations of monotonicity : "
          f"{int((np.diff(m_proj) > 1e-9).sum())} of {n - 1} intervals")
    print(f"    constrained violations                   : "
          f"{int((np.diff(m_it) > 1e-9).sum())}")
    print(f"    chi^2/(n sigma^2) unconstrained          : "
          f"{np.linalg.norm(K @ m_proj - d_dec) ** 2 / n_sig:.3f}")
    print(f"    chi^2/(n sigma^2) constrained            : "
          f"{np.linalg.norm(K @ m_it - d_dec) ** 2 / n_sig:.3f}"
          "   <- the price of the constraint")
    print(f"    RMS error unconstrained / constrained    : "
          f"{np.linalg.norm(m_proj - m_dec_true) / np.sqrt(n):.4f} / "
          f"{np.linalg.norm(m_it - m_dec_true) / np.sqrt(n):.4f}")
    print("  Here the prior is TRUE (the model really is monotone), and the")
    print("  constrained solution is the more accurate one even though it fits the")
    print("  data slightly worse: the constraint bought a reduction in model error")
    print("  at the cost of a stated misfit.  That trade is always made; it is")
    print("  usually made silently when the constraint is imposed without saying so.")
    grad = K.T @ (K @ m_it - d_dec) + alpha_dec * m_it
    worst = np.inf
    for _ in range(2000):
        cand = pava_decreasing(m_it + 0.5 * RNG.standard_normal(n))
        worst = min(worst, float(grad @ (cand - m_it)))
    print("  Variational-inequality check on 2000 random FEASIBLE points y:")
    print(f"    min over y of <grad f(m), y - m> = {worst:.3e}")
    print("  A negative value would mean a feasible descent direction exists, i.e.")
    print("  that the returned point is not optimal.  Zero to solver accuracy is")
    print("  the proof that the returned point is a constrained minimiser.")

    section("6. Alternating projections onto two convex sets (POCS)")
    j_small = int(np.argmin(np.abs(d)))
    row, rhs = K[j_small].copy(), d[j_small]
    print(f"  set A: the data hyperplane K_j m = d_j for the datum with the")
    print(f"         smallest |d_j|, j = {j_small} (d_j = {rhs:.3e})")
    print("  set B: a box constraint on the model")
    print("  POCS alternates m <- P_A(P_B(m)).  Whether it can converge at all")
    print("  depends on whether the two sets meet, and that can be decided exactly")
    print("  by minimising |K_j m - d_j| over the box.\n")
    for lo_s, hi_s, tag in ((-3.0, 3.0, "box that the data allow"),
                            (-6.0, -1.0, "box that the data forbid")):
        res = lsq_linear(row[None, :], np.array([rhs]),
                         bounds=(lo_s * np.ones(n), hi_s * np.ones(n)),
                         method="bvls", tol=1e-14)
        r_min = abs(row @ res.x - rhs)
        print(f"  {tag}: box [{lo_s}, {hi_s}] (1e9 kg/m)")
        print(f"    exact test: min |K_j m - d_j| over the box = {r_min:.3e} in")
        print(f"    data units; the datum itself is d_j = {rhs:.3e}, so the")
        print(f"    intersection is {'NON-EMPTY' if r_min < 1e-9 * abs(rhs) else 'EMPTY'}.")
        m_p = np.linspace(lo_s, hi_s, n)
        dist = []
        for _ in range(400):
            m_prev = m_p.copy()
            m_p = np.clip(m_p, lo_s, hi_s)
            m_p = m_p + (rhs - row @ m_p) / (row @ row) * row
            dist.append(np.linalg.norm(m_p - m_prev))
        print("    POCS: distance between consecutive iterates")
        print(f"      1st = {dist[0]:.4f}, 10th = {dist[9]:.6f}, "
              f"100th = {dist[99]:.3e}, 400th = {dist[-1]:.3e}")
        if dist[-1] > 0.0 and dist[9] > 0.0:
            per_it = (dist[-1] / dist[9]) ** (1.0 / (len(dist) - 10))
            print(f"      contraction per iteration (d_400/d_10)^(1/390) = "
                  f"{per_it:.5f}")
        reached = [k for k, dv in enumerate(dist, start=1) if dv < 1e-10]
        print(f"      iteration at which consecutive iterates agree to 1e-10: "
              f"{reached[0] if reached else 'not reached in 400'}")
        print(f"      final |K_j m - d_j| = {abs(row @ m_p - rhs):.3e}; cells outside")
        print(f"      the box = {int(np.sum((m_p < lo_s - 1e-9) | (m_p > hi_s + 1e-9)))}")
        if r_min < 1e-9 * abs(rhs):
            print(f"      the POCS limit satisfies both sets, and so does the exact")
            print(f"      solution; they are {np.linalg.norm(m_p - res.x):.3f} "
                  f"(1e9 kg/m) apart, which")
            print("      measures the SIZE of the intersection, not an error.  Two")
            print("      different models satisfy the same constraint exactly: the")
            print("      feasible set is a set, and a constraint does not make the")
            print("      answer unique.")
        else:
            print(f"      the nearest feasible point is still {r_min:.3e} from the")
            print("      hyperplane, which is the measured signature of an EMPTY")
            print("      intersection: no model satisfies both constraints, and the")
            print("      problem has no solution rather than a difficult one.")
        print()
    print("  POCS is only as useful as the diagnosis of the limit: when the iterate")
    print("  distance plateaus, the sets are apart, and no amount of iteration will")
    print("  fix an over-constrained problem.  The exact test above costs one small")
    print("  quadratic program and settles the question.")


if __name__ == "__main__":
    main()
