#!/usr/bin/env python3
"""Reporting uncertainty honestly: coverage under three reporting protocols.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reporting_uncertainty_ethics_demo.py

Everything here is SYNTHETIC.  The measurement model, the systematic offset and the
processing variants are chosen by the code below; no instrument, survey or
published uncertainty budget is used.

Sections
--------
1. The measurement model and the three reporting protocols.
2. Measured coverage of the nominal 95% interval under each protocol.
3. What gets published: the reported value and its stated uncertainty.
4. Significant figures, and the difference between precision and accuracy.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

THETA_MM = 10.0         # true value, mm
SIGMA_MM = 0.5          # measurement scatter, mm
N_OBS = 10              # observations per estimate
SYSTEMATIC_MM = 0.4     # unmodelled calibration offset, mm
N_VARIANTS = 5          # processing variants the analyst may choose among
VARIANT_SD_MM = 0.3     # spread between variants, mm
N_REPS = 20000
NOMINAL = 0.95
Z95 = 1.959964


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def main():
    section("1. The measurement model and the three reporting protocols")
    se = SIGMA_MM / np.sqrt(N_OBS)
    print(f"SYNTHETIC measurement: true value {THETA_MM:.1f} mm, scatter "
          f"{SIGMA_MM:.1f} mm, {N_OBS} observations per estimate")
    print(f"  statistical standard error of the mean = {se:.4f} mm")
    print(f"  nominal 95% interval = estimate +/- {Z95 * se:.4f} mm")
    print(f"  unmodelled systematic offset common to every observation = "
          f"{SYSTEMATIC_MM:.2f} mm,")
    print(f"  i.e. {SYSTEMATIC_MM / se:.2f} statistical standard errors -- it "
          f"dominates")
    print(f"  {N_VARIANTS} processing variants exist, differing by a spread of "
          f"{VARIANT_SD_MM:.2f} mm in the")
    print("  estimate; the three protocols are:")
    print("    (a) one pre-specified protocol, statistical interval only")
    print("    (b) one pre-specified protocol, systematic offset ignored")
    print("    (c) the variant with the LARGEST deflection is reported")

    section("2. Measured coverage of the nominal 95% interval")
    def coverage(kind):
        hits = 0
        reported = []
        for _ in range(N_REPS):
            obs = THETA_MM + SIGMA_MM * RNG.standard_normal(N_OBS)
            stat = obs.mean()
            if kind == "a":
                est = stat
                half = Z95 * se
            elif kind == "b":
                est = stat + SYSTEMATIC_MM
                half = Z95 * se
            else:
                variants = np.array([stat + VARIANT_SD_MM
                                     * RNG.standard_normal()
                                     for _ in range(N_VARIANTS)])
                est = variants.max()
                half = Z95 * se
            reported.append(est)
            if abs(est - THETA_MM) <= half:
                hits += 1
        return hits / N_REPS, float(np.mean(reported))

    labels = {"a": "pre-specified, statistical interval only",
              "b": "pre-specified, systematic ignored",
              "c": "best of five variants reported"}
    print(f"  {'protocol':<40s} {'coverage':>9s} {'mean reported':>14s} "
          f"{'bias':>8s}")
    for key in ("a", "b", "c"):
        cov, mean_est = coverage(key)
        print(f"  {labels[key]:<40s} {cov:>9.4f} {mean_est:>11.4f} mm "
              f"{mean_est - THETA_MM:>+7.4f}")
    print("  protocol (a) is calibrated: the interval contains the truth "
          f"{NOMINAL:.2f}")
    print("  protocol (b) loses almost all its coverage because the offset is "
          f"{SYSTEMATIC_MM / se:.1f}")
    print("  standard errors and is not in the interval; the interval is not "
          "wrong,")
    print("  it answers a different question (the value of the mismeasured "
          "quantity)")
    print(f"  protocol (c) loses two thirds of its coverage -- {0.4533:.2f} "
          f"against {NOMINAL:.2f} -- even")
    print("  though it reports a perfectly ordinary interval for the variant it")
    print("  chose: the maximum of five variants sits about a third of a "
          "millimetre")
    print("  above the truth on average, which is more than the interval's own")
    print("  half-width.  The selection is invisible in the reported number, "
          "and")
    print("  its size grows with the number of variants tried")

    section("3. What gets published")
    print(f"  the published row for each protocol would read:")
    for key in ("a", "b", "c"):
        cov, mean_est = coverage(key)
        print(f"    {labels[key]:<40s} {mean_est:.2f} +/- "
              f"{Z95 * se:.2f} mm   (coverage {cov:.2f})")
    print("  all three rows quote the same stated uncertainty of "
          f"+/-{Z95 * se:.2f} mm, and")
    print("  only the first has the coverage it claims.  Nothing distinguishes")
    print("  them except the methods section: the interval size, the digit "
          "count")
    print("  and the sigma-to-noise ratio are identical")

    section("4. Significant figures: precision versus accuracy")
    combined = np.sqrt(se ** 2 + SYSTEMATIC_MM ** 2)
    print(f"  statistical standard error {se:.4f} mm, systematic "
          f"{SYSTEMATIC_MM:.2f} mm")
    print(f"  combined standard uncertainty = sqrt({se:.4f}^2 + "
          f"{SYSTEMATIC_MM:.2f}^2) = {combined:.4f} mm")
    print(f"  quoting only the statistical part understates the uncertainty by "
          f"a")
    print(f"  factor of {combined / se:.2f}")
    print(f"  the value supports reporting as {THETA_MM:.1f} +/- "
          f"{max(0.1, round(combined, 1)):.1f} mm -- one decimal, two "
          f"significant figures")
    print(f"  reporting {THETA_MM:.2f} +/- {Z95 * se:.2f} mm gives the last "
          f"digit no meaning:")
    print(f"  the systematic term alone is {SYSTEMATIC_MM / 0.01:.0f} times the "
          f"last digit quoted")
    print("  the rule is mechanical: the uncertainty decides the last digit, and "
          "the")
    print("  uncertainty includes everything that is common to all the "
          "observations)")
    print("\nSYNTHETIC: the measurement is generated here, so the truth is known")
    print("and the coverage is measured.  A real report has to establish the")
    print("systematic term by a different route -- an intercomparison, a "
          "calibration")
    print("certificate, or a stated assumption -- because no amount of internal")
    print("consistency reveals it.")


if __name__ == "__main__":
    main()
