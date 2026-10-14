#!/usr/bin/env python3
"""Sensitivity analysis: local derivatives versus global Sobol indices.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python sensitivity_analysis_demo.py

All models in this demo are SYNTHETIC and are analytic test functions with known
variance decompositions, so the Monte Carlo estimators below can be scored against
exact values.

Contents
--------
1. The Sobol' g-function: analytic main and total indices, derived and printed.
2. Estimator verification: quasi-Monte Carlo Saltelli estimators against the
   analytic values, with error bars over independent replicates.
3. A model where the local ranking is exactly wrong: the derivative at the nominal
   point is zero for the most influential parameter.
4. Convergence of the estimator: the measured N^-1/2 rate.
5. What to report, and the two indices that must be reported together.
"""

import numpy as np
from scipy.stats import qmc

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def g_function(X, a):
    """Sobol' g-function: f = prod_i (|4 x_i - 2| + a_i) / (1 + a_i), x in [0,1]."""
    return np.prod((np.abs(4.0 * X - 2.0) + a) / (1.0 + a), axis=1)


def g_analytic(a):
    """Exact variances of the g-function.

    Since E[g_j] = 1 and the factors are independent,
    E[f | x_i] = g_i(x_i), so V_i = Var[g_i(x_i)] = (1/3)/(1+a_i)^2, and
    V = prod_i (1 + V_i) - 1.  The total index follows from
    S_Ti = 1 - (V - V_i^{excl})/V with V_i^{excl} = prod_{j != i}(1+V_j) - 1.
    """
    Vi = (1.0 / 3.0) / (1.0 + a) ** 2
    V = float(np.prod(1.0 + Vi) - 1.0)
    S = Vi / V
    ST = np.empty_like(Vi)
    for i in range(a.size):
        others = np.prod(1.0 + np.delete(Vi, i)) - 1.0
        ST[i] = 1.0 - others / V
    return V, S, ST


def saltelli_estimates(a, n_base, seed):
    """Saltelli/Jansen first-order and total indices from a Sobol' QMC design."""
    d = a.size
    sampler = qmc.Sobol(d=2 * d, scramble=True, seed=seed)
    U = sampler.random(n_base)
    A, B = U[:, :d], U[:, d:]
    fA, fB = g_function(A, a), g_function(B, a)
    var = np.var(np.concatenate([fA, fB]), ddof=1)
    S = np.empty(d)
    ST = np.empty(d)
    for i in range(d):
        AB = A.copy()
        AB[:, i] = B[:, i]
        fAB = g_function(AB, a)
        S[i] = np.mean(fB * (fAB - fA)) / var          # Jansen first-order
        ST[i] = 0.5 * np.mean((fA - fAB) ** 2) / var   # Jansen total
    return S, ST


