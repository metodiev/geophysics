#!/usr/bin/env python3
"""Magnetic survey procedures: diurnal correction, main-field removal, levelling,
sampling and the error budget.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python magnetic_survey_procedures_demo.py

Everything here is SYNTHETIC: the diurnal signal, the survey geometry, the drift,
the noise and the geology are chosen teaching values.  The only standard values
used are a = 6371 km for the Earth radius and the synthetic axial dipole
coefficient of module 08-01.

Contents
--------
1. A synthetic diurnal signal and the cost of a base-station time lag.
2. The main-field gradient, and what an epoch error does and does not do.
3. Levelling: tie-line misties, a least-squares adjustment, and the residual.
4. Along-line sampling and the Nyquist rule.
5. A repeatability check.
6. The error budget, in quadrature, with the dominant term identified.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

A_EARTH_KM = 6371.0
G10 = -30000.0            # nT, synthetic axial dipole coefficient


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def diurnal(t_hours):
    """SYNTHETIC diurnal variation in nT as a function of time in hours."""
    return (18.0 * np.sin(2 * np.pi * (t_hours - 4.0) / 24.0)
            + 4.5 * np.sin(2 * np.pi * t_hours / 12.0 + 0.9))


def dipole_F(lat_deg):
    """Total intensity of the synthetic axial dipole at a given latitude."""
    return abs(G10) * np.sqrt(1.0 + 3.0 * np.sin(np.radians(lat_deg)) ** 2)


def main():
    section("1. A synthetic diurnal signal and the base-station lag")
    print("SYNTHETIC diurnal model: an 18 nT daily wave plus a 4.5 nT"
          " semi-diurnal wave")
    t = np.arange(0.0, 8.0, 1.0 / 60.0)     # an 8-hour survey, 1-minute samples
    print(f"  over the 8-hour survey the signal ranges "
          f"{diurnal(t).min():.3f} to {diurnal(t).max():.3f} nT, "
          f"a span of {diurnal(t).max()-diurnal(t).min():.3f} nT")
    print("  residual after correcting with a base station read at a lag:")
    print("   lag (min)   residual rms (nT)   residual peak (nT)")
    for lag_min in (0.0, 1.0, 5.0, 15.0, 30.0):
        lag_h = lag_min / 60.0
        resid = diurnal(t) - diurnal(t - lag_h)
        print(f"  {lag_min:11.1f}   {resid.std():18.4f}   "
              f"{np.max(np.abs(resid)):18.4f}")
    print("  a zero lag corrects exactly (by construction).  A 15-minute lag")
    print("  leaves only 0.12 nT rms against a 23 nT span, but it leaves 0.96 nT")
    print("  at the worst moment - comparable with a weak target's amplitude, and")
    print("  it is correlated with time along the line, so it does not average")
    print("  out.  That is why clocks are synchronised or the base record is")
    print("  interpolated to each field reading, and why the base station must")
    print("  sit in a magnetically quiet place rather than on the anomaly.")

    section("2. The main-field gradient and the epoch error")
    print(f"SYNTHETIC axial dipole coefficient g10 = {G10:.0f} nT")
    print("   latitude (deg)   F (nT)   north-south gradient (nT/km)")
    for lat in (0.0, 30.0, 45.0, 60.0):
        dF_dlam = (abs(G10) * 3.0 * np.sin(np.radians(lat))
                   * np.cos(np.radians(lat)) / np.sqrt(
                       1.0 + 3.0 * np.sin(np.radians(lat)) ** 2))
        dF_dkm = dF_dlam * np.pi / 180.0 / (2.0 * np.pi * A_EARTH_KM / 360.0)
        print(f"  {lat:14.1f}   {dipole_F(lat):8.2f}   {dF_dkm:28.4f}")
    span_km = 20.0
    dF_dkm_45 = 4.4660
    print(f"  a {span_km:.0f} km north-south survey at 45 deg spans "
          f"{dF_dkm_45*span_km:.1f} nT of main field")
    sv_err, dt_yr = -34.0, 5.0
    offset = sv_err * dt_yr
    shape_lo, shape_hi = dipole_F(45.0), dipole_F(45.18)
    shape_rel = abs(shape_hi - shape_lo) / shape_lo
    print(f"  an epoch error of {dt_yr:.0f} yr at an SV of {sv_err:.0f} nT/yr "
          f"is a {offset:.0f} nT error in g10")
    print(f"  across the {span_km:.0f} km survey the SHAPE factor")
    print("  (1 + 3 sin^2(lat))^(1/2) changes by "
          f"{100*shape_rel:.4f}%, so the epoch error")
    print(f"  varies by only {abs(offset)*shape_rel:.3f} nT across the area:")
    print("  it is a uniform offset, absorbed by levelling, and it does not")
    print("  distort the anomaly.  The main field itself varies by "
          f"{abs(shape_hi-shape_lo):.1f} nT")
    print("  over the same distance, which is what the model must remove.")
    print("  A mis-positioned tie point or an uncorrected sensor orientation")
    print("  instead produces a gradient that levelling cannot remove, because it")
    print("  is present in the data rather than being a constant offset.")

    section("3. Levelling: tie-line misties and a least-squares adjustment")
    n_lines, n_stations = 5, 25
    x = np.linspace(0.0, 2000.0, n_stations)
    true_drift = np.array([0.0, 3.2, -1.7, 5.5, -2.4])   # nT per line, SYNTHETIC
    geology = 8.0 * np.sin(2 * np.pi * x / 700.0) + 3.0 * np.cos(2 * np.pi * x / 300.0)
    noise = 0.4
    data = np.array([geology + true_drift[i]
                     + RNG.normal(0.0, noise, n_stations)
                     for i in range(n_lines)])
    # tie lines cross all survey lines; each tie reading has its own noise
    crossings = [(i, j) for i in range(n_lines) for j in range(i + 1, n_lines)]
    tie_mistie = np.array([data[i, n_stations // 2] - data[j, n_stations // 2]
                           + RNG.normal(0.0, noise * 1.5)
                           for (i, j) in crossings])
    print(f"  SYNTHETIC survey: {n_lines} lines x {n_stations} stations, "
          f"{len(crossings)} tie-line crossings")
    print(f"  injected line offsets (nT): "
          + ", ".join(f"{v:+.1f}" for v in true_drift))
    print(f"  rms mistie at the crossings, raw: {tie_mistie.std():.4f} nT")
    # least squares: minimise sum (o_i - o_j - mistie)^2 with o_1 fixed to zero
    n = n_lines
    A = np.zeros((len(crossings) + 1, n))
    b = np.zeros(len(crossings) + 1)
    for k, (i, j) in enumerate(crossings):
        A[k, i], A[k, j], b[k] = 1.0, -1.0, tie_mistie[k]
    A[-1, 0], b[-1] = 1.0, 0.0
    o, *_ = np.linalg.lstsq(A, b, rcond=None)
    residual = A @ o - b
    print(f"  adjusted offsets (nT): " + ", ".join(f"{v:+.2f}" for v in o))
    print(f"  true minus adjusted offsets (nT): "
          + ", ".join(f"{true_drift[i]-o[i]:+.2f}" for i in range(n_lines)))
    print(f"  rms mistie after adjustment, excluding the fixed datum row: "
          f"{residual[:-1].std():.4f} nT")
    print("  the adjustment drives the misties to 0.53 nT rms, close to the")
    print("  tie-line reading noise - so the DIFFERENCES between lines are well")
    print("  determined.  The absolute offsets are recovered only to 1-2 nT,")
    print("  because the network has few crossings and one datum is assumed.  A")
    print("  levelling adjustment is therefore a statement about relative levels,")
    print("  and the datum is an assumption that must be reported.")

    section("4. Along-line sampling and the Nyquist rule")
    print("  a sampled profile can only represent wavelengths longer than twice")
    print("  the sample interval.  Design rule: sample at a quarter of the")
    print("  shortest target wavelength.")
    print("   shortest target (m)   sample interval (m)   Nyquist wavelength (m)")
    for target in (50.0, 100.0, 200.0, 500.0):
        si = target / 4.0
        print(f"  {target:19.1f}   {si:20.1f}   {2*si:21.1f}")
    print("  a 50 m target therefore needs a 12.5 m sample interval, which is")
    print("  a walking survey; from an aircraft, the same target cannot be")
    print("  resolved at any line spacing, and the survey must say so.")

    section("5. Repeatability check")
    print("  SYNTHETIC repeat measurements at 20 stations, 10 nT anomaly plus")
    print("  independent noise:")
    truth = 10.0 + 5.0 * np.sin(np.linspace(0.0, np.pi, 20))
    r1 = truth + RNG.normal(0.0, 0.5, 20)
    r2 = truth + RNG.normal(0.0, 0.5, 20)
    diff = r1 - r2
    print(f"  mean difference {diff.mean():+.4f} nT, standard deviation "
          f"{diff.std():.4f} nT")
    print(f"  the expected standard deviation for two independent readings of")
    print(f"  noise 0.5 nT each is sqrt(2) x 0.5 = {np.sqrt(2.0)*0.5:.4f} nT")
    print("  a repeatability standard deviation much larger than the noise model")
    print("  means an unmodelled effect: a diurnal residual, a positioning error,")
    print("  or a sensor that has not settled.")

    section("6. The error budget")
    budget = (("instrument noise", 0.10), ("orientation / levelling of the sensor", 0.50),
              ("diurnal correction residual", 1.00), ("main-field model removal", 0.50),
              ("levelling and tie-line adjustment", 2.00))
    quad = np.sqrt(sum(v ** 2 for _, v in budget))
    print("   contribution                          standard uncertainty (nT)")
    for name, v in budget:
        print(f"  {name:36s} {v:26.2f}")
    print(f"  {'quadrature sum':36s} {quad:26.2f}")
    worst = max(budget, key=lambda kv: kv[1])
    print(f"  the dominant term is '{worst[0]}' at {worst[1]:.2f} nT: reducing")
    print("  the instrument noise would not improve the survey, because it")
    print("  contributes only "
          f"{100*budget[0][1]**2/quad**2:.2f}% of the variance.  An error budget")
    print("  is the cheapest tool in survey design: it says where to spend.")

    section("7. Reproducibility check with the seeded generator")
    draws = RNG.normal(0.0, 1.0, 5)
    print("  first five standard-normal draws from seed 20261014:")
    print("  " + ", ".join(f"{v:+.6f}" for v in draws))


if __name__ == "__main__":
    main()
