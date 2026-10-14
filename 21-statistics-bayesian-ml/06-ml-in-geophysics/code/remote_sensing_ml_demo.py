#!/usr/bin/env python3
"""Remote-sensing classification: band choice, class imbalance and a haze offset.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python remote_sensing_ml_demo.py

Everything here is SYNTHETIC.  The reflectance spectra are drawn from
class-conditional Gaussians generated below; no satellite scene, ground-truth
map or published accuracy figure is used.

Sections
--------
1. The synthetic pixel population.
2. Six bands, a balanced training set: the reference numbers.
3. Three bands instead of six: what is lost.
4. A rare class in the training set.
5. A haze offset present only in the test scene.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

BANDS = ("blue", "green", "red", "NIR", "SWIR1", "SWIR2")
CLASSES = ("water", "forest", "urban", "cropland")
MEANS = np.array([
    [0.05, 0.06, 0.04, 0.02, 0.01, 0.01],   # water
    [0.03, 0.05, 0.04, 0.30, 0.15, 0.07],   # forest
    [0.15, 0.17, 0.19, 0.22, 0.25, 0.22],   # urban
    [0.05, 0.08, 0.07, 0.35, 0.20, 0.10],   # cropland
])
SD = np.array([0.020, 0.022, 0.025, 0.035, 0.030, 0.022])
COUNTS = (200, 400, 150, 250)
N_BANDS_MIN = 3            # the visible-only case


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def make_pixels():
    pixels, labels = [], []
    for k, n in enumerate(COUNTS):
        x = MEANS[k] + SD * RNG.standard_normal((n, MEANS.shape[1]))
        pixels.append(x)
        labels.append(np.full(n, k))
    return np.vstack(pixels), np.concatenate(labels)


def train_lda(x, y, n_classes=len(CLASSES)):
    """Gaussian maximum likelihood with a pooled covariance (linear discriminant)."""
    means = np.array([x[y == k].mean(axis=0) for k in range(n_classes)])
    centered = x - means[y]
    cov = centered.T @ centered / max(x.shape[0] - n_classes, 1)
    prior = np.array([np.mean(y == k) for k in range(n_classes)])
    return means, np.linalg.inv(cov), prior


def predict_lda(x, model, n_classes=len(CLASSES)):
    means, inv_cov, prior = model
    scores = np.empty((x.shape[0], n_classes))
    for k in range(n_classes):
        d = x - means[k]
        scores[:, k] = -0.5 * np.einsum("ij,jk,ik->i", d, inv_cov, d) \
            + np.log(prior[k])
    return scores.argmax(axis=1)


def kappa(truth, prediction, n_classes=len(CLASSES)):
    po = float(np.mean(truth == prediction))
    pe = sum((np.mean(prediction == k) * np.mean(truth == k))
             for k in range(n_classes))
    return po, (po - pe) / (1.0 - pe)


def report(tag, truth, prediction):
    po, kap = kappa(truth, prediction)
    recalls = ", ".join(f"{CLASSES[k]} {np.mean(prediction[truth == k] == k):.3f}"
                        for k in range(len(CLASSES)))
    print(f"  {tag}")
    print(f"    overall accuracy = {po:.3f}, kappa = {kap:.3f}")
    print(f"    per-class recall: {recalls}")
    return po, kap


def main():
    section("1. The synthetic pixel population")
    pixels, labels = make_pixels()
    print(f"SYNTHETIC pixels: {pixels.shape[0]}, {len(BANDS)} bands "
          f"({', '.join(BANDS)}), reflectance 0-1")
    print(f"  classes and counts: "
          + ", ".join(f"{CLASSES[k]} {COUNTS[k]}" for k in range(len(CLASSES))))
    print("  every class is a Gaussian with a shared covariance, so the linear")
    print("  discriminant is the correct model and its errors are irreducible")
    print("  band-wise standard deviations (reflectance): "
          + ", ".join(f"{SD[j]:.3f}" for j in range(len(BANDS))))

    idx = RNG.permutation(pixels.shape[0])
    train, test = idx[:500], idx[500:]

    section("2. Six bands, a balanced training set: the reference numbers")
    model = train_lda(pixels[train], labels[train])
    po6, kap6 = report("all six bands, 500 training pixels:",
                       labels[test], predict_lda(pixels[test], model))

    section("3. Three bands instead of six: what is lost")
    bands = np.arange(N_BANDS_MIN)
    model3 = train_lda(pixels[train][:, bands], labels[train])
    po3, kap3 = report("visible bands only (blue, green, red):",
                       labels[test], predict_lda(pixels[test][:, bands], model3))
    print(f"  kappa falls from {kap6:.3f} to {kap3:.3f}: the near-infrared and")
    print(f"  short-wave infrared carry most of the vegetation and moisture")
    print(f"  information, and discarding them costs {kap6 - kap3:.3f} kappa")

    section("4. A rare class in the training set")
    rare, rare_name = 3, "cropland"          # confusable with forest in NIR/SWIR
    rare_train = np.nonzero(labels[train] == rare)[0]
    drop = RNG.choice(rare_train, rare_train.size - 20, replace=False)
    keep = np.setdiff1d(np.arange(train.size), drop)
    sub_train = train[keep]
    model_r = train_lda(pixels[sub_train], labels[sub_train])
    po_r, kap_r = report(f"{rare_name} thinned from {rare_train.size} to "
                         f"{rare_train.size - drop.size} training pixels:",
                         labels[test], predict_lda(pixels[test], model_r))
    share_tr = float(np.mean(labels[sub_train] == rare))
    share_true = float(np.mean(labels == rare))
    print(f"  the {rare_name} mean is still estimated, but the TRAINING PRIOR is")
    print(f"  now wrong: {rare_name} is {100 * share_tr:.1f}% of the training set")
    print(f"  and {100 * share_true:.1f}% of the scene, so the rule under-predicts")
    print(f"  {rare_name} and its recall falls even though nothing about the spectra")
    print("  changed.  A decision rule carries its training prior into the field;")
    print("  it must be stated, and re-set if the deployment shares differ.")

    section("5. A haze offset present only in the test scene")
    haze = np.zeros(pixels.shape[1])
    haze[:3] = 0.02
    po_h, kap_h = report("+0.02 reflectance in the visible bands at test time:",
                         labels[test],
                         predict_lda(pixels[test] + haze, model))
    print(f"  kappa falls from {kap6:.3f} to {kap_h:.3f}: an unnoticed")
    print("  radiometric difference between the training and the deployment scene")
    print("  costs more than a classification error would suggest, and it is")
    print("  invisible in every training statistic, which is why it belongs in a")
    print("  deployment report rather than in the accuracy table")
    print("\nSYNTHETIC: these spectra are generated here.  A real classification")
    print("must report the acquisition dates, the atmospheric correction, the")
    print("ground-truth protocol and the class definitions used.")


if __name__ == "__main__":
    main()
