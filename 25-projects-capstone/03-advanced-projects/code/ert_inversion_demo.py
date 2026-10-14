#!/usr/bin/env python3
"""Advanced project 2: a one-dimensional resistivity sounding, its inversion, and
three honest measures of what the inversion actually resolves.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_inversion_demo.py

Everything here is SYNTHETIC.  The sounding curve is generated from a chosen
two-layer model with chosen noise; no field survey, no instrument and no
published sounding is used.

Sections
--------
1. The forward model: a two-layer Wenner sounding curve.
2. The inverse problem: parameters, misfit and the fitted model.
3. Linearised uncertainties and the parameter correlation matrix.
4. Resolution: the profile-likelihood equivalence class and the depth of
   investigation.
"""

import numpy as np
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)

RHO1_TRUE = 100.0          # top-layer resistivity, ohm m
RHO2_TRUE = 1000.0         # half-space resistivity, ohm m
H_TRUE = 10.0              # top-layer thickness, m
REL_NOISE = 0.03           # relative noise level
ABS_NOISE = 1.0            # absolute noise floor, ohm m
N_TERMS = 60               # image terms in the two-layer series
SPACINGS = np.unique(np.round(np.geomspace(1.0, 60.0, 25), 3))


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def rho_a_wenner(a, rho1, rho2, h):
    """Wenner apparent resistivity over a two-layer earth, by image series."""
    k = (rho2 - rho1) / (rho2 + rho1)

    def factor(r):
        n = np.arange(1, N_TERMS + 1)
        rr = np.atleast_1d(r)[:, None]
        series = k ** n / np.sqrt(1.0 + (2.0 * n * h / rr) ** 2)
        return 1.0 + 2.0 * np.sum(series, axis=1)

    return 2.0 * rho1 * (factor(a) - 0.5 * factor(2.0 * a))


def forward(pars, a):
    rho1, rho2, h = np.exp(pars)      # fit in log space: all parameters positive
    return rho_a_wenner(a, rho1, rho2, h)


