"""scipy.special and scipy.stats in practice.

Run:  .venv/bin/python special_stats_demo.py
Requires: scipy, numpy.

Companion to lesson 03-03-08. All data are SYNTHETIC, generated in code from
stated parameters with a seeded generator, so every difference reported here
is reproducible.

Part 1  the error function in a diffusion solution, and the two families of
        routines that compute it: erf/erfc/ndtr, and erfcx for the large
        argument where erfc underflows.
Part 2  fitting a Gutenberg-Richter magnitude distribution: maximum likelihood
        against cumulative least squares, with a Monte-Carlo-calibrated
        Kolmogorov-Smirnov p-value rather than the invalid naive one.
Part 3  correlation, sample size and p-values; and intervals from t against
        the normal.
Part 4  a distribution fit that should be rejected.
"""

import math

import numpy as np
from scipy import special, stats

RNG = np.random.default_rng(19740115)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Part 1 -- the error function
# --------------------------------------------------------------------------

def part1_error_function():
    section("1. The error function in a diffusion solution")
    kappa = 1.2e-6                     # m2/s, a nominal rock diffusivity
    YEAR = 3.15576e7
    dt = 12.0                          # K, surface step change
    print("  Half-space cooling: T(z, t)/dT = erfc( z / (2 sqrt(kappa t)) ).")
    print(f"  kappa = {kappa:.2e} m2/s, dT = {dt:.1f} K, values computed with")
    print("  scipy.special.erfc.")
    print(f"    {'t (yr)':>9}{'z (m)':>8}{'z/(2 sqrt(kappa t))':>22}"
          f"{'T/dT':>11}{'T (K)':>10}")
    for yrs in (100.0, 1000.0, 10000.0):
        t = yrs * YEAR
        for z in (50.0, 200.0, 1000.0):
            u = z / (2.0 * math.sqrt(kappa * t))
            print(f"    {yrs:>9.0f}{z:>8.0f}{u:>22.6f}{special.erfc(u):>11.6f}"
                  f"{dt * special.erfc(u):>10.4f}")
    t = 1000.0 * YEAR
    q = 2.5 * dt / math.sqrt(math.pi * kappa * t)
    print()
    print(f"  Surface heat-flow perturbation at t = 1000 yr: "
          f"q = k dT / sqrt(pi kappa t)")
    print(f"    = {1e3 * q:.4f} mW/m2  (with k = 2.5 W m-1 K-1, dT = {dt:.0f} K)")
    print("    This decays as t^-1/2: at 10 000 yr it is")
    print(f"    {1e3 * q / math.sqrt(10.0):.4f} mW/m2, one third of the 1000 yr value.")

    print()
    print("  The same number, three ways. erf, erfc and ndtr are one family:")
    xs = np.array([0.0, 0.25, 0.5, 1.0, 2.0, 3.0])
    print(f"    {'x':>7}{'erfc(x)':>20}{'2*ndtr(-x sqrt2)':>20}"
          f"{'1-erf(x)':>20}{'difference':>13}")
    for x in xs:
        a = special.erfc(x)
        b = 2.0 * special.ndtr(-x * math.sqrt(2.0))
        c = 1.0 - special.erf(x)
        print(f"    {x:>7.2f}{a:>20.16f}{b:>20.16f}{c:>20.16f}{abs(a - b):>13.2e}")
    print("    ndtr is the standard normal CDF, so erfc(x) = 2*Phi(-x*sqrt(2)).")
    print("    Using them interchangeably is safe; using 1 - erf(x) for large x")
    print("    is not, and the next table shows why.")

    print()
    print("  Cancellation and underflow at large argument. erfc ~ 0 and")
    print("  1 - erf is the difference of two nearly equal numbers; erfcx is")
    print("  exp(x^2) erfc(x), scaled so that it stays finite:")
    print(f"    {'x':>5}{'erfc(x)':>16}{'1 - erf(x)':>16}{'erfcx(x)':>16}"
          f"{'asymptotic erfc':>18}{'relative error':>16}")
    for x in (1.0, 2.0, 4.0, 8.0, 16.0, 26.0, 30.0):
        e = special.erfc(x)
        d = 1.0 - special.erf(x)
        e_scaled = special.erfcx(x)
        asym = math.exp(-x * x) / (x * math.sqrt(math.pi))
        rel = abs(asym - e) / e if e > 0 else float("nan")
        try:
            d_str = f"{d:.6e}"
        except ValueError:
            d_str = "0"
        print(f"    {x:>5.1f}{e:>16.6e}{d_str:>16}{e_scaled:>16.6e}"
              f"{asym:>18.6e}{rel:>16.2e}")
    print("    erfc underflows to zero somewhere between x = 26 and 30, and")
    print("    1 - erf(x) reaches exactly zero sooner because of cancellation.")
    print("    erfcx stays finite throughout, and the asymptotic form")
    print(f"    exp(-x^2)/(x sqrt(pi)) is good to {abs((math.exp(-26**2) / (26 * math.sqrt(math.pi)) - special.erfc(26.0)) / special.erfc(26.0)):.1e} relative at x = 26.")
    print("    A diffusion solution evaluated at a depth of several diffusion")
    print("    lengths is exactly the regime where this matters.")


