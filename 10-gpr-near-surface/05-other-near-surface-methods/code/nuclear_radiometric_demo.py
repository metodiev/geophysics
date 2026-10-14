#!/usr/bin/env python3
"""Nuclear and radiometric near-surface methods: counting statistics, detection
limits, gamma-ray attenuation and the depth of origin, three-window stripping and
its conditioning, and a neutron-moisture calibration.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nuclear_radiometric_demo.py

Everything here is SYNTHETIC.  The attenuating materials, activities, stripping
factors, detector efficiencies and water contents are chosen teaching values.
They are not measurements, not detector specifications and not site parameters.
The three gamma energies quoted are standard nuclear-data constants.

Contents
--------
1. Poisson counting statistics: the measured scatter of repeated counts.
2. Counting time for a target precision.
3. Critical level and detection limit for a net count measurement.
4. Gamma-ray attenuation: half-value layer and the depth the signal comes from.
5. Three-window stripping: conditioning and error amplification.
6. Neutron moisture gauge: calibration, count statistics and a mis-calibration bias.
"""

import numpy as np
from scipy.optimize import brentq
from scipy.special import exp1

RNG = np.random.default_rng(20261014)

GAMMA_LINES = {          # standard nuclear-data gamma energies
    "K-40": 1.4608e6,    # eV
    "Bi-214 (U-238 series)": 1.7645e6,
    "Tl-208 (Th-232 series)": 2.6145e6,
}


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. Poisson counting statistics")
    rate = 12.0          # counts/s, teaching value
    t_count = 30.0       # s
    n_trials = 20000
    counts = RNG.poisson(rate * t_count, n_trials)
    print(f"  true rate {rate:.2f} counts/s, counting time {t_count:.1f} s, "
          f"{n_trials} repeat measurements")
    print(f"  mean counts        = {counts.mean():.3f}  (expected {rate * t_count:.1f})")
    print(f"  measured std       = {counts.std(ddof=1):.3f}")
    print(f"  sqrt(mean counts)  = {np.sqrt(counts.mean()):.3f}")
    print(f"  ratio measured/sqrt(mean) = {counts.std(ddof=1) / np.sqrt(counts.mean()):.4f}")
    print("  For a Poisson process the variance equals the mean, so the standard")
    print("  deviation of a count N is sqrt(N) and the relative precision improves")
    print("  only as 1/sqrt(N): a radiometric measurement is a statistics-limited")
    print("  measurement before it is a geophysical one.")

    section("2. Counting time for a target precision")
    print("  to reach a relative precision e on N counts we need N >= 1/e^2:")
    print("    target e    required counts   time at 12 counts/s (s)")
    for e in (0.20, 0.10, 0.05, 0.02, 0.01):
        n_req = 1.0 / e ** 2
        print(f"    {e:8.2f}   {n_req:15.0f}   {n_req / rate:22.2f}")

    section("3. Critical level and detection limit")
    n_bg = 900.0          # background counts in the counting time (60 s), teaching value
    k = 1.6448536269514722      # standard normal 95th percentile, exact
    print(f"  counting time 60 s, background rate {n_bg / 60.0:.2f} counts/s, "
          f"one-sided 95% (k = {k:.6f})")
    print("   time (s)   N_B (counts)   L_C (counts)   L_D (counts)   L_D rate (counts/s)")
    for t in (30.0, 60.0, 120.0, 240.0):
        nb = n_bg * t / 60.0
        lc = k * np.sqrt(2.0 * nb)

        def f(ld, nb=nb, lc=lc):
            return lc + k * np.sqrt(2.0 * nb + ld) - ld

        ld = brentq(f, lc, 50.0 * lc, xtol=1e-9)
        print(f"  {t:9.0f}   {nb:13.1f}   {lc:13.2f}   {ld:13.2f}   {ld / t:18.3f}")
    print("  L_C is the smallest net count that would be called a detection 95% of the")
    print("  time when nothing is there; L_D is the true net signal detected 95% of the")
    print("  time.  Both grow with the counting time in counts but fall as 1/sqrt(t) in")
    print("  rate: a longer count is the only thing that buys sensitivity.")

    section("4. Gamma attenuation and the depth the signal comes from")
    mu_over_rho = 0.0055   # m^2/kg = 0.055 cm^2/g, teaching value at these energies
    rho_bulk = 1600.0      # kg/m^3, teaching value for soil
    mu = mu_over_rho * rho_bulk
    print(f"  mass attenuation coefficient mu/rho = {mu_over_rho:.4f} m^2/kg "
          f"(teaching value), bulk density rho = {rho_bulk:.0f} kg/m^3")
    print(f"  effective linear attenuation mu = {mu:.2f} 1/m; the plane-source "
          f"half-value layer is ln2/mu = {np.log(2.0) / mu:.4f} m")
    print("  For a detector above a half-space of uniform activity, integrating the")
    print("  unscattered flux over each horizontal layer gives a layer response")
    print("  proportional to the exponential integral E1(mu z), so the fraction of the")
    print("  signal originating above depth z is mu z E1(mu z) + 1 - exp(-mu z).")
    print("     depth (m)   cumulative fraction   per-metre weight E1(mu z)/E1(0)")
    for z in (0.02, 0.05, 0.10, 0.20, 0.30, 0.50, 1.00):
        u = mu * z
        cum = u * exp1(u) + 1.0 - np.exp(-u)
        print(f"     {z:9.2f}   {cum:19.4f}   {exp1(u) / exp1(1e-9):26.4f}")
    for frac in (0.50, 0.63, 0.90, 0.95):
        zf = brentq(lambda zz: mu * zz * exp1(mu * zz) + 1.0 - np.exp(-mu * zz) - frac,
                    1e-9, 50.0, xtol=1e-12)
        print(f"    {frac * 100:.0f}% of the signal comes from the top {zf * 100:6.2f} cm")
    zz = np.linspace(1e-9, 20.0 / mu, 200001)
    weight = exp1(mu * zz)
    mean_z = float(np.trapezoid(zz * weight, zz) / np.trapezoid(weight, zz))
    print(f"  mean depth of origin = {mean_z * 100:.2f} cm = 1/({1.0 / (mu * mean_z):.2f} mu):")
    print("  the signal is dominated by the top few centimetres yet has a long tail, so")
    print("  'the top 30 cm' describes the cumulative, not the average.  Both matter: a")
    print("  thin surface layer of a different activity changes the reading as much as a")
    print("  thick layer at depth.")

    section("5. Three-window stripping and its conditioning")
    A = np.array([[1.00, 0.20, 0.05],
                  [0.10, 1.00, 0.15],
                  [0.03, 0.12, 1.00]])
    print("  synthetic sensitivity matrix (rows: windows K, U, Th; columns: nuclides):")
    for row in A:
        print("   ", "  ".join(f"{v:6.3f}" for v in row))
    print(f"  condition number (2-norm) = {np.linalg.cond(A):.3f}, determinant = "
          f"{np.linalg.det(A):.5f}")
    Ainv = np.linalg.inv(A)
    print("  stripping matrix (inverse):")
    for row in Ainv:
        print("   ", "  ".join(f"{v:7.4f}" for v in row))
    err = 0.01
    acts_err = np.abs(Ainv).sum(axis=1) * err
    print(f"  a 1% error in every window count rate gives errors in the stripped")
    print("  activities of: " + ", ".join(f"{v * 100:.3f}%" for v in acts_err))
    print("  The amplification is modest here because the off-diagonal terms are")
    print("  small; with realistic overlapping windows it grows, and the order of the")
    print("  windows and the accuracy of the factors decide the result.")
    A_wrong = A.copy()
    A_wrong[0, 1] *= 1.05          # 5% error in one stripping factor
    instr = np.linalg.solve(A_wrong, A)
    test = np.ones(3)
    print("  a 5% error in a single stripping factor, applied to a unit-activity")
    print(f"  ground, returns activities {np.round(instr @ test, 4)} instead of "
          f"{np.round(test, 4)}")

    section("6. Neutron moisture gauge: calibration and its limits")
    theta = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30])
    counts_per_s = 100.0 + 900.0 * theta        # synthetic linear response
    t_gauge = 60.0
    meas = RNG.poisson(counts_per_s * t_gauge) / t_gauge
    slope, intercept = np.polyfit(theta, meas, 1)
    print(f"  synthetic response {counts_per_s[:1][0]:.0f}-{counts_per_s[-1]:.0f} counts/s,")
    print(f"  {t_gauge:.0f} s per reading, Poisson noise:")
    print("    theta (v/v)   expected (c/s)   measured (c/s)")
    for th, ex, me in zip(theta, counts_per_s, meas):
        print(f"    {th:11.2f}   {ex:14.1f}   {me:14.1f}")
    print(f"  fitted calibration: counts/s = {slope:.1f} theta + {intercept:.1f}")
    print(f"  true calibration  : counts/s = 900.0 theta + 100.0")
    print(f"  slope error {abs(slope - 900.0) / 900.0 * 100:.2f}%, "
          f"intercept error {abs(intercept - 100.0) / 100.0 * 100:.2f}%")
    n_cal = counts_per_s * t_gauge
    print(f"  at theta = 0.20 the count is {n_cal[3]:.0f}, so the one-sigma count")
    print(f"  error is {np.sqrt(n_cal[3]):.1f} counts/s = "
          f"{np.sqrt(n_cal[3]) / t_gauge:.2f} counts/s, which is "
          f"{np.sqrt(n_cal[3]) / t_gauge / slope * 100:.3f} percentage points of water content.")
    theta_shift = 0.02
    print(f"  a material change that shifts the calibration by {theta_shift * 100:.0f}% "
          f"water content (a density or absorption change) is")
    print("  a systematic error far larger than the counting statistics: the gauge")
    print("  measures thermal-neutron moderation, and the calibration belongs to the")
    print("  material, not to the instrument.")

    section("7. Summary")
    print("  Radiometric measurements are Poisson-limited: precision costs counting")
    print("  time as 1/e^2, so the method is cheap only for large signals.  Gamma rays")
    print("  come from the top few decimetres of soil, which fixes the depth of")
    print("  investigation and the interpretation.  Windows overlap, so the nuclide")
    print("  activities are obtained by inverting a stripping matrix whose conditioning")
    print("  limits the accuracy.  Nuclear gauges measure density and water content")
    print("  through material-specific calibrations, and their precision is set by")
    print("  counting statistics while their accuracy is set by the calibration.")
    for name, energy in GAMMA_LINES.items():
        print(f"  standard gamma line: {name}: {energy / 1e6:.4f} MeV")


if __name__ == "__main__":
    main()
