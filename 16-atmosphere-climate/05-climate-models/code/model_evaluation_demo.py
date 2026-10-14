#!/usr/bin/env python3
"""Model evaluation: bias, root-mean-square error, correlation, the centered
RMS difference and a skill score, measured on synthetic fields; and a
demonstration of the double penalty that makes a realistic but misplaced model
score worse than a featureless one.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python model_evaluation_demo.py

All models and data in this file are SYNTHETIC.  The "observations" are a
generated field, not a measurement, and no published score is quoted.

Contents
--------
1. A synthetic observation field and four synthetic models.
2. Bias, RMSE, correlation, standard-deviation ratio, centered RMS difference,
   and a skill score against a climatological reference.
3. The Taylor decomposition CRMSD^2 = s_m^2 + s_o^2 - 2 s_m s_o r, checked.
4. The double penalty: displacing a feature versus deleting it.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_TIME = 72          # 5-day samples through one year
N_SPACE = 30         # synthetic stations
NOISE_K = 0.5        # observational noise, K
SEASONAL_AMPLITUDE_K = 8.0
BASE_TEMPERATURE_K = 285.15
SHIFT_SAMPLES = 6    # 30-day displacement for the "misplaced" model


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def metrics(model, truth, reference):
    """Return a dict of the standard verification metrics, all in kelvin."""
    m = model.ravel()
    o = truth.ravel()
    r = reference.ravel()
    bias = float(np.mean(m - o))
    rmse = float(np.sqrt(np.mean((m - o) ** 2)))
    rmse_ref = float(np.sqrt(np.mean((r - o) ** 2)))
    skill = 1.0 - rmse ** 2 / rmse_ref ** 2
    m_anom = m - m.mean()
    o_anom = o - o.mean()
    sigma_m = float(np.std(m_anom))
    sigma_o = float(np.std(o_anom))
    corr = float(np.corrcoef(m_anom, o_anom)[0, 1])
    crmsd = float(np.sqrt(np.mean((m_anom - o_anom) ** 2)))
    return dict(bias=bias, rmse=rmse, rmse_ref=rmse_ref, skill=skill,
                sigma_m=sigma_m, sigma_o=sigma_o, corr=corr, crmsd=crmsd)


def main():
    section("1. Synthetic observations and models")
    phase = 2.0 * np.pi * np.arange(N_TIME) / N_TIME
    seasonal = np.sin(phase)                                  # dimensionless
    spatial = 1.0 + 0.30 * np.sin(2.0 * np.pi * np.arange(N_SPACE) / N_SPACE)
    truth = (BASE_TEMPERATURE_K + SEASONAL_AMPLITUDE_K
             * seasonal[:, None] * spatial[None, :]
             + NOISE_K * RNG.standard_normal((N_TIME, N_SPACE)))
    reference = np.repeat(truth.mean(axis=0)[None, :], N_TIME, axis=0)

    good = truth - NOISE_K * RNG.standard_normal((N_TIME, N_SPACE))
    biased = good + 1.5
    misplaced = np.roll(good, SHIFT_SAMPLES, axis=0)
    smoothed = reference + 0.30 * SEASONAL_AMPLITUDE_K * seasonal[:, None] * spatial[None, :]

    print(f"  grid: {N_TIME} time samples x {N_SPACE} locations")
    print(f"  truth: mean {truth.mean():.3f} K, std {truth.std():.3f} K")
    print(f"  reference for skill: the observed climatology (time mean at each")
    print(f"  location), RMSE against truth = "
          f"{np.sqrt(np.mean((reference - truth) ** 2)):.3f} K")

    section("2. Verification metrics (all in kelvin unless noted)")
    header = (f"  {'model':<12s} {'bias':>7s} {'RMSE':>7s} {'r':>7s} "
              f"{'std ratio':>10s} {'CRMSD':>7s} {'skill':>7s}")
    print(header)
    results = {}
    for name, model in (("good", good), ("biased", biased),
                        ("misplaced", misplaced), ("smoothed", smoothed)):
        met = metrics(model, truth, reference)
        results[name] = met
        print(f"  {name:<12s} {met['bias']:7.3f} {met['rmse']:7.3f} "
              f"{met['corr']:7.4f} {met['sigma_m'] / met['sigma_o']:10.4f} "
              f"{met['crmsd']:7.3f} {met['skill']:7.3f}")
    print("  Definitions: bias = mean(model - truth); RMSE = rms(model - truth);")
    print("  r = Pearson correlation of anomalies; std ratio = sigma_model/sigma_truth;")
    print("  CRMSD = rms of anomaly differences; skill = 1 - RMSE^2/RMSE_reference^2.")
    print("  The biased model has the same r and CRMSD as the good one: correlation")
    print("  and CRMSD are blind to a constant offset, RMSE is not.  Separating bias")
    print("  from pattern error is exactly what the centered statistic is for.")

    section("3. The Taylor decomposition, checked numerically")
    for name in ("good", "misplaced", "smoothed"):
        met = results[name]
        direct = met["crmsd"] ** 2
        taylor = (met["sigma_m"] ** 2 + met["sigma_o"] ** 2
                  - 2.0 * met["sigma_m"] * met["sigma_o"] * met["corr"])
        print(f"  {name:<11s} CRMSD^2 = {direct:10.5f}   "
              f"sigma_m^2 + sigma_o^2 - 2 sigma_m sigma_o r = {taylor:10.5f}   "
              f"difference = {abs(direct - taylor):.2e} K^2")
    print("  The identity is exact for population moments and holds to round-off")
    print("  here, so a point on a Taylor diagram is three numbers rewritten, not")
    print("  a new measurement.")

    section("4. The double penalty")
    print(f"  misplaced = the good model shifted by {SHIFT_SAMPLES} samples "
          f"({SHIFT_SAMPLES * 5} days)")
    print("  smoothed  = climatology plus 30% of the seasonal amplitude")
    print(f"  {'model':<12s} {'RMSE (K)':>9s} {'skill':>7s} {'seasonal amplitude (K)':>24s}")
    for name, model in (("good", good), ("misplaced", misplaced), ("smoothed", smoothed)):
        # measure the seasonal amplitude as the time-mean of the spatial rms of anomalies
        anom = model - model.mean(axis=0)[None, :]
        amp = float(np.mean(np.sqrt(np.mean(anom ** 2, axis=0))))
        print(f"  {name:<12s} {results[name]['rmse']:9.3f} "
              f"{results[name]['skill']:7.3f} {amp:24.3f}")
    print("  The misplaced model carries the full seasonal signal and the smoothed")
    print("  model carries almost none, yet the smoothed model scores better on both")
    print("  RMSE and skill. A misplaced feature is penalised twice: it is counted")
    print("  as a miss where it should be and as a false alarm where it is not.")
    print("  RMSE therefore rewards smoothing. This is the double penalty, and it")
    print("  is a property of the score, not of the models.")

    section("5. Correlations at zero lag, and at the best lag")
    truth_ts = truth.mean(axis=1)
    for name, model in (("good", good), ("misplaced", misplaced), ("smoothed", smoothed)):
        ts = model.mean(axis=1)
        r_zero = float(np.corrcoef(ts, truth_ts)[0, 1])
        best_lag = 0
        best_r = -2.0
        for lag in range(-12, 13):
            r_lag = float(np.corrcoef(np.roll(ts, lag), truth_ts)[0, 1])
            if r_lag > best_r:
                best_r, best_lag = r_lag, lag
        print(f"  {name:<12s} r(lag 0) = {r_zero:.4f}   "
              f"r(lag {best_lag - N_TIME if abs(best_lag) > N_TIME // 2 else best_lag:+d}) "
              f"= {best_r:.4f}")
    print("  A timing error is partly recoverable by shifting in time; a pattern")
    print("  error is not. Reporting only the zero-lag correlation conflates them.")

    section("6. Effective sample size and a significance threshold")
    phi = 0.8
    n_red = 200
    red_noise = np.zeros(n_red)
    for i in range(1, n_red):
        red_noise[i] = phi * red_noise[i - 1] + RNG.standard_normal()
    lag1 = float(np.corrcoef(red_noise[:-1], red_noise[1:])[0, 1])
    n_eff = n_red * (1.0 - lag1) / (1.0 + lag1)
    print(f"  a synthetic red-noise series of length {n_red} with AR(1) "
          f"coefficient {phi:.1f}")
    print(f"  measured lag-1 autocorrelation = {lag1:.4f}")
    print(f"  effective sample size N_eff = N(1-r1)/(1+r1) = {n_eff:.2f}")
    print(f"  95% critical correlation using N_eff     = "
          f"{1.96 / np.sqrt(n_eff):.4f}")
    print(f"  95% critical correlation if N were used  = "
          f"{1.96 / np.sqrt(n_red):.4f}")
    print(f"  ratio = {(1.96 / np.sqrt(n_eff)) / (1.96 / np.sqrt(n_red)):.3f}")
    print("  Serial correlation inflates the apparent information content. Ignoring")
    print("  it makes a correlation look far more significant than it is. The same")
    print("  correction applies to any score computed on a series with memory.")


if __name__ == "__main__":
    main()
