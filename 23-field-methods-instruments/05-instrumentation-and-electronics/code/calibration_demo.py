#!/usr/bin/env python3
"""Calibration arithmetic: a least-squares fit, its residuals, the standard errors of
the calibration parameters, an uncertainty budget and a drift check, on SYNTHETIC
values.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python calibration_demo.py

Everything here is SYNTHETIC.  The reference values, readings, uncertainties and
drift rates are chosen teaching values, and the relations printed are the standard
ones quoted in the text.  No laboratory standard, manufacturer figure or measured
calibration is reproduced.

Sections
--------
1. A five-point calibration: slope, intercept, residuals and their statistics.
2. Standard errors of the slope and intercept, and the relative error of the scale.
3. An uncertainty budget: the components and their shares.
4. Drift between calibrations, and the re-calibration interval it implies.
5. Traceability: the chain and what each link contributes.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def main():
    section("1. A five-point calibration")
    x = np.array([100.0, 200.0, 300.0, 400.0, 500.0])       # raw reading
    y = np.array([10.050, 19.980, 30.030, 40.010, 50.020])  # reference value
    slope = 0.099970
    intercept = 0.027000
    predicted = slope * x + intercept
    residual = y - predicted
    rms = np.sqrt((residual ** 2).mean())
    sd = np.sqrt((residual ** 2).sum() / (len(x) - 2))
    print(f"  fit: value = {slope:.6f} x raw + {intercept:.6f}")
    print(f"  {'raw':>7s} {'reference':>11s} {'fitted':>11s} {'residual':>10s}")
    for xi, yi, pi, ri in zip(x, y, predicted, residual):
        print(f"  {xi:7.0f} {yi:11.3f} {pi:11.4f} {ri:+10.4f}")
    print(f"  RMS residual (n = {len(x)}) = {rms:.5f}")
    print(f"  residual standard deviation (n - 2 = {len(x) - 2}) = {sd:.5f}")
    print("  -> the RMS is a description of the points; the standard deviation")
    print("     with n - 2 degrees of freedom is the input to the parameter")
    print("     uncertainties, and the difference grows as the fit has fewer")
    print("     points to spare.")

    section("2. Standard errors of the calibration")
    sum_dev2 = float(((x - x.mean()) ** 2).sum())
    se_slope = sd / np.sqrt(sum_dev2)
    se_intercept = sd * np.sqrt(1.0 / len(x) + x.mean() ** 2 / sum_dev2)
    print(f"  sum of squared deviations of x = {sum_dev2:.0f}")
    print(f"  standard error of the slope     = {se_slope:.6e} "
          f"value units per count")
    print(f"  relative error of the slope     = "
          f"{100.0 * se_slope / slope:.4f} %")
    print(f"  standard error of the intercept = {se_intercept:.5f} value units")
    print(f"  the scale is known to {100.0 * se_slope / slope:.3f} % and the")
    print(f"  offset to {se_intercept:.3f} value units at one standard error")
    print("  -> the *scale* uncertainty is what a quantitative measurement")
    print("     inherits; the offset matters only for absolute values.")

    section("3. An uncertainty budget for the calibrated measurement")
    terms = [("fit residual", sd),
             ("reference standard", 0.020),
             ("repeatability of a check", 0.010),
             ("drift since calibration", 0.005)]
    total = np.sqrt(sum(v ** 2 for _, v in terms))
    print(f"  {'component':<30s} {'value':>10s} {'share of variance':>18s}")
    for label, value in terms:
        print(f"  {label:<30s} {value:10.5f} {100.0 * value ** 2 / total ** 2:17.1f} %")
    print(f"  {'total (quadrature)':<30s} {total:10.5f} {100.0:17.1f} %")
    print("  -> the dominant term is the fit residual, which is set by the")
    print("     calibration's own scatter, not by the reference's accuracy:")
    print("     adding calibration points is the effective improvement.")

    section("4. Drift between calibrations")
    drift_per_day = 0.005
    tolerance = 0.05
    print(f"  SYNTHETIC drift {drift_per_day:.4f} value units per day, "
          f"tolerance {tolerance:.2f}")
    print(f"  {'days since calibration':>24s} {'drift':>9s} {'within tol.?':>14s}")
    for days in (1, 5, 10, 20, 50):
        d = drift_per_day * days
        print(f"  {days:24d} {d:9.3f} "
              f"{('yes' if d <= tolerance else 'no'):>14s}")
    print(f"  the re-calibration interval at this tolerance is "
          f"{tolerance / drift_per_day:.0f} days")
    print("  -> the interval is set by the *tolerance* and the *drift rate*,")
    print("     both of which must be measured; an interval chosen by habit has")
    print("     no relationship to either.")

    section("5. Traceability")
    print(f"  {'link':<38s} {'contribution':<28s}")
    links = [("definition (SI unit)", "exact by definition",),
             ("national standard realisation", "stated by the institute"),
             ("laboratory reference", "calibration certificate"),
             ("working standard", "before-and-after check"),
             ("field instrument", "this calibration")]
    for link, contribution in links:
        print(f"  {link:<38s} {contribution:<28s}")
    print("  -> each link must have a documented uncertainty, and the")
    print("     measurement's uncertainty is the quadrature sum down the chain,")
    print("     not the last link's alone.")

    print("\nSYNTHETIC: every number above comes from chosen parameters in this")
    print("file, combined with the standard relations quoted in the text.")


if __name__ == "__main__":
    main()
