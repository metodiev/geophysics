#!/usr/bin/env python3
"""Postseismic relaxation: the Maxwell time, its verification, and how well a
viscoelastic exponential and an afterslip logarithm can be told apart.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python postseismic_viscoelastic_demo.py

Everything is SYNTHETIC.  The viscosities, the transient amplitudes and the
noise are chosen teaching values.  No real earthquake, GPS time series or
published viscosity estimate is used or quoted.

Contents
--------
1. Maxwell relaxation: tau = eta/mu, verified by integrating the constitutive
   law directly.
2. A single-relaxation-time postseismic transient, fitted from noisy data.
3. The (tau, amplitude) trade-off, mapped on a misfit grid.
4. Afterslip logarithm versus viscoelastic exponential: can the data choose?
5. Two relaxation times instead of one: what a layered viscosity does to an
   exponential fit.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC teaching parameters (chosen, not measured) --------------------
SHEAR_MODULUS_PA = 30.0e9     # SYNTHETIC shear modulus, Pa
SECONDS_PER_YEAR = 365.25 * 24.0 * 3600.0
ETA_VALUES = (1.0e19, 1.0e20, 1.0e21)   # SYNTHETIC viscosities, Pa s
D_ELASTIC_M = 0.08            # SYNTHETIC coseismic offset, m
D_TOTAL_M = 0.25              # SYNTHETIC total transient amplitude, m
NOISE_M = 0.004               # SYNTHETIC 1-sigma displacement noise, m
SAMPLE_YEARS = np.concatenate((np.linspace(0.02, 1.0, 12),
                               np.linspace(1.5, 10.0, 18),
                               np.linspace(11.0, 30.0, 12)))


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def maxwell_time_yr(eta):
    return eta / SHEAR_MODULUS_PA / SECONDS_PER_YEAR


def main():
    section("1. The Maxwell time, derived and verified numerically")
    print("  A Maxwell material in shear has strain rate")
    print("      e_dot = sigma_dot/(2 mu) + sigma/(2 eta).")
    print("  Setting e_dot = 0 (a fixed imposed strain) leaves")
    print("      sigma_dot = -(mu/eta) sigma   ->   sigma(t) = sigma_0 exp(-t/tau)")
    print("  with tau = eta/mu, independent of the stress magnitude.")
    print(f"  SYNTHETIC shear modulus mu = {SHEAR_MODULUS_PA / 1e9:.0f} GPa")
    print("\n    eta (Pa s)   tau = eta/mu (yr)   numerical decay (yr)")
    print("    " + "-" * 58)
    for eta in ETA_VALUES:
        tau_yr = maxwell_time_yr(eta)
        # integrate dsigma/dt = -sigma/tau with a small step and measure the
        # time to fall to 1/e, as an independent check of the closed form.
        dt = tau_yr / 20000.0
        sigma, t = 1.0, 0.0
        while sigma > np.exp(-1.0):
            sigma += -sigma / tau_yr * dt
            t += dt
        print(f"    {eta:.1e}   {tau_yr:17.2f}   {t:20.2f}")
    print("  The numerical 1/e time reproduces eta/mu to better than 0.01%, which")
    print("  is the check that the constitutive integration is consistent with the")
    print("  closed form.")
    print("\n  Reading the numbers: a lower-crustal viscosity of 1e19 Pa s relaxes")
    print(f"  a stress in {maxwell_time_yr(1e19):.1f} yr, while 1e21 Pa s takes")
    print(f"  {maxwell_time_yr(1e21):.0f} yr -- longer than the observation window of")
    print("  most postseismic surveys.  The same data therefore say very different")
    print("  things about viscosity depending on the assumed structure.")

    section("2. A single-relaxation-time transient, fitted from noisy data")
    tau_true_yr = maxwell_time_yr(1.0e19)
    t = SAMPLE_YEARS
    d_clean = D_TOTAL_M - (D_TOTAL_M - D_ELASTIC_M) * np.exp(-t / tau_true_yr)
    d_noisy = d_clean + NOISE_M * RNG.standard_normal(t.size)
    print(f"  SYNTHETIC model: D(t) = {D_TOTAL_M:.2f} - "
          f"({D_TOTAL_M - D_ELASTIC_M:.2f}) exp(-t/{tau_true_yr:.2f}) m")
    print(f"  {t.size} samples over {t.min():.2f} to {t.max():.1f} yr, "
          f"noise {NOISE_M * 1e3:.1f} mm per sample")
    print("    t (yr)     D model (m)   D noisy (m)")
    for i in range(0, t.size, 6):
        print(f"    {t[i]:6.2f}   {d_clean[i]:11.4f}   {d_noisy[i]:10.4f}")

    def model_exp(tt, d_inf, amp, tau):
        return d_inf - amp * np.exp(-tt / tau)

    from scipy.optimize import curve_fit
    popt, pcov = curve_fit(model_exp, t, d_noisy,
                           p0=(0.25, 0.17, 5.0),
                           sigma=np.full(t.size, NOISE_M), absolute_sigma=True,
                           maxfev=40000)
    perr = np.sqrt(np.diag(pcov))
    resid = model_exp(t, *popt) - d_noisy
    print(f"\n  fit: D(t) = {popt[0]:.4f} - {popt[1]:.4f} exp(-t/{popt[2]:.3f}) m")
    print(f"  truth: D(t) = {D_TOTAL_M:.4f} - {D_TOTAL_M - D_ELASTIC_M:.4f} "
          f"exp(-t/{tau_true_yr:.3f}) m")
    print(f"  tau = {popt[2]:.3f} +/- {perr[2]:.3f} yr "
          f"({100.0 * (popt[2] / tau_true_yr - 1.0):+.1f}% versus truth)")
    print(f"  rms residual = {np.sqrt(np.mean(resid ** 2)) * 1e3:.2f} mm "
          f"(input noise {NOISE_M * 1e3:.1f} mm)")
    print(f"  correlation between tau and the amplitude = "
          f"{pcov[1, 2] / (perr[1] * perr[2]):+.3f}")
    print(f"  correlation between tau and D_inf = "
          f"{pcov[0, 2] / (perr[0] * perr[2]):+.3f}")

    section("3. When is (tau, amplitude) actually determined?")
    taus = np.linspace(1.0, 30.0, 291)
    amps = np.linspace(0.08, 0.40, 161)

    def chi2_grid(sel):
        g = np.zeros((taus.size, amps.size))
        for i, tt in enumerate(taus):
            for j, aa in enumerate(amps):
                m = D_TOTAL_M - aa * np.exp(-t[sel] / tt)
                g[i, j] = np.sum(((m - d_noisy[sel]) / NOISE_M) ** 2)
        return g

    for label, sel, note in (
            ("full window (0.02-30 yr)", np.ones(t.size, dtype=bool),
             "the window spans three relaxation times"),
            ("short window (0.02-1.5 yr)", t <= 1.5,
             "the window is a seventh of a relaxation time")):
        g = chi2_grid(sel)
        i0, j0 = np.unravel_index(np.argmin(g), g.shape)
        ok = g <= g[i0, j0] + 1.0
        print(f"\n  {label}: {sel.sum()} samples; {note}")
        print(f"    best chi2 = {g[i0, j0]:.2f}, best tau = {taus[i0]:.2f} yr, "
              f"best amplitude = {amps[j0]:.3f} m")
        print(f"    delta-chi2 = 1 contour: tau "
              f"{taus[ok.any(axis=1)].min():.2f}-{taus[ok.any(axis=1)].max():.2f} yr, "
              f"amplitude {amps[ok.any(axis=0)].min():.3f}-"
              f"{amps[ok.any(axis=0)].max():.3f} m")
        print("      fixed tau   least-misfit amplitude (m)   chi2")
        for tt in (3.0, 6.0, 11.0, 22.0, 40.0):
            row = g[np.argmin(np.abs(taus - tt))]
            jbest = int(np.argmin(row))
            print(f"      {tt:9.1f}   {amps[jbest]:28.3f}   {row[jbest]:8.2f}")
    print("\n  The full window determines tau to a few per cent: the data see both")
    print("  the curvature and the asymptote.  The short window does not -- tau and")
    print("  the amplitude trade off along a long ridge, so a decay time quoted from")
    print("  a window shorter than the decay time is an assumption, not a result.")

    section("4. Afterslip logarithm versus viscoelastic exponential")
    print("  Common afterslip parameterisation: D(t) = a ln(1 + t/t*).")
    print("  Fitting that logarithm to the SYNTHETIC exponential data:")

    def model_log(tt, a, tstar):
        return a * np.log1p(tt / tstar)

    popt_l, pcov_l = curve_fit(model_log, t, d_noisy, p0=(0.1, 0.2),
                               sigma=np.full(t.size, NOISE_M),
                               absolute_sigma=True, maxfev=40000,
                               bounds=([1e-4, 1e-4], [2.0, 1e3]))
    resid_l = model_log(t, *popt_l) - d_noisy
    print(f"    log fit: a = {popt_l[0]:.4f} m, t* = {popt_l[1]:.3f} yr; "
          f"rms residual {np.sqrt(np.mean(resid_l ** 2)) * 1e3:.2f} mm")
    print(f"    exponential fit rms residual "
          f"{np.sqrt(np.mean(resid ** 2)) * 1e3:.2f} mm")
    ratio = np.sqrt(np.mean(resid_l ** 2)) / np.sqrt(np.mean(resid ** 2))
    print(f"    ratio of rms residuals (log/exponential) = {ratio:.2f}")
    t_dense = np.linspace(0.02, 30.0, 400)
    d_log_true = 0.06 * np.log1p(t_dense / 0.15)
    d_log_noisy = d_log_true + NOISE_M * RNG.standard_normal(t_dense.size)
    p1, _ = curve_fit(model_exp, t_dense, d_log_noisy, p0=(0.2, 0.1, 5.0),
                      sigma=np.full(t_dense.size, NOISE_M), absolute_sigma=True,
                      maxfev=40000, bounds=([0.01, 1e-4, 0.01], [2.0, 2.0, 1e3]))
    p2, _ = curve_fit(model_log, t_dense, d_log_noisy, p0=(0.05, 0.5),
                      sigma=np.full(t_dense.size, NOISE_M), absolute_sigma=True,
                      maxfev=40000, bounds=([1e-4, 1e-4], [2.0, 1e3]))
    r1 = np.sqrt(np.mean((model_exp(t_dense, *p1) - d_log_noisy) ** 2))
    r2 = np.sqrt(np.mean((model_log(t_dense, *p2) - d_log_noisy) ** 2))
    print(f"\n  The reverse test: SYNTHETIC log-decaying data, {t_dense.size} samples")
    print(f"    exponential fit rms = {r1 * 1e3:.2f} mm")
    print(f"    logarithm fit rms   = {r2 * 1e3:.2f} mm")
    print(f"    ratio = {r1 / r2:.2f}")
    print("  Over a two-decade window each functional form absorbs the other to")
    print("  within a small factor, and neither wins by an order of magnitude.  The")
    print("  discriminants that do work are physical, not statistical: afterslip")
    print("  decays in time but does not migrate in depth, whereas viscoelastic")
    print("  relaxation spreads into the deep crust and measurably changes the")
    print("  pattern of surface displacement with time.")

    section("5. Two relaxation times instead of one")
    eta1, eta2 = 1.0e19, 5.0e19
    tau1, tau2 = maxwell_time_yr(eta1), maxwell_time_yr(eta2)
    w1, w2 = 0.6, 0.4
    d_two = D_TOTAL_M - (w1 * 0.15 * np.exp(-t / tau1)
                         + w2 * 0.15 * np.exp(-t / tau2))
    print(f"  SYNTHETIC two-layer relaxation: tau_1 = {tau1:.2f} yr "
          f"(weight {w1:.1f}), tau_2 = {tau2:.2f} yr (weight {w2:.1f})")
    p_single, _ = curve_fit(model_exp, t, d_two, p0=(0.25, 0.15, 5.0),
                            maxfev=40000)
    r_two = model_exp(t, *p_single) - d_two
    print(f"  a single exponential fitted to this two-mode curve gives")
    print(f"    D(t) = {p_single[0]:.4f} - {p_single[1]:.4f} "
          f"exp(-t/{p_single[2]:.3f}) m")
    print(f"    rms residual = {np.sqrt(np.mean(r_two ** 2)) * 1e3:.2f} mm")
    print(f"    and a tau of {p_single[2]:.3f} yr, which is neither "
          f"{tau1:.2f} nor {tau2:.2f} yr")
    print("  A layered viscosity therefore does not have a single relaxation time,")
    print("  and the fitted tau is an effective value that depends on the time")
    print("  window.  Reporting one viscosity from one decay constant is only")
    print("  defensible when the layer structure is independently constrained.")


if __name__ == "__main__":
    main()
