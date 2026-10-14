#!/usr/bin/env python3
"""Upper-mantle discontinuities: how a phase boundary becomes a depth, a
temperature, and a sharpness measurement -- and where each conversion breaks.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python upper_mantle_discontinuities_demo.py

Everything is SYNTHETIC.  Clapeyron slopes, densities, velocities, entropy and
volume changes are chosen teaching values, not measured ones.  No published
discontinuity topography, no real seismogram and no station is used.  The depths
410 km and 660 km are used as conventional labels.

Contents
--------
1. Clapeyron slopes: dz/dT = gamma / (rho g), with an independent check from
   gamma = dS/dV.
2. The SS-precursor style delay of an underside reflection: 2 z q_s.
3. Temperature topography and the delay it produces, inverted back to a
   temperature.
4. The transition zone as a differential thermometer: the two boundaries move in
   opposite directions, so the thickness signal is amplified.
5. Reflection coefficients of the two boundaries, and how a gradational
   transition filters them: sharpness is measured relative to a wavelength.
6. The topography-versus-velocity trade-off in one delay, with a Jacobian.
7. Triplication: the travel-time offset produced by a first-order jump.
"""

import numpy as np

RNG = np.random.default_rng(20261014)


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --- SYNTHETIC phase-boundary and elastic parameters (chosen) ---------------
D_410, D_660 = 410.0, 660.0            # km, conventional depths
G_410, G_660 = 2.0, -3.0               # MPa/K, Clapeyron slopes (chosen)
RHO_410, RHO_660 = 3600.0, 4400.0      # kg/m^3
G_ACC = 9.81                           # m/s^2
VS_410, VS_660 = 4.70, 5.80            # km/s
P_TEL = 0.055                          # s/km, teleseismic SS ray parameter
DS_410, DV_410 = -5.5, -2.6e-6         # J/(mol K), m^3/mol (chosen)
DS_660, DV_660 = +8.0, -3.0e-6         # endothermic at 660: dS > 0, dV < 0


def clapeyron_gamma(ds, dv):
    """gamma = dP/dT = dS/dV, converted from Pa/K to MPa/K."""
    return ds / dv / 1.0e6


def topo_per_kelvin(gamma_mpa, rho, g=G_ACC):
    """dz/dT = gamma / (rho g), returned in metres per kelvin."""
    return gamma_mpa * 1.0e6 / (rho * g)


def q_s(vs_km_s, p_s_km):
    """S vertical slowness, s/km."""
    return np.sqrt(1.0 / vs_km_s ** 2 - p_s_km ** 2)


