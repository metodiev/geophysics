"""Expectation, variance, moments and the algebra of averaging.

Run:  python3 expectation_variance_demo.py
Requires: Python standard library only.
Random seed: 20240119 (fixed).

Companion to lesson 01-13-03.

Central geophysical point: uncertainty is a physical quantity with units, and
its behaviour under averaging is governed by covariance. The last section shows
the case that matters most in practice -- a common systematic error does not
average away, no matter how many measurements you take.
"""

import math
import random

SEED = 20240119


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mean(xs):
    return sum(xs) / len(xs)


def variance(xs, ddof: int = 1):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / (len(xs) - ddof)


def covariance(xs, ys, ddof: int = 1):
    mx, my = mean(xs), mean(ys)
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (len(xs) - ddof)


def correlation(xs, ys):
    return covariance(xs, ys) / math.sqrt(variance(xs) * variance(ys))


def mu_k(xs, k):
    """k-th central moment (population form)."""
    m = mean(xs)
    return sum((x - m) ** k for x in xs) / len(xs)


def normal_pair(rng, n, rho):
    """Two standard normals with correlation rho, via Box-Muller."""
    xs, ys = [], []
    for _ in range(n):
        u1 = max(rng.random(), 1e-12)
        u2 = rng.random()
        r = math.sqrt(-2.0 * math.log(u1))
        z1 = r * math.cos(2 * math.pi * u2)
        z2 = r * math.sin(2 * math.pi * u2)
        xs.append(z1)
        ys.append(rho * z1 + math.sqrt(1 - rho * rho) * z2)
    return xs, ys


# --------------------------------------------------------------------------
# 1. Expectation and variance from a PMF and from a PDF
# --------------------------------------------------------------------------

def from_pmf_and_pdf() -> None:
    section("1. E[X] and Var[X] computed from a PMF and a PDF")
    lam_p = 3.2
    e1 = sum(k * math.exp(-lam_p + k * math.log(lam_p) - math.lgamma(k + 1))
             for k in range(80))
    e2 = sum(k * k * math.exp(-lam_p + k * math.log(lam_p) - math.lgamma(k + 1))
             for k in range(80))
    print(f"  Poisson(3.2): E = {e1:.6f}, Var = {e2 - e1 ** 2:.6f}  "
          f"(both equal lambda = {lam_p})")

    lam_e = 2.0
    # E[X] = int x f(x) dx, Var[X] = int (x - E)^2 f(x) dx, by Simpson.
    def integrand(k):
        return lambda x: (x ** k) * lam_e * math.exp(-lam_e * x)

    def simpson(f, a, b, n=20000):
        h = (b - a) / n
        total = f(a) + f(b)
        for i in range(1, n):
            total += (4.0 if i % 2 else 2.0) * f(a + i * h)
        return total * h / 3.0

    m1 = simpson(integrand(1), 0.0, 200.0)
    m2 = simpson(integrand(2), 0.0, 200.0)
    print(f"  Exponential(2): E = {m1:.6f} (= 1/lambda = {1 / lam_e:.6f}), "
          f"Var = {m2 - m1 ** 2:.6f} (= 1/lambda^2 = {1 / lam_e ** 2:.6f})")


# --------------------------------------------------------------------------
# 2. Linearity of expectation, including under dependence
# --------------------------------------------------------------------------

def linearity() -> None:
    section("2. Linearity of expectation needs no independence")
    rng = random.Random(SEED)
    n = 200_000
    xs = [rng.gauss(6.0, 0.5) for _ in range(n)]
    ys = [0.8 * x + rng.gauss(0.0, 0.3) for x in xs]  # strongly dependent on x
    print(f"  E[X]     = {mean(xs):.6f}")
    print(f"  E[Y]     = {mean(ys):.6f}")
    print(f"  E[X + Y] = {mean([x + y for x, y in zip(xs, ys)]):.6f}  "
          f"(= E[X] + E[Y] = {mean(xs) + mean(ys):.6f})")
    print("  X and Y are correlated by construction, yet the sum of expectations")
    print("  is the expectation of the sum. This is why we may sum many")
    print("  contributions to a potential field without tracking their dependence.")


# --------------------------------------------------------------------------
# 3. Variance of a sum, and covariance
# --------------------------------------------------------------------------

