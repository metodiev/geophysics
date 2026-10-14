#!/usr/bin/env python3
"""Decision-making under uncertainty and the value of information.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python decision_under_uncertainty_demo.py

All models and data in this demo are SYNTHETIC.  The resource volume, the prices,
the survey reliability and the hazard loss are chosen teaching values, and the
currency unit is dimensionless.

Contents
--------
1. A binary decision: drill or not, from a posterior on the resource volume.
2. The value of perfect information (EVPI), simulated and checked against the
   closed-form lognormal expectation.
3. The value of imperfect information (EVSI) from a survey, and its dependence on
   the assumed reliability.
4. Risk aversion: the exponential-utility certainty equivalent, and the risk
   tolerance at which the decision changes.
5. The cost-loss ratio: the value of information is largest when the decision
   threshold sits in the middle of the prior.
"""

import numpy as np
from scipy.stats import norm

RNG = np.random.default_rng(20261014)

LOG_MEDIAN = np.log(8.0)     # median volume 8 (volume units 10^6 m^3)
LOG_SD = 0.6                 # log-standard-deviation of the volume
PRICE = 5.0                  # value per unit volume
N_SIM = 4_000_000


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def e_positive_part(price, cost):
    """Exact E[max(0, price*V - cost)] for lognormal V (lognormal option value)."""
    mu, s = LOG_MEDIAN, LOG_SD
    k = cost / price
    d1 = (mu + s ** 2 - np.log(k)) / s
    d2 = d1 - s
    e_v = np.exp(mu + 0.5 * s ** 2)
    return price * (e_v * norm.cdf(d1) - k * norm.cdf(d2))


def draw_volume(n, seed):
    rng = np.random.default_rng(seed)
    return np.exp(LOG_MEDIAN + LOG_SD * rng.standard_normal(n))


