#!/usr/bin/env python3
"""Event attribution: probability ratio, fraction of attributable risk, their
uncertainty from a finite ensemble, the sensitivity to the event threshold, and
why thermodynamic and dynamical contributions do not add.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python event_attribution_demo.py

Everything is SYNTHETIC.  The "factual" and "counterfactual" ensembles are draws
from chosen normal distributions of a made-up daily maximum temperature.  No real
event, station, model ensemble or published attribution result is used.

Contents
--------
1. The two ensembles, the event definition, and exact tail probabilities.
2. Finite-ensemble estimates with Wilson intervals, and the bootstrap interval
   for the fraction of attributable risk.
3. How the uncertainty in FAR shrinks with ensemble size.
4. Sensitivity to the event threshold.
5. Thermodynamic versus dynamical contributions: FAR is not additive.
6. The intensity ("storyline") alternative to a probability-based statement.
"""

import numpy as np
from scipy import stats

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC ensembles (chosen, not measured) -----------------------------
MU_FACTUAL = 38.0       # deg C, mean of the synthetic factual daily maximum
SD = 2.5                # deg C, its standard deviation (same in both worlds)
SHIFT = 1.5             # deg C, thermodynamic shift in the counterfactual
DYN_SHIFT = 1.0         # deg C, circulation contribution in the factual world
THRESHOLD = 42.0        # deg C, the event definition (at least as hot as this)
N_MEMBERS = 50          # ensemble size for the finite-sample study
N_MC = 400              # Monte Carlo replicates for interval coverage


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def tail_probability(threshold, mean, sd=SD):
    """P(X >= threshold) for a normal distribution (exact)."""
    return float(stats.norm.sf((threshold - mean) / sd))


def wilson(k, n, z=1.959964):
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1.0 + z ** 2 / n
    centre = (p + z ** 2 / (2 * n)) / d
    half = z * np.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / d
    return (max(0.0, centre - half), min(1.0, centre + half))


def far_from_probs(p1, p0):
    """Fraction of attributable risk 1 - p0/p1 (and the probability ratio)."""
    return 1.0 - p0 / p1, p1 / p0


