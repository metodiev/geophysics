#!/usr/bin/env python3
"""Facies prediction from well logs: a nearest-centroid baseline versus a tree.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python facies_and_lithology_demo.py

Everything here is SYNTHETIC.  The logs, the bed boundaries and the facies come
from the generator below; no well, core description or published log response is
read or quoted.

Sections
--------
1. The synthetic well: bed statistics and depth trends.
2. A random split: what a naive validation reports.
3. A depth split: the same models asked to extrapolate downhole.
4. Why the two numbers differ, and what a depth split is really testing.
"""

import numpy as np
from scipy.ndimage import median_filter
from sklearn.tree import DecisionTreeClassifier

RNG = np.random.default_rng(20261014)

NDEPTH = 3000           # samples
DZ = 0.1                # depth sampling interval, m
DEPTH = np.arange(NDEPTH) * DZ
FACIES = ("sand", "shale", "carbonate")
GR_SD = 10.0            # gamma-ray noise, API units
RHOB_SD = 0.05          # density noise, g/cm^3
NPHI_SD = 0.04          # neutron-porosity noise, v/v


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def true_proportions(f):
    """Depth-dependent facies proportions: shale takes over downhole."""
    p_shale = 0.20 + 0.55 * f
    return np.array([(1.0 - p_shale) * 0.60, p_shale, (1.0 - p_shale) * 0.40])


def make_well():
    """One synthetic well: facies along depth and three log responses."""
    f = DEPTH / DEPTH[-1]
    proportions = np.array([true_proportions(fi) for fi in f])
    draws = RNG.random(NDEPTH)
    facies = (draws[:, None] > np.cumsum(proportions, axis=1)).sum(axis=1)
    # median filter -> beds of a few decimetres instead of white noise
    facies = median_filter(facies, size=9, mode="nearest")

    is_sand = facies == 0
    is_shale = facies == 1
    # Downhole the sand becomes shaly: its response migrates towards the
    # shallow shale signature.  This is the drift the depth split tests.
    gr = np.where(is_sand, 70.0 + 20.0 * f,
                  np.where(is_shale, 95.0 + 10.0 * f, 25.0 + 5.0 * f))
    rhob = np.where(is_sand, 2.32 + 0.16 * f,
                    np.where(is_shale, 2.45 + 0.10 * f, 2.66 + 0.02 * f))
    nphi = np.where(is_sand, 0.24 + 0.08 * f,
                    np.where(is_shale, 0.34 - 0.04 * f, 0.10 - 0.01 * f))
    gr = gr + GR_SD * RNG.standard_normal(NDEPTH)
    rhob = rhob + RHOB_SD * RNG.standard_normal(NDEPTH)
    nphi = nphi + NPHI_SD * RNG.standard_normal(NDEPTH)
    return facies, np.column_stack([gr, rhob, nphi])


def centroid_model(x, y):
    """Per-class mean and pooled standard deviation, used as a Gaussian ML rule."""
    mean = np.array([x[y == k].mean(axis=0) for k in range(3)])
    sd = x.std(axis=0)
    return mean, sd


def centroid_predict(x, model):
    mean, sd = model
    z = (x - mean[:, None, :]) / sd
    return np.argmin((z ** 2).sum(axis=2), axis=0)


def accuracy(truth, prediction):
    return float(np.mean(truth == prediction))


def recall(truth, prediction, k):
    return float(np.mean(prediction[truth == k] == k))


