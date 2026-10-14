#!/usr/bin/env python3
"""Four pitfalls measured: spurious correlation, non-stationarity, extrapolation
and selection leakage.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ml_pitfalls_geophysics_demo.py

Everything here is SYNTHETIC.  The series, the regression targets and the
distractor features are generated below; no geophysical data set is read.

Sections
--------
1. Spurious correlation between two independent random walks.
2. Non-stationarity: a mean shift that no split can repair.
3. Extrapolation: a polynomial fitted where the data were, applied where they
   were not.
4. Selection leakage: choosing features before splitting.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_WALK = 100        # samples per random walk
N_MC = 1000         # Monte Carlo replications
N_TEST = 200        # held-out samples in section 2
N_SAMPLES = 50      # samples in the leakage experiment
N_FEATURES = 200    # pure-noise candidate features


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def correlate(a, b):
    a = a - a.mean()
    b = b - b.mean()
    denom = np.sqrt((a ** 2).sum() * (b ** 2).sum())
    return float((a * b).sum() / max(denom, 1e-12))


def main():
    section("1. Spurious correlation between two independent random walks")
    levels, diffs = [], []
    for _ in range(N_MC):
        a = np.cumsum(RNG.standard_normal(N_WALK))
        b = np.cumsum(RNG.standard_normal(N_WALK))
        levels.append(correlate(a, b))
        diffs.append(correlate(np.diff(a), np.diff(b)))
    levels = np.array(levels)
    diffs = np.array(diffs)
    print(f"SYNTHETIC: two INDEPENDENT random walks, {N_WALK} samples each, "
          f"{N_MC} replications")
    print(f"  correlation of the levels:      mean |r| = {np.abs(levels).mean():.3f}, "
          f"|r| > 0.5 in {np.mean(np.abs(levels) > 0.5):.3f} of replications, "
          f"|r| > 0.8 in {np.mean(np.abs(levels) > 0.8):.3f}")
    print(f"  correlation of first differences: mean |r| = {np.abs(diffs).mean():.3f}, "
          f"|r| > 0.5 in {np.mean(np.abs(diffs) > 0.5):.3f} of replications")
    print(f"  1/sqrt(n) for comparison = {1.0 / np.sqrt(N_WALK):.3f}")
    print("  Trending series share their trend, not their physics: two unrelated")
    print("  geophysical quantities that both drift will correlate unless the")
    print("  trend is removed or the analysis is done on increments.")

    section("2. Non-stationarity: a mean shift that no split can repair")
    noise_level = 1.0
    stationary = noise_level * RNG.standard_normal(N_TEST)
    shifted = 2.0 * noise_level + noise_level * RNG.standard_normal(N_TEST)
    print(f"SYNTHETIC: a training mean of 0 K, then {N_TEST} held-out samples")
    print(f"  stationary process: RMSE = "
          f"{np.sqrt(np.mean(stationary ** 2)):.3f} K (expected "
          f"{noise_level:.3f} K), bias {stationary.mean():+.3f} K")
    print(f"  shifted process:    RMSE = {np.sqrt(np.mean(shifted ** 2)):.3f} K "
          f"(expected {np.sqrt(noise_level ** 2 + 2.0 ** 2):.3f} K), "
          f"bias {shifted.mean():+.3f} K")
    print(f"  the measured error grows from "
          f"{np.sqrt(np.mean(stationary ** 2)):.3f} K to "
          f"{np.sqrt(np.mean(shifted ** 2)):.3f} K, a factor of "
          f"{np.sqrt(np.mean(shifted ** 2)) / np.sqrt(np.mean(stationary ** 2)):.1f}")
    print("  A model cannot learn a shift it has not seen, and no cross-validation")
    print("  scheme inside the training period reveals it.  Only a temporal split")
    print("  that spans the change does, which is why the split must follow the")
    print("  physics and not the row order.")

    section("3. Extrapolation: fitted where the data were, applied where they were not")
    x = np.linspace(0.0, 1.0, 120)
    y = np.tanh(2.0 * x) + 0.02 * RNG.standard_normal(x.size)
    x_far = np.linspace(1.0, 1.5, 60)
    y_far = np.tanh(2.0 * x_far) + 0.02 * RNG.standard_normal(x_far.size)
    print("  truth on the training interval: y = tanh(2x), noise 0.02")
    for degree in (1, 3, 5):
        coef = np.polyfit(x, y, degree)
        inside = np.polyval(coef, x) - y
        outside = np.polyval(coef, x_far) - y_far
        print(f"  degree {degree}: RMSE inside x in [0, 1] = "
              f"{np.sqrt(np.mean(inside ** 2)):.4f}, "
              f"RMSE outside x in [1, 1.5] = "
              f"{np.sqrt(np.mean(outside ** 2)):.4f}, "
              f"max |error| outside = {np.abs(outside).max():.3f}")
    print("  Every fit looks excellent inside the training interval and none of")
    print("  them is validated there.  A geophysical model trained on one")
    print("  magnitude, depth or climate range has no claim outside it, however")
    print("  many decimal places its hold-out RMSE reports.")

    section("4. Selection leakage: choosing features before splitting")
    features = RNG.standard_normal((N_SAMPLES, N_FEATURES))
    target = RNG.standard_normal(N_SAMPLES)          # nothing is predictive
    folds = np.arange(N_SAMPLES) % 5

    def cv_r2(select_inside):
        preds = np.empty(N_SAMPLES)
        for k in range(5):
            test = folds == k
            train = ~test
            if select_inside:
                corr = np.array([abs(correlate(features[train, j], target[train]))
                                 for j in range(N_FEATURES)])
            else:
                corr = np.array([abs(correlate(features[:, j], target))
                                 for j in range(N_FEATURES)])
            chosen = np.argsort(corr)[::-1][:10]
            design = np.column_stack([np.ones(train.sum()),
                                      features[train][:, chosen]])
            coef, *_ = np.linalg.lstsq(design, target[train], rcond=None)
            test_design = np.column_stack([np.ones(test.sum()),
                                           features[test][:, chosen]])
            preds[test] = test_design @ coef
        residual = target - preds
        return 1.0 - (residual ** 2).sum() / ((target - target.mean()) ** 2).sum()

    r2_leak = cv_r2(select_inside=False)
    r2_honest = cv_r2(select_inside=True)
    print(f"SYNTHETIC: {N_SAMPLES} samples, {N_FEATURES} pure-noise features, "
          f"target independent of all of them")
    print(f"  select the 10 best features on ALL data, then cross-validate: "
          f"R2 = {r2_leak:+.3f}")
    print(f"  select the 10 best features inside each fold, then cross-validate: "
          f"R2 = {r2_honest:+.3f}")
    print(f"  the leak is worth {r2_leak - r2_honest:+.3f} in R2 on a problem with")
    print("  no signal at all.  Every preprocessing step that uses the full data")
    print("  set -- feature selection, standardisation, imputation, outlier")
    print("  removal, hyper-parameter choice -- belongs inside the fold.")
    print("\nSYNTHETIC: every series and matrix here is generated by this script.")


if __name__ == "__main__":
    main()
