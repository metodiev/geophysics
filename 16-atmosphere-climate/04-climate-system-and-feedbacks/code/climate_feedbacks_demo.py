#!/usr/bin/env python3
"""Feedbacks: Planck response, the additive feedback decomposition with its
spread, the ice-albedo feedback and its multiple equilibria, the
Clausius-Clapeyron rate for water vapour, and the sign ambiguity of the cloud
feedback.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python climate_feedbacks_demo.py

Everything is SYNTHETIC. Every feedback parameter, sensitivity distribution,
albedo ramp and cloud coefficient here is a CHOSEN TEACHING VALUE. No value is
quoted from a published assessment, and no number in this script is an estimate
of the real Earth's feedbacks. Physical constants (the Stefan-Boltzmann
constant, the latent heat of vaporisation, the gas constant of water vapour,
gravity) are standard constants.

Contents
--------
1. Planck response and the reference forcing.
2. Additive feedback decomposition over assumed ranges: total lambda, the
   equilibrium temperature change, and how the spread is produced.
3. Where the linear decomposition stops working: a state-dependent feedback.
4. Ice-albedo feedback: feedback parameter, multiple equilibria and hysteresis.
5. Water vapour: the Clausius-Clapeyron rate versus temperature.
6. Cloud feedback: a two-effect budget that spans both signs.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

SIGMA = 5.670374419e-8
SOLAR = 1361.0              # W/m^2, adopted total solar irradiance (standard)
T_REF = 288.0               # K, chosen reference surface temperature
F_2X = 3.7                  # W/m^2, chosen reference forcing (an assumption)
L_VAP = 2.5e6               # J/kg
R_VAPOUR = 461.5            # J/(kg K)


def section(title):
    print(f"\n{'=' * 72}\n{title}\n{'=' * 72}")


# ---------------------------------------------------------------------------
# 1. Planck response
# ---------------------------------------------------------------------------

def part1_planck():
    section("1. The Planck response: the stabilising baseline")
    lam0 = -4.0 * SIGMA * T_REF ** 3
    print("For OLR = sigma T^4, dOLR/dT = 4 sigma T^3. In the convention where")
    print("lambda is d(net downward flux)/dT, the Planck response is NEGATIVE:")
    print(f"  lambda_0 = -4 sigma T^3 = {lam0:.3f} W/(m^2 K) at T = {T_REF:.0f} K")
    print(f"  reference forcing used throughout: F_2x = {F_2X:.1f} W/m^2")
    print(f"  Planck-only response to F_2x: dT = -F_2x/lambda_0 = "
          f"{-F_2X / lam0:.2f} K")
    print("\n  That number is the answer a planet with no feedbacks would give.")
    print("  Every other feedback is a departure from it, and the departures are")
    print("  large enough that the result is not the Planck value.")


# ---------------------------------------------------------------------------
# 2. Additive feedback decomposition
# ---------------------------------------------------------------------------

def part2_decomposition():
    section("2. Additive decomposition with stated spread")
    print("SYNTHETIC assumed ranges, chosen to illustrate the arithmetic and NOT")
    print("to represent the real Earth. Each is a uniform distribution over the")
    print("stated interval, in W/(m^2 K), with lambda_0 = %.3f." %
          (-4.0 * SIGMA * T_REF ** 3))
    assumed = {
        "water vapour + lapse rate": (0.8, 1.4),
        "surface albedo": (0.1, 0.5),
        "cloud": (-0.4, 1.2),
        "carbon cycle": (0.0, 0.3),
    }
    print(f"\n{'feedback':>26} {'assumed range':>18} {'mean':>8} {'sd':>8}")
    for name, (lo, hi) in assumed.items():
        print(f"{name:>26} {f'[{lo:+.1f}, {hi:+.1f}]':>18} "
              f"{(lo + hi) / 2:8.2f} {(hi - lo) / np.sqrt(12.0):8.3f}")
    n = 400000
    lam0 = -4.0 * SIGMA * T_REF ** 3
    tot = np.full(n, lam0)
    draws = {}
    for name, (lo, hi) in assumed.items():
        d = RNG.uniform(lo, hi, n)
        draws[name] = d
        tot = tot + d
    ecs = -F_2X / tot
    print(f"\n  total lambda = lambda_0 + sum(lambda_i):")
    print(f"    mean {tot.mean():.3f}, sd {tot.std():.3f}, "
          f"range [{tot.min():.3f}, {tot.max():.3f}] W/(m^2 K)")
    print(f"  implied equilibrium temperature change -F_2x/lambda:")
    for q in (5, 25, 50, 75, 95):
        print(f"    {q:2d}th percentile: {np.percentile(ecs, q):.3f} K")
    print(f"    mean {ecs.mean():.3f} K, sd {ecs.std():.3f} K")
    print("  Contribution of each assumed feedback to the variance of the total:")
    for name, d in draws.items():
        cov = np.mean((d - d.mean()) * (tot - tot.mean()))
        print(f"    {name:>26}: {100.0 * cov / tot.var():5.1f}% of the variance")
    print("\n  Two things to notice. First, the distribution of the answer is")
    print("  SKEWED: -F_2x/lambda with lambda near zero produces a long upper")
    print("  tail, so the mean lies above the median. Second, most of the spread")
    print("  in the answer comes from the feedback with the widest assumed range")
    print("  -- here the cloud term -- not from the one with the largest mean.")
    print("  Changing the assumed ranges changes every number above; that is the")
    print("  point of writing them down.")


# ---------------------------------------------------------------------------
# 3. Where linearity fails
# ---------------------------------------------------------------------------

def part3_linearity():
    section("3. Where the linear decomposition stops working")
    lam0 = -4.0 * SIGMA * T_REF ** 3
    # a state-dependent cloud-like feedback: lambda_c = 0.8 + 0.15 * dT
    lam_c0, slope = 0.8, 0.15
    print("Take a single amplifying feedback whose parameter STRENGTHENS as the")
    print("state warms:")
    print(f"  lambda_c(dT) = {lam_c0:.2f} + {slope:.2f} dT   W/(m^2 K)")
    print("The linear answer uses lambda_c at dT = 0; the exact answer solves")
    print("  F = (|lambda_0| - lambda_c(dT)) dT  implicitly.")
    print("Ignoring the drift therefore UNDERestimates the warming.")
    print(f"\n{'F (W/m^2)':>11} {'linear dT (K)':>14} {'exact dT (K)':>13} "
          f"{'error':>9} {'lambda_c at dT':>16}")
    for f in (0.5, 1.0, 2.0, 3.7, 6.0, 8.0):
        lin = -f / (lam0 + lam_c0)
        # solve slope*dT^2 - (|lam0| - lam_c0)*dT + F = 0
        a = slope
        b = -(abs(lam0) - lam_c0)
        c = f
        disc = b ** 2 - 4.0 * a * c
        exact = (-b - np.sqrt(disc)) / (2.0 * a) if disc >= 0.0 else float("nan")
        print(f"{f:11.1f} {lin:14.3f} {exact:13.3f} "
              f"{(exact - lin) / lin * 100:8.2f}% {lam_c0 + slope * exact:16.3f}")
    print("\n  At the reference forcing the linear answer is wrong by a few per")
    print("  cent, and at three times that forcing it is wrong by tens of per")
    print("  cent. The decomposition is an expansion about the present state;")
    print("  using it far from that state is not a conservative approximation,")
    print("  it is a different model.")


# ---------------------------------------------------------------------------
# 4. Ice-albedo feedback
# ---------------------------------------------------------------------------

def ice_albedo_equilibria(solar, a_ice=0.62, a_free=0.30, t_lo=-10.0,
                          t_hi=10.0, a_olr=203.3, b_olr=2.09):
    """Closed-form equilibria of (S/4)(1-alpha(T)) = A + B T with a ramped albedo.

    Each albedo regime gives one linear equation, so there are at most three
    roots; a root counts only if it lies inside the regime that produced it.
    """
    roots = []
    t_cold = ((solar / 4.0) * (1.0 - a_ice) - a_olr) / b_olr
    if t_cold <= t_lo:
        roots.append(("ice", t_cold))
    t_warm = ((solar / 4.0) * (1.0 - a_free) - a_olr) / b_olr
    if t_warm >= t_hi:
        roots.append(("ice-free", t_warm))
    slope = (a_free - a_ice) / (t_hi - t_lo)
    alpha_lo = a_ice - slope * t_lo                     # intercept at T = 0
    num = a_olr - (solar / 4.0) * (1.0 - alpha_lo)
    den = (solar / 4.0) * slope - b_olr
    if abs(den) > 1e-12:
        t_ramp = num / den
        if t_lo < t_ramp < t_hi:
            roots.append(("ramp", t_ramp))
    return roots, slope


def ice_loop_width(a_ice=0.62, a_free=0.30, t_lo=-10.0, t_hi=10.0,
                   a_olr=203.3, b_olr=2.09):
    """Solar constants at which each branch disappears (the loop edges)."""
    s_low = 4.0 * (t_hi * b_olr + a_olr) / (1.0 - a_free)
    s_high = 4.0 * (t_lo * b_olr + a_olr) / (1.0 - a_ice)
    return s_low, s_high


def part4_ice_albedo():
    section("4. Ice-albedo feedback: one feedback parameter, two climates")
    a_ice, a_free, t_lo, t_hi = 0.62, 0.30, -10.0, 10.0
    a_olr, b_olr = 203.3, 2.09
    print("SYNTHETIC zero-dimensional energy balance model:")
    print("  C dT/dt = (S/4)(1 - alpha(T)) - (A + B T),  T in degrees C")
    print(f"  A = {a_olr:.1f} W/m^2, B = {b_olr:.2f} W/(m^2 K); albedo "
          f"{a_ice:.2f} below {t_lo:.0f} C,")
    print(f"  {a_free:.2f} above {t_hi:.0f} C, linear in between.")
    slope = (a_free - a_ice) / (t_hi - t_lo)
    lam_ice = -(SOLAR / 4.0) * slope
    print(f"\n  ramp slope dalpha/dT = {slope:+.4f} 1/K gives an ice-albedo")
    print(f"  feedback parameter -(S/4) dalpha/dT = {lam_ice:+.2f} W/(m^2 K)")
    print("  inside the band: strongly POSITIVE (destabilising), and it applies")
    print("  only where the albedo is actually changing.")
    print(f"\n{'S (W/m^2)':>10} {'equilibria (C, labelled)':>44} {'N':>3}")
    for sv in (1000.0, 1200.0, 1281.0, 1361.0, 1500.0, 1700.0, 1920.0, 2100.0):
        roots, _ = ice_albedo_equilibria(sv)
        txt = ", ".join(f"{t:7.2f} ({lab})" for lab, t in roots)
        print(f"{sv:10.0f} {txt:>44} {len(roots):3d}")
    s_low, s_high = ice_loop_width()
    print(f"\n  the ice-free branch exists only for S > {s_low:.0f} W/m^2 and the")
    print(f"  ice-covered branch only for S < {s_high:.0f} W/m^2, so between them")
    print(f"  there are three equilibria -- two stable, one on the ramp, unstable")
    print(f"  because lambda_total = {-(SOLAR / 4.0) * slope - b_olr:+.2f} W/(m^2 K) there.")
    print(f"\n{'ramp width (C)':>16} {'S ice-free limit':>18} "
          f"{'S ice limit':>13} {'loop width':>12}")
    for width in (10.0, 20.0, 40.0):
        sl, sh = ice_loop_width(t_lo=-width / 2.0, t_hi=width / 2.0)
        print(f"{width:16.0f} {sl:18.0f} {sh:13.0f} {sh - sl:12.0f}")
    print("\n  a WIDER ramp (a slower albedo transition) gives a NARROWER loop,")
    print("  because the feedback parameter -(S/4)dalpha/dT is smaller. The loop")
    print("  width is therefore a property of the assumed ramp, and its absolute")
    print(f"  size here ({s_high - s_low:.0f} W/m^2, tens of per cent of the solar")
    print("  constant) is a warning that this crude model overstates the reach of")
    print("  the feedback: at 1920 W/m^2 the warm branch is at +63 C, far outside")
    print("  the range where a linear OLR law means anything. What the model")
    print("  demonstrates is the STRUCTURE -- two stable branches, hysteresis,")
    print("  and an unstable branch between them -- not the numbers.")


# ---------------------------------------------------------------------------
# 5. Water vapour: Clausius-Clapeyron
# ---------------------------------------------------------------------------

def part5_water_vapour():
    section("5. Water vapour feedback: the Clausius-Clapeyron rate")
    print("Saturation vapour pressure obeys d(ln e_s)/dT = L/(R_v T^2):")
    print(f"  L = {L_VAP:.2e} J/kg, R_v = {R_VAPOUR:.1f} J/(kg K)")
    print(f"\n{'T (K)':>7} {'T (C)':>7} {'d ln es/dT (1/K)':>18} "
          f"{'per cent per K':>15}")
    for t in (250.0, 273.0, 288.0, 300.0, 310.0):
        rate = L_VAP / (R_VAPOUR * t ** 2)
        print(f"{t:7.0f} {t - 273.15:7.1f} {rate:18.5f} {rate * 100:15.2f}")
    print("\n  the rate FALLS with temperature: about 7.3%/K at freezing and")
    print("  6.3%/K at 288 K, because the same latent heat is spread over a larger")
    print("  T^2. The classic '7% per K' is the mid-tropospheric value.")
    print("  This law gives the CHANGE IN SATURATION, not the feedback. Converting")
    print("  it to a feedback parameter requires assuming how relative humidity")
    print("  changes -- the constant-relative-humidity assumption -- and then")
    print("  computing the resulting change in the water-vapour greenhouse effect.")
    print("  Neither step is taken here: the lesson reports the rate, which is")
    print("  physics, and the feedback parameter, which is an assumption.")


# ---------------------------------------------------------------------------
# 6. Cloud feedback
# ---------------------------------------------------------------------------

def part6_cloud():
    section("6. Cloud feedback: two effects, two signs")
    f_cloud, a_cloud, e_cloud = 0.6, 0.40, 0.80
    sw = SOLAR / 4.0
    lw = SIGMA * T_REF ** 4
    print("Two-effect budget for a cloud fraction f with albedo alpha and")
    print("longwave emissivity epsilon:")
    print("  N_cloud = -f alpha (S/4) + f epsilon sigma T^4")
    print(f"  f = {f_cloud:.2f}, alpha = {a_cloud:.2f}, epsilon = {e_cloud:.2f}, "
          f"S/4 = {sw:.2f}, sigma T^4 = {lw:.1f} W/m^2")
    print("\n  lambda_cloud = -(S/4)[alpha df/dT + f dalpha/dT]")
    print("                 + sigma T^4 [epsilon df/dT + f depsilon/dT]")
    print(f"\n{'df/dT (1/K)':>12} {'dalpha/dT':>10} {'deps/dT':>9} "
          f"{'lambda_cloud':>13} {'sign':>10}")
    cases = [
        (-0.005, 0.000, 0.000), (-0.005, -0.005, 0.000),
        (-0.005, 0.000, -0.005), (0.000, 0.000, 0.005),
        (0.005, 0.010, 0.000), (0.000, -0.010, 0.000),
        (0.005, 0.000, 0.010),
    ]
    vals = []
    for df, da, de in cases:
        lam = -(sw * (a_cloud * df + f_cloud * da)
                - lw * (e_cloud * df + f_cloud * de))
        vals.append(lam)
        print(f"{df:12.3f} {da:10.3f} {de:9.3f} {lam:13.3f} "
              f"{'positive' if lam > 0 else 'negative':>10}")
    print(f"\n  range over these seven defensible combinations: "
          f"[{min(vals):+.2f}, {max(vals):+.2f}] W/(m^2 K)")
    print("  The sign flips. A cloud that reflects more sunlight as it thins")
    print("  gives a negative (stabilising) feedback; a cloud that traps more")
    print("  longwave radiation as it thickens gives a positive one. Both are")
    print("  physically plausible, which is why the cloud feedback is the largest")
    print("  single source of spread in Section 2.")
    print("  These are chosen coefficients of a two-effect accounting model. They")
    print("  are not measurements, and no value here should be quoted as the")
    print("  Earth's cloud feedback.")


# ---------------------------------------------------------------------------
# 7. Carbon-cycle feedback
# ---------------------------------------------------------------------------

def carbon_state(emissions, beta, gamma, lam_eff, c0=800.0, f2x=3.7,
                 n_iter=400):
    """Atmosphere-land-ocean equilibrium with a climate-carbon feedback.

    Atmospheric carbon in excess of a pre-industrial value c0 responds to
    emissions E as  dC = (E - gamma dT)/(1 + beta), where beta is the uptake per
    unit excess (a carbon-concentration parameter) and gamma the additional
    uptake per kelvin of warming (a carbon-climate parameter). The temperature
    follows the logarithmic forcing  F = F_2x ln(1 + dC/c0)/ln 2  divided by the
    effective feedback parameter.
    """
    dc = emissions / (1.0 + beta)
    for _ in range(n_iter):
        f = f2x * np.log(1.0 + dc / c0) / np.log(2.0)
        dt = f / abs(lam_eff)
        dc_new = (emissions - gamma * dt) / (1.0 + beta)
        if abs(dc_new - dc) < 1e-12:
            dc = dc_new
            break
        dc = dc_new
    f = f2x * np.log(1.0 + dc / c0) / np.log(2.0)
    return dc, f, f / abs(lam_eff)


def part7_carbon():
    section("7. Carbon-cycle feedback: beta, gamma and the airborne fraction")
    c0, f2x = 800.0, 3.7
    grams_per_ppm = 2.124             # GtC per ppm, derived in lesson 05
    beta, gamma, lam_eff = 1.0, 100.0, 4.0
    emissions = 1000.0
    print("SYNTHETIC equilibrium carbon budget with chosen coefficients:")
    print(f"  pre-industrial atmosphere c0 = {c0:.0f} GtC "
          f"(= {c0 / grams_per_ppm:.0f} ppm)")
    print(f"  uptake beta = {beta:.2f} per unit excess; climate-carbon "
          f"gamma = {gamma:.0f} GtC/K")
    print(f"  effective |lambda| = {lam_eff:.2f} W/(m^2 K), F_2x = {f2x:.2f} W/m^2")
    print(f"  emitted: {emissions:.0f} GtC")
    dc0, f0, t0 = carbon_state(emissions, beta, 0.0, lam_eff)
    dc1, f1, t1 = carbon_state(emissions, beta, gamma, lam_eff)
    print(f"\n{'case':>22} {'dC (GtC)':>10} {'ppm':>8} {'airborne':>10} "
          f"{'F (W/m^2)':>11} {'dT (K)':>8}")
    for name, dc, f, t in (("without gamma", dc0, f0, t0),
                           ("with gamma", dc1, f1, t1)):
        print(f"{name:>22} {dc:10.1f} {(c0 + dc) / grams_per_ppm:8.0f} "
              f"{dc / emissions:10.3f} {f:11.3f} {t:8.3f}")
    print(f"\n  the climate-carbon feedback reduces the airborne fraction from")
    print(f"  {dc0 / emissions:.3f} to {dc1 / emissions:.3f} and the warming from")
    print(f"  {t0:.3f} K to {t1:.3f} K, a difference of "
          f"{t0 - t1:.3f} K for the same emissions.")
    print(f"\n{'gamma (GtC/K)':>15} {'dC (GtC)':>10} {'airborne':>10} "
          f"{'dT (K)':>8}")
    for g in (0.0, 50.0, 100.0, 200.0, 400.0):
        dc, f, t = carbon_state(emissions, beta, g, lam_eff)
        print(f"{g:15.0f} {dc:10.1f} {dc / emissions:10.3f} {t:8.3f}")
    print("  the warming spans "
          f"{carbon_state(emissions, beta, 400.0, lam_eff)[2]:.2f} to "
          f"{carbon_state(emissions, beta, 0.0, lam_eff)[2]:.2f} K across that")
    print("  range of gamma. As in Section 2, the honest output is the range and")
    print("  the reason for it, not a single value. Note also that this is an")
    print("  EQUILIBRIUM calculation: the real carbon feedback acts over decades")
    print("  to centuries as the ocean and land reservoirs adjust, so a transient")
    print("  calculation would show a smaller effect at first.")


def main():
    part1_planck()
    part2_decomposition()
    part3_linearity()
    part4_ice_albedo()
    part5_water_vapour()
    part6_cloud()
    part7_carbon()
    print("\nAll models and data in this module are SYNTHETIC teaching models.")


if __name__ == "__main__":
    main()