# --------------------------------------------------------------------------
# Part 2 -- magnitude statistics
# --------------------------------------------------------------------------

def gr_magnitudes(n, mc, b, rng):
    """Gutenberg-Richter magnitudes: m = mc + Exponential(scale = 1/(b ln 10))."""
    return mc + rng.exponential(1.0 / (b * math.log(10.0)), size=n)


def ks_calibrated(data, mc, n_mc=2000, rng=None):
    """Monte-Carlo KS p-value for an exponential fitted to the same data."""
    rng = np.random.default_rng(1) if rng is None else rng
    d = data - mc
    scale_obs = d.mean()
    d_obs = stats.kstest(d, stats.expon(0.0, scale_obs).cdf).statistic
    count = 0
    for _ in range(n_mc):
        sim = rng.exponential(scale_obs, size=d.size)
        d_sim = stats.kstest(sim, stats.expon(0.0, sim.mean()).cdf).statistic
        count += d_sim >= d_obs
    return d_obs, (count + 1) / (n_mc + 1)


def part2_magnitudes():
    section("2. Fitting a Gutenberg-Richter distribution")
    mc, b_true, n = 2.0, 1.0, 1500
    m = gr_magnitudes(n, mc, b_true, RNG)
    print(f"  {n} SYNTHETIC magnitudes, completeness threshold Mc = {mc:.1f},")
    print(f"  true b-value = {b_true:.2f} (exponential scale "
          f"1/(b ln10) = {1.0 / (b_true * math.log(10.0)):.6f}).")
    print(f"  Sample: min {m.min():.3f}, mean {m.mean():.3f}, "
          f"max {m.max():.3f}")

    inv_ln10 = 1.0 / math.log(10.0)
    beta_hat = 1.0 / (m.mean() - mc)
    b_hat = beta_hat * inv_ln10
    se = b_hat / math.sqrt(n)
    print()
    print("  Maximum likelihood (Aki-Utsu), which for this distribution has a")
    print("  closed form: beta = 1/(mean(m) - Mc),  b = beta / ln 10.")
    print(f"    b_hat          = {b_hat:.6f}")
    print(f"    standard error = b_hat/sqrt(n) = {se:.6f}")
    print(f"    truth          = {b_true:.6f}   difference = "
          f"{(b_hat - b_true) / se:+.3f} standard errors")

    loc, scale = stats.expon.fit(m - mc, floc=0.0)
    print(f"    stats.expon.fit(floc=0) gives scale = {scale:.6f} "
          f"-> b = {inv_ln10 / scale:.6f}")
    print(f"    the two agree to {abs(inv_ln10 / scale - b_hat):.3e}: "
          f"the closed form is the fit.")

    print()
    print("  Cumulative least squares -- the method used in most published")
    print("  b-value maps. Count events with M >= m, take log10 N, fit a line:")
    edges = np.arange(mc, np.ceil(m.max()), 0.1)
    counts = np.array([(m >= e).sum() for e in edges])
    keep = counts > 0
    slope, intercept, r, p, stderr = stats.linregress(edges[keep],
                                                      np.log10(counts[keep]))
    print(f"    slope = {slope:.6f} -> b = {-slope:.6f} "
          f"(standard error {stderr:.6f}, r^2 = {r ** 2:.6f})")
    print(f"    bias against the MLE: {(-slope) - b_hat:+.6f}, i.e. "
          f"{100 * ((-slope) / b_hat - 1):+.2f}%")
    print("    The least-squares estimate is biased low and its nominal")
    print("    standard error is meaningless, because the cumulative counts are")
    print("    not independent -- each event appears in every bin below its")
    print("    magnitude. The MLE has neither problem.")

    print()
    print("  Goodness of fit. The KS statistic D is the largest gap between")
    print("  the empirical and the fitted CDF:")
    ks_fit = stats.kstest(m - mc, stats.expon(0.0, scale).cdf)
    d_obs, p_naive = ks_fit.statistic, ks_fit.pvalue
    d_true = stats.kstest(
        m - mc, stats.expon(0.0, 1.0 / (b_true * math.log(10.0))).cdf)
    d_mc, p_mc = ks_calibrated(m, mc, n_mc=2000, rng=RNG)
    print(f"    D against the *fitted* exponential      = {d_obs:.6f}, "
          f"naive p = {p_naive:.3f}")
    print(f"    D against the *true* distribution       = {d_true.statistic:.6f}, "
          f"p = {d_true.pvalue:.3f}  (no parameters estimated: valid)")
    print(f"    Monte-Carlo calibration of the fitted case: D = {d_mc:.6f}, "
          f"p = {p_mc:.3f}")
    print("    The naive p-value is wrong when the parameters come from the same")
    print("    data: it uses the KS distribution of a *specified* distribution,")
    print("    and estimating the parameters makes D systematically smaller. The")
    print("    calibrated value is obtained by simulating that very procedure")
    print("    and is the number to quote.")

    print()
    print("  The same machinery on data that do not obey the law. Draw")
    print("  magnitudes from a Weibull with the same mean:")
    scale_w = (1.0 / (b_true * math.log(10.0)))
    m_bad = mc + RNG.weibull(1.3, size=n) * scale_w * math.gamma(1 + 1 / 1.3)
    m_bad = m_bad[m_bad >= mc]
    scale_b = (m_bad - mc).mean()
    d_bad, p_bad = ks_calibrated(m_bad, mc, n_mc=2000, rng=RNG)
    print(f"    n = {m_bad.size}, mean magnitude {m_bad.mean():.4f} "
          f"(a GR sample would have {mc + scale_w:.4f})")
    print(f"    D = {d_bad:.6f}, calibrated p = {p_bad:.4f}")
    print(f"    fitted b = {inv_ln10 / scale_b:.4f} -- a plausible-looking")
    print("    number from a distribution that is not Gutenberg-Richter at all.")
    print("    A fitted parameter is not evidence that the model is right;")
    print("    that is what the goodness-of-fit test is for.")


