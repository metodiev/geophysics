#!/usr/bin/env python3
"""Geophysics for unconventional reservoirs: elastic moduli and brittleness,
anisotropy and shear-wave splitting, microseismic source scaling and detection,
location uncertainty, and the pore pressure a fracture needs to slip.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python unconventional_geophysics_demo.py

Contents
--------
1. Young's modulus, Poisson's ratio and two brittleness indices from vp, vs, rho.
2. VTI anisotropy: exact phase velocities from a stiffness matrix, and the
   Thomsen parameters recovered from them.
3. HTI (fracture) anisotropy: shear-wave splitting time versus path length.
4. Microseismic source scaling: moment, magnitude, slip and rupture area.
5. Detection: the amplitude budget with distance, spreading and absorption.
6. Location uncertainty for four acquisition geometries.
7. Pore pressure needed to trigger slip on a fracture (Mohr-Coulomb).

All models and numbers are SYNTHETIC teaching values: chosen rock properties,
chosen fracture parameters and chosen acquisition geometries.
"""

import numpy as np
from scipy.optimize import least_squares

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def young_poisson(vp, vs, rho):
    """Young's modulus (Pa) and Poisson's ratio from vp, vs (m/s), rho (kg/m^3)."""
    e = rho * vs ** 2 * (3.0 * vp ** 2 - 4.0 * vs ** 2) / (vp ** 2 - vs ** 2)
    nu = (vp ** 2 - 2.0 * vs ** 2) / (2.0 * (vp ** 2 - vs ** 2))
    return e, nu


