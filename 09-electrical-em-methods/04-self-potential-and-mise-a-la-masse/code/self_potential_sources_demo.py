#!/usr/bin/env python3
"""Self-potential sources: electrokinetic coupling, electrochemical (Nernst)
cell potentials, membrane/diffusion potentials, and the buried-dipole forward
model used to read a depth from a surface profile.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python self_potential_sources_demo.py

Everything is SYNTHETIC.  The coupling coefficient, the redox couples, the
surface potentials and the source geometry are chosen teaching values, not
measurements of any real site, fluid, ore body or instrument.  The physical
constants used (epsilon_0, g, R, F, the standard electrode potentials) are
standard values with their units stated.

Contents
--------
1. Electrokinetic (streaming) coupling coefficient and the head it needs.
2. Nernst electrochemical potentials for synthetic redox couples.
3. Membrane / liquid-junction potentials versus transference number.
4. Forward model: a buried current dipole in a half-space, by the image method.
5. Depth from profile width, and the non-uniqueness of (depth, length, current).
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- standard constants (exact or conventional values, with units) -----------
EPS0 = 8.8541878128e-12     # F/m, vacuum permittivity (exact by definition)
G = 9.80665                 # m/s^2, standard gravity (exact by definition)
R_GAS = 8.314462618         # J/(mol K), molar gas constant (exact by definition)
FARADAY = 96485.33212       # C/mol, Faraday constant (exact by definition)
T_REF = 298.15              # K, 25 degC (defined)

# --- SYNTHETIC model parameters (chosen, not measured) ----------------------
EPS_R_WATER = 80.1          # assumed relative permittivity of pore water
ZETA = -20.0e-3             # V, assumed zeta potential of the mineral surfaces
ETA = 1.0e-3                # Pa s, assumed dynamic viscosity of water
RHO_W = 1000.0              # kg/m^3, assumed density of water
SIGMA_ROCK = 0.010          # S/m, assumed bulk conductivity of the rock


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def streaming_coefficient(sigma_s_m, zeta=ZETA, eps_r=EPS_R_WATER, eta=ETA):
    """Helmholtz-Smoluchowski coupling coefficient dV/dP in V/Pa."""
    eps = eps_r * EPS0
    return eps * zeta / (eta * sigma_s_m)


def head_to_pressure(h_m, rho=RHO_W, g=G):
    """Pressure in Pa at the base of a column of water of height h_m."""
    return rho * g * h_m


def dipole_profile(x_m, depth_m, length_m, current_a, sigma_s_m):
    """Surface potential of a buried vertical current dipole in a half-space.

    A current source at depth (depth - length/2) and a sink at
    (depth + length/2), both in a half-space with an insulating surface.  The
    insulating boundary is handled by the image method: each electrode is
    mirrored with the same sign, so a single source at depth z0 contributes

        V(x) = I / (4 pi sigma) [ 1/r + 1/r_image ],   r = sqrt(x^2 + z0^2),

    which reduces to the familiar half-space value I/(2 pi sigma r) on the
    surface.  Returns volts.
    """
    x = np.asarray(x_m, dtype=float)
    z_src = depth_m - 0.5 * length_m
    z_snk = depth_m + 0.5 * length_m
    if z_src <= 0.0:
        raise ValueError("the source electrode would be at or above the surface")
    r_src = np.sqrt(x ** 2 + z_src ** 2)
    r_snk = np.sqrt(x ** 2 + z_snk ** 2)
    return (current_a / (4.0 * np.pi * sigma_s_m)) * (
        2.0 / r_src - 2.0 / r_snk)


def main():
    section("1. Electrokinetic coupling: dV/dP from Helmholtz-Smoluchowski")
    eps = EPS_R_WATER * EPS0
    print("dV/dP = eps zeta / (eta sigma),  eps = eps_r eps_0")
    print(f"  eps_0 = {EPS0:.6e} F/m, eps_r = {EPS_R_WATER:.1f} (assumed)")
    print(f"  zeta  = {1000 * ZETA:.2f} mV (assumed), eta = {ETA:.1e} Pa s, "
          f"rho_w = {RHO_W:.0f} kg/m^3, g = {G:.5f} m/s^2")
    print(f"  eps = {eps:.6e} F/m; 1 m of water head = "
          f"{head_to_pressure(1.0):.1f} Pa")
    print("\n  sigma (S/m)   dV/dP (V/Pa)      dV/dh (mV per m of head)   "
          "head for 10 mV (m)")
    for sigma in (0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0):
        cs = streaming_coefficient(sigma)
        dv_dh = 1000.0 * cs * head_to_pressure(1.0)
        head_for_10mv = 0.010 / abs(dv_dh / 1000.0)
        print(f"  {sigma:9.3f}   {cs:+.6e}      {dv_dh:+12.3f}          "
              f"{head_for_10mv:10.3f}")
    print("the coefficient falls as 1/sigma because a more conductive pore fluid")
    print("screens the streaming current: the same head produces a smaller")
    print("voltage, and the head needed for a given anomaly grows linearly.")
    print("with zeta < 0 the sign is negative: the potential increases in the")
    print("direction of flow, which is the convention tested in lesson 02.")

    section("2. Electrochemical potentials: Nernst and standard couples")
    nernst_slope = R_GAS * T_REF / FARADAY * 1000.0
    print(f"RT/F at T = {T_REF:.2f} K = {nernst_slope:.3f} mV")
    print(f"(RT/F) ln(10) = {nernst_slope * np.log(10.0):.3f} mV per decade of "
          f"activity ratio")
    print("standard reduction potentials (V versus the standard hydrogen")
    print("electrode, 25 degC, unit activity):")
    couples = {"O2/H2O": 1.229, "Fe3+/Fe2+": 0.771, "Cu2+/Cu": 0.342,
               "H+/H2": 0.000, "Zn2+/Zn": -0.762}
    for name, e0 in couples.items():
        print(f"   {name:12s} E0 = {e0:+.3f} V")
    print("\n  cell (cathode / anode)          E0 cell (V)   decades for 100 mV")
    for cath, an in (("O2/H2O", "Fe3+/Fe2+"), ("O2/H2O", "Cu2+/Cu"),
                     ("Cu2+/Cu", "Zn2+/Zn"), ("Fe3+/Fe2+", "Fe3+/Fe2+")):
        e_cell = couples[cath] - couples[an]
        decades = 0.100 / (nernst_slope * np.log(10.0) / 1000.0)
        print(f"  {cath:12s} / {an:12s}   {e_cell:+9.3f}   "
              f"{decades if e_cell != 0.0 else float('nan'):14.2f}")
    print("a redox cell of this kind is what a polarised mineral body presents")
    print("to the ground: a potential difference of order a few hundred mV")
    print(f"({nernst_slope * np.log(10.0) / 1000.0:.4f} V per decade of activity")
    print("ratio), which is why electrochemical SP anomalies are of order tens")
    print("to hundreds of millivolts while electrokinetic ones are of order")
    print("tens of millivolts for realistic heads.")
    print("\nworked example: one decade of activity ratio on a single-electron")
    print(f"couple gives {nernst_slope * np.log(10.0):.3f} mV; ten decades give "
          f"{10 * nernst_slope * np.log(10.0) / 1000.0:.3f} V.")
    print("only a few decades are chemically available, which caps the")
    print("electrochemical contribution at a few hundred millivolts.")

    section("3. Membrane / liquid-junction potential versus transference number")
    ratio = 10.0
    print("for a 1:1 electrolyte between two reservoirs whose activities differ")
    print(f"by a factor {ratio:.0f}, the diffusion potential is")
    print("   E = (RT/F) (t+ - t-) ln(a1/a2),   t+ + t- = 1")
    print(f"with (RT/F) = {nernst_slope:.3f} mV and ln({ratio:.0f}) = "
          f"{np.log(ratio):.4f}")
    print("\n  t+      E (mV)     interpretation")
    for tp in (0.20, 0.40, 0.50, 0.60, 0.80, 1.00):
        e = nernst_slope * (tp - (1.0 - tp)) * np.log(ratio)
        if abs(tp - 0.5) < 1e-9:
            note = "no membrane selectivity: E = 0"
        elif tp > 0.5:
            note = "cation-selective (clay-like surface)"
        else:
            note = "anion-selective"
        print(f"  {tp:4.2f}   {e:+8.3f}   {note}")
    print("a perfectly cation-selective membrane (t+ = 1) gives the full Nernst")
    print(f"potential of {nernst_slope * np.log(ratio):.3f} mV per decade of")
    print("activity ratio - the largest electrochemical SP source a clay")
    print("membrane can produce, and the reason SP logs respond to salinity")
    print("contrasts across shale beds.")

    section("4. Forward model: a buried current dipole in a half-space")
    depth, length, current, sigma = 40.0, 20.0, 0.10, SIGMA_ROCK
    x = np.linspace(-200.0, 200.0, 401)
    v = dipole_profile(x, depth, length, current, sigma)
    print(f"model: source at {depth - length / 2:.1f} m, sink at "
          f"{depth + length / 2:.1f} m, I = {current:.3f} A, "
          f"sigma = {sigma:.4f} S/m")
    print(f"half-space single source check: I/(2 pi sigma r) at r = "
          f"{depth:.1f} m = {current / (2 * np.pi * sigma * depth) * 1000:.3f} mV")
    print(f"profile: {x[0]:.0f} to {x[-1]:.0f} m, peak = "
          f"{1000 * v.max():.3f} mV at x = {x[np.argmax(v)]:.1f} m")
    print(f"value at the edge of the profile (x = {x[-1]:.0f} m) = "
          f"{1000 * v[-1]:.3f} mV, i.e. {100 * v[-1] / v.max():.1f}% of the peak:")
    print("a vertical source-above-sink dipole gives a single-signed positive")
    print("lobe in this model, so there is no trough to measure.")
    half = 1000.0 * 0.5 * v.max()
    above = np.where(v >= 0.5 * v.max())[0]
    width = x[above[-1]] - x[above[0]] if above.size > 1 else np.nan
    print(f"half-width of the positive lobe = {width:.1f} m; "
          f"width / depth = {width / depth:.3f}")
    print("\n  depth (m)   length (m)   peak (mV)   half-width (m)   "
          "width / depth")
    for d in (20.0, 40.0, 80.0, 160.0):
        vv = dipole_profile(x, d, length, current, sigma)
        ab = np.where(vv >= 0.5 * vv.max())[0]
        w = x[ab[-1]] - x[ab[0]] if ab.size > 1 else np.nan
        print(f"  {d:9.1f}   {length:10.1f}   {1000 * vv.max():9.3f}   "
              f"{w:14.1f}   {w / d:13.3f}")
    print("the width ratio is the depth information in the shape; the amplitude")
    print(f"falls off with depth (peak {1000 * dipole_profile(np.array([0.0]), 20.0, length, current, sigma)[0]:.3f}"
          f" mV at 20 m against "
          f"{1000 * dipole_profile(np.array([0.0]), 160.0, length, current, sigma)[0]:.3f} mV at 160 m),")
    print("so a stronger source at greater depth can produce the same profile.")
    print("\ntwo analytic checks of the width rule:")
    xf = np.linspace(-400.0, 400.0, 80001)
    for label, d, ln in (("point source (monopole)", 0.0, 0.0),
                         ("point dipole, L = 1 m", 100.0, 1.0)):
        if ln == 0.0:
            h = 100.0
            vf = current / (2.0 * np.pi * sigma * np.sqrt(xf ** 2 + h ** 2))
            exp_ratio = 2.0 * np.sqrt(3.0)
            note = "2 sqrt(3)"
        else:
            vf = dipole_profile(xf, d, ln, current, sigma)
            exp_ratio = 2.0 * np.sqrt(2.0 ** (2.0 / 3.0) - 1.0)
            note = "2 sqrt(2^(2/3) - 1)"
        ab = np.where(vf >= 0.5 * vf.max())[0]
        w = xf[ab[-1]] - xf[ab[0]]
        print(f"   {label:24s}: measured FWHM/depth = {w / (h if ln == 0.0 else d):.4f},"
              f" analytic {note} = {exp_ratio:.4f}")
    print("the monopole result follows from 1/sqrt(x^2+h^2) = 1/(2h) and the")
    print("dipole result from h/(x^2+h^2)^(3/2) = 1/(2h^2); both are exact, and")
    print("both reproduce the measured profile, which validates the image sum.")

    section("5. Non-uniqueness: which (depth, length, current) are admitted?")
    xd = np.linspace(-200.0, 200.0, 41)
    true_d, true_l, true_i = 40.0, 20.0, 0.10
    clean = dipole_profile(xd, true_d, true_l, true_i, sigma)
    noise = 0.02 * clean.max() * RNG.standard_normal(xd.size)
    obs = clean + noise
    sigma_n = np.std(noise)
    print(f"SYNTHETIC data: {xd.size} stations over {xd[-1] - xd[0]:.0f} m, "
          f"noise rms = {1000 * sigma_n:.4f} mV "
          f"({100 * sigma_n / clean.max():.1f}% of the peak)")
    print("grid search over (depth, length) with the current solved in the")
    print("least-squares sense at each node (the model is linear in the")
    print("current).  Admitted means chi2 <= chi2_min + 4.")
    depths = np.arange(20.0, 100.1, 2.0)
    lengths = np.arange(4.0, 80.1, 2.0)   # combinations with z_source <= 0 are
                                          # excluded below
    chi2 = np.zeros((depths.size, lengths.size))
    amps = np.zeros_like(chi2)
    for i, d in enumerate(depths):
        for j, ln in enumerate(lengths):
            if 0.5 * ln >= d - 1.0:
                chi2[i, j] = np.inf
                continue
            basis = dipole_profile(xd, d, ln, 1.0, sigma)
            amp = float(np.dot(basis, obs) / np.dot(basis, basis))
            amps[i, j] = amp
            chi2[i, j] = np.sum(((amp * basis - obs) / sigma_n) ** 2)
    i0, j0 = np.unravel_index(np.argmin(chi2), chi2.shape)
    keep = chi2 <= chi2[i0, j0] + 4.0
    print(f"\nbest fit: depth = {depths[i0]:.1f} m, length = "
          f"{lengths[j0]:.1f} m, current = {amps[i0, j0]:.4f} A")
    print(f"truth  : depth = {true_d:.1f} m, length = {true_l:.1f} m, "
          f"current = {true_i:.4f} A")
    for name, axis, values in (("depth", 0, depths), ("length", 1, lengths)):
        ok = values[keep.any(axis=1 - axis)]
        print(f"admitted {name}: [{ok.min():.1f}, {ok.max():.1f}] m")
    keep &= np.isfinite(chi2)
    idx = np.argwhere(keep)
    if idx.size:
        corr = np.corrcoef(depths[idx[:, 0]], lengths[idx[:, 1]])[0, 1]
        print(f"correlation between admitted depth and length = {corr:+.3f}")
    print("the admitted set is a ridge, not a point: a deeper and longer body")
    print("with a larger current is the same measurement as a shallower, shorter")
    print("one.  Only the width of the profile constrains the depth, and at")
    print(f"{100 * sigma_n / clean.max():.0f}% noise that width is known to about")
    print("one grid step - which is what the admitted range measures.")


if __name__ == "__main__":
    main()