def main():
    section("1. The synthetic well: bed statistics and depth trends")
    facies, logs = make_well()
    bed = np.cumsum(np.concatenate([[0], (np.diff(facies) != 0).astype(int)]))
    print(f"SYNTHETIC well: {NDEPTH} samples, {DZ:.1f} m spacing, "
          f"{DEPTH[-1]:.0f} m total, {bed.max() + 1} beds")
    print("  proportions by depth third (sand / shale / carbonate):")
    for name, sl in (("shallow", slice(0, NDEPTH // 3)),
                     ("middle", slice(NDEPTH // 3, 2 * NDEPTH // 3)),
                     ("deep", slice(2 * NDEPTH // 3, NDEPTH))):
        counts = np.bincount(facies[sl], minlength=3) / (sl.stop - sl.start)
        print(f"    {name:<8s} {counts[0]:5.3f} {counts[1]:5.3f} {counts[2]:5.3f}")
    print("  downhole drift of the class means:")
    print("    sand       GR  70 -> 90 API, RHOB 2.32 -> 2.48 g/cm3, "
          "NPHI 0.24 -> 0.32 v/v")
    print("    shale      GR  95 -> 105 API, RHOB 2.45 -> 2.55 g/cm3, "
          "NPHI 0.34 -> 0.30 v/v")
    print("    carbonate  GR  25 -> 30 API, RHOB 2.66 -> 2.68 g/cm3, "
          "NPHI 0.10 -> 0.09 v/v")
    print(f"  noise: GR {GR_SD:.1f} API (1 s.d.), RHOB {RHOB_SD:.3f} g/cm3, "
          f"NPHI {NPHI_SD:.3f} v/v")

    def evaluate(tag, train_idx, test_idx):
        x_tr, y_tr = logs[train_idx], facies[train_idx]
        x_te, y_te = logs[test_idx], facies[test_idx]
        model = centroid_model(x_tr, y_tr)
        tree = DecisionTreeClassifier(max_depth=4, random_state=20261014)
        tree.fit(x_tr, y_tr)
        pred_c = centroid_predict(x_te, model)
        pred_t = tree.predict(x_te)
        print(f"  {tag}")
        print(f"    train {train_idx.size} samples, test {test_idx.size} samples; "
              f"test proportions "
              + "/".join(f"{np.mean(y_te == k):.3f}" for k in range(3)))
        print(f"    nearest centroid accuracy = {accuracy(y_te, pred_c):.3f}, "
              f"decision tree accuracy = {accuracy(y_te, pred_t):.3f}")
        return y_te, pred_c, pred_t

    section("2. Three splits of the same well")
    order = RNG.permutation(NDEPTH)
    evaluate("shuffled samples, 70/30 -- adjacent samples in both folds:",
             order[:2100], order[2100:])

    n_beds = bed.max() + 1
    bed_order = RNG.permutation(n_beds)
    counts = np.bincount(bed, minlength=n_beds)
    chosen, total = [], 0
    for b in bed_order:
        if total >= 2100:
            break
        chosen.append(b)
        total += counts[b]
    train_beds = np.isin(bed, chosen)
    evaluate("whole beds held out, ~70/30 -- no bed in both folds:",
             np.nonzero(train_beds)[0], np.nonzero(~train_beds)[0])

    cut = 900
    y_te, pred_c, pred_t = evaluate(
        f"depth split: train above {cut * DZ:.0f} m, test below it:",
        np.arange(cut), np.arange(cut, NDEPTH))

    section("3. What the depth split does to each class")
    print("  per-class recall on the deep test interval:")
    for k, name in enumerate(FACIES):
        print(f"    {name:<10s} centroid {recall(y_te, pred_c, k):.3f}, "
              f"tree {recall(y_te, pred_t, k):.3f}, "
              f"share of test interval {np.mean(y_te == k):.3f}")

    section("4. Why the three numbers differ")
    print("  The shuffled split puts samples from the same bed on both sides, so it")
    print("  measures interpolation inside a bed a few decimetres thick.  Holding")
    print("  out whole beds removes that leak and is the cheapest honest split.")
    print("  The depth split asks the question a field user asks: does the rule")
    print("  still work where the facies proportions and the log responses have")
    print("  moved?  Downhole the sand response migrates towards the shallow shale")
    print("  signature, so the sand recall -- not the overall accuracy -- is the")
    print("  number that collapses, and overall accuracy looks deceptively fine")
    print("  because the deep interval is 89% shale.")
    print("\nSYNTHETIC: the logs come from this generator.  A real well also has")
    print("invasion, bad-hole intervals, tool drift and core-to-log depth errors.")


if __name__ == "__main__":
    main()