def main():
    section("1. Elastic moduli and brittleness indices")
    rocks = (("brittle carbonate", 6.20e3, 3.40e3, 2700.0),
             ("shale (clay rich)", 3.20e3, 1.75e3, 2450.0),
             ("organic-rich shale", 2.90e3, 1.60e3, 2350.0),
             ("tight sandstone", 4.60e3, 2.80e3, 2600.0))
    print("  lithology              vp (m/s)   vs (m/s)   rho      E (GPa)   nu")
    moduli = {}
    for name, vp, vs, rho in rocks:
        e, nu = young_poisson(vp, vs, rho)
        moduli[name] = (e, nu)
        print(f"  {name:20s}   {vp:8.0f}   {vs:8.0f}   {rho:7.0f}   "
              f"{e / 1e9:7.1f}   {nu:5.3f}")
    e_vals = [moduli[k][0] for k in moduli]
    nu_vals = [moduli[k][1] for k in moduli]
    e_min, e_max = min(e_vals), max(e_vals)
    nu_min, nu_max = min(nu_vals), max(nu_vals)
    print("\ntwo brittleness conventions, normalised over the four rocks listed")
    print("(stated so the numbers are reproducible; they are not universal):")
    print(f"  BI_E  = (E - {e_min / 1e9:.1f})/({e_max / 1e9:.1f} - {e_min / 1e9:.1f})")
    print(f"  BI_nu = ({nu_max:.3f} - nu)/({nu_max:.3f} - {nu_min:.3f})")
    print("\n   lithology              BI_E     BI_nu")
    bi = {}
    for name in moduli:
        e, nu = moduli[name]
        bi_e = (e - e_min) / (e_max - e_min)
        bi_nu = (nu_max - nu) / (nu_max - nu_min)
        bi[name] = (bi_e, bi_nu)
        print(f"  {name:20s}   {bi_e:5.2f}   {bi_nu:6.2f}")
    by_e = sorted(bi, key=lambda k: -bi[k][0])
    by_nu = sorted(bi, key=lambda k: -bi[k][1])
    print(f"\nranked by BI_E : {', '.join(by_e)}")
    print(f"ranked by BI_nu: {', '.join(by_nu)}")
    if by_e[0] != by_nu[0]:
        print(f"The two conventions disagree at the top: {by_e[0]} is stiffest,")
        print(f"but {by_nu[0]} has the lower Poisson's ratio.  'Brittleness' is a")
    print("proxy for the tendency to fail by fracturing; a proxy inherits its")
    print("calibration set.  Report the convention, the endpoints and the moduli.")

    section("2. VTI anisotropy: exact phase velocities and Thomsen parameters")
    vp_v, vs_v, rho_ani = 3.20e3, 1.80e3, 2450.0
    eps_t, delta_t, gamma_t = 0.20, 0.10, 0.15     # chosen, shale-like
    c33 = rho_ani * vp_v ** 2
    c44 = rho_ani * vs_v ** 2
    c11 = c33 * (1.0 + 2.0 * eps_t)
    c66 = c44 * (1.0 + 2.0 * gamma_t)
    c13 = np.sqrt(2.0 * c33 * (c33 - c44) * delta_t + (c33 - c44) ** 2) - c44
    print(f"vertical vp = {vp_v / 1000:.2f} km/s, vertical vs = "
          f"{vs_v / 1000:.2f} km/s, rho = {rho_ani:.0f} kg/m^3")
    print(f"chosen Thomsen parameters: eps = {eps_t:.2f}, delta = {delta_t:.2f}, "
          f"gamma = {gamma_t:.2f}")
    print(f"stiffnesses: C11 = {c11 / 1e9:.1f}, C33 = {c33 / 1e9:.1f}, "
          f"C13 = {c13 / 1e9:.1f}, C44 = {c44 / 1e9:.1f}, C66 = {c66 / 1e9:.1f} GPa")

    def phase_velocities(theta_deg):
        th = np.radians(theta_deg)
        s2, c2 = np.sin(th) ** 2, np.cos(th) ** 2
        disc = np.sqrt(((c11 - c44) * s2 - (c33 - c44) * c2) ** 2
                       + 4.0 * (c13 + c44) ** 2 * s2 * c2)
        vp = np.sqrt((c11 * s2 + c33 * c2 + c44 + disc) / (2.0 * rho_ani))
        vsv = np.sqrt((c11 * s2 + c33 * c2 + c44 - disc) / (2.0 * rho_ani))
        vsh = np.sqrt((c66 * s2 + c44 * c2) / rho_ani)
        return vp, vsv, vsh

    print("\n   angle (deg)   vp (km/s)   vsv (km/s)   vsh (km/s)")
    for theta in (0.0, 30.0, 45.0, 60.0, 90.0):
        vp, vsv, vsh = phase_velocities(theta)
        print(f"  {theta:12.0f}   {vp / 1000:10.3f}   {vsv / 1000:11.3f}   "
              f"{vsh / 1000:11.3f}")
    vp0 = phase_velocities(0.0)[0]
    vp90 = phase_velocities(90.0)[0]
    vsh0 = phase_velocities(0.0)[2]
    vsh90 = phase_velocities(90.0)[2]
    eps_back = (vp90 ** 2 - vp0 ** 2) / (2.0 * vp0 ** 2)
    gamma_back = (vsh90 ** 2 - vsh0 ** 2) / (2.0 * vsh0 ** 2)
    print(f"\nrecovered from the phase velocities: eps = {eps_back:.4f}, "
          f"gamma = {gamma_back:.4f}")
    print(f"chosen values were eps = {eps_t:.2f}, gamma = {gamma_t:.2f}: the")
    print("recovery is exact because the definitions ARE the 0 and 90 degree")
    print("limits.  Tests of a forward model against its own definitions verify")
    print("the algebra, not the Earth.")
    print("\nwhat ignoring anisotropy costs: NMO velocity in a VTI medium is")
    print("vp_v*sqrt(1+2*delta).  Using the vertical velocity instead biases")
    print(f"depths by sqrt(1+2*delta) = {np.sqrt(1.0 + 2.0 * delta_t):.3f}, i.e. "
          f"{(np.sqrt(1.0 + 2.0 * delta_t) - 1.0) * 100:.1f}%.")

    section("3. HTI fracture anisotropy: shear-wave splitting")
    vs0 = 3.00e3
    print(f"isotropic shear velocity v_s = {vs0 / 1000:.2f} km/s")
    print("for HTI with parameter gamma the two shear modes are polarised along")
    print("and across the fractures: v_fast = v_s sqrt(1+2 gamma), v_slow = v_s")
    print("\n   gamma   v_fast (km/s)   split (%)   dt 50 m   dt 100 m   dt 200 m"
          "  (ms)")
    for gamma in (0.02, 0.05, 0.10):
        v_fast = vs0 * np.sqrt(1.0 + 2.0 * gamma)
        split = (v_fast - vs0) / vs0 * 100
        dts = [d * (1.0 / vs0 - 1.0 / v_fast) * 1000.0 for d in (50.0, 100.0, 200.0)]
        print(f"  {gamma:5.2f}   {v_fast / 1000:12.3f}   {split:9.1f}   "
              f"{dts[0]:8.3f}   {dts[1]:9.3f}   {dts[2]:9.3f}")
    approx = 0.05 * 100.0 / vs0 * 1000.0
    exact = 100.0 * (1.0 / vs0 - 1.0 / (vs0 * np.sqrt(1.1))) * 1000.0
    print(f"first-order form dt ~ gamma*d/v_s: for gamma = 0.05, d = 100 m it")
    print(f"gives {approx:.3f} ms against the exact {exact:.3f} ms, "
          f"{(approx / exact - 1.0) * 100:.0f}% high.")
    print("Splitting measures the path integral of shear anisotropy: it gives")
    print("fracture ORIENTATION and an intensity product, not aperture, not")
    print("connectivity and not permeability.")

    section("4. Microseismic source scaling")
    mu_shear = 20.0e9       # Pa, chosen shear modulus of the source rock
    dsigma = 1.0e6          # Pa, chosen static stress drop
    print(f"chosen shear modulus mu = {mu_shear / 1e9:.1f} GPa, stress drop "
          f"d_sigma = {dsigma / 1e6:.1f} MPa")
    print("circular crack: M0 = (16/7) d_sigma a^3, Mw = (2/3)(log10 M0 - 9.1),")
    print("mean slip u = M0/(mu pi a^2)")
    print("\n   radius a (m)   area (m^2)   M0 (N m)   Mw    mean slip (mm)")
    for a in (10.0, 20.0, 50.0, 100.0):
        m0 = 16.0 / 7.0 * dsigma * a ** 3
        mw = 2.0 / 3.0 * (np.log10(m0) - 9.1)
        area = np.pi * a ** 2
        slip = m0 / (mu_shear * area) * 1000.0
        print(f"  {a:12.0f}   {area:10.1f}   {m0:10.3e}   {mw:5.2f}   "
              f"{slip:15.3f}")
    print("A 100 m rupture with a 1 MPa stress drop is Mw = 2.2: microseismicity")
    print("is small because the ruptures are small, not because the rock is soft.")

    section("5. Detection: the amplitude budget with distance")
    f_dom, v_wave = 20.0, 3000.0
    q_val = 100.0
    print("amplitude model: A(r) = A0 exp(-pi f r / (Q v)) / r,")
    print("geometric spreading 1/r and absorption exp(...)")
    print(f"chosen f = {f_dom:.0f} Hz, v = {v_wave / 1000:.1f} km/s, "
          f"Q = {q_val:.0f}, A0 = 1.0")
    print("\n   distance (m)   1/r          absorption    product   loss (%)")
    for r in (250.0, 500.0, 1000.0, 2000.0, 4000.0):
        geo = 1.0 / r
        abso = np.exp(-np.pi * f_dom * r / (q_val * v_wave))
        print(f"  {r:12.0f}   {geo:9.2e}   {abso:12.4f}   "
              f"{geo * abso:9.2e}   {(1 - abso) * 100:8.1f}")
    print("\n   Q      A0      detection radius (m) for noise floor 1.0e-3")
    for q, a0 in ((50.0, 1.0), (100.0, 1.0), (200.0, 1.0), (100.0, 3.0)):
        r = 100.0
        while r < 50000.0:
            if a0 * np.exp(-np.pi * f_dom * r / (q * v_wave)) / r < 1.0e-3:
                break
            r += 10.0
        print(f"  {q:4.0f}   {a0:5.1f}   {r:33.0f}")
    print("At these ranges the 1/r term dominates: between Q = 50 and Q = 200 the")
    print("detection radius moves from 740 m to 910 m, while a 3x amplitude gain")
    print("moves it to 1990 m.  Detection range is a budget, not a property of")
    print("the event, and improving resolution by raising frequency shortens it.")

    section("6. Location uncertainty for four acquisition geometries")
    v_pick = 3000.0
    sigma_pick = 0.002      # s, chosen arrival-time pick error
    t0 = 0.35               # s, chosen origin time
    src = np.array([2000.0, 2000.0, 3000.0])
    surf16 = np.array([[x, y, 0.0] for x in (0.0, 4000.0)
                       for y in (0.0, 4000.0)]
                      + [[x, y, 0.0] for x in (1000.0, 3000.0)
                         for y in (1000.0, 3000.0)])
    surf4 = np.array(  # perfectly symmetric about the source
        [[0.0, 0.0, 0.0], [4000.0, 0.0, 0.0],
         [0.0, 4000.0, 0.0], [4000.0, 4000.0, 0.0]])
    dh12 = np.array([[1800.0, 2000.0, z]
                     for z in np.linspace(1500.0, 2500.0, 12)])

    def solve(stations, picks, known_t0):
        if known_t0:
            def resid(m):
                return (t0 + np.linalg.norm(stations - m, axis=1) / v_pick) - picks
            out = least_squares(resid, np.array(
                [stations[:, 0].mean(), stations[:, 1].mean(), 3000.0]),
                method="trf")
            return out.x, np.sqrt(np.mean(out.fun ** 2))

        def resid(m):
            return (m[3] + np.linalg.norm(stations - m[:3], axis=1) / v_pick) - picks
        out = least_squares(resid, np.array([stations[:, 0].mean(),
                                             stations[:, 1].mean(), 1500.0, 0.5]),
                            method="trf")
        return out.x[:3], np.sqrt(np.mean(out.fun ** 2))

    cases = (("16 surface stations, 4 km aperture", surf16, False, src),
             ("4 symmetric surface corners", surf4, False, src),
             ("12-level downhole, origin time unknown", dh12, False,
              np.array([2300.0, 2000.0, 3000.0])),
             ("12-level downhole, origin time known", dh12, True,
              np.array([2300.0, 2000.0, 3000.0])))
    print(f"chosen pick error = {sigma_pick * 1000:.0f} ms, v = "
          f"{v_pick / 1000:.1f} km/s, origin time = {t0:.2f} s, 100 realisations")
    print("\n   geometry                                error (m)   depth error (m)"
          "   residual (ms)")
    for label, stations, known, true in cases:
        picks_true = t0 + np.linalg.norm(stations - true, axis=1) / v_pick
        errs, zerrs, residuals = [], [], []
        for _ in range(100):
            picks = picks_true + sigma_pick * RNG.standard_normal(stations.shape[0])
            est, rms = solve(stations, picks, known)
            errs.append(np.linalg.norm(est - true))
            zerrs.append(abs(est[2] - true[2]))
            residuals.append(rms)
        print(f"  {label:38s}   {np.mean(errs):8.0f}   {np.mean(zerrs):14.0f}   "
              f"{np.mean(residuals) * 1000:12.2f}")
    print("\nEvery row fits the picks to within the pick error, and the locations")
    print("still differ by two orders of magnitude.  Geometry, not misfit, is")
    print("what decides; a microseismic cloud is a set of locations WITH these")
    print("error bars, and the depth-origin-time trade-off is the usual culprit.")

    section("7. Pore pressure needed to trigger slip")
    print("Coulomb condition for a cohesionless fracture: tau >= mu_f (sigma_n - P)")
    print("so slip starts at  P >= sigma_n - tau / mu_f.  A negative answer means")
    print("the fracture is already critically stressed before any injection.")
    print("\n   sigma_n (MPa)   tau/sigma_n   mu_f = 0.4   mu_f = 0.6   mu_f = 0.8"
          "   (required P, MPa)")
    for sigma_n, tau in ((40.0, 20.0), (40.0, 26.0), (60.0, 39.0)):
        row = []
        for mu_f in (0.4, 0.6, 0.8):
            p_req = sigma_n - tau / mu_f
            row.append("already critical" if p_req <= 0.0 else f"{p_req:.1f}")
        print(f"  {sigma_n:13.0f}   {tau / sigma_n:11.2f}   {row[0]:>11s}   "
              f"{row[1]:>11s}   {row[2]:>11s}")
    print("\nA stress state already near failure needs only a small pressure")
    print("change, and the same pressure change is safe on a fracture in a")
    print("different orientation.  Induced seismicity therefore depends on the")
    print("pre-existing stress field and the fracture orientations, neither of")
    print("which a surface geophysical survey measures directly.")


if __name__ == "__main__":
    main()
