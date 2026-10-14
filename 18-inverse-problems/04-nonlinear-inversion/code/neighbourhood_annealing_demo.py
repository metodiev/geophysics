#!/usr/bin/env python3
"""Neighbourhood and very fast simulated annealing, measured on a declared
synthetic objective: the neighbourhood algorithm's Voronoi-cell contraction, its
measured cell acceptance fraction, and a comparison with a Cauchy-proposal
annealer and with random search at equal forward-model cost.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python neighbourhood_annealing_demo.py

All models and data are SYNTHETIC.  The objective is a DECLARED test function --
Gaussian wells with a weak tilt -- standing in for a misfit surface whose true
form is not known in practice.

Contents
--------
1. The objective, its wells and the reference minimum.
2. The neighbourhood algorithm: cell contraction and measured acceptance.
3. Very fast simulated annealing with a Cauchy-like proposal.
4. Equal-cost comparison in two and four dimensions.
"""

import numpy as np

RNG = np.random.default_rng(20261014)
N_DIM_MAX = 4
SPREAD = 0.30
TOL = 0.05
_CENTRES = np.random.default_rng(53).uniform(-0.8, 0.8, size=(5, N_DIM_MAX))
_DEPTHS = np.array([1.0, 0.9, 0.8, 0.7, 0.6])
_TILT = np.random.default_rng(59).uniform(-0.3, 0.3, size=N_DIM_MAX)


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def objective(U, nd):
    U = np.atleast_2d(U)
    c = _CENTRES[:, :nd]
    d2 = ((U[:, None, :] - c[None, :, :]) ** 2).sum(axis=2)
    wells = (_DEPTHS[None, :] * np.exp(-d2 / (2.0 * SPREAD**2))).sum(axis=1)
    return 1.0 - wells + 0.05 * (U @ _TILT[:nd])


def val(u, nd):
    return float(objective(np.asarray(u).reshape(1, -1), nd)[0])


def ball_volume(r, nd):
    from math import gamma, pi
    return pi ** (nd / 2.0) / gamma(nd / 2.0 + 1.0) * r**nd


def uniform_ball(n_pts, r, nd, rng=RNG):
    direction = rng.standard_normal((n_pts, nd))
    direction /= np.linalg.norm(direction, axis=1, keepdims=True)
    radius = r * rng.random(n_pts) ** (1.0 / nd)
    return direction * radius[:, None]


def cell_acceptance(pts, best_idx, nd, n_draw=1000, rng=RNG):
    """Fraction of uniform candidates inside the best model's Voronoi cell."""
    cand = rng.uniform(-1.0, 1.0, size=(n_draw, nd))
    d_all = np.linalg.norm(cand[:, None, :] - pts[None, :, :], axis=2)
    return float(np.mean(np.argmin(d_all, axis=1) == best_idx))


