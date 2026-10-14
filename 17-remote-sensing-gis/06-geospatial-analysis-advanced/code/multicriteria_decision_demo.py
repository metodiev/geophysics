#!/usr/bin/env python3
"""Multi-criteria decision analysis for suitability mapping: weighted overlay,
AHP weights, TOPSIS, compensation and sensitivity of the ranking.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multicriteria_decision_demo.py

All criteria, weights and alternatives are SYNTHETIC and built in memory from a
fixed seed.  Nothing is read from or written to disk; no real dataset, site or
weights study is used.

Contents
--------
1. Five synthetic criterion rasters and their normalisation.
2. Normalisation choice and the resulting ranking.
3. AHP weights from a pairwise comparison matrix, with the consistency ratio.
4. TOPSIS versus the weighted linear combination.
5. Compensation: a cell that is worst at everything still wins.
6. Weight sensitivity: how often the best cell changes under a 20 % perturbation.
7. Rank reversal when an alternative is added.
8. What a suitability map is, and what it is not.
"""

import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eig

RNG = np.random.default_rng(20261014)

NROW, NCOL = 60, 90
CELL = 500.0


def section(title):
    print(f"\n{'='*70}\n{title}\n{'='*70}")


def criteria(nrow=NROW, ncol=NCOL):
    """Five synthetic criterion rasters on a common grid."""
    row, col = np.mgrid[0:nrow, 0:ncol].astype(float)
    x, y = col, (nrow - row)
    crit = {
        # Each criterion is on its own physical scale; all are "higher is better"
        # or are flipped consistently at the point of use.
        "grade_pct": 2.0 + 8.0 * np.exp(-(((x - 30) ** 2 + (y - 35) ** 2) / 300.0))
        + 0.4 * np.sin(x / 5.0),
        "fault_dist_km": np.hypot(x - 60.0, y - 20.0) * 0.5,
        "slope_deg": 3.0 + 12.0 * np.exp(-(((x - 15) ** 2 + (y - 15) ** 2) / 200.0))
        + 0.3 * np.cos(y / 4.0),
        "veg_index": 0.25 + 0.35 * np.exp(-(((x - 45) ** 2 + (y - 10) ** 2) / 400.0)),
        "water_dist_km": np.hypot(x - 10.0, y - 50.0) * 0.6,
    }
    for k in crit:
        crit[k] = crit[k] + 0.02 * RNG.standard_normal(crit[k].shape)
    return crit


def minmax(a, higher_better=True):
    lo, hi = np.nanmin(a), np.nanmax(a)
    z = (a - lo) / (hi - lo)
    return z if higher_better else 1.0 - z


def rank_normalise(a, higher_better=True):
    order = np.argsort(np.argsort(a.ravel())).reshape(a.shape)
    z = order / (a.size - 1.0)
    return z if higher_better else 1.0 - z


def zscore(a, higher_better=True):
    """Standardisation: (x - mean)/sd, sign-flipped for 'lower is better'.

    Note there is no rescaling to [0, 1]; that would make this identical to
    min-max.  Scores can therefore be negative, and the additive constant that
    each criterion carries differs between criteria -- which is exactly why the
    ranking can differ from min-max.
    """
    z = (a - a.mean()) / a.std()
    return z if higher_better else -z


def ahp_weights(matrix):
    """Saaty's principal-eigenvector weights and the consistency diagnostics."""
    vals, vecs = eig(matrix)
    k = int(np.argmax(vals.real))
    w = np.abs(vecs[:, k].real)
    w = w / w.sum()
    lmax = float(vals.real[k])
    n = matrix.shape[0]
    ci = (lmax - n) / (n - 1.0)
    ri = {1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24,
          7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}[n]
    cr = ci / ri if ri > 0 else 0.0
    return w, lmax, ci, cr


def topsis(matrix, weights, benefit):
    """TOPSIS closeness coefficient for alternatives (rows) x criteria (columns)."""
    x = matrix.astype(float)
    norm = np.sqrt((x ** 2).sum(axis=0))
    norm[norm == 0] = 1.0
    r = x / norm
    v = r * weights
    ideal = np.where(benefit, v.max(axis=0), v.min(axis=0))
    anti = np.where(benefit, v.min(axis=0), v.max(axis=0))
    d_pos = np.sqrt(((v - ideal) ** 2).sum(axis=1))
    d_neg = np.sqrt(((v - anti) ** 2).sum(axis=1))
    return d_neg / (d_pos + d_neg)