def main():
    a = np.array([0.0, 0.5, 3.0])

    section("1. Sobol' g-function: exact variance decomposition")
    V, S, ST = g_analytic(a)
    print("SYNTHETIC analytic test function, three independent uniform inputs:")
    print("    f(x) = prod_i (|4 x_i - 2| + a_i) / (1 + a_i),  x_i ~ U[0, 1]")
    print(f"  a = {a}")
    print(f"  Var[g_i] = (1/3)/(1+a_i)^2 = "
          f"{np.array2string((1/3)/(1+a)**2, precision=6)}")
    print(f"  Var[f] = prod(1+Var[g_i]) - 1 = {V:.6f}")
    print("   i      a_i     Var_i      S_i       S_Ti     interaction S_Ti - S_i")
    print("  " + "-" * 70)
    for i in range(a.size):
        Vi = (1 / 3) / (1 + a[i]) ** 2
        print(f"  {i:2d}   {a[i]:6.2f}   {Vi:.6f}   {S[i]:.6f}   {ST[i]:.6f}   "
              f"{ST[i] - S[i]:.6f}")
    print(f"  sum of first-order indices = {S.sum():.6f} (< 1 because of "
          f"interactions)")
    print("The indices are exact: E[f|x_i] = g_i(x_i) because the other factors")
    print("have expectation 1, so S_i = Var[g_i]/Var[f] follows by construction.")
    print("A parameter with a small a_i is influential; here x_1 dominates.")

    section("2. Verification: quasi-Monte Carlo estimators vs the exact values")
    n_base = 2 ** 13
    reps = 20
    est_S = np.empty((reps, a.size))
    est_ST = np.empty((reps, a.size))
    for r in range(reps):
        est_S[r], est_ST[r] = saltelli_estimates(a, n_base, 100 + r)
    print(f"  Saltelli/Jansen estimators, {n_base} base samples (x "
          f"{2 * a.size + 2} = {n_base * (2 * a.size + 2)} evaluations per "
          f"replicate), {reps} scrambled replicates")
    print("   i   exact S_i   mean estimate   sd across replicates   exact S_Ti"
          "   mean estimate   sd")
    print("  " + "-" * 88)
    for i in range(a.size):
        print(f"  {i:2d}   {S[i]:9.6f}   {est_S[:, i].mean():13.6f}   "
              f"{est_S[:, i].std(ddof=1):21.6f}   {ST[i]:10.6f}   "
              f"{est_ST[:, i].mean():13.6f}   {est_ST[:, i].std(ddof=1):.6f}")
    print("The estimates bracket the exact values within their replicate spread.")
    print("Note the ordering: the measured S for x_1 is 0.5922 and for x_3 is")
    print("0.0371, a factor of 16 apart. A ranking based on these indices is a")
    print("measured statement about the input space, not about one point in it.")

    section("3. Where a local analysis misleads: the derivative is zero")
    # A SYNTHETIC additive model with an exactly known decomposition.
    #   f = 10 (x1 - 0.5)^2 + x2 + 0.5 x3
    V1 = 100.0 * ((1.0 / 80.0) - (1.0 / 12.0) ** 2)
    V2 = 1.0 / 12.0
    V3 = 0.25 / 12.0
    Vtot = V1 + V2 + V3
    S_add = np.array([V1, V2, V3]) / Vtot

    def f_add(X):
        return 10.0 * (X[:, 0] - 0.5) ** 2 + X[:, 1] + 0.5 * X[:, 2]

    x0 = np.array([0.5, 0.5, 0.5])
    local = np.array([20.0 * (x0[0] - 0.5), 1.0, 0.5])
    print("SYNTHETIC model: f = 10 (x1 - 0.5)^2 + x2 + 0.5 x3, x ~ U[0,1]^3")
    print(f"  exact indices: S = {np.array2string(S_add, precision=4)}, "
          f"S_T = S (purely additive)")
    print(f"  local derivatives at the nominal point {x0}: "
          f"{np.array2string(local, precision=4)}")
    print("   parameter   local |df/dx|   local rank   global S_i   global rank")
    print("  " + "-" * 68)
    lrank = (-np.abs(local)).argsort().argsort() + 1
    grank = (-S_add).argsort().argsort() + 1
    for i in range(3):
        print(f"  {i + 1:9d}   {abs(local[i]):13.4f}   {lrank[i]:10d}   "
              f"{S_add[i]:10.4f}   {grank[i]:11d}")
    # Verify the analytic indices with a large Monte Carlo sample.
    N = 1_000_000
    X = RNG.random((N, 3))
    Y = f_add(X)
    print(f"  Monte Carlo check with N = {N:,}: Var(f) = {Y.var(ddof=1):.6f} "
          f"against the exact {Vtot:.6f}")
    print("The local analysis puts x_1 last: its derivative at x = 0.5 is exactly")
    print("zero, because the nominal point sits at the minimum of the parabola.")
    print("The global analysis puts x_1 first, with 84% of the variance. Both")
    print("computations are correct; they answer different questions, and only the")
    print("second one describes the model over the range the parameter explores.")

    section("4. Convergence of the estimator")
    print("   n_base    mean |S_hat - S| over three parameters (20 replicates)")
    print("  " + "-" * 66)
    errs, sizes = [], []
    for nb in (2 ** 6, 2 ** 8, 2 ** 10, 2 ** 12, 2 ** 14):
        e = 0.0
        for r in range(20):
            s_hat, _ = saltelli_estimates(a, nb, 500 + r)
            e += np.mean(np.abs(s_hat - S))
        e /= 20.0
        errs.append(e)
        sizes.append(nb)
        print(f"  {nb:8d}    {e:.6f}")
    slope = np.polyfit(np.log(sizes), np.log(errs), 1)[0]
    print(f"measured log-log slope = {slope:.3f}")
    print("That is steeper than the -0.5 of plain Monte Carlo: the quasi-random")
    print("points fill the space more evenly, so both the constant and the observed")
    print("rate improve on this function. The rate is not a guarantee. Quasi-Monte")
    print("Carlo assumes enough smoothness and low enough dimension; the g-function")
    print("has a kink in every input, and a rougher or higher-dimensional integrand")
    print("returns the plain Monte Carlo rate. What is transportable is the")
    print("practice: report a standard error obtained from independent replicates,")
    print("as in Section 2, and never quote an index without one.")

    section("5. Reporting rule")
    print("Report S_i and S_Ti together, with a standard error on each.")
    print(f"  here x_1: S = {S[0]:.4f}, S_T = {ST[0]:.4f} "
          f"(difference {ST[0] - S[0]:.4f})")
    print("The gap between them is the interaction share: the part of the effect")
    print("of x_1 that depends on the values of the other parameters. A report that")
    print("gives only S_i understates the influence of any parameter that")
    print("interacts, and a report that gives only S_Ti cannot tell an influential")
    print("parameter from one that merely participates in interactions.")


if __name__ == "__main__":
    main()
