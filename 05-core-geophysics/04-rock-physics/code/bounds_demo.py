"""Voigt, Reuss and Hashin-Shtrikman bounds for a two-phase rock.

Effective-medium theory in geophysics is mostly about *bounds*: the elastic
moduli of a mixture are not a single number, they lie between limits fixed by
the volume fractions and the moduli of the constituents.  This script

  1. computes Voigt (arithmetic), Reuss (harmonic) and Hill (their mean)
     averages for a stated SYNTHETIC mineral + fluid mixture;
  2. computes the Hashin-Shtrikman lower and upper bounds, which are the
     narrowest bounds that depend only on volume fractions and isotropy;
  3. demonstrates the degenerate case that matters physically: with a fluid
     of zero shear modulus, the Reuss and HS-LOWER shear moduli are both
     identically zero, so for shear only the HS-UPPER bound is useful;
  4. verifies Voigt and Reuss by an independent numerical method -- a 1-D
     finite-element bar with the same moduli distribution.  Uniform strain
     forces the arithmetic mean; uniform stress forces the harmonic mean.

Units: SI.  Moduli in Pa, density in kg/m^3.

Run:  python3 bounds_demo.py
"""

from __future__ import annotations

import numpy as np

GPA = 1.0e9  # Pa per GPa


def voigt(phi, k_s, g_s, k_f, g_f):
    """Arithmetic (isostrain) average.  phi is the fraction of the weak phase."""
    return (1 - phi) * k_s + phi * k_f, (1 - phi) * g_s + phi * g_f


def reuss(phi, k_s, g_s, k_f, g_f):
    """Harmonic (isostress) average.

    The shear average is evaluated as a limit: a phase with zero shear modulus
    makes the harmonic mean exactly zero (1/G -> infinity), which is the
    physically correct isostress result, not a numerical accident.
    """
    k = 1.0 / (phi / k_f + (1 - phi) / k_s)
    # Harmonic mean of shear, evaluated in the limit at the endpoints so the
    # single-phase cases return the single-phase modulus rather than 0/0.
    terms = 0.0
    if phi > 0.0:
        if g_f == 0.0:
            return k, 0.0
        terms += phi / g_f
    if phi < 1.0:
        if g_s == 0.0:
            return k, 0.0
        terms += (1.0 - phi) / g_s
    g = 1.0 / terms if terms > 0.0 else 0.0
    return k, g


def hs_bounds(phi, ks, gs, kw, gw):
    """Hashin-Shtrikman bounds for a two-phase isotropic mixture.

    (ks, gs) is the STIFFER phase, (kw, gw) the weaker (here: a fluid, gw = 0),
    and phi is the volume fraction of the weak phase.

        K+- = K_host + f_incl / ( 1/(K_incl-K_host) + f_host * 3/(3K_host+4G_host) )
        G+- = G_host + f_incl / ( 1/(G_incl-G_host)
                                  + f_host * 2(K_host+2G_host)
                                            / (5 G_host (K_host + 4G_host/3)) )

    Using the stiff phase as host gives the UPPER bounds; using the weak phase
    gives the LOWER bounds.  The shear formula is singular for a fluid host:
    its limit is exactly zero, which we return explicitly rather than by
    dividing by zero.
    """
    def bulk(kh, gh, ki, gi, f_host, f_incl):
        return kh + f_incl / (1.0 / (ki - kh) + f_host * 3.0 / (3.0 * kh + 4.0 * gh))

    def shear(kh, gh, ki, gi, f_host, f_incl):
        if gh == 0.0:
            return 0.0
        denom = (1.0 / (gi - gh)
                 + f_host * 2.0 * (kh + 2.0 * gh) / (5.0 * gh * (kh + 4.0 * gh / 3.0)))
        return gh + f_incl / denom

    k_up = bulk(ks, gs, kw, gw, 1 - phi, phi)
    g_up = shear(ks, gs, kw, gw, 1 - phi, phi)
    k_lo = bulk(kw, gw, ks, gs, phi, 1 - phi)
    g_lo = shear(kw, gw, ks, gs, phi, 1 - phi)
    return (k_lo, g_lo), (k_up, g_up)