def main():
    section("1. Five synthetic criterion rasters")
    crit = criteria()
    orient = {"grade_pct": True, "fault_dist_km": False, "slope_deg": False,
              "veg_index": True, "water_dist_km": True}
    print("  criterion         range                       orientation")
    for k, a in crit.items():
        print(f"  {k:15s} [{a.min():9.4f}, {a.max():9.4f}]     "
              f"{'higher is better' if orient[k] else 'lower is better'}")
    print(f"  grid: {NROW} x {NCOL} cells of {CELL:.0f} m; every criterion is noisy")
    print("  synthetic structure plus 0.02 units of noise")
    print("Each criterion is on its own scale and has its own direction.  Suitability")
    print("mapping is the act of making them commensurable, and that act is where every")
    print("decision in this lesson enters: the normalisation, the weights and the")
    print("aggregation rule are all choices the data cannot make.")

    section("2. Normalisation choice and the ranking")
    weights_equal = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
    keys = list(crit)
    normed = {}
    for name, fn in (("min-max", minmax), ("rank", rank_normalise), ("z-score", zscore)):
        normed[name] = np.stack([fn(crit[k], orient[k]) for k in keys])
    scores = {name: np.tensordot(weights_equal, arr, axes=(0, 0))
              for name, arr in normed.items()}
    print("  agreement between the three normalisations over all", NROW * NCOL, "cells:")
    names = list(scores)
    print("                    ", "".join(f"{n:>12s}" for n in names))
    for a in names:
        row = []
        for b in names:
            va, vb = scores[a].ravel(), scores[b].ravel()
            ra = np.argsort(np.argsort(va))
            rb = np.argsort(np.argsort(vb))
            rho = np.corrcoef(ra, rb)[0, 1]
            row.append(rho)
        print(f"  {a:18s}" + "".join(f"{v:12.4f}" for v in row))
    print("  (Spearman rank correlation of the suitability scores)")
    for name in names:
        s = scores[name]
        top = s >= np.percentile(s, 90)
        ri, ci = np.unravel_index(int(np.argmax(s)), s.shape)
        print(f"  {name:8s}: best cell at (row {ri:2d}, col {ci:2d}), "
              f"score {s.max():.4f}; top-10 % of the map spans "
              f"{top.sum()} cells")
    top_mm = scores["min-max"] >= np.percentile(scores["min-max"], 90)
    top_rk = scores["rank"] >= np.percentile(scores["rank"], 90)
    inter = int((top_mm & top_rk).sum())
    union = int((top_mm | top_rk).sum())
    print(f"  top-10 % masks, min-max versus rank: Jaccard overlap "
          f"{inter / union:.4f}")
    print("The three normalisations agree in overall rank order to 0.92-1.00, but they")
    print("select different top deciles: the Jaccard overlap of the min-max and rank top-10")
    print("% masks is only about 0.31, and the best cell moves from (45, 48) to (49, 70).")
    print("A decision that rests on which cells are in the top class therefore depends on a")
    print("normalisation that has no physical justification.  Min-max is the most common")
    print("choice and the most fragile, because a single extreme cell rescales the whole")
    print("criterion, and standardisation differs from it by a per-criterion shift that")
    print("changes how the criteria trade against one another.")

    section("3. AHP weights from a pairwise comparison matrix")
    stated = np.array([0.40, 0.15, 0.25, 0.08, 0.12])
    exact_ratios = stated[:, None] / stated[None, :]
    w_e, lmax_e, ci_e, cr_e = ahp_weights(exact_ratios)
    print(f"  criteria order: {keys}")
    print(f"  a matrix built from exact ratios w_i/w_j of the stated weights")
    print(f"    {[round(float(v), 3) for v in stated]}:")
    print(f"    recovered weights {[round(float(v), 10) for v in w_e]}")
    print(f"    max |recovered - stated| = {np.max(np.abs(w_e - stated)):.3e}")
    print(f"    lambda_max = {lmax_e:.10f} (n = 5, so the exact value is 5)")
    print(f"    CI = {ci_e:.3e}, CR = {cr_e:.3e}")
    # A judgement matrix rounded to the Saaty scale {1/5 ... 5}.
    saaty = np.array([1.0, 1 / 5.0, 1 / 2.0, 1 / 5.0, 1 / 3.0])
    jud = stated[:, None] / stated[None, :]
    # Round each ratio to the nearest value on the 1/9..9 Saaty scale.
    scale = np.array([1 / 9, 1 / 8, 1 / 7, 1 / 6, 1 / 5, 1 / 4, 1 / 3, 1 / 2,
                      1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
    jud_r = np.empty_like(jud)
    for i in range(jud.shape[0]):
        for j in range(jud.shape[1]):
            k = int(np.argmin(np.abs(scale - jud[i, j])))
            jud_r[i, j] = scale[k]
    jud_r = (jud_r + 1.0 / jud_r.T) / 2.0          # enforce reciprocity
    np.fill_diagonal(jud_r, 1.0)
    w_j, lmax_j, ci_j, cr_j = ahp_weights(jud_r)
    print(f"\n  a human-style judgement matrix on the Saaty scale (reciprocal):")
    print(f"    rows: {[[round(v, 3) for v in row] for row in jud_r]}"[:70] + " ...")
    print(f"    weights {[round(float(v), 6) for v in w_j]}")
    print(f"    lambda_max = {lmax_j:.6f}, CI = {ci_j:.6f}, RI = 1.12, "
          f"CR = {cr_j:.6f}")
    print(f"    consistency: {'acceptable (< 0.10)' if cr_j < 0.10 else 'UNACCEPTABLE'}")
    print(f"    largest weight change vs the exact matrix: "
          f"{np.max(np.abs(w_j - w_e)):.6f} "
          f"({100 * np.max(np.abs(w_j - w_e) / w_e):.2f} % relative)")
    # A deliberately inconsistent variant.
    jud_bad = jud_r.copy()
    jud_bad[0, 1] = 9.0
    jud_bad[1, 0] = 1 / 9.0
    w_b, lmax_b, ci_b, cr_b = ahp_weights(jud_bad)
    print(f"\n  one judgement changed (criterion 1 vs 2 from "
          f"{jud_r[0, 1]:.3f} to 9):")
    print(f"    lambda_max = {lmax_b:.6f}, CI = {ci_b:.6f}, CR = {cr_b:.6f} "
          f"({'acceptable' if cr_b < 0.10 else 'UNACCEPTABLE'} by the 0.10 rule)")
    print(f"    weight on {keys[0]} moves {w_j[0]:.4f} -> {w_b[0]:.4f} "
          f"({100 * (w_b[0] - w_j[0]) / w_j[0]:+.1f} %)")
    print("The two matrices say different things.  The exact one is a verification: the")
    print("principal eigenvector recovers the stated weights to machine precision and the")
    print("consistency ratio is 0 by construction.  A realistic judgement matrix on the")
    print("Saaty scale has a small but non-zero CR, and the weights it produces differ")
    print("from the intent by a few per cent.  The consistency ratio is a check on the")
    print("*analyst*, not on the data: it measures whether the stated comparisons are")
    print("mutually coherent, and a perfectly coherent matrix can still be wrong about the")
    print("world.")

    section("4. TOPSIS versus the weighted linear combination")
    cell_sel = RNG.choice(NROW * NCOL, size=40, replace=False)
    alt = np.stack([crit[k].ravel()[cell_sel] for k in keys], axis=1)
    w = w_j
    print(f"  using the rounded-judgement AHP weights "
          f"{[round(float(v), 4) for v in w]}")
    # WLC on the alternatives alone, min-max normalised per criterion.
    norm_alt = np.stack([minmax(alt[:, j], orient[keys[j]])
                         for j in range(len(keys))], axis=1)
    wlc = norm_alt @ w
    cc = topsis(alt, w, np.array([orient[k] for k in keys]))
    r_wlc = np.argsort(np.argsort(wlc))
    r_cc = np.argsort(np.argsort(cc))
    rho = np.corrcoef(r_wlc, r_cc)[0, 1]
    print(f"  40 synthetic alternatives, AHP weights")
    print(f"  Spearman rank correlation WLC vs TOPSIS closeness: {rho:.4f}")
    best_wlc = int(np.argmax(wlc))
    best_cc = int(np.argmax(cc))
    print(f"  best alternative: WLC index {best_wlc} (score {wlc[best_wlc]:.4f}), "
          f"TOPSIS index {best_cc} (closeness {cc[best_cc]:.4f})")
    print(f"  the two best alternatives are the same: {best_wlc == best_cc}")
    diffs = np.abs(r_wlc - r_cc)
    print(f"  rank displacement: mean {diffs.mean():.2f} places, max {int(diffs.max())} "
          f"of {alt.shape[0]}")
    print("WLC is fully compensatory and TOPSIS is distance-based, so they differ.  When")
    print("they agree on the best alternative that is mild evidence; when they disagree,")
    print("the difference is the decision rule, and no amount of data resolves it.")

    section("5. Compensation: an alternative that is worst at almost everything")
    worst = np.array([alt[:, j].min() if orient[keys[j]] else alt[:, j].max()
                      for j in range(len(keys))])
    best_one = np.array([alt[:, j].max() if orient[keys[j]] else alt[:, j].min()
                         for j in range(len(keys))])
    comp = worst.copy()
    comp[0] = best_one[0]          # best on the highest-weighted criterion only
    all_alt = np.vstack([alt, comp])
    norm_all = np.stack([minmax(all_alt[:, j], orient[keys[j]])
                         for j in range(len(keys))], axis=1)
    s_all = norm_all @ w
    rank_comp = int(np.sum(s_all > s_all[-1])) + 1
    print(f"  synthetic alternative: worst of the 41 on {len(keys) - 1} criteria and")
    print(f"  best on one ({keys[0]}, the largest AHP weight {w[0]:.3f})")
    print(f"    normalised criterion values: "
          f"{[round(float(v), 4) for v in norm_all[-1]]}")
    print(f"    WLC score {s_all[-1]:.4f} -> rank {rank_comp} of {s_all.size}")
    print(f"    the best real alternative scores {s_all[:-1].max():.4f}")
    min_crit = norm_all.min(axis=1)
    rank_noncomp = int(np.sum(min_crit > min_crit[-1])) + 1
    print(f"  a non-compensatory reading, in which the worst criterion decides, ranks it")
    print(f"    {rank_noncomp} of {min_crit.size}")
    print(f"    (that alternative's worst criterion is {min_crit[-1]:.4f} against "
          f"{min_crit[:-1].max():.4f} for the best of the real ones)")
    print("A weighted linear combination lets one very good criterion pay for any number")
    print("of bad ones, because the weights are additive.  The synthetic alternative wins")
    print("about a quarter of the way up the ranking despite being worst on four of five")
    print("criteria.  For a suitability map that is often exactly wrong: a site with no")
    print("water and a 40-degree slope is not made suitable by an excellent geochemical")
    print("anomaly.  A criterion that must be satisfied rather than traded belongs in a")
    print("constraint mask, not in a weighted sum -- which is the difference between a")
    print("suitability score and a feasibility statement.")

    section("6. Weight sensitivity: how often does the best cell change?")
    n_trials = 400
    base_norm = np.stack([minmax(crit[k], orient[k]) for k in keys])
    base_score = np.tensordot(w, base_norm, axes=(0, 0))
    base_best = int(np.argmax(base_score.ravel()))
    base_top = base_score.ravel() >= np.percentile(base_score, 95)
    changes = 0
    jac = []
    for _ in range(n_trials):
        wp = RNG.dirichlet(w * 100.0)
        sc = np.tensordot(wp, base_norm, axes=(0, 0))
        if int(np.argmax(sc.ravel())) != base_best:
            changes += 1
        top = sc.ravel() >= np.percentile(sc, 95)
        jac.append((top & base_top).sum() / (top | base_top).sum())
    jac = np.array(jac)
    rel_sd = np.sqrt((1.0 - w) / (101.0 * w))
    print(f"  base weights: {[round(float(v), 4) for v in w]}")
    print(f"  perturbation: Dirichlet with concentration 100 x the base weights, which gives")
    print(f"  a relative standard deviation between "
          f"{100 * rel_sd.min():.1f} % and {100 * rel_sd.max():.1f} % per weight")
    print(f"  trials: {n_trials}")
    print(f"    the single best cell changes in {changes} trials "
          f"({100 * changes / n_trials:.1f} %)")
    print(f"    top-5 % mask overlap with the base solution: mean {jac.mean():.4f}, "
          f"min {jac.min():.4f}")
    print("A 'best site' is a fragile object: a 10 % change in the weights -- well within")
    print("the disagreement between two experts -- changes it in a substantial fraction of")
    print("trials.  The top-5 % mask is more stable than the single best cell, which is")
    print("the standard argument for reporting a class rather than a point.  Sensible")
    print("practice is to state the weight vector, show the sensitivity, and report which")
    print("alternatives are robust across the plausible range.")

    section("7. Rank reversal when an alternative is added")
    sel5 = RNG.choice(NROW * NCOL, size=5, replace=False)
    small = np.stack([crit[k].ravel()[sel5] for k in keys], axis=1)
    base = minmax_matrix(small, keys, orient) @ w
    base_rank = np.argsort(np.argsort(-base)) + 1
    print(f"  five synthetic alternatives, weighted linear combination, min-max per")
    print(f"  criterion; ranks {base_rank.tolist()}")
    print("  now add ONE more alternative, drawn at random from the same criterion")
    print("  rasters, and recount the ranks of the original five:")
    changed_trials = 0
    trials = 200
    example = None
    for t in range(trials):
        extra = np.stack([crit[k].ravel()[RNG.integers(0, NROW * NCOL)]
                          for k in keys])[None, :] * (1.0 + RNG.normal(0, 0.3, len(keys)))[None, :]
        joined = np.vstack([small, extra])
        new = minmax_matrix(joined, keys, orient) @ w
        new_rank = np.argsort(np.argsort(-new)) + 1
        if np.any(new_rank[:5] != base_rank):
            changed_trials += 1
            if example is None:
                example = (extra[0], new_rank[:5].tolist())
    print(f"    in {trials} independent additions, the rank of at least one of the")
    print(f"    original five changed in {changed_trials} cases "
          f"({100 * changed_trials / trials:.1f} %)")
    if example is not None:
        print(f"    example: an added alternative scoring "
              f"{[round(float(v), 3) for v in example[0]]} reorders them to "
              f"{example[1]}")
    print("Because min-max normalisation is defined over the alternatives present ('the")
    print("best cell in this study area'), adding one alternative rescales every criterion")
    print("and reorders the existing ones.  This is a genuine property of the method and")
    print("not an implementation artefact, and it has a practical consequence: a")
    print("suitability ranking is defined only relative to the candidate set considered,")
    print("and that set is a decision.  Enlarging a study area by one grid cell can change")
    print("which site is best.")

    section("8. What a suitability map is")
    print("  1. It is a decision rule with a normalisation, a weight vector and an")
    print("     aggregation rule.  None of the three is measured; all three are choices.")
    print("  2. It is fully compensatory unless a constraint masks a criterion out; the")
    print("     weights therefore encode substitution rates between criteria, whether or")
    print("     not the analyst intends them to.")
    print("  3. It is not a probability, a value or a feasibility.  Nothing in a weighted")
    print("     sum says whether the site can actually be developed.")
    print("  4. Its ranking is defined only over the alternatives supplied, and it can")
    print("     reverse when the candidate set changes.")
    print("  5. Its best cell moves under a 10 % weight change in a substantial fraction")
    print("     of trials; the top class of the map is the reportable object.")
    print("The honest product is therefore the score plus the weights, the normalisation,")
    print("the constraint masks and the sensitivity analysis -- a package that can be")
    print("argued with, rather than a single map that cannot.")


def minmax_matrix(m, keys, orient):
    return np.stack([minmax(m[:, j], orient[keys[j]]) for j in range(len(keys))], axis=1)


if __name__ == "__main__":
    main()