# --------------------------------------------------------------------------
# Part 3 -- correlation, sample size, intervals
# --------------------------------------------------------------------------

def part3_correlation():
    section("3. Correlation coefficients, sample size and p-values")
    rho = 0.35
    big = 20000
    z = RNG.normal(size=(big, 2))
    y = rho * z[:, 0] + math.sqrt(1 - rho ** 2) * z[:, 1]
    print(f"  One bivariate normal sample with true Pearson rho = {rho:.2f}.")
    print("  Each row uses the first n pairs of that one sample, so every row")
    print("  estimates the same quantity:")
    print(f"    {'n':>7}{'r':>10}{'p (Pearson)':>14}{'p (Spearman)':>15}"
          f"{'95% CI for rho':>24}")
    for n in (10, 30, 100, 1000, 20000):
        res = stats.pearsonr(z[:n, 0], y[:n])
        rs, ps = stats.spearmanr(z[:n, 0], y[:n])
        lo, hi = res.confidence_interval(confidence_level=0.95)
        print(f"    {n:>7}{res.statistic:>10.4f}{res.pvalue:>14.3e}{ps:>15.3e}"
              f"{f'[{lo:+.3f}, {hi:+.3f}]':>24}")
    print("    The point estimate moves with n -- 0.79 at n = 10, 0.35 by")
    print("    n = 20 000 -- because ten pairs is not many. The p-value moves by")
    print("    hundreds of orders of magnitude on the same data, from 6.2e-03 to")
    print("    below the resolution of double precision. A p-value answers")
    print("    'could this have arisen by chance', not 'is this important'.")
    print("    The confidence interval is the quantity that survives the change")
    print("    in n, and it narrows as n^-1/2.")

    print()
    print("  The same trap in a geophysical regression. Permeability against")
    print("  porosity, SYNTHETIC, 25 samples:")
    n = 25
    phi = RNG.uniform(0.05, 0.30, n)
    logk = 12.0 * phi - 3.0 + RNG.normal(0.0, 0.35, n)
    lr = stats.linregress(phi, logk)
    df = n - 2
    t_q = stats.t.ppf(0.975, df)
    print(f"    slope = {lr.slope:.4f} +/- {lr.stderr:.4f} (log10 mD per unit "
          f"porosity)")
    print(f"    intercept = {lr.intercept:.4f}, r^2 = {lr.rvalue ** 2:.4f}, "
          f"p = {lr.pvalue:.3e}")
    print(f"    t(0.975, {df}) = {t_q:.4f} against the normal quantile 1.9600")
    print(f"    95% interval from t: "
          f"[{lr.slope - t_q * lr.stderr:.4f}, {lr.slope + t_q * lr.stderr:.4f}]"
          f"   width {2 * t_q * lr.stderr:.4f}")
    print(f"    95% interval from z: "
          f"[{lr.slope - 1.96 * lr.stderr:.4f}, {lr.slope + 1.96 * lr.stderr:.4f}]"
          f"   width {2 * 1.96 * lr.stderr:.4f}")
    coverage = 2.0 * stats.t.cdf(1.96, df) - 1.0
    print(f"    The z-interval is {100 * (1 - 1.96 / t_q):.2f}% too narrow and")
    print(f"    its actual coverage is {100 * coverage:.2f}%, not 95%. With")
    print(f"    {df} degrees of freedom that is the difference between the claim")
    print("    you are making and the claim the data support; a regression on")
    print("    25 samples must quote t.")


