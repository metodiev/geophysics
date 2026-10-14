"""Random variables: PMFs, PDFs, CDFs and derived distributions.

Run:  python3 random_variables_demo.py
Requires: Python standard library only.
Random seed: 20240118 (fixed).

Companion to lesson 01-13-02.

Physical thread: earthquake magnitudes above a completeness threshold are, to a
good approximation, exponentially distributed (the Gutenberg-Richter law written
in natural units). Radiated energy is a power of the magnitude. This script
follows that thread from a discrete count model, through a continuous density,
to a derived heavy-tailed distribution, checking every claim numerically.
"""

import math
import random

SEED = 20240118


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


# --------------------------------------------------------------------------
# Small numerical helpers (no third-party libraries)
# --------------------------------------------------------------------------

def poisson_pmf(k: int, lam: float) -> float:
    return math.exp(-lam + k * math.log(lam) - math.lgamma(k + 1))


def exp_pdf(x: float, lam: float) -> float:
    return lam * math.exp(-lam * x)


def simpson(f, a: float, b: float, n: int = 20000) -> float:
    """Composite Simpson's rule; n must be even."""
    if n % 2:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        total += (4.0 if i % 2 else 2.0) * f(a + i * h)
    return total * h / 3.0


# --------------------------------------------------------------------------
# 1. A discrete random variable: earthquake counts
# --------------------------------------------------------------------------

def discrete_pmf() -> None:
    section("1. Discrete PMF: Poisson counts (illustrative rate 3.2 per year)")
    lam = 3.2
    total = sum(poisson_pmf(k, lam) for k in range(60))
    mean = sum(k * poisson_pmf(k, lam) for k in range(60))
    ex2 = sum(k * k * poisson_pmf(k, lam) for k in range(60))
    print(f"  sum of PMF over k = 0..59 : {total:.12f}   (axiom: equals 1)")
    for k in range(6):
        print(f"    P(N = {k}) = {poisson_pmf(k, lam):.6f}")
    print(f"  E[N]   = {mean:.6f}   (analytic {lam})")
    print(f"  Var[N] = {ex2 - mean ** 2:.6f}   (analytic {lam})")
    print("  For the Poisson family the mean and the variance are the same")
    print("  number; that equality is the reason counts per unit time are the")
    print("  natural diagnostic for a Poisson process.")


# --------------------------------------------------------------------------
# 2. A continuous random variable: waiting time between events
# --------------------------------------------------------------------------

def continuous_pdf() -> None:
    section("2. Continuous PDF: exponential waiting time, lambda = 2.3 per unit")
    lam = 2.302585092994046  # ln(10); see the magnitude model in Section 6
    area = simpson(lambda x: exp_pdf(x, lam), 0.0, 40.0)
    short = simpson(lambda x: exp_pdf(x, lam), 0.0, 0.5)
    cdf_diff = (1 - math.exp(-lam * 0.5)) - (1 - math.exp(0.0))
    print(f"  integral of PDF over [0, 40]  = {area:.10f}   (must be 1)")
    print(f"  P(X < 0.5) by quadrature      = {short:.10f}")
    print(f"  F(0.5) - F(0) by formula      = {cdf_diff:.10f}")
    print(f"  P(X = 0.5) exactly            = 0     (a density is not a probability)")
    print(f"  median  = ln 2 / lambda       = {math.log(2) / lam:.6f}")
    print(f"  mean    = 1 / lambda          = {1 / lam:.6f}")
    print("  Only intervals carry probability; the density at a point carries")
    print("  probability *per unit x*, which is why it can exceed 1.")


# --------------------------------------------------------------------------
# 3. The CDF and memorylessness
# --------------------------------------------------------------------------

def cdf_and_memorylessness() -> None:
    section("3. The CDF, and the memoryless property of the exponential")
    lam = 2.302585092994046
    t = 1.0
    print(f"  F(t)  = 1 - exp(-lambda t) at t = 1  : {1 - math.exp(-lam * t):.6f}")
    print(f"  S(t)  = exp(-lambda t)               : {math.exp(-lam * t):.6f}")
    # P(X > s + t | X > s) should equal P(X > t) for any s.
    for s in (0.0, 2.0, 5.0):
        cond = math.exp(-lam * (s + t)) / math.exp(-lam * s)
        print(f"    P(X > {s + t:.0f} | X > {s:.0f}) = {cond:.6f}")
    print(f"  All equal P(X > 1) = {math.exp(-lam * t):.6f}: the process has no memory.")
    print("  A fault that has not ruptured for 200 years is not 'due'; under a")
    print("  Poisson model its hazard rate next year is unchanged. Real faults")
    print("  violate this because stress is transferred, which is exactly why")
    print("  the memoryless model is a benchmark rather than a law.")


# --------------------------------------------------------------------------
# 4. Empirical CDF and the Kolmogorov-Smirnov distance
# --------------------------------------------------------------------------