def variance_of_sum() -> None:
    section("3. Var[X + Y] = Var X + Var Y + 2 Cov(X, Y)")
    for rho in (0.0, 0.8, -0.5):
        rng = random.Random(SEED + 1)
        xs, ys = normal_pair(rng, 200_000, rho)
        vx, vy = variance(xs), variance(ys)
        cov = covariance(xs, ys)
        vsum = variance([x + y for x, y in zip(xs, ys)])
        predicted = vx + vy + 2 * cov
        r = correlation(xs, ys)
        print(f"  rho = {rho:>4}: Var X = {vx:.4f}, Var Y = {vy:.4f}, "
              f"Cov = {cov:.4f}, Corr = {r:.4f}")
        print(f"            Var(X+Y) sample = {vsum:.6f}, "
              f"predicted = {predicted:.6f}, "
              f"analytic = {2 + 2 * rho:.6f}")


# --------------------------------------------------------------------------
# 4. Averaging measurements: what the standard error really is
# --------------------------------------------------------------------------

def anomaly_estimate() -> None:
    section("4. Mean and variance of an anomaly estimate")
    sigma_true = 5.0          # mGal: anomaly amplitude, illustrative
    sigma_noise = 0.6         # mGal: single-reading noise
    print(f"  True anomaly {sigma_true} mGal, single-reading noise sd "
          f"{sigma_noise} mGal")
    print(f"  {'n':>6}  {'SE theory':>12}  {'SE observed':>12}  {'bias':>10}")
    for n in (1, 4, 16, 64, 256):
        rng = random.Random(SEED + 2)
        reps = 20_000
        estimates = []
        for _ in range(reps):
            readings = [sigma_true + rng.gauss(0.0, sigma_noise) for _ in range(n)]
            estimates.append(mean(readings))
        theory = sigma_noise / math.sqrt(n)
        observed = math.sqrt(variance(estimates))
        print(f"  {n:>6}  {theory:>12.6f}  {observed:>12.6f}  "
              f"{mean(estimates) - sigma_true:>10.6f}")
    print("  Theory and simulation agree: the standard error falls as n^-1/2.")
    print("  Quadrupling the number of readings halves the standard error.")


# --------------------------------------------------------------------------
# 5. Moments: skewness and kurtosis
# --------------------------------------------------------------------------

def moments() -> None:
    section("5. Standardised moments of the exponential distribution")
    rng = random.Random(SEED + 3)
    lam = 2.0
    n = 400_000
    xs = [rng.expovariate(lam) for _ in range(n)]
    sd = math.sqrt(mu_k(xs, 2))
    skew = mu_k(xs, 3) / sd ** 3
    exkurt = mu_k(xs, 4) / sd ** 4 - 3.0
    print(f"  skewness          empirical = {skew:.6f}   analytic = 2.000000")
    print(f"  excess kurtosis   empirical = {exkurt:.6f}   analytic = 6.000000")
    print("  A Gaussian has zero skewness and zero excess kurtosis. The")
    print("  exponential's strongly positive values are the signature of a")
    print("  one-sided waiting-time distribution: short gaps are common, long")
    print("  gaps decay away but still occur.")


# --------------------------------------------------------------------------
# 6. When averaging fails: a common systematic error
# --------------------------------------------------------------------------

def systematic_floor() -> None:
    section("6. A common systematic error does not average away")
    truth = 20.0
    sd_bias = 0.30       # mGal: shared mis-calibration across all readings
    sd_noise = 1.00      # mGal: independent per-reading noise
    print(f"  truth = {truth} mGal, shared bias sd = {sd_bias}, "
          f"noise sd = {sd_noise}")
    print(f"  {'n':>6}  {'SE theory':>12}  {'SE observed':>12}  "
          f"{'mean est':>10}")
    for n in (1, 16, 256, 4096):
        rng = random.Random(SEED + 4)
        reps = 10_000
        estimates = []
        for _ in range(reps):
            bias = rng.gauss(0.0, sd_bias)
            readings = [truth + bias + rng.gauss(0.0, sd_noise) for _ in range(n)]
            estimates.append(mean(readings))
        theory = math.sqrt(sd_bias ** 2 + sd_noise ** 2 / n)
        observed = math.sqrt(variance(estimates))
        print(f"  {n:>6}  {theory:>12.6f}  {observed:>12.6f}  "
              f"{mean(estimates):>10.6f}")
    print("  As n grows the noise term collapses as n^-1/2 but the standard")
    print("  error flattens at the shared bias sd of 0.30 mGal. Beyond roughly")
    print("  n = 100 extra readings buy nothing. In practice this is why")
    print("  instrument calibration and survey-design errors — not random noise —")
    print("  usually set the accuracy of a geophysical anomaly.")


def main() -> None:
    from_pmf_and_pdf()
    linearity()
    variance_of_sum()
    anomaly_estimate()
    moments()
    systematic_floor()
    print("\nDone. Reproducible with seed 20240119.")


if __name__ == "__main__":
    main()