def neighbourhood(nd, n_eval, n_initial=16, n_new=16, rng=RNG, keep=200,
                  probe_at=(1, 10, 40)):
    """The neighbourhood algorithm, sampling the inscribed ball of the best cell.

    Returns (best point, best value, forward evaluations, radius history,
    probe results as (generation, acceptance fraction, cell radius)).
    """
    pts = rng.uniform(-1.0, 1.0, size=(n_initial, nd))
    vals = objective(pts, nd)
    n_fwd = n_initial
    rad_hist, probes = [], []
    gen = 0
    while n_fwd < n_eval:
        gen += 1
        best_idx = int(np.argmin(vals))
        d_others = np.linalg.norm(pts - pts[best_idx], axis=1)
        d_others[best_idx] = np.inf
        r_ins = 0.5 * float(np.min(d_others))
        rad_hist.append(r_ins)
        if gen in probe_at:
            probes.append((gen, cell_acceptance(pts, best_idx, nd, rng=rng), r_ins))
        new_pts = np.clip(pts[best_idx][None, :]
                          + uniform_ball(n_new, max(r_ins, 1e-9), nd, rng),
                          -1.5, 1.5)
        pts = np.vstack([pts, new_pts])
        vals = np.concatenate([vals, objective(new_pts, nd)])
        n_fwd += n_new
        if pts.shape[0] > keep:
            keep_idx = np.argsort(vals)[: keep // 2]
            recent = np.arange(pts.shape[0] - keep // 2, pts.shape[0])
            sel = np.unique(np.concatenate([keep_idx, recent]))
            pts, vals = pts[sel], vals[sel]
    j = int(np.argmin(vals))
    return pts[j], float(vals[j]), n_fwd, rad_hist, probes


def vfsa(nd, n_eval, T0=0.5, rng=RNG):
    """Cauchy-like proposal with geometric cooling, Metropolis acceptance."""
    u = rng.uniform(-1.0, 1.0, nd)
    fu = val(u, nd)
    best, fb = u.copy(), fu
    for k in range(1, n_eval + 1):
        T = max(T0 * (0.995 ** k), 1e-6)
        r = rng.random(nd)
        sign = np.where(rng.random(nd) > 0.5, 1.0, -1.0)
        du = sign * T * ((1.0 + 1.0 / T) ** np.abs(2.0 * r - 1.0) - 1.0)
        cand = np.clip(u + du, -1.5, 1.5)
        fc = val(cand, nd)
        if fc < fu or rng.random() < np.exp(-(fc - fu) / T):
            u, fu = cand, fc
        if fu < fb:
            best, fb = u.copy(), fu
    return best, fb


def reference_minimum(nd, rng=RNG):
    best, fb = _CENTRES[0, :nd].copy(), val(_CENTRES[0, :nd], nd)
    step = 0.05
    for _ in range(2000):
        cand = np.clip(best + step * rng.standard_normal(nd), -1.5, 1.5)
        fc = val(cand, nd)
        if fc < fb:
            best, fb = cand, fc
        else:
            step *= 0.999
    return best, fb


def main():
    section("1. The objective, its wells and the reference minimum")
    print("  f(u) = 1 - sum_k d_k exp(-||u-c_k||^2/(2*0.30^2)) + 0.05 t.u")
    print(f"  five wells of depths {_DEPTHS[0]:.2f} to {_DEPTHS[-1]:.2f}; the layout")
    print("  is the first n coordinates of one fixed 4-D set, so the 2-D and")
    print("  4-D problems share their low-dimensional structure.")
    refs = {}
    for nd in (2, 4):
        _, fg = reference_minimum(nd)
        refs[nd] = fg
        print(f"  reference global minimum, n = {nd}: f = {fg:.6f}")
    print(f"  success tolerance: final f within {TOL} of the reference minimum.")
    print("  DECLARED synthetic function: no ranking below should be transferred to")
    print("  a real misfit surface without repeating the measurement.")

    section("2. The neighbourhood algorithm: cell contraction and acceptance")
    print("  Each generation draws new models inside the Voronoi cell of the current")
    print("  best model.  The cell is characterised by the ball inscribed in it:")
    print("  radius = half the distance from the best model to its nearest sample")
    print("  neighbour.  The acceptance fraction is measured by rejection.\n")
    _, fb, n_fwd, rad, probes = neighbourhood(2, 640)
    print(f"  one run, n = 2, {n_fwd} forward evaluations, {len(rad)} generations")
    print("   generation   inscribed radius   ball volume / box volume")
    for k in (0, 1, 4, 9, 19, len(rad) - 1):
        if k < len(rad):
            print(f"   {k + 1:10d}   {rad[k]:16.6f}   "
                  f"{ball_volume(rad[k], 2) / 4.0:24.3e}")
    print("\n   generation   measured acceptance fraction   inscribed radius")
    for gen, acc, r_ins in probes:
        print(f"   {gen:10d}   {acc:28.5f}   {r_ins:16.6f}")
    print(f"\n  best value found = {fb:.6f} against the reference {refs[2]:.6f}")
    print("  Two things are measured.  First, the contraction is real and violent:")
    print("  the inscribed radius falls from 0.138 to 1e-4 in four generations, and")
    print("  the measured acceptance fraction falls with it.  Second, this")
    print("  implementation PAYS for that contraction: having committed to the best")
    print("  of a 16-point initial sample, it never escapes that poor basin, and it")
    print("  finishes further from the global minimum than a plain random search of")
    print("  the same cost.  That is the failure mode of a naive neighbourhood")
    print("  algorithm -- premature collapse -- and the standard remedies are a")
    print("  larger initial sample and the simultaneous treatment of several cells,")
    print("  both of which cost more model evaluations.  The contraction is powerful")
    print("  and brittle, and which of the two dominates is measured, not assumed.")

    section("3. Very fast simulated annealing")
    print("  Temperature T(k) = 0.5 x 0.995^k with a Cauchy-like proposal")
    print("    du_i = sign x T x ((1 + 1/T)^|2r-1| - 1),   r uniform on (0,1),")
    print("  accepted by the Metropolis rule.  At large T the proposal is nearly")
    print("  uniform over the box; at small T it is local.\n")
    nd = 4
    print("   budget   success rate over 8 runs   median final f"
          "   median distance to the global well")
    for n_eval in (1000, 4000):
        ok, fvals, dists = 0, [], []
        for _ in range(8):
            u, fu = vfsa(nd, n_eval)
            fvals.append(fu)
            dists.append(float(np.linalg.norm(u - _CENTRES[0, :nd])))
            if abs(fu - refs[nd]) < TOL:
                ok += 1
        print(f"   {n_eval:6d}   {ok / 8:24.2f}   {np.median(fvals):16.6f}   "
              f"{np.median(dists):31.4f}")
    print("  The measured difference between the two budgets is 0.50 against 0.25")
    print("  over 8 runs each: with a success probability near 0.4, 8 runs give a")
    print("  standard error of about 0.17, so the two numbers are statistically")
    print("  indistinguishable.  Reporting them without the sample size would be a")
    print("  fabricated trend.  What the annealer delivers for its cost is the")
    print("  ability to work with no model-space geometry at all: only an objective,")
    print("  a proposal and a schedule, which is exactly why it is used when the")
    print("  geometry is awkward.")

    section("4. Equal-cost comparison, two and four dimensions")
    print("   n   method                        budget   success rate"
          "   median final f")
    for nd in (2, 4):
        for n_eval in (1000,):
            ok, fvals = 0, []
            for _ in range(8):
                U = RNG.uniform(-1.0, 1.0, size=(n_eval, nd))
                fu = float(np.min(objective(U, nd)))
                fvals.append(fu)
                if abs(fu - refs[nd]) < TOL:
                    ok += 1
            print(f"   {nd}   {'random search':27s} {n_eval:7d}   {ok / 8:12.2f}   "
                  f"{np.median(fvals):16.6f}")
            for name, runner in (("neighbourhood algorithm",
                                  lambda N, d=nd: neighbourhood(d, N)[1]),
                                 ("very fast simulated annealing",
                                  lambda N, d=nd: vfsa(d, N)[1])):
                ok, fvals = 0, []
                for _ in range(8):
                    fv = runner(n_eval)
                    fvals.append(fv)
                    if abs(fv - refs[nd]) < TOL:
                        ok += 1
                print(f"   {nd}   {name:27s} {n_eval:7d}   {ok / 8:12.2f}   "
                      f"{np.median(fvals):16.6f}")
    print("  Read the table against its own measurements, not against reputation.")
    print("  At n = 2 the true minimum is easy to hit and random search already")
    print("  succeeds; the naive neighbourhood algorithm collapses prematurely and")
    print("  does worse.  At n = 4 nothing succeeds reliably at this cost, the")
    print("  annealer is best, and random search fails outright -- the target volume")
    print("  is now too small to find by chance.  The transferable statement is that")
    print("  contraction without an escape mechanism is not a global method, and that")
    print("  a method's ranking depends on the dimension and the cost, both of which")
    print("  are measured here rather than assumed.")
    print("  A note on cost accounting: the neighbourhood algorithm's random draws")
    print("  produce no forward evaluations and are therefore free in the currency")
    print("  used here, cheap in a fast forward model, and ruinous when the cell of")
    print("  a high-dimensional model space is thinner than the draws can find.")


if __name__ == "__main__":
    main()
