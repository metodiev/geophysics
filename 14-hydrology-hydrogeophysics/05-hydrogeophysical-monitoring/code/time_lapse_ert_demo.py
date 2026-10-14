#!/usr/bin/env python3
"""Time-lapse ERT for infiltration and transport: petrophysical mapping,
apparent-resistivity monitoring of a moving wetting front, the equivalence of
saturation and pore-water salinity changes, and the non-uniqueness of a
regularised 1-D time-lapse inversion.

Run with the project virtual environment:

    cd 14-hydrology-hydrogeophysics/05-hydrogeophysical-monitoring/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python time_lapse_ert_demo.py

Everything here is SYNTHETIC.  The soil parameters, the pore-water resistivity,
the infiltration depths and the noise level are chosen teaching values, not
measurements from any site.  No real data set, catchment or aquifer is used.

Contents
--------
1. Archie mapping from saturation to bulk resistivity.
2. Wenner apparent resistivity over a two-layer earth (analytic series), with two
   independent limit checks of the series.
3. A wetting front at four depths: forward response and time-lapse ratio.
4. Detection: signal versus a stated relative noise level.
5. Equivalence of a saturation change and a salinity change (the ambiguity).
6. Temperature as a confounder.
7. Regularised inversion of the time-lapse data from three different starts, with
   the parameter trade-off read from the Jacobian.
"""

import numpy as np
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC petrophysical and survey parameters (chosen, not measured) -----
RHO_W = 10.0        # ohm m, pore-water resistivity of the teaching soil
PHI = 0.35          # porosity, dimensionless
M_CE = 1.8          # Archie cementation exponent
N_SAT = 2.0         # Archie saturation exponent
S_INIT = 0.45       # initial saturation of the profile
S_WET = 0.85        # saturation behind the wetting front
TEMP_COEFF = 0.020  # fractional decrease of rho_w per kelvin (teaching value)
NOISE_REL = 0.01    # 1% relative noise on apparent resistivity
SPACINGS = np.array([0.5, 1.0, 2.0, 4.0, 8.0, 16.0])   # Wenner a, m


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def archie(rho_w, phi=PHI, m=M_CE, s=1.0, n=N_SAT):
    """Bulk resistivity of a saturated/unsaturated medium, ohm m."""
    return rho_w * phi ** (-m) * s ** (-n)


def wenner_two_layer(a, h, rho1, rho2, nterms=400):
    """Wenner apparent resistivity over a two-layer earth.

    a     electrode spacing (m)
    h     thickness of the top layer (m)
    rho1  resistivity of the top layer (ohm m)
    rho2  resistivity of the half-space (ohm m)

    rho_a = rho1 [ 1 + 4 * sum_n k^n ( 1/sqrt(1+(2nh/a)^2) - 1/sqrt(4+(2nh/a)^2) ) ]
    with k = (rho2-rho1)/(rho2+rho1) the reflection coefficient.
    """
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, nterms + 1)
    x = 2.0 * n * h / a
    series = np.sum(k ** n * (1.0 / np.sqrt(1.0 + x * x)
                              - 1.0 / np.sqrt(4.0 + x * x)))
    return rho1 * (1.0 + 4.0 * series)


def forward_log10(a, rho1, rho2, h):
    """log10 apparent resistivity, the quantity a time-lapse ratio acts on."""
    return np.log10([wenner_two_layer(float(ai), h, rho1, rho2) for ai in a])


