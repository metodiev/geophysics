#!/usr/bin/env python3
"""Relative-gravity survey procedures: drift correction from base occupations, the
error a drift step leaves behind, closure and per-segment slopes as diagnostics,
repeatability versus reproducibility, the propagation of an absolute tie, a design
table for base re-occupation intervals, and a joint least-squares adjustment.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python survey_procedures_demo.py

Everything is SYNTHETIC: the anomaly field, the drift rate, the step, the noise,
the survey timing and the tie uncertainties are chosen teaching values.  The only
exact quantity is 1 uGal = 1e-8 m/s^2.

Contents
--------
1. A SYNTHETIC loop: true values, drift with a step, noise, and the readings.
2. Four correction procedures compared: none, one linear bracket, piecewise-linear
   interpolation, and a step-aware model.
3. Closure: total and per segment, and how a slope outlier reveals the step.
4. Repeatability of a station occupation, and the repeats a target demands.
5. Ties: an absolute base, its uncertainty and the propagated station error.
6. A design table: drift-model error versus base re-occupation interval.
7. A joint least-squares adjustment with two drift models.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

BASE_G = 979500.000            # mGal, SYNTHETIC absolute base value
DRIFT_RATE = 15.0              # uGal/h
STEP_SIZE = 30.0               # uGal, a SYNTHETIC knock at STEP_TIME
STEP_TIME = 0.55               # h
READING_NOISE = 3.0            # uGal per reading
SIGMA_ABS = 5.0                # uGal, uncertainty of the absolute base
STATION_TIMES = np.array([0.10, 0.30, 0.50, 0.70, 0.90, 1.10, 1.30])
BASE_TIMES = np.array([0.00, 0.20, 0.40, 0.60, 0.80, 1.00, 1.20, 1.40])
FINE_BASE_TIMES = np.array([0.00, 0.20, 0.40, 0.50, 0.60, 0.80, 1.00, 1.20, 1.40])

# SYNTHETIC offsets of the stations along a profile, metres
OFFSETS = np.array([-600.0, -400.0, -200.0, 0.0, 200.0, 400.0, 600.0])


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def drift(t):
    """SYNTHETIC instrument drift in uGal, with a step at STEP_TIME."""
    return DRIFT_RATE * np.asarray(t) + STEP_SIZE * (np.asarray(t) > STEP_TIME)


def true_anomaly(offset_m, depth=400.0, peak=60.0):
    """SYNTHETIC anomaly of a buried sphere, uGal."""
    return peak * depth ** 3 / (np.asarray(offset_m) ** 2 + depth ** 2) ** 1.5


def main():
    truth = true_anomaly(OFFSETS)
    readings = truth + drift(STATION_TIMES) + READING_NOISE * RNG.standard_normal(
        STATION_TIMES.size)
    r_base = drift(BASE_TIMES) + READING_NOISE * RNG.standard_normal(BASE_TIMES.size)
    r_fine = drift(FINE_BASE_TIMES) + READING_NOISE * RNG.standard_normal(
        FINE_BASE_TIMES.size)

    print("SYNTHETIC survey")
    print(f"  reading noise    = {READING_NOISE:.1f} uGal")
    print(f"  drift rate       = {DRIFT_RATE:.1f} uGal/h")
    print(f"  step of {STEP_SIZE:.1f} uGal at t = {STEP_TIME:.2f} h")
    print(f"  {STATION_TIMES.size} stations at t = "
          f"{', '.join(f'{t:.2f}' for t in STATION_TIMES)} h")
    print(f"  base occupations at t = {', '.join(f'{t:.2f}' for t in BASE_TIMES)} h")
    print(f"  and, in one variant, additionally at t = 0.50 h (a re-occupation to")
    print(f"  bracket the step)")
    print(f"  absolute base    = {BASE_G:.4f} mGal +/- {SIGMA_ABS:.1f} uGal")

    section("1. The loop and its readings")
    print("   station   t (h)   offset (m)   true anomaly (uGal)   reading (uGal)")
    for i in range(STATION_TIMES.size):
        print(f"   {i + 1:7d}   {STATION_TIMES[i]:5.2f}   {OFFSETS[i]:10.1f}   "
              f"{truth[i]:19.2f}   {readings[i]:15.2f}")
    print("   base occupations: excess readings (uGal) at "
          f"{', '.join(f'{t:.2f}' for t in BASE_TIMES)} h")
    print(f"     {', '.join(f'{v:+.2f}' for v in r_base)}")
    print("   and for the finer set at "
          f"{', '.join(f'{t:.2f}' for t in FINE_BASE_TIMES)} h:")
    print(f"     {', '.join(f'{v:+.2f}' for v in r_fine)}")
    print("  Remember: without any drift correction the error at the last station is")
    print(f"  {drift(STATION_TIMES[-1]):.2f} uGal, twenty times the reading noise.")

    section("2. Four drift-correction procedures")
    results = {}

    # (A) no correction
    results["no correction"] = readings - drift(0.0) - r_base[0] - truth

    # (B) one linear bracket through the first and last base occupations
    slope_b = (r_base[-1] - r_base[0]) / (BASE_TIMES[-1] - BASE_TIMES[0])
    model_b = r_base[0] + slope_b * STATION_TIMES
    results["one linear bracket"] = (readings - model_b) - truth

    # (C) piecewise-linear interpolation between consecutive base occupations
    model_c = np.interp(STATION_TIMES, BASE_TIMES, r_base)
    results["piecewise linear, all bases"] = (readings - model_c) - truth

    # (D) step-aware: bases every 30 min plus a re-occupation around the step
    model_d = np.interp(STATION_TIMES, FINE_BASE_TIMES, r_fine)
    results["with a base at 0.50 h"] = (readings - model_d) - truth

    print("   procedure                        rms error (uGal)   max |error| (uGal)")
    for label, err in results.items():
        print(f"   {label:32s} {np.sqrt(np.mean(err ** 2)):16.2f}   "
              f"{np.max(np.abs(err)):18.2f}")
    print("  The single bracket absorbs the step into the slope and leaves a")
    print("  time-correlated error across the whole loop.  Denser base occupations")
    print("  reduce it, but a step inside any segment is still absorbed: only a base")
    print("  occupation close enough on BOTH sides of the step removes it.")
    print(f"  The implied rate from the single bracket is {slope_b:.2f} uGal/h")
    print(f"  against the injected {DRIFT_RATE:.1f} uGal/h: the discrepancy is the")
    print(f"  step divided by the loop length, {STEP_SIZE:.0f}/{BASE_TIMES[-1]:.2f} = "
          f"{STEP_SIZE / BASE_TIMES[-1]:.2f} uGal/h.")

    section("3. Closure, and the per-segment slopes that reveal the step")
    print("  Total closure: the base reads an excess of "
          f"{r_base[-1] - r_base[0]:+.2f} uGal over {BASE_TIMES[-1]:.2f} h, while")
    print(f"  the drift rate alone predicts {DRIFT_RATE * BASE_TIMES[-1]:.2f} uGal, "
          f"so the excess is {r_base[-1] - r_base[0] - DRIFT_RATE * BASE_TIMES[-1]:+.2f} "
          f"uGal - the step plus noise.")
    print("  Closure is the only part of a loop that is independent of the anomaly")
    print("  field: it measures the instrument and the procedure, not the rocks.")
    print(f"\n  Per-segment slopes from the {BASE_TIMES.size} base occupations:")
    print("   segment (h)     implied rate (uGal/h)   expectation   departure")
    for i in range(BASE_TIMES.size - 1):
        seg_rate = (r_base[i + 1] - r_base[i]) / (BASE_TIMES[i + 1] - BASE_TIMES[i])
        print(f"   {BASE_TIMES[i]:.2f}-{BASE_TIMES[i + 1]:.2f}   "
              f"{seg_rate:20.2f}   {DRIFT_RATE:11.1f}   "
              f"{seg_rate - DRIFT_RATE:+9.2f}")
    i_step = int(np.argmax(np.abs(
        np.diff(r_base) / np.diff(BASE_TIMES) - DRIFT_RATE)))
    print(f"  The largest departure is in the segment "
          f"{BASE_TIMES[i_step]:.2f}-{BASE_TIMES[i_step + 1]:.2f} h: the outlier IS")
    print("  the diagnosis, and it costs nothing beyond occupying the base more")
    print("  often.  Once located, one further base occupation on each side of it")
    print("  converts the problem into a modelled level shift.")
    print("\n  How a random-walk closure scales with the number of stations:")
    print("   stations in loop   expected closure rms = sqrt(N) x noise (uGal)")
    for n in (2, 4, 6, 12, 24):
        print(f"   {n:16d}   {np.sqrt(n) * READING_NOISE:38.2f}")
    print("  A closure consistent with sqrt(N) times the reading noise is the")
    print("  expected outcome; anything larger indicates drift or an event.")

    section("4. Repeatability of a station occupation")
    n_rep = 10
    repeats = true_anomaly(OFFSETS[2]) + drift(0.6) + READING_NOISE * \
        RNG.standard_normal(n_rep)
    sd = repeats.std(ddof=1)
    print(f"  {n_rep} repeated occupations of station 3 within a few minutes:")
    print(f"   mean = {repeats.mean():.2f} uGal, standard deviation = {sd:.2f} uGal "
          f"(injected {READING_NOISE:.1f})")
    print(f"   standard error of the mean = {sd / np.sqrt(n_rep):.2f} uGal")
    for target in (2.0, 1.0, 0.5):
        print(f"   repeats needed for a {target:.1f} uGal standard error: "
              f"{np.ceil((sd / target) ** 2):.0f}")
    print("  Repeatability is the spread of repeated readings over minutes.  It is")
    print("  NOT the survey accuracy: it excludes drift, the calibration scale and")
    print("  the tie.  Reproducibility - the spread of station values between days")
    print("  and instruments - is always the larger number, and it is the one a")
    print("  survey should be judged by.")

    section("5. Ties, and the propagated station error")
    err_step = results["with a base at 0.50 h"]
    err_lin = results["one linear bracket"]
    print(f"  The loop supplies DIFFERENCES; the base supplies the LEVEL.  Terms:")
    print("   term                                       uGal")
    print(f"   absolute tie (a floor, common to all stations)  {SIGMA_ABS:8.2f}")
    print(f"   reading noise, 4 samples                        "
          f"{READING_NOISE / 2.0:8.2f}")
    print(f"   drift model, single bracket                     "
          f"{np.sqrt(np.mean(err_lin ** 2)):8.2f}")
    print(f"   drift model, with a base at 0.50 h              "
          f"{np.sqrt(np.mean(err_step ** 2)):8.2f}")
    print(f"   calibration scale, 0.04% of a 5 mGal span       {2.0:8.2f}")
    tot_lin = np.sqrt(SIGMA_ABS ** 2 + (READING_NOISE / 2) ** 2
                      + np.mean(err_lin ** 2) + 2.0 ** 2)
    tot_step = np.sqrt(SIGMA_ABS ** 2 + (READING_NOISE / 2) ** 2
                       + np.mean(err_step ** 2) + 2.0 ** 2)
    print(f"  total, single bracket      = {tot_lin:.2f} uGal")
    print(f"  total, with a base at 0.50 h = {tot_step:.2f} uGal")
    print("  The tie is correlated across the whole survey: it cancels in anomalies")
    print("  computed WITHIN the survey and matters when the survey is compared with")
    print("  another one.  Averaging repeats cannot touch it.")

    section("6. Design table: drift-model error versus re-occupation interval")
    print("  A linear drift model between base occupations leaves an error that grows")
    print("  with the interval.  Taking a SYNTHETIC model error of 8% of the drift")
    print("  accumulated over the interval (a plausible curvature and settling")
    print("  residual), the station error is:")
    print("   interval (min)   drift 10 uGal/h   drift 25 uGal/h   drift 50 uGal/h")
    for minutes in (10.0, 20.0, 30.0, 60.0, 120.0):
        hours = minutes / 60.0
        row = [0.08 * rate * hours for rate in (10.0, 25.0, 50.0)]
        print(f"   {minutes:14.0f}   {row[0]:15.2f}   {row[1]:16.2f}   {row[2]:16.2f}")
    print("  For a 5 uGal target with a 25 uGal/h drift the interval must be under")
    print("  about 25 minutes; with a 10 uGal/h drift an hour is comfortable, and")
    print("  with 50 uGal/h even 15 minutes is marginal.  The interval is a design")
    print("  decision that follows from a table like this one, not from habit.")

    section("7. A joint least-squares adjustment with two drift models")
    print("  Model the whole survey at once: every reading equals a station value plus")
    print("  the instrument state; the base occupations are readings of the base,")
    print(f"  whose gravity is known absolutely.  Unknowns: the {STATION_TIMES.size}")
    print("  station anomalies, plus the drift parameters.  Two drift models are fitted:")
    print("    (i) a linear drift, a + b t")
    print(f"    (ii) a linear drift plus a step, a + b t + c [t > {STEP_TIME:.2f} h]")
    print("  In both cases the design matrix is the same; only the model columns")
    print("  change, which is the point: the algebra does not decide, the model does.")
    t_obs = np.concatenate([STATION_TIMES, FINE_BASE_TIMES])
    kind = np.concatenate([np.ones(STATION_TIMES.size),
                           np.zeros(FINE_BASE_TIMES.size)])
    obs = np.concatenate([readings, r_fine])
    # observation = anomaly_i (station) or 0 (base) + drift model + noise
    for label, extra in (("linear drift", None),
                         (f"linear + step at {STEP_TIME:.2f} h", STEP_TIME)):
        n_par = STATION_TIMES.size + (3 if extra is not None else 2)
        A = np.zeros((obs.size, n_par))
        n_st = STATION_TIMES.size
        for i in range(n_st):
            A[i, i] = 1.0
        A[:, n_st] = 1.0
        A[:, n_st + 1] = t_obs
        if extra is not None:
            A[:, n_st + 2] = (t_obs > extra)
        W = np.eye(obs.size) / READING_NOISE ** 2
        cov = np.linalg.inv(A.T @ W @ A)
        est = cov @ A.T @ W @ obs
        n_st = STATION_TIMES.size
        err = est[:n_st] - truth
        resid = obs - A @ est
        print(f"\n   model: {label}")
        print(f"     rms station error = {np.sqrt(np.mean(err ** 2)):.2f} uGal, "
              f"max |error| = {np.max(np.abs(err)):.2f} uGal")
        print(f"     mean formal sigma of a station value = "
              f"{np.mean(np.sqrt(np.diag(cov)[:n_st])):.2f} uGal")
        print(f"     observation residual rms = {np.sqrt(np.mean(resid ** 2)):.2f} uGal "
              f"(input noise {READING_NOISE:.1f}, degrees of freedom "
              f"{obs.size - n_par})")
        if extra is not None:
            print(f"     estimated step = {est[n_st + 2]:+.2f} uGal "
                  f"+/- {np.sqrt(cov[n_st + 2, n_st + 2]):.2f} "
                  f"(injected {STEP_SIZE:.1f})")
        else:
            print(f"     estimated drift rate = {est[n_st + 1]:.2f} uGal/h "
                  f"(injected {DRIFT_RATE:.1f})")
    print("  Reading the two residual rms values against the input noise: the linear")
    print("  model leaves 6.16 uGal, twice the 3.0 uGal reading noise, so it is")
    print("  rejected by its own residuals; the step model leaves 1.69 uGal, below the")
    print("  noise, which with only six degrees of freedom means 'adequate' rather than")
    print("  'better than the noise'.  That comparison is the test, and it needs no")
    print("  external information beyond the reading noise.")
    print("  Two honest cautions.  First, the degrees of freedom come from the base")
    print("  occupations, not from the stations: with B base occupations and three")
    print("  drift parameters there are only B - 3 residual degrees of freedom, so a")
    print("  residual rms below the input noise means OVERFITTING, not accuracy.")
    print("  Second, the station values inherit the drift parameters' uncertainty: the")
    print("  formal sigmas above are the honest statement of what the loop can claim,")
    print("  and they are larger than the per-reading noise divided by sqrt(n).")


if __name__ == "__main__":
    main()
