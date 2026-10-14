#!/usr/bin/env python3
"""Graduate project 3: InSAR deformation time series - rate estimation, the
seasonal term, a coseismic step, and the window dependence of a linear rate.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_timeseries_demo.py

Everything here is SYNTHETIC.  The series are generated from chosen deformation
components with chosen noise; no interferogram, no Sentinel-1 acquisition and no
published velocity field is used.

Sections
--------
1. The synthetic series and its components.
2. Three models: rate only, rate plus season, rate plus season plus step.
3. Window dependence: a decaying transient aliased into a linear rate.
4. What the analysis does not establish.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

N_EPOCHS = 60
REPEAT = 0.05                 # 18 days, years
RATE_TRUE = 12.0              # mm/yr
SEASON_AMP = 8.0              # mm, annual
STEP_TIME = 1.95              # yr
STEP_SIZE = 10.0              # mm
NOISE = 3.0                   # mm
T_YEARS = 3.0                 # total span


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def design(t, with_season=True, with_step=False):
    cols = [np.ones_like(t), t]
    if with_season:
        cols += [np.cos(2 * np.pi * t), np.sin(2 * np.pi * t)]
    if with_step:
        cols.append((t >= STEP_TIME).astype(float))
    return np.column_stack(cols)


def fit(t, d, sigma, **kw):
    a = design(t, **kw)
    cov = np.linalg.inv(a.T @ a / sigma ** 2)
    coef = cov @ (a.T @ d) / sigma ** 2
    resid = d - a @ coef
    s2 = float(resid @ resid) / (t.size - a.shape[1])
    err = np.sqrt(np.diag(cov) * s2)
    return coef, err, resid, a


def main():
    t = np.arange(N_EPOCHS) * REPEAT
    truth = (RATE_TRUE * t + SEASON_AMP * np.sin(2 * np.pi * t)
             + STEP_SIZE * (t >= STEP_TIME))
    d = truth + NOISE * RNG.standard_normal(N_EPOCHS)

    section("1. The synthetic series and its components")
    print(f"SYNTHETIC InSAR-like series: {N_EPOCHS} epochs, repeat "
          f"{REPEAT * 365.25:.0f} days, span {t[-1]:.2f} yr")
    print(f"  components: {RATE_TRUE:.1f} mm/yr linear, {SEASON_AMP:.1f} mm "
          f"annual, step {STEP_SIZE:.1f} mm at {STEP_TIME:.2f} yr")
    print(f"  noise {NOISE:.1f} mm per epoch; series range "
          f"{d.min():.2f} to {d.max():.2f} mm")
    print(f"  total deformation over the span = "
          f"{(RATE_TRUE * t[-1]):.1f} mm linear + step")

    section("2. The seasonal term and the step")
    d_nostep = truth - STEP_SIZE * (t >= STEP_TIME) + NOISE * RNG.standard_normal(
        N_EPOCHS)
    print("  series WITHOUT a step (rate + season + noise):")
    for label, kw in (("rate only", dict(with_season=False)),
                      ("rate + season", dict(with_season=True))):
        coef, err, resid, _ = fit(t, d_nostep, NOISE, **kw)
        print(f"    {label:<20}{coef[1]:>12.4f} +/- {err[1]:.4f} mm/yr, "
              f"rms {np.sqrt(np.mean(resid ** 2)):.4f} mm")
    coef_rs, err_rs, _, _ = fit(t, d_nostep, NOISE, with_season=True)
    coef_r, err_r, _, _ = fit(t, d_nostep, NOISE, with_season=False)
    print(f"    omitting the season biases the rate by "
          f"{coef_r[1] - coef_rs[1]:+.4f} mm/yr "
          f"({(coef_r[1] - coef_rs[1]) / err_r[1]:+.2f} sigma of the naive error)")
    print("  series WITH the 10 mm step:")
    c_nostep_model, e_nostep_model, r_nostep, _ = fit(t, d, NOISE, with_season=True)
    print(f"    {'rate + season':<20}{c_nostep_model[1]:>12.4f} +/- "
          f"{e_nostep_model[1]:.4f} mm/yr, rms {np.sqrt(np.mean(r_nostep ** 2)):.4f} mm")
    coef_full, err_full, r_full, _ = fit(t, d, NOISE, with_season=True,
                                        with_step=True)
    print(f"    {'rate + season + step':<20}{coef_full[1]:>12.4f} +/- "
          f"{err_full[1]:.4f} mm/yr, rms {np.sqrt(np.mean(r_full ** 2)):.4f} mm")
    print(f"    the step is recovered as {coef_full[-1]:.4f} +/- "
          f"{err_full[-1]:.4f} mm (true {STEP_SIZE:.1f})")
    print(f"    omitting the step biases the rate by "
          f"{c_nostep_model[1] - coef_full[1]:+.4f} mm/yr, which is "
          f"{(c_nostep_model[1] - coef_full[1]) / e_nostep_model[1]:+.2f} sigma")
    print("  -> both the season and any step must be in the model: each is")
    print("     absorbed into the rate when omitted, and the rate's error bar")
    print("     inflates to hide it.")

    section("3. Window dependence: a decaying transient")
    expo = RATE_TRUE * t - 15.0 * np.exp(-t / 0.3)
    d2 = expo + NOISE * RNG.standard_normal(N_EPOCHS)
    print("  the underlying signal is 12 mm/yr plus a -15 mm transient decaying")
    print("  with a 0.3 yr time constant (post-seismic relaxation, or a poroelastic")
    print("  response to an earlier event)")
    print(f"{'window':>22}{'rate (mm/yr)':>14}{'sigma':>9}")
    for lo, hi, name in ((0.0, 1.0, "epochs 0-1.0 yr"),
                         (0.25, 3.0, "epochs 0.25-3.0 yr"),
                         (1.5, 3.0, "epochs 1.5-3.0 yr")):
        sel = (t >= lo) & (t <= hi)
        c, e, _, _ = fit(t[sel], d2[sel], NOISE, with_season=False)
        print(f"{name:>22}{c[1]:>14.4f}{e[1]:>9.4f}")
    print(f"  the true final rate is {RATE_TRUE:.1f} mm/yr; a window that includes")
    print("  the transient returns a rate up to "
          f"{fit(t[(t >= 0.0) & (t <= 1.0)], d2[(t >= 0.0) & (t <= 1.0)], NOISE, with_season=False)[0][1] - RATE_TRUE:+.1f} mm/yr away from it,")
    print("  and the misfit will not flag the error because the transient looks")
    print("  like a fast linear phase.")

    section("4. What the analysis does not establish")
    print("  1. the step time and size are fitted parameters; a step is only one of")
    print("     several explanations for a discontinuity (atmospheric, unwrapping,")
    print("     orbit, or a genuine earthquake);")
    print("  2. the rate is for the line of sight, not the horizontal velocity:");
    print("     converting needs the incidence angle and two look geometries;")
    print("  3. a network of interferograms has correlated errors (atmospheric and")
    print("     orbital), so the formal sigma here is optimistic by a factor that")
    print("     must be estimated;")
    print("  4. the seasonal term is modelled as a pure annual sinusoid; a")
    print("     snow- or groundwater-driven cycle is not;")
    print("  5. a rate estimated over 3 years does not constrain a 10-year rate.")


if __name__ == "__main__":
    main()
