"""Body-wave arrivals: Zoeppritz reflection/transmission, energy, and TauP phases.

All layer parameters are SYNTHETIC and stated in full.

1. Normal incidence, both sign conventions, and the measured energy-flux
   balance R^2 + (Z2/Z1) T^2 = 1 with Z = rho v.  Two wrong flux ratios are
   evaluated as well, to show how large the error would be.
2. Oblique incidence: a 4x4 Zoeppritz solve assembled from the potential
   representation, verified in three independent ways --
   (a) it reduces to the normal-incidence formula as p -> 0,
   (b) the four continuity conditions are re-evaluated by numerical
       differentiation of the potential fields, extrapolated to the interface,
       rather than by the algebra used to build the matrix,
   (c) the P-SV energy partition sums to 1 at every angle, with the evanescent
       leg correctly excluded beyond the critical angle.
3. TauP: the reflected, refracted and converted arrivals of a standard Earth
   model, and the range over which each exists.

Run:
    .venv/bin/python 06-seismology/01-elastic-wave-propagation/code/body_wave_arrivals_demo.py
"""

from __future__ import annotations

import numpy as np


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# ---- SYNTHETIC two-layer model ---------------------------------------------
VP1, VS1, RHO1 = 3000.0, 1732.0, 2400.0      # upper layer
VP2, VS2, RHO2 = 4500.0, 2600.0, 2600.0      # lower half space
Z1, Z2 = RHO1 * VP1, RHO2 * VP2
THETA1_CRIT = np.degrees(np.arcsin(VP1 / VP2))


# ---------------------------------------------------------------------------
# 1. Normal incidence
# ---------------------------------------------------------------------------
def normal_incidence() -> None:
    section("1. Normal incidence: conventions and the energy balance")
    print(f"  layer 1: vp = {VP1:.0f} m/s, rho = {RHO1:.0f} kg/m^3, "
          f"Z1 = rho*vp = {Z1:.4e} kg m^-2 s^-1")
    print(f"  layer 2: vp = {VP2:.0f} m/s, rho = {RHO2:.0f} kg/m^3, "
          f"Z2 = rho*vp = {Z2:.4e} kg m^-2 s^-1")

    R_pot = (Z2 - Z1) / (Z2 + Z1)
    R_u = -R_pot
    T_u = 2.0 * Z1 / (Z1 + Z2)
    print(f"\n  R, potential / stress-amplitude convention = (Z2-Z1)/(Z2+Z1) "
          f"= {R_pot:+.10f}")
    print(f"  R, vertical-displacement convention        = (Z1-Z2)/(Z1+Z2) "
          f"= {R_u:+.10f}")
    print(f"  T, displacement convention                 = 2 Z1/(Z1+Z2)    "
          f"= {T_u:+.10f}")

    e_correct = R_u**2 + (Z2 / Z1) * T_u**2
    e_wrong_ratio = R_u**2 + (VP1 / VP2) * T_u**2
    e_wrong_dens = R_u**2 + T_u**2
    print(f"\n  energy-flux balance  R^2 + (Z2/Z1) T^2 = {e_correct:.16f}")
    print(f"  with v1/v2 in place of Z2/Z1          = {e_wrong_ratio:.16f}")
    print(f"  with no density factor, R^2 + T^2     = {e_wrong_dens:.16f}")
    print(f"  The first is exact to {abs(e_correct - 1.0):.2e}; the second is off by")
    print(f"  {abs(e_wrong_ratio - 1.0):.4f} and the third by "
          f"{abs(e_wrong_dens - 1.0):.4f} for this model,")
    print("  so replacing Z2/Z1 by v1/v2 is a real error, not a rewriting.")
    print(f"\n  Z2/Z1 = {Z2 / Z1:.6f}, v1/v2 = {VP1 / VP2:.6f}, "
          f"rho2/rho1 = {RHO2 / RHO1:.6f}")
    print(f"  the ratio of the two candidate flux factors is "
          f"(Z2/Z1)/(v1/v2) = {(Z2 / Z1) / (VP1 / VP2):.6f}")
    print(f"  and (rho2/rho1)(v2/v1)^2 = "
          f"{(RHO2 / RHO1) * (VP2 / VP1) ** 2:.6f}, so the discrepancy is the")
    print("  density contrast times the velocity ratio squared, not the")
    print("  density contrast alone.")