def main():
    section("1. The forward model")
    rho_a_true = rho_a_wenner(SPACINGS, RHO1_TRUE, RHO2_TRUE, H_TRUE)
    sigma = REL_NOISE * rho_a_true + ABS_NOISE
    rho_a_obs = rho_a_true + sigma * RNG.standard_normal(SPACINGS.size)
    print(f"SYNTHETIC two-layer model: rho1 = {RHO1_TRUE:.0f} ohm m, "
          f"rho2 = {RHO2_TRUE:.0f} ohm m, h = {H_TRUE:.1f} m")
    print(f"  reflectance k = (rho2-rho1)/(rho2+rho1) = "
          f"{(RHO2_TRUE - RHO1_TRUE) / (RHO2_TRUE + RHO1_TRUE):.4f}")
    print(f"  {SPACINGS.size} Wenner spacings from {SPACINGS[0]:.1f} to "
          f"{SPACINGS[-1]:.1f} m; noise {REL_NOISE:.0%} relative + "
          f"{ABS_NOISE:.1f} ohm m")
    print(f"{'a (m)':>8}{'rho_a true':>13}{'rho_a obs':>13}{'sigma':>10}")
    for i in (0, 6, 12, 18, 24):
        print(f"{SPACINGS[i]:>8.1f}{rho_a_true[i]:>13.2f}{rho_a_obs[i]:>13.2f}"
              f"{sigma[i]:>10.2f}")
    print(f"  the curve runs from {rho_a_true[0]:.1f} ohm m at short spacing")
    print(f"  to {rho_a_true[-1]:.1f} ohm m at long spacing, approaching - but")
    print(f"  not reaching - rho2 = {RHO2_TRUE:.0f} ohm m.")

    section("2. The inversion")
    start = np.log([50.0, 300.0, 5.0])
    sol = least_squares(lambda p: (forward(p, SPACINGS) - rho_a_obs) / sigma,
                        start, method="lm", xtol=1e-12, ftol=1e-12)
    rho1_f, rho2_f, h_f = np.exp(sol.x)
    resid = (forward(sol.x, SPACINGS) - rho_a_obs) / sigma
    chi2 = float(resid @ resid)
    n_data, n_par = SPACINGS.size, 3
    print(f"  least squares in log-parameters, no regularisation")
    print(f"  fitted: rho1 = {rho1_f:.3f} ohm m "
          f"({rho1_f / RHO1_TRUE - 1.0:+.2%}), "
          f"rho2 = {rho2_f:.2f} ohm m ({rho2_f / RHO2_TRUE - 1.0:+.2%}), "
          f"h = {h_f:.4f} m ({h_f / H_TRUE - 1.0:+.2%})")
    print(f"  chi^2 = {chi2:.3f} for {n_data} data and {n_par} parameters "
          f"(expect about {n_data - n_par} = {n_data - n_par})")
    print(f"  rms residual = {np.sqrt(chi2 / n_data):.3f} sigma")
    print("  -> the sounding is well fitted, and that says nothing yet about")
    print("     how well each parameter is determined.")

    section("3. Linearised uncertainties and correlation")
    jac = sol.jac
    dof = n_data - n_par
    cov = np.linalg.inv(jac.T @ jac) * chi2 / dof
    err = np.sqrt(np.diag(cov))
    corr = cov / np.outer(err, err)
    names = ("rho1", "rho2", "h")
    print("  linearised 1-sigma uncertainties (in the log parameters, i.e.")
    print("  relative for the resistivities):")
    for i, nm in enumerate(names):
        print(f"    {nm:<5} {np.exp(sol.x[i]):>10.4f}  "
              f"relative 1-sigma = {err[i] * 100:>6.2f}%")
    print(f"  relative 1-sigma on h = {err[2]:.4f} -> "
          f"+/- {err[2] * h_f:.3f} m")
    print("  correlation matrix:")
    for i, nm in enumerate(names):
        print("    " + nm.ljust(5) + "  " +
              "  ".join(f"{corr[i, j]:+.3f}" for j in range(3)))
    print(f"  corr(rho2, h) = {corr[1, 2]:+.3f}: the two rise and fall together,")
    print("  so an equally good fit can be a thinner layer over a less resistive")
    print("  half-space or a thicker one over a more resistive half-space.  The")
    print("  linearised covariance states the degeneracy; the next section")
    print("  measures its full extent.")

    section("4. Resolution: profile likelihood and depth of investigation")
    h_grid = np.linspace(0.8 * H_TRUE, 1.3 * H_TRUE, 101)
    chi2_h = np.empty(h_grid.size)
    rho2_h = np.empty(h_grid.size)
    for j, h_try in enumerate(h_grid):
        def residual2(p, h_try=h_try):
            return (forward(np.array([p[0], p[1], np.log(h_try)]), SPACINGS)
                    - rho_a_obs) / sigma

        s2 = least_squares(residual2, np.log([rho1_f, rho2_f]), method="lm",
                           xtol=1e-12, ftol=1e-12)
        chi2_h[j] = float(s2.fun @ s2.fun)
        rho2_h[j] = np.exp(s2.x[1])
    accept = chi2_h <= chi2_h.min() + 1.0
    h_lo, h_hi = h_grid[accept].min(), h_grid[accept].max()
    print(f"  profile likelihood over h: chi^2_min = {chi2_h.min():.3f}")
    print(f"  h within chi^2_min + 1 (1-sigma for one parameter): "
          f"{h_lo:.2f} to {h_hi:.2f} m "
          f"(linearised value {h_f:.2f} +/- {err[2] * h_f:.2f} m)")
    print(f"  the accepted rho2 range is {rho2_h[accept].min():.0f} to "
          f"{rho2_h[accept].max():.0f} ohm m, against a fitted "
          f"{rho2_f:.0f} ohm m")
    print(f"{'h (m)':>8}{'chi^2':>10}{'rho2 (ohm m)':>15}")
    for j in (0, 25, 50, 75, 100):
        print(f"{h_grid[j]:>8.2f}{chi2_h[j]:>10.3f}{rho2_h[j]:>15.1f}")
    sens = np.abs(rho_a_wenner(SPACINGS, rho1_f, 1.1 * rho2_f, h_f)
                  - rho_a_wenner(SPACINGS, rho1_f, rho2_f, h_f)) / rho1_f
    sens_norm = sens / sens.max()
    idx = np.flatnonzero(sens_norm >= 0.5)
    k0 = max(idx[0], 1)
    a_half = float(np.interp(0.5, sens_norm[k0 - 1:k0 + 1],
                             SPACINGS[k0 - 1:k0 + 1]))
    print(f"  sensitivity to rho2 (normalised) reaches 50% of its maximum at")
    print(f"  a = {a_half:.2f} m; with the Wenner median depth of investigation")
    print(f"  of about a/2 that is a depth of order {a_half / 2:.2f} m, and the")
    print(f"  longest spacing probes to about {SPACINGS[-1] / 2:.0f} m")
    print("  -> quote the trade-off and the DOI; a single best-fit number hides")
    print("     both.")


if __name__ == "__main__":
    main()
