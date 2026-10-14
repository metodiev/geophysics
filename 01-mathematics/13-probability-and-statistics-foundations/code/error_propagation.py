"""Error and uncertainty propagation: analytic formulae against Monte Carlo.

Run:  python3 error_propagation.py
Requires: Python standard library only.
Random seed: 20240125 (fixed).  Monte Carlo ensembles use N = 400 000 draws.

Companion to lesson 01-13-09.

Each case quotes a first-order (linearised) uncertainty and the uncertainty
measured from a Monte Carlo ensemble, with the Monte Carlo standard error on
that measurement. Where the two disagree, the disagreement is the point, and
the reason is stated.
"""

import math
import random

SEED = 20240125
N = 400_000


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def mean(xs):
    return sum(xs) / len(xs)


def stdev(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def se_of_sd(sd, n):
    return sd / math.sqrt(2.0 * (n - 1))


def report(label, analytic, mc_sd, n):
    se = se_of_sd(mc_sd, n)
    ratio = abs(mc_sd - analytic) / se
    print(f"  {label}")
    print(f"    first-order sd = {analytic:.6f}")
    print(f"    Monte Carlo sd = {mc_sd:.6f}   (MC standard error {se:.6f}, "
          f"difference {ratio:.2f} SE)")


# --------------------------------------------------------------------------
# 1. Two independent inputs, a ratio
# --------------------------------------------------------------------------

def density_case() -> None:
    section("1. Ratio of two measured quantities: density rho = m / V")
    m, sm = 2.50, 0.02        # kg
    v, sv = 1.00, 0.03        # litres
    rel = math.sqrt((sm / m) ** 2 + (sv / v) ** 2)
    rho = m / v
    print(f"  m = {m} +/- {sm} kg ({100 * sm / m:.3f} %), "
          f"V = {v} +/- {sv} L ({100 * sv / v:.3f} %)")
    print(f"  rho = {rho:.6f}, relative sd = {rel:.6f}, "
          f"sd(rho) = {rho * rel:.6f}")
    rng = random.Random(SEED)
    vals = [rng.gauss(m, sm) / rng.gauss(v, sv) for _ in range(N)]
    report("Monte Carlo check", rho * rel, stdev(vals), N)
    print(f"    Monte Carlo mean = {mean(vals):.6f} against the nominal "
          f"{rho:.6f}")
    print("  For a product or ratio of independent quantities the relative")
    print("  variances add in quadrature. The Monte Carlo spread agrees with the")
    print("  formula; the mean is displaced upward by about 0.1 %, which is the")
    print("  second-order term, not an error in the arithmetic. The estimator")
    print("  m/V is slightly biased because 1/V is convex.")


# --------------------------------------------------------------------------
# 2. Nonlinear function where the error model itself matters
# --------------------------------------------------------------------------

def gaussian_moments_of_inverse_square(r0, rel, n=200_000, span=12.0):
    """E[Y] and sd(Y) for Y = (r0/r)^2, r ~ N(r0, (rel*r0)^2), by Simpson.

    The integration window is truncated at r0 +/- span sigma. That truncation
    removes the region x <= r0 - span sigma, which is where the integrals of
    y and y^2 formally diverge; the omission is stated because it matters.
    """
    sigma = rel * r0
    a, b = r0 - span * sigma, r0 + span * sigma
    h = (b - a) / n

    def density(x):
        z = (x - r0) / sigma
        return math.exp(-0.5 * z * z) / (math.sqrt(2.0 * math.pi) * sigma)

    def moment(power):
        total = 0.0
        for i in range(n + 1):
            x = a + i * h
            w = 1.0 if i in (0, n) else (4.0 if i % 2 else 2.0)
            total += w * density(x) * (r0 / x) ** (2 * power)
        return total * h / 3.0

    e1 = moment(1)
    e2 = moment(2)
    return e1, math.sqrt(max(e2 - e1 * e1, 0.0))


def nonlinear_case() -> None:
    section("2. Nonlinear function g = G M / r^2")
    G, M, r = 6.674e-11, 1.0e12, 1000.0
    g0 = G * M / r ** 2
    print(f"  G = {G:.3e} (exact), M = {M:.3e} kg (exact), r = {r} m")
    print(f"  g(r) = {g0:.6e} m/s^2.  First order: sd(g)/g0 = 2 sd(r)/r")

    rel = 0.05
    e1, exact_sd = gaussian_moments_of_inverse_square(r, rel)
    rng = random.Random(SEED + int(rel * 100))
    vals = [G * M / rng.gauss(r, rel * r) ** 2 / g0 for _ in range(N)]
    print(f"\n  Gaussian r with sd(r)/r = {rel:.2f}")
    print(f"    first-order sd(g)/g0        = {2 * rel:.6f}")
    print(f"    exact sd by quadrature      = {exact_sd:.6f}")
    print(f"    Monte Carlo sd              = {stdev(vals):.6f}  "
          f"(MC standard error {se_of_sd(stdev(vals), N):.6f})")
    print(f"    exact E[g]/g0 by quadrature = {e1:.6f}")
    print(f"    Monte Carlo mean of g/g0    = {mean(vals):.6f}")
    print("    The linearised value is 2.1 % below the exact one. The excess is")
    print("    the curvature of r^-2, and Monte Carlo reproduces the quadrature")
    print("    result to a few parts in 10^4.")

    rel = 0.30
    rng = random.Random(SEED + 30)
    draws = [rng.gauss(r, rel * r) for _ in range(N)]
    vals = [G * M / x ** 2 / g0 for x in draws]
    nonpos = sum(1 for x in draws if x <= 0.0)
    srt = sorted(vals)
    print(f"\n  Gaussian r with sd(r)/r = {rel:.2f}")
    print(f"    first-order sd(g)/g0        = {2 * rel:.6f}")
    print(f"    Monte Carlo sd              = {stdev(vals):.6f}  (not a")
    print(f"      meaningful quantity: see below)")
    print(f"    Monte Carlo mean of g/g0    = {mean(vals):.6f}")
    print(f"    Monte Carlo median of g/g0  = {srt[N // 2]:.6f}")
    print(f"    draws with r <= 0           = {nonpos} "
          f"({100 * nonpos / N:.4f} % of draws)")
    print("    Here the model breaks. The integrals for the mean and variance of")
    print("    GM/r^2 do not converge, because 1/r^2 grows faster near r = 0 than")
    print("    the Gaussian density decays, and at this width the Gaussian puts a")
    print("    genuinely reachable probability below r = 0. A handful of near-zero")
    print("    draws dominate the sample spread, so the quoted 'standard")
    print("    deviation' of 53 349 describes the sample, not the physics. The")
    print("    median (0.9983) is stable; the mean is not an estimate of anything.")
    print("    At 5 % the same divergence exists formally but is suppressed by a")
    print("    factor of order exp(-200) at r = 0, so no finite sample can see it.")
    print("    A divergence you cannot reach is still a warning about the model.")

    print("\n  A positive quantity needs a positive error model. Take log r")
    print("  normal with relative sd s, so g/g0 = exp(-2Z), Z ~ N(0, sigma_L^2),")
    print("  sigma_L^2 = ln(1 + s^2). Then exactly")
    print("      E[g]/g0 = (1+s^2)^2,  sd(g)/g0 = (1+s^2)^2 sqrt((1+s^2)^4 - 1).")
    print(f"  {'s':>6}  {'first order 2s':>15}  {'exact sd':>12}  "
          f"{'MC sd':>12}  {'MC mean':>10}  {'exact mean':>11}")
    for s in (0.05, 0.15, 0.30, 0.50):
        rng = random.Random(SEED + 100 + int(s * 100))
        sig_log = math.sqrt(math.log(1.0 + s * s))
        vals = [G * M / (r * math.exp(rng.gauss(0.0, sig_log))) ** 2 / g0
                for _ in range(N)]
        factor = (1.0 + s * s) ** 2
        exact = factor * math.sqrt((1.0 + s * s) ** 4 - 1.0)
        print(f"  {s:>6.2f}  {2 * s:>15.6f}  {exact:>12.6f}  "
              f"{stdev(vals):>12.6f}  {mean(vals):>10.6f}  {factor:>11.6f}")
    print("  With a positive error model every Monte Carlo column reproduces the")
    print("  closed form, and the picture is quantitative rather than")
    print("  catastrophic: first order understates the spread by 0.7 % at s =")
    print("  0.05, 6 % at s = 0.15, 27 % at s = 0.30 and 88 % at s = 0.50. The")
    print("  error is one-sided, so a linearised uncertainty budget on a")
    print("  strongly nonlinear quantity is optimistic, never conservative.")


# --------------------------------------------------------------------------
# 3. Two-way travel time to depth
# --------------------------------------------------------------------------

def depth_case() -> None:
    section("3. Depth from two-way travel time: d = v T / 2")
    v, sv = 3000.0, 100.0       # m/s
    T, sT = 0.500, 0.005        # s
    d = v * T / 2.0
    rel = math.sqrt((sv / v) ** 2 + (sT / T) ** 2)
    print(f"  v = {v} +/- {sv} m/s ({100 * sv / v:.3f} %)")
    print(f"  T = {T} +/- {sT} s ({100 * sT / T:.3f} %)")
    print(f"  d = v T / 2 = {d:.4f} m")
    print(f"  relative sd = sqrt((sv/v)^2 + (sT/T)^2) = {rel:.6f}")
    print(f"  sd(d)       = {d * rel:.6f} m")
    rng = random.Random(SEED + 7)
    vals = [rng.gauss(v, sv) * rng.gauss(T, sT) / 2.0 for _ in range(N)]
    report("Monte Carlo check", d * rel, stdev(vals), N)
    print(f"  The velocity term contributes {100 * sv / v:.3f} % and the timing")
    print(f"  term {100 * sT / T:.3f} %; velocity dominates. Reporting only the")
    print(f"  timing error would understate sd(d) by a factor of "
          f"{rel / (sT / T):.2f}. Quoting the uncertainty of the quantity one")
    print("  measured well while omitting the one converted through an assumed")
    print("  velocity is one of the commonest errors in a depth estimate.")


# --------------------------------------------------------------------------
# 4. Common-mode cancellation in a difference
# --------------------------------------------------------------------------

def common_mode_case() -> None:
    section("4. Correlated inputs: a shared calibration error in a difference")
    sb, si = 0.30, 1.00       # mGal: shared bias sd, independent noise sd
    rng = random.Random(SEED + 8)
    diffs = []
    for _ in range(N):
        bias = rng.gauss(0.0, sb)
        g1 = rng.gauss(0.0, si) + bias
        g2 = rng.gauss(0.0, si) + bias
        diffs.append(g2 - g1)
    rho = sb * sb / (sb * sb + si * si)
    naive = math.sqrt(2.0) * math.sqrt(sb * sb + si * si)
    correct = math.sqrt(2.0) * si
    print(f"  sd of shared calibration bias = {sb} mGal")
    print(f"  sd of independent reading noise = {si} mGal")
    print(f"  correlation implied by the shared bias = {rho:.6f}")
    print("\n  If the readings were treated as independent:")
    report("    sd of the difference:", naive, stdev(diffs), N)
    print("\n  Using Var(g2 - g1) = 2 sigma_i^2, because the bias is common:")
    report("    sd of the difference:", correct, stdev(diffs), N)
    print("\n  The shared calibration error cancels exactly in the difference,")
    print("  and the correlated formula matches the Monte Carlo result to well")
    print("  under one standard error while the independent formula overshoots by")
    print(f"  {100 * (naive / correct - 1):.1f} %. This is the arithmetic behind")
    print("  relative gravity, differential GNSS and differential InSAR: common")
    print("  drift subtracts out, so a difference can be more precise than either")
    print("  measurement. It also shows the cost of the assumption: the same")
    print("  formula applied where errors are correlated but do *not* cancel, or")
    print("  where they are anti-correlated, would be wrong by the same amount in")
    print("  the opposite direction. Correlation must be argued physically, not")
    print("  assumed away.")


def main() -> None:
    density_case()
    nonlinear_case()
    depth_case()
    common_mode_case()
    print("\nDone. Reproducible with seed 20240125.")


if __name__ == "__main__":
    main()
