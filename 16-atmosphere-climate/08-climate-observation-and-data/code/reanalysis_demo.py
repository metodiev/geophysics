#!/usr/bin/env python3
"""Reanalysis caveats: a toy sequential data-assimilation experiment showing that
a reanalysis product is observations plus a model, that in data-sparse periods it
reports the model, and that a change in observing-system density produces a
discontinuity -- and therefore a trend -- that is not in the climate.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python reanalysis_demo.py

Everything is SYNTHETIC.  The "truth", the observations and the assimilating
model are a chosen scalar system with a deliberately large climate bias so the
effect is visible.  No real reanalysis product, model, satellite, observing
system or published value is used, and no real observing-system history is
described.

Contents
--------
1. A synthetic truth, an observation system with changing density, and a model
   with a deliberate climate bias.
2. Sequential assimilation (a scalar Kalman filter) and the analysis error in the
   sparse and dense eras.
3. The model-only limit: what the product reports when there are no observations.
4. The discontinuity at the observing-system change, and the trend it manufactures.
5. The product's own spread versus its actual error.
6. What an honest reanalysis caveat says.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC system (chosen, not measured) --------------------------------
N_YEARS = 60
PHI = 0.70                 # persistence per year, dimensionless
C_TRUE = 0.05              # K per step, forcing term of the truth
C_MODEL = -0.10            # K per step, the assimilating model's (biased) term
Q = 0.05 ** 2              # K^2, process noise variance (model and truth alike)
R_OBS = 0.03 ** 2          # K^2, observation error variance (sd 0.03 K)
SPARSE_PROB = 0.05         # observation availability before the transition
DENSE_PROB = 0.80          # observation availability after the transition
TRANSITION_YEAR = 30       # the observing-system change


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def simulate_truth():
    """Stationary AR(1) anomalies with zero trend (SYNTHETIC)."""
    x = np.empty(N_YEARS)
    x[0] = 0.0
    for t in range(1, N_YEARS):
        x[t] = PHI * x[t - 1] + C_TRUE + np.sqrt(Q) * RNG.standard_normal()
    return x


def observation_mask():
    prob = np.where(np.arange(N_YEARS) < TRANSITION_YEAR, SPARSE_PROB, DENSE_PROB)
    return RNG.random(N_YEARS) < prob


def assimilate(truth, mask, c_model=C_MODEL):
    """Scalar Kalman filter with intermittent observations.

    Returns the analysis, the background (forecast), the background error
    standard deviation at each step, and the mask actually used.
    """
    a = np.empty(N_YEARS)
    bg = np.empty(N_YEARS)
    bsd = np.empty(N_YEARS)
    xb, B = 0.0, 0.25          # first guess and its variance
    for t in range(N_YEARS):
        bg[t] = xb
        bsd[t] = np.sqrt(B)
        if mask[t]:
            y = truth[t] + np.sqrt(R_OBS) * RNG.standard_normal()
            K = B / (B + R_OBS)
            a[t] = xb + K * (y - xb)
            Bpost = (1.0 - K) * B
        else:
            a[t] = xb
            Bpost = B
        xb = PHI * a[t] + c_model
        B = PHI ** 2 * Bpost + Q
    return a, bg, bsd, mask


def trend(x, years=None):
    years = np.arange(x.size) if years is None else years
    A = np.column_stack([np.ones_like(years, dtype=float), years.astype(float)])
    beta, *_ = np.linalg.lstsq(A, x, rcond=None)
    return beta[1]


def main():
    section("1. The synthetic truth and the observing system")
    truth = simulate_truth()
    print(f"  {N_YEARS} years, AR(1) persistence phi = {PHI:.2f}, "
          f"process noise sd {np.sqrt(Q):.2f} K")
    print(f"  truth forcing term {C_TRUE:+.3f} K/step -> model climate mean "
          f"{C_TRUE / (1 - PHI):+.3f} K")
    print(f"  assimilating model uses {C_MODEL:+.3f} K/step -> its climate mean "
          f"is {C_MODEL / (1 - PHI):+.3f} K")
    print(f"  (the difference of {abs((C_TRUE - C_MODEL) / (1 - PHI)):.3f} K is")
    print("  deliberately large so the mechanism is visible)")
    print(f"  observation error sd {np.sqrt(R_OBS):.2f} K; availability is")
    print(f"  {SPARSE_PROB:.2f} before year {TRANSITION_YEAR} and "
          f"{DENSE_PROB:.2f} after it")
    print(f"  the truth has NO trend: fitted {trend(truth):+.4f} K/yr, mean "
          f"{truth.mean():+.3f} K, std {truth.std():.3f} K")

    section("2. Assimilation and the analysis error by era")
    mask = observation_mask()
    a, bg, bsd, _ = assimilate(truth, mask)
    n_early = int(mask[:TRANSITION_YEAR].sum())
    n_late = int(mask[TRANSITION_YEAR:].sum())
    err = a - truth
    print(f"  observations ingested: {n_early} before year "
          f"{TRANSITION_YEAR}, {n_late} after it")
    print("  era      rms error    mean error   fitted trend (K/yr)")
    for name, sl in (("sparse", slice(0, TRANSITION_YEAR)),
                     ("dense", slice(TRANSITION_YEAR, N_YEARS))):
        print(f"  {name:8s} {np.sqrt(np.mean(err[sl] ** 2)):7.3f} K   "
              f"{np.mean(err[sl]):+.3f} K   {trend(a[sl]):+.4f}")
    print(f"  truth trend {trend(truth):+.4f} K/yr; analysis trend over the "
          f"whole record {trend(a):+.4f} K/yr")

    section("3. The model-only limit")
    a0, bg0, bsd0, _ = assimilate(truth, np.zeros(N_YEARS, dtype=bool))
    print("  with observation availability set to 0 the product is the model")
    print("  run alone (a free-running simulation):")
    print(f"    rms difference from truth      = "
          f"{np.sqrt(np.mean((a0 - truth) ** 2)):.3f} K")
    print(f"    mean difference (climate bias) = {np.mean(a0 - truth):+.3f} K")
    print(f"    std of the product             = {a0.std():.3f} K")
    print(f"    std of the truth               = {truth.std():.3f} K")
    print(f"    model-only fitted trend        = {trend(a0):+.4f} K/yr")
    print("  The free-running model has the right variability and no trend, but")
    print("  the wrong mean level.  In a data-sparse period the product inherits")
    print("  that level and still looks like a perfectly plausible climate record.")

    section("4. The discontinuity at the observing-system change")
    bias_early = np.mean(err[:TRANSITION_YEAR])
    bias_late = np.mean(err[TRANSITION_YEAR:])
    artefact = trend(a) - trend(truth)
    print(f"  mean analysis-bias before the change : {bias_early:+.3f} K")
    print(f"  mean analysis-bias after the change  : {bias_late:+.3f} K")
    print(f"  change in bias at the transition     : "
          f"{bias_late - bias_early:+.3f} K")
    print(f"  fitted trend of the analysis         : {trend(a):+.4f} K/yr")
    print(f"  fitted trend of the truth            : {trend(truth):+.4f} K/yr")
    print(f"  trend artefact                       : {artefact:+.4f} K/yr")
    print("  The sparse-era product sits at the model's climate; the dense-era")
    print("  product sits at the observed one.  A trend fitted across the")
    print("  transition inherits the difference -- a property of the observing")
    print("  system, not of the atmosphere.  A purely level-shaped artefact")
    print("  appears as a trend because a trend model has no other way to fit it.")

    section("5. The product's own spread versus its actual error")
    print("  era      mean background sd   actual rms error   ratio")
    for name, sl in (("sparse", slice(0, TRANSITION_YEAR)),
                     ("dense", slice(TRANSITION_YEAR, N_YEARS))):
        sd = np.mean(bsd[sl])
        rmse = np.sqrt(np.mean(err[sl] ** 2))
        print(f"  {name:8s} {sd:18.3f}   {rmse:16.3f}   {sd / rmse:7.3f}")
    print("  The filter's error estimate covers the model's internal uncertainty")
    print("  but not the model's climate bias, so in the sparse era it is")
    print("  confident while being wrong by half a kelvin.  A product's internal")
    print("  spread is not an error estimate against reality unless the model's")
    print("  own climate bias is included -- in an operational reanalysis it")
    print("  usually is not.")

    section("6. What an honest reanalysis caveat says")
    print("  A reanalysis is a model simulation constrained by observations.")
    print("  1. It is physically consistent and complete in space and time --")
    print("     which is why it is used, and why its completeness in data-sparse")
    print("     regions is a model statement, not an observation.")
    print("  2. It is not homogenised for climate trends: a change in the")
    print("     observing system is a change in the product, as measured above.")
    print("  3. Its uncertainty is not its ensemble spread alone; the spread")
    print("     does not contain the model's climate bias.")
    print("  4. Trends from a reanalysis are most credible where the observing")
    print("     system was stable and dense; elsewhere they are hypotheses, and")
    print("     they should be compared with independent products.")
    print("  All numbers above are SYNTHETIC and the biases are chosen.")


if __name__ == "__main__":
    main()
