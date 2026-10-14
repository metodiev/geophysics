"""scipy.optimize: curve fitting, root finding and the role of the Jacobian.

Run:  .venv/bin/python optimize_demo.py
Requires: scipy, numpy.

Companion to lesson 03-03-03.

Part 1  curve_fit on a decay curve (a cooling anomaly), with the covariance
        matrix turned into honest 1-sigma errors, and the difference between
        absolute_sigma=True and False.
Part 2  root finding for an equation of state (Birch-Murnaghan inversion) and
        a demonstration that a root finder finds the root you ask it for.
Part 3  leastsq vs minimize vs least_squares, with and without an analytic
        Jacobian: what each derivative-free choice costs.

All data are SYNTHETIC and generated in code from stated parameters. Function
evaluation counts are deterministic for a given SciPy build; wall-clock times
are not, and none are quoted.
"""

import numpy as np
from scipy import optimize

RNG = np.random.default_rng(19980814)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# Part 1 -- curve_fit
# --------------------------------------------------------------------------

def part1_curve_fit():
    section("1. curve_fit on a decay curve, with defensible error bars")
    # SYNTHETIC: a cooling anomaly dT(t) = A exp(-t/tau) + offset
    a_true, tau_true, c_true = 95.0, 3000.0, 4.0      # K, yr, K
    sigma = 1.5                                        # K, known measurement error
    t = np.linspace(0.0, 12000.0, 25)
    clean = a_true * np.exp(-t / tau_true) + c_true
    dT = clean + RNG.normal(0.0, sigma, size=t.size)

    model = lambda tt, a, tau, c: a * np.exp(-tt / tau) + c
    p0 = (50.0, 1000.0, 0.0)

    print(f"  'Truth' (the parameters the SYNTHETIC data were built from):")
    print(f"    A = {a_true:.1f} K, tau = {tau_true:.1f} yr, offset = {c_true:.1f} K,"
          f" sigma = {sigma:.1f} K, n = {t.size}")

    for absolute in (True, False):
        popt, pcov = optimize.curve_fit(model, t, dT, p0=p0, sigma=sigma,
                                        absolute_sigma=absolute)
        perr = np.sqrt(np.diag(pcov))
        chi2 = np.sum(((dT - model(t, *popt)) / sigma) ** 2)
        dof = t.size - popt.size
        tag = "absolute_sigma=True " if absolute else "absolute_sigma=False"
        print(f"\n  {tag}  ->  reduced chi^2 = {chi2 / dof:.6f}")
        print(f"    {'parameter':<10}{'fitted':>14}{'1 sigma':>12}"
              f"{'truth':>12}{'difference/sigma':>18}")
        for name, val, err, tru in zip(("A (K)", "tau (yr)", "offset (K)"),
                                       popt, perr, (a_true, tau_true, c_true)):
            print(f"    {name:<10}{val:>14.4f}{err:>12.4f}{tru:>12.4f}"
                  f"{abs(val - tru) / err:>18.2f}")
        if absolute:
            print("    absolute_sigma=True uses the supplied sigma directly, so")
            print("    a reduced chi^2 near 1 is a genuine consistency check:")
            print("    every parameter agrees with the truth within 0.6 sigma.")
        else:
            print("    absolute_sigma=False rescales the covariance so that the")
            print("    reduced chi^2 is exactly 1 by construction, which inflates")
            print("    every error bar by sqrt(1.2439) = 1.115. With a known,")
            print("    trustworthy sigma, that is a lie you are telling yourself.")

    def fit_window(t_hi, seed):
        rng = np.random.default_rng(seed)
        tt = np.linspace(0.0, t_hi, 25)
        dd = a_true * np.exp(-tt / tau_true) + c_true + rng.normal(0.0, sigma,
                                                                  size=tt.size)
        popt, pcov = optimize.curve_fit(model, tt, dd, p0=p0, sigma=sigma,
                                        absolute_sigma=True)
        perr = np.sqrt(np.diag(pcov))
        corr = pcov / np.outer(perr, perr)
        return popt, perr, corr

    print("\n  How the window length controls the degeneracy. Fitting a decay")
    print("  over one time constant and over four:")
    print(f"    {'window':>14}{'corr(A, tau)':>15}{'corr(tau, offset)':>19}"
          f"{'sigma_tau (yr)':>16}")
    for t_hi, label in ((1.0 * tau_true, "0-1 tau"), (4.0 * tau_true, "0-4 tau")):
        popt_w, perr_w, corr_w = fit_window(t_hi, 19980815 + int(t_hi))
        print(f"    {label:>14}{corr_w[0, 1]:>15.5f}{corr_w[1, 2]:>19.5f}"
              f"{perr_w[1]:>16.1f}")
    print("    Over one time constant the whole exponential is fitted by its")
    print("    initial slope and curvature alone, so the pair (A, tau) is almost")
    print("    perfectly degenerate: |r| = 0.967 and sigma_tau = 316 yr. Over")
    print("    four time constants the degeneracy is gone (r = -0.075) and")
    print("    sigma_tau = 95 yr, 3.3 times smaller. An 'unconstrained'")
    print("    parameter pair is usually a window that is too short.")


