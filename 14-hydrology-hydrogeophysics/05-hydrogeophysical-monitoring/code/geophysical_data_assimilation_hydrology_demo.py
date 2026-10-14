#!/usr/bin/env python3
"""Assimilating geophysical data into a hydrological model: an ensemble Kalman
filter updating a two-layer soil-moisture model with ERT-derived water-content
observations, and what the filter does when the petrophysical observation
operator is wrong.

Run with the project virtual environment:

    cd 14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geophysical_data_assimilation_hydrology_demo.py

Everything here is SYNTHETIC: the soil, the rainfall series, the petrophysical
parameters, the observation error and the bias are chosen teaching values.  No
real catchment, station or data set is used, and no weather record is quoted.

Contents
--------
1. The observation operator: Archie inversion, and the bias produced by a wrong
   cementation exponent.
2. The forecast model: a two-layer soil-moisture bucket forced by synthetic rain.
3. The truth run and the open-loop (no assimilation) forecast error.
4. Ensemble Kalman filter: analysis error, innovation statistics, spread.
5. The effect of observation frequency.
6. A biased petrophysical operator: the filter follows the bias and becomes
   over-confident.
7. A biased rainfall forcing: assimilation cannot repair a biased model.
"""

import numpy as np
from scipy.special import erfinv

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC soil, petrophysical and survey parameters (chosen) -------------
PHI = 0.40          # porosity
THETA_R = 0.05      # residual water content
D1, D2 = 0.20, 0.60   # layer thicknesses, m
KS = 0.30           # saturated conductivity of the surface layer, m/d
BETA = 6.0          # Brooks-Corey-type exponent of the conductivity curve
KC = 0.85           # crop coefficient for layer 1
ET2_FRAC = 0.30     # fraction of PET taken from layer 2
M_TRUE = 1.80       # true Archie cementation exponent
N_ARCHIE = 2.00     # Archie saturation exponent
M_ASSUMED = 1.60    # cementation exponent assumed by the analyst (the error)
SIGMA_OBS = 0.010   # m^3/m^3, 1 sd of the ERT-derived water content
OBS_INTERVAL = 2    # days between geophysical surveys
N_MEMBERS = 200
N_DAYS = 150
FORCING_SIGMA = 0.25   # multiplicative sd of the ensemble rainfall


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def archie_saturation(rho_ratio, phi, m, n=N_ARCHIE):
    """S from rho/rho_w = phi^-m S^-n."""
    return (rho_ratio * phi ** m) ** (-1.0 / n)


def petrophysical_bias(theta, phi=PHI, m_true=M_TRUE, m_assumed=M_ASSUMED):
    """Water-content error from inverting Archie with the wrong exponent.

    The true relation is  rho/rho_w = phi^-m_true S^-n  with S = theta/phi.
    The analyst inverts with m_assumed, obtaining
        S_obs = S * phi^{(m_true - m_assumed)/n},
    so the bias is proportional to theta and multiplicative, not additive.
    """
    s = theta / phi
    s_obs = s * phi ** ((m_true - m_assumed) / N_ARCHIE)
    return s_obs * phi - theta


def rain_series(n_days, rng):
    """Synthetic daily rainfall, mm/d: a storm process with a seasonal weight."""
    wet = rng.random(n_days) < 0.28
    depth = rng.exponential(9.0, n_days)
    seasonal = 1.0 + 0.35 * np.sin(2.0 * np.pi * np.arange(n_days) / 365.0)
    return np.where(wet, depth * seasonal, 0.0)


def pet_series(n_days, rng):
    """Synthetic daily potential evapotranspiration, mm/d."""
    seasonal = 2.6 + 1.4 * np.sin(2.0 * np.pi * np.arange(n_days) / 365.0 + 1.0)
    return np.maximum(seasonal + 0.25 * rng.standard_normal(n_days), 0.2)


def conductivity(theta):
    """Unsaturated conductivity factor, m/d."""
    se = np.clip((theta - THETA_R) / (PHI - THETA_R), 0.0, 1.0)
    return KS * se ** BETA


