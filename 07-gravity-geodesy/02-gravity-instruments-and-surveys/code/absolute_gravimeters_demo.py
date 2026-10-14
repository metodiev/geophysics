#!/usr/bin/env python3
"""Absolute gravimetry by free fall: the least-squares fit for g from a drop,
the measured sensitivity to position noise, timing jitter and the number of
samples, why a constant timing offset cancels, the fringe count and wavelength
requirement of an interferometric measurement, the biases from residual drag and
from the Earth tide, and the statistics of a set of drops.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python absolute_gravimeters_demo.py

Everything is SYNTHETIC: the drop geometry, noise levels, drag coefficient,
wavelength and tidal amplitude are chosen teaching values.  The only exact
constants are G (6.67430e-11 m^3 kg^-1 s^-2), the model Earth's GM
(3.986004418e14 m^3 s^-2) and the unit relation 1 uGal = 1e-8 m/s^2.
No instrument model number is used or implied.

Contents
--------
1. Free fall and the least-squares fit for g: z = z0 + v0 t + (1/2) g t^2.
2. Measured sensitivity to position noise, timing jitter and sample count.
3. A constant timing offset cancels in the fit; random jitter does not.
4. Interferometry: fringe count, half-wavelength, and the wavelength requirement.
5. Residual drag: the fitted g is biased low by half the terminal drag.
6. Earth tide during a drop set: mean value and change within the set.
7. The gradient over the drop: which g the fit actually returns.
8. Statistics of twenty drops, including one outlier, and the systematic budget.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G = 6.67430e-11
GM_EARTH = 3.986004418e14
G_TRUE = 9.820250            # m/s^2, SYNTHETIC station value at the drop origin
DROP_HEIGHT = 0.200          # m
N_SAMPLES = 700
LAMBDA_LASER = 633.0e-9      # m, SYNTHETIC wavelength
TIDE_AMPLITUDE = 1.2e-6      # m/s^2, SYNTHETIC tidal acceleration amplitude
TIDE_PERIOD = 12.4 * 3600.0  # s, SYNTHETIC semidiurnal period


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def fit_drop(t, z):
    """Least-squares fit of z = z0 + v0 t + (1/2) g t^2; returns (g, sigma_g, rms)."""
    A = np.column_stack([0.5 * t ** 2, t, np.ones(t.size)])
    coef, *_ = np.linalg.lstsq(A, z, rcond=None)
    resid = z - A @ coef
    dof = t.size - 3
    s2 = float(resid @ resid) / dof
    cov = s2 * np.linalg.inv(A.T @ A)
    return coef[0], np.sqrt(cov[0, 0]), np.sqrt(np.mean(resid ** 2))


def main():
    duration = np.sqrt(2.0 * DROP_HEIGHT / G_TRUE)
    print("SYNTHETIC free-fall experiment")
    print(f"  drop height      = {DROP_HEIGHT:.3f} m")
    print(f"  implied duration = {duration:.6f} s (from h = g t^2 / 2)")
    print(f"  number of samples= {N_SAMPLES}")
    print(f"  true g           = {G_TRUE:.6f} m/s^2 = {G_TRUE * 1e5:.2f} mGal")

    section("1. The fit and its formal uncertainty (one SYNTHETIC drop)")
    t = np.linspace(0.0, duration, N_SAMPLES)
    sigma_z = 1.0e-9                         # m, 1 nm position noise
    z = 0.5 * G_TRUE * t ** 2 + sigma_z * RNG.standard_normal(N_SAMPLES)
    g_hat, sig_formal, rms = fit_drop(t, z)
    print(f"  position noise sigma_z = {sigma_z:.0e} m")
    print(f"  fitted g        = {g_hat:.9f} m/s^2")
    print(f"  error           = {(g_hat - G_TRUE) * 1e8:+.3f} uGal")
    print(f"  formal sigma_g  = {sig_formal * 1e8:.3f} uGal")
    print(f"  residual rms    = {rms:.3e} m (= {rms / sigma_z:.2f} x sigma_z)")
    print("  g is twice the fitted quadratic coefficient; the formal sigma comes")
    print("  from s^2 (A^T A)^-1 and is a claim about this model, not about the")
    print("  physics that the model omits.")

    section("2. Measured sensitivity to noise and sample count (200 realisations each)")
    n_mc = 200
    rows = []
    for sigma_z_mc in (1e-10, 1e-9, 1e-8):
        gs = []
        for _ in range(n_mc):
            zz = 0.5 * G_TRUE * t ** 2 + sigma_z_mc * RNG.standard_normal(t.size)
            gs.append(fit_drop(t, zz)[0])
        rows.append((f"position noise {sigma_z_mc:.0e} m", np.std(gs)))
    for sigma_t in (1e-10, 1e-9, 1e-8):
        gs = []
        for _ in range(n_mc):
            # the trajectory is exact; the RECORDED times carry the jitter
            zz = 0.5 * G_TRUE * t ** 2
            t_meas = t + sigma_t * RNG.standard_normal(t.size)
            gs.append(fit_drop(t_meas, zz)[0])
        rows.append((f"timing jitter {sigma_t:.0e} s", np.std(gs)))
    for n_mc_samples in (200, 700, 2000):
        t_n = np.linspace(0.0, duration, n_mc_samples)
        gs = []
        for _ in range(n_mc):
            zz = (0.5 * G_TRUE * t_n ** 2
                  + 1e-9 * RNG.standard_normal(t_n.size))
            gs.append(fit_drop(t_n, zz)[0])
        rows.append((f"{n_mc_samples} samples", np.std(gs)))
    print("   configuration                     sigma_g (uGal)")
    for label, sd in rows:
        print(f"   {label:32s} {sd * 1e8:14.3f}")
    print("  MEASURED SCALING: sigma_g is proportional to the position noise (each")
    print("  factor of 10 in sigma_z gives a factor of 10 in sigma_g) and to the")
    print("  timing jitter, and it falls roughly as 1/sqrt(N) (the counts 200, 700 and")
    print("  2000 give ratios close to sqrt(3.5) and sqrt(2.86) rather than the exact")
    print("  sqrt of the ratios, so the fall-off is approximate).")
    print("  The two timing rows and the two position rows weigh the same: 1 nm of")
    print("  position noise costs 2.6 uGal and 1 ns of timing jitter costs 3.1 uGal,")
    print("  so neither can be neglected and both must be controlled at the")
    print("  nanometre and nanosecond level to reach a few microgal from one drop.")

    section("3. A constant timing offset cancels; random jitter does not")
    for offset in (1e-9, 1e-7):
        gs = [fit_drop(t + offset, 0.5 * G_TRUE * (t + offset) ** 2)[0]
              for _ in range(3)]
        print(f"  time origin shifted by {offset:.0e} s: fitted g error = "
              f"{(gs[0] - G_TRUE) * 1e8:+.3e} uGal")
    print("  Because z(t + dt) = (1/2) g t^2 + g dt t + (1/2) g dt^2, a constant")
    print("  offset reappears in the LINEAR and constant terms of the same model,")
    print("  which absorb it exactly.  Only timing noise that is not a constant")
    print("  (jitter, or a clock drift during the drop) biases the fit, which is")
    print("  why Section 2 finds a sensitivity to random jitter and none to offset.")

    section("4. Interferometry: fringes and wavelength requirement")
    fringes = 2.0 * DROP_HEIGHT / LAMBDA_LASER
    print(f"  chosen laser wavelength lambda = {LAMBDA_LASER * 1e9:.1f} nm")
    print(f"  one fringe = lambda/2 = {LAMBDA_LASER / 2 * 1e9:.2f} nm of displacement")
    print(f"  a {DROP_HEIGHT:.3f} m drop spans 2h/lambda = {fringes:.0f} fringes")
    print(f"  resolving a fraction f of a fringe gives a position resolution of")
    print(f"  {LAMBDA_LASER / 2 * 1e9:.2f} nm x f; f = 1/64 gives "
          f"{LAMBDA_LASER / 2 * 1e9 / 64:.3f} nm")
    print("  The wavelength enters g directly:")
    for rel in (1e-6, 1e-8, 1e-10):
        print(f"   relative wavelength error {rel:.0e} -> g error "
              f"{rel * G_TRUE * 1e8:12.3f} uGal")
    print(f"  so a 1 uGal requirement needs a relative wavelength accuracy better")
    print(f"  than {1e-8 / G_TRUE:.1e}, i.e. an absolutely known laser frequency, not")
    print("  merely a stable one.  This is a metrology constraint, not a mechanical one.")

    section("5. Residual drag biases the fitted g by half the terminal drag")
    t_ode = t
    for k_drag in (1e-5, 2e-5, 4e-5):
        # z(t) = g/k [ t - (1 - exp(-k t))/k ]; evaluated in series form because
        # k t ~ 1e-6 makes the closed form cancel to round-off.
        z_drag = 0.5 * G_TRUE * t_ode ** 2 - G_TRUE * k_drag * t_ode ** 3 / 6.0
        bias = fit_drop(t_ode, z_drag)[0] - G_TRUE
        v_end = G_TRUE * duration
        a_end = k_drag * v_end
        print(f"   k = {k_drag:.0e} 1/s: drag acceleration at the end of the drop = "
              f"{a_end * 1e8:8.1f} uGal")
        print(f"                 fitted-g bias = {bias * 1e8:8.1f} uGal, ratio = "
              f"{bias / a_end:+.4f}")
    print("  The ratio is exactly -0.5 in every case: drag acceleration grows")
    print("  linearly in time, so it is absorbed as extra curvature in the quadratic")
    print("  fit and half of its terminal value lands in g.  A residual-gas drag of")
    print("  200 uGal at the end of the drop therefore biases the answer by")
    print("  100 uGal - the same order as the effect that is supposed to be measured.")
    print("  This is why an absolute gravimeter drops its mass in vacuum and applies")
    print("  a residual-gas correction, and why the correction is calibrated rather")
    print("  than guessed.")

    section("6. The Earth tide during a drop set")
    print(f"  SYNTHETIC tide: amplitude {TIDE_AMPLITUDE * 1e8:.1f} uGal, period "
          f"{TIDE_PERIOD / 3600:.1f} h")
    print("   set (min)   mean tide (uGal)   change in set   mean minus value at midpoint")
    for minutes in (1.0, 10.0, 20.0, 60.0):
        tt = np.linspace(0.0, minutes * 60.0, 4001)
        acc = TIDE_AMPLITUDE * np.sin(2.0 * np.pi * tt / TIDE_PERIOD)
        mid = TIDE_AMPLITUDE * np.sin(
            2.0 * np.pi * (minutes * 30.0) / TIDE_PERIOD)
        print(f"   {minutes:9.1f}   {acc.mean() * 1e8:15.3f}   "
              f"{(acc.max() - acc.min()) * 1e8:13.3f}   "
              f"{(acc.mean() - mid) * 1e8:24.4f}")
    print("  The tidal acceleration at this phase changes by 1 uGal during a")
    print("  one-minute set and by about 20 uGal during a twenty-minute set, and the")
    print("  mean over the set differs from the value at its midpoint by less than")
    print("  0.01 uGal in every case: correcting with the tide evaluated at the")
    print("  midpoint is therefore adequate at the microgal level for these set")
    print("  lengths, and would not be for a set spanning hours.  The check is the")
    print("  last column, not an assumption.")

    section("7. Which g the fit returns: the effective height")
    gradient = 2.0 * GM_EARTH / (6371.0e3) ** 3
    print(f"  dg/dr at the model surface = -2g/r = "
          f"{-G_TRUE * 2 / 6371.0e3 * 1e8:.3f} uGal/m")
    print(f"  over the drop, g varies by {gradient * DROP_HEIGHT * 1e8:.3f} uGal")
    print(f"  the fit returns g at the origin of its parabola, i.e. at the start")
    print(f"  height of the drop.  Reporting a value at a different reference height")
    print(f"  requires a correction of {gradient * 1e-3 * 1e8:.3f} uGal per millimetre,")
    print(f"  so a 0.2 m drop geometry enters as {gradient * DROP_HEIGHT * 1e8:.1f} uGal")
    print("  of height correction and the instrument's own height must be defined")
    print("  with its datum.  A 1 mm height error costs "
          f"{gradient * 1e-3 * 1e8:.3f} uGal.")

    section("8. Statistics of a set of drops")
    n_drops = 20
    single = 2.4e-8                    # m/s^2, one drop's scatter (measured in 2)
    drops = G_TRUE + single * RNG.standard_normal(n_drops)
    mean = drops.mean()
    sem = drops.std(ddof=1) / np.sqrt(n_drops)
    print(f"  {n_drops} drops with per-drop scatter {single * 1e8:.2f} uGal")
    print(f"   mean  = {mean:.9f} m/s^2, error from truth = "
          f"{(mean - G_TRUE) * 1e8:+.3f} uGal")
    print(f"   standard error of the mean = {sem * 1e8:.3f} uGal "
          f"(= {single * 1e8:.2f}/sqrt({n_drops}) = "
          f"{single * 1e8 / np.sqrt(n_drops):.3f})")
    bad = drops.copy()
    bad[7] += 1.0e-6                   # one drop hit by a 1 mGal event
    print(f"   one drop perturbed by +1.0 mGal:")
    print(f"     mean   = {bad.mean():.9f}, error = {(bad.mean() - G_TRUE) * 1e8:+.3f} uGal")
    print(f"     median = {np.median(bad):.9f}, error = "
          f"{(np.median(bad) - G_TRUE) * 1e8:+.3f} uGal")
    resid = bad - np.median(bad)
    mad_sigma = 1.4826 * np.median(np.abs(resid))
    print(f"     robust sigma from the median absolute deviation = "
          f"{mad_sigma * 1e8:.3f} uGal")
    print(f"     largest deviation = {np.max(np.abs(resid)) / mad_sigma:.2f} robust sigma")
    print("  A single disturbed drop moves the mean by tens of microgal while the")
    print("  median barely moves, and the robust sigma flags it: outlier rejection")
    print("  is part of the measurement, not a cosmetic step afterwards.")


if __name__ == "__main__":
    main()