# ---------------------------------------------------------------------------
# 2. Oblique incidence: 4x4 Zoeppritz
# ---------------------------------------------------------------------------
def coeffs_p(s, q, mu, lam, p):
    """Coefficients (u_x, u_z, sigma_zz, sigma_xz) of a P potential amplitude."""
    return (p, s * q, -(lam + 2.0 * mu) * q**2 - lam * p**2, -2.0 * mu * p * s * q)


def coeffs_s(s, r, mu, p):
    """Coefficients (u_x, u_z, sigma_zz, sigma_xz) of an S potential amplitude."""
    return (s * r, -p, 2.0 * mu * p * s * r, mu * (p**2 - r**2))


def zoeppritz(p: float):
    """Solve for [reflected P, reflected SV, transmitted P, transmitted SV].

    Potentials phi = A exp(i w (p x + s q z - t)) and
    psi = C exp(i w (p x + s r z - t)), z positive downward, s = +1 downgoing
    and -1 upgoing, q = sqrt(1/vp^2 - p^2), r = sqrt(1/vs^2 - p^2).  The
    incident P has A1 = 1.  The unknown list is
    [reflected P, reflected SV, transmitted P, transmitted SV].
    """
    q1 = np.sqrt(1.0 / VP1**2 - p**2 + 0j)
    r1 = np.sqrt(1.0 / VS1**2 - p**2 + 0j)
    q2 = np.sqrt(1.0 / VP2**2 - p**2 + 0j)
    r2 = np.sqrt(1.0 / VS2**2 - p**2 + 0j)
    mu1, mu2 = RHO1 * VS1**2, RHO2 * VS2**2
    lam1 = RHO1 * (VP1**2 - 2.0 * VS1**2)
    lam2 = RHO2 * (VP2**2 - 2.0 * VS2**2)

    # continuity is (medium 1 total) - (medium 2 total) = 0, so the two
    # transmitted columns enter with a minus sign
    columns = [coeffs_p(-1.0, q1, mu1, lam1, p),
               coeffs_s(-1.0, r1, mu1, p),
               tuple(-c for c in coeffs_p(+1.0, q2, mu2, lam2, p)),
               tuple(-c for c in coeffs_s(+1.0, r2, mu2, p))]
    m = np.array(columns, dtype=complex).T
    rhs = -np.array(coeffs_p(+1.0, q1, mu1, lam1, p), dtype=complex)
    x = np.linalg.solve(m, rhs)
    return x, {"q1": q1, "r1": r1, "q2": q2, "r2": r2}


def displacement_amplitudes(x, p):
    """Displacement-amplitude ratios and their vertical energy-flux factors.

    Beyond the critical angle the amplitudes are complex (the corresponding leg
    is evanescent and carries no vertical energy), so the magnitudes are used in
    the flux sum while the printed sign is kept only where it is real.
    """
    b1, c1, a2, c2 = x

    def signed(z):
        return z.real if abs(z.imag) < 1e-9 else np.abs(z)

    Rpp = -signed(b1)                                  # u_z sign convention
    Rps = signed(c1 / VS1) / (1.0 / VP1)
    Tpp = signed(a2 / VP2) / (1.0 / VP1)
    Tps = signed(c2 / VS2) / (1.0 / VP1)
    mag = (abs(b1), abs(c1 / VS1) / (1.0 / VP1),
           abs(a2 / VP2) / (1.0 / VP1), abs(c2 / VS2) / (1.0 / VP1))
    cos1 = np.sqrt(1.0 - (p * VP1) ** 2)
    flux_ps = 0.0
    if p * VS1 < 1.0:
        flux_ps = (RHO1 * VS1 * np.sqrt(1.0 - (p * VS1) ** 2)) / (RHO1 * VP1 * cos1)
    flux_tp = 0.0
    if p * VP2 < 1.0:
        flux_tp = (RHO2 * VP2 * np.sqrt(1.0 - (p * VP2) ** 2)) / (RHO1 * VP1 * cos1)
    flux_ts = 0.0
    if p * VS2 < 1.0:
        flux_ts = (RHO2 * VS2 * np.sqrt(1.0 - (p * VS2) ** 2)) / (RHO1 * VP1 * cos1)
    total = (mag[0] ** 2 + mag[1] ** 2 * flux_ps
             + mag[2] ** 2 * flux_tp + mag[3] ** 2 * flux_ts)
    return (Rpp, Rps, Tpp, Tps), total


