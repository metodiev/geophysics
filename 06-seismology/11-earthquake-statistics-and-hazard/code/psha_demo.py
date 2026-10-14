#!/usr/bin/env python3
"""Probabilistic seismic hazard analysis: the total-probability integral, the
hazard curve, deaggregation, and the sensitivity of the answer to its inputs.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python psha_demo.py

Everything is SYNTHETIC.  The source model, the synthetic ground-motion relation
and every coefficient below are teaching values chosen for arithmetic
transparency; none is fitted to a real catalogue and none is quoted from a
published hazard model.

Contents
--------
1. Source model: a Gutenberg-Richter area source and a synthetic ground-motion
   relation; median peak ground acceleration on a (M, R) grid.
2. The hazard curve by numerical evaluation of the total-probability integral,
   with a numerical check that it recovers the total rate at a low amplitude.
3. Return period versus probability: the exact Poisson conversion, and the
   amplitudes that give 10% and 2% probability of exceedance in 50 years.
4. Deaggregation: which magnitudes and distances make the hazard at 0.2 g.
5. Sensitivity to the aleatory sigma and to the epistemic inputs (b and a).
"""

import numpy as np
from scipy.special import erf

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC source model (chosen teaching values) -------------------------
B_GR = 1.00              # Gutenberg-Richter b-value
M_MIN = 4.5              # lower magnitude of the source model
M_MAX = 7.5              # upper magnitude (truncation of the GR law)
RATE_MIN = 0.05          # rate of events with m >= M_MIN, per year
DM = 0.25                # magnitude bin width
R_MIN, R_MAX = 5.0, 50.0  # distance range of the area source, km
R0_KM = 5.0              # near-source saturation distance of the relation, km

# --- SYNTHETIC ground-motion relation (chosen teaching values) ---------------
C0 = 1.411               # ln(PGA) intercept at m = 6, R = R0
C1 = 1.00                # magnitude scaling per magnitude unit
C2 = 1.30                # geometric-spreading coefficient
SIGMA = 0.60             # natural-log standard deviation (aleatory)

PGA_LOW = 0.001          # g; numerical check amplitude
N_R_BINS = 18            # distance discretisation


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def median_pga(m, r, b=1.0):
    """Median PGA in g from the synthetic relation ln PGA = c0 + c1 (m-6)
    - c2 ln(r + R0).  The b argument is unused here and kept so that the
    sensitivity study can swap relations without changing call sites."""
    return np.exp(C0 + C1 * (m - 6.0) - C2 * np.log(r + R0_KM))


def magnitude_rates(b=B_GR, rate_min=RATE_MIN):
    """Rates per year in magnitude bins, for a truncated Gutenberg-Richter law.

    The cumulative rate above m is rate_min x [10^(-b(m-M_MIN)) -
    10^(-b(M_MAX-M_MIN))] / [1 - 10^(-b(M_MAX-M_MIN))], which reaches 0 at
    M_MAX; the rate in a bin is the difference between its two edges.  The bins
    therefore sum exactly to rate_min.
    """
    edges = np.arange(M_MIN, M_MAX + 1e-9, DM)
    m_centers = 0.5 * (edges[:-1] + edges[1:])
    trunc = 1.0 - 10.0 ** (-b * (M_MAX - M_MIN))
    cum = rate_min * (10.0 ** (-b * (edges - M_MIN)) - 10.0 ** (
        -b * (M_MAX - M_MIN))) / trunc
    return m_centers, -(np.diff(cum))


def distance_weights(n_bins=N_R_BINS):
    """Area-source distance distribution: uniform in epicentral distance."""
    edges = np.linspace(R_MIN, R_MAX, n_bins + 1)
    r_centers = 0.5 * (edges[:-1] + edges[1:])
    w = np.diff(edges)
    return r_centers, w / w.sum()


def exceedance_probability(z, med, sigma=SIGMA):
    """P(PGA > z | median) for a lognormal PGA with natural-log scatter sigma.

    P = 1 - Phi((ln z - ln median)/sigma) = 0.5 erfc((ln z - ln median)/
    (sigma sqrt(2))).
    """
    return 0.5 * (1.0 - erf((np.log(z) - np.log(med)) / (sigma * np.sqrt(2.0))))


def hazard_curve(z_values, b=B_GR, rate_min=RATE_MIN, sigma=SIGMA):
    """Annual exceedance rate of PGA > z, by the total-probability integral."""
    m_centers, rates = magnitude_rates(b=b, rate_min=rate_min)
    r_centers, w_r = distance_weights()
    med = median_pga(m_centers[:, None], r_centers[None, :])
    lam = rates[:, None] * w_r[None, :]
    z = np.atleast_1d(z_values)
    return np.array([float(np.sum(lam * exceedance_probability(zi, med, sigma)))
                     for zi in z])