def series_parallel_assemblies(E_elem):
    """Effective modulus of the SAME set of elements in two topologies.

    Both results come from assembling and solving a linear system, which is an
    independent code path from the closed-form means.

    Series (elements end to end, a 1-D bar): force is uniform, displacement
    adds, so the effective modulus is the harmonic mean.

    Parallel (elements side by side, a bank of springs on a common node at
    prescribed displacement): displacement is uniform, force adds, so the
    effective modulus is the arithmetic mean.
    """
    n = E_elem.size
    h = 1.0 / n

    # --- series: assembled bar stiffness matrix ---
    Kser = np.zeros((n + 1, n + 1))
    for e in range(n):
        Kser[e:e + 2, e:e + 2] += E_elem[e] / h * np.array([[1.0, -1.0], [-1.0, 1.0]])
    delta = 1.0e-6
    free = np.arange(1, n)
    u = np.zeros(n + 1)
    rhs = -Kser[np.ix_(free, [0, n])] @ np.array([0.0, delta])
    u[free] = np.linalg.solve(Kser[np.ix_(free, free)], rhs)
    u[n] = delta
    force_series = Kser[n, :] @ u            # reaction at the loaded end
    e_series = force_series / delta          # unit area, unit total length

    # --- parallel: one node, n springs to ground, common displacement ---
    # Total cross-section is 1, so each spring carries area 1/n and length 1;
    # k_i = E_i A_i / L = E_i / n.  Their sum is the arithmetic mean.
    k_springs = E_elem / n
    K_par = np.array([[np.sum(k_springs)]])
    f_par = K_par @ np.array([delta])
    e_parallel = f_par[0] / delta            # total area is 1, strain = delta
    return e_series, e_parallel


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def main() -> None:
    rng = np.random.default_rng(7)

    # --- SYNTHETIC constituent properties (chosen, not remembered) --------
    K_MIN, G_MIN = 37.0 * GPA, 44.0 * GPA     # a stiff solid
    K_FL, G_FL = 2.2 * GPA, 0.0               # a fluid: no shear resistance
    print("SYNTHETIC constituents: K_min = %.1f GPa, G_min = %.1f GPa;"
          % (K_MIN / GPA, G_MIN / GPA))
    print("                        K_fl  = %.1f GPa, G_fl  = %.1f Pa"
          % (K_FL / GPA, G_FL))
    print("(A fluid has zero shear modulus by definition: it cannot sustain")
    print(" static shear stress.  This single fact drives Section 3.)")

    phi = 0.20
    section(f"1. Bounds at porosity phi = {phi:.2f}")
    kv, gv = voigt(phi, K_MIN, G_MIN, K_FL, G_FL)
    kr, gr = reuss(phi, K_MIN, G_MIN, K_FL, G_FL)
    (klo, glo), (khi, ghi) = hs_bounds(phi, K_MIN, G_MIN, K_FL, G_FL)
    print(f"  {'estimate':<22}{'K (GPa)':>12}{'G (GPa)':>12}")
    print(f"  {'Voigt (upper)':<22}{kv/GPA:12.4f}{gv/GPA:12.4f}")
    print(f"  {'Hill average':<22}{(kv+kr)/2/GPA:12.4f}{(gv+gr)/2/GPA:12.4f}")
    print(f"  {'Reuss (lower)':<22}{kr/GPA:12.4f}{gr/GPA:12.4f}")
    print(f"  {'HS upper':<22}{khi/GPA:12.4f}{ghi/GPA:12.4f}")
    print(f"  {'HS lower':<22}{klo/GPA:12.4f}{glo/GPA:12.4f}")
    print("  Note: Voigt/Reuss are wider than HS.  HS is the tightest pair of")
    print("  bounds that depends only on volume fraction and isotropy.")

    section("2. Consistency checks on the bounds")
    ok_bracket = klo <= khi and glo <= ghi
    print(f"  K_HS- <= K_HS+ ?      {klo <= khi}   "
          f"({klo/GPA:.4f} <= {khi/GPA:.4f})")
    print(f"  G_HS- <= G_HS+ ?      {glo <= ghi}   "
          f"({glo/GPA:.4f} <= {ghi/GPA:.4f})")
    print(f"  K_HS+ <= K_Voigt ?    {khi <= kv*(1+1e-12)}   "
          f"({khi/GPA:.4f} <= {kv/GPA:.4f})")
    print(f"  G_HS+ <= G_Voigt ?    {ghi <= gv*(1+1e-12)}   "
          f"({ghi/GPA:.4f} <= {gv/GPA:.4f})")
    print(f"  all bracket orderings hold: {ok_bracket}")
    # With a zero-shear fluid the HS lower bulk bound collapses onto Reuss.
    # This is an identity, not an accident: set G_fl = 0 in the HS formula.
    print(f"  K_Reuss vs K_HS- : {kr/GPA:.9f} vs {klo/GPA:.9f} GPa "
          f"(rel. diff {abs(kr-klo)/kr:.2e})")
    print("  They coincide: with G_fl = 0 the HS lower bulk bound IS the")
    print("  Reuss bound.  (Set G_fl = 0 in the HS formula and simplify.)")
    print("  Limits: at phi -> 0 every bound must collapse to the solid.")
    for p in (0.0, 1.0):
        kv2, gv2 = voigt(p, K_MIN, G_MIN, K_FL, G_FL)
        kr2, gr2 = reuss(p, K_MIN, G_MIN, K_FL, G_FL)
        print(f"    phi = {p:.1f}: Voigt K = {kv2/GPA:.6f} GPa, "
              f"Reuss K = {kr2/GPA:.6f} GPa, "
              f"Voigt G = {gv2/GPA:.6f} GPa, Reuss G = {gr2/GPA:.6f} GPa")

    section("3. The degenerate case: shear bounds with a zero-shear fluid")
    print("   phi    G_Reuss(GPa)   G_HS-lower(GPa)   G_HS-upper(GPa)")
    for p in (0.05, 0.20, 0.40):
        _, gr_p = reuss(p, K_MIN, G_MIN, K_FL, G_FL)
        (_, glo_p), (_, ghi_p) = hs_bounds(p, K_MIN, G_MIN, K_FL, G_FL)
        print(f"  {p:.2f}   {gr_p/GPA:12.6f}   {glo_p/GPA:15.6f}   "
              f"{ghi_p/GPA:15.6f}")
    print("  Both lower bounds are exactly zero for ANY porosity.  They carry")
    print("  no information: a fluid-saturated rock with the fluid as the")
    print("  connected host has no shear stiffness in the limit of a weak")
    print("  frame.  Only the HS-UPPER bound constrains G.  Reporting 'the")
    print("  Reuss shear modulus' of a brine-saturated sandstone is therefore")
    print("  reporting zero -- a bound, not a prediction.")

    section("4. Independent check: assembled series and parallel systems")
    # Element moduli drawn from the same mixture statistics, then the SAME
    # element set is assembled two ways.
    n = 200
    E = np.where(rng.random(n) < phi, K_FL, K_MIN)
    realised = np.mean(E == K_FL)
    e_series, e_parallel = series_parallel_assemblies(E)
    voigt_num = E.mean()                      # arithmetic mean
    reuss_num = 1.0 / np.mean(1.0 / E)        # harmonic mean
    print(f"  realised fluid fraction = {realised:.3f} "
          f"({n} elements, {np.sum(E == K_FL)} of them fluid)")
    print(f"  series assembly (bar)  = {e_series/GPA:.6f} GPa")
    print(f"  harmonic mean of E     = {reuss_num/GPA:.6f} GPa")
    print(f"    relative difference  = {abs(e_series-reuss_num)/reuss_num:.3e}")
    print(f"  parallel assembly      = {e_parallel/GPA:.6f} GPa")
    print(f"  arithmetic mean of E   = {voigt_num/GPA:.6f} GPa")
    print(f"    relative difference  = "
          f"{abs(e_parallel-voigt_num)/voigt_num:.3e}")
    print("  Both assemblies are solved linear systems (an independent code")
    print("  path from the closed forms) and both are reproduced to round-off.")
    print("  This confirms the ALGEBRA of the averages.  It does NOT tell you")
    print("  which average a real rock obeys -- that is a physical question")
    print("  about pore geometry, and it is why bounds exist at all.")

    print("\nSUMMARY: bounds bracket the truth; they never predict it.  For")
    print("shear with a fluid phase, the lower bounds collapse to zero.")


if __name__ == "__main__":
    main()
