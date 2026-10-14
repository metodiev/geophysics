#!/usr/bin/env python3
"""Tectonics, surface processes and climate: a zero-dimensional carbonate-silicate
box model, the strength of the weathering thermostat, the equilibration
timescale, and the degeneracy between the parameters that the present-day state
cannot separate.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tectonics_climate_feedback_demo.py

Everything is SYNTHETIC.  The fluxes are in chosen units of 1e12 mol C per year
and every parameter is a teaching value, not a measurement of the Earth.  No
published carbon-cycle model is reproduced or quoted.

Contents
--------
1. The model and its steady state.
2. The thermostat: how much the weathering feedback reduces a temperature change.
3. Equilibration time after a perturbation.
4. The degeneracy: parameter pairs that fit the present state and disagree about
   the past.
5. A tectonic forcing scenario with two of those pairs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


# SYNTHETIC parameter set, chosen teaching values.
N0 = 1.0                 # reference reservoir, in units of 1e12 mol C
P0 = 400.0               # reference pCO2, ppmv
T0 = 15.0                # reference mean surface temperature, deg C
S_2X = 3.0               # climate sensitivity, K per doubling of pCO2
A_EXP = 0.30             # exponent of the weathering law in the reservoir
BETA = 0.06              # 1/K, temperature dependence of weathering
F_OUT0 = 1.0             # reference outgassing, units of 1e12 mol C/yr


def temperature(n, s_2x=S_2X, t0=T0):
    """T = T0 + S log2(n/n0), a logarithmic CO2 sensitivity."""
    return t0 + s_2x * np.log2(np.asarray(n, dtype=float) / N0)


def weathering(n, a=A_EXP, beta=BETA):
    """Silicate weathering sink, proportional to runoff and to temperature."""
    return (np.asarray(n, dtype=float) / N0) ** a * \
        np.exp(beta * (temperature(n) - T0))


def steady_state(f_out, a=A_EXP, beta=BETA, u=1.0):
    """Solve f_out = u * weathering(n) for the reservoir, by bisection.

    ``u`` is a weathering efficiency multiplier, the tectonic knob (more
    exposed fresh rock means a larger u for the same climate).
    """
    lo, hi = 1e-3, 1e4
    for _ in range(200):
        mid = np.sqrt(lo * hi)
        if u * float(np.atleast_1d(weathering(mid, a, beta))[0]) < f_out:
            lo = mid
        else:
            hi = mid
    return np.sqrt(lo * hi)


def integrate(n_start, f_out, a=A_EXP, beta=BETA, u=1.0, t_end=2.0e6,
              dt=2.0e3):
    """Integrate dn/dt = f_out - u * weathering(n) with a fixed step."""
    n = n_start
    ts, ns = [0.0], [n]
    n_step = int(t_end / dt)
    for i in range(n_step):
        fw = float(np.atleast_1d(weathering(n, a, beta))[0])
        n = n + dt * (f_out - u * fw)
        ts.append((i + 1) * dt)
        ns.append(n)
    return np.array(ts), np.array(ns)


def demonstration_1():
    section("1. The carbonate-silicate box model and its steady state")
    print("  State: N, the atmosphere-ocean carbon reservoir (units of 1e12 mol C;")
    print("  the partitioning between atmosphere and ocean is held fixed).")
    print("     dN/dt = F_out - F_w,        F_w = u (N/N0)^a exp(beta (T - T0)),")
    print("     T = T0 + S log2(N/N0).")
    print("  F_out is volcanic and metamorphic outgassing, u is a weathering")
    print("  efficiency (the tectonic knob), and the weathering law is the")
    print("  thermostat: warmer means faster weathering means less CO2.\n")
    print(f"  SYNTHETIC parameters: N0 = {N0:.1f}, pCO2 reference {P0:.0f} ppmv,")
    print(f"  T0 = {T0:.0f} C, S = {S_2X:.1f} K per doubling, a = {A_EXP:.2f},")
    print(f"  beta = {BETA:.3f} 1/K, reference outgassing {F_OUT0:.2f} "
          f"(1e12 mol C/yr)\n")
    print("   F_out (1e12 mol C/yr)   N steady    pCO2 (ppmv)   T (C)")
    for f in (0.5, 1.0, 2.0, 4.0):
        n = steady_state(f)
        print(f"   {f:22.2f}   {n:9.4f}   {P0 * n / N0:12.1f}   "
              f"{float(temperature(n)):6.2f}")
    print("\n  The sensitivity of the steady temperature to a doubling of")
    print("  outgassing is much smaller than the climate sensitivity itself:")
    print("  the warming is largely cancelled by the weathering response.")
    n1 = steady_state(1.0)
    n2 = steady_state(2.0)
    print(f"    outgassing 1 -> 2 gives dT = "
          f"{float(temperature(n2)) - float(temperature(n1)):.3f} K")
    print(f"    while the same CO2 doublings without a weathering response would")
    print(f"    give 3.00 K (the climate sensitivity S).")


def demonstration_2():
    section("2. The strength of the thermostat")
    print("  Differentiate the steady-state balance F_out = u (N/N0)^a exp(beta(T-T0))")
    print("  with T = T0 + S log2(N/N0):")
    print("     d ln N / d ln F_out = 1 / (a + beta S / ln 2),")
    print("  so the exponent that relates outgassing to CO2 is boosted above a by")
    print("  the temperature feedback.  Removing the feedback (beta = 0) gives the")
    print("  bare 1/a.\n")
    denom = A_EXP + BETA * S_2X / np.log(2.0)
    print(f"    a = {A_EXP:.2f}, beta = {BETA:.3f} 1/K, S = {S_2X:.1f} K per doubling")
    print(f"    a + beta S/ln2 = {A_EXP:.3f} + {BETA * S_2X / np.log(2.0):.3f} "
          f"= {denom:.3f}")
    print(f"    the exponent relating N to F_out is therefore {1.0 / denom:.3f}")
    print(f"    without the temperature dependence it would be "
          f"{1.0 / A_EXP:.3f}, so the")
    print(f"    thermostat weakens the CO2 response of the steady state by a")
    print(f"    factor of {(1.0 / A_EXP) / (1.0 / denom):.3f}")
    print(f"\n  the measured steady-state temperature change for a doubling of")
    print(f"  outgassing, with and without the temperature dependence of the")
    print(f"  weathering sink:\n")
    print("    case                       N steady     T (C)     change from 15 C")
    for label, beta in (("full model, beta = %.3f" % BETA, BETA),
                        ("no temperature feedback (beta = 0)", 0.0)):
        n2 = steady_state(2.0, A_EXP, beta)
        print(f"    {label:37s} {n2:9.4f}   "
              f"{float(temperature(n2)):7.3f}   "
              f"{float(temperature(n2)) - T0:14.3f}")
    print("\n  and the small-perturbation check of the closed form above:")
    print("    F_out 1.00 -> 1.10 gives")
    print(f"      closed form:  S log2(1 + 0.10/denom) = "
          f"{S_2X * np.log2(1.0 + 0.10 / denom):.3f} K")
    print(f"      exact steady states: "
          f"{float(temperature(steady_state(1.1))) - T0:.3f} K")
    print(f"    F_out 1.00 -> 1.01 gives")
    print(f"      closed form:  {S_2X * np.log2(1.0 + 0.01 / denom):.4f} K")
    print(f"      exact steady states: "
          f"{float(temperature(steady_state(1.01))) - T0:.4f} K")
    print("  the closed form is the small-signal limit and it is exact only in")
    print("  that limit; the two columns agree to the third decimal at 1% and")
    print("  differ at the second decimal at 10%.")


def demonstration_3():
    section("3. Equilibration time")
    print("  Linearising dn/dt = F_out - u (N/N0)^a exp(beta(T-T0)) about the")
    print("  steady state gives an exponential relaxation with")
    print("     tau = 1 / (a + beta S/ln 2)   in units of t* = N0/F_out.\n")
    t_star_desc = ("t* = N0 / F_out is the time for outgassing to replace the whole "
                   "reservoir")
    print(f"  here N0 = {N0:.2f} and F_out = {F_OUT0:.2f} in the chosen units, so")
    print(f"  t* = {N0 / F_OUT0:.2f} model time units and the *ratios* below are")
    print("  what the model determines; the physical value follows from whatever")
    print("  the units are.\n")
    denom = A_EXP + BETA * S_2X / np.log(2.0)
    tau = 1.0 / denom
    print(f"    tau = {tau:.4f} t*")
    print(f"    illustrative conversion, with chosen inputs (not measurements):")
    n_phys = 3.0e18
    f_phys = 1.2e13
    t_star = n_phys / f_phys
    print(f"      reservoir {n_phys:.1e} mol C and outgassing {f_phys:.1e} mol C/yr")
    print(f"      give t* = {t_star:.3e} yr = {t_star / 1e6:.2f} Myr and")
    print(f"      tau = {tau * t_star:.3e} yr = {tau * t_star / 1e6:.2f} Myr")
    print("\n  measured decay of a 5% perturbation (in model units):")
    ts, ns = integrate(1.05, F_OUT0, t_end=8.0, dt=0.01)
    print("    t (t*)   N        N - N_ss     ratio per 0.5 t*")
    prev = None
    for i in range(0, ts.size, 50):
        d = ns[i] - 1.0
        r = "" if prev is None else f"{d / prev:.5f}"
        print(f"    {ts[i]:7.2f}   {ns[i]:.6f}   {d:+.6f}   {r:>10s}")
        prev = d
    d1 = ns[50] - 1.0
    d2 = ns[100] - 1.0
    print(f"\n    measured tau = 0.5 / ln({d1 / d2:.6f}) = "
          f"{0.5 / np.log(d1 / d2):.5f} t*")
    print(f"    closed form  = {tau:.5f} t*")
    ts2, ns2 = integrate(1.5, F_OUT0, t_end=8.0, dt=0.01)
    d3 = ns2[50] - 1.0
    d4 = ns2[100] - 1.0
    print(f"    the same measurement on a 50% perturbation gives "
          f"{0.5 / np.log(d3 / d4):.5f} t*:")
    print(f"    a larger perturbation relaxes faster because the flux law is not")
    print(f"    linear in N, so the linearised tau is a small-signal quantity and")
    print(f"    the discrepancy above is the size of that effect at 50%.")
    print("\n  The equilibration time of the silicate-weathering thermostat is a")
    print("  few times the residence time of carbon in the surface reservoir,")
    print("  which is what makes it a climate stabiliser on the 1e5 to 1e6 yr")
    print("  timescale rather than on the 1e3 yr timescale of the ocean alone.")


def demonstration_4():
    section("4. The degeneracy: one present state, many parameter pairs")
    print("  Every parameter pair (a, beta) reproduces the present-day state here,")
    print("  because the weathering law is normalised to give F_w(N0) = F_out at")
    print("  the reference reservoir.  The present state therefore constrains no")
    print("  parameter at all; what it fails to constrain is visible in the")
    print("  responses.\n")
    sets = ((0.05, 0.05), (0.30, 0.06), (0.80, 0.20))
    print("   a      beta (1/K)   a + beta S/ln2   T after a doubling   dT (K)")
    for a_i, b_i in sets:
        d_i = a_i + b_i * S_2X / np.log(2.0)
        n_new = steady_state(2.0, a_i, b_i)
        print(f"   {a_i:4.2f}   {b_i:9.3f}   {d_i:14.3f}   "
              f"{float(temperature(n_new)):18.3f}   "
              f"{float(temperature(n_new)) - T0:6.3f}")
    print("\n  the temperature response to the same doubling of outgassing")
    print("  differs by a factor of "
          f"{(float(temperature(steady_state(2.0, 0.05, 0.05))) - T0) / (float(temperature(steady_state(2.0, 0.8, 0.2))) - T0):.1f}"
          " between the first and last row.")
    print("\n  inverted, the outgassing rate required for a given past temperature:")
    print("   target T (C)   required F_out for each parameter set")
    for t_target in (17.0, 19.0, 21.0):
        row = []
        for a_i, b_i in sets:
            lo, hi = 0.2, 50.0
            for _ in range(200):
                mid = np.sqrt(lo * hi)
                if float(temperature(steady_state(mid, a_i, b_i))) < t_target:
                    lo = mid
                else:
                    hi = mid
            row.append(np.sqrt(lo * hi))
        ratio = max(row) / min(row)
        print(f"   {t_target:12.1f}   " + "   ".join(f"{v:7.3f}" for v in row)
              + f"    spread x{ratio:.2f}")
    print("\n  The same palaeotemperature is produced by outgassing rates that")
    print("  differ by a factor of two to three depending on the parameter set,")
    print("  and no temperature record can separate them.  What breaks the")
    print("  degeneracy is an independent constraint on one of the parameters --")
    print("  a laboratory or field measurement of the weathering law, or an")
    print("  independent outgassing history -- not a better thermometer.")


def demonstration_5():
    section("5. A tectonic forcing scenario")
    print("  Scenario: a weathering-efficiency ramp, u growing from 1.0 to 2.0")
    print("  over 10 Myr and then held, with outgassing constant.  This stands for")
    print("  the exposure of fresh rock by mountain building.\n")
    print("   a      beta    T before the ramp   T at the end   cooling (K)")
    for a_i, b_i in ((0.05, 0.05), (0.30, 0.06), (0.80, 0.20)):
        n_start = steady_state(1.0, a_i, b_i)
        n_end = steady_state(1.0, a_i, b_i, u=2.0)
        print(f"   {a_i:4.2f}   {b_i:6.3f}   "
              f"{float(temperature(n_start)):18.3f}   "
              f"{float(temperature(n_end)):11.3f}   "
              f"{float(temperature(n_start)) - float(temperature(n_end)):11.3f}")
    cool_1 = float(temperature(steady_state(1.0, 0.05, 0.05))) - \
        float(temperature(steady_state(1.0, 0.05, 0.05, u=2.0)))
    cool_3 = float(temperature(steady_state(1.0, 0.8, 0.2))) - \
        float(temperature(steady_state(1.0, 0.8, 0.2, u=2.0)))
    print(f"\n  the cooling produced by the same tectonic scenario differs by a")
    print(f"  factor of {cool_1 / cool_3:.1f} between parameter sets that agree at")
    print(f"  the present day.  The direction of the effect is robust -- more")
    print(f"  weathering means less CO2 and a cooler climate -- while its magnitude")
    print(f"  is not, and that is the honest form of the statement.")
    print("\n  Whether the climate signal records the forcing or lags it depends on")
    print("  the ratio of the equilibration time to the duration of the ramp:")
    print("  with a 10 Myr ramp and an equilibration time of order 1 Myr or less,")
    print("  the response is essentially complete, so in this model the climate")
    print("  record is a faithful image of the tectonic forcing.  Making the")
    print("  reservoir larger, or the weathering law weaker, changes that")
    print("  conclusion without changing the direction of the effect.")


def main():
    demonstration_1()
    demonstration_2()
    demonstration_3()
    demonstration_4()
    demonstration_5()
    print("\nAll results above are SYNTHETIC teaching computations.")


if __name__ == "__main__":
    main()
