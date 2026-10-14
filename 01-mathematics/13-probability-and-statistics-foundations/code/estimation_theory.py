"""Point estimation: bias, consistency, efficiency and mean squared error.

Run:  python3 estimation_theory.py
Requires: Python standard library only.
Random seed: 20240122 (fixed).

Companion to lesson 01-13-06.

Four claims are tested rather than asserted:

  1. Bessel's correction removes the bias of the sample variance (and costs
     nothing but a factor that vanishes as n grows).
  2. Consistency: the spread of an estimator shrinks with n, and a biased
     estimator can still be consistent.
  3. Efficiency depends on the *shape* of the parent distribution: for an
     exponential-tailed (Laplace) sample the median beats the mean; for a
     Gaussian the mean wins.
  4. Unbiasedness is not the only virtue: for a Gaussian the biased variance
     estimator n^-1 * sum (x - mean)^2 has a *smaller* mean squared error.
"""

import math
import random

SEED = 20240122


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mean(xs):
    return sum(xs) / len(xs)


def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2] if n % 2 else 0.5 * (s[n // 2 - 1] + s[n // 2])


def trimmed_mean(xs, frac=0.1):
    s = sorted(xs)
    k = int(frac * len(s))
    core = s[k:len(s) - k]
    return sum(core) / len(core)


def laplace(rng, b=1.0):
    u = rng.random() - 0.5
    return -b * math.copysign(math.log(1 - 2 * abs(u)), u)


# --------------------------------------------------------------------------
# 1. Bias of the sample variance
# --------------------------------------------------------------------------

def variance_bias() -> None:
    section("1. Bias of the sample variance and Bessel's correction")
    sigma2 = 4.0
    n = 5
    rng = random.Random(SEED)
    reps = 100_000
    biased, unbiased = [], []
    for _ in range(reps):
        xs = [rng.gauss(0.0, math.sqrt(sigma2)) for _ in range(n)]
        m = mean(xs)
        ss = sum((x - m) ** 2 for x in xs)
        biased.append(ss / n)
        unbiased.append(ss / (n - 1))
    print(f"  parent variance sigma^2 = {sigma2}, n = {n}, reps = {reps:,}")
    print(f"  E[sum (x-m)^2 / n]     analytic = {sigma2 * (n - 1) / n:.6f}  "
          f"simulated = {mean(biased):.6f}")
    print(f"  E[sum (x-m)^2 / (n-1)] analytic = {sigma2:.6f}  "
          f"simulated = {mean(unbiased):.6f}")
    print(f"  relative bias of the n-divisor estimator = "
          f"{(mean(biased) - sigma2) / sigma2:.6f} (theory {-1 / n:.6f})")
    print("  The n-divisor estimator systematically understates the spread: it")
    print("  measures deviations from the sample mean, which is itself fitted to")
    print("  the data. Dividing by n-1 removes exactly that bias.")


# --------------------------------------------------------------------------
# 2. Consistency
# --------------------------------------------------------------------------

def consistency() -> None:
    section("2. Consistency: spread shrinks with n, biased or not")
    rng = random.Random(SEED + 1)
    reps = 10_000
    print(f"  {'n':>6}  {'sd(mean) sim':>14}  {'sd theory':>12}  "
          f"{'mean of biased est':>19}")
    for n in (4, 16, 64, 256, 1024):
        rng2 = random.Random(SEED + 1 + n)
        ests, biased_ests = [], []
        for _ in range(reps):
            xs = [rng2.gauss(5.0, 1.0) for _ in range(n)]
            ests.append(mean(xs))
            biased_ests.append(mean(xs) + 3.0 / n)   # bias -> 0 as n grows
        print(f"  {n:>6}  {math.sqrt(sum((e - mean(ests)) ** 2 for e in ests) / (reps - 1)):>14.6f}"
              f"  {1 / math.sqrt(n):>12.6f}  {mean(biased_ests):>19.6f}")
    print("  The spread falls as n^-1/2 in every case. The biased estimator has")
    print("  bias 3/n, which vanishes as n grows: bias is a property of the")
    print("  estimator at a fixed n, not a permanent defect. Consistency is")
    print("  about the limit.")


# --------------------------------------------------------------------------
# 3. Efficiency depends on the shape of the parent
# --------------------------------------------------------------------------

def efficiency() -> None:
    section("3. Efficiency: which estimator wins depends on the parent")
    reps, n = 20_000, 25
    for name, gen in (("Gaussian(0,1)", lambda r: r.gauss(0.0, 1.0)),
                      ("Laplace(0,1) ", laplace)):
        rng = random.Random(SEED + 2)
        ests = {"mean": [], "median": [], "midrange": [], "trim 10%": []}
        for _ in range(reps):
            xs = [gen(rng) for _ in range(n)]
            ests["mean"].append(mean(xs))
            ests["median"].append(median(xs))
            ests["midrange"].append(0.5 * (min(xs) + max(xs)))
            ests["trim 10%"].append(trimmed_mean(xs, 0.1))
        print(f"\n  {name}, n = {n}, reps = {reps:,}   "
              f"(MSE against the true location 0)")
        best = min(ests, key=lambda k: sum(e * e for e in ests[k]) / reps)
        for k, v in ests.items():
            mse = sum(e * e for e in v) / reps
            var = sum((e - mean(v)) ** 2 for e in v) / (reps - 1)
            print(f"    {k:<10} MSE = {mse:.6f}   variance = {var:.6f}   "
                  f"bias = {mean(v):+.6f}")
        print(f"    most efficient: {best}")
        if name.startswith("Laplace"):
            ratio = (sum(e * e for e in ests["mean"]) /
                     sum(e * e for e in ests["median"]))
            print(f"    MSE(mean)/MSE(median) = {ratio:.4f} at n = {n} "
                  f"(asymptotic value 2)")
    print("\n  For the Gaussian the mean is best and the midrange is worst: the")
    print("  extreme order statistics carry little information about the centre.")
    print("  For the Laplace sample the median beats the mean, by a factor that")
    print("  approaches the asymptotic prediction of 2 (median variance b^2/n")
    print("  against mean variance 2 b^2/n) but is smaller at n = 25. Which")
    print("  estimator is 'efficient' is a statement about the noise")
    print("  distribution, not a universal fact.")


# --------------------------------------------------------------------------
# 4. MSE = variance + bias^2, and why unbiased is not always best
# --------------------------------------------------------------------------

def mse_tradeoff() -> None:
    section("4. MSE = variance + bias^2, and a biased estimator that wins")
    sigma2 = 4.0
    n = 5
    rng = random.Random(SEED + 3)
    reps = 100_000
    est_n, est_n1 = [], []
    for _ in range(reps):
        xs = [rng.gauss(0.0, math.sqrt(sigma2)) for _ in range(n)]
        m = mean(xs)
        ss = sum((x - m) ** 2 for x in xs)
        est_n.append(ss / n)
        est_n1.append(ss / (n - 1))
    print(f"  estimating sigma^2 = {sigma2} from n = {n}, reps = {reps:,}")
    print(f"  {'estimator':>14}  {'variance':>12}  {'bias^2':>12}  {'MSE':>12}")
    for label, v in (("1/n", est_n), ("1/(n-1)", est_n1)):
        m = mean(v)
        var = sum((e - m) ** 2 for e in v) / (reps - 1)
        bias2 = (m - sigma2) ** 2
        print(f"  {label:>14}  {var:>12.6f}  {bias2:>12.6f}  {var + bias2:>12.6f}")
    print(f"  theory: Var(1/(n-1)) = 2 sigma^4/(n-1) = {2 * sigma2 ** 2 / (n - 1):.6f}")
    print(f"          Var(1/n)     = 2 sigma^4 (n-1)/n^2 = "
          f"{2 * sigma2 ** 2 * (n - 1) / n ** 2:.6f}")
    print("  The unbiased estimator has the larger mean squared error: removing")
    print("  the bias is paid for with extra variance. 'Unbiased' is a property")
    print("  worth having for its own sake, but it is not the same as 'accurate'.")


def main() -> None:
    variance_bias()
    consistency()
    efficiency()
    mse_tradeoff()
    print("\nDone. Reproducible with seed 20240122.")


if __name__ == "__main__":
    main()