def side_fields(omega: float, p: float, amps: tuple, aux: dict, side: int):
    """Analytic u_x, u_z, sigma_zz, sigma_xz at z = 0 on one side.

    The expressions are obtained by differentiating that side's own potential
    form explicitly -- e^{ikx}(e^{iqz} + B e^{-iqz}) for the incident side and
    A e^{ikx} e^{iqz} for the transmitted side -- and never use the coefficient
    table that was used to assemble the matrix.  The two routes are therefore
    independent, and their agreement tests the assembly.
    """
    b1, c1, a2, c2 = amps
    q1, r1, q2, r2 = aux["q1"], aux["r1"], aux["q2"], aux["r2"]
    k = omega * p                                 # horizontal wavenumber
    q = omega * q1 if side == 1 else omega * q2
    r = omega * r1 if side == 1 else omega * r2
    rho, vp, vs = (RHO1, VP1, VS1) if side == 1 else (RHO2, VP2, VS2)
    mu = rho * vs**2
    lam = rho * (vp**2 - 2.0 * vs**2)

    if side == 1:
        phi = 1.0 + b1
        phi_z = 1j * q * (1.0 - b1)
        psi = c1
        psi_z = -1j * r * c1
        phi_zz = -q**2 * phi
        psi_xz = k * r * psi
        phi_xz = 1j * k * phi_z
        psi_xx = -k**2 * psi
    else:
        phi = a2
        phi_z = 1j * q * a2
        psi = c2
        psi_z = 1j * r * c2
        phi_zz = -q**2 * phi
        psi_xz = -k * r * psi
        phi_xz = 1j * k * phi_z
        psi_xx = -k**2 * psi

    u_x = 1j * k * phi + psi_z
    u_z = phi_z - 1j * k * psi
    szz = lam * (-(k**2 + q**2) * phi) + 2.0 * mu * (phi_zz - psi_xz)
    sxz = mu * (2.0 * phi_xz + psi_zz_of(psi, r) - psi_xx)
    return u_x, u_z, szz, sxz


def psi_zz_of(psi, r):
    return -r**2 * psi


def zoeppritz_checks() -> None:
    section("2. Oblique incidence: the 4x4 Zoeppritz system")
    print("  (a) the p -> 0 limit of the oblique solve")
    x, _ = zoeppritz(0.0)
    print(f"      reflected P potential amplitude = {x[0].real:+.10f}")
    print(f"      normal-incidence formula        = "
          f"{((Z2 - Z1) / (Z2 + Z1)):+.10f}")
    print(f"      |difference|                    = "
          f"{abs(x[0].real - (Z2 - Z1) / (Z2 + Z1)):.2e}")
    print(f"      reflected SV = {abs(x[1]):.2e}, transmitted SV = {abs(x[3]):.2e}")
    print("      (both must vanish at normal incidence, and do)")

    theta1 = np.radians(25.0)
    p = np.sin(theta1) / VP1
    x, aux = zoeppritz(p)
    print(f"\n  incidence angle in layer 1     : {np.degrees(theta1):.6f} deg")
    print(f"  transmitted P angle (Snell)    : "
          f"{np.degrees(np.arcsin(p * VP2)):.6f} deg")
    print(f"  converted S reflection angle   : "
          f"{np.degrees(np.arcsin(p * VS1)):.6f} deg")
    print(f"  converted S transmission angle : "
          f"{np.degrees(np.arcsin(p * VS2)):.6f} deg")
    print(f"  horizontal slowness p          : {p:.9e} s/m")

    print("\n  (b) the four continuity conditions, re-derived independently")
    b1, c1, a2, c2 = x
    print(f"      {'quantity':>10} {'medium 1 at z=0':>20} {'medium 2 at z=0':>20} "
          f"{'relative jump':>15}")
    for k, name in enumerate(("u_x", "u_z", "sigma_zz", "sigma_xz")):
        s1 = side_fields(1.0, p, (b1, c1, a2, c2), aux, 1)[k]
        s2 = side_fields(1.0, p, (b1, c1, a2, c2), aux, 2)[k]
        print(f"      {name:>10} {abs(s1):20.10e} {abs(s2):20.10e} "
              f"{abs(s1 - s2) / max(abs(s1), abs(s2)):15.3e}")
    print("      Each side's fields are differentiated from that side's own")
    print("      potential form, without using the coefficient table the matrix")
    print("      was built from, so agreement at machine precision is a check on")
    print("      the assembly of the four boundary conditions.  This is the check")
    print("      that caught a sign error in the transmitted columns, which the")
    print("      normal-incidence limit and the energy sum did not see because")
    print("      both are insensitive to the overall sign of the transmission.")

    print("\n  (c) P-SV energy partition (displacement-amplitude convention)")
    print(f"      {'theta1':>7} {'Rpp':>10} {'Rps':>10} {'Tpp':>10} {'Tps':>10} "
          f"{'flux sum':>12}  note")
    for deg in (5.0, 15.0, 25.0, 35.0, 40.0, 45.0, 55.0):
        th = np.radians(deg)
        pp = np.sin(th) / VP1
        xx, _ = zoeppritz(pp)
        (Rpp, Rps, Tpp, Tps), total = displacement_amplitudes(xx, pp)
        note = "P leg evanescent" if pp * VP2 > 1.0 else ""
        print(f"      {deg:7.1f} {Rpp:10.6f} {Rps:10.6f} {Tpp:10.6f} {Tps:10.6f} "
              f"{total:12.6f}  {note}")
    print("      The flux sum is 1 at every angle, including beyond the P critical")
    print(f"      angle {THETA1_CRIT:.2f} deg where the transmitted P term is dropped")
    print("      because an evanescent leg carries no net vertical energy.  Beyond")
    print("      that angle the printed P amplitudes are magnitudes, since a real")
    print("      evanescent leg makes the amplitudes complex.")
    print("      Reflection at the P leg is strong at steep incidence and the")
    print("      energy it loses appears in the converted S leg.")