def main():
    e_v = float(np.exp(LOG_MEDIAN + 0.5 * LOG_SD ** 2))
    v_star_20 = 20.0 / PRICE

    section("1. The decision and the volume threshold")
    print("SYNTHETIC posterior on recoverable volume V: lognormal")
    print(f"  median {np.exp(LOG_MEDIAN):.2f}, log-sd {LOG_SD:.2f} "
          f"(volume units 10^6 m^3)")
    print(f"  E[V] = exp(mu + sigma^2/2) = {e_v:.4f} volume units")
    print(f"  value per unit {PRICE:.2f} currency units")
    print(f"  break-even volume V* = cost / price")
    print("   cost   EV(drill) = price E[V] - cost    optimal action   P(V > V*)")
    print("   " + "-" * 68)
    for cost in (20.0, 40.0, 48.0):
        ev_drill = PRICE * e_v - cost
        p_exceed = float(norm.sf((np.log(cost / PRICE) - LOG_MEDIAN) / LOG_SD))
        action = "drill" if ev_drill > 0 else "do not drill"
        print(f"  {cost:5.1f}   {ev_drill:+27.4f}   {action:15s}   {p_exceed:9.4f}")
    print("The decision depends only on the sign of the expected net value. Note")
    print("that at cost 48 the decision is 'do not drill' even though P(V > V*) =")
    print(f"{float(norm.sf((np.log(48.0 / PRICE) - LOG_MEDIAN) / LOG_SD)):.4f}: the mean, "
          f"not the exceedance probability, prices the project.")

    section("2. Value of perfect information, two ways")
    v = draw_volume(N_SIM, 2)
    print(f"  {N_SIM:,} draws; simulated E[V] = {v.mean():.4f} (exact {e_v:.4f})")
    print("   cost    EV no info    E[max(0,value)] sim   EVPI sim   EVPI exact"
          "   difference")
    print("   " + "-" * 84)
    for cost in (20.0, 40.0, 48.0):
        ev_act = max(0.0, PRICE * e_v - cost)
        ev_pos_sim = float(np.mean(np.maximum(0.0, PRICE * v - cost)))
        evpi_sim = ev_pos_sim - ev_act
        evpi_exact = e_positive_part(PRICE, cost) - ev_act
        print(f"  {cost:5.1f}   {ev_act:9.4f}   {ev_pos_sim:19.4f}   "
              f"{evpi_sim:8.4f}   {evpi_exact:10.4f}   "
              f"{abs(evpi_sim - evpi_exact):10.4f}")
    print("The closed form is the lognormal option value")
    print("  E[max(0, P V - C)] = P [ E[V] Phi(d1) - (C/P) Phi(d2) ],")
    print("  d1 = (mu + sigma^2 - ln(C/P))/sigma,  d2 = d1 - sigma,")
    print("and the simulation reproduces it to within its own Monte Carlo error.")
    print("EVPI rises as the decision becomes marginal: 0.58 at cost 20, 6.87 at")
    print("cost 40 and 11.25 at cost 48, where the decision is nearly indifferent.")
    print("Information is worth most where it could change the action, which is not")
    print("where the resource is largest.")

    section("3. Value of imperfect information from a survey")
    v = draw_volume(N_SIM, 5)
    v_ind = 10.0                       # the size the survey is sensitive to
    print("  survey: a binary indicator with sensitivity p(signal | V > V_ind) and")
    print(f"  specificity p(no signal | V <= V_ind), with V_ind = {v_ind:.1f} volume")
    print("  units. The survey measures field size; whether that is worth anything")
    print("  depends on the decision it is supposed to inform, so both the clear")
    print(f"  decision (cost 20, break-even V* = {20.0 / PRICE:.1f}) and the marginal")
    print(f"  decision (cost 48, break-even V* = {48.0 / PRICE:.1f}) are shown.")
    print(f"  P(V > V_ind) = {float(norm.sf((np.log(v_ind) - LOG_MEDIAN) / LOG_SD)):.4f}")
    for cost in (20.0, 48.0):
        print(f"    cost {cost:.1f}: EV(drill) without information = "
              f"{max(0.0, PRICE * v.mean() - cost):.4f}")
    print("   p_sens   p_spec   P(signal)   E[V | signal]   E[V | no signal]"
          "   EVSI (cost 20)   EVSI (cost 48)")
    print("   " + "-" * 96)
    for p_sens, p_spec in ((0.9, 0.9), (0.8, 0.8), (0.7, 0.7), (0.55, 0.55)):
        rng = np.random.default_rng(7)
        above = v > v_ind
        hit = rng.random(N_SIM) < np.where(above, p_sens, 1.0 - p_spec)
        p_signal = float(hit.mean())
        # Within the subset {signal}, the empirical distribution of V is already
        # proportional to p(V) p(signal | V): no reweighting is needed.
        e_sig = float(v[hit].mean())
        e_nosig = float(v[~hit].mean())
        evsi = []
        for cost in (20.0, 48.0):
            ev_act = max(0.0, PRICE * v.mean() - cost)
            ev_info = p_signal * max(0.0, PRICE * e_sig - cost) \
                + (1.0 - p_signal) * max(0.0, PRICE * e_nosig - cost)
            evsi.append(ev_info - ev_act)
        print(f"   {p_sens:6.2f}   {p_spec:6.2f}   {p_signal:10.4f}   "
              f"{e_sig:14.4f}   {e_nosig:15.4f}   {evsi[0]:15.4f}   {evsi[1]:15.4f}")
    evpi_20 = e_positive_part(PRICE, 20.0) - max(0.0, PRICE * v.mean() - 20.0)
    evpi_48 = e_positive_part(PRICE, 48.0) - max(0.0, PRICE * v.mean() - 48.0)
    print(f"   {1.0:6.2f}   {1.0:6.2f}   "
          f"{float(norm.sf((np.log(v_ind) - LOG_MEDIAN) / LOG_SD)):10.4f}   "
          f"{'-':>14s}   {'-':>15s}   {evpi_20:15.4f}   {evpi_48:15.4f}"
          f"   (perfect: EVSI = EVPI)")
    print("Two results follow directly from the table.")
    print("First, the same survey is worth NOTHING at cost 20 and several units at")
    print("cost 48. At cost 20 the decision is to drill whatever the signal says,")
    print("so better information cannot change the action and has no value. At cost")
    print("48 the decision is marginal, and the signal flips it: for"
          " p_sens = p_spec = 0.8 a positive signal")
    print(f"gives E[V] = 12.84, above the break-even 9.6, while a negative signal")
    print("leaves E[V] = 7.27 below it; the difference is the EVSI.")
    print("Second, the perfect-sensor row reproduces the closed-form EVPI of")
    print("Section 2. It is computed analytically rather than by simulation, because")
    print("with p = 1 the 'no signal' subset is empty and a simulated value is")
    print("undefined.")
    print("A survey also has a cost, and the acquisition decision compares the EVSI")
    print("with that cost; the comparison, not the EVSI alone, is the business case.")

    section("4. Risk aversion changes the decision")
    print("  utility U(x) = -exp(-A x), A the absolute risk aversion;")
    print("  the certainty equivalent is CE = -ln(E[exp(-A x)])/A")
    payoff = PRICE * v - 20.0
    print("     A (per currency unit)      CE of drilling     decision")
    print("   " + "-" * 58)
    for A in (0.0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.3):
        if A == 0.0:
            ce = float(payoff.mean())
        else:
            m = float(np.max(-A * payoff))
            ce = float(-np.log(np.mean(np.exp(-A * payoff - m))) / A - m / A)
        print(f"   {A:20.3f}   {ce:15.4f}      "
              f"{'drill' if ce > 0 else 'do not drill'}")
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        m = float(np.max(-mid * payoff))
        ce = -np.log(np.mean(np.exp(-mid * payoff - m))) / mid - m / mid
        if ce > 0:
            lo = mid
        else:
            hi = mid
    a_crit = 0.5 * (lo + hi)
    print(f"  the decision flips at A = {a_crit:.5f} per currency unit, a risk")
    print(f"  tolerance of 1/A = {1 / a_crit:.3f} currency units")
    print("The expected value is positive, but the downside is a certain loss of")
    print("the drilling cost. A decision maker averse enough to that loss declines a")
    print("positive-expected-value project; that is a preference, not an error.")
    print("Which of the two rules is used must be stated, because it changes the")
    print("action.")

    section("5. Cost-loss ratio: where information is worth the most")
    L = 50.0
    p = np.linspace(0.0, 1.0, 100_001)
    dp = p[1] - p[0]
    print("  protection decision: cost C to protect, loss L if the hazard occurs.")
    print("  Protect when the probability p exceeds C/L: the cost-loss ratio.")
    print("  Prior: p is completely unknown, modelled as uniform on [0, 1].")
    print("  Expected cost without information uses the prior mean; with perfect")
    print("  information it averages min(C, p L) over the prior.")
    print(f"  loss L = {L:.1f} throughout.")
    print("     C     C/L     E[cost] no info   E[cost] perfect info   "
          "value of information")
    print("   " + "-" * 84)
    for C in (5.0, 12.5, 25.0, 37.5, 45.0):
        no_info = min(C, 0.5 * L)
        with_info = float(np.sum(np.minimum(C, p * L)) * dp)
        print(f"  {C:5.1f}   {C / L:5.3f}   {no_info:15.4f}   {with_info:20.4f}   "
              f"{no_info - with_info:20.4f}")
    print("The value of information is largest when C = L/2 = 25.0, i.e. when the")
    print("decision threshold sits in the middle of the range the prior admits, and")
    print("smallest when it sits at either end where the action is nearly certain")
    print("whatever the truth is. The value of information is therefore a property")
    print("of the decision, the loss function and the prior, not of the data alone.")


if __name__ == "__main__":
    main()
