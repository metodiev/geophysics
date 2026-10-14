#!/usr/bin/env python3
"""Tidal harmonic analysis on a SYNTHETIC tide.

Run with the project virtual environment:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tidal_harmonics_demo.py

All models and data are SYNTHETIC: a chosen set of tidal constituents with chosen
amplitudes and phases.  The constituent speeds are the conventional tidal
constants of the standard harmonic convention, used here as model inputs.  No
real tide gauge, port or prediction is used.

Contents
--------
1. The constituent set and the Rayleigh separation criterion.
2. Least-squares harmonic analysis with known frequencies.
3. The Rayleigh criterion measured: fit error versus record length.
4. Aliasing by sampling interval, measured.
5. Prediction error versus record length.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# Conventional constituent angular speeds, degrees per hour.  These are the
# standard values of the tidal harmonic convention, quoted here as model inputs.
SPEEDS = {
    "M2": 28.9841042,
    "S2": 30.0000000,
    "N2": 28.4397295,
    "K1": 15.0410686,
    "O1": 13.9430356,
}
# SYNTHETIC amplitudes (m) and phases (radians), chosen for teaching.
TRUTH = {
    "M2": (1.20, 0.40),
    "S2": (0.35, 1.10),
    "N2": (0.25, 2.30),
    "K1": (0.20, 4.00),
    "O1": (0.15, 5.10),
}
NOISE = 0.03              # m, Gaussian, SYNTHETIC


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def basis(t_hours, names, mean=True):
    cols = [np.ones_like(t_hours)] if mean else []
    for n in names:
        w = np.deg2rad(SPEEDS[n])
        cols += [np.cos(w * t_hours), np.sin(w * t_hours)]
    return np.column_stack(cols)


def synth(t_hours, names, rng=None):
    y = np.zeros_like(t_hours)
    for n in names:
        a, ph = TRUTH[n]
        w = np.deg2rad(SPEEDS[n])
        y += a * np.cos(w * t_hours - ph)
    if rng is not None:
        y = y + NOISE * rng.standard_normal(t_hours.size)
    return y


def fit(t_hours, y, names, mean=True):
    G = basis(t_hours, names, mean)
    coef, *_ = np.linalg.lstsq(G, y, rcond=None)
    amp, ph = {}, {}
    off = 1 if mean else 0
    for i, n in enumerate(names):
        a, b = coef[off + 2 * i], coef[off + 2 * i + 1]
        amp[n] = float(np.hypot(a, b))
        ph[n] = float(np.arctan2(b, a))
    resid = y - G @ coef
    return amp, ph, resid


def alias(f_deg_per_h, fs_deg_per_h):
    """Fold a frequency into the Nyquist band of a sampling rate."""
    f = f_deg_per_h
    while f > fs_deg_per_h / 2:
        f = abs(f - fs_deg_per_h)
    return f


def main():
    names = list(SPEEDS)

    section("1. The constituent set, and the Rayleigh criterion")
    print("  constituent  speed (deg/h)   period (h)   amplitude (m)   phase (rad)")
    for n in names:
        a, ph = TRUTH[n]
        print(f"  {n:11s}  {SPEEDS[n]:13.7f}   {360.0/SPEEDS[n]:10.4f}   "
              f"{a:13.3f}   {ph:12.3f}")
    print("\n  Rayleigh criterion: two constituents are separable only if the")
    print("  record is at least T = 360/|speed difference| hours long.")
    print("   pair      |df| (deg/h)   T (h)      T (days)")
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            df = abs(SPEEDS[names[i]] - SPEEDS[names[j]])
            print(f"  {names[i]}-{names[j]:8s} {df:11.7f}   {360.0/df:8.3f}   "
                  f"{360.0/df/24.0:8.3f}")

    # -------------------------------------------------- exact analysis -------
    section("2. Harmonic analysis on a 30-day hourly record")
    dt_h = 1.0
    t30 = np.arange(0.0, 30.0 * 24.0, dt_h)
    y30 = synth(t30, names)
    amp, ph, resid = fit(t30, y30, names)
    print("  constituent   amplitude (m)   phase (rad)   error (m)")
    for n in names:
        a_true, ph_true = TRUTH[n]
        print(f"  {n:11s}   {amp[n]:13.6f}   {ph[n]:11.6f}   "
              f"{amp[n]-a_true:+.2e}")
    print(f"  residual rms = {resid.std():.3e} m")
    print("  with known frequencies and no noise the fit is exact to double")
    print("  precision: harmonic analysis is a linear least-squares problem, and")
    print("  the only hard parts are which frequencies to include and how long")
    print("  the record is.")

    # ------------------------------------------------ Rayleigh measured ------
    section("3. The Rayleigh criterion measured (noisy, 20 realisations)")
    print("  fit M2 and N2 only (separation 27.555 days); input noise "
          f"sigma = {NOISE:.2f} m")
    print("   length(d)   std of M2 error   std of N2 error   cond(G)")
    for days in (2.0, 5.0, 10.0, 27.55, 40.0, 60.0):
        tt = np.arange(0.0, days * 24.0, dt_h)
        e_m2, e_n2 = [], []
        for _ in range(20):
            yy = synth(tt, ("M2", "N2"), RNG)
            G = basis(tt, ("M2", "N2"))
            coef, *_ = np.linalg.lstsq(G, yy, rcond=None)
            e_m2.append(np.hypot(coef[1], coef[2]) - TRUTH["M2"][0])
            e_n2.append(np.hypot(coef[3], coef[4]) - TRUTH["N2"][0])
        print(f"  {days:9.2f}   {np.std(e_m2):16.5f}   {np.std(e_n2):16.5f}   "
              f"{np.linalg.cond(G):9.2e}")
    print("  the M2-N2 separation time is 27.555 days.  Below it the two columns")
    print("  of the design matrix are nearly parallel and the matrix is")
    print("  ill-conditioned: the same 0.03 m of noise produces an amplitude")
    print("  error of 0.056 m at 2 days against 0.0010 m at 60 days, a factor of")
    print("  58, and the condition number moves with it.  The noise-free fit of")
    print("  section 2 hid this: the Rayleigh criterion is a statement about")
    print("  conditioning, and noise is what makes conditioning matter.")

    # --------------------------------------------------------- aliasing ------
    section("4. Aliasing by sampling interval, measured")
    print("   interval     fs (deg/h)   M2 alias   S2 alias   N2 alias   "
          "K1 alias   O1 alias")
    for label, hours in (("1 h", 1.0), ("3 h", 3.0), ("6 h", 6.0),
                         ("12 h", 12.0), ("24 h", 24.0)):
        fs = 360.0 / hours
        al = {n: alias(SPEEDS[n], fs) for n in names}
        print(f"  {label:8s}   {fs:10.2f}   " +
              "".join(f"{al[n]:10.5f}" for n in names))
    print("  all values in degrees per hour, folded into the Nyquist band.")
    print("  at 24 h sampling, S2 (30.0000 deg/h) folds to 0.0000: it is")
    print("  indistinguishable from the mean level, and M2 and N2 fold to")
    print("  1.01590 and 1.56027 deg/h, i.e. periods of 14.77 and 9.59 days.")
    print("  the 14.77-day alias of M2 IS the M2-S2 beat period.")


    print("\n  consequence for a fit: include M2 and S2 in a model of DAILY data")
    tt = np.arange(0.0, 60.0 * 24.0, 24.0)
    yy = synth(tt, names)
    G = basis(tt, names)
    coef, *_ = np.linalg.lstsq(G, yy, rcond=None)
    amp_d, _, _ = fit(tt, yy, names)
    print(f"  condition number of the full daily design matrix = "
          f"{np.linalg.cond(G):.3e}")
    print("  constituent   amplitude from daily data (m)   truth (m)")
    for n in names:
        print(f"  {n:11s}   {amp_d[n]:28.4f}   {TRUTH[n][0]:9.3f}")
    print("  M2 and S2 are not recoverable from daily samples: their columns are")
    print("  nearly parallel (a constant is almost an S2 at this sampling).  The")
    print("  fit returns arbitrary splits between them, and between S2 and the")
    print("  mean.  This is why tidal analysis uses hourly data.")

    # -------------------------------------------------------- prediction -----
    section("5. Prediction error versus record length")
    print("  the model contains all five constituents in every case; fit on the")
    print(f"  record, then predict the following 30 days (hourly, "
          f"noise sigma = {NOISE:.2f} m)")
    for days in (7.0, 14.77, 30.0, 60.0):
        t_all = np.arange(0.0, 120.0 * 24.0, dt_h)
        y_all = synth(t_all, names, RNG)
        n_fit = int(round(days * 24.0))
        amp_f, _, resid_f = fit(t_all[:n_fit], y_all[:n_fit], names)
        Gf = basis(t_all[:n_fit], names)
        coef_f, *_ = np.linalg.lstsq(Gf, y_all[:n_fit], rcond=None)
        pred = basis(t_all[n_fit:n_fit + int(30.0 * 24.0)], names) @ coef_f
        y_true = synth(t_all[n_fit:n_fit + int(30.0 * 24.0)], names)
        rms = float(np.sqrt(np.mean((pred - y_true) ** 2)))
        m2_err = amp_f["M2"] - TRUTH["M2"][0]
        n2_err = amp_f["N2"] - TRUTH["N2"][0]
        print(f"  record {days:5.2f} d: fit residual rms {resid_f.std():.4f} m, "
              f"M2 error {m2_err:+.4f} m, N2 error {n2_err:+.4f} m, "
              f"prediction rms {rms:.4f} m")
    print("  the fit residual is 0.028-0.030 m at every length, i.e. the noise")
    print("  level: it cannot rank the records.  The prediction error falls from")
    print("  0.0195 m at 7 days to 0.0025 m at 60 days, a factor of 8, and it is")
    print("  the prediction, not the residual, that shows what the record failed")
    print("  to separate.  A model with enough freedom always fits; only an")
    print("  out-of-sample test tells you whether it learned anything.")


if __name__ == "__main__":
    main()