def advance(theta, p_mm, pet_mm, ks_mult=1.0, et_mult=1.0):
    """One daily step of the two-layer bucket.  theta in m^3/m^3, fluxes mm/d.

    Water contents are updated in metres of water and converted back:
        d(D1 theta1)/dt = P - ET1 - q12
        d(D2 theta2)/dt = q12 - ET2 - q_out
    """
    t1, t2 = float(theta[0]), float(theta[1])
    k1 = conductivity(t1) * ks_mult
    q12 = k1 * 1000.0                                   # mm/d
    te1 = KC * pet_mm * (t1 / PHI)
    te2 = ET2_FRAC * pet_mm * (t2 / PHI)
    av1 = max((t1 - THETA_R) * D1 * 1000.0, 0.0)
    av2 = max((t2 - THETA_R) * D2 * 1000.0, 0.0)
    te1 = min(te1, av1)
    te1 = min(te1, av1)
    q12 = min(q12, av1)
    te2 = min(te2, av2)
    q_out = min(conductivity(t2) * ks_mult * 1000.0, av2)
    n1 = (t1 * D1 * 1000.0 + p_mm - te1 - q12) / (D1 * 1000.0)
    n2 = (t2 * D2 * 1000.0 + q12 - te2 - q_out) / (D2 * 1000.0)
    return np.array([min(max(n1, THETA_R), PHI), min(max(n2, THETA_R), PHI)])


def run_model(theta0, p, pet, ks_mult=1.0, et_mult=1.0):
    """Deterministic run; returns the state trajectory, shape (n_days+1, 2)."""
    out = np.zeros((len(p) + 1, 2))
    out[0] = theta0
    for k in range(len(p)):
        out[k + 1] = advance(out[k], p[k], pet[k] * et_mult, ks_mult)
    return out


def enkf(p_true, pet_true, theta_true, biased, sigma_obs, interval,
         ks_mult_truth=1.0, rain_bias=1.0, seed=1, collect=False):
    """Ensemble Kalman filter of the bucket model with theta1 observations.

    The observation is the petrophysical operator applied to the true state:
    y = theta1_true + bias(theta1_true) + noise, with the bias switched on by
    ``biased``.  The filter is told the correct noise sd; it is not told about
    the bias, which is exactly the situation being demonstrated.
    """
    rng = np.random.default_rng(seed)
    n = len(p_true)
    ens = np.zeros((N_MEMBERS, 2))
    ens[:, 0] = theta_true[0, 0] + 0.01 * rng.standard_normal(N_MEMBERS)
    ens[:, 1] = theta_true[0, 1] + 0.01 * rng.standard_normal(N_MEMBERS)
    ks_m = np.exp(0.30 * rng.standard_normal(N_MEMBERS))
    rain_m = np.exp(FORCING_SIGMA * rng.standard_normal((N_MEMBERS, n)))
    anal = np.zeros((n + 1, 2))
    spread = np.zeros(n + 1)
    innov, chi2 = [], []
    for k in range(n + 1):
        anal[k] = ens.mean(axis=0)
        spread[k] = ens[:, 0].std(ddof=1)
        if k == n:
            break
        for i in range(N_MEMBERS):
            ens[i] = advance(ens[i], p_true[k] * rain_bias * rain_m[i, k],
                             pet_true[k], ks_m[i])
        if k % interval == interval - 1:
            th = theta_true[k + 1, 0]
            y = th + (petrophysical_bias(th) if biased else 0.0) \
                + sigma_obs * rng.standard_normal()
            hx = ens[:, 0]
            pf = hx.var(ddof=1)
            cov = np.cov(ens.T)                       # (2, 2)
            kk = cov[:, 0] / (pf + sigma_obs ** 2)
            innov.append(y - hx.mean())
            chi2.append((y - hx.mean()) ** 2 / (pf + sigma_obs ** 2))
            for i in range(N_MEMBERS):
                ens[i] += kk * (y + sigma_obs * rng.standard_normal() - hx[i])
            ens[:, 0] = np.clip(ens[:, 0], THETA_R, PHI)
            ens[:, 1] = np.clip(ens[:, 1], THETA_R, PHI)
    if collect:
        return anal, spread, np.array(innov), np.array(chi2)
    return anal


