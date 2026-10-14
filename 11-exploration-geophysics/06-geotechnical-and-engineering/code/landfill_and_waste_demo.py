#!/usr/bin/env python3
"""Landfill, waste and brownfield assessment: the low-induction-number weighted
apparent conductivity, the equivalence of a cap or plume in an ERT sounding, the
magnetic clutter from soil that competes with a buried drum, and the base-rate
logic of calling a conductivity anomaly contamination.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python landfill_and_waste_demo.py

Everything is SYNTHETIC: conductivities, layer thicknesses, magnetisations and
priors are chosen teaching values.  The induction weighting is an explicitly
stated SYNTHETIC teaching kernel, not a specific instrument's response.
Print-only; no network access.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

MU0_OVER_4PI = 1.0e-7


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def kernel(z, h):
    """Stated teaching depth-weighting kernel for an induction reading, peaked at h.

    K(z) = (z/D) exp(-z^2/(2D)) with D = h^2/2: normalised so the integral is 1
    and the peak is at z = h.  A real system's kernel is system-specific.
    """
    d = 0.5 * h ** 2
    return (z / d) * np.exp(-z ** 2 / (2.0 * d))


def sigma_apparent(z, profil, h):
    dz = z[1] - z[0]
    return np.sum(profil * kernel(z, h)) * dz


def rho_a_two_layer(ab2, rho1, rho2, h1, n_terms=400):
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, n_terms + 1)
    return rho1 * (1.0 + 2.0 * np.sum(k ** n / (1.0 + (2.0 * n * h1 / ab2) ** 2) ** 1.5))


def dipole_field(moment, depth):
    """Vertical field on the axis of a vertical dipole, in nT."""
    return 2.0 * MU0_OVER_4PI * moment / depth ** 3 * 1e9


def main():
    section("1. Induction weighting: the reading is an average over depth")
    h = 1.5                       # m, stated coil height/geometry scale
    z = np.arange(0.0, 60.0, 0.05)
    print(f"  stated teaching kernel K(z) with peak at z = {h:.1f} m; "
          f"integral = {kernel(z, h).sum()*(z[1]-z[0]):.4f}")
    print("  a background of 0.02 S/m with a 0.30 S/m layer of 5 m thickness")
    print("\n   layer top (m)   sigma_a (S/m)   fraction of layer in kernel")
    dz = z[1] - z[0]
    for top in (0.5, 1.5, 3.0, 6.0, 12.0, 25.0):
        prof = np.where((z >= top) & (z < top + 5.0), 0.30, 0.02)
        frac = (kernel(z, h) * dz)[(z >= top) & (z < top + 5.0)].sum()
        print(f"   {top:13.1f}   {sigma_apparent(z, prof, h):13.4f}   {frac:23.4f}")
    print("\n  A 5 m layer of 0.30 S/m raises the reading by a factor of 13 when it")
    print("  starts at 0.5 m, by a factor of 6 at 1.5 m, and by only 1.3 at 3 m; below")
    print("  6 m it is invisible to this system.  The reading is dominated by the top")
    print("  few metres, so a strong shallow anomaly and a weaker deeper one are the")
    print("  same number: amplitude alone does not give depth.")

    section("2. Conductance equivalence depends on the window")
    print("  two models with the same conductance S = sigma * h:")
    print("  A: 10 m of 0.05 S/m (S = 0.5 S)   B: 2.5 m of 0.20 S/m (S = 0.5 S)")
    print("  both starting at 3 m in a 0.02 S/m background")
    prof_a = np.where((z >= 3.0) & (z < 13.0), 0.05, 0.02)
    prof_b = np.where((z >= 3.0) & (z < 5.5), 0.20, 0.02)
    for hh, name in ((1.5, "narrow window (shallow system)"),
                     (6.0, "medium window"),
                     (15.0, "broad window (deeper system)")):
        sa = sigma_apparent(z, prof_a, hh)
        sb = sigma_apparent(z, prof_b, hh)
        print(f"    {name:30s}: A = {sa:.4f}, B = {sb:.4f} S/m, "
              f"difference {(sb/sa-1)*100:+7.2f}%")
    print("\n  With the broad window (peak at 15 m) the two equal-conductance models")
    print("  differ by only 2.5%, below a typical noise level: only S is resolved.")
    print("  With the medium window (peak at 6 m) they differ by 91%, because the")
    print("  system then responds to WHERE the conductivity sits, not just to how much")
    print("  of it there is.  Whether a thickness is resolvable is a property of the")
    print("  system and of the target depth, not of the ground alone.")

    print("\n  The same ambiguity in a DC sounding (cap 150 ohm m over waste 5 ohm m,")
    print("  cap thickness 4 m): log-sensitivity Jacobian over AB/2 = 2-100 m")
    spac = np.logspace(0.3, 2.0, 12)
    base = np.array([rho_a_two_layer(s, 150.0, 5.0, 4.0) for s in spac])
    step_r, step_h = 0.5, 0.1
    dr = np.array([rho_a_two_layer(s, 150.0, 5.5, 4.0) for s in spac])
    dh = np.array([rho_a_two_layer(s, 150.0, 5.0, 4.1) for s in spac])
    jac = np.column_stack([(dr - base) / step_r * 5.0 / base,
                           (dh - base) / step_h * 4.0 / base])
    sv = np.linalg.svd(jac, compute_uv=False)
    direction = np.linalg.svd(jac)[2][-1]
    print(f"    singular values {sv[0]:.3f} and {sv[1]:.3f}, "
          f"condition number {sv[0]/sv[1]:.2f}")
    print(f"    least-determined direction (d ln rho_waste, d ln h_cap) = "
          f"({direction[0]:+.3f}, {direction[1]:+.3f})")
    print("    the two trade: a more resistive waste with a thinner cap fits as well")
    print("    as a more conductive waste with a thicker one.  Report the pair.")

    section("3. Magnetic clutter: a drum is not the only anomaly")
    drum_moment = 200.0           # A m^2, SYNTHETIC magnetised steel drum (teaching)
    soil_chi = 0.001              # SI, stated soil susceptibility
    field = 40.0                  # A/m, stated ambient field strength
    soil_moment = soil_chi * field * 125.0   # 5 x 5 x 5 m block of magnetised soil
    print(f"  drum: moment = {drum_moment:.0f} A m^2 (SYNTHETIC)")
    print(f"  soil block 5x5x5 m: M = chi H = {soil_chi*field:.3f} A/m, "
          f"moment = {soil_moment:.2f} A m^2")
    print("  both treated as point dipoles at the stated depth (valid when the")
    print("  source is small compared with the distance)")
    print("\n   depth (m)   drum anomaly (nT)   soil-block anomaly (nT)   ratio")
    for depth in (1.0, 2.0, 4.0):
        bd = dipole_field(drum_moment, depth)
        bs = dipole_field(soil_moment, depth)
        print(f"   {depth:9.1f}   {bd:17.1f}   {bs:24.2f}   {bd/bs:8.1f}")
    print("\n  A buried drum dominates, but a modestly magnetic soil block produces")
    print("  metre-scale anomalies of the same order as small metallic debris: with a")
    print("  1 nT threshold the soil is not noise, it is a target, and it must be")
    print("  modelled or mapped out before a magnetic survey can find drums.")

    section("4. Is a conductive anomaly contamination? Base rates decide")
    prior = 0.15                  # P(contamination | conductive anomaly region)
    tpr = 0.90                    # P(conductive | contamination)
    fpr = 0.40                    # P(conductive | clay / natural conductor)
    ppv = prior * tpr / (prior * tpr + (1.0 - prior) * fpr)
    print(f"  prior P(contamination) = {prior:.2f}")
    print(f"  P(conductive | contamination) = {tpr:.2f}; "
          f"P(conductive | clay) = {fpr:.2f}")
    print(f"  P(contamination | conductive anomaly) = {ppv:.3f}")
    print(f"  false-discovery rate = {1.0-ppv:.3f}: {round((1-ppv)*100)} of every 100")
    print("  conductive anomalies flagged for investigation are natural.")
    for pri in (0.05, 0.15, 0.40):
        p = pri * tpr / (pri * tpr + (1 - pri) * fpr)
        print(f"    prior {pri:.2f} -> posterior {p:.3f}")
    print("  Sampling the pore water settles what conductivity cannot: the survey")
    print("  prioritises, the borehole decides.")
    print("\n  All models and data in this module are SYNTHETIC.")


if __name__ == "__main__":
    main()
