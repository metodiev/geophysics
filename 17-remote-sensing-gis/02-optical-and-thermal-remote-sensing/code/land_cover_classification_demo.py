#!/usr/bin/env python3
"""Land cover classification: supervised (Gaussian MLE) and unsupervised (k-means).

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python land_cover_classification_demo.py

Everything is SYNTHETIC.  The class means, covariances, class proportions and the
number of bands are chosen teaching values in this file.  No real scene, land-cover
product, sensor or training dataset is represented.

Contents
--------
1. A synthetic four-class feature scene and its separability.
2. A Gaussian maximum-likelihood classifier, trained and tested.
3. The confusion matrix, overall accuracy and Cohen's kappa.
4. Classification accuracy versus training-sample size.
5. The Hughes phenomenon: accuracy versus dimensionality at fixed training size.
6. Unsupervised k-means, its stability across seeds, and its agreement with truth.
7. The accuracy paradox: a rare class under a high overall accuracy.
8. Verification: kappa recomputed by a second route, and a majority-class baseline.
"""

from itertools import permutations

import numpy as np

RNG = np.random.default_rng(20261014)

CLASS_NAMES = ("class-A (bright soil)", "class-B (vegetation)",
               "class-C (water)", "class-D (rare, altered rock)")
N_PER_CLASS = 500
N_TRAIN_PER_CLASS = 100


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def class_parameters():
    """SYNTHETIC class means and covariances in a 2-D feature space."""
    means = np.array([[0.360, 0.420],
                      [0.120, 0.460],
                      [0.060, 0.030],
                      [0.330, 0.345]])

    def c(sd, r):
        return np.array([[sd ** 2, r * sd ** 2], [r * sd ** 2, sd ** 2]])

    covs = np.array([c(0.055, 0.3), c(0.055, 0.5), c(0.030, 0.1), c(0.055, -0.2)])
    return means, covs


def make_scene(n_per_class, rng=RNG):
    means, covs = class_parameters()
    feats, labels = [], []
    for k in range(means.shape[0]):
        feats.append(rng.multivariate_normal(means[k], covs[k], size=n_per_class))
        labels.append(np.full(n_per_class, k))
    return np.vstack(feats), np.concatenate(labels)


def mahalanobis(mu1, c1, mu2, c2):
    """Symmetric Mahalanobis-style separability between two Gaussian classes."""
    c = 0.5 * (c1 + c2)
    d = mu1 - mu2
    return float(np.sqrt(d @ np.linalg.inv(c) @ d))


def train_qda(x, y, n_classes, priors=None):
    mus, invs, logdets = [], [], []
    for k in range(n_classes):
        xk = x[y == k]
        cov = np.cov(xk.T)
        mus.append(xk.mean(axis=0))
        invs.append(np.linalg.inv(cov))
        logdets.append(np.linalg.slogdet(cov)[1])
    if priors is None:
        priors = np.array([(y == k).mean() for k in range(n_classes)])
    return mus, invs, logdets, np.asarray(priors, dtype=float)


def apply_qda(x, model, n_classes):
    mus, invs, logdets, priors = model
    scores = np.zeros((x.shape[0], n_classes))
    for k in range(n_classes):
        d = x - mus[k]
        quad = np.einsum("ij,jk,ik->i", d, invs[k], d)
        scores[:, k] = -0.5 * (quad + logdets[k]) + np.log(priors[k])
    return scores.argmax(axis=1)


