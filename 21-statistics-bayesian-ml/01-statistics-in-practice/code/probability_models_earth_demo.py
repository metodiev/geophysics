#!/usr/bin/env python3
"""Choosing a probability model for SYNTHETIC Earth data: the normal and the
lognormal fitted to the same right-skewed sample, compared by likelihood,
Kolmogorov-Smirnov distance and tail probability, followed by block maxima and
their extreme-value limit.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python probability_models_earth_demo.py

Everything is SYNTHETIC.  The "permeability" values are drawn from a lognormal
law with stated parameters and the block maxima come from a Gaussian with
stated parameters; no measured value is used.

Sections
--------
1. Sample moments versus the lognormal closed forms.
2. Normal versus lognormal: likelihood, AIC and KS distance.
3. Tail probability: what each model predicts beyond the largest sample.
4. Block maxima and the Gumbel/GEV fit.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

N = 4000
MEDIAN = 100.0   # median permeability, mD
SIGMA_LN = 1.0   # log-scale standard deviation, dimensionless
THRESHOLD = 1000.0  # tail threshold, mD
BLOCK = 50           # block size for the maxima
N_BLOCKS = 1500


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    print("SYNTHETIC permeability: 4000 lognormal draws with median "
          f"{MEDIAN:.0f} mD and log-sd {SIGMA_LN:.2f}.")

    x = RNG.lognormal(mean=np.log(MEDIAN), sigma=SIGMA_LN, size=N)

    section("1. Sample moments versus lognormal closed forms")
    mu_ln = np.log(MEDIAN)
    mean_th = np.exp(mu_ln + SIGMA_LN ** 2 / 2.0)
    var_th = (np.exp(SIGMA_LN ** 2) - 1.0) * np.exp(2.0 * mu_ln + SIGMA_LN ** 2)
    skew_th = (np.exp(SIGMA_LN ** 2) + 2.0) * np.sqrt(np.exp(SIGMA_LN ** 2) - 1.0)
    print(f"  mean      sample = {x.mean():9.2f} mD   theory = {mean_th:9.2f} mD")
    print(f"  median    sample = {np.median(x):9.2f} mD   theory = {MEDIAN:9.2f} mD")
    print(f"  std       sample = {x.std(ddof=1):9.2f} mD   theory = "
          f"{np.sqrt(var_th):9.2f} mD")
    print(f"  skewness  sample = {stats.skew(x, bias=False):9.3f}      theory = "
          f"{skew_th:9.3f}")
    print("  the mean sits above the median by a factor "
          f"{x.mean() / np.median(x):.2f}: that is the signature of skew.")

    section("2. Normal versus lognormal: likelihood, AIC and KS distance")
    mu_n, sd_n = stats.norm.fit(x)
    shape, loc, scale = stats.lognorm.fit(x, floc=0.0)
    ll_n = float(np.sum(stats.norm.logpdf(x, mu_n, sd_n)))
    ll_ln = float(np.sum(stats.lognorm.logpdf(x, shape, loc, scale)))
    aic_n = 2 * 2 - 2 * ll_n
    aic_ln = 2 * 3 - 2 * ll_ln
    ks_n = stats.kstest(x, lambda v: stats.norm.cdf(v, mu_n, sd_n))
    ks_ln = stats.kstest(x, lambda v: stats.lognorm.cdf(v, shape, loc, scale))
    print(f"  normal    : log-likelihood = {ll_n:11.1f}   AIC = {aic_n:9.1f}   "
          f"KS D = {ks_n.statistic:.4f}")
    print(f"  lognormal : log-likelihood = {ll_ln:11.1f}   AIC = {aic_ln:9.1f}   "
          f"KS D = {ks_ln.statistic:.4f}")
    print(f"  fitted lognormal: sigma_log = {shape:.3f} (truth {SIGMA_LN:.3f}), "
          f"median = {scale * np.exp(0):.1f} mD (truth {MEDIAN:.0f} mD)")
    print(f"  AIC difference (normal - lognormal) = {aic_n - aic_ln:.1f}; "
          "positive favours the lognormal.")

    section("3. Tail probability P(X > 1000 mD)")
    p_emp = float(np.mean(x > THRESHOLD))
    p_n = float(stats.norm.sf(THRESHOLD, mu_n, sd_n))
    p_ln = float(stats.lognorm.sf(THRESHOLD, shape, loc, scale))
    print(f"  empirical fraction        = {p_emp:.5f}  ({int(p_emp * N)} of {N})")
    print(f"  normal model predicts     = {p_n:.3e}")
    print(f"  lognormal model predicts  = {p_ln:.5f}")
    print("  the normal assigns a probability "
          f"{p_ln / max(p_n, 1e-300):.1f}x smaller than the lognormal, and "
          f"{(p_ln / max(p_n, 1e-300)) / (p_ln / max(p_emp, 1e-300)):.1f}x "
          "smaller than the empirical value suggests.")
    print("  the number of samples does not constrain the tail beyond the largest")
    print(f"  observation ({x.max():.1f} mD); anything past it is model.")

    section("4. Block maxima and the extreme-value limit")
    normals = RNG.standard_normal(BLOCK * N_BLOCKS).reshape(N_BLOCKS, BLOCK)
    maxima = normals.max(axis=1)
    c, loc_g, scale_g = stats.genextreme.fit(maxima)
    print(f"  {N_BLOCKS} block maxima of {BLOCK} standard normals")
    print(f"  GEV shape parameter xi = {c:+.4f} (Gumbel limit: 0)")
    print(f"  fitted location = {loc_g:.4f}, scale = {scale_g:.4f}")
    for T in (10.0, 100.0, 1000.0):
        level = stats.genextreme.ppf(1.0 - 1.0 / T, c, loc_g, scale_g)
        print(f"  return level for a {T:6.0f}-block period = {level:.4f} "
              "(standard-normal units)")
    print(f"  sample maximum over {BLOCK * N_BLOCKS} normals = "
          f"{normals.max():.4f}; the Gaussian normalising constant "
          f"sqrt(2 ln n) = {np.sqrt(2 * np.log(BLOCK * N_BLOCKS)):.4f}.")


if __name__ == "__main__":
    main()