def main():
    section("1. Clapeyron slopes and the topographic response")
    print("  a phase boundary at pressure P0 + gamma (T - T0) sits at")
    print("  z = z0 + gamma (T - T0) / (rho g), so dz/dT = gamma / (rho g).")
    dzdt_410 = topo_per_kelvin(G_410, RHO_410)
    dzdt_660 = topo_per_kelvin(G_660, RHO_660)
    print(f"  410 km: gamma = {G_410:+.1f} MPa/K, rho = {RHO_410:.0f} kg/m^3"
          f"  ->  dz/dT = {dzdt_410:+.2f} m/K")
    print(f"  660 km: gamma = {G_660:+.1f} MPa/K, rho = {RHO_660:.0f} kg/m^3"
          f"  ->  dz/dT = {dzdt_660:+.2f} m/K")
    print("  independent check, gamma = dS/dV:")
    for name, ds, dv in (("410", DS_410, DV_410), ("660", DS_660, DV_660)):
        print(f"    {name}: dS = {ds:+.1f} J/(mol K), dV = {dv * 1e6:+.2f} cm^3/mol"
              f"  ->  gamma = {clapeyron_gamma(ds, dv):+.2f} MPa/K")
    print("  the sign follows the sign of dS/dV: dS < 0 with dV < 0 gives a")
    print("  positive slope (the boundary deepens when it is hot), and the")
    print("  reverse combination gives a negative one.")

    section("2. The delay of an underside reflection (SS-precursor geometry)")
    print(f"  a wave with ray parameter p = {P_TEL:.3f} s/km reflecting off the")
    print("  underside of a boundary at depth z arrives 2 z q_s before the surface")
    print("  reflection, where q_s = sqrt(1/vs^2 - p^2):")
    print("    boundary   vs (km/s)   q_s (s/km)   two-way delay (s)")
    for name, z, vs in (("410 km", D_410, VS_410), ("660 km", D_660, VS_660)):
        qq = q_s(vs, P_TEL)
        print(f"    {name:9s}  {vs:8.2f}   {qq:10.5f}   {2.0 * z * qq:14.2f}")
    d410 = 2.0 * D_410 * q_s(VS_410, P_TEL)
    d660 = 2.0 * D_660 * q_s(VS_660, P_TEL)
    print(f"  the two precursors are separated by {d660 - d410:.2f} s, which is")
    print("  twice the S travel time across the transition zone at this slowness.")

    section("3. Temperature topography, and its inversion")
    print(f"  at p = {P_TEL:.3f} s/km, a boundary displaced by dz changes its")
    print(f"  precursor delay by 2 q_s dz; for the 410 km boundary, "
          f"2 q_s = {2 * q_s(VS_410, P_TEL):.4f} s/km.")
    print("    dT (K)    dz (km)    delay change (s) for the 410 km boundary")
    for dt in (-200, -100, -50, 50, 100, 200):
        dz = dzdt_410 * dt / 1000.0
        print(f"  {dt:8.0f}  {dz:9.2f}   {2.0 * q_s(VS_410, P_TEL) * dz:14.3f}")
    print("  inversion: a measured differential delay of +1.00 s corresponds to")
    dz_need = 1.0 / (2.0 * q_s(VS_410, P_TEL))
    print(f"    dz = {dz_need:.3f} km, i.e. dT = {dz_need * 1000.0 / dzdt_410:+.1f} K")
    print("  the conversion is exact arithmetic, and its uncertainty is the")
    print("  uncertainty in gamma and in the velocity structure used for q_s.")

    section("4. The transition zone as a differential thermometer")
    print("  the two boundaries move in OPPOSITE directions for the same")
    print("  temperature anomaly, so the thickness signal is the sum:")
    print("    dT (K)   dz_410 (km)   dz_660 (km)   TZ thickness change (km)")
    for dt in (-200, -100, -50, 50, 100, 200):
        dz1 = dzdt_410 * dt / 1000.0
        dz2 = dzdt_660 * dt / 1000.0
        print(f"  {dt:8.0f}  {dz1:11.2f}   {dz2:11.2f}   {dz2 - dz1:20.2f}")
    combined = abs(dzdt_410) + abs(dzdt_660)
    print(f"  the thickness sensitivity is {combined:.1f} m/K, the SUM of the two")
    print(f"  single-boundary sensitivities ({abs(dzdt_410):.1f} and "
          f"{abs(dzdt_660):.1f} m/K), not their difference.")
    print("  a 100 K cooling thickens the transition zone by "
          f"{combined * 100 / 1000:.2f} km.")

    section("5. Reflection coefficients and the sharpness filter")
    jumps = (("410 km", (3.54, 4.66), (3.65, 4.80)),
             ("660 km", (3.99, 5.55), (4.01, 5.85)))
    print("  normal-incidence S reflection coefficient R = (Z2 - Z1)/(Z2 + Z1)")
    print("  with Z = rho vs, for the SYNTHETIC jumps (rho, vs) of lesson 01:")
    for name, above, below in jumps:
        z1 = above[0] * above[1]
        z2 = below[0] * below[1]
        print(f"    {name}: (rho, vs) {above} -> {below}")
        print(f"            Z1 = {z1:6.3f}, Z2 = {z2:6.3f}, "
              f"R = {(z2 - z1) / (z2 + z1):+.4f}"
              f"  ({(z2 - z1) / (z2 + z1) * 100:+.2f} % amplitude)")
    R0 = 0.0305
    f_dom = 0.20          # Hz, a 5 s dominant period
    print(f"\n  a gradational boundary of one-way duration tau filters the")
    print(f"  reflection by sinc(pi f tau); at f = {f_dom:.2f} Hz (5 s period):")
    print("    transition width (km)   tau (s)   |R| / R0")
    for w in (0.0, 2.0, 5.0, 10.0, 20.0, 23.5, 40.0):
        if w == 0.0:
            ratio = 1.0
            tau = 0.0
        else:
            tau = w / VS_410
            arg = np.pi * f_dom * tau
            ratio = abs(np.sin(arg) / arg)
        print(f"  {w:21.1f}   {tau:7.3f}   {ratio:9.4f}")
    print("  the reflection vanishes when tau = 1/f, i.e. when the transition")
    print(f"  takes as long as one period: here {1.0 / f_dom:.1f} s, or "
          f"{VS_410 / f_dom:.1f} km.")
    print("  the 40 km row is the first side lobe of the sinc: |R| rises again")
    print("  with reversed polarity, so a weak inverted reflection is not")
    print("  evidence of a sharp boundary.")
    print("  SHARPNESS IS THEREFORE MEASURED RELATIVE TO A FREQUENCY, not in")
    print("  kilometres: the same 10 km transition is sharp at 0.05 Hz and")
    print("  invisible at 0.5 Hz.")

    section("6. Topography or velocity? one delay, two explanations")
    tz_thickness = D_660 - D_410
    dq = 2.0 * q_s(VS_410, P_TEL)
    print("  a precursor delay change can come from moving the boundary or from")
    print("  changing the velocity above it:")
    print(f"    d(delay)/d(dz)              = {dq:+.5f} s/km")
    frac = 0.01
    dt_vel = 2.0 * tz_thickness * frac / VS_410
    print(f"    a {frac * 100:.0f} % vs reduction over the whole {tz_thickness:.0f} km"
          f" transition zone gives {dt_vel:.3f} s")
    print(f"    d(delay)/d(vs/vs)           = {dt_vel / frac:+.3f} s per unit "
          "fractional change")
    print("  so 1 % of velocity is equivalent to "
          f"{dt_vel / dq:.2f} km of boundary motion:")
    print("  the two mechanisms are degenerate in a single delay.  Breaking the")
    print("  degeneracy requires either a second slowness (the two have different")
    print("  moveout) or an absolute constraint on one of them.")

    section("7. Triplication: what a first-order jump does to the travel time")
    v_above, v_below = 8.90, 9.60        # km/s across the 410 km jump
    print(f"  a jump from {v_above:.2f} to {v_below:.2f} km/s at "
          f"{D_410:.0f} km produces")
    print("  three branches at the same distance: the direct ray, the ray that")
    print("  turns just below the jump, and the ray that grazes it.")
    print("  the classic diagnostic is the distance offset of the triplication:")
    print("    p_crit (s/rad)   turning radius (km)   note")
    for label, v, z in (("above", v_above, D_410 - 1.0), ("below", v_below, D_410 + 1.0)):
        r = 6371.0 - z
        print(f"    {r / v:13.2f}   {r:19.1f}   {label} the jump")
    p_above = (6371.0 - D_410 + 1.0) / v_above
    p_below = (6371.0 - D_410 - 1.0) / v_below
    print(f"    p jumps from {p_below:.2f} to {p_above:.2f} s/rad across the")
    print(f"    boundary, a change of {p_above - p_below:.2f} s/rad "
          f"({(p_above - p_below) / p_below * 100:.1f} %)")
    print("  that discontinuity in p is the jump in dT/dDelta, and it is what")
    print("  produces the observed offset in the travel-time curve.")
    print("  A velocity gradient instead of a jump gives a continuous p(Delta),")
    print("  hence no offset, hence no observable 'discontinuity' in the times.")


if __name__ == "__main__":
    main()