def empirical_cdf() -> None:
    section("4. Empirical CDF against the theoretical CDF (200 000 draws)")
    lam = 2.302585092994046
    rng = random.Random(SEED)
    n = 200_000
    xs = sorted(rng.expovariate(lam) for _ in range(n))
    ks = 0.0
    for i, x in enumerate(xs):
        theo = 1 - math.exp(-lam * x)
        ks = max(ks, abs(i / n - theo), abs((i + 1) / n - theo))
    print(f"  samples                       = {n:,}")
    print(f"  max |F_emp - F_theory|        = {ks:.6f}")
    print(f"  expected order 1/sqrt(n)      = {1 / math.sqrt(n):.6f}")
    print(f"  ratio                         = {ks * math.sqrt(n):.4f}")
    print("  The empirical CDF tracks the theoretical one to within a few")
    print("  multiples of n^-1/2, which is the size of sampling fluctuation the")
    print("  law of large numbers promises and the CLT quantifies in lesson 05.")


# --------------------------------------------------------------------------
# 5. The probability integral transform
# --------------------------------------------------------------------------

def probability_integral_transform() -> None:
    section("5. Probability integral transform: F(X) is uniform")
    lam = 2.302585092994046
    rng = random.Random(SEED + 1)
    n = 200_000
    us = [1 - math.exp(-lam * rng.expovariate(lam)) for _ in range(n)]
    mean = sum(us) / n
    var = sum((u - mean) ** 2 for u in us) / (n - 1)
    exceed = sum(1 for u in us if u > 0.9) / n
    print(f"  samples                     = {n:,}")
    print(f"  mean of F(X)                = {mean:.6f}   (uniform: 0.5)")
    print(f"  variance of F(X)            = {var:.6f}   (uniform: {1 / 12:.6f})")
    print(f"  fraction of F(X) above 0.9  = {exceed:.6f}   (uniform: 0.100000)")
    print("  This is the engine of inverse-transform sampling and of every")
    print("  goodness-of-fit test that compares a data CDF with a model CDF.")


# --------------------------------------------------------------------------
# 6. A derived distribution: magnitude to energy
# --------------------------------------------------------------------------

def derived_distribution() -> None:
    section("6. Derived distribution: exponential magnitude -> power-law energy")
    # Gutenberg-Richter in natural-log units: magnitude M ~ Exp(lambda).
    # Radiated energy scales as a power of M: log10 E = 1.5 M + const.
    b = 1.0
    lam = b * math.log(10.0)
    print(f"  lambda for magnitudes       = b ln 10 = {lam:.6f}")
    print("  Transformation: Y = 10^(1.5 M), so S_Y(y) = y^(-lambda/(1.5 ln 10))")
    alpha = lam / (1.5 * math.log(10.0))
    print(f"  power-law tail exponent     = {alpha:.6f}   (= b / 1.5 = {b / 1.5:.6f})")
    print(f"  tail exponent < 1 ?         = {alpha < 1.0}   -> E[Y] diverges")

    rng = random.Random(SEED + 2)
    n = 400_000
    draws = [10.0 ** (1.5 * rng.expovariate(lam)) for _ in range(n)]
    ys = sorted(draws)

    def median_of(seq):
        ordered = sorted(seq)
        m = len(ordered)
        return ordered[m // 2] if m % 2 else 0.5 * (ordered[m // 2 - 1] + ordered[m // 2])

    analytic_median = 10.0 ** (1.5 * math.log(2.0) / lam)
    print(f"\n  analytic median of Y        = {analytic_median:.6f}")
    print(f"  empirical median of Y       = {median_of(draws):.6f}")
    print(f"  largest single draw         = {ys[-1]:.6e}")

    print("\n  sample mean of Y against n (tail exponent < 1: the mean diverges):")
    for k in (1_000, 10_000, 100_000, 400_000):
        prefix = draws[:k]
        print(f"    n = {k:>7,}   mean = {sum(prefix) / k:>14.6f}   "
              f"median = {median_of(prefix):>12.6f}")

    print("\n  survival function against the power law:")
    for y in (1e3, 1e6, 1e9):
        empirical = sum(1 for v in draws if v > y) / n
        expected_count = n * y ** (-alpha)
        print(f"    y = {y:.0e}   P(Y>y) empirical = {empirical:.8f}   "
              f"y^-alpha = {y ** (-alpha):.8f}   expected count = {expected_count:.2f}")
    print("  The median is stable and matches theory to three digits; the mean")
    print("  keeps climbing because a handful of enormous values dominate it.")
    print("  At y = 1e9 the theory predicts fewer than one sample, so an empirical")
    print("  zero there measures the sample size, not the model. Magnitudes are")
    print("  not heavy-tailed (exponential); energies are (power law, alpha<1).")


def main() -> None:
    discrete_pmf()
    continuous_pdf()
    cdf_and_memorylessness()
    empirical_cdf()
    probability_integral_transform()
    derived_distribution()
    print("\nDone. Reproducible with seed 20240118.")


if __name__ == "__main__":
    main()
