"""Petrophysics: velocity-porosity laws, anisotropy, Q, and Archie's failure.

Four verifiable rock-physics results, each checked against a closed form or an
exact limit rather than asserted:

  1. VELOCITY-POROSITY.  Wyllie time-average and Raymer-Hunt-Gardner on the
     same inputs; the models diverge as porosity rises, and each is reported
     against the other rather than presented alone.
  2. ANISOTROPY.  Thomsen parameters computed from a synthetic VTI stiffness
     matrix, then verified against phase velocities obtained by solving the
     Christoffel eigenvalue problem independently.  The isotropic limit is
     checked to return epsilon = gamma = delta = 0.
  3. ATTENUATION.  A Zener (standard linear solid) element: the measured peak
     of 1/Q lands at f = 1/(2 pi tau), and the low- and high-frequency
     asymptotes match the algebraic limits.
  4. ARCHIE'S LAW.  Archie is inverted on data generated with an added
     clay-conduction path.  The inverted saturation is biased, and the bias is
     reported as a function of porosity -- a model failing outside its
     assumptions.

All constituent properties are STATED SYNTHETIC INPUTS chosen for the
demonstration.  They are not measured rock properties.

Run:  python3 petrophysics_demo.py
"""

from __future__ import annotations

import numpy as np

GPA = 1.0e9


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def wyllie(phi, v_ma, v_fl):
    """Wyllie time-average: 1/Vp = phi/Vfl + (1-phi)/Vma."""
    return 1.0 / (phi / v_fl + (1.0 - phi) / v_ma)


def raymer(phi, v_ma, v_fl):
    """Raymer-Hunt-Gardner: Vp = (1-phi)^2 Vma + phi Vfl."""
    return (1.0 - phi) ** 2 * v_ma + phi * v_fl


def christoffel_vti(c11, c33, c13, c44, c66, rho, theta_deg):
    """Phase velocities of a VTI medium at angle theta from the symmetry axis."""
    th = np.radians(theta_deg)
    s2, c2 = np.sin(th) ** 2, np.cos(th) ** 2
    sc = np.sin(th) * np.cos(th)
    G = np.array([
        [c11 * s2 + c44 * c2, 0.0, (c13 + c44) * sc],
        [0.0, c66 * s2 + c44 * c2, 0.0],
        [(c13 + c44) * sc, 0.0, c44 * s2 + c33 * c2],
    ])
    eig = np.linalg.eigvalsh(G) / rho
    eig = np.sort(np.sqrt(np.clip(eig, 0.0, None)))[::-1]
    return eig[0], eig[1], eig[2]      # quasi-P, quasi-SV, SH


def thomsen(c11, c33, c13, c44, c66):
    eps = (c11 - c33) / (2.0 * c33)
    gam = (c66 - c44) / (2.0 * c44)
    delta = ((c13 + c44) ** 2 - (c33 - c44) ** 2) / (2.0 * c33 * (c33 - c44))
    return eps, gam, delta


