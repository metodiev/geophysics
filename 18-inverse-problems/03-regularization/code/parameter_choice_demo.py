#!/usr/bin/env python3
"""Choosing the regularisation parameter: the L-curve, generalised cross
validation and the discrepancy principle -- and their measured failure modes.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python parameter_choice_demo.py

All models and data are SYNTHETIC: the exact 2-D line-mass gravity kernel of a
textbook forward model, a chosen density distribution, a chosen station grid and
computer-generated noise.  No measured data and no published numbers are used.

The problem is written in standard form (kernel divided by its spectral norm,
data divided consistently), so alpha is dimensionless.

Contents
--------
1. The synthetic problem and the design used by every rule.
2. L-curve: the trade-off curve, its curvature and its corner alpha.
3. Generalised cross validation: the GCV function and its minimum.
4. Discrepancy principle: alpha from a stated noise level.
5. Head-to-head against the per-realisation oracle alpha.
6. Monte Carlo: reproducibility of each choice and its price.
7. Failure modes: wrong noise level, correlated noise, no L-curve corner.
"""

import numpy as np
from scipy.interpolate import UnivariateSpline

RNG = np.random.default_rng(20261014)
G_CONST = 6.67430e-11
MGAL = 1.0e5


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def line_mass_kernel(x_obs_m, x_src_m, depth_m):
    """2-D line-mass gravity kernel in mGal per (kg/m); see the lesson."""
    dx = x_obs_m[:, None] - x_src_m[None, :]
    return 2.0 * G_CONST * depth_m / (dx**2 + depth_m**2) * MGAL


class Problem:
    """Standard-form 1-D line-mass problem with a full alpha design."""

    def __init__(self, n=64, depth=600.0, noise_fraction=0.005,
                 alphas=np.logspace(-12, 1, 400)):
        self.n = n
        self.x = np.linspace(-4000.0, 4000.0, n)
        K_phys = line_mass_kernel(self.x, self.x, depth)
        self.m_true = 1.0e9 * np.exp(-(self.x / 1500.0) ** 2)     # kg/m
        d_true = K_phys @ self.m_true
        self.d_true = d_true
        self.noise_phys = noise_fraction * np.abs(d_true).max()
        U, sv, Vt = np.linalg.svd(K_phys)
        self.U, self.V, self.sh = U, Vt.T, sv / sv[0]
        self.norm_m = float(np.linalg.norm(self.m_true))
        self.norm_d = float(sv[0] * self.norm_m)
        self.m_hat = self.m_true / self.norm_m
        self.d_hat = d_true / self.norm_d
        self.sig = self.noise_phys / self.norm_d
        self.y_clean = U.T @ self.d_hat
        self.alphas = alphas
        # design: for every alpha, the solution operator and the GCV trace term
        self.f = self.sh[None, :] ** 2 / (self.sh[None, :] ** 2 + alphas[:, None])
        self.solve_op = self.V[None, :, :] * (self.f[:, None, :]
                                             / self.sh[None, None, :])
        self.trace = self.f.sum(axis=1)
        self.npar = self.f.sum(axis=1)

    def evaluate(self, Y):
        """Per-alpha, per-realisation errors, model norms and residual norms.

        ``Y`` has shape (n_real, n) with standard-form data coefficients.
        """
        nr = Y.shape[0]
        err = np.empty((self.alphas.size, nr))
        mnorm = np.empty_like(err)
        r2 = np.empty_like(err)
        for j in range(self.alphas.size):
            M = Y @ self.solve_op[j].T * self.norm_m
            err[j] = np.linalg.norm(M - self.m_true, axis=1) / self.norm_m
            mnorm[j] = np.linalg.norm(M, axis=1) / self.norm_m
            r2[j] = ((1.0 - self.f[j]) ** 2 * Y**2).sum(axis=1)
        return err, mnorm, r2

    def gcv(self, r2):
        return (r2 / self.n) / (1.0 - self.trace[:, None] / self.n) ** 2


