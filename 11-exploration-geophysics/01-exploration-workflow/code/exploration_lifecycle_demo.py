#!/usr/bin/env python3
"""Exploration lifecycle: the staged funnel from reconnaissance to reserve.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python exploration_lifecycle_demo.py

Everything here is SYNTHETIC.  The stage probabilities, costs, deposit-size
distribution, grade distribution, metal price and mining/processing costs are
chosen teaching values, not published statistics for any real belt, company or
deposit.

Contents
--------
1. The staged funnel: conditional advance probabilities, overall chance of
   success, and expected cost per discovery.
2. Deposit-size distribution (lognormal) and contained metal.
3. Grade-tonnage curve for one deposit; the cut-off grade as an economic choice.
4. Optimal cut-off: marginal break-even versus a capacity- and discount-
   constrained mine plan.
5. Portfolio arithmetic: P(at least one discovery) for independent targets.
6. Price sensitivity of the reserve, and drill-density scaling.
7. Verification: the numerical integrals against the closed-form lognormal.
"""

import numpy as np
from scipy import integrate, optimize, stats

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC program parameters (chosen, not measured) ---------------------
STAGES = [
    # name, area worked (km^2), stage cost (MUSD), P(advance to next stage)
    ("1 Regional reconnaissance", 12000.0, 0.60, 0.35),
    ("2 Prospect delineation", 900.0, 2.50, 0.30),
    ("3 Target definition", 60.0, 6.00, 0.25),
    ("4 Discovery drilling", 6.0, 24.00, 0.55),
    ("5 Resource definition", 1.5, 40.00, 0.60),
    ("6 Feasibility / reserve", 1.5, 55.00, 1.00),
]

TONNAGE_MEDIAN_MT = 30.0      # median deposit size of the SYNTHETIC population
TONNAGE_SIGMA_LN = 1.10       # lognormal shape parameter (natural log units)
GRADE_MEAN_PCT = 0.50         # mean grade of the SYNTHETIC deposit population

DEPOSIT_MT = 100.0            # ore tonnage of the single SYNTHETIC studied deposit
GRADE_MEDIAN_PCT = 0.30       # median grade inside that deposit
GRADE_SIGMA_LN = 0.60         # lognormal shape parameter of grade

PRICE_USD_PER_T = 9000.0      # metal price, USD per tonne of contained metal
RECOVERY = 0.88               # metallurgical recovery of the plant, dimensionless
COST_PER_T_USD = 15.0         # mining + processing cost, USD per tonne of ore
CAPITAL_MUSD = 350.0          # fixed capital cost of the SYNTHETIC project
MILL_CAPACITY_MT_PER_YR = 8.0 # mill throughput of the SYNTHETIC project


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


def money(x):
    return f"{x:,.1f}"


