"""Uncertainty as a physical quantity: propagation, coverage and weighting.

Run:  python3 uncertainty_demo.py
Requires: Python standard library only.

Companion to lesson 02-01-02.  Three things are demonstrated with numbers that
are printed rather than asserted:

1.  A measured value with a resolution and a scatter is summarised correctly,
    and the report is rounded to a defensible number of significant figures.
2.  Analytic first-order propagation in quadrature is checked against a
    Monte Carlo simulation that assumes nothing but the input distributions.
    Where the two disagree, the analytic formula is the one that is wrong --
    and the size of the disagreement is printed.
3.  Independent measurements with different uncertainties are combined by
    inverse-variance weighting, and the chi-square of the combination is
    reported so that the combination can be judged rather than trusted.

All measurement values are SYNTHETIC.  The gravitational constant and its
relative uncertainty are taken from the constant handbook (CODATA, measured).
"""

import math
import random

G = 6.67430e-11          # m^3 kg^-1 s^-2, measured (CODATA 2018)
G_REL = 2.2e-5           # relative standard uncertainty of G, CODATA


def section(title: str) -> None:
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def mean(xs):
    return sum(xs) / len(xs)


def stdev(xs):
    """Sample standard deviation (n - 1 denominator)."""
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def fmt(value: float, unc: float) -> str:
    """Round to the decimal place of the uncertainty (two digits on it)."""
    if unc <= 0:
        return repr(value)
    e = int(math.floor(math.log10(unc)))
    if -3 <= e <= 5:
        dec = max(0, -e)
        return f"{value:.{dec}f} +- {unc:.{dec}f}"
    factor = 10.0 ** e
    return f"({value / factor:.2f} +- {unc / factor:.2f})e{e:+d}"


