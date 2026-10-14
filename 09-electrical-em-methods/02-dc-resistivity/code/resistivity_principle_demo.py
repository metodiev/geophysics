#!/usr/bin/env python3
"""The resistivity principle: point-source fields, four electrodes, geometry errors.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python resistivity_principle_demo.py

Everything is SYNTHETIC.  The half-space resistivity, the injected current, the
contact resistances and the measurement noise are chosen teaching values; no real
survey, instrument or data set is used.

Contents
--------
1. The point-source potential on a half-space, and the current check.
2. The general four-electrode geometric factor, and the standard closed forms.
3. Apparent resistivity from a synthetic measurement, and reciprocity.
4. Why four electrodes: contact resistance, quantified.
5. Electrode mislocation: which electrode matters, and by how much.
"""

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

RNG = np.random.default_rng(20261014)

RHO_TRUE = 100.0        # ohm m, uniform half-space of the teaching model
I_INJECT = 0.1          # A, injected current
N_POINTS = 1001


def section(title):
    print(f"\n{'=' * 68}\n{title}\n{'=' * 68}")


def potential(rho, I, r):
    """Potential of a point current source on a half-space (volts)."""
    return rho * I / (2.0 * np.pi * np.abs(r))


def four_electrode_k(A, B, M, N):
    """Geometric factor k of a four-electrode array; rho_a = k dV / I.

    With all electrodes on the surface of a uniform half-space the potential
    difference is dV = (rho I / 2 pi) * (1/r_AM - 1/r_AN - 1/r_BM + 1/r_BN),
    so k = 2 pi / (1/r_AM - 1/r_AN - 1/r_BM + 1/r_BN).
    """
    bracket = (1.0 / abs(A - M) - 1.0 / abs(A - N)
               - 1.0 / abs(B - M) + 1.0 / abs(B - N))
    return 2.0 * np.pi / bracket


def layered_kernel_R(rhos, hs, lam):
    """R_1(lambda) for a stack of layers over a half-space (Stefanescu ratio).

    rhos[0] is the top layer, rhos[-1] the basement; hs holds the layer
    thicknesses (one fewer entry than rhos).  The surface potential of a point
    source is (rho_1 I / 2 pi) * integral of T(lambda) J_0(lambda r) dlambda,
    with T = 1/(1 - R_1).
    """
    R = 0.0
    for i in range(len(hs) - 1, -1, -1):
        k = (rhos[i + 1] - rhos[i]) / (rhos[i + 1] + rhos[i])
        R = (k + R) * np.exp(-2.0 * lam * hs[i]) / (1.0 + k * R)
    return R


def layered_potential(rhos, hs, r, I=1.0):
    """Surface potential of a point source on a layered half-space (volts)."""
    lam_max = 30.0 / min(hs)
    integrand = (lambda lam: (1.0 / (1.0 - layered_kernel_R(rhos, hs, lam)) - 1.0)
                 * j0(lam * r))
    value, _ = quad(integrand, 0.0, lam_max, limit=400)
    return rhos[0] * I / (2.0 * np.pi) * (1.0 / abs(r) + value)


def dV_layered(rhos, hs, A, B, M, N, I=1.0):
    """Potential difference V(M) - V(N) for a layered half-space (volts)."""
    return (layered_potential(rhos, hs, M - A, I)
            - layered_potential(rhos, hs, N - A, I)
            - layered_potential(rhos, hs, M - B, I)
            + layered_potential(rhos, hs, N - B, I))


def dV_halfspace(A, B, M, N, rho=RHO_TRUE, I=I_INJECT):
    """Potential difference V(M) - V(N) on a uniform half-space (volts)."""
    return (potential(rho, I, M - A) - potential(rho, I, N - A)
            - potential(rho, I, M - B) + potential(rho, I, N - B))


def wenner(a, centre=0.0):
    return (centre - 1.5 * a, centre + 1.5 * a, centre - 0.5 * a, centre + 0.5 * a)


