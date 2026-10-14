#!/usr/bin/env python3
"""Rock magnetism: hysteresis, susceptibility, the Koenigsberger ratio,
blocking volumes and domain state.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python rock_magnetism_demo.py

Everything here is SYNTHETIC.  The loops, susceptibilities, blocking
temperatures and coercivities are chosen teaching-model parameters; no rock
sample, mineral and no published measurement is used.  The only standard
constants are mu0 = 4*pi*1e-7 H/m and k_B = 1.380649e-23 J/K.

Contents
--------
1. A synthetic hysteresis loop: saturation, remanence and coercivity.
2. Coercivity of remanence and three synthetic domain-state regimes.
3. Susceptibility to induced magnetisation and the equivalent field.
4. The Koenigsberger ratio: when remanence beats induction.
5. Blocking volume and the sharpness of blocking.
6. Loop shape versus domain state.
7. Susceptibility versus temperature and the Curie point of the model.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0 = 4.0e-7 * np.pi
KB = 1.380649e-23           # J/K, exact SI

# --- SYNTHETIC teaching material parameters ---------------------------------
JS_AM = 4.0e5               # A/m, saturation magnetisation of the model
HC_AM = 6.0e3               # A/m, loop coercivity
SHARPNESS = 1.82            # loop width parameter, Mr/Ms = tanh(1/SHARPNESS)
K_ANIS_J_M3 = 2.0e4         # J/m^3, anisotropy energy density
T_CURIE_K = 900.0           # K, Curie temperature of the teaching model
KAPPA_SI = 0.045            # dimensionless volume susceptibility

MATERIALS = (
    ("fine/single-domain-like", 8.0e3, 2.0e4, 0.68),
    ("intermediate", 6.0e3, 1.2e4, 1.82),
    ("coarse/multi-domain-like", 2.0e3, 2.6e3, 4.93),
)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def loop_branch(H, js, hc, direction, width):
    """One branch of a synthetic loop: a displaced saturating tanh.

    direction = +1 gives the ascending branch, which crosses zero at H = +hc,
    and -1 the descending branch, crossing zero at H = -hc.  Displacing each
    branch by the coercivity is what makes the loop a loop.  At H = 0 the two
    branches sit at -js tanh(1/width) and +js tanh(1/width), so the model's
    Mr/Ms = tanh(1/width).
    """
    return js * np.tanh((H - direction * hc) / (width * hc))


def loop_metrics(js, hc, width):
    """(Mr/Ms) of the synthetic loop with these parameters."""
    Hs = np.linspace(-3.0e4, 3.0e4, 20001)
    up = loop_branch(Hs, js, hc, +1, width)
    dn = loop_branch(Hs, js, hc, -1, width)
    return 0.5 * abs(float(np.interp(0.0, Hs, dn)) - float(np.interp(0.0, Hs, up)))


def main():
    section("1. A synthetic hysteresis loop")
    H = np.linspace(-3.0e4, 3.0e4, 20001)
    up = loop_branch(H, JS_AM, HC_AM, +1, SHARPNESS)
    dn = loop_branch(H, JS_AM, HC_AM, -1, SHARPNESS)
    Ms = float(np.max(np.abs(np.concatenate([up, dn]))))
    Mr = loop_metrics(JS_AM, HC_AM, SHARPNESS)
    print(f"SYNTHETIC material: Js = {JS_AM:.3e} A/m, loop coercivity "
          f"Hc = {HC_AM:.3e} A/m,")
    print(f"loop width parameter = {SHARPNESS:.2f}")
    print(f"  J/Js at H = 0: ascending branch "
          f"{float(np.interp(0.0, H, up))/JS_AM:+.4f}, descending branch "
          f"{float(np.interp(0.0, H, dn))/JS_AM:+.4f}")
    print(f"  saturation magnetisation Ms = {Ms:.3e} A/m")
    print(f"  saturation remanence Mr = {Mr:.3e} A/m")
    print(f"  ratio Mr/Ms = {Mr/Ms:.4f}  (model value tanh(1/{SHARPNESS:.2f}) "
          f"= {np.tanh(1.0/SHARPNESS):.4f})")
    print(f"  coercivity in field units: mu0 Hc = {MU0*HC_AM*1e6:.4f} "
          "microtesla")
    print("  the loop is open by construction; a real measurement adds noise and")
    print("  the two branches are never exactly symmetric.")

    section("2. Coercivity of remanence and domain-state regimes")
    print("  Hcr is a SECOND, independent property of this model: the back field")
    print("  that removes a saturation remanence.  Three SYNTHETIC materials:")
    print("  material                   Hc (A/m)   Hcr (A/m)   Hcr/Hc    Mr/Ms")
    for name, hc, hcr, width in MATERIALS:
        print(f"  {name:25s} {hc:9.3e}  {hcr:9.3e}   {hcr/hc:7.3f}   "
              f"{loop_metrics(JS_AM, hc, width)/JS_AM:6.4f}")
    print("  fine, stable grains give high Mr/Ms and high Hcr/Hc; coarse grains")
    print("  give low values of both.  This model does not generate the regime")
    print("  boundaries, so none are quoted; the pairs were chosen, not measured.")

    section("3. Susceptibility to induced magnetisation")
    print(f"SYNTHETIC volume susceptibility kappa = {KAPPA_SI:.4f} "
          "(SI, dimensionless)")
    for B_nT in (50000.0, 100000.0):
        H_eff = B_nT * 1.0e-9 / MU0
        J_ind = KAPPA_SI * H_eff
        print(f"  ambient field {B_nT:.0f} nT -> H = {H_eff:.4f} A/m -> "
              f"J = kappa H = {J_ind:.6f} A/m")
        print(f"    equivalent flux density mu0 J = {MU0*J_ind*1e9:.3f} nT = "
              f"{100*MU0*J_ind/(B_nT*1e-9):.4f}% of the ambient field")
    print("  susceptibility is the ratio of induced magnetisation to the")
    print("  inducing field; it is not a remanence and it vanishes with H.")

    section("4. The Koenigsberger ratio")
    H_amb = 50000.0e-9 / MU0
    print(f"  with kappa = {KAPPA_SI:.4f} in a 50000 nT field, "
          f"H = {H_amb:.4f} A/m, so kappa H = {KAPPA_SI*H_amb:.4f} A/m")
    for Jr in (1.0e-2, 1.0e-1, 1.0, 10.0):
        Q = Jr / (KAPPA_SI * H_amb)
        print(f"    Jr = {Jr:8.3f} A/m -> Q = {Q:9.4f} "
              f"({'remanence-dominated' if Q > 1 else 'induced-dominated'})")
    print(f"  the crossover Q = 1 sits at Jr = {KAPPA_SI*H_amb:.4f} A/m.")
    print("  Q depends on the ambient field, so it is a property of the rock IN")
    print("  ITS FIELD, not a material constant.")

    section("5. Blocking volume and the sharpness of blocking")
    tau0, tau_obs = 1.0e-9, 100.0
    print(f"SYNTHETIC parameters: attempt time tau0 = {tau0:.1e} s, "
          f"observation time tau = {tau_obs:.0f} s")
    print(f"  the argument ln(tau/tau0) = {np.log(tau_obs/tau0):.4f}")
    print("   T (K)    blocking volume (m^3)   equivalent diameter (nm)")
    for T in (300.0, 500.0, 700.0, 800.0):
        Vb = KB * T * np.log(tau_obs / tau0) / K_ANIS_J_M3
        dia = (6.0 * Vb / np.pi) ** (1.0 / 3.0) * 1.0e9
        print(f"  {T:6.1f}   {Vb:22.4e}   {dia:21.3f}")
    print("  the blocking volume grows only linearly in T while the logarithmic")
    print("  factor is fixed, so a modest temperature change moves grains across")
    print("  the threshold - which is why blocking looks sharp in practice.")

    section("6. Loop shape versus domain state")
    print("  the same formula with different loop widths, at fixed Js = "
          f"{JS_AM:.1e} A/m:")
    print("  width    Mr/Ms    Hc (A/m)   comment")
    for width, hc, name in ((0.68, 8.0e3, "narrow loop, high remanence"),
                            (1.82, 6.0e3, "intermediate"),
                            (4.93, 2.0e3, "flat loop, low remanence")):
        print(f"  {width:6.2f}   {loop_metrics(JS_AM, hc, width)/JS_AM:6.4f}   "
              f"{hc:9.3e}   {name}")
    print("  the width parameter sets Mr/Ms through tanh(1/width), so width and")
    print("  Mr/Ms are not independent here: a limitation to state, not to hide.")

    section("7. Susceptibility versus temperature and the Curie point")
    T = np.linspace(250.0, 1000.0, 16)
    kap = KAPPA_SI * np.maximum(1.0 - T / T_CURIE_K, 0.0) ** 0.5
    print(f"SYNTHETIC Curie temperature of the model: T_C = {T_CURIE_K:.1f} K = "
          f"{T_CURIE_K - 273.15:.1f} deg C")
    print("   T (K)   T (deg C)   kappa(T)/kappa(250 K)")
    for tt, kk in zip(T, kap):
        print(f"  {tt:6.1f}   {tt-273.15:9.1f}   {kk/KAPPA_SI:18.6f}")
    print("  above T_C the model has no spontaneous magnetisation, so remanence")
    print("  is gone and only induced magnetisation remains.  Heating through T_C")
    print("  and cooling is therefore the standard test that separates a")
    print("  remanence from an induced magnetisation.")


if __name__ == "__main__":
    main()
