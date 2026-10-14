"""Sampling distributions, the law of large numbers and the CLT.

Run:  python3 sampling_and_clt_demo.py
Requires: Python standard library only.
Random seed: 20240121 (fixed).

Companion to lesson 01-13-05.

Three questions are answered numerically:

  1. Does the sample mean converge, and how fast?  (LLN, and its failure for
     the Cauchy distribution, whose mean does not exist.)
  2. How large must n be before the mean is approximately normal?  (CLT, for a
     bounded and for a skewed parent.)
  3. When does the CLT fail outright?  (A power law with tail exponent 1.5:
     finite mean, infinite variance.)
"""

import math
import random
import statistics

SEED = 20240121
PHI = statistics.NormalDist()


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mean(xs):
    return sum(xs) / len(xs)


def stdev(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def pareto15(rng):
    return rng.random() ** (-1.0 / 1.5)     # Pareto with tail exponent 1.5


def cauchy(rng):
    return math.tan(math.pi * (rng.random() - 0.5))


def max_cdf_gap(zs):
    """Kolmogorov-Smirnov distance between standardised samples and N(0,1)."""
    xs = sorted(zs)
    n = len(xs)
    gap = 0.0
    for i, z in enumerate(xs):
        theo = PHI.cdf(z)
        gap = max(gap, abs(i / n - theo), abs((i + 1) / n - theo))
    return gap


def quantile(sorted_xs, p):
    n = len(sorted_xs)
    idx = p * (n - 1)
    lo = int(math.floor(idx))
    hi = min(n - 1, int(math.ceil(idx)))
    return sorted_xs[lo] + (sorted_xs[hi] - sorted_xs[lo]) * (idx - lo)


def iqr(xs):
    s = sorted(xs)
    return quantile(s, 0.75) - quantile(s, 0.25)


# --------------------------------------------------------------------------
# 1. Law of large numbers, and a case where it fails
# --------------------------------------------------------------------------

def law_of_large_numbers() -> None:
    section("1. The law of large numbers: convergence, and its failure mode")
    rng = random.Random(SEED)
    marks = (1_000, 10_000, 100_000, 1_000_000)
    exp_runs, pareto_runs = [], []
    e = p = 0.0
    for i in range(1, 1_000_001):
        e += rng.expovariate(1.0)
        p += pareto15(rng)
        if i in marks:
            exp_runs.append((i, e / i))
            pareto_runs.append((i, p / i))
    print("  running sample mean (true values: Exp(1) 1.0, Pareto(1.5) 3.0)")
    print(f"  {'n':>12}  {'Exp(1)':>14}  {'Pareto(1.5)':>14}")
    for (n, a), (_, b) in zip(exp_runs, pareto_runs):
        print(f"  {n:>12,}  {a:>14.6f}  {b:>14.6f}")
    print("  Both converge, because both have a finite mean; the Pareto mean")
    print("  fluctuates far more at a given n because its tail is heavy.")

    print("\n  Same experiment for the standard Cauchy distribution, whose mean")
    print("  does not exist. Five independent runs, two sample sizes:")
    print(f"  {'n':>10}   " + "  ".join(f"{'run ' + str(k):>14}"
                                        for k in range(1, 6)))
    for n in (1_000, 100_000):
        rngc = random.Random(SEED + n)
        row = [mean([cauchy(rngc) for _ in range(n)]) for _ in range(5)]
        print(f"  {n:>10,}   " + "  ".join(f"{v:>14.6f}" for v in row))
    print("  The five averages disagree wildly and show no tendency to agree as")
    print("  n grows: the running mean of a Cauchy sample is itself Cauchy, and")
    print("  averaging does not concentrate it. A finite mean is the entire")
    print("  hypothesis of the law of large numbers.")


# --------------------------------------------------------------------------
# 2. CLT for a bounded and a skewed parent
# --------------------------------------------------------------------------

def clt_approach(gen, true_mean, true_sd, ns, reps, label) -> None:
    print(f"\n  {label}: max |F_emp - Phi| of the standardised mean")
    print(f"  {'n':>6}  {'KS gap':>12}")
    for n in ns:
        rng = random.Random(SEED + n)
        zs = []
        for _ in range(reps):
            s = sum(gen(rng) for _ in range(n))
            zs.append((s / n - true_mean) / (true_sd / math.sqrt(n)))
        print(f"  {n:>6}  {max_cdf_gap(zs):>12.6f}")
    print(f"  (With {reps:,} replicates the Monte Carlo noise floor on this")
    print(f"   statistic is about {1 / math.sqrt(reps):.4f}.)")


def clt_light_tails() -> None:
    section("2. Convergence to the normal for light-tailed parents")
    uniform = lambda rng: rng.random()
    expo = lambda rng: rng.expovariate(1.0)
    clt_approach(uniform, 0.5, math.sqrt(1 / 12), (1, 2, 5, 30, 300), 20_000,
                 "Uniform(0,1) (bounded, symmetric)")
    clt_approach(expo, 1.0, 1.0, (1, 2, 5, 30, 300), 20_000,
                 "Exponential(1) (skewed)")
    print("\n  For the symmetric bounded parent the approximation is already")
    print("  usable at n = 2. For the strongly skewed exponential it is still")
    print("  poor at n = 5 and only becomes respectable near n = 30-300. The")
    print("  rule of thumb 'n greater than 30' is a statement about skewness,")
    print("  not a theorem.")


# --------------------------------------------------------------------------
# 3. CLT failure for a heavy tail
# --------------------------------------------------------------------------

def clt_failure() -> None:
    section("3. CLT failure: Pareto(1.5), finite mean, infinite variance")
    print("  Studentised mean Z = (mean - 3) sqrt(n) / s, using the sample sd s")
    print(f"  {'n':>8}  {'reps':>7}  {'P(|Z|>1.96)':>12}  {'P(|Z|>5)':>11}  "
          f"{'P(|Z|>20)':>12}")
    for n, reps in ((10, 20_000), (100, 20_000), (1_000, 5_000),
                    (10_000, 2_000)):
        rng = random.Random(SEED + 1000 + n)
        a = b = c = 0
        for _ in range(reps):
            xs = [pareto15(rng) for _ in range(n)]
            s = stdev(xs)
            if s == 0.0:
                continue
            z = (mean(xs) - 3.0) * math.sqrt(n) / s
            if abs(z) > 1.96:
                a += 1
            if abs(z) > 5:
                b += 1
            if abs(z) > 20:
                c += 1
        print(f"  {n:>8,}  {reps:>7,}  {a / reps:>12.6f}  {b / reps:>11.6f}  "
              f"{c / reps:>12.6f}")
    print("  Under a normal limit these would be 0.050, ~0 and ~0 at every n.")
    print("  Instead P(|Z| > 1.96) is far too large at every sample size and")
    print("  shrinks only slowly: there is no Gaussian approximation for a tail")
    print("  exponent below 2, no matter how large the sample. The limit is a")
    print("  stable law, not a normal. The LLN still holds, because the mean of")
    print("  a Pareto(1.5) exists: 'the average converges' and 'the average is")
    print("  Gaussian' are different claims with different hypotheses.")

    print("\n  Rate of convergence of the sample mean (robust scale across 1000")
    print("  runs). Theory: interquartile range of Xbar ~ n^-1/2 with finite")
    print("  variance, and ~ n^-(1 - 1/alpha) = n^-1/3 for alpha = 1.5.")
    for label, gen, norm in (("Exp(1)   ", lambda r: r.expovariate(1.0),
                              lambda n: math.sqrt(n)),
                             ("Pareto1.5", pareto15, lambda n: n ** (1 / 3))):
        scales = []
        for n in (100, 1_000, 10_000):
            rng = random.Random(SEED + 2000 + n)
            scales.append(iqr([mean([gen(rng) for _ in range(n)])
                               for _ in range(1000)]))
        fitted = math.log(scales[0] / scales[2]) / math.log(100)
        print(f"    {label}: IQR of the mean = " +
              ", ".join(f"{s:.6f} (n={n:,})" for n, s in
                        zip((100, 1_000, 10_000), scales)))
        print("      IQR * n^(1/2 for Exp, 1/3 for Pareto) = " +
              ", ".join(f"{s * norm(n):.4f}" for n, s in
                        zip((100, 1_000, 10_000), scales)))
        print(f"      fitted exponent 100 -> 10 000 = {fitted:.4f}")
    print("  The exponential follows n^-0.5 closely. The Pareto mean follows")
    print("  n^-0.33: it does converge, but a factor of 100 in n buys only a")
    print("  factor of about 4.6 in precision, against 10 when the variance is")
    print("  finite. The spread is measured by an interquartile range, not a")
    print("  standard deviation, because for alpha = 1.5 the variance of the")
    print("  mean does not exist either; a sample sd across runs is erratic.")
    print("  This is the quantitative reason why estimating the mean of a")
    print("  heavy-tailed quantity is expensive: it is not that the estimator is")
    print("  wrong, it is that it is slow.")


def main() -> None:
    law_of_large_numbers()
    clt_light_tails()
    clt_failure()
    print("\nDone. Reproducible with seed 20240121.")


if __name__ == "__main__":
    main()