def interp_amplitude(z_values, lam_values, target_lam):
    """Amplitude at which the hazard curve crosses target_lam, by log-log
    linear interpolation."""
    lo, hi = z_values[0], z_values[-1]
    lz = np.log(z_values)
    llam = np.log(lam_values)
    return float(np.exp(np.interp(np.log(target_lam), llam[::-1], lz[::-1])))


def main():
    section("1. The source model and the median ground motion")
    m_centers, rates = magnitude_rates()
    r_centers, w_r = distance_weights()
    print(f"SYNTHETIC area source: b = {B_GR:.2f}, m from {M_MIN:.1f} to "
          f"{M_MAX:.1f}, rate {RATE_MIN:.3f} events/yr at m >= {M_MIN:.1f}")
    print(f"distance range {R_MIN:.0f}-{R_MAX:.0f} km, {N_R_BINS:d} bins, "
          f"uniform in distance")
    print(f"SYNTHETIC relation: ln PGA(g) = {C0:.3f} + {C1:.2f}(m-6) - "
          f"{C2:.2f} ln(r + {R0_KM:.0f}); sigma = {SIGMA:.2f} (natural log)")
    print(f"\nmagnitude bins: {m_centers.size:d}, total rate check = "
          f"{rates.sum():.5f} events/yr (input {RATE_MIN:.5f})")
    print("\nmedian PGA (g) on a magnitude-distance grid:")
    print("      M      r=10 km   r=30 km   r=100 km")
    for m in (4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5):
        print(f"    {m:4.1f}   {median_pga(m, 10.0):9.4f}   "
              f"{median_pga(m, 30.0):9.4f}   {median_pga(m, 100.0):10.4f}")
    ratio = median_pga(6.5, 10.0) / median_pga(5.5, 10.0)
    print(f"\none magnitude unit multiplies the median by "
          f"{median_pga(6.5, 10.0) / median_pga(5.5, 10.0):.2f} at 10 km")
    print(f"and doubling the distance scales it by "
          f"{median_pga(6.5, 20.0) / median_pga(6.5, 10.0):.3f} at M6.5")
    print(f"the lognormal mean is exp(sigma^2/2) = "
          f"{np.exp(SIGMA ** 2 / 2.0):.4f} times the median, so the MEAN PGA is")
    print(f"{(np.exp(SIGMA ** 2 / 2.0) - 1.0) * 100:.1f} % above the median.")

    section("2. The hazard curve: total probability over (m, r)")
    z_values = np.array([0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4,
                         0.5, 0.7, 1.0])
    lam = hazard_curve(z_values)
    print("      PGA z (g)   annual rate   return period (yr)   "
          "P(exceed in 50 yr)")
    for zi, li in zip(z_values, lam):
        print(f"      {zi:9.3f}   {li:11.5f}   {1.0 / li:18.1f}   "
              f"{1.0 - np.exp(-50.0 * li):18.4f}")
    lam_low = hazard_curve(np.array([PGA_LOW]))[0]
    print(f"\nnumerical check: at z = {PGA_LOW:g} g (far below any median on the")
    print(f"grid) the hazard rate is {lam_low:.5f} per yr, against the source")
    print(f"rate {rates.sum():.5f} per yr.  The integral recovers the total rate")
    print(f"because every event then exceeds the threshold, as it must.")
    print("  The hazard curve is a curve of RATES.  It is not a forecast of an")
    print("  event, and reading it as one is the most common misuse of PSHA.")

    section("3. Return period versus probability, and the design amplitudes")
    for p, t in ((0.10, 50.0), (0.02, 50.0)):
        t_r = -t / np.log(1.0 - p)
        print(f"  P = {p * 100:4.1f} % in {t:.0f} yr  ->  mean return period "
              f"T = -{t:.0f}/ln(1-{p:.2f}) = {t_r:.1f} yr")
    print("  the exact Poisson relation is P = 1 - exp(-t/T); the familiar")
    print("  '1/T' form is the small-p approximation.")
    z_fine = np.geomspace(0.002, 1.5, 120)
    lam_fine = hazard_curve(z_fine)
    for p, t in ((0.10, 50.0), (0.02, 50.0)):
        t_r = -t / np.log(1.0 - p)
        target = 1.0 / t_r
        z_t = interp_amplitude(z_fine, lam_fine, target)
        print(f"  amplitude exceeded at {p * 100:4.1f} % in {t:.0f} yr "
              f"(rate {target:.6f}/yr): {z_t:.4f} g")
    z10 = interp_amplitude(z_fine, lam_fine, 1.0 / (-50.0 / np.log(0.9)))
    z2 = interp_amplitude(z_fine, lam_fine, 1.0 / (-50.0 / np.log(0.98)))
    print(f"\n  the 2%-in-50-yr amplitude is {z2:.4f} g and the 10%-in-50-yr")
    print(f"  amplitude is {z10:.4f} g: a factor "
          f"{z2 / z10:.2f} apart, i.e. the tail of the hazard curve is steep")
    print(f"  in log amplitude over the range codes care about.")

    section("4. Deaggregation: where the hazard at 0.2 g comes from")
    z_target = 0.2
    r_centers, w_r = distance_weights()
    contrib = np.zeros((m_centers.size, r_centers.size))
    for i, m in enumerate(m_centers):
        for j, r in enumerate(r_centers):
            p = exceedance_probability(z_target, median_pga(m, r))
            contrib[i, j] = rates[i] * w_r[j] * p
    total = contrib.sum()
    print(f"rate of PGA > {z_target:.1f} g = {total:.5f} per yr "
          f"(return period {1.0 / total:.0f} yr)")
    m_groups = [(4.5, 5.5), (5.5, 6.0), (6.0, 6.5), (6.5, 7.0), (7.0, 7.6)]
    r_groups = [(5.0, 10.0), (10.0, 20.0), (20.0, 30.0), (30.0, 40.0),
                (40.0, 50.1)]
    print("\npercentage contribution to the hazard (rows magnitude, "
          "columns distance in km)")
    print("      M      5-10   10-20   20-30   30-40   40-50")
    for m_lo, m_hi in m_groups:
        sel_m = (m_centers >= m_lo) & (m_centers < m_hi)
        row = []
        for r_lo, r_hi in r_groups:
            sel_r = (r_centers >= r_lo) & (r_centers < r_hi)
            row.append(100.0 * contrib[np.ix_(sel_m, sel_r)].sum() / total)
        print(f"    {m_lo:.1f}   " + "".join(f"{v:7.1f}" for v in row))
    m_mean = float(np.sum(contrib.sum(axis=1) * m_centers) / total)
    r_mean = float(np.sum(contrib.sum(axis=0) * r_centers) / total)
    i_mode, j_mode = np.unravel_index(np.argmax(contrib), contrib.shape)
    print(f"\nmean magnitude of the contributing events = {m_mean:.2f}")
    print(f"mean distance of the contributing events  = {r_mean:.1f} km")
    print(f"modal bin (largest single contribution)   = M{m_centers[i_mode]:.2f} "
          f"at {r_centers[j_mode]:.1f} km, "
          f"{100.0 * contrib[i_mode, j_mode] / total:.1f} % of the hazard")
    frac_big = float(contrib[m_centers > 6.5, :].sum() / total)
    print(f"fraction of the hazard from m > 6.5       = "
          f"{100.0 * frac_big:.1f} %")
    print("  the mean magnitude is not the largest magnitude, and the modal bin")
    print("  is not the mean: a hazard curve is built from the whole mixture.")

    section("5. Sensitivity: aleatory sigma and epistemic inputs")
    print("  aleatory scatter (the relation's sigma, per event):")
    print("      sigma     rate(0.2 g)   rate(0.4 g)   T(0.4 g) yr")
    for s in (0.30, 0.60, 0.90):
        ll = hazard_curve(np.array([0.2, 0.4]), sigma=s)
        print(f"      {s:5.2f}   {ll[0]:11.5f}   {ll[1]:11.5f}   "
              f"{1.0 / ll[1]:11.0f}")
    l_03 = hazard_curve(np.array([0.3]))[0]
    print(f"\n  rate(0.3 g) at sigma = {SIGMA:.2f} is {l_03:.5f} per yr")
    print("  epistemic: the same integral with different defensible inputs")
    print("      input                        rate(0.3 g)   ratio to reference")
    for label, bb, rr in (("b = 0.90", 0.90, RATE_MIN),
                          ("b = 1.00 (reference)", 1.00, RATE_MIN),
                          ("b = 1.10", 1.10, RATE_MIN),
                          ("a-value halved (rate 0.025)", 1.00, 0.025),
                          ("a-value doubled (rate 0.100)", 1.00, 0.100)):
        val = hazard_curve(np.array([0.3]), b=bb, rate_min=rr)[0]
        print(f"      {label:28s}   {val:11.5f}   {val / l_03:17.2f}")
    print("  a factor of 4 between the extreme branches is produced by inputs")
    print("  that are all defensible.  That spread is epistemic uncertainty, and")
    print("  it is invisible in any single hazard curve.")


if __name__ == "__main__":
    main()