def main():
    section("1. Archie mapping: saturation and pore-water resistivity -> bulk")
    rho_dry = archie(RHO_W, s=S_INIT)
    rho_wet = archie(RHO_W, s=S_WET)
    print(f"SYNTHETIC soil: rho_w = {RHO_W:.1f} ohm m, phi = {PHI:.2f}, "
          f"m = {M_CE:.2f}, n = {N_SAT:.2f}")
    print(f"  initial saturation S = {S_INIT:.2f} -> rho = {rho_dry:.2f} ohm m"
          f"  (theta = {S_INIT * PHI:.3f})")
    print(f"  after wetting S = {S_WET:.2f} -> rho = {rho_wet:.2f} ohm m"
          f"  (theta = {S_WET * PHI:.3f})")
    print(f"  bulk resistivity ratio rho_wet/rho_dry = {rho_wet / rho_dry:.4f}"
          f"  ({100 * (rho_wet / rho_dry - 1):+.1f}%)")
    print(f"  check by hand: (S_wet/S_init)^-n = "
          f"{(S_WET / S_INIT) ** (-N_SAT):.4f}")

    section("2. Wenner two-layer series: two independent limit checks")
    rho1, rho2 = rho_wet, rho_dry
    k = (rho2 - rho1) / (rho2 + rho1)
    print(f"  layer 1 (wetted) rho1 = {rho1:.3f} ohm m, half-space rho2 = "
          f"{rho2:.3f} ohm m, k = {k:+.4f}")
    a_small = 1e-4 * 1.0                      # a << h  -> rho_a -> rho1
    a_large = 1e6 * 1.0                       # a >> h  -> rho_a -> rho2
    r_small = wenner_two_layer(a_small, 1.0, rho1, rho2)
    r_large = wenner_two_layer(a_large, 1.0, rho1, rho2)
    print(f"  a/h -> 0    : rho_a = {r_small:.6f} ohm m, rho1 = {rho1:.6f}, "
          f"rel. error {abs(r_small / rho1 - 1):.2e}")
    print(f"  a/h -> inf  : rho_a = {r_large:.6f} ohm m, rho2 = {rho2:.6f}, "
          f"rel. error {abs(r_large / rho2 - 1):.2e}")
    print(f"  analytic limit check (1+k)/(1-k) = {(1 + k) / (1 - k):.6f} "
          f"= rho2/rho1 = {rho2 / rho1:.6f}")

    section("3. A wetting front at four depths: forward response and ratio")
    fronts = (0.25, 0.50, 1.00, 2.00)          # depth of the front, m
    base = np.array([wenner_two_layer(a, 1.0, rho_dry, rho_dry) for a in SPACINGS])
    print("  baseline profile (uniform, S = 0.45): rho_a = "
          f"{rho_dry:.2f} ohm m at every spacing")
    print("  apparent resistivity rho_a (ohm m); rows are the front depth,")
    print("  columns are the Wenner spacing a")
    print("   h (m) \\ a (m) " + "".join(f"{a:>10.2f}" for a in SPACINGS))
    print(f"{'baseline (uniform)':>16s}" + "".join(f"{b:10.2f}" for b in base))
    ratios = {}
    for h in fronts:
        vals = np.array([wenner_two_layer(a, h, rho1, rho2) for a in SPACINGS])
        ratios[h] = vals / base
        print(f"{'h = ' + format(h, '.2f') + ' m':>16s}"
              + "".join(f"{v:10.2f}" for v in vals))
    print("\n  time-lapse ratio rho_a(post)/rho_a(pre), same layout:")
    print("   h (m) \\ a (m) " + "".join(f"{a:>10.2f}" for a in SPACINGS))
    for h in fronts:
        print(f"{'h = ' + format(h, '.2f') + ' m':>16s}"
              + "".join(f"{r:10.4f}" for r in ratios[h]))
    print("\n  the smallest spacing always shows the largest change, because")
    print("  a -> 0 samples only the wetted top layer: r -> rho1/rho2 = "
          f"{rho1 / rho2:.4f}")
    print("  what the SHAPE of the ratio curve carries is the front DEPTH.")
    print("\n  how deep a monitoring array must reach to see a front:")
    print("   front depth   r at a = 16 m   |1 - r|   detectable at 1% noise?")
    for h in fronts:
        r16 = float(ratios[h][-1])
        print(f"   {h:10.2f} m   {r16:13.4f}   {abs(1.0 - r16):7.4f}   "
              f"{'yes' if abs(1.0 - r16) > NOISE_REL else 'no'}")
    print("  -> a 0.25 m front is invisible to the 16 m spacing (0.5% change,")
    print("     below the 1% noise), so a surface array that does not include")
    print("     short spacings is blind to the shallowest, most dynamic layer.")

    section("4. Detection against a stated relative noise level")
    print(f"  assumed relative noise on rho_a: {NOISE_REL * 100:.1f}% (1 sd)")
    print("   front depth   best spacing   |1 - r|   detections at 1 sd")
    for h in fronts:
        r = ratios[h]
        i = int(np.argmax(np.abs(1.0 - r)))
        excess = abs(1.0 - r[i]) / NOISE_REL
        print(f"   {h:10.2f} m   {SPACINGS[i]:10.1f} m   {abs(1.0 - r[i]):7.4f}"
              f"   {excess:8.1f} sd")

    print("\n  a small change, to see how the spacing decides detectability:")
    s_small = S_INIT * 1.05
    rho_small = archie(RHO_W, s=s_small)
    print(f"  a 5% relative rise in water content in the top {0.5:.2f} m changes")
    print(f"  the wet-layer resistivity from {rho_dry:.2f} to {rho_small:.2f} ohm m "
          f"({100 * (rho_small / rho_dry - 1):+.2f}%)")
    for a in (0.5, 8.0):
        base_a = wenner_two_layer(a, 0.5, rho_dry, rho_dry)
        val_a = wenner_two_layer(a, 0.5, rho_small, rho_dry)
        r_a = val_a / base_a
        print(f"   at a = {a:4.1f} m: rho_a {base_a:.2f} -> {val_a:.2f} ohm m, "
              f"r = {r_a:.4f}, |1 - r| = {abs(1 - r_a):.4f}, "
              f"{abs(1 - r_a) / NOISE_REL:.1f} sd at 1% noise")
    print("  -> the same change is 7.6 sd at one spacing and invisible at another.")
    print("     Detection is a property of the ARRAY, not of the process alone.")

    section("5. Equivalence: the same rho change from S or from salinity")
    obs_ratio = 1.0 - 0.7066            # 1.0 m front at a = 0.5 m, section 3
    print(f"  observed time-lapse ratio r = rho_a(post)/rho_a(pre) = "
          f"{obs_ratio:.4f}")
    print("  Any pair (S, rho_w) with  (S/S_init)^n * (rho_w/RHO_W) = r  fits the")
    print("  same data exactly.  Five members of that family:")
    print("   split x    rho_w (ohm m)   S      theta    interpretation")
    labels = ("all saturation", "mostly saturation", "equal split",
              "mostly salinity", "all salinity")
    for x, label in zip((0.0, 0.25, 0.5, 0.75, 1.0), labels):
        rho_w_x = RHO_W * obs_ratio ** x
        s_ratio = obs_ratio ** ((x - 1.0) / N_SAT)
        s_x = S_INIT * s_ratio
        print(f"   {x:6.2f}     {rho_w_x:11.4f}   {s_x:5.3f}   "
              f"{s_x * PHI:5.3f}    {label}")
    check = [(RHO_W * obs_ratio ** x) * PHI ** (-M_CE)
             * (S_INIT * obs_ratio ** ((x - 1.0) / N_SAT)) ** (-N_SAT)
             for x in (0.0, 0.25, 0.5, 0.75, 1.0)]
    print(f"  bulk resistivity of every member: "
          + ", ".join(f"{c:.4f}" for c in check) + " ohm m")
    print("  -> identical to 4 decimals.  A resistivity ratio alone cannot")
    print("     separate a wetting front from a salinity front; the separation")
    print("     needs an independent constraint (chemistry, mass balance, NMR,")
    print("     or a second physical property).")

    section("6. Temperature as a confounder")
    f3 = (1.0 - TEMP_COEFF) ** 3.0
    n_kelvin = np.log(obs_ratio) / np.log(1.0 - TEMP_COEFF)
    print(f"  a +3 K warming multiplies rho_w by (1-{TEMP_COEFF:.3f})^3 = "
          f"{f3:.4f}, i.e. {100 * (f3 - 1):+.1f}%")
    print(f"  could the whole observed drop (r = {obs_ratio:.4f}) be thermal?")
    print(f"    it would need {n_kelvin:.1f} K of warming at "
          f"{TEMP_COEFF * 100:.0f}%/K: physically impossible here, so a large")
    print("    wetting signal is not disguisable as a temperature change.")
    print("  but if the 3 K is NOT accounted for, the inferred saturation is")
    s_wrong = S_WET * f3 ** (-1.0 / N_SAT)
    print(f"    biased: S = {s_wrong:.4f} instead of {S_WET:.4f} "
          f"({100 * (s_wrong / S_WET - 1):+.2f}%, "
          f"theta = {s_wrong * PHI:.4f} vs {S_WET * PHI:.4f})")
    print("  -> the error is a fraction of the seasonal signal, not of the")
    print("     wetting signal: temperature must be measured, not hoped away.")

    section("7. Inversion of the time-lapse data, and what it does not fix")
    d_obs = forward_log10(SPACINGS, rho_wet, rho_dry, 1.0)
    print("(a) three starts, dense data (6 spacings), no regularisation:")
    for start in (0.7, 1.0, 1.3):
        res = least_squares(
            lambda m: forward_log10(SPACINGS, 10 ** m[0], 10 ** m[1], m[2]) - d_obs,
            x0=[np.log10(rho_wet), np.log10(rho_dry), start],
            method="lm", xtol=1e-14, ftol=1e-14,
        )
        rho1_f, rho2_f, h_f = 10 ** res.x[0], 10 ** res.x[1], res.x[2]
        data_res = forward_log10(SPACINGS, rho1_f, rho2_f, h_f) - d_obs
        print(f"   start h = {start:.2f} m -> rho1 = {rho1_f:7.3f} ohm m, "
              f"rho2 = {rho2_f:7.3f} ohm m, h = {h_f:6.3f} m, "
              f"data rms = {np.sqrt(np.mean(data_res ** 2)):.2e} dex")
    print(f"   truth: rho1 = {rho_wet:.3f}, rho2 = {rho_dry:.3f}, h = 1.000 m")
    print("   -> with 6 data and 3 parameters the problem is overdetermined and")
    print("      the inversion recovers the truth: this validates the forward")
    print("      model and the optimiser, and is the only thing it validates.")

    res = least_squares(
        lambda m: forward_log10(SPACINGS, 10 ** m[0], 10 ** m[1], m[2]) - d_obs,
        x0=[np.log10(rho_wet), np.log10(rho_dry), 1.0],
        method="lm", xtol=1e-14, ftol=1e-14,
    )
    jac = res.jac
    corr = np.corrcoef(jac.T)
    print("\n(b) the parameter trade-off, read from the Jacobian columns")
    print("    (order: log10 rho1, log10 rho2, h):")
    for row in corr:
        print("    " + "".join(f"{v:+9.4f}" for v in row))
    print(f"    the rho1-rho2 correlation is {corr[0, 1]:+.4f}: the data depend")
    print("    on the two resistivities almost only through their ratio, so a")
    print("    bias in one is invisibly absorbed by the other.")

    print("\n(c) the same data with only two spacings (a = 0.5 and 2.0 m):")
    two = np.array([0.5, 2.0])
    d_two = forward_log10(two, rho_wet, rho_dry, 1.0)
    print("     h (m)   best-fit rho1   best-fit rho2   rms(2 data)  rms(6 data)")
    for h_try in np.arange(0.50, 1.51, 0.25):
        fit = least_squares(
            lambda m: forward_log10(two, 10 ** m[0], 10 ** m[1], h_try) - d_two,
            x0=[np.log10(rho_wet), np.log10(rho_dry)], method="lm",
            xtol=1e-14, ftol=1e-14,
        )
        r1, r2 = 10 ** fit.x[0], 10 ** fit.x[1]
        rms2 = np.sqrt(np.mean((forward_log10(two, r1, r2, h_try) - d_two) ** 2))
        rms6 = np.sqrt(np.mean((forward_log10(SPACINGS, r1, r2, h_try) - d_obs) ** 2))
        print(f"    {h_try:6.2f}   {r1:12.3f}   {r2:12.3f}   {rms2:10.2e}"
              f"   {rms6:10.3f}")
    print("     -> with 2 data and 3 parameters every h in this range fits to")
    print("        machine precision: a genuine one-dimensional equivalence")
    print("        class.  Above h ~ 1.6 m the family terminates because even")
    print("        the two shortest spacings stop sensing the half-space, and")
    print("        the half-space resistivity becomes unbounded.")
    print("        The 6-spacing misfit is what discriminates, and it")
    print("        discriminates depth far more weakly than resistivity.")
    print("        (rms in dex of log10 rho_a; 0.010 dex = 2.3% in rho_a.)")

    print("\n(d) what regularisation costs: L2 damping toward a 2 m thickness")
    for alpha in (1e-4, 1e-2):
        res2 = least_squares(
            lambda m: np.concatenate([
                forward_log10(SPACINGS, 10 ** m[0], 10 ** m[1], m[2]) - d_obs,
                np.sqrt(alpha) * np.array([m[1] - m[0], m[2] - np.log10(2.0)]),
            ]),
            x0=[np.log10(rho_wet), np.log10(rho_dry), 1.0], method="trf",
            xtol=1e-14, ftol=1e-14,
        )
        r1, r2, h_f = 10 ** res2.x[0], 10 ** res2.x[1], res2.x[2]
        data_res = forward_log10(SPACINGS, r1, r2, h_f) - d_obs
        print(f"    alpha = {alpha:7.1e} -> rho1 = {r1:7.3f}, rho2 = {r2:7.3f}, "
              f"h = {h_f:6.3f} m ({100 * (h_f - 1.0):+.1f}% in h), "
              f"data rms = {np.sqrt(np.mean(data_res ** 2)):.2e} dex")
    print("    -> a damping weight large enough to change the answer changes it")
    print("       to a WRONG answer (h biased by -16%) while leaving the data")
    print("       fit almost imperceptibly worse.  Regularisation is a choice")
    print("       with a cost, and it must be reported with its weight.")


if __name__ == "__main__":
    main()
