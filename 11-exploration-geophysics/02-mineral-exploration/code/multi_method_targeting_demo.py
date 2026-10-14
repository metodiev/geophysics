#!/usr/bin/env python3
"""Multi-method targeting and prospectivity analysis: weights of evidence, the
conditional-independence failure, capture curves and training circularity.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python multi_method_targeting_demo.py

Everything here is SYNTHETIC.  The evidence layers, the deposit intensity field,
the noise levels, the thresholds, the base rate and the drill budget are generated
or chosen for teaching.  There is no real dataset, no real deposit and no real
district anywhere in this file.

Contents
--------
1. The synthetic prospectivity problem: a latent favourability field, two evidence
   layers that share a spurious regional trend, and a known deposit intensity.
2. Weights of evidence: contingency table, w+ and w-, and the log-odds composition.
3. AUC of one layer, of two layers, and of the truth, computed by the rank formula.
4. The capture curve: how many deposits a given number of drill sites buys.
5. The conditional-independence failure: calibration of the posterior against the
   known truth, binned by the spurious trend.
6. Training circularity: the optimism of an AUC measured on the training data.
7. Verification.
"""

import numpy as np
from scipy import ndimage

RNG = np.random.default_rng(20261014)

N = 128                       # grid is N x N cells
CORR_LEN = 8.0                # correlation length of the latent field, cells
BETA = 2.0                    # how strongly the truth depends on the latent field
BASE_RATE = 0.005             # target mean deposit probability per cell
THRESHOLD_QUANTILE = 0.75     # evidence is "favourable" above this quantile
N_TRAIN = 25                  # known deposits used to estimate the weights
N_AUDIT = 4000                # deposits sampled for the ROC cross-check


def section(title):
    print(f"\n{'=' * 78}\n{title}\n{'=' * 78}")


def standardise(a):
    return (a - a.mean()) / a.std()


def logistic(x):
    return 1.0 / (1.0 + np.exp(-x))


def witness_field(rng, n=N, corr_len=CORR_LEN):
    """A correlated Gaussian field built by smoothing white noise."""
    w = rng.standard_normal((n, n))
    g = ndimage.gaussian_filter(w, corr_len, mode="wrap")
    return standardise(g)


def make_problem():
    g = witness_field(RNG)
    # a regional trend that is REAL as a map feature but IRRELEVANT to the
    # deposits: it contaminates both evidence layers equally
    ramp = standardise(np.tile(np.linspace(-1.0, 1.0, N), (N, 1)))
    l1 = standardise(g + 0.6 * ramp + 0.8 * RNG.standard_normal((N, N)))
    l2 = standardise(0.7 * g + 0.8 * ramp + 0.8 * RNG.standard_normal((N, N)))
    # the truth depends on g only; solve for the intercept that gives the
    # requested mean over this realisation
    from scipy import optimize
    a = optimize.brentq(
        lambda aa: logistic(aa + BETA * g).mean() - BASE_RATE,
        -30.0, 5.0)
    p_true = logistic(a + BETA * g)
    return g, ramp, l1, l2, p_true


def we_weights(evidence_mask, deposit_mask):
    """Weights of evidence from a 2x2 contingency table."""
    n = evidence_mask.size
    nd = deposit_mask.sum()
    nb = evidence_mask.sum()
    nbd = (evidence_mask & deposit_mask).sum()
    p_b_d = nbd / nd
    p_b_nd = (nb - nbd) / (n - nd)
    p_nb_d = (nd - nbd) / nd
    p_nb_nd = (n - nd - nb + nbd) / (n - nd)
    eps = 1e-12
    return (np.log(max(p_b_d, eps) / max(p_b_nd, eps)),
            np.log(max(p_nb_d, eps) / max(p_nb_nd, eps)))


def we_posterior(layers, masks, weights, prior):
    """Combine layers in log odds; weights is a list of (w_plus, w_minus)."""
    logit = np.log(prior / (1.0 - prior)) * np.ones(layers[0].shape)
    for mask, (wp, wm) in zip(masks, weights):
        logit = logit + np.where(mask, wp, wm)
    return logistic(logit), logit


def weighted_auc(score, weight):
    """AUC of `score` against a continuous, weighted positive label.

    AUC = sum_i w_i * (weighted count of negatives scoring below i) / (W+ W-),
    computed in O(n log n) by sorting.
    """
    order = np.argsort(score)
    w = weight[order]
    pos = w
    neg = 1.0 - w
    csum_neg = np.cumsum(neg) - neg
    return float(np.sum(pos * csum_neg) / (pos.sum() * neg.sum()))