def main():
    section("1. The observation operator and the bias in it")
    print(f"SYNTHETIC petrophysics: phi = {PHI:.2f}, true m = {M_TRUE:.2f}, "
          f"assumed m = {M_ASSUMED:.2f}, n = {N_ARCHIE:.2f}")
    print("  true relation: rho/rho_w = phi^-m S^-n with S = theta/phi")
    print("  inverting with m_assumed gives S_obs = S phi^{(m_true-m_assumed)/n}")
    factor = PHI ** ((M_TRUE - M_ASSUMED) / N_ARCHIE)
    print(f"  phi^((m_true-m_assumed)/n) = {PHI:.2f}**"
          f"{((M_TRUE - M_ASSUMED) / N_ARCHIE):.2f} = {factor:.4f}")
    print("   state theta1 (m^3/m^3)   S      inferred S   bias (m^3/m^3)   bias (%)")
    for theta in (0.08, 0.14, 0.24, 0.32):
        b = petrophysical_bias(theta)
        print(f"   {theta:22.3f}   {theta / PHI:5.3f}   {theta / PHI * factor:11.4f}"
              f"   {b:15.4f}   {100 * b / theta:8.2f}")
    print("  the bias is MULTIPLICATIVE: "
          f"{100 * (factor - 1):+.2f}% of the true water content at every state,")
    print(f"  i.e. between {abs(petrophysical_bias(0.08)):.4f} and "
          f"{abs(petrophysical_bias(0.32)):.4f} m^3/m^3 across the modelled range.")
    b_lo, b_hi = abs(petrophysical_bias(0.08)), abs(petrophysical_bias(0.32))
    print(f"  that is {b_lo / SIGMA_OBS:.1f} to {b_hi / SIGMA_OBS:.1f} x the "
          f"measurement noise sd of {SIGMA_OBS:.3f} m^3/m^3.")
    print("  -> an ERT water content is produced by a PETROPHYSICAL OPERATOR: a")
    print("     plausible error in one of its exponents gives a SYSTEMATIC error")
    print("     of order the measurement noise when the soil is dry and nearly")
    print("     three times it when the soil is wet.  A constant-error model for")
    print("     this observation would be wrong by construction.")

    section("2. The forecast model and the synthetic truth")
    p = rain_series(N_DAYS, RNG)
    pet = pet_series(N_DAYS, RNG)
    theta0 = np.array([0.22, 0.26])
    truth = run_model(theta0, p, pet)
    print(f"  two-layer bucket: D1 = {D1:.2f} m, D2 = {D2:.2f} m, "
          f"Ks = {KS:.2f} m/d, beta = {BETA:.0f}")
    print(f"  synthetic rainfall: {N_DAYS} days, total = {p.sum():.1f} mm, "
          f"max daily = {p.max():.1f} mm/d, wet days = {int((p > 0).sum())}")
    print(f"  synthetic PET: total = {pet.sum():.1f} mm, mean = "
          f"{pet.mean():.2f} mm/d")
    print(f"  truth theta1: min {truth[:, 0].min():.3f}, max "
          f"{truth[:, 0].max():.3f}, mean {truth[:, 0].mean():.3f} m^3/m^3")
    print(f"  truth theta2: min {truth[:, 1].min():.3f}, max "
          f"{truth[:, 1].max():.3f}, mean {truth[:, 1].mean():.3f} m^3/m^3")
    print("  (these are model states, not measurements of any soil)")

    section("3. Open loop: forecasting without any geophysics")
    open_loop = run_model(theta0, p * 1.02, pet, ks_mult=1.35)
    for name, i in (("theta1", 0), ("theta2", 1)):
        rmse = np.sqrt(np.mean((open_loop[:, i] - truth[:, i]) ** 2))
        print(f"  open-loop RMSE of {name} = {rmse:.5f} m^3/m^3 "
              f"({100 * rmse / truth[:, i].mean():.1f}% of the mean state)")
    print("  the open loop drifts because its two parameters are wrong by a")
    print("  stated amount (Ks high by 35%, rainfall high by 2%): assimilation")
    print("  with observations is the only way to notice.")

    section("4. Ensemble Kalman filter with unbiased observations")
    anal, spread, innov, chi2 = enkf(p, pet, truth, False, SIGMA_OBS,
                                     OBS_INTERVAL, seed=7, collect=True)
    for name, i in (("theta1", 0), ("theta2", 1)):
        rmse = np.sqrt(np.mean((anal[:, i] - truth[:, i]) ** 2))
        print(f"  analysis RMSE of {name} = {rmse:.5f} m^3/m^3")
    r1_open = np.sqrt(np.mean((open_loop[:, 0] - truth[:, 0]) ** 2))
    r1_an = np.sqrt(np.mean((anal[:, 0] - truth[:, 0]) ** 2))
    print(f"  improvement in theta1: {r1_open / r1_an:.2f}x")
    r2_open = np.sqrt(np.mean((open_loop[:, 1] - truth[:, 1]) ** 2))
    r2_an = np.sqrt(np.mean((anal[:, 1] - truth[:, 1]) ** 2))
    print(f"  improvement in theta2: {r2_open / r2_an:.2f}x, by cross-covariance")
    print(f"  observations assimilated: {len(innov)} (every "
          f"{OBS_INTERVAL} days)")
    print(f"  innovation mean = {innov.mean():+.5f} m^3/m^3 "
          f"(bias test), sd = {innov.std(ddof=1):.5f}")
    print(f"  mean normalised innovation squared = {chi2.mean():.3f} "
          f"(1.0 is consistent)")
    ratio = float(np.sqrt(np.mean(spread[1:] ** 2))
                  / np.sqrt(np.mean((anal - truth) ** 2)))
    print(f"  ensemble spread / actual rms error (theta1) = {ratio:.3f}")
    print("  -> the filter propagates information from the measured layer into")
    print("     the unmeasured one through the cross-covariance of the ensemble.")

    section("5. How often must the geophysics be repeated?")
    print("   interval (d)   events   analysis RMSE theta1   RMSE theta2")
    for interval in (1, 2, 5, 10, 25):
        a = enkf(p, pet, truth, False, SIGMA_OBS, interval, seed=7)
        print(f"   {interval:11d}   {len(range(0, N_DAYS, interval)):7d}   "
              f"{np.sqrt(np.mean((a[:, 0] - truth[:, 0]) ** 2)):19.5f}   "
              f"{np.sqrt(np.mean((a[:, 1] - truth[:, 1]) ** 2)):11.5f}")
    print("  -> RMSE improves steeply at first and then flattens: the marginal")
    print("     value of a survey falls fast, so the survey interval is an")
    print("     economic decision informed by this curve, not a technical one.")

    section("6. A biased observation operator (m assumed 1.60 instead of 1.80)")
    a_biased, spread_b, innov_b, chi2_b = enkf(p, pet, truth, True, SIGMA_OBS,
                                               OBS_INTERVAL, seed=7, collect=True)
    r1_b = np.sqrt(np.mean((a_biased[:, 0] - truth[:, 0]) ** 2))
    print(f"  injected observation bias is {100 * (factor - 1):+.2f}% of the")
    print(f"  true water content: {petrophysical_bias(0.14):+.4f} m^3/m^3 at the")
    print("  mean state, growing with the state")
    print(f"  analysis RMSE of theta1 with the bias = {r1_b:.5f} "
          f"(unbiased case {r1_an:.5f}, open loop {r1_open:.5f})")
    r2_b = np.sqrt(np.mean((a_biased[:, 1] - truth[:, 1]) ** 2))
    print(f"  analysis RMSE of theta2 with the bias = {r2_b:.5f} "
          f"(unbiased case {r2_an:.5f})")
    print(f"  mean state error (theta1) = "
          f"{(a_biased[:, 0] - truth[:, 0]).mean():+.5f} m^3/m^3, "
          f"i.e. the filter has been dragged to the bias")
    print(f"  innovation mean = {innov_b.mean():+.5f} m^3/m^3 "
          f"(unbiased {innov.mean():+.5f})")
    print(f"  mean normalised innovation squared = {chi2_b.mean():.3f} "
          f"(unbiased {chi2.mean():.3f}; 1.0 is consistent)")
    ratio_b = float(np.sqrt(np.mean(spread_b[1:] ** 2))
                    / np.sqrt(np.mean((a_biased - truth) ** 2)))
    print(f"  ensemble spread / actual rms error (theta1) = {ratio_b:.3f} "
          f"(unbiased {ratio:.3f})")
    print("  -> the filter does exactly what it is designed to do and produces a")
    print("     worse state with a confident error bar.  Assimilation transfers")
    print("     the bias from the observation into the model and hides it in the")
    print("     spread.  The innovation mean is the diagnostic that exposes it,")
    print("     and it is available only if the observations are checked against")
    print("     an independent measurement.")

    section("7. A biased forcing: what assimilation hides and what it does not")
    print("  5-day forecasts launched from every analysis:")
    a_unb = enkf(p, pet, truth, False, SIGMA_OBS, OBS_INTERVAL, seed=7)
    a_low = enkf(p, pet, truth, False, SIGMA_OBS, OBS_INTERVAL,
                 rain_bias=0.85, seed=7)
    print("   forcing bias   analysis RMSE theta1 (d 0)   1-day forecast   5-day forecast")
    for label, a, rb in (("none", a_unb, 1.0), ("rainfall 15% low", a_low, 0.85)):
        row = [np.sqrt(np.mean((a[:, 0] - truth[:, 0]) ** 2))]
        for horizon in (1, 5):
            errs = []
            for k in range(0, N_DAYS - horizon):
                f = a[k].copy()
                for h in range(horizon):
                    f = advance(f, p[k + h] * rb, pet[k + h])
                errs.append(f[0] - truth[k + horizon, 0])
            row.append(np.sqrt(np.mean(np.array(errs) ** 2)))
        print(f"   {label:14s}   {row[0]:24.5f}   {row[1]:12.5f}   {row[2]:14.5f}")
    print("   (all in m^3/m^3)")
    print("  -> the analysis barely notices the 15% rainfall bias: it re-anchors")
    print("     the state to the observation every two days.  The bias reappears")
    print("     in the FORECAST, where the model must run on its own.  Analysis")
    print("     skill is not forecast skill, and only the forecast is used.")
    print("  -> data assimilation corrects the STATE, not the process.  Reporting")
    print("     an analysis error without a forecast error hides structural")
    print("     error, which is a modelling problem and not a filtering one.")


if __name__ == "__main__":
    main()