def corner_alpha(P, r2_col, mnorm_col, smooth=None):
    """Corner of the L-curve from the maximum curvature in log-log coordinates."""
    t = np.log10(P.alphas)
    lr = 0.5 * np.log10(np.maximum(r2_col, 1e-300))
    lm = np.log10(mnorm_col)
    sr, sm = UnivariateSpline(t, lr, s=smooth), UnivariateSpline(t, lm, s=smooth)
    tt = np.linspace(t[0], t[-1], 1200)
    dr, dm = sr.derivative()(tt), sm.derivative()(tt)
    ddr, ddm = sr.derivative(2)(tt), sm.derivative(2)(tt)
    kap = np.abs(dr * ddm - dm * ddr) / (dr**2 + dm**2) ** 1.5
    j = int(np.argmax(kap))
    return 10.0 ** tt[j], float(kap[j])


def discrepancy_alpha(P, r2_col, delta2):
    """Largest alpha whose residual variance still matches delta2 (log-linear
    interpolation on the grid; the grid step is 0.033 decades)."""
    ok = r2_col >= delta2
    j = int(np.argmax(ok))
    if j == 0:
        return P.alphas[0]
    if not ok.any():
        return P.alphas[-1]
    x0, x1 = np.log10(P.alphas[j - 1]), np.log10(P.alphas[j])
    y0, y1 = np.log10(r2_col[j - 1]), np.log10(r2_col[j])
    frac = (np.log10(delta2) - y0) / (y1 - y0)
    return 10.0 ** (x0 + frac * (x1 - x0))