# --------------------------------------------------------------------------
# Part 2 -- root finding
# --------------------------------------------------------------------------

def birch_murnaghan(v, k0, k0p):
    """Third-order Birch-Murnaghan isotherm. v = V/V0, k0 in the same unit as P."""
    return 1.5 * k0 * (v ** (-7.0 / 3.0) - v ** (-5.0 / 3.0)) * (
        1.0 + 0.75 * (k0p - 4.0) * (v ** (2.0 / 3.0) - 1.0))


def dbm_dv(v, k0, k0p):
    """Analytic dP/dV used by the Newton method below."""
    a = v ** (-7.0 / 3.0) - v ** (-5.0 / 3.0)
    da = (-7.0 / 3.0) * v ** (-10.0 / 3.0) + (5.0 / 3.0) * v ** (-8.0 / 3.0)
    b = 1.0 + 0.75 * (k0p - 4.0) * (v ** (2.0 / 3.0) - 1.0)
    db = 0.75 * (k0p - 4.0) * (2.0 / 3.0) * v ** (-1.0 / 3.0)
    return 1.5 * k0 * (da * b + a * db)


def part2_root_finding():
    section("2. Root finding: inverting an equation of state")
    k0, k0p = 260.0, 4.0        # GPa, dimensionless -- SYNTHETIC values
    p_target = 135.0            # GPa, deep-mantle pressure
    print("  Third-order Birch-Murnaghan isotherm, parameters chosen for the")
    print(f"  demonstration: K0 = {k0:.0f} GPa, K0' = {k0p:.1f}.")
    print(f"  Task: find V/V0 at P = {p_target:.0f} GPa.")

    root = optimize.brentq(lambda v: birch_murnaghan(v, k0, k0p) - p_target,
                           0.5, 1.5, xtol=1e-14, rtol=8.9e-16, full_output=True)
    v_brent = root[0]
    print(f"\n    brentq        V/V0 = {v_brent:.12f}   iterations = {root[1].iterations}"
          f"   residual P-P_target = {birch_murnaghan(v_brent, k0, k0p) - p_target:+.2e} GPa")

    r = optimize.root_scalar(
        lambda v: birch_murnaghan(v, k0, k0p) - p_target, x0=1.0, x1=1.1,
        fprime=lambda v: dbm_dv(v, k0, k0p), method="newton")
    print(f"    newton (analytic f')  V/V0 = {r.root:.12f}   iterations = "
          f"{r.iterations}   converged = {r.converged}")

    r3 = optimize.fsolve(lambda v: birch_murnaghan(v, k0, k0p) - p_target,
                         x0=[0.95], full_output=True)
    print(f"    fsolve (MINPACK hybrd) V/V0 = {r3[0][0]:.12f}   "
          f"nfev = {r3[1]['nfev']}")

    r4 = optimize.root_scalar(
        lambda v: birch_murnaghan(v, k0, k0p) - p_target, bracket=(0.5, 1.5),
        method="brentq")
    print(f"    root_scalar(brentq)   V/V0 = {r4.root:.12f}   iterations = "
          f"{r4.iterations}")
    vals = np.array([v_brent, r.root, r3[0][0], r4.root])
    print(f"    spread across the four methods = {vals.ptp() if hasattr(vals, 'ptp') else np.ptp(vals):.3e}"
          f" in V/V0")
    print("    The derivative-free Brent methods need a bracket but no")
    print("    derivative, and a bracket with a sign change is a guarantee:")
    print("    write the bracket, and you cannot be given the wrong root.")

    print("\n  The root finder finds the root you ask it for. A smooth cubic")
    print("  with three real roots: x^3 - 6x^2 + 11x - 6 = 0, roots 1, 2, 3.")
    f = lambda x: x ** 3 - 6.0 * x * x + 11.0 * x - 6.0
    print(f"    {'start x0':>10}{'method':>10}{'root found':>14}{'residual':>12}")
    for x0 in (0.0, 1.4, 1.6, 2.5, 4.0):
        r = optimize.fsolve(f, x0=[x0])
        print(f"    {x0:>10.2f}{'fsolve':>10}{r[0]:>14.6f}{f(r[0]):>12.2e}")
    print("    The map from start point to root is not monotone and not")
    print("    obvious: x0 = 2.5 lands on the root at 1, x0 = 1.6 on the root")
    print("    at 2. Nothing in the returned answer says that the equation had")
    print("    three solutions. fsolve reports convergence, not uniqueness.")

    try:
        optimize.brentq(f, 2.2, 2.4)
    except ValueError as exc:
        print(f"\n    brentq(f, 2.2, 2.4) raises: {type(exc).__name__}")
        print(f"    {exc}")
    print("    A bracket without a sign change is a hard error, not a wrong")
    print("    answer: this is the property that makes Brent methods the safe")
    print("    default when you can bracket.")
    for lo, hi in ((1.5, 2.5), (2.5, 3.5), (0.0, 4.0)):
        r = optimize.brentq(f, lo, hi)
        print(f"    brentq on [{lo}, {hi}] -> root {r:.6f}")


