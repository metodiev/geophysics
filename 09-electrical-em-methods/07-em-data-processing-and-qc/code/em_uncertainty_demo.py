#!/usr/bin/env python3
"""Quantifying uncertainty in EM interpretation: linearised error bars, Monte
Carlo intervals, measured coverage, and systematic error that no error bar sees.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_uncertainty_demo.py

EVERYTHING IS SYNTHETIC.  The two-layer earth is an exact image-series teaching
model; the noise level, the gain error and the prior are chosen values.  No
field data, instrument or published figure is used.

Contents
--------
1. Forward model, synthetic sounding, and its exact sensitivity matrix.
2. Grid inversion: the misfit valley, its elongation, and the trade-off between
   layer resistivity and thickness.
3. Linearised (Gauss-Newton) covariance: sigma, 68% and 95% intervals.
4. Monte Carlo: 200 noise realisations, empirical intervals, and the covariance
   between parameters.
5. Measured coverage of the linearised intervals.  Does 95% mean 95%?
6. Systematic error: a gain error of a few per cent, and what it does to an
   interval that only knows about noise.
7. A prior is a choice: how the reported interval moves when the parameter
   bounds move.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC earth and survey ---------------------------------------------
RHO1_T = 25.0            # ohm m
RHO2_T = 500.0           # ohm m
H_T = 8.0                # m
SPACINGS = np.logspace(0.0, 2.0, 12)      # Wenner a, 1 m to 100 m
REL_SIG = 0.03                            # 3% relative error per datum
N_MC = 200
NTERMS = 400


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def rho_a(a, rho1, rho2, H, nterms=NTERMS):
    """Exact Wenner apparent resistivity over a two-layer earth (image series).

    rho_a = rho1 [1 + 4a sum_n k^n (1/sqrt(a^2+(2nH)^2) - 1/sqrt(4a^2+(2nH)^2))]
    with k = (rho2-rho1)/(rho2+rho1).  Vectorised over the first argument.
    """
    a = np.atleast_1d(np.asarray(a, float))
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, nterms + 1)
    kn = k ** n
    term = kn[None, :] * (1.0 / np.sqrt(a[:, None] ** 2 + (2.0 * n[None, :] * H) ** 2)
                          - 1.0 / np.sqrt(4.0 * a[:, None] ** 2
                                          + (2.0 * n[None, :] * H) ** 2))
    return rho1 * (1.0 + 4.0 * a * term.sum(axis=1))


def build_library(rho1_grid, rho2_grid, H_grid):
    """Predictions of every model in the grid; shape (n_models, n_data)."""
    rows = []
    for H in H_grid:
        for rho1 in rho1_grid:
            for rho2 in rho2_grid:
                rows.append(rho_a(SPACINGS, rho1, rho2, H))
    return np.array(rows)


def jacobian(p, spacings, sig):
    """Central-difference Jacobian of the two-layer sounding, weighted-ready."""
    J = np.empty((spacings.size, 3))
    for j in range(3):
        h = 1e-5 * abs(p[j]) + 1e-8
        dp = np.zeros(3)
        dp[j] = h
        up = rho_a(spacings, *(p + dp))
        dn = rho_a(spacings, *(p - dp))
        J[:, j] = (up - dn) / (2.0 * h)
    return J


def refine(d, p, spacings, sig, iters=200):
    """Damped Gauss-Newton refinement; removes the grid quantisation."""
    p = np.array(p, float)
    lam = 1e-3
    chi2 = float(np.sum(((d - rho_a(spacings, *p)) / sig) ** 2))
    for _ in range(iters):
        J = jacobian(p, spacings, sig)
        Jw = J / sig[:, None]
        rw = (d - rho_a(spacings, *p)) / sig
        N = Jw.T @ Jw
        A = N + lam * np.diag(np.maximum(np.diag(N), 1e-30))
        try:
            dp = np.linalg.solve(A, Jw.T @ rw)
        except np.linalg.LinAlgError:
            break
        p_new = p + dp
        if np.any(p_new <= 0.0):
            lam *= 5.0
            continue
        c_new = float(np.sum(((d - rho_a(spacings, *p_new)) / sig) ** 2))
        if c_new < chi2:
            p, chi2, lam = p_new, c_new, max(lam * 0.3, 1e-10)
        else:
            lam *= 3.0
            if lam > 1e8:
                break
    return p, chi2


def main():
    section("1. Synthetic sounding and its sensitivity matrix")
    print("Wenner sounding over a two-layer earth; the forward model is the exact")
    print("image series of module 07-01, so the data are a model prediction plus")
    print("noise and nothing else.")
    print(f"SYNTHETIC earth: rho1 = {RHO1_T:.1f} ohm m, rho2 = {RHO2_T:.1f} ohm m, "
          f"H = {H_T:.1f} m")
    d_true = rho_a(SPACINGS, RHO1_T, RHO2_T, H_T)
    sig = REL_SIG * d_true
    print(f"{SPACINGS.size} spacings from {SPACINGS[0]:.2f} m to "
          f"{SPACINGS[-1]:.1f} m, {REL_SIG * 100:.0f}% relative error")
    print("\n    a (m)     rho_a (ohm m)     sigma (ohm m)")
    for a, d, s in zip(SPACINGS, d_true, sig):
        print(f"  {a:7.2f}   {d:13.4f}   {s:13.4f}")
    d_obs = d_true + sig * RNG.standard_normal(d_true.size)
    print(f"\nobserved sounding (one realisation): rho_a = "
          + ", ".join(f"{v:.1f}" for v in d_obs))
    # Jacobian by central differences at the true model
    def model_vec(p):
        return rho_a(SPACINGS, p[0], p[1], p[2])
    p0 = np.array([RHO1_T, RHO2_T, H_T])
    J = np.empty((SPACINGS.size, 3))
    steps = np.array([0.5, 5.0, 0.2])
    for j in range(3):
        dp = np.zeros(3)
        dp[j] = steps[j]
        J[:, j] = (model_vec(p0 + dp) - model_vec(p0 - dp)) / (2.0 * steps[j])
    print("\nsensitivity matrix d rho_a / d p at the true model "
          "(finest-difference step):")
    print("    a (m)      d/drho1      d/drho2        d/dH")
    for a, row in zip(SPACINGS, J):
        print(f"  {a:7.2f}   {row[0]:+11.4f}   {row[1]:+11.4f}   {row[2]:+11.5f}")
    print("The 1 m sounding barely sees rho2 and the 100 m sounding barely sees H;")
    print("that is why a sounding must span decades of spacing.")

    section("2. Grid inversion: the misfit valley")
    rho1_grid = np.linspace(20.0, 32.0, 13)
    rho2_grid = np.logspace(np.log10(100.0), np.log10(1500.0), 40)
    H_grid = np.logspace(np.log10(3.0), np.log10(16.0), 40)
    library = build_library(rho1_grid, rho2_grid, H_grid)
    inv_sig2 = 1.0 / sig ** 2
    A = library * inv_sig2[None, :]
    B = np.sum(library ** 2 * inv_sig2[None, :], axis=1)
    grid = np.array([(r1, r2, Hh) for Hh in H_grid for r1 in rho1_grid
                     for r2 in rho2_grid])
    print(f"library: {library.shape[0]} models = {rho1_grid.size} x "
          f"{rho2_grid.size} x {H_grid.size}")

    def invert(d):
        c0 = float(np.sum(d ** 2 * inv_sig2))
        chi2 = c0 - 2.0 * (A @ d) + B
        m = int(np.argmin(chi2))
        # continuous refinement, so that the estimate is not quantised by the grid
        return refine(d, grid[m], SPACINGS, sig)

    p_fit, chi2_fit = invert(d_obs)
    print(f"grid best fit, then refined continuously:")
    print(f"   rho1 = {p_fit[0]:.3f} (true {RHO1_T}), rho2 = {p_fit[1]:.2f} "
          f"(true {RHO2_T}), H = {p_fit[2]:.4f} (true {H_T})")
    print(f"chi2 = {chi2_fit:.2f} for {SPACINGS.size} data and 3 parameters "
          f"(expected about {SPACINGS.size - 3})")
    print("grid resolution: d rho1 = %.2f, d rho2/rho2 = %.3f, dH/H = %.3f; the"
          % (rho1_grid[1] - rho1_grid[0], rho2_grid[1] / rho2_grid[0] - 1.0,
             H_grid[1] / H_grid[0] - 1.0))
    print("refinement removes the quantisation, which would otherwise exceed")
    print("sigma_H and make the coverage test below meaningless.")
    print("\nrho2 and H trade off: the misfit along the valley")
    print("    rho2 (ohm m)      H (m)      chi2")
    for fac in (0.80, 0.90, 1.00, 1.10, 1.25):
        r2 = RHO2_T * fac
        best = None
        for Hh in H_grid:
            pred = rho_a(SPACINGS, RHO1_T, r2, Hh)
            c = float(np.sum(((d_true - pred) / sig) ** 2))
            if best is None or c < best[0]:
                best = (c, Hh)
        print(f"   {r2:12.1f}   {best[1]:9.3f}   {best[0]:7.3f}")

    section("3. Linearised covariance")
    Jinv = J / sig[:, None]                      # weighted Jacobian
    cov = np.linalg.inv(Jinv.T @ Jinv)
    sdp = np.sqrt(np.diag(cov))
    names = ("rho1 (ohm m)", "rho2 (ohm m)", "H (m)")
    print("covariance of the parameters from (J^T W J)^-1, W = 1/sigma^2:")
    print("   parameter        value        sigma         68% interval        "
          "95% interval")
    for j, nm in enumerate(names):
        v = p0[j]
        print(f"   {nm:14s} {v:8.3f}  {sdp[j]:11.4f}   "
              f"[{v - sdp[j]:8.3f},{v + sdp[j]:8.3f}]   "
              f"[{v - 1.96 * sdp[j]:8.3f},{v + 1.96 * sdp[j]:8.3f}]")
    print("\ncorrelation matrix of the parameter estimates:")
    corr = cov / np.outer(sdp, sdp)
    for j, nm in enumerate(names):
        print(f"   {nm:14s} " + " ".join(f"{corr[j, i]:+7.3f}"
                                         for i in range(3)))
    print("rho2 and H are strongly correlated: the data constrain a combination,")
    print("not two numbers.  The linearised interval already says so.")

    section("4. Monte Carlo: 200 noise realisations")
    hits = np.zeros(3)
    fits = np.empty((N_MC, 3))
    for k in range(N_MC):
        d = d_true + sig * RNG.standard_normal(d_true.size)
        p, _ = invert(d)
        fits[k] = p
        hits += (np.abs(fits[k] - p0) < 1.96 * sdp)
    print("      parameter      linear 1.96 sigma      MC 2.5-97.5 pct      "
          "MC skewness")
    for j, nm in enumerate(names):
        lo, hi = np.percentile(fits[:, j], [2.5, 97.5])
        sk = float(np.mean(((fits[:, j] - fits[:, j].mean())
                            / fits[:, j].std()) ** 3))
        print(f"   {nm:14s}   {2 * 1.96 * sdp[j]:18.3f}   "
              f"[{lo:7.3f},{hi:7.3f}]   {sk:+13.3f}")
    print(f"\nempirical correlation between the fitted rho2 and H: "
          f"{np.corrcoef(fits[:, 1], fits[:, 2])[0, 1]:+.4f}")
    print(f"linearised correlation:                              "
          f"{corr[1, 2]:+.4f}")
    print("The two agree closely here, because this problem is nearly linear in")
    print("the parameters over the region the data support.")

    section("5. Measured coverage of the 95% interval")
    print(f"Fraction of the {N_MC} realisations in which the true value lies "
          f"inside the")
    print("linearised 95% interval (nominal 0.950):")
    for j, nm in enumerate(names):
        print(f"   {nm:14s} {hits[j] / N_MC:.3f}")
    print("A number below 0.95 is an interval that is too small; the deficit is")
    print("the signature of non-linearity or of a mis-stated error model, and it")
    print("cannot be seen from a single sounding.  It takes a simulation like")
    print("this one, or a check against a known synthetic, to measure it.")

    section("6. Systematic error: the interval that cannot see it")
    print("Two systematic errors of the kind a survey actually carries: a gain")
    print("error (the current or the measured voltage is out by a factor) and a")
    print("geometry error (the electrode spacing is not what the file says).")
    eps = RNG.standard_normal(d_true.size)      # the SAME noise for every row
    print("\n   systematic        value   rho1 bias/sigma   rho2 bias/sigma   "
          "H bias/sigma")
    for label, gs in (("gain", (0.0, 0.01, 0.02, 0.03, 0.05)),
                      ("spacing", (0.01, 0.03, 0.05))):
        for g in gs:
            if label == "gain":
                d = d_true * (1.0 + g) + sig * eps
            else:
                d = rho_a(SPACINGS * (1.0 + g), RHO1_T, RHO2_T, H_T) + sig * eps
            p, _ = invert(d)
            b = (p - p0) / sdp
            print(f"   {label:10s}   {g:5.3f}   {b[0]:+16.2f}   {b[1]:+16.2f}   "
                  f"{b[2]:+13.2f}")
    print("\nA 3% gain error puts rho1 three sigma from the truth: the noise-based")
    print("95% interval for rho1 excludes it, yet nothing in a single sounding")
    print("reveals the error.  The covariance knows only the random part.  The")
    print("size of the systematic term has to be measured against an independent")
    print("check (repeat the sounding with a different current, or re-measure a")
    print("spacing), and then added to the budget by hand.")

    section("7. What the data actually admit, and what the prior adds")
    sub = SPACINGS <= 20.0            # a shallow sounding: no long spacings
    sig_sub = sig[sub]
    d_sub = d_true[sub] + sig_sub * RNG.standard_normal(int(sub.sum()))
    print(f"the observation is limited to a <= 20 m: {int(sub.sum())} data "
          f"instead of {SPACINGS.size}")
    print("Profile the misfit: for each rho2, minimise over rho1 and H.")
    best = np.inf
    prof = []
    for r2 in rho2_grid:
        sel = np.abs(grid[:, 1] - r2) < 1e-12
        resid = (d_sub[None, :] - library[sel][:, sub]) / sig_sub[None, :]
        c = np.min(np.sum(resid ** 2, axis=1))
        prof.append(c)
        best = min(best, c)
    prof = np.array(prof)
    adm = rho2_grid[prof - best < 5.99]           # 95% for one parameter
    print(f"rho2 values admitted at 95% (delta chi2 < 5.99) with rho1 and H free:")
    print(f"   {adm.min():.1f} to {adm.max():.1f} ohm m "
          f"(a factor {adm.max() / adm.min():.1f} in rho2)")
    print(f"the best profile chi2 is {best:.2f}")
    print("\n   rho2 (ohm m)   best H (m)   chi2    delta chi2   admitted at 95%?")
    for r2 in (150.0, 186.8, 250.0, 426.0, 700.0, 1200.0):
        k = int(np.argmin(np.abs(rho2_grid - r2)))
        sel = np.abs(grid[:, 1] - rho2_grid[k]) < 1e-9
        resid = (d_sub[None, :] - library[sel][:, sub]) / sig_sub[None, :]
        c = np.sum(resid ** 2, axis=1)
        m = int(np.argmin(c))
        dchi = c[m] - best
        print(f"   {rho2_grid[k]:12.1f}   {grid[sel][m][2]:10.3f}   {c[m]:6.2f}   "
              f"{dchi:10.2f}   {'yes' if dchi < 5.99 else 'no'}")
    print("\nThe data define a set of admissible earths; the number that gets")
    print("written into a report is one chosen member of that set, and only the")
    print("interval records the choice.  A shallow sounding whose longest spacing")
    print("never approaches the second layer simply cannot measure it, however")
    print("well the inversion is written down.")

if __name__ == "__main__":
    main()
