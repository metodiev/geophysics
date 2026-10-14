"""Common distributions and the earth-science mechanism that produces each.

Run:  python3 distributions_demo.py
Requires: Python standard library only.
Random seed: 20240120 (fixed).

Companion to lesson 01-13-04.

The aim is not to list formulas but to show, numerically, *which* generative
mechanism yields *which* distribution:

  * Gaussian          -- many small independent additive contributions
  * Exponential       -- constant hazard: waiting times in a Poisson process
  * Poisson           -- counts of events in a fixed interval
  * Lognormal         -- many small multiplicative contributions
  * Power law (Pareto)-- scale-invariant fragmentation or preferential growth
  * Gumbel            -- the maximum of a large sample from a light tail
"""

import math
import random

SEED = 20240120


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mean(xs):
    return sum(xs) / len(xs)


def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - 1)


def quantile(sorted_xs, q):
    idx = min(len(sorted_xs) - 1, max(0, int(q * len(sorted_xs))))
    return sorted_xs[idx]


# --------------------------------------------------------------------------
# 1. Gaussian: the sum of many small additive contributions
# --------------------------------------------------------------------------

def gaussian_from_sums() -> None:
    section("1. Gaussian from additive contributions (12 uniforms)")
    rng = random.Random(SEED)
    n = 200_000
    sums = [sum(rng.random() for _ in range(12)) for _ in range(n)]
    m, v = mean(sums), variance(sums)
    print(f"  sum of 12 U(0,1): analytic mean 6, variance 1")
    print(f"  empirical mean     = {m:.6f}")
    print(f"  empirical variance = {v:.6f}")
    sd = math.sqrt(v)
    inside = sum(1 for x in sums if abs(x - m) < 1.96 * sd) / n
    print(f"  fraction within 1.96 sd = {inside:.6f}   (Gaussian: 0.950000)")
    print("  Measurement error is additive by nature: independent small effects")
    print("  (thermometer drift, timing error, elevation error) accumulate,")
    print("  which is why a Gaussian is the default model for instrument noise.")


# --------------------------------------------------------------------------
# 2. Exponential waiting times and Poisson counts
# --------------------------------------------------------------------------

def exponential_and_poisson() -> None:
    section("2. Exponential waiting times produce Poisson counts")
    lam = 1.5          # events per unit time (illustrative catalogue rate)
    T = 4.0
    rng = random.Random(SEED + 1)
    blocks = 200_000
    counts = []
    for _ in range(blocks):
        t = 0.0
        c = 0
        while True:
            t += rng.expovariate(lam)
            if t > T:
                break
            c += 1
        counts.append(c)
    print(f"  inter-arrival ~ Exp({lam}), observation window T = {T}")
    print(f"  analytic Poisson(lam*T) mean = {lam * T:.6f}, "
          f"variance = {lam * T:.6f}")
    print(f"  empirical mean               = {mean(counts):.6f}")
    print(f"  empirical variance           = {variance(counts):.6f}")
    print(f"  P(count = 0) analytic        = {math.exp(-lam * T):.6f}")
    print(f"  P(count = 0) empirical       = "
          f"{sum(1 for c in counts if c == 0) / blocks:.6f}")
    print("  A constant hazard rate gives exponential gaps; exponential gaps")
    print("  give Poisson counts. Seismicity is only approximately Poisson, but")
    print("  the pairing is the benchmark against which clustering is judged.")


# --------------------------------------------------------------------------
# 3. Lognormal: multiplicative contributions
# --------------------------------------------------------------------------

def lognormal_mechanism() -> None:
    section("3. Lognormal from multiplicative contributions (permeability)")
    rng = random.Random(SEED + 2)
    mu, sigma = 0.0, 1.0
    n = 300_000
    vals = [math.exp(rng.gauss(mu, sigma)) for _ in range(n)]
    m = mean(vals)
    med = quantile(sorted(vals), 0.5)
    analytic_mean = math.exp(mu + sigma * sigma / 2)
    analytic_median = math.exp(mu)
    print(f"  lognormal(mu={mu}, sigma={sigma})")
    print(f"  analytic mean   = exp(mu + sigma^2/2) = {analytic_mean:.6f}")
    print(f"  empirical mean                        = {m:.6f}")
    print(f"  analytic median = exp(mu)             = {analytic_median:.6f}")
    print(f"  empirical median                      = {med:.6f}")
    print(f"  fraction of samples above the mean    = "
          f"{sum(1 for x in vals if x > m) / n:.6f}")
    print("  More than half the samples lie below the mean: the mean is pulled")
    print("  up by a minority of large values, so the *median* is the honest")
    print("  central estimate. Porosity-permeability relations multiply local")
    print("  factors (grain size, sorting, cementation), and a product of many")
    print("  positive factors is lognormal by the same reasoning that makes a")
    print("  sum Gaussian. Ore grades follow the same mechanism.")


# --------------------------------------------------------------------------
# 4. Power law: scale-invariant fragmentation
# --------------------------------------------------------------------------