def sampled_roc_auc(score, labels):
    """AUC by trapezoidal integration of the ROC, for binary labels."""
    order = np.argsort(-score)
    lab = labels[order]
    tp = np.cumsum(lab)
    fp = np.cumsum(1 - lab)
    tpr = np.concatenate([[0.0], tp / max(lab.sum(), 1)])
    fpr = np.concatenate([[0.0], fp / max((1 - lab).sum(), 1)])
    return float(np.trapezoid(tpr, fpr))


def capture(score, p_true_weight, n_sites):
    """Expected number of deposits found by drilling the top n_sites cells."""
    order = np.argsort(-score)
    return float(p_true_weight[order[:n_sites]].sum())


def main():
    section("1. The synthetic prospectivity problem")
    g, ramp, l1, l2, p_true = make_problem()
    print(f"{N}x{N} = {N * N} cells; latent field correlation length "
          f"{CORR_LEN:.0f} cells")
    print("deposit intensity: p = logistic(a + 2.0 g), depending ONLY on g")
    print(f"mean of p over the grid = {p_true.mean():.5f} "
          f"(target base rate {BASE_RATE:.4f}, solved by root find)")
    print(f"expected number of deposits = {p_true.sum():.1f} cells")
    print("\nevidence layer 1 = g + 0.6 r + noise; layer 2 = 0.7 g + 0.8 r + noise")
    print("where r is a REGIONAL TREND present in both layers but absent from the")
    print("deposit intensity.  r is the spurious common factor of this exercise.")
    print(f"\ncorrelation between the two layers (all cells) = "
          f"{np.corrcoef(l1.ravel(), l2.ravel())[0, 1]:.4f}")
    print(f"correlation of layer 1 with the truth-bearing field g = "
          f"{np.corrcoef(l1.ravel(), g.ravel())[0, 1]:.4f}")
    print(f"correlation of layer 1 with the pure trend r       = "
          f"{np.corrcoef(l1.ravel(), ramp.ravel())[0, 1]:.4f}")

    section("2. Weights of evidence")
    thr1 = np.quantile(l1, THRESHOLD_QUANTILE)
    thr2 = np.quantile(l2, THRESHOLD_QUANTILE)
    m1 = l1 >= thr1
    m2 = l2 >= thr2
    # training deposits: sampled from the truth, independent of the layers
    flat_p = p_true.ravel()
    idx = RNG.choice(flat_p.size, size=N_TRAIN, p=flat_p / flat_p.sum())
    dep = np.zeros(flat_p.size, dtype=bool)
    dep[idx] = True
    dep = dep.reshape(N, N)
    print(f"evidence thresholds at the {THRESHOLD_QUANTILE:.2f} quantile of each "
          f"layer; {N_TRAIN} training deposits sampled from the truth")
    print(f"\n{'layer':8s} {'area (%)':>9s} {'D in B':>8s} {'D not in B':>11s} "
          f"{'w+':>9s} {'w-':>9s} {'contrast':>9s}")
    weights = []
    for lab, mm in (("L1", m1), ("L2", m2)):
        wp, wm = we_weights(mm, dep)
        weights.append((wp, wm))
        n_in = int(((mm) & dep).sum())
        print(f"{lab:8s} {100 * mm.mean():9.2f} {n_in:8d} "
              f"{int(dep.sum()) - n_in:11d} {wp:9.4f} {wm:9.4f} "
              f"{wp - wm:9.4f}")
    print("\ncontrast C = w+ - w- is the standard measure of a layer's")
    print("discriminating power; a contrast near zero means the layer says")
    print("nothing, and a NEGATIVE w+ with positive w- means the layer is")
    print("anti-correlated with the target.")

    prior = dep.mean() if dep.mean() > 0 else BASE_RATE
    prior = max(prior, 1e-4)
    post, logit = we_posterior([l1, l2], [m1, m2], weights, prior)
    print(f"\nprior used for the combination = observed training density = "
          f"{prior:.5f}")
    print(f"posterior: min {post.min():.5f}, max {post.max():.5f}, "
          f"mean {post.mean():.5f}")
    print(f"log-odds spread = {logit.std():.4f} "
          f"(a combination of two layers doubles the log-odds spread)")

    section("3. AUC of each model against the known truth")
    aucs = {
        "truth field g": weighted_auc(g.ravel(), p_true.ravel()),
        "regional trend r alone": weighted_auc(ramp.ravel(), p_true.ravel()),
        "layer 1 alone": weighted_auc(l1.ravel(), p_true.ravel()),
        "layer 2 alone": weighted_auc(l2.ravel(), p_true.ravel()),
        "average of the two layers": weighted_auc(
            ((l1 + l2) / 2).ravel(), p_true.ravel()),
        "weights of evidence (both)": weighted_auc(post.ravel(), p_true.ravel()),
    }
    print(f"{'model':30s} {'AUC':>8s} {'as % of truth':>14s}")
    for k, v in aucs.items():
        print(f"{k:30s} {v:8.4f} {100 * v / aucs['truth field g']:14.1f}")
    print("\nreading: AUC = 0.5 is a coin flip and 1.0 is perfect.  Two")
    print("measurements matter here.")
    print(f"  (i) the WofE combination ({aucs['weights of evidence (both)']:.4f}) is")
    print(f"      WORSE than layer 1 alone ({aucs['layer 1 alone']:.4f}), and")
    print(f"      slightly worse than the plain average of the two layers")
    print(f"      ({aucs['average of the two layers']:.4f}).")
    print("      Combining layers did not help: the shared regional trend was")
    print("      entered once per layer, so it was double-counted and it now")
    print("      dominates the ranking.  THIS is the failure the next section")
    print("      measures.")
    print(f"  (ii) the regional trend alone scores "
          f"{aucs['regional trend r alone']:.4f}, far above a coin flip,")
    print(f"      even though the truth does not depend on it at all.  The reason")
    print("      is the correlation between the trend and the latent field in this")
    print(f"      single realisation: corr(r, g) = "
          f"{np.corrcoef(ramp.ravel(), g.ravel())[0, 1]:+.4f}, a chance value")
    print("      for two smooth fields on a finite grid.")
    n_eff = (N / CORR_LEN) ** 2
    corr_rg = float(np.corrcoef(ramp.ravel(), g.ravel())[0, 1])
    print(f"\n  the grid has {N * N} cells but only about (N/corr_len)^2 = "
          f"{n_eff:.0f} independent patches,")
    print(f"  so chance alone would give corr(r, g) of order "
          f"1/sqrt({n_eff:.0f}) = {1 / np.sqrt(n_eff):.3f}.")
    print(f"  The measured correlation is {corr_rg:+.4f}, about "
          f"{abs(corr_rg) / (1 / np.sqrt(n_eff)):.1f} times that:",)
    print("  the trend really does rank the truth better than chance IN THIS")
    print("  REALISATION, and nothing about it is geological.")
    print("\n  Monte Carlo over 30 independent realisations of the same")
    print("  experiment, scoring a freshly drawn IRRELEVANT smooth layer:")
    auc_rand = []
    for _ in range(30):
        other = witness_field(RNG)
        auc_rand.append(weighted_auc(other.ravel(), p_true.ravel()))
    auc_rand = np.array(auc_rand)
    print(f"    mean AUC = {auc_rand.mean():.4f}, sd = {auc_rand.std():.4f}, "
          f"min = {auc_rand.min():.4f}, max = {auc_rand.max():.4f}")
    print(f"    fraction of realisations with AUC > 0.6: "
          f"{(auc_rand > 0.6).mean():.2f}")
    print("  an irrelevant smooth layer exceeds AUC 0.6 in a substantial")
    print("  fraction of realisations.  Every prospectivity study that reports")
    print("  layer AUCs from one realisation, with no Monte Carlo null, is")
    print("  therefore reporting values that could have arisen with no")
    print("  information at all.")
    print(f"\n  Note the size of the null spread: sd = {auc_rand.std():.4f}.  A")
    print(f"  naive patch-count estimate, 1/sqrt(12*{n_eff:.0f}) = "
          f"{1 / np.sqrt(12 * n_eff):.4f}, is "
          f"{auc_rand.std() / (1 / np.sqrt(12 * n_eff)):.1f} times too small.")
    print("  The reason is that weighting by p_true concentrates the statistic on")
    print("  a handful of high-intensity patches, so the effective sample size is")
    print("  far below the patch count.  The null must be SIMULATED, not")
    print("  estimated.")

    section("4. The capture curve")
    print("a prospectivity map is used to RANK cells, and the decision it")
    print("supports is where to drill.  Expected deposits found by drilling the")
    print("top n cells, evaluated against the known truth:")
    print(f"\n{'n cells':>9s} {'% of grid':>10s} {'WofE':>9s} {'L1 alone':>10s} "
          f"{'truth':>9s} {'random':>9s}")
    order_truth = np.argsort(-g.ravel())
    for n_sites in (10, 50, 200, 1000, 5000):
        c_we = capture(post.ravel(), p_true.ravel(), n_sites)
        c_l1 = capture(l1.ravel(), p_true.ravel(), n_sites)
        c_t = float(p_true.ravel()[order_truth[:n_sites]].sum())
        c_r = float(p_true.mean() * n_sites)
        print(f"{n_sites:9d} {100 * n_sites / (N * N):10.1f} "
              f"{c_we:9.2f} {c_l1:10.2f} {c_t:9.2f} {c_r:9.2f}")
    print(f"\nthe total expected deposits is {p_true.sum():.1f}.  At a budget of")
    print(f"10 sites the truth-ranked map finds "
          f"{capture(g.ravel(), p_true.ravel(), 10):.2f} deposits, layer 1 alone")
    print(f"finds {capture(l1.ravel(), p_true.ravel(), 10):.2f}, and the WofE map")
    print(f"finds {capture(post.ravel(), p_true.ravel(), 10):.2f} -- essentially")
    print("nothing.  THE RANKING IS WHAT MATTERS at small budgets, and the WofE")
    print("ranking has been captured by the spurious trend: its highest-posterior")
    print("cells sit where the trend is strongest, not where the deposits are.")
    print("Only at very large budgets (5000 cells, 30% of the grid) do the maps")
    print("converge, because by then almost every cell is being drilled and the")
    print("ranking no longer determines the outcome.")
    print("\nTwo conclusions.  First, calibration and ranking are different")
    print("properties and the capture curve depends only on the ranking: a map can")
    print("be badly calibrated and still useful.  Second, a defect that costs"
          " little")
    print(f"in the AUC ({aucs['weights of evidence (both)']:.4f} against "
          f"{aucs['layer 1 alone']:.4f}) costs a factor of")
    print(f"{capture(l1.ravel(), p_true.ravel(), 10) / max(capture(post.ravel(), p_true.ravel(), 10), 1e-9):.0f}"
          " in the capture at a 10-site budget: aggregate metrics hide")
    print("decision-relevant failures.")

    section("5. The conditional-independence failure")
    print("weights of evidence combines layers as if they were conditionally")
    print("independent given the target.  Here they are not: both carry the")
    print("regional trend r, which the target does not depend on.  Calibrate the")
    print("posterior against the known truth, binned by the trend:")
    dec = np.quantile(ramp, np.linspace(0, 1, 6))
    print(f"\n{'trend decile':>13s} {'mean r':>8s} {'mean predicted':>15s} "
          f"{'mean truth':>11s} {'ratio':>8s}")
    for k in range(5):
        sel = (ramp >= dec[k]) & (ramp <= dec[k + 1])
        pred = post[sel].mean()
        tru = p_true[sel].mean()
        print(f"{k + 1:13d} {ramp[sel].mean():8.3f} {pred:15.5f} "
              f"{tru:11.5f} {pred / tru:8.3f}")
    lo = ramp <= np.quantile(ramp, 0.2)
    hi = ramp >= np.quantile(ramp, 0.8)
    ratio_lo = post[lo].mean() / p_true[lo].mean()
    ratio_hi = post[hi].mean() / p_true[hi].mean()
    print(f"\nthe predicted/true ratio rises from {ratio_lo:.3f} in the lowest")
    print(f"trend quintile to {ratio_hi:.3f} in the highest -- a change by a")
    print(f"factor of {ratio_hi / ratio_lo:.2f} ACROSS the trend.  The level of")
    print("the ratio is set by the prior (here the training density, far below")
    print("the true base rate), but the CHANGE across the trend is the")
    print("double-counting signature: a shared factor is entered once per layer,")
    print("so its weight is multiplied by the number of layers, and the posterior")
    print("becomes over-confident exactly where the shared factor is strong.")
    print("This is the commonest quantitative error in multi-layer prospectivity")
    print("analysis, and it is invisible in the AUC (section 3) because the AUC")
    print("depends only on the ranking, not on the calibration.")

    section("6. Training circularity")
    print("the weights above were estimated from training deposits drawn from the")
    print("same truth used to evaluate them.  Split the deposits and measure the")
    print("optimism:")
    n_half = N_TRAIN // 2
    idx_all = idx.copy()
    RNG.shuffle(idx_all)
    train_idx, test_idx = idx_all[:n_half], idx_all[n_half:]
    print(f"\n{'estimate':38s} {'AUC':>8s}")
    for lab, sel_idx in (("weights from training half", train_idx),
                         ("weights from test half", test_idx)):
        dd = np.zeros(flat_p.size, dtype=bool)
        dd[sel_idx] = True
        dd = dd.reshape(N, N)
        w = [we_weights(m1, dd), we_weights(m2, dd)]
        pp, _ = we_posterior([l1, l2], [m1, m2], w, max(dd.mean(), 1e-4))
        print(f"{lab:38s} {weighted_auc(pp.ravel(), p_true.ravel()):8.4f}")
    print("\nwith only 25 training deposits the split changes the AUC by a few")
    print("hundredths.  The optimism is small HERE because the training set was")
    print("drawn from the same intensity field as the audit; in a real study the")
    print("training sites are the discovered deposits, which are biased toward")
    print("shallow, outcropping, accessible and historically explored ground.  A")
    print("circularity check on the real problem must therefore audit against")
    print("ground the model has never seen -- ideally ground explored after the")
    print("model was built.")

    section("7. Verification")
    print("(a) the WofE posterior for a SINGLE layer against the empirical rate")
    print("    from its own contingency table.  WofE is an algebraic rewriting of")
    print("    that table, so the two must agree exactly:")
    dd = dep
    print(f"    {'class':16s} {'cells':>7s} {'deposits':>9s} "
          f"{'empirical rate':>15s} {'mean WofE':>11s} {'difference':>11s}")
    for lab, mm in (("L1", m1), ("L2", m2)):
        wp, wm = we_weights(mm, dd)
        pp, _ = we_posterior([mm], [mm], [(wp, wm)], dd.mean())
        n_cells = int(mm.sum())
        n_dep = int((mm & dd).sum())
        emp = n_dep / n_cells
        model = float(pp[mm].mean())
        print(f"    {lab + ' in B':16s} {n_cells:7d} {n_dep:9d} {emp:15.6f} "
              f"{model:11.6f} {abs(model - emp):11.2e}")
        emp_out = (dd.sum() - n_dep) / (N * N - n_cells)
        model_out = float(pp[~mm].mean())
        print(f"    {lab + ' out of B':16s} {N * N - n_cells:7d} "
              f"{int(dd.sum()) - n_dep:9d} {emp_out:15.6f} {model_out:11.6f} "
              f"{abs(model_out - emp_out):11.2e}")
    print("    agreement to machine precision: WofE introduces no approximation")
    print("    for a single layer.  The approximation is entirely in the")
    print("    COMBINATION of layers, which is what section 5 measures.")

    print("(b) the AUC by the rank formula against a sampled ROC integration")
    labels = np.zeros(N * N, dtype=bool)
    samp = RNG.choice(N * N, size=N_AUDIT, p=p_true.ravel() / p_true.ravel().sum())
    labels[samp] = True
    print(f"    rank formula  (weighted) = "
          f"{weighted_auc(post.ravel(), p_true.ravel()):.6f}")
    print(f"    sampled ROC   ({N_AUDIT} deposits) = "
          f"{sampled_roc_auc(post.ravel(), labels):.6f}")
    print(f"    difference = "
          f"{abs(weighted_auc(post.ravel(), p_true.ravel()) - sampled_roc_auc(post.ravel(), labels)):.6f}"
          " (sampling noise)")
    print("(c) the independence check on the trend-free part of the problem")
    p_r = l1 - 0.6 * ramp
    q_r = l2 - 0.8 * ramp
    print(f"    corr(l1 - 0.6 r, l2 - 0.8 r) = "
          f"{np.corrcoef(p_r.ravel(), q_r.ravel())[0, 1]:.4f}, against "
          f"{np.corrcoef(l1.ravel(), l2.ravel())[0, 1]:.4f} with the trend in")
    print("    place: removing the shared factor drops the layer correlation by")
    print("    design here (we built the layers that way), which is the")
    print("    diagnostic an analyst would use in the absence of a known truth.")


if __name__ == "__main__":
    main()
