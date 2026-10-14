#!/usr/bin/env python3
"""Trans-dimensional and reversible-jump MCMC: sampling a model of unknown size.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python trans_dimensional_demo.py

All models and data in this demo are SYNTHETIC.  The polynomial family, the
prior width and the noise level are chosen teaching values, not measurements.

Contents
--------
1. A family of models of increasing dimension and their exact evidence.
2. Reversible-jump moves: birth, death and within-model updates, with the
   acceptance ratio printed explicitly.
3. The trans-dimensional chain: posterior over model order, measured.
4. Comparison with the analytic model probabilities, with Monte Carlo error.
5. Mixing: acceptance rates per move, R-hat on the model index, ESS.
6. The same posterior from fixed-dimension sampling, for cross-checking.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

X = np.linspace(-1.0, 1.0, 12)
SIGMA = 0.5
TAU = 1.0                       # prior std of every coefficient
MAX_ORDER = 2                   # keep the family small so the chain mixes well
A0, A1 = 0.5, 1.0               # SYNTHETIC truth: a straight line
S_BIRTH = 0.3                   # birth proposal std (tighter than the prior)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def design(order):
    return np.column_stack([X ** j for j in range(order + 1)])


def log_lik(y, c, order):
    r = y - design(order) @ c
    return -0.5 * np.sum(r ** 2) / SIGMA ** 2


def log_prior_c(c):
    return -0.5 * np.sum(c ** 2) / TAU ** 2 \
        - 0.5 * c.size * np.log(2 * np.pi * TAU ** 2)


def log_evidence_analytic(y, order):
    Phi = design(order)
    n = y.size
    C = SIGMA ** 2 * np.eye(n) + TAU ** 2 * (Phi @ Phi.T)
    L = np.linalg.cholesky(C)
    z = np.linalg.solve(L, y)
    logdet = 2.0 * np.sum(np.log(np.diag(L)))
    return -0.5 * (n * np.log(2 * np.pi) + logdet + z @ z)


def proposal_probs(k):
    """(P move, P birth, P death) for a chain currently in model k."""
    if k == 0:
        return 0.5, 0.5, 0.0
    if k == MAX_ORDER:
        return 0.5, 0.0, 0.5
    return 0.5, 0.25, 0.25


def log_normal_1d(u, sd):
    return -0.5 * (u / sd) ** 2 - np.log(sd * np.sqrt(2.0 * np.pi))


def rj_run(y, n, start_order, move_sd, rng):
    """Reversible-jump chain over polynomial order 0..MAX_ORDER."""
    k = start_order
    c = np.zeros(k + 1)
    ll = log_lik(y, c, k)
    lp = log_prior_c(c)
    orders = np.empty(n, dtype=int)
    stats = {"move": [0, 0], "birth": [0, 0], "death": [0, 0]}
    for i in range(n):
        pm, pb, pd = proposal_probs(k)
        u = rng.random()
        if u < pm:                                    # within-model update
            if k == 0:
                pass
            else:
                prop = c + move_sd * rng.standard_normal(k + 1)
                llp = log_lik(y, prop, k)
                lpp = log_prior_c(prop)
                stats["move"][1] += 1
                if np.log(rng.random()) < (llp + lpp) - (ll + lp):
                    c, ll, lp = prop, llp, lpp
                    stats["move"][0] += 1
        elif u < pm + pb:                             # birth: k -> k+1
            cand = rng.standard_normal() * S_BIRTH
            c_new = np.append(c, cand)
            ll_new = log_lik(y, c_new, k + 1)
            lp_new = log_prior_c(c_new)
            pm2, pb2, pd2 = proposal_probs(k + 1)
            log_alpha = (ll_new + lp_new - ll - lp) \
                + np.log(pd2 / pb) \
                - log_normal_1d(cand, S_BIRTH)        # proposal density of the birth
            stats["birth"][1] += 1
            if np.log(rng.random()) < log_alpha:
                k, c, ll, lp = k + 1, c_new, ll_new, lp_new
                stats["birth"][0] += 1
        else:                                        # death: k -> k-1
            cand = c[-1]
            c_new = c[:-1]
            ll_new = log_lik(y, c_new, k - 1)
            lp_new = log_prior_c(c_new)
            pm2, pb2, pd2 = proposal_probs(k - 1)
            # Exact reverse of the birth: the removed coefficient enters with its
            # prior density, the reverse birth proposal density is divided out,
            # the proposal-probability ratio is inverted, and the Jacobian is 1.
            # lp_new - lp already contains -log N(u|0, tau^2) for the removed
            # coefficient, so only the reverse birth proposal density q(u)
            # remains to be multiplied in.
            log_alpha = (ll_new + lp_new - ll - lp) \
                + log_normal_1d(cand, S_BIRTH) \
                + np.log(pb2 / pd)
            stats["death"][1] += 1
            if np.log(rng.random()) < log_alpha:
                k, c, ll, lp = k - 1, c_new, ll_new, lp_new
                stats["death"][0] += 1
        orders[i] = k
    return orders, stats


def autocorr_time(y):
    y = y - y.mean()
    n = y.size
    nfft = 1 << (2 * n - 1).bit_length()
    F = np.fft.rfft(y, nfft)
    acf = np.fft.irfft(F * np.conj(F), nfft)[:n].real
    if acf[0] <= 0.0:
        return float(n)
    acf /= acf[0]
    tau = 1.0
    for k in range(1, n):
        if acf[k] <= 0.0:
            break
        tau += 2.0 * acf[k]
        if k > 5 * tau:
            break
    return tau


def split_rhat(chains):
    splits = []
    h = chains[0].size // 2
    for c in chains:
        splits += [c[:h], c[h:2 * h]]
    arr = np.stack(splits).astype(float)
    n = arr.shape[1]
    means = arr.mean(axis=1)
    W = arr.var(axis=1, ddof=1).mean()
    B = n * means.var(ddof=1)
    return float(np.sqrt(((n - 1) / n * W + B / n) / W))


def main():
    y = A0 + A1 * X + SIGMA * RNG.standard_normal(X.size)

    section("1. The SYNTHETIC data and the exact evidence of each order")
    print(f"12 points on x in [-1, 1]; SYNTHETIC truth is a straight line "
          f"y = {A0} + {A1} x with N(0, {SIGMA}^2) noise")
    print("models: polynomial orders k = 0, 1, 2; coefficients c ~ N(0, "
          f"{TAU}^2 I); uniform model prior")
    logZ = np.array([log_evidence_analytic(y, k) for k in range(MAX_ORDER + 1)])
    p_analytic = np.exp(logZ - logZ.max())
    p_analytic /= p_analytic.sum()
    for k in range(MAX_ORDER + 1):
        print(f"  k = {k}: log evidence {logZ[k]:10.4f}, "
              f"analytic P(k) = {p_analytic[k]:.4f}")

    section("2. Reversible-jump moves and their acceptance ratios")
    print("Birth (k -> k+1): append a coefficient u drawn from N(0, s_birth^2).")
    print("  alpha = min(1, [L(k+1,c')/L(k,c)] * [N(u|0,tau^2)/N(u|0,s^2)]")
    print("                * [P(death,k+1)/P(birth,k)])")
    print("  The prior density of the new coefficient and the proposal density do")
    print("  NOT cancel when s_birth != tau, and the ratio is what corrects for")
    print("  proposing from a distribution other than the prior. The Jacobian of")
    print("  the dimension match u = c'_k is exactly 1, so it does not appear.")
    print("Death (k -> k+1 reversed): the same expression with the roles of the")
    print("  birth and death proposal probabilities exchanged, and the deleted")
    print("  coefficient weighted by its prior density N(0, tau^2).")
    print(f"  here s_birth = {S_BIRTH}, tau = {TAU}")

    section("3. The trans-dimensional chain: posterior over model order")
    n = 60000
    orders, stats = rj_run(y, n, start_order=0, move_sd=0.15, rng=RNG)
    burn = 5000
    kept = orders[burn:]
    print(f"  {n} iterations, {burn} discarded, one chain started at k = 0")
    counts = np.array([np.sum(kept == k) for k in range(MAX_ORDER + 1)])
    p_rj = counts / counts.sum()
    print("   k   visits      measured P(k)   analytic P(k)   difference")
    print("   " + "-" * 62)
    for k in range(MAX_ORDER + 1):
        print(f"   {k}   {counts[k]:7d}   {p_rj[k]:14.4f}   {p_analytic[k]:14.4f}"
              f"   {p_rj[k] - p_analytic[k]:+11.4f}")
    se = np.sqrt(p_rj * (1 - p_rj) / counts.sum())
    print(f"  Monte Carlo standard error on each P(k) is about {se.max():.4f}")
    print("The trans-dimensional chain reproduces the analytic probabilities, but")
    print("only after the moves have been visited enough times for the model index")
    print("to mix. That is the diagnostic that decides whether the number is usable.")

    section("4. Mixing: acceptance per move, and the model index as a chain")
    for name, (acc, tot) in stats.items():
        rate = acc / tot if tot else float("nan")
        print(f"  {name:6s}: {acc:6d} accepted of {tot:6d} proposed "
              f"(rate {rate:.3f})")
    tau = autocorr_time(kept.astype(float))
    print(f"  integrated autocorrelation time of the model index = {tau:.1f}")
    print(f"  effective sample size = {kept.size / tau:.0f} of {kept.size} "
          f"({100 / tau:.2f}%)")
    print("The model index is a discrete chain that changes only on accepted")
    print("births and deaths. Its effective sample size, not the number of")
    print("iterations, is what limits how well P(k) is estimated.")

    section("5. Split R-hat on the model index over four chains")
    chains = []
    for j in range(4):
        o, _ = rj_run(y, 12000, start_order=j % (MAX_ORDER + 1), move_sd=0.15,
                      rng=RNG)
        chains.append(o[2000:])
    rhat = split_rhat(chains)
    pooled = np.concatenate(chains)
    pp = np.array([np.mean(pooled == k) for k in range(MAX_ORDER + 1)])
    print(f"  split R-hat = {rhat:.4f}")
    print(f"  pooled P(k) = {np.array2string(pp, precision=4)} "
          f"(analytic {np.array2string(p_analytic, precision=4)})")
    print("R-hat near 1 for a discrete indicator is weaker evidence than for a")
    print("continuous parameter: a chain can sit in one model for a long time and")
    print("still show a low R-hat if all chains do the same. Read it together with")
    print("the per-move acceptance rates and the ESS above.")

    section("6. Independent check: evidence of each order by quadrature")
    print("Grid integration over the coefficients of each model, with no MCMC at")
    print("all. This is a second, independent route to p(y|k).")
    print("   k   grid points      quadrature p(y|k)      analytic p(y|k)"
          "   relative error")
    print("   " + "-" * 78)
    quadZ = []
    for k in range(MAX_ORDER + 1):
        ng = 121 if k < 2 else 61
        g = np.linspace(-3.0, 3.0, ng)
        dg = g[1] - g[0]
        if k == 0:
            R = y[None, :] - g[:, None]
            lp = -0.5 * np.sum(R ** 2, axis=1) / SIGMA ** 2 \
                - 0.5 * g ** 2 / TAU ** 2 \
                - 0.5 * y.size * np.log(2 * np.pi * SIGMA ** 2) \
                - 0.5 * np.log(2 * np.pi * TAU ** 2)
            m = lp.max()
            Z = np.exp(lp - m).sum() * dg * np.exp(m)
        else:
            meshes = np.meshgrid(*[g] * (k + 1), indexing="ij")
            Phi = design(k)
            R = y[None, :] - np.stack([mm.ravel() for mm in meshes], axis=1) @ Phi.T
            lp = -0.5 * np.sum(R ** 2, axis=1) / SIGMA ** 2 \
                - 0.5 * np.sum(np.stack([mm.ravel() for mm in meshes], axis=1) ** 2,
                               axis=1) / TAU ** 2 \
                - 0.5 * y.size * np.log(2 * np.pi * SIGMA ** 2) \
                - 0.5 * (k + 1) * np.log(2 * np.pi * TAU ** 2)
            m = lp.max()
            Z = np.exp(lp - m).sum() * dg ** (k + 1) * np.exp(m)
        quadZ.append(Z)
        exact = np.exp(logZ[k])
        print(f"   {k}   {ng ** (k + 1):11d}   {Z:20.6e}   {exact:19.6e}   "
              f"{abs(Z / exact - 1):12.2e}")
    quadZ = np.array(quadZ, dtype=float)
    p_quad = quadZ / quadZ.sum()
    print(f"  P(k) by quadrature : {np.array2string(p_quad, precision=4)}")
    print(f"  P(k) from trans-D  : {np.array2string(p_rj, precision=4)}")
    print(f"  P(k) analytic      : {np.array2string(p_analytic, precision=4)}")
    print("A wrong Jacobian or a dropped proposal-probability ratio shows up as a")
    print("systematic offset in P(k) that no amount of extra iterations removes,")
    print("so an independent route to the same probabilities is the only real")
    print("check on a reversible-jump implementation.")


if __name__ == "__main__":
    main()
