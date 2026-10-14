#!/usr/bin/env python3
"""Mineral prospectivity mapping: which analyst choice moves the score?

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mineral_prospectivity_ml_demo.py

Everything here is SYNTHETIC.  The geophysical fields, the fault, the deposit
locations and the negative samples are generated below; no deposit inventory,
geochemical survey or published prospectivity map is used.

Sections
--------
1. The synthetic grid, its features and its deposit set.
2. Uniform random negatives: the usual protocol.
3. Matched negatives: the same model with harder non-deposit cells.
4. Targeting efficiency, the decision-relevant metric.
"""

import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.stats import rankdata
from sklearn.linear_model import LogisticRegression

RNG = np.random.default_rng(20261014)

NX, NY = 60, 60             # cells, 1 km each
CELL_KM = 1.0
SMOOTH = 6.0                # correlation length of the fields, in cells
N_DEPOSIT = 100             # expected number of deposits
N_NEGATIVE = 800            # negative cells in the training set
MATCH_RADIUS = 3            # cells, for the matched-negative design
BLOCK = 15                  # 4 x 4 spatial blocks of BLOCK x BLOCK cells


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def auc_score(scores, labels):
    ranks = rankdata(scores)
    n_pos = int(labels.sum())
    n_neg = int(labels.size - n_pos)
    return (ranks[labels == 1].sum() - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg)


def build_grid():
    """Three correlated layers plus the distance to a synthetic fault trace."""
    shape = (NY, NX)
    layers = [gaussian_filter(RNG.standard_normal(shape), SMOOTH)
              for _ in range(3)]
    for layer in layers:
        layer -= layer.mean()
        layer /= layer.std()
    yy, xx = np.mgrid[0:NY, 0:NX]
    fault_x = 18.0 + 0.35 * yy + 5.0 * np.sin(yy / 9.0)
    distance = np.abs(xx - fault_x) * CELL_KM
    distance = distance / distance.std()
    return np.stack(layers + [distance], axis=-1)


