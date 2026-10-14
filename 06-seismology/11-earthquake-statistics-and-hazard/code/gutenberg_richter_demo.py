#!/usr/bin/env python3
"""Gutenberg-Richter statistics: b-value estimation, catalogue completeness, and
the sampling variability that limits every claimed b-value anomaly.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gutenberg_richter_demo.py

Everything is SYNTHETIC.  The catalogue is drawn from a *chosen* Gutenberg-
Richter law with b = 1.00 and M_c = 1.00; no real earthquake catalogue is read
and no number is quoted from a published one.  The only non-synthetic numbers
below are exact standard unit conversions (moment and radiated energy from
magnitude), with the relations printed alongside.

Contents
--------
1. Draw a complete synthetic catalogue; compare its largest event with the
   sample-size prediction M_c + log10(N)/b.
2. Estimate b three ways: Aki-Utsu maximum likelihood, least squares on
   cumulative counts, and maximum likelihood with a wrong M_c.
3. Completeness: maximum curvature on a complete catalogue, then the failure of
   maximum curvature on a catalogue whose detection probability fades.
4. Measure the sampling distribution of b-hat and the resolution it allows.
5. Print moment and radiated-energy unit conversions for integer magnitudes.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC population parameters (chosen, not measured) ------------------
B_TRUE = 1.00          # Gutenberg-Richter b-value of the parent population
MC_TRUE = 1.00         # magnitude of completeness of the complete catalogue
N_EVENTS = 5000        # catalogue size of the main synthetic catalogue
DMAG = 0.1             # reporting grid: magnitudes are truncated to 0.1
M_REF = 3.0            # magnitude at which the a-value is reported
M_LOW = 0.5            # lower limit of the incomplete catalogue
M50_DET = 1.00         # magnitude of 50% detection probability
W_DET = 0.20           # width of the logistic detection ramp


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def sample_magnitudes(n, b, mc, rng, dmag=DMAG):
    """Magnitudes from a Gutenberg-Richter law, truncated to the reporting grid.

    For the continuous law with density p(m) = b ln(10) 10^{-b(m-mc)} above mc,
    the CDF is F(m) = 1 - 10^{-b(m-mc)}, so m = mc + (-log10(1-u))/b for
    u ~ U(0,1).  Magnitudes are then truncated DOWN to the grid dmag, the
    convention of a catalogue that reports magnitudes to one decimal.
    """
    u = rng.random(n)
    m = mc + (-np.log10(1.0 - u)) / b
    return np.floor(m / dmag) * dmag


def b_aki_utsu(mags, mc, dmag=DMAG):
    """Aki-Utsu maximum-likelihood b-value for gridded magnitudes.

    b = log10(e) / (mean(m) - (mc - dmag/2)); the dmag/2 term is the standard
    bin-width correction for magnitudes truncated to the reporting grid.
    """
    m = mags[mags >= mc - 1e-9]
    return np.log10(np.e) / (m.mean() - (mc - dmag / 2.0)), m.size


def b_least_squares(mags, mc, mmax, dmag=DMAG):
    """Least-squares slope of log10 N(>=m) versus m over [mc, mmax]."""
    edges = np.arange(mc, mmax + 2.0 * dmag, dmag)
    centers = 0.5 * (edges[:-1] + edges[1:])
    cum = np.array([np.sum(mags >= e) for e in edges[:-1]], dtype=float)
    keep = cum >= 1.0
    return -np.polyfit(centers[keep], np.log10(cum[keep]), 1)[0]


def max_curvature_mc(mags, dmag=DMAG):
    """Magnitude of completeness from the mode of the magnitude histogram
    (the 'maximum curvature' method, uncorrected)."""
    lo = np.floor(mags.min() / dmag) * dmag
    hi = np.ceil(mags.max() / dmag) * dmag + dmag
    edges = np.arange(lo, hi + dmag, dmag)
    counts, _ = np.histogram(mags, bins=edges)
    return float(edges[int(np.argmax(counts))])


def main():
    section("1. A complete synthetic Gutenberg-Richter catalogue")
    print(f"parent law: b = {B_TRUE:.2f}, M_c = {MC_TRUE:.2f} "
          f"(SYNTHETIC: chosen, not measured)")
    mags = sample_magnitudes(N_EVENTS, B_TRUE, MC_TRUE, RNG)
    print(f"\ncatalogue size                            N = {mags.size:d} events")
    print(f"magnitude range                             = {mags.min():.1f} to "
          f"{mags.max():.1f}")
    print(f"mean magnitude                              = {mags.mean():.4f}")
    a_value = np.log10(mags.size) + B_TRUE * MC_TRUE
    print(f"a-value (a = log10 N + b M_c)               = {a_value:.3f} "
          f"decades")
    pred_max = MC_TRUE + np.log10(mags.size) / B_TRUE
    print(f"predicted largest event M_c + log10(N)/b     = {pred_max:.2f}")
    print(f"observed largest event                      = {mags.max():.2f}")
    print("  a finite catalogue cannot contain an event larger than its sample")
    print("  size allows, so the largest event seen is a property of the sample,")
    print("  not of the Earth.  Statements about 'maximum magnitude' need a")
    print("  statistical argument, not the largest event on record.")

    section("2. Estimating b: three routes, three answers")
    b_mle, n_used = b_aki_utsu(mags, MC_TRUE)
    print(f"(a) Aki-Utsu MLE at the TRUE M_c = {MC_TRUE:.2f}:")
    print(f"    events used N            = {n_used:d}")
    print(f"    mean magnitude           = {mags[mags >= MC_TRUE].mean():.4f}")
    print(f"    b_hat (MLE)              = {b_mle:.4f}")
    print(f"    b_true                   = {B_TRUE:.4f}")
    print(f"    relative difference      = "
          f"{(b_mle - B_TRUE) / B_TRUE * 100:+.2f} %")

    b_ls = b_least_squares(mags, MC_TRUE, mags.max())
    print(f"\n(b) least squares on cumulative log10 N(>=m):")
    print(f"    b_hat (LSQ)              = {b_ls:.4f}   "
          f"({(b_ls - B_TRUE) / B_TRUE * 100:+.2f} % of b_true)")
    print("    neighbouring points of a cumulative curve are not independent, so")
    print("    the LSQ slope carries a bias the MLE does not have.")

    print(f"\n(c) the same MLE with a WRONG completeness magnitude:")
    print("      assumed M_c   N used     b_hat     difference from b_true")
    for mc in (0.5, 0.8, MC_TRUE, 1.2, 1.5, 2.0, 2.5):
        b_hat, n = b_aki_utsu(mags, mc)
        print(f"      {mc:11.2f}   {n:6d}   {b_hat:8.4f}   "
              f"{(b_hat - B_TRUE) / B_TRUE * 100:+8.2f} %")
    print("  assuming M_c too LOW averages in magnitudes from a population that")
    print("  is not fully recorded, raising the mean and UNDERESTIMATING b; here")
    print("  it costs more than half the value of b.  Assuming M_c too HIGH keeps")
    print("  fewer events and enlarges the scatter of b_hat.  Completeness is a")
    print("  model choice that has to be justified before b means anything.")

    section("3. Completeness: maximum curvature, complete and incomplete")
    mc_maxc = max_curvature_mc(mags)
    b_at_maxc, _ = b_aki_utsu(mags, mc_maxc)
    print("(a) complete catalogue (every event above M_c = 1.0 is recorded):")
    print(f"    M_c by maximum curvature (uncorrected) = {mc_maxc:.2f}")
    print(f"    true M_c                               = {MC_TRUE:.2f}")
    print(f"    b_hat at the MAXC estimate             = {b_at_maxc:.4f}")
    print(f"    b_hat at the true M_c                  = {b_mle:.4f}")

    print("\n(b) catalogue whose detection probability fades with magnitude:")
    print(f"    logistic detection q(m) = 1/(1+exp(-(m-{M50_DET:.2f})/"
          f"{W_DET:.2f}))")
    n_all = 60000
    u = RNG.random(n_all)
    m_true = M_LOW + (-np.log10(1.0 - u)) / B_TRUE
    q = 1.0 / (1.0 + np.exp(-(m_true - M50_DET) / W_DET))
    m_det = np.floor(m_true[RNG.random(n_all) < q] / DMAG) * DMAG
    mc_99 = M50_DET + np.log(99.0) * W_DET
    mc_99_grid = float(np.ceil(mc_99 / DMAG) * DMAG)
    print(f"    events generated above M = {M_LOW:.1f}  : {n_all:d}")
    print(f"    events detected                     : {m_det.size:d} "
          f"({m_det.size / n_all * 100:.1f} %)")
    print(f"    magnitude of 50% detection           = {M50_DET:.2f}")
    print(f"    magnitude of 99% detection           = {mc_99:.3f} "
          f"-> {mc_99_grid:.2f} on the {DMAG:.1f} reporting grid")
    mc_maxc_det = max_curvature_mc(m_det)
    b_maxc_det, n_maxc_det = b_aki_utsu(m_det, mc_maxc_det)
    b_99, n_99 = b_aki_utsu(m_det, mc_99_grid)
    print(f"    M_c by maximum curvature             = {mc_maxc_det:.2f} "
          f"(N = {n_maxc_det:d})")
    print(f"    b_hat at that M_c                    = {b_maxc_det:.4f} "
          f"({(b_maxc_det - B_TRUE) / B_TRUE * 100:+.2f} % of b_true)")
    print(f"    b_hat above the 99% detection level  = {b_99:.4f} "
          f"({(b_99 - B_TRUE) / B_TRUE * 100:+.2f} % of b_true, N = {n_99:d})")
    print("    Maximum curvature lands where detection is only about 50%")
    print("    complete, so the b-value built on it is biased low even though")
    print("    the detection model is smooth and the simulation exact.")

    section("4. Sampling variability: how well can b be resolved?")
    print("  replicate complete catalogues of size N, estimate b at the true M_c")
    print("      N     mean b_hat   s.d. b_hat   b/sqrt(N) predicted   5%-95%")
    for n_rep in (100, 500, 2000):
        bs = np.empty(400)
        for i in range(400):
            bs[i] = b_aki_utsu(sample_magnitudes(n_rep, B_TRUE, MC_TRUE, RNG),
                               MC_TRUE)[0]
        lo, hi = np.percentile(bs, [5.0, 95.0])
        print(f"  {n_rep:5d}   {bs.mean():9.4f}   {bs.std(ddof=1):10.4f}   "
              f"{B_TRUE / np.sqrt(n_rep):15.4f}   {lo:.3f}-{hi:.3f}")
    print("\n  the standard error of b is approximately b/sqrt(N), so:")
    for n_rep in (100, 500, 5000):
        err = B_TRUE / np.sqrt(n_rep)
        print(f"    N = {n_rep:5d}: 1 s.e. = {err:.3f}, "
              f"2 s.e. (a 95% difference) = {2 * err:.3f}")
    print("  a difference smaller than about 2 s.e. is not evidence of a")
    print("  difference in the parent population.")

    section("5. Magnitude as moment and radiated energy (exact conversions)")
    print("  log10 M0 (N m) = 1.5 M + 9.1      ->  M0 = 10^(1.5 M + 9.1) N m")
    print("  log10 E  (J)   = 1.5 M + 4.8      ->  E  = 10^(1.5 M + 4.8) J")
    print("      M        M0 (N m)              E (J)")
    for m in (4.0, 5.0, 6.0, 7.0, 8.0):
        print(f"    {m:4.1f}   {10.0 ** (1.5 * m + 9.1):12.3e}   "
              f"{10.0 ** (1.5 * m + 4.8):12.3e}")
    print(f"  one magnitude unit multiplies radiated energy by 10^1.5 = "
          f"{10.0 ** 1.5:.2f}")
    print(f"  and by GR multiplies the number of events by 10^b = "
          f"{10.0 ** B_TRUE:.1f}")
    print(f"  so the energy in one magnitude bin grows by 10^(1.5-b) = "
          f"{10.0 ** (1.5 - B_TRUE):.2f} per magnitude unit.")
    print("  When b = 1.5 exactly, every magnitude bin carries the same energy;")
    print("  at b = 1.0 the total is dominated by the largest events.  This is a")
    print("  property of the distribution, not an observation about any")
    print("  particular earthquake.")


if __name__ == "__main__":
    main()