def main():
    section("1. Two ensembles, one event definition")
    p1_exact = tail_probability(THRESHOLD, MU_FACTUAL)
    p0_exact = tail_probability(THRESHOLD, MU_FACTUAL - SHIFT)
    far_exact, pr_exact = far_from_probs(p1_exact, p0_exact)
    print(f"SYNTHETIC factual        : T ~ N({MU_FACTUAL:.1f}, {SD:.1f}^2) deg C")
    print(f"SYNTHETIC counterfactual : T ~ N({MU_FACTUAL - SHIFT:.1f}, {SD:.1f}^2) deg C")
    print(f"event definition: daily maximum >= {THRESHOLD:.1f} deg C")
    print(f"  p1 = P(event | factual)        = {p1_exact:.4f}")
    print(f"  p0 = P(event | counterfactual) = {p0_exact:.4f}")
    print(f"  probability ratio  PR = p1/p0  = {pr_exact:.2f}")
    print(f"  fraction of attributable risk  = {far_exact:.3f}")
    print("  FAR is the fraction of the factual event probability that is")
    print("  absent in the counterfactual.  Both numbers are exact for the")
    print("  stated distributions -- the uncertainty below is sampling only.")

    section("2. What a finite ensemble can actually deliver")
    n = N_MEMBERS
    fact = MU_FACTUAL + SD * RNG.standard_normal(n)
    cfac = (MU_FACTUAL - SHIFT) + SD * RNG.standard_normal(n)
    k1 = int(np.sum(fact >= THRESHOLD))
    k0 = int(np.sum(cfac >= THRESHOLD))
    w1 = wilson(k1, n)
    w0 = wilson(k0, n)
    p1 = k1 / n
    p0 = k0 / n
    print(f"  ensemble of {n} members per world (SYNTHETIC draws)")
    print(f"  factual:        {k1:3d}/{n} exceedances -> p1 = {p1:.3f} "
          f"(95% Wilson [{w1[0]:.3f}, {w1[1]:.3f}])")
    print(f"  counterfactual: {k0:3d}/{n} exceedances -> p0 = {p0:.3f} "
          f"(95% Wilson [{w0[0]:.3f}, {w0[1]:.3f}])")
    if k0 == 0:
        print("  the counterfactual tail is EMPTY, so the probability ratio and")
        print(f"  FAR are not estimable from this ensemble (the exact FAR is")
        print(f"  {far_exact:.3f}).  The Wilson upper limit for p0 is "
              f"{w0[1]:.3f},")
        print(f"  which exceeds the factual p1 = {p1:.3f} and therefore gives no")
        print("  positive lower bound on FAR at all.  This is the central")
        print("  practical limit of event attribution: rare events need large")
        print("  ensembles, and a small one cannot resolve the counterfactual.")
    else:
        far_hat, pr_hat = far_from_probs(p1, p0)
        print(f"  probability ratio estimate = {pr_hat:.2f}")
        print(f"  FAR estimate               = {far_hat:.3f}")
        fars = []
        for _ in range(2000):
            b1 = RNG.choice(fact, n, replace=True)
            b0 = RNG.choice(cfac, n, replace=True)
            q1 = max(np.mean(b1 >= THRESHOLD), 1.0 / n)
            q0 = np.mean(b0 >= THRESHOLD)
            fars.append(1.0 - q0 / q1)
        lo, hi = np.percentile(fars, [2.5, 97.5])
        print(f"  bootstrap 95% interval for FAR = [{lo:.3f}, {hi:.3f}]")
        print(f"  the exact FAR is {far_exact:.3f}; the interval is "
              f"{hi - lo:.3f} wide -- the ensemble, not the physics, sets this.")

    section("3. Uncertainty versus ensemble size")
    print("   n per world   mean FAR   FAR 5th-95th width   P(zero exceedance in CF)")
    for n2 in (10, 25, 50, 100, 250, 1000):
        samples = []
        empty = 0
        for _ in range(N_MC):
            f2 = MU_FACTUAL + SD * RNG.standard_normal(n2)
            c2 = (MU_FACTUAL - SHIFT) + SD * RNG.standard_normal(n2)
            kk1 = np.sum(f2 >= THRESHOLD)
            kk0 = np.sum(c2 >= THRESHOLD)
            if kk0 == 0 or kk1 == 0:
                empty += 1
                samples.append(np.nan)
                continue
            samples.append(1.0 - (kk0 / n2) / (kk1 / n2))
        arr = np.array(samples)
        q5, q95 = np.nanpercentile(arr, [5, 95])
        print(f"  {n2:11d}   {np.nanmean(arr):8.3f}   {q95 - q5:15.3f}   "
              f"{empty / N_MC:22.3f}")
    print("  With small ensembles the counterfactual tail is often empty, and")
    print("  FAR is either undefined or pinned at 1.  A reported FAR with no")
    print("  ensemble-size statement is not reproducible.")

    section("4. Sensitivity to the event threshold")
    print("  threshold (deg C)   p1      p0      PR      FAR")
    for thr in (39.0, 40.0, 41.0, 42.0, 43.0, 44.0):
        a = tail_probability(thr, MU_FACTUAL)
        b = tail_probability(thr, MU_FACTUAL - SHIFT)
        f, r = far_from_probs(a, b)
        print(f"  {thr:17.1f}   {a:.4f}  {b:.4f}  {r:6.2f}  {f:6.3f}")
    print("  FAR rises with the threshold because the tail is where the shift")
    print("  matters most.  The event definition is therefore part of the")
    print("  result, not a preamble to it.")

    section("5. Thermodynamic and dynamical contributions do not add")
    print("  The variable is modelled as T = base + d_thermo + d_dynamic, with")
    print("  d_thermo = +1.5 deg C and d_dynamic = +1.0 deg C in the factual")
    print("  world, so base = 35.5 deg C.  Each row removes some contributions.")
    print("  removed contribution(s)          P(event)    PR     FAR")
    rows = (
        ("both (full counterfactual)", SHIFT, DYN_SHIFT),
        ("thermodynamic only (keep dyn)", SHIFT, 0.0),
        ("dynamic only (keep thermo)", 0.0, DYN_SHIFT),
    )
    far_thermo = far_dyn = far_both = None
    for name, d_t, d_dyn in rows:
        mean_cf = MU_FACTUAL - d_t - d_dyn
        a = tail_probability(THRESHOLD, MU_FACTUAL)
        b = tail_probability(THRESHOLD, mean_cf)
        f, r = far_from_probs(a, b)
        if name.startswith("both"):
            far_both = f
        elif name.startswith("thermodynamic"):
            far_thermo = f
        else:
            far_dyn = f
        print(f"  {name:31s}  {b:.4f}   {r:5.2f}  {f:6.3f}")
    print(f"  the two single-contribution FARs are {far_thermo:.3f} and "
          f"{far_dyn:.3f};")
    print(f"  the combined FAR is {far_both:.3f}, not the sum "
          f"{far_thermo + far_dyn:.3f}.")
    print("  FAR is a nonlinear function of the tail probabilities, so")
    print("  contributions do not decompose additively.  A study that adds")
    print("  a thermodynamic and a dynamic FAR is making an error.")
    # a compensating case
    mean_cf = MU_FACTUAL - SHIFT + 1.0   # warming up, circulation less favourable
    a = tail_probability(THRESHOLD, MU_FACTUAL)
    b = tail_probability(THRESHOLD, mean_cf)
    f, r = far_from_probs(a, b)
    print(f"  an opposing circulation change of -1.0 deg C against a +{SHIFT:.1f} "
          f"deg C")
    print(f"  thermodynamic shift gives FAR = {f:.3f} (PR = {r:.2f}): the two")
    print("  contributions can cancel, and the net sign is a measurement.")

    section("6. The intensity (storyline) alternative")
    z = stats.norm.isf(1.0 / 100.0)     # the factual 100-year level
    t100_fact = MU_FACTUAL + SD * z
    t100_cf = MU_FACTUAL - SHIFT + SD * z
    print(f"  a different question: how much hotter is the 1-in-100 level?")
    print(f"  factual 1-in-100 daily maximum       : {t100_fact:.2f} deg C")
    print(f"  counterfactual 1-in-100 daily maximum: {t100_cf:.2f} deg C")
    print(f"  difference (the thermodynamic shift) : {t100_fact - t100_cf:.2f} deg C")
    print("  The intensity statement is conditional on the event having")
    print("  occurred ('this event is 1.5 deg C hotter than it would have")
    print("  been'), while the probability statement is about how often such")
    print("  events occur.  They are different questions and need different")
    print("  uncertainty statements; neither is the 'true' answer.")


if __name__ == "__main__":
    main()