def evaluate(x, y, rows, cols, tag):
    """Pooled out-of-fold AUC under random folds and under spatial blocks."""
    block = (rows // BLOCK) * (NX // BLOCK) + (cols // BLOCK)

    def fit_predict(train, test):
        mean, sd = x[train].mean(axis=0), x[train].std(axis=0)
        clf = LogisticRegression(max_iter=2000)
        clf.fit((x[train] - mean) / sd, y[train])
        return clf.predict_proba((x[test] - mean) / sd)[:, 1]

    oof_random = np.empty(y.size)
    for k in range(5):
        test = np.nonzero(np.arange(y.size) % 5 == k)[0]
        oof_random[test] = fit_predict(np.setdiff1d(np.arange(y.size), test), test)
    oof_block = np.empty(y.size)
    for b in range((NX // BLOCK) ** 2):
        test = np.nonzero(block == b)[0]
        train = np.nonzero(block != b)[0]
        if test.size:
            oof_block[test] = fit_predict(train, test)

    a_random = auc_score(oof_random, y)
    a_block = auc_score(oof_block, y)
    print(f"  {tag}")
    print(f"    pooled AUC, 5 random folds      = {a_random:.3f}")
    print(f"    pooled AUC, leave-one-block-out = {a_block:.3f}")
    print(f"    difference (random minus block) = {a_random - a_block:+.3f}")
    return a_random, a_block


def main():
    section("1. The synthetic grid, its features and its deposit set")
    features = build_grid()
    latent = (1.4 * features[..., 0] + 0.7 * features[..., 1]
              - 0.6 * features[..., 2] + 0.6 * features[..., 3]
              + 0.6 * gaussian_filter(RNG.standard_normal((NY, NX)), SMOOTH))
    weight = 1.0 / (1.0 + np.exp(-latent))
    weight = (weight / weight.sum()).ravel()
    is_deposit = (RNG.random(NX * NY) < N_DEPOSIT * weight).astype(int)
    deposit_idx = np.nonzero(is_deposit)[0]
    print(f"SYNTHETIC grid: {NY} x {NX} cells of {CELL_KM:.0f} km "
          f"({NY * NX} cells); fields smoothed with sigma = {SMOOTH:.1f} cells")
    print(f"  features: magnetic, gravity and geochemical layers, plus the "
          f"distance to a curved fault")
    print(f"  deposits: {deposit_idx.size} cells drawn with probability")
    print("  proportional to sigmoid(latent) -- a graded response, so the label")
    print("  carries irreducible noise and no rule can separate the classes")
    print(f"  latent field: 1.4 z_mag + 0.7 z_grav - 0.6 z_geochem + "
          f"0.6 z_fault, plus a correlated residual")
    print("  a real inventory also carries a reporting bias: ground near roads and")
    print("  outcrop is visited first, so 'no deposit' often means 'not visited'")

    x_all = features.reshape(-1, 4)
    rows_all = np.arange(NX * NY) // NX
    cols_all = np.arange(NX * NY) % NX

    uniform = RNG.choice(np.setdiff1d(np.arange(NX * NY), deposit_idx),
                         N_NEGATIVE, replace=False)
    sample_u = np.concatenate([deposit_idx, uniform])
    x_u, y_u = x_all[sample_u], is_deposit[sample_u]

    near = set()
    for cell in deposit_idx:
        r, c = divmod(int(cell), NX)
        for dr in range(-MATCH_RADIUS, MATCH_RADIUS + 1):
            for dc in range(-MATCH_RADIUS, MATCH_RADIUS + 1):
                rr, cc = r + dr, c + dc
                if 0 <= rr < NY and 0 <= cc < NX:
                    near.add(rr * NX + cc)
    near = np.array(sorted(near - set(int(i) for i in deposit_idx)))
    matched = RNG.choice(near, min(N_NEGATIVE, near.size), replace=False)
    sample_m = np.concatenate([deposit_idx, matched])
    x_m, y_m = x_all[sample_m], is_deposit[sample_m]

    section("2. Uniform random negatives: the usual protocol")
    print(f"  {N_NEGATIVE} non-deposit cells drawn uniformly at random; "
          f"positives {y_u.sum()}, negatives {int((y_u == 0).sum())}")
    evaluate(x_u, y_u, rows_all[sample_u], cols_all[sample_u],
             "negatives sampled from the whole grid:")
    print("  every candidate cell of the grid is a legitimate 'no deposit', so")
    print("  this design measures whether the model can rank fertile ground above")
    print("  the average cell -- a weak test that flatters any smooth predictor")

    section("3. Matched negatives: harder, and more honest")
    print(f"  {matched.size} non-deposit cells within {MATCH_RADIUS} cells of a "
          f"known deposit; positives {y_m.sum()}")
    a_m, b_m = evaluate(x_m, y_m, rows_all[sample_m], cols_all[sample_m],
                        "negatives sampled next to known deposits:")
    print("  these cells sit on the same anomalies as the deposits, so the model")
    print("  must resolve a local detail rather than a regional trend")

    section("4. Targeting efficiency, the decision-relevant metric")
    mean, sd = x_u.mean(axis=0), x_u.std(axis=0)
    full = LogisticRegression(max_iter=2000).fit((x_u - mean) / sd, y_u)
    score = full.predict_proba((x_all - mean) / sd)[:, 1]
    top10 = np.argsort(score)[::-1][:int(0.10 * NX * NY)]
    captured = float(np.isin(top10, deposit_idx).sum()) / deposit_idx.size
    print(f"  uniform-negative model, top 10% of all {NX * NY} cells: "
          f"{captured:.3f} of the deposits captured")
    print("  a random 10% would capture 0.100, so the uplift is the number a")
    print("  targeting programme buys:")
    print(f"    uplift = {captured / 0.10:.2f}x")
    print("  that number is fitted on the deposits it is asked to find, so it")
    print("  belongs in a report only beside an out-of-sample version")
    print(f"\nSYNTHETIC: this grid is generated by the script.  The two fold designs")
    print(f"moved the AUC by at most {abs(a_m - b_m):.3f} either way, while the")
    print("choice of negatives moved it by "
          f"{auc_score(full.predict_proba((x_u - mean) / sd)[:, 1], y_u) - b_m:.3f}.")
    print("Both are analyst choices; only one of them is usually reported.")


if __name__ == "__main__":
    main()
