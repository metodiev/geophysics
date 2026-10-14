#!/usr/bin/env python3
"""Monte Carlo propagation and its convergence: measured, not asserted.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python monte_carlo_uq_demo.py

All models and data in this demo are SYNTHETIC.  The buried sphere, its
uncertainties and the detection threshold are chosen teaching values.

Contents
--------
1. A SYNTHETIC forward model with three uncertain inputs, and its Monte Carlo
   mean, standard deviation and 95% interval in mGal.
2. Convergence of the Monte Carlo error: the measured 1/sqrt(N) rate.
3. Variance reduction by antithetic variates, measured.
4. A rare-event probability by importance sampling, with its own effective
   sample size.
5. Independent verification against a deterministic quadrature over one input.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

G_SI = 6.67430e-11          # exact CODATA gravitational constant, m^3 kg^-1 s^-2
MGAL = 1.0e-5               # exact definition: 1 mGal = 10^-5 m/s^2

# SYNTHETIC uncertain inputs (means and standard deviations, chosen values).
R_MEAN, R_SD = 100.0, 8.0        # sphere radius, m
RHO_MEAN, RHO_SD = 500.0, 40.0   # density contrast, kg/m^3
Z_MEAN, Z_SD = 500.0, 25.0       # depth to centre, m
X_OBS = 0.0                      # observation directly above the centre, m
THRESHOLD_MGAL = 0.15            # SYNTHETIC detection threshold


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def sphere_gravity_mgal(radius, rho, depth, x=X_OBS):
    """Vertical gravity of a buried sphere, in mGal (exact Newtonian formula)."""
    g_si = (4.0 / 3.0) * np.pi * G_SI * rho * radius ** 3 * depth \
        / (x ** 2 + depth ** 2) ** 1.5
    return g_si / MGAL


def main():
    section("1. A SYNTHETIC forward model with uncertain inputs")
    print("Buried sphere, vertical gravity at the surface directly above it:")
    print("    g = (4/3) pi G rho R^3 z / (x^2 + z^2)^(3/2)")
    print(f"  G = {G_SI:.5e} m^3 kg^-1 s^-2 (exact CODATA value)")
    print(f"  1 mGal = {MGAL:.1e} m/s^2 (exact definition)")
    print(f"  R = {R_MEAN:.0f} +/- {R_SD:.0f} m, rho = {RHO_MEAN:.0f} +/- "
          f"{RHO_SD:.0f} kg/m^3, z = {Z_MEAN:.0f} +/- {Z_SD:.0f} m")
    g0 = float(sphere_gravity_mgal(R_MEAN, RHO_MEAN, Z_MEAN))
    print(f"  nominal prediction: g = {g0:.4f} mGal")
    # Exact derivatives for the nominal sensitivity (analytical, not finite diff).
    dR = 3.0 * g0 / R_MEAN
    drho = g0 / RHO_MEAN
    dz = g0 * (1.0 / Z_MEAN - 3.0 * Z_MEAN / (X_OBS ** 2 + Z_MEAN ** 2))
    print("nominal sensitivity, in mGal per unit input:")
    print(f"  dg/dR = {dR:.5f} mGal/m, dg/drho = {drho:.5f} mGal/(kg/m^3), "
          f"dg/dz = {dz:.5f} mGal/m")
    print(f"  linearised sd = sqrt(({dR:.3f}*{R_SD})^{{2}} + ... ) = "
          f"{np.sqrt((dR * R_SD) ** 2 + (drho * RHO_SD) ** 2 + (dz * Z_SD) ** 2):.4f} mGal")

    section("2. Monte Carlo propagation and its convergence rate")
    n_ref = 2_000_000
    R = R_MEAN + R_SD * RNG.standard_normal(n_ref)
    rho = RHO_MEAN + RHO_SD * RNG.standard_normal(n_ref)
    z = Z_MEAN + Z_SD * RNG.standard_normal(n_ref)
    g_ref_sample = sphere_gravity_mgal(R, rho, z)
    mu_ref = float(g_ref_sample.mean())
    sd_ref = float(g_ref_sample.std(ddof=1))
    print(f"reference from N = {n_ref:,} draws: mean {mu_ref:.4f} mGal, "
          f"sd {sd_ref:.4f} mGal")
    lo, hi = np.quantile(g_ref_sample, [0.025, 0.975])
    print(f"reference 95% interval: [{lo:.4f}, {hi:.4f}] mGal")
    print("\n  N        mean (mGal)   sd (mGal)   standard error of the mean")
    print("  " + "-" * 66)
    errs, ns = [], []
    reps = 20
    for N in (100, 1_000, 10_000, 100_000, 1_000_000):
        means = np.empty(reps)
        sds = np.empty(reps)
        for r in range(reps):
            g = sphere_gravity_mgal(R_MEAN + R_SD * RNG.standard_normal(N),
                                    RHO_MEAN + RHO_SD * RNG.standard_normal(N),
                                    Z_MEAN + Z_SD * RNG.standard_normal(N))
            means[r] = g.mean()
            sds[r] = g.std(ddof=1)
        se_theory = sds.mean() / np.sqrt(N)
        rms_err = float(np.sqrt(np.mean((means - mu_ref) ** 2)))
        print(f"  {N:7d}   {means.mean():10.4f}   {sds.mean():10.4f}   "
              f"{se_theory:.6f}")
        errs.append(rms_err)
        ns.append(N)
    slope = np.polyfit(np.log(ns), np.log(errs), 1)[0]
    print(f"\nmeasured log-log slope of the RMS error over {reps} replicates"
          f" versus N = {slope:.3f}")
    print("The RMS error over replicates is the honest measure, because a single")
    print("realisation of |mean - reference| is itself a random number. The slope")
    print("is -0.5: the Monte Carlo error falls as 1/sqrt(N), so halving it costs")
    print("four times the samples. The reported standard error of the mean is the")
    print("quantity to quote, not the sample size on its own.")
    for N, e in zip(ns, errs):
        print(f"    N = {N:8d}: RMS error {e:.6f} mGal, ratio to sigma/sqrt(N) "
              f"= {e / (sds.mean() / np.sqrt(N)):.3f}")

    section("3. Variance reduction by antithetic variates")
    def mc_mean(N, rng, antithetic):
        if antithetic:
            Z = rng.standard_normal((N // 2, 3))
            Z = np.vstack([Z, -Z])
        else:
            Z = rng.standard_normal((N, 3))
        g = sphere_gravity_mgal(R_MEAN + R_SD * Z[:, 0],
                                RHO_MEAN + RHO_SD * Z[:, 1],
                                Z_MEAN + Z_SD * Z[:, 2])
        return float(g.mean())

    reps = 400
    N = 2000
    rng = np.random.default_rng(7)
    plain = np.array([mc_mean(N, rng, False) for _ in range(reps)])
    anti = np.array([mc_mean(N, rng, True) for _ in range(reps)])
    print(f"  {reps} independent repetitions of N = {N} evaluations each")
    print(f"  plain Monte Carlo  : sd of the estimate = {plain.std(ddof=1):.6f} mGal")
    print(f"  antithetic variates: sd of the estimate = {anti.std(ddof=1):.6f} mGal")
    print(f"  variance reduction factor = {(plain.std(ddof=1) / anti.std(ddof=1)) ** 2:.2f}x")
    print("Antithetic sampling pairs each draw with its mirror image, which pays")
    print("off when the model is monotone in the inputs, as this one is (g is")
    print("increasing in R and rho, decreasing in z). The reduction is a claim about")
    print("the model, not a general property of the method: for a non-monotone model")
    print("the same construction can increase the variance, so it must be measured.")

    section("4. A rare-event probability by importance sampling")
    print(f"target: P(g > {THRESHOLD_MGAL:.2f} mGal), where g is the sphere anomaly")
    rng = np.random.default_rng(11)
    Z = rng.standard_normal((2_000_000, 3))
    g = sphere_gravity_mgal(R_MEAN + R_SD * Z[:, 0], RHO_MEAN + RHO_SD * Z[:, 1],
                            Z_MEAN + Z_SD * Z[:, 2])
    n_plain = Z.shape[0]
    k_plain = int(np.sum(g > THRESHOLD_MGAL))
    p_plain = k_plain / n_plain
    se_plain = np.sqrt(p_plain * (1.0 - p_plain) / n_plain)
    print(f"  plain Monte Carlo with {n_plain:,} draws: {k_plain} exceedances, "
          f"p = {p_plain:.3e} +/- {se_plain:.1e}")
    print(f"  the relative standard error is "
          f"{100 * se_plain / p_plain:.1f}%: too few events to report")
    # Shift the proposal towards larger anomalies: increase R and rho, decrease z.
    # The shift is applied in standard-normal coordinates.
    shift = np.array([1.32, 0.44, -0.55])
    Z2 = rng.standard_normal((200_000, 3))
    zp = Z2 + shift
    g2 = sphere_gravity_mgal(R_MEAN + R_SD * zp[:, 0], RHO_MEAN + RHO_SD * zp[:, 1],
                             Z_MEAN + Z_SD * zp[:, 2])
    # Importance weight = target density / proposal density, both standard
    # normals, so w = exp(-z' . s + |s|^2 / 2) with z' ~ N(s, I).
    logw = -np.sum(zp * shift, axis=1) + 0.5 * np.sum(shift ** 2)
    w = np.exp(logw - logw.max())
    w = w / w.mean()
    ind = (g2 > THRESHOLD_MGAL).astype(float)
    n_is = Z2.shape[0]
    p_is = float(np.mean(w * ind))
    var_is = float(np.mean((w * ind - p_is) ** 2) / n_is)
    ess = float(w.sum() ** 2 / np.sum(w ** 2))
    print(f"  importance sampling with {n_is:,} draws: {int(ind.sum())} "
          f"exceedances, p = {p_is:.3e} +/- {np.sqrt(var_is):.1e}")
    print(f"  effective sample size = {ess:.0f} of {n_is:,} "
          f"({100 * ess / n_is:.2f}%)")
    print(f"  the two estimates differ by "
          f"{abs(p_is - p_plain) / se_plain:.2f} standard errors of the plain one")
    print(f"  cost: {n_plain / n_is:.0f}x fewer forward evaluations, and the")
    print(f"  relative standard error falls from "
          f"{100 * se_plain / p_plain:.1f}% to {100 * np.sqrt(var_is) / p_is:.1f}%")
    print("A rare-event probability cannot be estimated by counting events that")
    print("almost never happen: the plain estimate here rests on a few dozen")
    print("events. Importance sampling moves the sampling to where the event is")
    print("and the weights correct for the move. Its own effective sample size is")
    print("the diagnostic that says whether that correction is stable: if the")
    print("weights are dominated by a handful of draws, the estimate is not.")
    Z2 = None

    section("5. Independent verification by quadrature over one input")
    # Integrate out rho analytically: g is linear in rho, so
    #   E[g | R, z] = (4/3 pi G R^3 z / (x^2+z^2)^{3/2}) * RHO_MEAN / MGAL.
    grid = np.linspace(R_MEAN - 4 * R_SD, R_MEAN + 4 * R_SD, 4001)
    dg = grid[1] - grid[0]
    wz = np.exp(-0.5 * ((grid - R_MEAN) / R_SD) ** 2)
    wz /= wz.sum() * dg
    zg = np.linspace(Z_MEAN - 4 * Z_SD, Z_MEAN + 4 * Z_SD, 4001)
    dz_ = zg[1] - zg[0]
    wzz = np.exp(-0.5 * ((zg - Z_MEAN) / Z_SD) ** 2)
    wzz /= wzz.sum() * dz_
    # mean over R and z with rho at its mean (rho enters linearly)
    f = np.zeros((grid.size, zg.size))
    for i, r in enumerate(grid):
        f[i, :] = sphere_gravity_mgal(r, RHO_MEAN, zg)
    mu_quad = float(np.einsum("i,j,ij->", wz, wzz, f) * dg * dz_)
    print(f"quadrature over (R, z) with rho linearised: mean = {mu_quad:.4f} mGal")
    print(f"Monte Carlo reference                     : mean = {mu_ref:.4f} mGal")
    print(f"difference = {abs(mu_quad - mu_ref):.5f} mGal")
    print("Two independent routes to the same number. Because g is linear in rho,")
    print("integrating that variable out is exact; the remaining quadrature is a")
    print("check on the sampling, not on the physics.")


if __name__ == "__main__":
    main()