def power_law_and_hill() -> None:
    section("4. Power law (Pareto) and Hill tail-index estimation")
    rng = random.Random(SEED + 3)
    n = 400_000
    detail = {}
    for alpha in (2.5, 1.5):
        # Inverse-transform sampling: X = U^(-1/alpha), X >= 1.
        draws = [rng.random() ** (-1.0 / alpha) for _ in range(n)]
        xs = sorted(draws)
        detail[alpha] = draws
        print(f"  Pareto(alpha = {alpha}), P(X > x) = x^-alpha for x >= 1")
        if alpha > 1:
            print(f"    analytic mean   = alpha/(alpha-1)  = "
                  f"{alpha / (alpha - 1):.6f} (finite)")
            print(f"    empirical mean                     = {mean(xs):.6f}")
        else:
            print("    analytic mean          = INFINITE (alpha <= 1)")
            print(f"    empirical mean                     = {mean(xs):.6f} "
                  f"(no stable value exists)")
        if alpha > 2:
            var_theory = alpha / ((alpha - 1) ** 2 * (alpha - 2))
            print(f"    analytic variance = alpha/((a-1)^2(a-2)) = "
                  f"{var_theory:.6f} (finite)")
            print(f"    empirical variance                 = {variance(xs):.6f}")
        else:
            print("    analytic variance      = INFINITE (alpha <= 2)")
            print(f"    empirical variance                 = {variance(xs):.6f} "
                  f"(driven by the single largest draw)")
        print(f"    empirical median                   = {quantile(xs, 0.5):.6f}")
        print(f"    analytic median = 2^(1/alpha)      = {2 ** (1 / alpha):.6f}")
        # Hill estimator on the largest 5 % of the sample.
        k = n // 20
        tail = xs[-k:]
        threshold = tail[0]
        inv = mean([math.log(x / threshold) for x in tail])
        print(f"    Hill alpha estimate from top {k}     = {1 / inv:.6f}")
        print(f"    P(X > 100): empirical = "
              f"{sum(1 for x in xs if x > 100) / n:.8f}, "
              f"analytic = {100.0 ** (-alpha):.8f}")

    print("\n  Sample variance against n, tail index 2.5 (finite variance) "
          "and 1.5 (infinite):")
    for alpha in (2.5, 1.5):
        draws = detail[alpha]
        row = "  ".join(f"n={k}: {variance(draws[:k]):>10.4f}"
                        for k in (1_000, 10_000, 100_000, 400_000))
        print(f"    alpha = {alpha}: {row}")

    # Distribution of the sample-variance estimator across independent samples.
    rng2 = random.Random(SEED + 5)
    reps, m = 400, 10_000
    ests = []
    for _ in range(reps):
        block = [rng2.random() ** (-1.0 / 2.5) for _ in range(m)]
        ests.append(variance(block))
    ests.sort()
    print(f"\n  Sample variance for alpha = 2.5 over {reps} independent samples "
          f"of n = {m}")
    print(f"    analytic variance        = 2.222222")
    print(f"    mean of the estimates    = {mean(ests):.6f}  "
          f"(itself unconverged: the estimator's own variance diverges)")
    print(f"    median of the estimates  = {quantile(ests, 0.5):.6f}")
    print(f"    fraction below analytic  = "
          f"{sum(1 for v in ests if v < 2.222222) / reps:.4f}")
    print("  The estimator is unbiased in expectation, yet 78.5 % of these")
    print("  samples understate the variance and the median estimate (1.689) is")
    print("  far below the analytic 2.222. The estimator's own variance diverges")
    print("  because it involves the fourth moment, which does not exist for")
    print("  alpha = 2.5; even the mean of 400 repetitions has not converged.")
    print("  Reliable variance estimation needs a finite fourth moment,")
    print("  i.e. a tail exponent above 4.")
    print("\n  The variance of the alpha = 1.5 sample grows without settling,")
    print("  because that variance does not exist at all. Every standard error")
    print("  built from a sample variance is therefore meaningless for alpha <=")
    print("  2, which is why heavy-tailed geophysical data (fracture lengths,")
    print("  fault scarp heights, ore grades) call for median-based and")
    print("  quantile-based methods rather than means and variances.")


# --------------------------------------------------------------------------
# 5. Gumbel: the distribution of the maximum
# --------------------------------------------------------------------------

def gumbel_maximum() -> None:
    section("5. Gumbel: standardised maximum of exponentials")
    rng = random.Random(SEED + 4)
    block = 1000
    reps = 40_000
    maxima = []
    for _ in range(reps):
        maxima.append(max(rng.expovariate(1.0) for _ in range(block)))
    # For Exp(1), the maximum minus ln(n) converges to a Gumbel variable.
    shifted = sorted(m - math.log(block) for m in maxima)
    print(f"  block size n = {block}, blocks = {reps}")
    print(f"  {'y':>8}  {'P(Y <= y) emp':>16}  {'exp(-e^-y)':>14}")
    for y in (-1.0, 0.0, 1.0, 2.0):
        emp = sum(1 for v in shifted if v <= y) / reps
        theo = math.exp(-math.exp(-y))
        print(f"  {y:>8.3f}  {emp:>16.6f}  {theo:>14.6f}")
    print(f"  empirical mean of Y = {mean(shifted):.6f}  "
          f"(Gumbel mean = Euler-Mascheroni = "
          f"{0.5772156649015329:.6f})")
    print("  The maximum of a large sample has its own distribution family,")
    print("  independent (for light tails) of the parent. This is the basis of")
    print("  extreme-value analysis of floods, storm surges and maximum")
    print("  magnitudes, where the quantity of interest is the largest event,")
    print("  not the typical one.")


def main() -> None:
    gaussian_from_sums()
    exponential_and_poisson()
    lognormal_mechanism()
    power_law_and_hill()
    gumbel_maximum()
    print("\nDone. Reproducible with seed 20240120.")


if __name__ == "__main__":
    main()
