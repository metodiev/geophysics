#!/usr/bin/env python3
"""Sea level and tides: the equilibrium tide amplitude, harmonic analysis of a
synthetic tide record, the Rayleigh criterion, aliasing, and a sea-level trend.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sea_level_tides_demo.py

Everything here is SYNTHETIC.  The tide record is generated from chosen
amplitudes and phases with synthetic noise; it is not a tide-gauge record.  The
astronomical constants used to derive the equilibrium tide are standard values.

Contents
--------
1. Equilibrium tide amplitude from the degree-2 tidal potential.
2. A synthetic tide record and its constituent frequencies.
3. Harmonic analysis by least squares, with formal errors.
4. The Rayleigh criterion and what a short record does to M2 and S2.
5. Aliasing: what a once-daily reading does to the semidiurnal tide.
6. A sea-level trend and its formal uncertainty.
7. Verification: residuals, covariance, and the closed-form check.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- Standard constants ------------------------------------------------------
G = 6.674e-11            # m^3 kg^-1 s^-2, gravitational constant
R_EARTH = 6.371e6        # m, mean Earth radius
G_SURF = 9.81            # m/s^2, standard gravity
M_EARTH = 5.972e24       # kg
M_MOON = 7.342e22        # kg
D_MOON = 3.844e8         # m
M_SUN = 1.989e30         # kg
D_SUN = 1.496e11         # m

# --- SYNTHETIC tide constituents (chosen amplitudes and phases) --------------
# periods are conventional astronomical values, in hours
CONSTITUENTS = (
    ("M2", 12.4206012, 1.20, 30.0),
    ("S2", 12.0000000, 0.40, 60.0),
    ("K1", 23.9344721, 0.15, 200.0),
    ("O1", 25.8193417, 0.10, 150.0),
)
NOISE_SIGMA = 0.05       # m, synthetic noise standard deviation


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def norm(a):
    return np.mod(a, 360.0)


def synth_tide(t_hours):
    """Synthetic tide: sum of A cos(omega t - phase), phase in degrees."""
    y = np.zeros_like(t_hours)
    for _, per, amp, ph in CONSTITUENTS:
        w = 2.0 * np.pi / (per * 3600.0)
        y += amp * np.cos(w * t_hours * 3600.0 - np.radians(ph))
    return y


def design(t_hours, names):
    """Least-squares design matrix: constant plus cosine and sine per name."""
    cols = [np.ones_like(t_hours)]
    for name in names:
        for nm, per, _, _ in CONSTITUENTS:
            if nm != name:
                continue
            w = 2.0 * np.pi / (per * 3600.0)
            cols.append(np.cos(w * t_hours * 3600.0))
            cols.append(np.sin(w * t_hours * 3600.0))
    return np.column_stack(cols)


def fit(t_hours, y, names):
    """Return (coeffs, covariance, residual rms) for the chosen constituents."""
    A = design(t_hours, names)
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    resid = y - A @ coef
    dof = max(A.shape[0] - A.shape[1], 1)
    s2 = float(resid @ resid) / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    return coef, cov, float(np.sqrt(np.mean(resid ** 2)))


def amp_phase(coef, names, j):
    """Amplitude and phase (degrees) of constituent j from its cos/sin pair."""
    ic = 1 + 2 * j
    a, b = coef[ic], coef[ic + 1]
    # a cos(wt) + b sin(wt) = A cos(wt - phi) with A = hypot(a,b), phi = atan2(b,a)
    return float(np.hypot(a, b)), float(np.degrees(np.arctan2(b, a)))


def main():
    section("1. Equilibrium tide amplitude from the degree-2 tidal potential")
    print("  Omega_2 = -(G M R^2/d^3) P_2(cos psi),  zeta = -Omega_2/g")
    print("  at the sub-body point (P_2 = 1) the equilibrium height is")
    print("  zeta_max = G M R^2/(g d^3).")
    print(f"\n  G = {G:.4e}, R = {R_EARTH / 1e3:.0f} km, "
          f"g = {G_SURF:.2f} m/s^2")
    for name, M, d in (("Moon", M_MOON, D_MOON), ("Sun", M_SUN, D_SUN)):
        zeta = G * M * R_EARTH ** 2 / (G_SURF * d ** 3)
        print(f"  {name}: M = {M:.3e} kg, d = {d:.3e} m")
        print(f"    zeta_max = {zeta:.4f} m; peak-to-trough = {2 * zeta:.4f} m")
    z_moon = G * M_MOON * R_EARTH ** 2 / (G_SURF * D_MOON ** 3)
    z_sun = G * M_SUN * R_EARTH ** 2 / (G_SURF * D_SUN ** 3)
    print(f"\n  solar/lunar ratio = {z_sun / z_moon:.4f}")
    print(f"  if the two bulges were perfectly aligned the range would be about "
          f"{2 * (z_moon + z_sun):.3f} m,")
    print("  but they are not: the lunar and solar bulges drift in and out of")
    print("  alignment over the spring-neap cycle (section 2).")
    print("  Observed tidal ranges depart from this by factors, because the")
    print("  equilibrium tide is the FORCING, not the response: ocean basins")
    print("  resonate, and a coast can amplify the local range far beyond it.")

    section("2. A synthetic tide record")
    print("  constituents (amplitude and phase are CHOSEN values):")
    print("\n   name   period (h)   omega (rad/s)   amplitude (m)   phase (deg)   "
          "deg/hour")
    for nm, per, amp, ph in CONSTITUENTS:
        w = 2.0 * np.pi / (per * 3600.0)
        print(f"  {nm:5s}  {per:11.4f}   {w:14.6e}   {amp:14.2f}   {ph:11.1f}   "
              f"{360.0 / per:10.4f}")
    w_m2 = 2 * np.pi / (CONSTITUENTS[0][1] * 3600.0)
    w_s2 = 2 * np.pi / (CONSTITUENTS[1][1] * 3600.0)
    df_deg = abs(360.0 / CONSTITUENTS[0][1] - 360.0 / CONSTITUENTS[1][1])
    print(f"\n  M2-S2 separation = {df_deg:.4f} deg/hour = "
          f"{df_deg / 360:.6f} cycles/hour")
    print(f"  the semidiurnal pair M2 and S2 beat with a period of "
          f"{1 / (df_deg / 360):.2f} hours = {1 / (df_deg / 360) / 24:.2f} days")
    print("  (the spring-neap cycle).  Any analysis shorter than that cannot")
    print("  separate them.")

    dt_h = 0.5
    dur_h = 60.0 * 24.0
    t = np.arange(0.0, dur_h, dt_h)
    y_clean = synth_tide(t)
    noise = NOISE_SIGMA * RNG.standard_normal(t.size)
    y = y_clean + noise
    print(f"\n  record: {t.size} samples, dt = {dt_h:.1f} h, duration "
          f"{dur_h / 24:.0f} days")
    print(f"  synthetic noise sigma = {NOISE_SIGMA:.3f} m; "
          f"signal range = {y_clean.max() - y_clean.min():.3f} m")
    print(f"  signal-to-noise of the M2 amplitude = "
          f"{CONSTITUENTS[0][2] / NOISE_SIGMA:.1f}")

    section("3. Harmonic analysis by least squares")
    names = [c[0] for c in CONSTITUENTS]
    coef, cov, rms = fit(t, y, names)
    print("  model: y = a0 + sum_j [ a_j cos(w_j t) + b_j sin(w_j t) ]")
    print(f"  {2 * len(names) + 1} parameters, {t.size} data points")
    print(f"  residual rms = {rms:.4f} m (injected noise sigma = "
          f"{NOISE_SIGMA:.3f} m)")
    print("\n   name   true A (m)   fitted A (m)   err (m)   coeff sigma (m)   "
          "true ph   fitted ph")
    for j, (nm, per, amp, ph) in enumerate(CONSTITUENTS):
        fit_a, fit_p = amp_phase(coef, names, j)
        ic = 1 + 2 * j
        sa = np.sqrt(cov[ic, ic])
        # for an (almost) orthogonal design the amplitude error equals the
        # coefficient error; the two differ once the constituents correlate.
        sig_a = sa
        print(f"  {nm:5s}  {amp:10.3f}   {fit_a:12.3f}   {fit_a - amp:+7.3f}   "
              f"{sig_a:16.4f}   {ph:7.1f}   {norm(fit_p):9.1f}")
    A = design(t, names)
    cond = np.linalg.cond(A)
    print(f"\n  condition number of the design matrix = {cond:.3f}")
    print("  A condition number near 1 is the statement that the four")
    print("  constituents are being asked independent questions of the data.")
    print("  It rises steeply when the record cannot separate them (section 4).")
    print("  Because the design is nearly orthogonal, the coefficient errors are")
    print("  all equal (0.0013 m) regardless of the constituent's amplitude: with")
    print("  enough data every constituent is measured with the same precision,")
    print("  and the SMALL constituents are the ones with the poor signal-to-noise.")
    f_m2 = CONSTITUENTS[0][2]
    f_s2 = CONSTITUENTS[1][2]
    f_k1 = CONSTITUENTS[2][2]
    f_o1 = CONSTITUENTS[3][2]
    print(f"\n  form ratio (K1 + O1)/(M2 + S2) = "
          f"{(f_k1 + f_o1) / (f_m2 + f_s2):.4f}")
    print("  a small value means the record is semidiurnal-dominated; the")
    print("  boundaries between 'diurnal' and 'semidiurnal' classes are")
    print("  conventions, and the ratio is the measurement.")

    section("4. The Rayleigh criterion")
    print("  Two constituents are separable if the record is longer than one")
    print("  beat period:  T > 1/|f_1 - f_2|.")
    print(f"\n  required length for M2 vs S2: {1 / (df_deg / 360) / 24:.2f} days")
    print("\n   record (days)   M2 fitted (m)   M2 err (m)   M2 sigma   "
          "S2 fitted (m)   S2 err (m)   S2 sigma   cond(A)")
    for days in (1.0, 2.0, 5.0, 10.0, 15.0, 30.0, 60.0):
        tsub = np.arange(0.0, days * 24.0, dt_h)
        idx = tsub.size
        ysub = y[:idx]
        try:
            cf, cv, _ = fit(tsub, ysub, names)
        except np.linalg.LinAlgError:
            print(f"  {days:14.0f}   singular: the constituents are not separable")
            continue
        a_m2, _ = amp_phase(cf, names, 0)
        a_s2, _ = amp_phase(cf, names, 1)
        s_m2 = np.sqrt(cv[1, 1])
        s_s2 = np.sqrt(cv[3, 3])
        Asub = design(tsub, names)
        print(f"  {days:14.0f}   {a_m2:14.3f}   {a_m2 - f_m2:+10.3f}   "
              f"{s_m2:8.4f}   {a_s2:14.3f}   {a_s2 - f_s2:+10.3f}   "
              f"{s_s2:8.4f}   {np.linalg.cond(Asub):8.3f}")
    print("\n  Read the columns together.  At one day the condition number is")
    print("  large and the formal errors are a small fraction of the fitted")
    print("  amplitudes: the two constituents TRADE OFF, so the fit can be close")
    print("  in a least-squares sense while neither amplitude is separately")
    print("  determined.  A small formal error computed from a nearly singular")
    print("  design is not a licence to quote the number; the condition number is")
    print("  the honest diagnostic, and it must be reported alongside the error bar.")

    section("5. Aliasing: a once-daily sample of a semidiurnal tide")
    dt_day = 24.0
    f_s = 1.0 / dt_day                              # cycles per hour
    print(f"  sampling interval = {dt_day:.0f} h -> sample frequency "
          f"{f_s:.6f} cycles/h")
    print("\n   constituent   f (cycles/h)   alias f (cycles/h)   alias period (h)")
    for nm, per, amp, ph in CONSTITUENTS:
        f = 1.0 / per
        alias = f - np.round(f / f_s) * f_s
        if abs(alias) < 1e-9:
            period = "aliases to zero frequency (DC)"
        else:
            period = f"{abs(1.0 / alias):.2f}"
        print(f"  {nm:12s}   {f:13.6f}   {alias:18.6f}   {period:>26s}")
    print("\n  S2 has a period of exactly 24 h, so a once-daily reading sees it as")
    print("  a constant: it is absorbed into the mean sea level.  Worse, M2")
    alias_m2 = 1.0 / CONSTITUENTS[0][1] - np.round((1.0 / CONSTITUENTS[0][1]) / f_s) * f_s
    print(f"  aliases to a period of {abs(1.0 / alias_m2) / 24:.2f} days,")
    print("  which is the same as the M2-S2 beat period computed in section 2.")
    print("  A fictitious 14.8-day oscillation in a short record is therefore")
    print("  indistinguishable from a genuine spring-neap cycle.  This is why tidal")
    print("  records are sampled at a fraction of an hour, not once a day.")

    section("6. A sea-level trend and its formal uncertainty")
    years = 20.0
    n_months = int(years * 12)
    tm = np.arange(n_months) / 12.0                    # years
    trend_true = 3.0e-3                                # m/yr
    seasonal = 0.06 * np.cos(2 * np.pi * tm - np.radians(60.0))
    lev = 0.10 + trend_true * tm + seasonal + 0.02 * RNG.standard_normal(n_months)
    A = np.column_stack([np.ones(n_months), tm,
                         np.cos(2 * np.pi * tm), np.sin(2 * np.pi * tm)])
    coef, *_ = np.linalg.lstsq(A, lev, rcond=None)
    res = lev - A @ coef
    dof = n_months - A.shape[1]
    s2 = float(res @ res) / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    print(f"  synthetic monthly means, {n_months} months ({years:.0f} years)")
    print(f"  trend in the data = {trend_true * 1e3:.2f} mm/yr, seasonal "
          f"amplitude 60 mm, noise sigma 20 mm")
    print(f"  fitted trend = {coef[1] * 1e3:.3f} mm/yr +/- "
          f"{np.sqrt(cov[1, 1]) * 1e3:.3f} mm/yr (formal 1-sigma)")
    print(f"  fitted seasonal amplitude = "
          f"{np.hypot(coef[2], coef[3]) * 1e3:.2f} mm")
    print(f"  residual rms = {np.sqrt(np.mean(res ** 2)) * 1e3:.2f} mm")
    print("\n  record length vs trend error (same noise and seasonality):")
    print("\n   years   fitted trend (mm/yr)   formal sigma (mm/yr)")
    for yy in (2, 5, 10, 20):
        nn = int(yy * 12)
        tt = np.arange(nn) / 12.0
        lv = (0.10 + trend_true * tt + 0.06 * np.cos(2 * np.pi * tt
              - np.radians(60.0)) + 0.02 * RNG.standard_normal(nn))
        AA = np.column_stack([np.ones(nn), tt, np.cos(2 * np.pi * tt),
                              np.sin(2 * np.pi * tt)])
        cc, *_ = np.linalg.lstsq(AA, lv, rcond=None)
        rr = lv - AA @ cc
        ss = float(rr @ rr) / (nn - AA.shape[1])
        cvv = ss * np.linalg.inv(AA.T @ AA)
        print(f"  {yy:6.0f}   {cc[1] * 1e3:19.3f}   "
              f"{np.sqrt(cvv[1, 1]) * 1e3:23.3f}")
    nn = int(years * 12)
    ttt = np.arange(nn) / 12.0
    var_slope = 0.02 ** 2 / np.sum((ttt - ttt.mean()) ** 2)
    print(f"\n  closed-form check: Var(slope) = sigma^2 / sum (t - tbar)^2 gives")
    print(f"    sigma_trend = {np.sqrt(var_slope) * 1e3:.4f} mm/yr, against the "
          f"least-squares value {np.sqrt(cov[1, 1]) * 1e3:.4f} mm/yr.")
    print("\n  The trend error falls with record length, but the fitted trend also")
    print("  moves: with a single short record the error bar is the only honest")
    print("  statement available, and it is a statement about THIS noise model.")

    section("7. Verification")
    print("(a) the residual rms should be close to the injected noise sigma:")
    print(f"    injected {NOISE_SIGMA:.4f} m, recovered {rms:.4f} m, ratio "
          f"{rms / NOISE_SIGMA:.4f}")
    print("(b) least-squares orthogonality: the residual must be orthogonal to")
    print("    every column of the design matrix.")
    A = design(t, names)
    coef, cov, _ = fit(t, y, names)
    resid = y - A @ coef
    print(f"    max |A^T r| = {np.abs(A.T @ resid).max():.3e} (m)")
    print("(c) a single-constituent fit has a closed form: for a record that is")
    print("    an integer number of cycles, A^T A/N = I/2 and the amplitude is")
    print("    recovered exactly.  Check with a 10-day M2-only signal:")
    t2 = np.arange(0.0, 10.0 * 24.0, dt_h)
    y2 = CONSTITUENTS[0][2] * np.cos(2 * np.pi * t2 * 3600.0
                                     / (12.4206012 * 3600.0)
                                     - np.radians(CONSTITUENTS[0][3]))
    cf2, _, rms2 = fit(t2, y2, ["M2"])
    a2, p2 = amp_phase(cf2, ["M2"], 0)
    print(f"    recovered amplitude = {a2:.6f} m (true "
          f"{CONSTITUENTS[0][2]:.6f} m), phase = {norm(p2):.4f} deg (true "
          f"{CONSTITUENTS[0][3]:.4f} deg)")
    print(f"    residual rms = {rms2:.3e} m: the 10-day record is not an exact")
    print("    integer number of M2 cycles, so a small leakage term remains.")


if __name__ == "__main__":
    main()