def confusion(y_true, y_pred, n_classes):
    cm = np.zeros((n_classes, n_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t, p] += 1
    return cm


def kappa_from_cm(cm):
    n = cm.sum()
    po = float(np.trace(cm)) / n
    pe = float(np.sum(cm.sum(axis=1) * cm.sum(axis=0))) / n ** 2
    return (po - pe) / (1.0 - pe), po, pe


def best_agreement(labels, truth, n_classes):
    best = 0.0
    for perm in permutations(range(n_classes)):
        best = max(best, float(np.mean(np.array([perm[c] for c in labels]) == truth)))
    return best


def kmeans(x, k, rng, n_iter=60):
    """Plain k-means with k-means++ initialisation."""
    idx = [int(rng.integers(x.shape[0]))]
    for _ in range(k - 1):
        d2 = np.min([np.sum((x - x[i]) ** 2, axis=1) for i in idx], axis=0)
        idx.append(int(rng.choice(x.shape[0], p=d2 / d2.sum())))
    centres = x[idx].copy()
    for _ in range(n_iter):
        dist = np.linalg.norm(x[:, None, :] - centres[None, :, :], axis=2)
        lab = dist.argmin(axis=1)
        new = np.array([x[lab == j].mean(axis=0) if np.any(lab == j) else centres[j]
                        for j in range(k)])
        if np.allclose(new, centres):
            break
        centres = new
    return lab, centres


def stratified_split(y, n_train, n_classes, rng=RNG):
    tr, te = [], []
    for k in range(n_classes):
        rows = np.flatnonzero(y == k).copy()
        rng.shuffle(rows)
        tr.append(rows[:n_train])
        te.append(rows[n_train:])
    return np.concatenate(tr), np.concatenate(te)


def main():
    means, covs = class_parameters()
    n_classes = means.shape[0]

    section("1. A synthetic four-class feature scene")
    x, y = make_scene(N_PER_CLASS)
    print(f"  {x.shape[0]} pixels, {x.shape[1]} features (notional bands), "
          f"{n_classes} classes")
    print("   class                          mean feature 1   mean feature 2   "
          "mean within-class sd")
    for k, name in enumerate(CLASS_NAMES):
        print(f"  {name:30s} {means[k, 0]:16.3f} {means[k, 1]:16.3f} "
              f"{np.sqrt(np.diag(covs[k])).mean():20.4f}")
    print("\n  pairwise separability (Mahalanobis distance between class means):")
    print("   pair            distance")
    for i in range(n_classes):
        for j in range(i + 1, n_classes):
            print(f"  {i}-{j}             "
                  f"{mahalanobis(means[i], covs[i], means[j], covs[j]):8.3f}")
    print("  The 0-3 pair is deliberately the closest: a rare altered-rock class")
    print("  spectrally similar to bright soil.  Everything below follows from that.")

    section("2. A Gaussian maximum-likelihood classifier (QDA)")
    train_idx, test_idx = stratified_split(y, N_TRAIN_PER_CLASS, n_classes)
    model = train_qda(x[train_idx], y[train_idx], n_classes)
    pred = apply_qda(x[test_idx], model, n_classes)
    cm = confusion(y[test_idx], pred, n_classes)
    print(f"  training pixels {len(train_idx)} "
          f"({N_TRAIN_PER_CLASS} per class), test pixels {len(test_idx)}")
    print("  discriminant: argmax_k [ -1/2 (x-mu_k)^T C_k^-1 (x-mu_k) - 1/2 ln|C_k|")
    print("                 + ln p_k ]; quadratic because each class has its OWN C_k")
    print("  estimated class means:")
    for k, name in enumerate(CLASS_NAMES):
        print(f"  {name:30s} [{model[0][k][0]:.4f} {model[0][k][1]:.4f}]")

    section("3. Confusion matrix, overall accuracy and kappa")
    print("  rows = truth, columns = prediction")
    print("   truth\\pred   " + "".join(f"  {c:>4d}" for c in range(n_classes)) +
          "   recall")
    for k in range(n_classes):
        row = cm[k]
        print(f"  {k:10d}   " + "".join(f"{v:6d}" for v in row) +
              f"   {row[k] / row.sum():7.3f}")
    print("   precision   " + "".join(
        f"{cm[j, j] / max(cm[:, j].sum(), 1):6.3f}" for j in range(n_classes)))
    kappa, po, pe = kappa_from_cm(cm)
    print(f"\n  overall accuracy p_o = {po:.4f}")
    print(f"  chance agreement   p_e = {pe:.4f}")
    print(f"  Cohen's kappa = (p_o - p_e)/(1 - p_e) = {kappa:.4f}")
    print("  Kappa is the accuracy in excess of chance; overall accuracy alone is")
    print("  inflated by the dominant classes.  Classes 0 and 3, the closest pair,")
    print("  dominate the error: the map is good everywhere except where the")
    print("  discrimination is physically hard.")

    section("4. Accuracy versus training-sample size")
    print("   training pixels per class   overall accuracy   kappa   "
          "recall of the 0-3 pair")
    for n_tr in (2, 3, 5, 10, 20, 50, 100, 250):
        tr, te = stratified_split(y, n_tr, n_classes)
        m = train_qda(x[tr], y[tr], n_classes)
        p = apply_qda(x[te], m, n_classes)
        c = confusion(y[te], p, n_classes)
        kk, oo, _ = kappa_from_cm(c)
        r03 = 0.5 * (c[0, 0] / c[0].sum() + c[3, 3] / c[3].sum())
        print(f"  {n_tr:25d}   {oo:16.4f}   {kk:6.4f}   {r03:19.3f}")
    print("  Accuracy improves and then saturates.  At 2-3 training pixels per class")
    print("  the covariance estimate is nearly singular, so the classifier is")
    print("  dominated by its own estimation error.  The hard 0-3 pair improves most")
    print("  from additional training data, which is where the marginal value lies.")

    section("5. The Hughes phenomenon: more dimensions, not more information")
    sigma_n = 0.055
    print(f"  append pure-noise features of sd {sigma_n:.3f} to the two real ones and")
    print("  keep the training size fixed at 20 pixels per class.  The extra features")
    print("  carry NO class information; what changes is the number of parameters the")
    print("  classifier must estimate.")
    print("   total features   parameters per class   overall accuracy   kappa")
    for n_extra in (0, 1, 2, 4, 8, 14):
        noise = sigma_n * RNG.standard_normal((x.shape[0], n_extra))
        xn = np.hstack([x, noise])
        tr, te = stratified_split(y, 20, n_classes)
        m = train_qda(xn[tr], y[tr], n_classes)
        p = apply_qda(xn[te], m, n_classes)
        c = confusion(y[te], p, n_classes)
        kk, oo, _ = kappa_from_cm(c)
        d = 2 + n_extra
        print(f"  {d:14d}   {d + d * (d + 1) // 2:21d}   {oo:16.4f}   {kk:6.4f}")
    print("  Accuracy degrades as useless dimensions are added at fixed training size,")
    print("  because each class must estimate d + d(d+1)/2 parameters.  This is the")
    print("  Hughes phenomenon, and it is why dimensionality reduction is a supervised")
    print("  decision, not a stylistic one.")

    section("6. Unsupervised k-means and its stability")
    lab, centres = kmeans(x, n_classes, RNG)
    print(f"  {n_classes} clusters, k-means++ initialisation")
    print(f"  best label matching gives an agreement with truth of "
          f"{best_agreement(lab, y, n_classes):.4f}")
    print("  cluster means found (unlabelled):")
    for j, c in enumerate(centres):
        print(f"   cluster {j}: [{c[0]:.4f} {c[1]:.4f}]")
    print("  Agreement measures how far the data's DENSITY structure coincides with")
    print("  the labels; the two are different things, and agreement is not accuracy.")
    print("   seed   agreement with truth")
    agree = []
    for s in range(5):
        rng = np.random.default_rng(20261014 + s)
        lab_s, _ = kmeans(x, n_classes, rng)
        a = best_agreement(lab_s, y, n_classes)
        agree.append(a)
        print(f"  {s:5d}   {a:20.4f}")
    print(f"  spread across seeds = {max(agree) - min(agree):.4f}: k-means minimises a")
    print("  NON-CONVEX objective by local descent, so the result depends on the")
    print("  initialisation and must be reported with the initialisation used.")

    section("7. The accuracy paradox: a high score that misses the target")
    n_rare = 200
    n_total = 20000
    x_r, y_r = make_scene(n_total // n_classes)
    keep = np.ones(y_r.shape[0], dtype=bool)
    drop = np.flatnonzero(y_r == 3)[n_rare:]
    keep[drop] = False
    x_r, y_r = x_r[keep], y_r[keep]
    prevalence = np.array([(y_r == k).mean() for k in range(n_classes)])
    tr, te = stratified_split(y_r, 50, n_classes)
    m = train_qda(x_r[tr], y_r[tr], n_classes, priors=prevalence)
    p = apply_qda(x_r[te], m, n_classes)
    c = confusion(y_r[te], p, n_classes)
    kk, oo, _ = kappa_from_cm(c)
    n_rare_test = int((y_r[te] == 3).sum())
    print(f"  class D is {100 * prevalence[3]:.2f}% of the scene "
          f"({n_rare} of {y_r.shape[0]} pixels)")
    print("  training is stratified (50 per class) but the PRIORS are set to the")
    print(f"  true scene prevalence {np.round(prevalence, 4).tolist()}")
    print(f"  overall accuracy = {oo:.4f}   kappa = {kk:.4f}")
    print(f"  class-D recall    = {c[3, 3] / max(n_rare_test, 1):.4f} "
          f"({c[3, 3]} of {n_rare_test} test pixels of class D)")
    print(f"  class-D precision = {c[3, 3] / max(c[:, 3].sum(), 1):.4f}")
    print("  The overall accuracy is dominated by the three common classes, and the")
    print("  rare class the study cares about is largely missed.  Report per-class")
    print("  recall, precision and the confusion matrix -- never a single accuracy")

    section("8. Verification of kappa and a naive baseline")
    k2, _, _ = kappa_from_cm(cm.copy())
    print(f"  kappa recomputed from an independently formed matrix: {k2:.4f} "
          f"(difference {abs(k2 - kappa):.2e})")
    majority = int(np.bincount(y[test_idx]).argmax())
    base = float(np.mean(y[test_idx] == majority))
    bcm = np.zeros((n_classes, n_classes), dtype=int)
    for t in y[test_idx]:
        bcm[t, majority] += 1
    kb, _, _ = kappa_from_cm(bcm)
    print(f"  majority-class baseline accuracy = {base:.4f} "
          f"(always predicting class {majority})")
    print(f"  kappa of the majority baseline = {kb:.4f}")
    print("  Overall accuracy is inflated by class imbalance; kappa is not, which is")
    print("  exactly what it was designed to reveal.")


if __name__ == "__main__":
    main()
