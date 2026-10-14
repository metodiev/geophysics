"""Hypothesis testing: p-values, power, and manufactured discoveries.

Run:  python3 hypothesis_testing.py
Requires: Python standard library only.
Random seed: 20240124 (fixed).

Companion to lesson 01-13-08.

The three numerical results here are the ones that matter in practice:

  1. Under the null hypothesis a p-value is Uniform(0,1), so a 5 % threshold
     rejects a true null exactly 5 % of the time -- per test.
  2. Power depends on effect size, sample size and the noise standard
     deviation through a single combination.
  3. Running many tests, or repeatedly testing a growing sample, inflates the
     chance of a false discovery far above the nominal rate.
"""

import math
import random
import statistics

SEED = 20240124
PHI = statistics.NormalDist()


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mean(xs):
    return sum(xs) / len(xs)


def two_sided_p(z: float) -> float:
    return 2.0 * (1.0 - PHI.cdf(abs(z)))


def z_test(sample, mu0: float, sigma: float) -> float:
    n = len(sample)
    z = (mean(sample) - mu0) / (sigma / math.sqrt(n))
    return two_sided_p(z)


# --------------------------------------------------------------------------
# 1. The null distribution of the p-value
# --------------------------------------------------------------------------

def null_p_values() -> None:
    section("1. Under the null hypothesis the p-value is Uniform(0,1)")
    rng = random.Random(SEED)
    reps, n, sigma = 100_000, 25, 1.0
    ps = []
    for _ in range(reps):
        ps.append(z_test([rng.gauss(0.0, sigma) for _ in range(n)], 0.0, sigma))
    ps.sort()
    print(f"  H0 true, n = {n}, reps = {reps:,}")
    for level in (0.01, 0.05, 0.10, 0.50):
        print(f"    fraction of p-values below {level:.2f} = "
              f"{sum(1 for p in ps if p < level) / reps:.6f}")
    gap = 0.0
    for i, p in enumerate(ps):
        gap = max(gap, abs(i / reps - p), abs((i + 1) / reps - p))
    print(f"    max |F_emp - Uniform|            = {gap:.6f}   "
          f"(noise scale {1 / math.sqrt(reps):.6f})")
    print(f"    mean of the p-values             = {mean(ps):.6f}   (uniform 0.5)")
    print("  Stated plainly: a significance threshold of 0.05 rejects a true null")
    print("  hypothesis five times in a hundred. That is the definition of the")
    print("  threshold, not a defect of the test.")


# --------------------------------------------------------------------------
# 2. Power
# --------------------------------------------------------------------------

def power_curve() -> None:
    section("2. Power: analytic formula against simulation")
    sigma, n, alpha = 1.0, 25, 0.05
    zcrit = PHI.inv_cdf(1 - alpha / 2)
    print(f"  sigma = {sigma}, n = {n}, two-sided alpha = {alpha}, "
          f"z_crit = {zcrit:.6f}")
    print(f"  {'effect delta':>13}  {'power (theory)':>15}  "
          f"{'power (simulated)':>18}")
    reps = 20_000
    for delta in (0.0, 0.2, 0.4, 0.6, 0.8, 1.0):
        theory = (PHI.cdf(delta * math.sqrt(n) / sigma - zcrit)
                  + PHI.cdf(-delta * math.sqrt(n) / sigma - zcrit))
        rng = random.Random(SEED + 1 + int(delta * 100))
        rejects = 0
        for _ in range(reps):
            if z_test([rng.gauss(delta, sigma) for _ in range(n)], 0.0,
                      sigma) < alpha:
                rejects += 1
        print(f"  {delta:>13.2f}  {theory:>15.6f}  {rejects / reps:>18.6f}")
    print("  At delta = 0 the rejection rate is the Type I error rate, 0.05. As")
    print("  the effect grows the power rises. Note the combination: only")
    print("  delta * sqrt(n) / sigma matters, so quadrupling n doubles the")
    print("  effective effect.")


# --------------------------------------------------------------------------
# 3. Multiple comparisons
# --------------------------------------------------------------------------