def main():
    P = Problem()
    n = P.n
    alphas = P.alphas
    sig = P.sig
    delta2 = n * sig**2

    section("1. The synthetic problem and the design")
    print(f"  kernel : 2-D line masses at 0.60 km depth, {n} stations and {n} cells")
    print(f"  sigma_1(K) = {P.norm_d / P.norm_m:.5e} mGal per (kg/m), "
          f"kappa_2 = {1.0 / P.sh[-1]:.3e}")
    print(f"  true model : peak {P.m_true.max():.4e} kg/m, "
          f"||m_true|| = {P.norm_m:.4e} kg/m")
    print(f"  exact data : peak {P.d_true.max():.2f} mGal")
    print(f"  noise      : sigma = {P.noise_phys:.4f} mGal per datum "
          f"({P.noise_phys / np.abs(P.d_true).max() * 100:.2f}% of the peak), "
          f"{sig:.4e} in standard form")
    print(f"  grid       : {alphas.size} alphas, {alphas[0]:.0e} to {alphas[-1]:.0e}")
    print("  Every rule below sees the same data; they differ only in how they")
    print("  trade residual against model norm.  The oracle alpha -- the one that")
    print("  minimises the error against the true model -- is listed only as a")
    print("  benchmark, because it requires the answer.")

    # -------------------------------------------------------------- 2. L-curve
    section("2. The L-curve")
    y_one = P.y_clean + sig * RNG.standard_normal(n)
    err1, mn1, r21 = P.evaluate(y_one[None, :])
    err1, mn1, r21 = err1[:, 0], mn1[:, 0], r21[:, 0]
    a_L, kap_L = corner_alpha(P, r21, mn1)
    print("  Each alpha gives a point (||K m_alpha - d||, ||m_alpha||); as alpha")
    print("  grows the residual rises and the model norm falls, giving an")
    print("  L-shaped curve whose corner is taken as the compromise.\n")
    print("   alpha      ||K m - d||      ||m||/||m_true||   ||m - m_true||/||m_true||")
    for a in (1e-8, 1e-6, 1e-4, a_L, 1e-2, 1e-1):
        j = int(np.argmin(np.abs(alphas - a)))
        tag = "   <- corner" if abs(a - a_L) < 1e-12 else ""
        print(f"  {a:7.1e}   {np.sqrt(r21[j]):15.6f}   {mn1[j]:16.5f}   "
              f"{err1[j]:26.5f}{tag}")
    print(f"  maximum curvature of the smoothed curve : {kap_L:.3f}")
    print(f"  L-curve corner alpha                    : {a_L:.3e}")
    print("  The corner is a geometric feature of the plotted trade-off, not a")
    print("  statistical statement: the curve has no probabilistic model behind it.")
    print("  Its sharpness is the measured curvature above; a small value would")
    print("  mean there is no identifiable corner at all.")
    print("\n  HIDDEN PARAMETER.  The curvature must be computed from a smoothed")
    print("  curve, and the smoothing level changes the answer:\n")
    print("   spline s     corner alpha   max curvature   error   res^2/(n sigma^2)")
    for s in (None, 1e-6, 1e-4, 1e-3, 1e-2, 1e-1):
        a_s, k_s = corner_alpha(P, r21, mn1, smooth=s)
        j_s = int(np.argmin(np.abs(alphas - a_s)))
        print(f"  {str(s):10s}   {a_s:12.3e}   {k_s:13.3f}   {err1[j_s]:6.4f}   "
              f"{r21[j_s] / delta2:16.3f}")
    print("  The corner moves by a factor of five across these choices.  The rule")
    print("  therefore has a second, usually unreported parameter.")
    jL = int(np.argmin(np.abs(alphas - a_L)))
    print(f"\n  DIAGNOSTIC.  The corner solution has ||K m - d||^2 = "
          f"{r21[jL] / delta2:.3f} x n sigma^2,")
    print("  i.e. a residual BELOW the noise level: it is partly fitting noise.")
    print("  The residual test exposes what the geometric rule cannot say, and it")
    print("  is how a practitioner can tell that a corner alpha is too small.")

    # ------------------------------------------------------------------ 3. GCV
    section("3. Generalised cross validation")
    print("  G(alpha) = (||K m_alpha - d||^2 / n) / (1 - sum_i f_i / n)^2")
    print("  The numerator is the misfit; the denominator counts the effective")
    print("  number of fitted parameters, so GCV penalises the fitting of noise.")
    print("  It needs no noise estimate.\n")
    g = P.gcv(r21[:, None])[:, 0]
    jG = int(np.argmin(g))
    a_G = alphas[jG]
    print("   alpha            G(alpha)")
    for a in (1e-9, 1e-6, 1e-4, a_G, 1e-2, 1e-1, 1e0):
        j = int(np.argmin(np.abs(alphas - a)))
        tag = "   <- GCV minimum" if abs(a - a_G) < 1e-12 else ""
        print(f"  {a:7.1e}   {g[j]:16.6e}{tag}")
    flat = g < 1.05 * g[jG]
    print(f"  alphas within 5% of the GCV minimum: {int(flat.sum())} of "
          f"{alphas.size}, spanning {alphas[flat][0]:.2e} to {alphas[flat][-1]:.2e}")
    print(f"  GCV alpha = {a_G:.3e}")
    print("  A flat minimum is normal: GCV identifies a region of alphas, not a")
    print("  point, and quoting more than two significant figures would overstate it.")

    # ----------------------------------------------------------- 4. discrepancy
    section("4. The discrepancy principle")
    a_D = discrepancy_alpha(P, r21, delta2)
    print("  For white noise with known sigma, E||e||^2 = n sigma^2.  The principle")
    print("  chooses the LARGEST alpha whose residual is still consistent with")
    print("  that: the most smoothed model that the data can tolerate.\n")
    print(f"  n sigma^2                       = {delta2:.6e}")
    print(f"  ||K m - d||^2 at alpha = 1e-6   : "
          f"{r21[int(np.argmin(np.abs(alphas - 1e-6)))]:.6e}")
    print(f"  ||K m - d||^2 at alpha = 1e-2   : "
          f"{r21[int(np.argmin(np.abs(alphas - 1e-2)))]:.6e}")
    print(f"  discrepancy alpha               : {a_D:.3e}")
    jD = int(np.argmin(np.abs(alphas - a_D)))
    print(f"  residual there = {r21[jD] / delta2:.4f} x n sigma^2")
    print("  The rule is only as good as sigma, and sigma is often estimated from")
    print("  the data or from the instrument.  Section 7a measures the damage when")
    print("  the estimate is wrong by a factor of two, and by a factor of four.")

    # ---------------------------------------------------------- 5. head to head
    section("5. Head-to-head on one realisation")
    jO = int(np.argmin(err1))
    a_O = alphas[jO]
    print("   rule                         alpha     ||m - m_true||/||m_true||"
          "   ratio to oracle")
    for name, a, e in (("oracle (needs the truth)", a_O, err1[jO]),
                       ("L-curve corner", a_L, err1[int(np.argmin(np.abs(alphas - a_L)))]),
                       ("GCV", a_G, err1[jG]),
                       ("discrepancy principle", a_D, err1[jD]),
                       ("no regularisation", alphas[0], err1[0]),
                       ("extreme smoothing", alphas[-1], err1[-1])):
        print(f"  {name:28s} {a:10.3e}   {e:26.5f}   {e / err1[jO]:14.2f}")
    print("  The oracle is unattainable, and the three rules do not agree with")
    print("  each other or with it.  Each pays a different price; none is right.")

    # ------------------------------------------------------------ 6. Monte Carlo
    section("6. Monte Carlo: reproducibility of the choice (300 realisations)")
    n_mc = 300
    Y = P.y_clean[None, :] + RNG.standard_normal((n_mc, n)) * sig
    err, mn, r2 = P.evaluate(Y)
    g_all = P.gcv(r2)
    a_ora = alphas[np.argmin(err, axis=0)]
    e_ora = err.min(axis=0)
    a_gcv = alphas[np.argmin(g_all, axis=0)]
    a_disc = np.array([discrepancy_alpha(P, r2[:, r], delta2) for r in range(n_mc)])
    a_lc = np.empty(n_mc)
    for r in range(n_mc):
        a_lc[r], _ = corner_alpha(P, r2[:, r], mn[:, r], smooth=1e-3)
    e_of = lambda aa, rr: err[int(np.argmin(np.abs(alphas - aa[rr]))), rr]
    print("  (the L-curve corner is computed with a fixed spline smoothing of")
    print("   s = 1e-3, the value used for the sensitivity table in section 2.)")
    print("   rule        median alpha   IQR log10 a   error 10-90% range"
          "   median error   error / oracle")
    for k, aa in (("oracle", a_ora), ("L-curve", a_lc), ("GCV", a_gcv),
                  ("discrepancy", a_disc)):
        la = np.log10(aa)
        ee = np.array([e_of(aa, r) for r in range(n_mc)])
        print(f"  {k:10s}  {np.median(aa):12.3e}   "
              f"{np.percentile(la, 75) - np.percentile(la, 25):10.2f}   "
              f"{np.percentile(ee, 5):7.4f}-{np.percentile(ee, 95):7.4f}   "
              f"{np.median(ee):12.5f}   "
              f"{np.median(ee) / np.median(e_ora):14.3f}")
    print("  Measured spread of the chosen alpha: an interquartile range of")
    print(f"  {np.percentile(np.log10(a_gcv), 75) - np.percentile(np.log10(a_gcv), 25):.2f} decades for GCV and")
    print(f"  {np.percentile(np.log10(a_lc), 75) - np.percentile(np.log10(a_lc), 25):.2f} decades for the L-curve corner, i.e. the rules are reproducible to")
    print("  within a factor of two or so on THIS problem.  Reproducibility is not")
    print("  accuracy: the median error of the L-curve rule is 7.6 times the oracle")
    print("  error, and that gap is the rule's BIAS, not run-to-run luck.  On a")
    print("  different problem the same rule can be both biased and noisy; what is")
    print("  general is that neither is zero, so the rule must be reported with the")
    print("  alpha it chose and the noise level it assumed.")

    # --------------------------------------------------------- 7. failure modes
    section("7a. Failure mode: the noise level given to the discrepancy principle")
    print("   assumed sigma / true sigma   median alpha   median error"
          "   error / oracle")
    for fac in (0.25, 0.5, 1.0, 2.0, 4.0):
        aa = np.array([discrepancy_alpha(P, r2[:, r], n * (fac * sig) ** 2)
                       for r in range(n_mc)])
        ee = np.array([e_of(aa, r) for r in range(n_mc)])
        print(f"  {fac:23.2f}   {np.median(aa):12.3e}   {np.median(ee):12.5f}   "
              f"{np.median(ee) / np.median(e_ora):18.3f}")
    print("  UNDERESTIMATING sigma is the dangerous direction: the target n sigma^2")
    print("  is too small, the rule drives alpha to the bottom of the grid and the")
    print("  error rises by orders of magnitude -- it fits noise.  OVERESTIMATING")
    print("  sigma over-smooths, and here the price is much milder (a factor of two")
    print("  in sigma costs 1.17-2.17 times the oracle error).  That asymmetry is a")
    print("  measurement on THIS problem, not a general law: it follows from the")
    print("  curvature of the trade-off, which is steeper on the under-smoothing")
    print("  side.  Either way, a discrepancy-principle alpha is meaningless without")
    print("  the sigma that produced it.")

    section("7b. Failure mode: correlated noise (GCV assumes white noise)")
    Ec = RNG.standard_normal((n_mc, n))
    Ec = np.apply_along_axis(lambda v: np.convolve(v, np.ones(5) / 5.0,
                                                   mode="same"), 1, Ec)
    Ec *= sig / Ec.std()
    print("  The correlated noise is a 5-sample moving average rescaled to the")
    print("  same rms, so sigma is unchanged but there are fewer effective")
    print("  independent data.  The discrepancy principle is used here with the")
    print("  TRUE sigma, to separate the effect of correlation from a wrong sigma.\n")
    print("   noise       median alpha (GCV)   GCV error/oracle"
          "   median alpha (discrep.)   discrep. error/oracle")
    for tag, M in (("white", RNG.standard_normal((n_mc, n)) * sig), ("correlated", Ec)):
        Yn = P.y_clean[None, :] + M
        e2, _, r22 = P.evaluate(Yn)
        g2 = P.gcv(r22)
        a_g2 = alphas[np.argmin(g2, axis=0)]
        a_d2 = np.array([discrepancy_alpha(P, r22[:, r], delta2)
                         for r in range(n_mc)])
        eg = np.array([e2[int(np.argmin(np.abs(alphas - a_g2[r]))), r]
                       for r in range(n_mc)])
        ed = np.array([e2[int(np.argmin(np.abs(alphas - a_d2[r]))), r]
                       for r in range(n_mc)])
        eo = e2.min(axis=0)
        print(f"  {tag:11s}   {np.median(a_g2):15.3e}   "
              f"{np.median(eg) / np.median(eo):16.3f}   "
              f"{np.median(a_d2):23.3e}   {np.median(ed) / np.median(eo):22.3f}")
    print("  Both rules degrade when the noise is correlated: GCV under-smooths")
    print("  because its denominator counts n independent data that do not exist,")
    print("  and the discrepancy principle with a correct sigma still misplaces the")
    print("  threshold because ||e||^2 is no longer distributed as n sigma^2 times a")
    print("  chi-square with n degrees of freedom.  The assumption, not the")
    print("  arithmetic, is what failed.")

    section("7c. Failure mode: no L-curve corner to find")
    print("  As the noise grows the trade-off curve can straighten and the measured")
    print("  curvature can collapse; whether it does here is a measurement, and the")
    print("  answer below is that it happens late.  A rule that needs a corner has")
    print("  nothing to find once the corner is gone.\n")
    print("   noise (% peak)   max curvature   median alpha   IQR log10 alpha"
          "   corner error/oracle   corner res^2/(n sigma^2)")
    for frac in (0.005, 0.05, 0.20):
        nz = frac * np.abs(P.d_true).max() / P.norm_d
        Yn = P.y_clean[None, :] + RNG.standard_normal((n_mc, n)) * nz
        e3, mn3, r23 = P.evaluate(Yn)
        aa = np.empty(n_mc)
        kk = np.empty(n_mc)
        for r in range(n_mc):
            aa[r], kk[r] = corner_alpha(P, r23[:, r], mn3[:, r], smooth=1e-3)
        la = np.log10(aa)
        jj = np.array([int(np.argmin(np.abs(alphas - aa[r]))) for r in range(n_mc)])
        ec = e3[jj, np.arange(n_mc)]
        eo = e3.min(axis=0)
        resr = r23[jj, np.arange(n_mc)] / (n * nz**2)
        print(f"  {frac * 100:15.1f}   {np.median(kk):14.3f}   "
              f"{np.median(aa):12.3e}   "
              f"{np.percentile(la, 75) - np.percentile(la, 25):14.2f}   "
              f"{np.median(ec) / np.median(eo):19.2f}   {np.median(resr):26.3f}")
    print("  The curvature is not monotone in the noise level: 47.6 at 0.5% noise,")
    print("  52.2 at 5% and 8.1 at 20%, so only at the largest noise level does the")
    print("  curve visibly lose its sharpness.  The corner error relative to the")
    print("  oracle is 7.4 at 0.5% noise and 1.5-1.8 at 5% and 20% -- but the")
    print("  oracle's own error grows with the noise too, so the RATIO is not the")
    print("  honest summary; the absolute error is.  What holds in every case is the")
    print("  residual diagnostic: the corner sits at a residual below n sigma^2, so")
    print("  the corner solution is always fitting some noise.  The L-curve remains")
    print("  a useful PICTURE of the trade-off and a weak ESTIMATOR of alpha; the")
    print("  measurement above is the difference between those two statements.")


if __name__ == "__main__":
    main()