def main() -> None:
    # ==================================================================
    section("1. Velocity-porosity laws: two models, one set of inputs")
    v_ma, v_fl = 4500.0, 1500.0        # m/s  SYNTHETIC matrix and pore fluid
    print(f"  SYNTHETIC: V_matrix = {v_ma:.0f} m/s, V_fluid = {v_fl:.0f} m/s")
    print("   phi    Wyllie(m/s)   Raymer(m/s)   (Wyllie-Raymer)/Wyllie")
    for phi in (0.05, 0.10, 0.20, 0.30, 0.40):
        w = wyllie(phi, v_ma, v_fl)
        r = raymer(phi, v_ma, v_fl)
        print(f"  {phi:5.2f}   {w:11.1f}   {r:11.1f}   "
              f"{100*(w-r)/w:+21.1f} %")
    print("  The two models agree to about 1% at 5% porosity and diverge to")
    print("  about 11% at 40%, with the sign of the difference changing near")
    print("  15%.  Neither is 'right': each is an empirical fit valid over a")
    print("  particular porosity range and lithology.  Reporting a velocity")
    print("  from one of them without saying which, and over what range it was")
    print("  calibrated, is not a prediction.")
    phi = 0.20
    print(f"  limits: at phi=0 both give {wyllie(0.0, v_ma, v_fl):.1f} m/s "
          f"(the matrix); at phi=1 both give "
          f"{wyllie(1.0, v_ma, v_fl):.1f} m/s (the fluid).")

    # ==================================================================
    section("2. VTI anisotropy: stiffness matrix, Thomsen, and Christoffel")
    # SYNTHETIC stiffness matrix for a VTI rock (GPa), mildly anisotropic.
    c11, c33, c13, c44, c66 = 66.0 * GPA, 55.0 * GPA, 18.0 * GPA, \
        20.0 * GPA, 23.0 * GPA
    rho = 2500.0
    eps, gam, delta = thomsen(c11, c33, c13, c44, c66)
    print(f"  SYNTHETIC VTI stiffness (GPa): C11={c11/GPA:.1f} C33={c33/GPA:.1f}"
          f" C13={c13/GPA:.1f} C44={c44/GPA:.1f} C66={c66/GPA:.1f}")
    print(f"  rho = {rho:.0f} kg/m^3")
    print(f"  Thomsen: epsilon = {eps:.4f}, gamma = {gam:.4f}, "
          f"delta = {delta:.4f}")
    vp0, vs0, _ = christoffel_vti(c11, c33, c13, c44, c66, rho, 0.0)
    vp90, vs90, _ = christoffel_vti(c11, c33, c13, c44, c66, rho, 90.0)
    print(f"  Christoffel (independent eigen-solve):")
    print(f"    Vp(0 deg)  = {vp0:7.1f} m/s      Vp(90 deg) = {vp90:7.1f} m/s")
    print(f"    Vs(0 deg)  = {vs0:7.1f} m/s      Vs(90 deg) = {vs90:7.1f} m/s")
    print(f"  check Vp90/Vp0 - 1 = {vp90/vp0 - 1:.6f} vs "
          f"sqrt(1+2*epsilon)-1 = {np.sqrt(1+2*eps)-1:.6f}")
    print(f"  check Vs90/Vs0 - 1 = {vs90/vs0 - 1:.6f} vs "
          f"sqrt(1+2*gamma)-1 = {np.sqrt(1+2*gam)-1:.6f}")
    # Isotropic limit.
    ci = 40.0 * GPA
    eps0, gam0, del0 = thomsen(ci, ci, ci - 2 * 15.0 * GPA, 15.0 * GPA, 15.0 * GPA)
    print(f"  isotropic limit (C11=C33, C44=C66=15 GPa): epsilon = {eps0:.3e}, "
          f"gamma = {gam0:.3e}, delta = {del0:.3e}")
    print("  The Thomsen relations are confirmed by an independent eigen-solve")
    print("  of the Christoffel matrix, and the isotropic limit is exact.")

    # ==================================================================
    section("3. Attenuation: the Zener element, measured against its limits")
    tau, delta_m = 1.0e-3, 0.10          # s, dimensionless relaxation strength
    f = np.logspace(-1, 4, 4000)         # Hz
    w = 2.0 * np.pi * f
    inv_q = delta_m * (w * tau) / (1.0 + (w * tau) ** 2)   # 1/Q(f)
    f_peak = f[np.argmax(inv_q)]
    print(f"  SYNTHETIC Zener element: tau = {tau:.1e} s, "
          f"relaxation strength = {delta_m:.2f}")
    print(f"  measured peak of 1/Q at f = {f_peak:.6f} Hz")
    print(f"  predicted 1/(2 pi tau)    = {1.0/(2*np.pi*tau):.6f} Hz")
    print(f"  relative difference = "
          f"{abs(f_peak - 1/(2*np.pi*tau))*2*np.pi*tau:.3e}")
    print(f"  1/Q at the peak = {inv_q.max():.6f}  vs max "
          f"delta/2 = {delta_m/2:.6f}")
    # Asymptotes.  1/Q is symmetric under w*tau -> 1/(w*tau), so the two
    # reciprocal test frequencies must give the same Q.  That symmetry is a
    # property of the Zener element and is itself a check.
    for wtau, label in ((1e-3, "low"), (1e3, "high")):
        q_num = 1.0 / (delta_m * wtau / (1.0 + wtau**2))
        asym = 1.0 / (delta_m * wtau) if wtau < 1 else wtau / delta_m
        print(f"  {label:4s}-frequency limit at w*tau = {wtau:8.1e}: "
              f"numerical Q = {q_num:12.4f}, asymptotic = {asym:12.4f}")
    print("  The two test frequencies are reciprocals of each other, and the")
    print("  numerical Q values agree with each other: 1/Q is symmetric under")
    print("  w*tau -> 1/(w*tau).  Both also match the algebraic asymptotes.")
    # Velocity dispersion: V ~ sqrt(M), M goes from M_R to M_U.
    m_relaxed = 1.0
    m_unrelaxed = 1.0 + delta_m
    disp = np.sqrt(m_unrelaxed / m_relaxed) - 1.0
    print(f"  total velocity dispersion between the limits = "
          f"{100*disp:.4f} %")
    print("  A Q of about 20 (1/Q = 0.05) therefore carries a velocity")
    print("  dispersion of a few percent across the band -- small, but exactly")
    print("  the size of the anomalies 4-D seismic tries to measure.  Q and")
    print("  dispersion are two views of one relaxation, not two properties.")

    # ==================================================================
    section("4. Archie's law inverted on clay-contaminated synthetic data")
    a, m, n_exp = 1.0, 2.0, 2.0          # SYNTHETIC Archie parameters
    rw = 0.5                             # ohm m  SYNTHETIC pore-water resistivity
    c_clay = 0.02                        # S/m    SYNTHETIC extra conduction path
    print(f"  SYNTHETIC Archie: a={a:.1f}, m={m:.1f}, n={n_exp:.1f}, "
          f"Rw={rw:.2f} ohm m ; added clay conduction {c_clay:.3f} S/m")
    print("   phi    Sw_true   Sw_Archie   error")
    for phi in (0.05, 0.10, 0.20, 0.30):
        sw_true = 0.40
        c_archie = phi**m * sw_true**n_exp / (a * rw)     # true Archie term
        c_total = c_archie + sw_true * c_clay             # parallel clay path
        rt = 1.0 / c_total
        sw_archie = (a * rw / (phi**m * rt)) ** (1.0 / n_exp)
        print(f"  {phi:5.2f}   {sw_true:7.2f}   {sw_archie:9.4f}   "
              f"{sw_archie-sw_true:+6.4f}")
    print("  Archie ignores the clay conduction path, so it reads the extra")
    print("  conductivity as extra water and OVERESTIMATES saturation.  At")
    print("  phi = 0.05 the inversion returns a saturation of 1.33 -- greater")
    print("  than 1, which is physically impossible.  A bound being violated")
    print("  is the clearest possible signal that the model is outside its")
    print("  assumptions.  The bias grows as porosity falls, because the")
    print("  clay term becomes an ever larger share of the total conduction.")
    print("  A shaly-sand model with an explicit clay term is required in that")
    print("  regime; applying Archie there is a known, quantified error.")

    print("\nSUMMARY: every model above is checked against a limit, an")
    print("independent solution, or a regime where it demonstrably fails.")


if __name__ == "__main__":
    main()