def multiple_comparisons() -> None:
    section("3. Many tests at once: the family-wise error rate")
    alpha = 0.05
    reps = 200_000
    print(f"  {reps:,} simulated studies, each running m independent z-tests")
    print(f"  under a true null hypothesis, each at alpha = {alpha}")
    print("  Section 1 established that such a p-value is exactly Uniform(0,1),")
    print("  so the smallest of m of them is drawn here directly from its exact")
    print("  distribution: 1 - U^(1/m) is Beta(1, m).")
    print(f"  {'m':>6}  {'1-(1-a)^m':>11}  {'observed FWER':>14}  "
          f"{'Bonferroni a/m':>15}  {'observed FWER':>14}")
    for m in (1, 10, 50, 100, 1000):
        rng = random.Random(SEED + 2 + m)
        any_uncorrected = 0
        any_bonferroni = 0
        for _ in range(reps):
            p_min = 1.0 - rng.random() ** (1.0 / m)
            if p_min < alpha:
                any_uncorrected += 1
            if p_min < alpha / m:
                any_bonferroni += 1
        print(f"  {m:>6}  {1 - (1 - alpha) ** m:>11.6f}  "
              f"{any_uncorrected / reps:>14.6f}  {alpha / m:>15.6f}  "
              f"{any_bonferroni / reps:>14.6f}")
    print("  With 1000 tests the chance of at least one false discovery under a")
    print("  completely true null hypothesis is essentially certain. Bonferroni")
    print("  correction, and the honest reporting of how many tests were run,")
    print("  are not optional refinements; without them a 'discovery' carries no")
    print("  information.")

    print("\n  Optional stopping: test the growing sample repeatedly")
    print(f"  {'stop at n_max':>15}  {'observed rate':>14}  {'nominal':>9}")
    sigma = 1.0
    for n_max in (30, 100, 1000):
        rng = random.Random(SEED + 3 + n_max)
        studies = 4_000
        found = 0
        for _ in range(studies):
            total = 0.0
            declared = False
            for k in range(1, n_max + 1):
                total += rng.gauss(0.0, sigma)
                if k >= 10:
                    z = (total / k) / (sigma / math.sqrt(k))
                    if two_sided_p(z) < alpha:
                        declared = True
                        break
            if declared:
                found += 1
        print(f"  {n_max:>15}  {found / studies:>14.6f}  {alpha:>9.2f}")
    print("  Touching the data, testing, and stopping when the p-value dips below")
    print("  0.05 is not a test at 0.05. The nominal level applies to one test")
    print("  decided in advance; every additional look spends significance. With")
    print("  1000 looks available, a true null is declared significant about 46 %")
    print("  of the time. This is the machinery behind the replication problems in")
    print("  field sciences. The same effect appears when terrain, band, station")
    print("  or model are searched over and only the winning combination is")
    print("  reported.")


# --------------------------------------------------------------------------
# 4. Sample size for a geophysical detection
# --------------------------------------------------------------------------

def sample_size() -> None:
    section("4. How many picks to detect a travel-time delay?")
    sigma, delta = 0.10, 0.05      # seconds: pick scatter, and the delay sought
    alpha, power = 0.05, 0.90
    z_a = PHI.inv_cdf(1 - alpha / 2)
    z_b = PHI.inv_cdf(power)
    n_star = ((z_a + z_b) * sigma / delta) ** 2
    print(f"  pick scatter sigma = {sigma} s, delay to detect = {delta} s")
    print(f"  z(0.975) = {z_a:.6f}, z(0.90) = {z_b:.6f}")
    print(f"  required n = ((z_a + z_b) sigma / delta)^2 = {n_star:.6f}")
    print(f"  so {math.ceil(n_star)} picks are needed for 90 % power at "
          f"alpha = 0.05")
    rng = random.Random(SEED + 4)
    reps = 20_000
    for n in (40, 42, 43, 60):
        theory = (PHI.cdf(delta * math.sqrt(n) / sigma - z_a)
                  + PHI.cdf(-delta * math.sqrt(n) / sigma - z_a))
        rejects = sum(1 for _ in range(reps)
                      if z_test([rng.gauss(delta, sigma) for _ in range(n)],
                                0.0, sigma) < alpha)
        print(f"    n = {n:>3}: power theory {theory:.6f}, "
              f"simulated {rejects / reps:.6f}")
    print("  The exact continuous answer is 42.03, so the z formula puts 42 picks")
    print("  a hair below 90 % and 43 above it. The simulation, with a standard")
    print("  error of about 0.002 at this number of replicates, cannot resolve")
    print("  that hair and lands either side of it; both estimates agree with the")
    print("  formula to well within Monte Carlo noise. The formula is the reason")
    print("  a survey is designed before it is acquired: it converts an accuracy")
    print("  target into a count of measurements, and it does so before any data")
    print("  exist.")


def main() -> None:
    null_p_values()
    power_curve()
    multiple_comparisons()
    sample_size()
    print("\nDone. Reproducible with seed 20240124.")


if __name__ == "__main__":
    main()
