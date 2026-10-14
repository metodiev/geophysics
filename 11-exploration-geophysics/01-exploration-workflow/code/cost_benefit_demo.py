#!/usr/bin/env python3
"""Cost, risk and value of information for an exploration decision.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python cost_benefit_demo.py

Everything here is SYNTHETIC.  The success value, failure cost, test quality,
test price and prior probability are chosen teaching values, not numbers from any
real project, contract or company report.

Contents
--------
1. Payoff structure and the break-even probability of a drill-or-walk decision.
2. Expected value of perfect information (EVPI): derived in closed form and
   verified against a brute-force sweep.
3. A geophysical test as a likelihood ratio: Bayes update and the posterior
   decision.
4. Expected value of sample information (EVSI) versus test quality; a useless
   test has exactly zero value.
5. The price of the test, the maximum price worth paying, and the optimal number
   of repeat tests.
6. Portfolio value and the effect of a shared failure mode.
7. Verification: Monte-Carlo check of the Bayesian posteriors and of EVSI.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC economics (MUSD) ---------------------------------------------
W_SUCCESS = 500.0      # net value of a discovery after all costs
K_FAILURE = 60.0       # sunk cost of a drilling program that fails
P_PRIOR = 0.15         # prior probability that a prospect is a deposit
TPR = 0.80             # test sensitivity: P(anomaly | deposit)
FPR = 0.20             # test false-positive rate: P(anomaly | barren)
TEST_COST = 3.0        # cost of one geophysical test (MUSD)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def value(p, w=W_SUCCESS, k=K_FAILURE):
    """Optimal expected value of the drill-or-walk decision at prior p.

    Drill:  p w - (1-p) k.   Walk: 0.   The optimal action is the larger.
    """
    return np.maximum(0.0, p * w - (1.0 - p) * k)


def evpi(p, w=W_SUCCESS, k=K_FAILURE):
    """EVPI with perfect information, closed form: min(p w, (1-p) k)."""
    return np.minimum(p * w, (1.0 - p) * k)


def evpi_bruteforce(p, w=W_SUCCESS, k=K_FAILURE):
    """EVPI by explicit enumeration of states and actions (no algebra)."""
    with_info = p * max(w, 0.0) + (1.0 - p) * max(-k, 0.0)
    return with_info - value(p, w, k)


def posterior(p, tpr=TPR, fpr=FPR):
    """Return (P(+), p_given_+, p_given_-) for a test with (tpr, fpr)."""
    p_plus = p * tpr + (1.0 - p) * fpr
    p_given_plus = p * tpr / p_plus
    p_given_minus = p * (1.0 - tpr) / (1.0 - p_plus)
    return p_plus, p_given_plus, p_given_minus


def evsi(p, tpr=TPR, fpr=FPR, w=W_SUCCESS, k=K_FAILURE):
    """Expected value of sample information for one test (before its cost)."""
    p_plus, p_pos, p_neg = posterior(p, tpr, fpr)
    return (p_plus * value(p_pos, w, k)
            + (1.0 - p_plus) * value(p_neg, w, k) - value(p, w, k))


def evsi_sequential(n, p, tpr=TPR, fpr=FPR, w=W_SUCCESS, k=K_FAILURE):
    """EVSI of n conditionally independent tests with the same quality.

    Each test is applied to the current posterior; a positive result stops the
    sequence (you act), a negative result continues.  This is an optimal
    stopping calculation, evaluated by backward induction on the posterior.
    """
    def recurse(pp, remaining):
        if remaining == 0:
            return value(pp, w, k)
        p_plus, p_pos, p_neg = posterior(pp, tpr, fpr)
        return p_plus * value(p_pos, w, k) + (1.0 - p_plus) * recurse(
            p_neg, remaining - 1)
    return recurse(p, n) - value(p, w, k)


def main():
    section("1. Payoff structure and the break-even probability")
    print(f"SYNTHETIC economics: success value W = {W_SUCCESS:.0f} MUSD, "
          f"failure cost K = {K_FAILURE:.0f} MUSD")
    print(f"prior probability of a deposit = {P_PRIOR:.2f}")
    p_star = K_FAILURE / (W_SUCCESS + K_FAILURE)
    print(f"\ndrill : EMV = p W - (1-p) K")
    print(f"walk  : EMV = 0")
    print(f"indifference when p W = (1-p) K  ->  p* = K/(W+K) = "
          f"{K_FAILURE:.0f}/{W_SUCCESS + K_FAILURE:.0f} = {p_star:.5f}")
    print(f"\n{'p':>7s} {'EMV drill':>11s} {'EMV walk':>9s} {'decision':>10s}")
    for p in (0.05, 0.10, p_star, 0.15, 0.25, 0.50):
        emv_d = p * W_SUCCESS - (1 - p) * K_FAILURE
        print(f"{p:7.3f} {emv_d:11.2f} {0.0:9.2f} "
              f"{'drill' if emv_d > 0 else 'walk':>10s}")
    print(f"\nat the prior p = {P_PRIOR:.2f} the decision is to drill, with "
          f"EMV = {value(P_PRIOR):.2f} MUSD")

    section("2. Expected value of perfect information (EVPI)")
    print("with perfect information you develop only if the prospect is a")
    print("deposit: value = p W.  Without it you take max(0, pW-(1-p)K).  So")
    print("   EVPI = pW - max(0, pW-(1-p)K) = min(pW, (1-p)K)")
    print(f"\n{'p':>7s} {'closed form':>12s} {'brute force':>12s} "
          f"{'difference':>12s}")
    for p in (0.02, 0.05, p_star, 0.15, 0.30, 0.50, 0.80):
        a = evpi(p)
        b = evpi_bruteforce(p)
        print(f"{p:7.3f} {a:12.3f} {b:12.3f} {abs(a - b):12.2e}")
    p_grid = np.linspace(1e-6, 1 - 1e-6, 200001)
    p_max_evpi = p_grid[np.argmax(evpi(p_grid))]
    print(f"\nEVPI peaks at p = {p_max_evpi:.5f}, i.e. exactly at the "
          f"indifference")
    print(f"probability p* = {p_star:.5f}.  Information is worth most where the")
    print(f"decision is uncertain; at p = 0.02 EVPI = {evpi(0.02):.2f} MUSD and at "
          f"p = 0.80 EVPI = {evpi(0.80):.2f} MUSD, both far below the peak")
    print(f"value of {evpi(p_star):.2f} MUSD.")

    section("3. A geophysical test as a likelihood ratio")
    print(f"SYNTHETIC test: sensitivity P(+|deposit) = {TPR:.2f}, "
          f"false-positive rate P(+|barren) = {FPR:.2f}")
    p_plus, p_pos, p_neg = posterior(P_PRIOR)
    print(f"P(+) = p TPR + (1-p) FPR = {P_PRIOR * TPR:.4f} + "
          f"{(1 - P_PRIOR) * FPR:.4f} = {p_plus:.4f}")
    print(f"posterior after + : p = {p_pos:.5f}  -> EMV drill = "
          f"{value(p_pos):.2f} MUSD, decision = "
          f"{'drill' if p_pos * W_SUCCESS > (1 - p_pos) * K_FAILURE else 'walk'}")
    print(f"posterior after - : p = {p_neg:.5f}  -> EMV drill = "
          f"{p_neg * W_SUCCESS - (1 - p_neg) * K_FAILURE:.2f} MUSD, "
          f"decision = "
          f"{'drill' if p_neg * W_SUCCESS > (1 - p_neg) * K_FAILURE else 'walk'}")
    print(f"\nprior decision: drill with EMV {value(P_PRIOR):.2f} MUSD")
    print(f"after + : drill with EMV {value(p_pos):.2f} MUSD")
    print(f"after - : walk  with EMV 0.00 MUSD")
    print("the test changes the ACTION in one branch, which is where its value")
    print("comes from.  A test that never changes an action has zero value,")
    print("however accurate it is.")

    section("4. EVSI versus test quality")
    print(f"EVSI = P(+) V(p+) + P(-) V(p-) - V(p), prior p = {P_PRIOR:.2f}")
    print(f"\n{'TPR':>6s} {'FPR':>6s} {'EVSI (MUSD)':>12s} {'net of cost':>12s}")
    for tpr, fpr in ((0.50, 0.50), (0.60, 0.50), (0.80, 0.20), (0.90, 0.10),
                     (0.95, 0.05), (0.99, 0.01)):
        s = evsi(P_PRIOR, tpr, fpr)
        print(f"{tpr:6.2f} {fpr:6.2f} {s:12.3f} {s - TEST_COST:12.3f}")
    print("\na test with TPR = FPR carries no information: the likelihood ratio")
    print("is 1 at both outcomes and the posterior equals the prior.")
    for tpr in (0.5, 0.7, 0.9):
        s = evsi(P_PRIOR, tpr, tpr)
        print(f"  TPR = FPR = {tpr:.1f}: EVSI = {s:.3e} MUSD "
              f"(numerically zero)")
    print(f"\nperfect information is worth EVPI = {evpi(P_PRIOR):.2f} MUSD;")
    ratio = evsi(P_PRIOR, TPR, FPR) / evpi(P_PRIOR)
    print(f"the test with TPR = {TPR:.2f}, FPR = {FPR:.2f} captures "
          f"{ratio * 100:.1f}% of that.")

    section("5. The price of the test and how many to run")
    print(f"maximum price worth paying for this test = EVSI = "
          f"{evsi(P_PRIOR):.3f} MUSD; the quoted price is {TEST_COST:.1f} MUSD")
    print(f"net expected gain of one test = "
          f"{evsi(P_PRIOR) - TEST_COST:.3f} MUSD")
    print(f"\n{'n tests':>8s} {'EVSI (MUSD)':>12s} {'net (MUSD)':>12s} "
          f"{'marginal (MUSD)':>16s}")
    prev = 0.0
    for n in range(1, 7):
        s = evsi_sequential(n, P_PRIOR)
        print(f"{n:8d} {s:12.3f} {s - n * TEST_COST:12.3f} "
              f"{s - prev - TEST_COST:16.3f}")
        prev = s
    nets = {n: evsi_sequential(n, P_PRIOR) - n * TEST_COST for n in range(1, 7)}
    n_opt = max(nets, key=nets.get)
    print(f"\noptimal number of repeat tests = {n_opt} of {TEST_COST:.1f} MUSD "
          f"each (net {nets[n_opt]:.3f} MUSD):")
    print("EVSI is bounded by EVPI and saturates quickly, while the cost is")
    print("linear, so the marginal test stops paying.  Repeating a test is also")
    print("not independent in reality; this calculation assumes it stays so.")

    section("6. Portfolio value and a shared failure mode")
    n_prospects = 20
    print(f"{n_prospects} independent prospects, prior p = {P_PRIOR:.2f} each")
    p_any = 1.0 - (1.0 - P_PRIOR) ** n_prospects
    print(f"E[deposits]          = {n_prospects * P_PRIOR:.2f}")
    print(f"P(at least one)      = {p_any:.4f}")
    print(f"E[value if drilled]  = {n_prospects * value(P_PRIOR):.1f} MUSD "
          f"(each at its own EMV)")
    print("\nnow let all prospects share ONE common failure mode: with")
    print("probability q the whole belt concept is wrong and then every prospect")
    print(f"{'q':>6s} {'P(any)':>9s} {'E[deposits]':>12s} "
          f"{'P(zero)':>9s}")
    for q in (0.0, 0.2, 0.4, 0.6):
        # belt works with prob (1-q); then each prospect is a deposit w.p. p
        p_any_q = (1.0 - q) * (1.0 - (1.0 - P_PRIOR) ** n_prospects)
        e_dep = (1.0 - q) * n_prospects * P_PRIOR
        print(f"{q:6.2f} {p_any_q:9.4f} {e_dep:12.2f} {1.0 - p_any_q:9.4f}")
    print("a shared failure mode lowers both the mean and, more sharply, the")
    print("chance of any success: the portfolio is not a diversification device")
    print("against a wrong regional concept.")

    section("6b. The flaw of averages: E[V(p)] is not V(E[p])")
    a_beta, b_beta = 1.8, 10.2      # Beta(1.8, 10.2): mean 0.15, SYNTHETIC
    grid = np.linspace(1e-9, 1 - 1e-9, 400001)
    dens = grid ** (a_beta - 1) * (1 - grid) ** (b_beta - 1)
    dens /= dens.sum()
    mean_p = float(np.sum(grid * dens))
    e_v = float(np.sum(value(grid) * dens))
    print(f"let the prior probability itself be uncertain: p ~ Beta({a_beta}, "
          f"{b_beta})")
    print(f"  E[p]                  = {mean_p:.6f}")
    print(f"  V(E[p])               = {value(mean_p):.4f} MUSD")
    print(f"  E[V(p)] by quadrature = {e_v:.4f} MUSD")
    print(f"  Jensen gap            = {e_v - value(mean_p):.4f} MUSD "
          f"({(e_v / value(mean_p) - 1) * 100:.2f}%)")
    print("V(p) = max(0, pW-(1-p)K) is convex in p, so E[V(p)] >= V(E[p]) with")
    print("equality only when p is certain.  A cost-benefit analysis that plugs a")
    print("single 'best-estimate' probability into a convex value function")
    print("systematically understates the expected value.")

    section("7. Verification")
    # (a) Monte-Carlo the two posteriors and P(+).
    n_mc = 400000
    is_dep = RNG.random(n_mc) < P_PRIOR
    anomaly = np.where(is_dep, RNG.random(n_mc) < TPR, RNG.random(n_mc) < FPR)
    p_plus_mc = anomaly.mean()
    p_pos_mc = is_dep[anomaly].mean()
    p_neg_mc = is_dep[~anomaly].mean()
    print(f"(a) Monte Carlo with {n_mc} prospects")
    print(f"    P(+)      analytic {p_plus:.6f}   simulated {p_plus_mc:.6f}")
    print(f"    p after + analytic {p_pos:.6f}   simulated {p_pos_mc:.6f}")
    print(f"    p after - analytic {p_neg:.6f}   simulated {p_neg_mc:.6f}")
    print(f"    standard error of a proportion ~ "
          f"{np.sqrt(p_pos * (1 - p_pos) / max(1, anomaly.sum())):.6f}")
    # (b) EVSI by direct enumeration over a fine p grid and a two-point test.
    p_pos_eps, p_neg_eps = p_pos, p_neg
    s_check = (p_plus * value(p_pos_eps) + (1 - p_plus) * value(p_neg_eps)
               - value(P_PRIOR))
    print(f"(b) EVSI analytic {evsi(P_PRIOR):.10f} vs re-evaluated from the "
          f"posteriors {s_check:.10f}")
    print(f"    difference = {abs(evsi(P_PRIOR) - s_check):.2e} MUSD")
    # (c) Brute-force enumeration of the n+1 distinct outcome classes of an
    #     n = 3 programme under the optimal stopping policy, against recursion.
    n_paths = 3
    total = 0.0
    print(f"(c) {n_paths}-test programme: the {n_paths + 1} distinct outcome "
          f"classes (stop at the first positive)")
    for k in range(n_paths):                 # k negatives, then a positive
        prob, pp = 1.0, P_PRIOR
        for _ in range(k):
            p_pl, _, p_m = posterior(pp)
            prob *= (1.0 - p_pl)
            pp = p_m
        p_pl, p_p, _ = posterior(pp)
        prob *= p_pl
        total += prob * value(p_p)
        print(f"    path {k} negative(s) then positive: probability "
              f"{prob:.6f}, posterior {p_p:.6f}, value {value(p_p):8.3f} MUSD")
    prob, pp = 1.0, P_PRIOR                # the all-negative path
    for _ in range(n_paths):
        p_pl, _, p_m = posterior(pp)
        prob *= (1.0 - p_pl)
        pp = p_m
    total += prob * value(pp)
    print(f"    all {n_paths} negative: probability {prob:.6f}, posterior "
          f"{pp:.6f}, value {value(pp):8.3f} MUSD")
    print(f"    enumerated E[value] = {total:.10f} MUSD")
    print(f"    backward recursion:  value(p) + EVSI(3) = "
          f"{value(P_PRIOR) + evsi_sequential(n_paths, P_PRIOR):.10f} MUSD")
    print(f"    difference = "
          f"{abs(total - value(P_PRIOR) - evsi_sequential(n_paths, P_PRIOR)):.2e}")
    # (d) The indifference identity that anchors the EVPI formula.
    print(f"(d) at the threshold p* = {p_star:.5f} the two branches of "
          f"min(pW,(1-p)K) agree:")
    print(f"    p*W = {p_star * W_SUCCESS:.6f} MUSD and "
          f"(1-p*)K = {(1 - p_star) * K_FAILURE:.6f} MUSD; EVPI = "
          f"{evpi(p_star):.6f} MUSD")
    print(f"    EMV at the threshold = {value(p_star):.3e} MUSD: the decision is")
    print("    exactly indifferent there, which is why EVPI peaks at p*.")


if __name__ == "__main__":
    main()