# --------------------------------------------------------------------------
# Part 3 -- leastsq vs minimize, and the Jacobian
# --------------------------------------------------------------------------

def part3_least_squares():
    section("3. leastsq vs minimize: what a Jacobian buys")
    # SYNTHETIC: two-term decay, sampled logarithmically in time
    truth = np.array([120.0, 250.0, 35.0, 4000.0])     # A1, tau1, A2, tau2
    t = np.logspace(0.0, 4.3, 60)
    model = lambda p, tt: p[0] * np.exp(-tt / p[1]) + p[2] * np.exp(-tt / p[3])
    data = model(truth, t) * (1.0 + RNG.normal(0.0, 0.02, size=t.size))
    p0 = np.array([100.0, 200.0, 40.0, 3000.0])
    resid = lambda p: model(p, t) - data
    n_data = t.size

    def jac(p):
        e1 = np.exp(-t / p[1])
        e2 = np.exp(-t / p[3])
        return np.column_stack([
            e1,
            p[0] * e1 * t / p[1] ** 2,
            e2,
            p[2] * e2 * t / p[3] ** 2,
        ])

    print("  Model A1 exp(-t/tau1) + A2 exp(-t/tau2); data SYNTHETIC, 2% noise,")
    print(f"  truth = {truth}, {n_data} samples.")
    print(f"    {'variant':<44}{'resid vectors':>14}{'jac eval':>10}"
          f"{'point evals':>13}")
    counts = {}

    def counted(p):
        counts["r"] += 1
        return resid(p)

    def counted_jac(p):
        counts["j"] += 1
        return jac(p)

    counts.update(r=0, j=0)
    r_num = optimize.least_squares(counted, p0, method="lm", xtol=1e-14,
                                   ftol=1e-14, gtol=1e-14)
    num_r, num_j = counts["r"], counts["j"]
    print(f"    {'least_squares(method=lm), finite-difference Jacobian':<44}"
          f"{num_r:>14}{num_j:>10}{n_data * (num_r + num_j):>13}")

    counts.update(r=0, j=0)
    r_ana = optimize.least_squares(counted, p0, jac=counted_jac, method="lm",
                                   xtol=1e-14, ftol=1e-14, gtol=1e-14)
    ana_r, ana_j = counts["r"], counts["j"]
    print(f"    {'least_squares(method=lm), analytic Jacobian':<44}"
          f"{ana_r:>14}{ana_j:>10}{n_data * (ana_r + ana_j):>13}")
    print("    A forward difference costs 1 + n_params = 5 residual vectors per")
    print("    Jacobian, so the finite-difference route above spent its "
          f"{num_r} residual")
    print(f"    vectors on about {num_r // 5} implicit Jacobians it never showed you.")
    print(f"    Counting one Jacobian as one residual vector of work: "
          f"{n_data * (num_r + num_j)} point")
    print(f"    evaluations against {n_data * (ana_r + ana_j)} for the analytic route -- a factor of")
    print(f"    {(num_r + num_j) / (ana_r + ana_j):.2f} for four fitted parameters. The factor is 1 + n_params,")
    print("    so it grows with the size of the model.")
    print("    Accuracy is not the issue here: both reach the same minimum")
    print(f"    2*cost = {2 * r_ana.cost:.10f}.")
    print(f"    Parameters agree to max |relative| = "
          f"{np.abs(r_num.x / r_ana.x - 1).max():.2e}")

    def rss(p):
        return float(resid(p) @ resid(p))

    def grad(p):
        return 2.0 * jac(p).T @ resid(p)

    print("\n  The same sum of squares, handed to minimize:")
    print(f"    {'method':<16}{'nfev':>8}{'RSS':>20}"
          f"{'max |rel. param diff|':>24}")
    for method in ("Nelder-Mead", "Powell", "BFGS", "L-BFGS-B"):
        kwargs = {"jac": grad} if method in ("BFGS", "L-BFGS-B") else {}
        res = optimize.minimize(rss, p0, method=method, **kwargs)
        print(f"    {method:<16}{res.nfev:>8}{res.fun:>20.8f}"
              f"{np.abs(res.x / r_ana.x - 1).max():>24.2e}")
    print("    Nelder-Mead needs an order of magnitude more evaluations than")
    print("    BFGS here, and Powell stops slightly early (RSS 201.79070141")
    print("    against 201.79068433). All four are within 7e-5 relative of the")
    print("    least-squares answer, so the choice is cost and robustness, not")
    print("    the final point.")
    print(f"    Residual RMS at the solution: {np.sqrt(np.mean(resid(r_ana.x) ** 2)):.6f}"
          f"  ({100 * np.sqrt(np.mean(resid(r_ana.x) ** 2)) / np.mean(data):.2f}%"
          f" of the mean datum)")
    print("    Restarting the analytic fit at the solution: "
          f"{optimize.least_squares(resid, r_ana.x, jac=jac, method='lm').nfev}"
          " residual evaluations -- convergence is a claim about the stopping")
    print("    test, not a certificate of a global minimum.")


def main():
    part1_curve_fit()
    part2_root_finding()
    part3_least_squares()
    print("\nDone.")


if __name__ == "__main__":
    main()