def main() -> None:
    random.seed(20261014)

    section("1. A repeated measurement: resolution is not scatter")
    # SYNTHETIC: 20 repeat readings of the same station, in mGal.  The station
    # is fixed, so every difference here is instrument and environment noise.
    readings = [979812.37, 979812.41, 979812.35, 979812.44, 979812.39,
                979812.32, 979812.47, 979812.38, 979812.36, 979812.43,
                979812.40, 979812.29, 979812.45, 979812.42, 979812.33,
                979812.39, 979812.41, 979812.37, 979812.44, 979812.38]
    resolution = 0.01        # mGal, the instrument's display resolution
    m = mean(readings)
    s = stdev(readings)
    sem = s / math.sqrt(len(readings))
    print(f"  n                        = {len(readings)}")
    print(f"  mean                     = {m:.4f} mGal")
    print(f"  sample standard deviation= {s:.4f} mGal")
    print(f"  standard error of mean   = {sem:.4f} mGal")
    print(f"  instrument resolution    = {resolution:.2f} mGal")
    print(f"  scatter / resolution     = {s / resolution:.2f}")
    print("  The scatter is five times the resolution, so quoting the")
    print("  resolution as the uncertainty would understate the error by 5x.")
    print(f"  defensible report        : {fmt(m, s)} mGal (s.d. of a single reading)")
    print(f"  defensible report of mean: {fmt(m, sem)} mGal (standard error)")

    section("2. Analytic propagation: mass inferred from g and depth")
    # z = g d^2 / G  with g, d measured and G uncertain.
    g_meas, g_unc = 7.42e-6, 0.05e-6     # m/s^2  (SYNTHETIC anomaly)
    d_meas, d_unc = 300.0, 2.0           # m      (SYNTHETIC depth)
    z = g_meas * d_meas ** 2 / G
    rel = math.sqrt((g_unc / g_meas) ** 2 + (2 * d_unc / d_meas) ** 2 + G_REL ** 2)
    print(f"  z = g d^2 / G            = {z:.6e} kg")
    print(f"  rel. unc. from g         = {g_unc / g_meas:.6e}")
    print(f"  rel. unc. from d (x2)    = {2 * d_unc / d_meas:.6e}")
    print(f"  rel. unc. from G         = {G_REL:.6e}")
    print(f"  combined (quadrature)    = {rel:.6e}")
    print(f"  absolute uncertainty     = {z * rel:.4e} kg")
    print(f"  reported as              : {fmt(z, z * rel)} kg")
    print(f"  G alone constrains the answer to log10(1/2.2e-5) = "
          f"{math.log10(1 / G_REL):.2f} significant figures.")

    section("3. Monte Carlo check of the quadrature rule")
    n = 200_000
    xs = []
    for _ in range(n):
        gs = random.gauss(g_meas, g_unc)
        ds = random.gauss(d_meas, d_unc)
        xs.append(gs * ds ** 2 / G)
    mc_mean = mean(xs)
    mc_sd = stdev(xs)
    print(f"  Monte Carlo (n = {n})   mean = {mc_mean:.6e} kg, "
          f"sd = {mc_sd:.4e} kg")
    print(f"  analytic                mean = {z:.6e} kg, "
          f"sd = {z * rel:.4e} kg")
    print(f"  ratio of standard deviations = {mc_sd / (z * rel):.6f}")
    print(f"  shift of the mean (x sigma)  = "
          f"{(mc_mean - z) / (z * rel):+.4f}")
    print("  Agreement to a few parts in 10^4 confirms first-order")
    print("  propagation is adequate at these relative uncertainties.")

    section("4. Where quadrature propagation breaks: a ratio of Gaussians")
    b_meas, b_unc = 1.0, 0.5            # SYNTHETIC, 50% uncertainty each
    c_meas, c_unc = 1.0, 0.5
    y = b_meas / c_meas
    y_rel = math.sqrt((b_unc / b_meas) ** 2 + (c_unc / c_meas) ** 2)
    print(f"  y = b / c, each input N(1, 0.5).")
    print(f"  first-order propagation: {y:.4f} +- {y_rel:.4f}")
    print("  The denominator can pass through zero (0.5 = 0.5 sigma from")
    print("  zero at 1 sigma), so the exact distribution has divergent")
    print("  mean and variance.  Watch the sample standard deviation grow")
    print("  with n while the central 68% interval stays put:")
    print("      n          median    q16      q84      sample sd")
    for count in (10_000, 100_000, 1_000_000):
        ys = sorted(random.gauss(b_meas, b_unc) / random.gauss(c_meas, c_unc)
                    for _ in range(count))
        q16 = ys[int(0.1587 * count)]
        q50 = ys[count // 2]
        q84 = ys[int(0.8413 * count)]
        sd = stdev(ys)
        print(f"  {count:9d}  {q50:9.3f} {q16:8.3f} {q84:8.3f}  {sd:10.3f}")
    print("  The 68% interval is stable at roughly [-1, +3]; the standard")
    print("  deviation is not, because the rare near-zero denominators carry")
    print("  enormous weight.  Report quantiles when the model has heavy")
    print("  tails, and say which distribution you are assuming.")

    section("5. Combining independent measurements of one quantity")
    # Four SYNTHETIC determinations of the same anomaly, in mGal.
    data = [(2.10, 0.06), (2.02, 0.04), (2.15, 0.10), (2.04, 0.03)]
    wsum = sum(1.0 / u ** 2 for _, u in data)
    wmean = sum(v / u ** 2 for v, u in data) / wsum
    wunc = math.sqrt(1.0 / wsum)
    plain = mean([v for v, _ in data])
    chi2 = sum((v - wmean) ** 2 / u ** 2 for v, u in data)
    dof = len(data) - 1
    print(f"  measurement        value      unc.")
    for v, u in data:
        print(f"                     {v:6.2f}     {u:4.2f}")
    print(f"  unweighted mean  = {plain:.4f} mGal")
    print(f"  inverse-variance = {wmean:.4f} +- {wunc:.4f} mGal")
    print(f"  chi^2            = {chi2:.4f} for {dof} degrees of freedom")
    print(f"  chi^2 / dof      = {chi2 / dof:.4f}")
    print("  chi^2/dof near 1 means the quoted errors explain the spread.")
    print("  Values well above 1 mean the errors are underestimated or the")
    print("  measurements are inconsistent; both are physics conclusions.")

    section("6. Coverage: what '1 sigma' actually means")
    zs = []
    for _ in range(n):
        zs.append(random.gauss(0.0, 1.0))
    for k in (1, 2, 3):
        frac = sum(1 for x in zs if abs(x) <= k) / n
        print(f"  |z| <= {k}:  observed {frac:.4f}")
    print("  Normal-theory values are 0.6827, 0.9545 and 0.9973.  A 1-sigma")
    print("  interval is a 68% claim, not a guarantee, and it assumes the")
    print("  error distribution is Gaussian and unbiased.")

    section("7. Precision is not accuracy")
    # SYNTHETIC: a biased instrument with tiny scatter.
    truth = 2.00
    bias = 0.30
    readings2 = [truth + bias + random.gauss(0.0, 0.01) for _ in range(20)]
    print(f"  true anomaly            = {truth:.2f} mGal")
    print(f"  mean of 20 readings     = {mean(readings2):.4f} mGal")
    print(f"  standard error of mean  = "
          f"{stdev(readings2) / math.sqrt(20):.5f} mGal")
    print(f"  actual error of the mean= {mean(readings2) - truth:+.4f} mGal")
    print(f"  error / standard error  = "
          f"{(mean(readings2) - truth) / (stdev(readings2) / math.sqrt(20)):.1f}"
          f" sigma")
    print("  The mean is precise to 0.002 mGal and wrong by 0.30 mGal:")
    print("  a systematic error.  Repeating the measurement cannot find it.")

    section("8. An error budget: where the effort belongs")
    # SYNTHETIC survey, representative magnitudes, all inputs stated.
    gradient = 2 * 3.986004418e14 / 6371000.0 ** 3 / 1e-5   # mGal per metre
    budget = [
        ("elevation known to 0.03 m", 0.03 * gradient),
        ("instrument repeatability", 0.010),
        ("tidal correction residual", 0.005),
        ("Bouguer density known to 100 kg/m^3 over 100 m relief",
         2 * math.pi * G * 100.0 * 100.0 / 1e-5),
        ("latitude/correction model residual", 0.002),
    ]
    total = math.sqrt(sum(u ** 2 for _, u in budget))
    print(f"  vertical gravity gradient = {gradient:.4f} mGal/m")
    print("      contribution                          u (mGal)   share")
    for name, u in budget:
        print(f"  {name:44s} {u:8.5f}   {100 * u ** 2 / total ** 2:5.1f} %")
    print(f"  {'combined in quadrature':44s} {total:8.5f}   100.0 %")
    better_instrument = math.sqrt(total ** 2 - 0.010 ** 2 + 0.001 ** 2)
    better_density = math.sqrt(total ** 2 - budget[3][1] ** 2
                               + (2 * math.pi * G * 20.0 * 100.0 / 1e-5) ** 2)
    print(f"  A ten-fold better instrument gives {better_instrument:.5f} mGal")
    print(f"  A five-fold better density    gives {better_density:.5f} mGal")
    print("  The instrument is not the limiting factor, so buying a better one")
    print("  buys nothing.  The budget, not the specification sheet, decides.")


if __name__ == "__main__":
    main()
