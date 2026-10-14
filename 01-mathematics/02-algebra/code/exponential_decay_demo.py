"""Exponentials, logarithms and decay laws in the Earth sciences.

Run:  python3 exponential_decay_demo.py
Requires: Python standard library only.

Companion to lesson 01-02-03. All data below are SYNTHETIC: they are generated
from the stated model so that the recovery of the model parameters can be
checked exactly. Nothing here is a measurement of a real sample.
"""

import math


def section(title: str) -> None:
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def least_squares_line(xs: list[float], ys: list[float]) -> tuple[float, float]:
    """Return (slope, intercept) of the ordinary least-squares line."""
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    intercept = (sy - slope * sx) / n
    return slope, intercept


def main() -> None:
    section("1. One decay law, three equivalent parameterisations")
    half_life = 5730.0                      # years, conventional 14C half-life
    lam = math.log(2.0) / half_life        # per year
    tau = 1.0 / lam                        # mean life, years
    print(f"14C half-life T = {half_life:.0f} yr  (commonly quoted as 5730 +/- 40 yr)")
    print(f"decay constant lambda = ln2 / T = {lam:.6e} /yr")
    print(f"mean life tau = 1/lambda = {tau:.1f} yr")
    print("lambda, T and tau are three ways to write the same number; the")
    print("half-life is convenient for reading, lambda for calculus.")
    print(f"\n{'t (yr)':>8} {'t/T':>6} {'N/N0 = exp(-lambda t)':>24} {'2**(-t/T)':>14}")
    for t in (0.0, 1000.0, 5730.0, 11460.0, 28650.0, 57300.0):
        print(f"{t:>8.0f} {t / half_life:>6.2f} {math.exp(-lam * t):>24.8f} "
              f"{2.0 ** (-t / half_life):>14.8f}")
    print("After ten half-lives only 1/1024 of the original 14C remains; that")
    print("is why the practical limit of the method is about 10 half-lives.")

    section("2. Age from a measured activity ratio (14C)")
    print(f"{'N/N0':>10} {'conventional age (yr)':>24}")
    for ratio in (0.9, 0.5, 0.25, 0.1, 0.01):
        age = -math.log(ratio) / lam
        print(f"{ratio:>10.3f} {age:>24.0f}")
    print("This is the *conventional* radiocarbon age, which assumes a constant")
    print("atmospheric 14C level. Converting it to a calendar age requires a")
    print("calibration curve; the calculation above is only the first step.")

    section("3. The isochron equation for a long-lived parent (238U -> 206Pb)")
    u238_half_life = 4.468e9                # years
    lam_u = math.log(2.0) / u238_half_life
    print(f"238U half-life = {u238_half_life:.4e} yr, lambda = {lam_u:.6e} /yr")
    print(f"{'206Pb*/238U':>12} {'age (Ma)':>12}")
    for ratio in (0.1, 0.5, 1.0, 2.0, 4.0):
        age = math.log(1.0 + ratio) / lam_u / 1.0e6
        print(f"{ratio:>12.2f} {age:>12.1f}")
    print("The equation used is D*/P = exp(lambda t) - 1, inverted as")
    print("t = ln(1 + D*/P)/lambda. The logarithm is what turns a ratio into a")
    print("date; doubling the ratio does not double the age.")

    section("4. Fitting the decay constant to synthetic counting data")
    # SYNTHETIC: exact counts following N(t) = N0 exp(-lambda t), no noise.
    n0 = 10000.0
    true_half_life = 14.0                   # days, arbitrary but stated
    true_lam = math.log(2.0) / true_half_life
    days = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0]
    counts = [n0 * math.exp(-true_lam * t) for t in days]
    slope, intercept = least_squares_line(days, [math.log(c) for c in counts])
    fitted_lam = -slope
    print(f"true lambda = {true_lam:.6f} /day  (T = {true_half_life} days)")
    print(f"fit of ln N against t: slope = {slope:.6f} /day, "
          f"intercept = {intercept:.6f}")
    print(f"fitted lambda = {fitted_lam:.6f} /day -> T = "
          f"{math.log(2.0) / fitted_lam:.4f} days")
    print(f"intercept means N0 = exp({intercept:.6f}) = {math.exp(intercept):.2f} "
          f"counts (true {n0:.0f})")
    print("Because the data are exact, the fit reproduces the parameters; with")
    print("real counts the scatter in ln N would broaden the confidence interval.")

    section("5. Seismic attenuation: amplitude decay and the quality factor Q")
    f, v, q = 20.0, 3500.0, 100.0           # Hz, m/s, dimensionless
    alpha = math.pi * f / (q * v)          # amplitude attenuation, 1/m
    print(f"f = {f:.0f} Hz, v = {v:.0f} m/s, Q = {q:.0f}")
    print(f"attenuation coefficient alpha = pi f / (Q v) = {alpha:.3e} /m")
    print(f"skin depth 1/alpha = {1.0 / alpha:.1f} m")
    print(f"\n{'x (m)':>8} {'A/A0':>12}")
    for x in (0.0, 100.0, 200.0, 500.0, 1000.0):
        print(f"{x:>8.0f} {math.exp(-alpha * x):>12.6f}")
    ratio = math.exp(-alpha * 200.0) / math.exp(-alpha * 100.0)
    q_recovered = -math.pi * f * 100.0 / (v * math.log(ratio))
    print(f"From A(200)/A(100) = {ratio:.6f} we recover Q = {q_recovered:.1f}")

    section("6. Newton cooling of a shallow intrusion")
    # Temperature of a body relaxing to its surroundings.
    t_inf, t_0, tau_cool = 10.0, 900.0, 4.0  # degC, degC, days
    temperature = lambda t: t_inf + (t_0 - t_inf) * math.exp(-t / tau_cool)
    print(f"T(t) = {t_inf} + ({t_0} - {t_inf}) exp(-t/{tau_cool})  [t in days]")
    print(f"{'t (days)':>9} {'T (degC)':>10} {'excess T - 10':>14} "
          f"{'ln(excess)':>11}")
    for t in (0.0, 2.0, 4.0, 8.0, 16.0):
        excess = temperature(t) - t_inf
        print(f"{t:>9.1f} {temperature(t):>10.4f} {excess:>14.4f} "
              f"{math.log(excess):>11.5f}")
    # Time to reach a threshold temperature, solved by rearranging.
    threshold = 100.0
    t_threshold = -tau_cool * math.log((threshold - t_inf) / (t_0 - t_inf))
    print(f"Time to cool to {threshold:.0f} degC: "
          f"t = -tau ln((T-T_inf)/(T0-T_inf)) = {t_threshold:.3f} days")
    print(f"check: T({t_threshold:.3f}) = {temperature(t_threshold):.6f} degC")
    print("Solving for time requires the logarithm; that inversion is the whole")
    print("reason the exponential appears in every thermal and nuclear age")
    print("equation.")


if __name__ == "__main__":
    main()