# --------------------------------------------------------------------------
# Part 4 -- a fit that should be rejected
# --------------------------------------------------------------------------

def part4_reject():
    section("4. A distribution fit that should be rejected")
    n = 400
    mu, sigma = -1.0, 1.2
    k = 10.0 ** RNG.normal(mu, sigma, n)
    print(f"  {n} SYNTHETIC permeabilities, log10(k) drawn from a normal with")
    print(f"  mu = {mu} and sigma = {sigma}, so k is lognormal by construction.")
    print(f"  Range {k.min():.4g} to {k.max():.4g} mD.")
    print(f"    sample mean {k.mean():.4g}, median {np.median(k):.4g}, "
          f"skewness {stats.skew(k):.4f}")
    print()
    fit_n = stats.norm.fit(k)
    d_norm = stats.kstest(k, stats.norm(*fit_n).cdf)
    fit_l = stats.lognorm.fit(k, floc=0.0)
    d_log = stats.kstest(k, stats.lognorm(*fit_l).cdf)
    sh = stats.shapiro(np.log(k))
    print(f"    {'model':<28}{'KS D':>12}{'naive p':>12}{'log-likelihood':>18}")
    print(f"    {'normal(mu, sigma), fitted':<28}{d_norm.statistic:>12.5f}"
          f"{d_norm.pvalue:>12.3e}{np.sum(stats.norm.logpdf(k, *fit_n)):>18.1f}")
    print(f"    {'lognormal(s, 0, scale), fitted':<28}{d_log.statistic:>12.5f}"
          f"{d_log.pvalue:>12.3e}{np.sum(stats.lognorm.logpdf(k, *fit_l)):>18.1f}")
    print(f"    Shapiro-Wilk on log(k): W = {sh.statistic:.5f}, "
          f"p = {sh.pvalue:.4f}")
    print("    Permeability is positive and roughly lognormal, and the two")
    print("    models are not close: the normal fit is rejected outright and")
    print("    the lognormal one is not, with a log-likelihood difference of")
    print(f"    {np.sum(stats.lognorm.logpdf(k, *fit_l)) - np.sum(stats.norm.logpdf(k, *fit_n)):.1f}.")
    print("    Both were fitted by maximum likelihood by the same routine; the")
    print("    model, not the optimiser, is what decided the answer.")
    print()
    print("  A mean and a standard deviation are not a description of a")
    print("  lognormal variable. The arithmetic mean is not the median and it")
    print("  is not what a flow calculation needs:")
    print(f"    mean k   = {k.mean():.4g} mD   (what a normal-model summary reports)")
    print(f"    median k = {np.median(k):.4g} mD   (the population value is "
          f"10^mu = {10 ** mu:.4g})")
    print(f"    geometric mean = {stats.gmean(k):.4g} mD, the sample estimate "
          f"of that median")
    print(f"    the arithmetic mean is {k.mean() / np.median(k):.1f} times the "
          f"median, and the gap grows")
    print("    with sigma, because the lognormal's mean is "
          "exp(mu + sigma^2/2).")
    print("    Any statistic that averages permeability linearly is dominated")
    print("    by its largest few samples, which is why effective permeability")
    print("    and the arithmetic mean of a lognormal sample are different")
    print("    quantities.")


def main():
    part1_error_function()
    part2_magnitudes()
    part3_correlation()
    part4_reject()
    print("\nDone.")


if __name__ == "__main__":
    main()