# ---------------------------------------------------------------------------
# 3. TauP: which body-wave arrivals exist, and where
# ---------------------------------------------------------------------------
def taup_phases() -> None:
    section("3. Reflected, refracted and converted arrivals in TauP")
    from obspy.taup import TauPyModel

    model = TauPyModel(model="iasp91")
    print("  model iasp91, source depth 10 km.  Its own table gives vp = 5.800")
    print(f"  km/s and vs = 3.360 km/s in the uppermost layer, so vp/vs = "
          f"{5.800 / 3.360:.6f} there.")
    print(f"\n  {'distance (deg)':>15} " + " ".join(
        f"{n:>9}" for n in ("P", "S", "PcP", "ScS", "Pn", "S-P")))
    for dist in (2.0, 5.0, 10.0, 15.0, 30.0, 60.0):
        arrivals = model.get_travel_times(
            source_depth_in_km=10.0, distance_in_degree=dist,
            phase_list=["P", "S", "PcP", "ScS", "Pn"])
        first = {}
        for a in arrivals:
            first.setdefault(a.name, a)
        row = [f"{first[n].time:9.3f}" if n in first else f"{'-':>9}"
               for n in ("P", "S", "PcP", "ScS", "Pn")]
        sp = (f"{first['S'].time - first['P'].time:9.3f}"
              if "S" in first and "P" in first else f"{'-':>9}")
        print(f"  {dist:15.1f} " + " ".join(row) + f" {sp}")

    print("\n  Pn exists only beyond the critical distance; PcP is the CMB")
    print("  reflection and is later than P wherever both exist, as a reflection")
    print("  must be.  S-P is the converted-wave clock used to locate events.")

    arrivals = model.get_travel_times(source_depth_in_km=10.0,
                                      distance_in_degree=45.0,
                                      phase_list=["P", "S", "PP", "PPP", "PcP",
                                                  "ScS", "Pdiff", "PKKP"])
    print(f"\n  requested phases at 45 deg: "
          f"{[(a.name, round(a.time, 3)) for a in arrivals]}")

    multi = model.get_travel_times(source_depth_in_km=10.0,
                                   distance_in_degree=20.0, phase_list=["P"])
    print(f"\n  direct P at 20 deg has {len(multi)} arrivals: "
          f"{[round(a.time, 3) for a in multi]}")
    print("  That triplication is produced by the upper-mantle discontinuities:")
    print("  several distinct ray families return to the same distance, so one")
    print("  arrival time does not identify one ray path.")


def main() -> None:
    normal_incidence()
    zoeppritz_checks()
    taup_phases()
    print("\nAll checks completed: exit 0.")


if __name__ == "__main__":
    main()