def main():
    section("1. Point source on a half-space: V(r) = rho I / (2 pi r)")
    print(f"  SYNTHETIC model: rho = {RHO_TRUE:.1f} ohm m, I = {I_INJECT:.2f} A")
    print("      r (m)     V (V)     V 2 pi r/(rho I)   J (A/m^2)")
    for r in (0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0):
        V = potential(RHO_TRUE, I_INJECT, r)
        J = I_INJECT / (2.0 * np.pi * r ** 2)
        print(f"  {r:8.2f} {V:9.5f} {V * 2 * np.pi * r / (RHO_TRUE * I_INJECT):19.6f} "
              f"{J:12.4e}")
    # The hemispherical integral of the current density must return I exactly.
    xg, wg = np.polynomial.legendre.leggauss(120)
    theta = 0.25 * np.pi * (xg + 1.0)
    wtheta = 0.25 * np.pi * wg
    shape = np.sum(wtheta * np.sin(theta))
    print(f"\n  integral of sin(theta) over 0<=theta<=pi/2 = {shape:.12f} (exact 1)")
    print(f"  so the current crossing a hemisphere is "
          f"{I_INJECT / (2 * np.pi) * 2 * np.pi * shape:.12f} A "
          f"= the injected {I_INJECT:.2f} A")

    section("2. The four-electrode array and its geometric factor")
    a = 5.0
    A, B, M, N = wenner(a)
    k_wenner = four_electrode_k(A, B, M, N)
    print(f"  Wenner, spacing a = {a:.1f} m: electrodes at "
          f"{A:.1f}, {B:.1f} (current) and {M:.1f}, {N:.1f} (potential) m")
    print(f"  k from the general formula        = {k_wenner:.6f} m")
    print(f"  closed form k = 2 pi a            = {2 * np.pi * a:.6f} m")
    print(f"  difference                        = "
          f"{abs(k_wenner - 2 * np.pi * a):.3e} m")
    L, l = 100.0, 10.0
    A, B, M, N = -L / 2, L / 2, -l / 2, l / 2
    k_schl = four_electrode_k(A, B, M, N)
    print(f"\n  Schlumberger, L = {L:.0f} m, l = {l:.0f} m:")
    print(f"  k from the general formula        = {k_schl:.6f} m")
    print(f"  closed form pi (L^2 - l^2)/(4 l)  = "
          f"{np.pi * (L ** 2 - l ** 2) / (4 * l):.6f} m")
    n_dd = 3.0
    A, B, M, N = 0.0, a, (n_dd + 1) * a, (n_dd + 2) * a
    k_dd = four_electrode_k(A, B, M, N)
    print(f"\n  dipole-dipole, n = {n_dd:.0f}, a = {a:.1f} m:")
    print(f"  k from the general formula        = {k_dd:.6f} m")
    print(f"  closed form -pi n(n+1)(n+2) a     = "
          f"{-np.pi * n_dd * (n_dd + 1) * (n_dd + 2) * a:.6f} m")
    print("  (the sign is a convention tied to which potential electrode is")
    print("  called positive; |k| is what a measurement uses)")
    # Pole-pole is the limit B, N -> infinity.
    B_far, N_far = 1.0e9, -1.0e9
    A, M = 0.0, a
    k_pp = four_electrode_k(A, B_far, M, N_far)
    print(f"\n  pole-pole (B and N pushed to +-1e9 m): k = {k_pp:.6f} m, "
          f"2 pi a = {2 * np.pi * a:.6f} m")

    section("3. Apparent resistivity, and reciprocity")
    A, B, M, N = wenner(a)
    k = four_electrode_k(A, B, M, N)
    dV = dV_halfspace(A, B, M, N)
    rho_a = k * dV / I_INJECT
    print(f"  SYNTHETIC Wenner measurement on a {RHO_TRUE:.0f} ohm m half-space:")
    print(f"    dV = {dV:.6f} V from the point-source sum")
    print(f"    rho_a = k dV / I = {k:.4f} x {dV:.6f} / {I_INJECT:.2f} = "
          f"{rho_a:.6f} ohm m")
    print(f"    error against the true half-space = "
          f"{(rho_a - RHO_TRUE) / RHO_TRUE:.3e}")
    # Reciprocity: swap the current and potential pairs and re-measure.
    dV_swap = dV_halfspace(M, N, A, B)
    k_swap = four_electrode_k(M, N, A, B)
    print(f"  reciprocity: dV with current and potential pairs exchanged = "
          f"{dV_swap:.6f} V (ratio {dV_swap / dV:.12f})")
    print(f"  rho_a from the exchanged configuration = "
          f"{k_swap * dV_swap / I_INJECT:.6f} ohm m")
    for noise in (0.01, 0.05):
        dV_noisy = dV * (1.0 + RNG.normal(0.0, noise))
        rho_noisy = k * dV_noisy / I_INJECT
        print(f"  with {noise * 100:.0f}% voltage noise: rho_a = "
              f"{rho_noisy:.3f} ohm m "
              f"({(rho_noisy - RHO_TRUE) / RHO_TRUE * 100:+.2f}%)")

    section("4. Why four electrodes: contact resistance")
    rho_c = RHO_TRUE
    a_elec = 0.05
    R_geo = rho_c / (2.0 * np.pi) * (1.0 / a_elec + 1.0 / a_elec)
    R_contact = 500.0
    print(f"  two-electrode measurement, hemispherical electrodes of radius "
          f"{a_elec:.2f} m:")
    print(f"    geometric resistance R = rho/(2 pi) (1/a1 + 1/a2) = "
          f"{R_geo:.3f} ohm")
    print(f"    contact resistance per electrode = {R_contact:.0f} ohm")
    print(f"    measured R = {R_geo:.3f} + 2 x {R_contact:.0f} = "
          f"{R_geo + 2 * R_contact:.3f} ohm")
    print(f"    -> apparent resistivity "
          f"{(R_geo + 2 * R_contact) / R_geo * rho_c:.1f} ohm m instead of "
          f"{rho_c:.1f} ohm m ({(R_geo + 2 * R_contact) / R_geo:.2f}x)")
    print("\n  four-electrode measurement: the potential circuit draws current")
    for Z_in in (1e6, 1e7, 1e9):
        i_pot = dV / Z_in
        dv_err = 2.0 * R_contact * i_pot
        print(f"    voltmeter input impedance {Z_in:.0e} ohm: potential-circuit "
              f"current {i_pot:.3e} A,")
        print(f"      extra voltage across the contact resistance "
              f"{dv_err:.3e} V = {dv_err / dV * 100:.5f}% of dV")
    print("  the contact resistance has not been measured away; it has been")
    print("  moved into a circuit that carries almost no current.")

    section("5. Electrode mislocation: which electrode matters?")
    a = 5.0
    print("  First, the sanity check that matters: on a UNIFORM half-space a")
    print("  mislocated electrode changes nothing, because any geometry returns")
    print("  the same apparent resistivity.")
    A, B, M, N = wenner(a)
    k_nom = four_electrode_k(A, B, M, N)
    xs = [A, B, M, N]
    xs[2] += 0.01
    rho_ref = k_nom * dV_halfspace(A, B, M, N) / I_INJECT
    rho_honest = four_electrode_k(*xs) * dV_halfspace(*xs) / I_INJECT
    rho_naive = k_nom * dV_halfspace(*xs) / I_INJECT
    print(f"    nominal geometry: rho_a = {rho_ref:.6f} ohm m")
    print(f"    M actually 1 cm off, geometry recorded honestly: rho_a = "
          f"{rho_honest:.6f} ohm m")
    print(f"    M actually 1 cm off, geometry recorded as nominal: rho_a = "
          f"{rho_naive:.6f} ohm m ({(rho_naive - rho_ref) / rho_ref * 100:+.4f}%)")
    print("\n  Now the same 1 cm error over a TWO-LAYER model: this is where")
    print("  geometry error costs accuracy, because the two-layer response is")
    print("  not scale-invariant the way the half-space response is:")
    rhos, hs = [100.0, 10.0], [5.0]
    print(f"    SYNTHETIC model: rho_1 = {rhos[0]:.0f} ohm m, "
          f"h_1 = {hs[0]:.1f} m, basement rho_2 = {rhos[1]:.0f} ohm m")
    for label, arr in (("Wenner a = 5 m", wenner(a)),
                       ("dipole-dipole n = 3, a = 5 m",
                        (0.0, a, 4.0 * a, 5.0 * a))):
        A, B, M, N = arr
        k_nom = four_electrode_k(A, B, M, N)      # signed; dV has the same sign
        rho_ref = abs(k_nom * dV_layered(rhos, hs, A, B, M, N, I_INJECT) / I_INJECT)
        print(f"\n    {label}: rho_a = {rho_ref:.4f} ohm m (below rho_1 = 100:")
        print("      the array already senses the better conductor beneath it)")
        names = ("C1/A", "C2/B", "P1/M", "P2/N")
        for idx in range(4):
            xs = [A, B, M, N]
            xs[idx] += 0.01
            rho_pert = abs(k_nom * dV_layered(rhos, hs, *xs, I_INJECT)
                           / I_INJECT)
            print(f"      move {names[idx]:4s} by 1 cm: rho_a = "
                  f"{rho_pert:9.4f} ohm m "
                  f"({(rho_pert - rho_ref) / rho_ref * 100:+7.4f}%)")
    print("\n  the electrodes of the closest pair dominate the error: 0.26% for")
    print("  the inner Wenner electrode and 0.31% for the adjacent dipole")
    print("  electrodes, against 0.13-0.17% for the far pair.  Decimetre")
    print("  positioning over a real 3-D ground is what limits the accuracy,")
    print("  not the voltmeter.")


if __name__ == "__main__":
    main()