def main():
    section("1. The staged funnel: conditional advance probabilities")
    print(f"{'stage':30s} {'area (km2)':>11s} {'cost (MUSD)':>12s} {'P(advance)':>11s}")
    for name, area, cost, p in STAGES:
        print(f"{name:30s} {area:11.1f} {cost:12.2f} {p:11.2f}")
    pos = float(np.prod([s[3] for s in STAGES]))
    print(f"\noverall probability of success (product of the conditional P) = {pos:.5f}"
          f"  = 1 in {1 / pos:,.0f}")
    # Expected cost to a terminal decision: a branch is abandoned at the first
    # failed stage, so the cost of stage i is incurred only with probability
    # (prod of advance probabilities before i).
    surv = 1.0
    e_cost = 0.0
    for name, area, cost, p in STAGES:
        e_cost += surv * cost
        surv *= p
    print(f"expected spend per attempt (branch-stopped)          = {money(e_cost)} MUSD")
    print(f"expected spend per discovery = {money(e_cost / pos)} MUSD")
    print(f"  (the funnel is a geometric series, not a sum: each stage is entered")
    print(f"   only by the survivors of the previous one)")
    print(f"area at the reconnaissance stage  = {STAGES[0][1]:,.0f} km2")
    print(f"area at the reserve stage         = {STAGES[-1][1]:,.1f} km2")
    print(f"area reduction factor over the lifecycle = "
          f"{STAGES[0][1] / STAGES[-1][1]:,.0f}x")

    section("2. Deposit-size distribution (SYNTHETIC lognormal population)")
    mu = np.log(TONNAGE_MEDIAN_MT)
    shape = TONNAGE_SIGMA_LN
    scale = np.exp(mu)
    dist = stats.lognorm(s=shape, scale=scale)
    print(f"median size = {TONNAGE_MEDIAN_MT:.1f} Mt, sigma_ln = {shape:.2f}")
    print(f"{'percentile':>11s} {'tonnage (Mt)':>13s} {'contained Cu (kt)':>18s}")
    for q in (0.10, 0.25, 0.50, 0.75, 0.90, 0.99):
        t = dist.ppf(q)
        print(f"{q * 100:10.0f}% {t:13.1f} {t * 1e6 * GRADE_MEAN_PCT / 100.0 / 1e3:18.1f}")
    print(f"mean size  = {dist.mean():.1f} Mt  "
          f"(exp(mu + sigma^2/2) = {np.exp(mu + shape ** 2 / 2):.1f} Mt)")
    print(f"P(size > 100 Mt) = {dist.sf(100.0):.4f};  "
          f"P(size > 500 Mt) = {dist.sf(500.0):.5f}")
    print("a heavy right tail is what makes a few large deposits carry most of the")
    print("contained metal: the top decile supplies a disproportionate share.")

    section("3. Grade-tonnage: the cut-off grade is an economic choice")
    gscale = GRADE_MEDIAN_PCT / 100.0        # median grade, mass fraction
    gshape = GRADE_SIGMA_LN
    gdist = stats.lognorm(s=gshape, scale=gscale)
    print(f"deposit: {DEPOSIT_MT:.0f} Mt at median grade {GRADE_MEDIAN_PCT:.2f}% Cu, "
          f"sigma_ln = {gshape:.2f}")
    print(f"mean grade = {gdist.mean() * 100:.3f}% Cu")
    print(f"\n{'cut-off (%)':>12s} {'ore (Mt)':>10s} {'mean grade (%)':>15s} "
          f"{'contained Cu (kt)':>18s}")
    for cut_pct in (0.05, 0.10, 0.20, 0.30, 0.50, 0.80, 1.20):
        cut = cut_pct / 100.0
        frac = gdist.sf(cut)
        ore = DEPOSIT_MT * frac
        cond = gdist.expect(lambda g: g, lb=cut) / frac if frac > 0 else 0.0
        print(f"{cut_pct:12.2f} {ore:10.1f} {cond * 100:15.3f} "
              f"{ore * cond * 1e3:18.1f}")
    print("raising the cut-off always reduces the contained metal; it can only")
    print("improve the *margin per tonne*, so the cut-off is set by economics.")

    section("4. Optimal cut-off: break-even versus a constrained mine plan")
    recovery, price, cost_t = RECOVERY, PRICE_USD_PER_T, COST_PER_T_USD
    breakeven = cost_t / (recovery * price)
    print(f"price = {price:,.0f} USD/t, recovery = {recovery:.2f}, "
          f"cost = {cost_t:.1f} USD/t of ore")
    print(f"break-even (marginal) grade = cost/(recovery*price) = "
          f"{breakeven * 100:.4f}% Cu")

    def head_grade(cut):
        frac = gdist.sf(cut)
        if frac <= 0.0:
            return 0.0
        return gdist.expect(lambda g: g, lb=cut) / frac

    def ore_mt(cut):
        return DEPOSIT_MT * gdist.sf(cut)

    def operating_profit_musd(cut):
        return ore_mt(cut) * 1e6 * (recovery * head_grade(cut) * price - cost_t) / 1e6

    def npv_musd(cut, rate):
        """NPV of a mill of fixed capacity fed from the ore above `cut`."""
        ore = ore_mt(cut)
        if ore <= 0.0:
            return -CAPITAL_MUSD
        life_yr = ore / MILL_CAPACITY_MT_PER_YR
        annual = (MILL_CAPACITY_MT_PER_YR * 1e6
                  * (recovery * head_grade(cut) * price - cost_t) / 1e6)
        if rate == 0.0:
            pv = annual * life_yr
        else:
            pv = annual * (1.0 - (1.0 + rate) ** -life_yr) / rate
        return pv - CAPITAL_MUSD

    cut_no_fixed = optimize.minimize_scalar(
        lambda c: -operating_profit_musd(c), bounds=(1e-5, 0.02), method="bounded"
    ).x
    print(f"\nmarginal optimum, no capacity limit and no discounting:")
    print(f"  cut-off = {cut_no_fixed * 100:.4f}% Cu, undiscounted profit = "
          f"{money(operating_profit_musd(cut_no_fixed))} MUSD")
    print(f"  the optimum sits exactly at break-even grade: rock below it loses")
    print(f"  money on every tonne, and nothing couples one tonne to the next.")
    print(f"\nmill capacity = {MILL_CAPACITY_MT_PER_YR:.1f} Mt/yr, "
          f"capital = {money(CAPITAL_MUSD)} MUSD")
    print(f"{'discount rate':>14s} {'cut-off (%)':>12s} {'life (yr)':>10s} "
          f"{'NPV (MUSD)':>12s} {'vs break-even':>14s}")
    for rate in (0.0, 0.05, 0.10, 0.20, 0.35):
        opt = optimize.minimize_scalar(
            lambda c, r=rate: -npv_musd(c, r), bounds=(1e-5, 0.02),
            method="bounded"
        ).x
        life = ore_mt(opt) / MILL_CAPACITY_MT_PER_YR
        print(f"{rate * 100:13.0f}% {opt * 100:12.4f} {life:10.2f} "
              f"{npv_musd(opt, rate):12.1f} {(opt - breakeven) * 100:+13.4f}pp")
    print("with a fixed mill throughput the marginal tonnes can only be processed")
    print("later, so their revenue is discounted; the optimum cut-off therefore")
    print("rises ABOVE break-even grade as the discount rate rises.  The reserve")
    print("tonnage depends on the discount rate, which is a financial choice.")

    section("5. Portfolio arithmetic (independent targets)")
    for n, p in ((12, 0.05), (40, 0.02), (5, 0.20)):
        p_any = 1.0 - (1.0 - p) ** n
        print(f"N = {n:2d} targets, p = {p:.2f} each:  E[discoveries] = {n * p:.2f},  "
              f"P(at least one) = {p_any:.3f},  P(none) = {(1 - p) ** n:.3f}")
    print("the expectation is fixed by N*p, but the *median* outcome is still zero")
    print("whenever N*p < ~0.7: most programs fail, which is the honest baseline.")

    section("6. Price sensitivity of the reserve, and drill density")
    print(f"{'price (USD/t)':>13s} {'cut-off (%)':>12s} {'reserve (Mt)':>13s} "
          f"{'contained Cu (kt)':>18s}")
    base_ore = None
    for price_i in (6000.0, 7500.0, 9000.0, 11000.0, 14000.0):
        be_i = cost_t / (recovery * price_i)
        ore = ore_mt(be_i)
        if abs(price_i - price) < 1.0:
            base_ore = ore
        print(f"{price_i:13,.0f} {be_i * 100:12.3f} {ore:13.2f} "
              f"{ore * head_grade(be_i) * 1e3:18.1f}")
    ore_lo = ore_mt(cost_t / (recovery * 6000.0))
    ore_hi = ore_mt(cost_t / (recovery * 14000.0))
    print(f"a price fall from 9000 to 6000 USD/t removes "
          f"{(1 - ore_lo / base_ore) * 100:.1f}% of the reserve tonnage;")
    print(f"a price rise to 14000 USD/t adds {(ore_hi / base_ore - 1) * 100:.1f}%.")
    print("the deposit did not change: only the price did.  A reserve tonnage is")
    print("an economic statement whose uncertainty sits in the price line.")

    print("\ndrill density needed to step from 400 m to 100 m grid spacing:")
    area_km2 = 1.5
    for spacing_m in (400.0, 200.0, 100.0, 50.0):
        n_holes = area_km2 * 1e6 / spacing_m ** 2
        print(f"  {spacing_m:5.0f} m spacing: {n_holes:8.0f} holes over "
              f"{area_km2:.1f} km2  ({spacing_m ** 2 / 50 ** 2:6.1f}x the 50 m count)")
    print("confidence classes are bought with drill metres: the cost of moving a")
    print("tonnage from inferred to measured scales as (old/new spacing)^2.")

    section("7. Verification against closed-form results")
    cut = 0.0025
    numeric_ore, _ = integrate.quad(lambda g: gdist.pdf(g), cut, 30.0)
    print(f"(a) ore fraction above {cut * 100:.2f}% Cu")
    print(f"    numeric integral   = {numeric_ore:.10f}")
    print(f"    lognormal survival = {gdist.sf(cut):.10f}")
    print(f"    difference         = {abs(numeric_ore - gdist.sf(cut)):.2e}")
    numeric_head, _ = integrate.quad(lambda g: g * gdist.pdf(g), cut, 30.0)
    print(f"(b) head grade above the cut-off")
    print(f"    numeric integral   = {numeric_head / numeric_ore * 100:.8f}% Cu")
    print(f"    closed form        = {head_grade(cut) * 100:.8f}% Cu")
    print(f"    difference         = "
          f"{abs(numeric_head / numeric_ore - head_grade(cut)) * 100:.2e} percentage points")
    print(f"(c) geometric series for the expected spend: "
          f"{money(e_cost)} MUSD vs an independent stage-by-stage sum of "
          f"{money(sum(s[2] for s in STAGES))} MUSD for a program that ran every")
    print("    stage unconditionally.  The gap is the whole point of staging.")


if __name__ == "__main__":
    main()
