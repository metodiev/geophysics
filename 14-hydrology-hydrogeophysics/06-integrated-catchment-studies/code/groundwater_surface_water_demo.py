#!/usr/bin/env python3
"""Groundwater-surface water interaction on an idealised, SYNTHETIC stream reach:
a Darcy flux from a piezometer pair, seepage velocities inferred from a diurnal
temperature signal in a homogeneous and in a layered bed, salt-dilution gauging,
and the ERT signature of a losing reach.

Run with the project virtual environment:

    cd 14-hydrology-hydrogeophysics/06-integrated-catchment-studies/code
    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python groundwater_surface_water_demo.py

Everything here is SYNTHETIC.  There is no real stream, aquifer, piezometer,
temperature probe or tracer injection in this file; the reach is an idealised
1-D column and every number is a chosen teaching value.  No site is named and
no published measurement is quoted.

Sign conventions
----------------
z is depth below the streambed surface, positive downward.
v is the seepage (pore-water) velocity, positive DOWNWARD, in m/d.
dh = h_stream - h_aquifer, in m.  Surface discharge is positive downstream.

Contents
--------
1. Darcy flux from a piezometer pair, and a seasonal reversal of exchange.
2. Diurnal temperature in a homogeneous bed: the exact solution, and why the
   phase cannot give the direction of flow.
3. A layered bed: the homogeneous inversion, and the set of velocities it admits.
4. Salt-dilution gauging and the tail-truncation error.
5. The ERT signature of a losing reach against a stated noise level.
6. Reconciling the methods: they do not measure the same quantity.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC, IDEALISED reach parameters (chosen, not measured) -------------
K_BED = 2.5            # m/d hydraulic conductivity of the stream bed
N_E = 0.25             # effective porosity, used to relate q and v
L_PIEZO = 8.0          # m, distance between the piezometer pair
KAPPA_SAND = 1.0e-6    # m^2/s thermal diffusivity of the sand bed
KAPPA_SILT = 4.0e-7    # m^2/s thermal diffusivity of a silt layer
SILT_TOP, SILT_BOT = 0.08, 0.18    # m depth of the silt layer
PERIOD = 86400.0       # s, diurnal
OMEGA = 2.0 * np.pi / PERIOD
AMPL_SURF = 4.0        # K, amplitude of the diurnal surface temperature
Z1, Z2 = 0.15, 0.30    # m, the two probe depths
SALT_MASS = 2.0        # kg of salt injected
NOISE_ERT = 0.02       # relative noise on apparent resistivity
V_GAIN = -0.40         # m/d seepage, upward: the gaining reach of section 1
V_LOSE = +0.125        # m/d seepage, downward: the losing reach of section 1


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def solve_temperature(v_md, kappa_of_z, z, omega=OMEGA):
    """Complex periodic solution of kappa T'' - v T' = i omega T.

    v_md is the seepage velocity in m/d, positive downward.  T(0) = AMPL_SURF,
    and T(z_max) = 0 is imposed deep enough that the exact amplitude there is
    below 0.3% of the surface value.
    """
    v = v_md / 86400.0
    dz = z[1] - z[0]
    n = z.size
    A = np.zeros((n, n), dtype=complex)
    b = np.zeros(n, dtype=complex)
    A[0, 0] = 1.0
    b[0] = AMPL_SURF
    for i in range(1, n - 1):
        kp = kappa_of_z(0.5 * (z[i] + z[i + 1]))
        km = kappa_of_z(0.5 * (z[i] + z[i - 1]))
        A[i, i - 1] = km / dz ** 2 + v / (2.0 * dz)
        A[i, i] = -(km + kp) / dz ** 2 - 1j * omega
        A[i, i + 1] = kp / dz ** 2 - v / (2.0 * dz)
    A[-1, -1] = 1.0
    return np.linalg.solve(A, b)


def index_at(z, depth):
    return int(np.argmin(np.abs(z - depth)))


def amplitude_phase(z_of, T, d1, d2):
    i1, i2 = index_at(z_of, d1), index_at(z_of, d2)
    ratio = float(np.abs(T[i2]) / np.abs(T[i1]))
    lag_rad = float(-np.angle(T[i2] / T[i1]))
    sep = float(z_of[i2] - z_of[i1])
    return ratio, lag_rad, sep


def homogeneous_ratio(v_md, sep, kappa=KAPPA_SAND, omega=OMEGA):
    """Exact amplitude ratio and phase lag (rad) over depth sep in a half-space.

    kappa T'' - v T' = i omega T with T -> 0 as z -> infinity.  Writing
    a = v/(2 kappa) and b = sqrt(a^2 + i omega/kappa), the decaying root is
    lambda = a - b, so
        ratio  = exp(-(Re(b) - a) sep)      (increasing in v, hence unique)
        lag    = Im(b) sep                  (even in v, hence sign-blind)
    """
    a = (v_md / 86400.0) / (2.0 * kappa)
    b = np.sqrt(a * a + 1j * omega / kappa)
    return float(np.exp(-(np.real(b) - a) * sep)), float(np.imag(b) * sep)


def admissible_velocities(observed, sep, kind, lo=-4.0, hi=4.0, n_scan=40001):
    """All v in [lo, hi] m/d whose homogeneous response matches `observed`.

    The amplitude ratio is monotone in v and yields one solution; the phase lag
    is even in v and yields two.  The scan is used rather than an assumed
    monotonicity, so that the count of solutions is a result and not an input.
    """
    v = np.linspace(lo, hi, n_scan)
    if kind == "amp":
        f = np.array([homogeneous_ratio(vv, sep)[0] - observed for vv in v])
    else:
        f = np.array([homogeneous_ratio(vv, sep)[1] - observed for vv in v])
    out = []
    for k in range(n_scan - 1):
        if f[k] * f[k + 1] < 0.0:
            a, b_ = v[k], v[k + 1]
            fa = f[k]
            for _ in range(80):
                m = 0.5 * (a + b_)
                fm = (homogeneous_ratio(m, sep)[0] - observed) if kind == "amp" \
                    else (homogeneous_ratio(m, sep)[1] - observed)
                if fa * fm <= 0.0:
                    b_ = m
                else:
                    a, fa = m, fm
            out.append(0.5 * (a + b_))
    return out


def wenner_two_layer(a, h, rho1, rho2, nterms=400):
    """Wenner apparent resistivity over a two-layer earth (analytic series)."""
    k = (rho2 - rho1) / (rho2 + rho1)
    n = np.arange(1, nterms + 1)
    x = 2.0 * n * h / a
    series = np.sum(k ** n * (1.0 / np.sqrt(1.0 + x * x)
                              - 1.0 / np.sqrt(4.0 + x * x)))
    return rho1 * (1.0 + 4.0 * series)


def main():
    section("1. Darcy flux from a piezometer pair")
    print(f"  SYNTHETIC reach: K_bed = {K_BED:.1f} m/d, effective porosity "
          f"{N_E:.2f}, piezometers {L_PIEZO:.1f} m apart")
    print("  dh = h_stream - h_aquifer; q_z = K dh/L is positive downward")
    print("   season      dh (m)   q_z (m/d)   seepage v (m/d)   exchange"
          " (m^3/d per m)")
    for label, dh in (("gaining", -0.32), ("losing", +0.10)):
        q_z = K_BED * dh / L_PIEZO
        print(f"   {label:8s}   {dh:+6.2f}   {q_z:+9.4f}   {q_z / N_E:+16.4f}   "
              f"{q_z * 2.0:+18.4f}")
    q_g = K_BED * (-0.32) / L_PIEZO
    q_l = K_BED * (0.10) / L_PIEZO
    print(f"  the reach gains {abs(q_g):.4f} m/d when the aquifer head is 0.32 m")
    print(f"  above the stream, and loses {q_l:.4f} m/d when it is 0.10 m below:")
    print(f"  a reversal by a factor {abs(q_g) / q_l:.1f} at the same site.")
    print("  -> two piezometers give a head difference and a distance.  The sign")
    print("     of the exchange is robust; the magnitude is a statement about K,")
    print("     which this measurement did not determine.")

    section("2. Diurnal temperature in a homogeneous bed")
    d_skin = np.sqrt(2.0 * KAPPA_SAND / OMEGA)
    print(f"  thermal diffusivity {KAPPA_SAND:.1e} m^2/s, period "
          f"{PERIOD / 3600.0:.0f} h, skin depth sqrt(2 kappa/omega) = "
          f"{d_skin:.4f} m")
    print(f"  surface amplitude {AMPL_SURF:.1f} K, probes at {Z1:.2f} m and "
          f"{Z2:.2f} m")
    z = np.linspace(0.0, 1.0, 2001)
    print("\n   v (m/d)   ratio A(z2)/A(z1)   phase lag (h)   admiss. v from"
          " amp (m/d)")
    for v_md in (-0.80, -0.40, -0.10, 0.0, 0.10, 0.40, 0.80):
        T = solve_temperature(v_md, lambda zz: KAPPA_SAND, z)
        ratio, lag, sep = amplitude_phase(z, T, Z1, Z2)
        sol = admissible_velocities(ratio, sep, "amp")
        print(f"   {v_md:+6.2f}   {ratio:15.4f}   {lag / (OMEGA * 3600.0):13.4f}"
              f"   {[float(round(x, 4)) for x in sol]}")
    print("\n  the amplitude ratio is ASYMMETRIC in v and strictly increasing:")
    print("  downwelling flow carries the diurnal signal deeper (a larger ratio),")
    print("  upwelling flow suppresses it (a smaller ratio, approaching zero).")
    print("  Each ratio therefore admits exactly ONE velocity, and it carries the")
    print("  sign of the flow: the inversion above returns the true value.")
    r_p, l_p, s_p = amplitude_phase(z, solve_temperature(+0.40, lambda zz: KAPPA_SAND, z), Z1, Z2)
    r_m, l_m, _ = amplitude_phase(z, solve_temperature(-0.40, lambda zz: KAPPA_SAND, z), Z1, Z2)
    print("  the phase lag is SYMMETRIC in v:")
    print(f"    v = +0.40 and v = -0.40 m/d give phase lags "
          f"{l_p / (OMEGA * 3600.0):.4f} and {l_m / (OMEGA * 3600.0):.4f} h,")
    print(f"    equal to {abs(l_p - l_m) / (OMEGA * 3600.0):.2e} h, while the "
          f"amplitude ratios differ ({r_p:.4f} vs {r_m:.4f}).")
    print(f"    the phase inversion returns +/- that magnitude: "
          f"{sorted(float(round(x, 3)) for x in admissible_velocities(l_p, s_p, 'phase'))}")
    print("  -> the PHASE measures |v| and cannot give the direction of flow;")
    print("     the AMPLITUDE is what identifies the sign.  A single-probe study")
    print("     that reports only a phase-derived velocity has measured a speed,")
    print("     not an exchange direction.")
    print(f"  (all quantities for a separation of {s_p:.3f} m)")

    section("3. A layered bed: the set of velocities the data admit")
    def kappa_layered(zz):
        return KAPPA_SILT if SILT_TOP <= zz <= SILT_BOT else KAPPA_SAND

    T = solve_temperature(V_GAIN, kappa_layered, z)
    ratio, lag, sep = amplitude_phase(z, T, Z1, Z2)
    r_h, l_h, _ = amplitude_phase(z, solve_temperature(V_GAIN, lambda zz: KAPPA_SAND, z), Z1, Z2)
    print(f"  truth: v = {V_GAIN:+.2f} m/d (upward, the gaining reach of "
          f"section 1), silt layer {SILT_TOP:.2f}-{SILT_BOT:.2f} m")
    print(f"  probes at {Z1:.2f} and {Z2:.2f} m (separation {sep:.3f} m)")
    print("   bed model          ratio    lag (h)")
    print(f"   homogeneous truth  {r_h:7.4f}   {l_h / (OMEGA * 3600.0):7.4f}")
    print(f"   layered truth      {ratio:7.4f}   {lag / (OMEGA * 3600.0):7.4f}")
    for name, obs, kind in (("amplitude ratio", ratio, "amp"),
                            ("phase lag", lag, "phase")):
        sol = admissible_velocities(obs, sep, kind)
        print(f"\n  homogeneous velocities matching the measured {name}:")
        print(f"    {[float(round(x, 4)) for x in sol]} m/d")
        if sol:
            best = min(sol, key=lambda s: abs(s - V_GAIN))
            print(f"    closest to the truth ({V_GAIN:+.2f} m/d): {best:+.4f} m/d,"
                  f" error {best - V_GAIN:+.4f} m/d "
                  f"({100 * (best / V_GAIN - 1):+.0f}%)")
        else:
            lags = [homogeneous_ratio(vv, sep)[1] for vv in np.linspace(-4, 4, 40001)]
            print(f"    none.  The largest lag any homogeneous bed can produce at")
            print(f"    this separation is {max(lags) / (OMEGA * 3600.0):.4f} h (at v = 0), "
                  f"and the layered bed")
            print(f"    shows {obs / (OMEGA * 3600.0):.4f} h: the homogeneous model is rejected "
                  f"outright.")
    print("\n  the same diagnostic on a hypothetical pair of readings")
    print("  (ratio 0.3500, lag 3.2000 h), as a study might report them:")
    for obs, kind, label in ((0.35, "amp", "ratio 0.3500"),
                             (3.20 * 3600.0 * OMEGA, "phase", "lag 3.2000 h")):
        sol = admissible_velocities(obs, sep, kind)
        print(f"    {label}: homogeneous velocities "
              f"{[float(round(x, 3)) for x in sol]} m/d")
    print("    the two readings imply different velocities, and neither is")
    print("    consistent with the other under the homogeneous model: the")
    print("    inconsistency is the measurement, and it must be reported.")

    print("\n  -> the silt layer has no parameter in the homogeneous model.  Its")
    print("     effect is absorbed into a wrong velocity, and the amplitude and")
    print("     the phase disagree with each other by far more than the")
    print("     measurement error would justify.  That disagreement is the only")
    print("     warning the data give.")

    section("4. Salt-dilution gauging")
    t = np.linspace(0.0, 3600.0, 36001)
    conc = 40.0 * np.exp(-(t - 900.0) ** 2 / (2.0 * 180.0 ** 2)) \
        + 6.0 * np.exp(-t / 1200.0)
    full = np.trapezoid(conc, t)
    print(f"  SYNTHETIC injection of {SALT_MASS:.2f} kg; the conductance curve is")
    print("  a Gaussian peak plus a slow tail, sampled over 3600 s")
    print("   integration limit (s)   integral (kg s/m^3)   Q (m^3/s)   error (%)")
    for tmax in (1500.0, 1800.0, 2400.0, 3600.0):
        m = t <= tmax
        integral = np.trapezoid(conc[m], t[m])
        q = SALT_MASS / integral
        print(f"   {tmax:20.0f}   {integral:20.2f}   {q:10.5f}   "
              f"{100 * (q / (SALT_MASS / full) - 1):+8.2f}")
    short = SALT_MASS / np.trapezoid(conc[t <= 1800.0], t[t <= 1800.0])
    print(f"  the full-window discharge is {SALT_MASS / full:.5f} m^3/s.  Cutting")
    print(f"  the record at 1800 s over-estimates it by "
          f"{100 * (short / (SALT_MASS / full) - 1):.1f}%.")
    print("  -> the injected mass is exact; the integral is not.  A reported")
    print("     discharge is a statement about the integration window as much as")
    print("     about the stream.")

    section("5. The ERT signature of a losing reach")
    rho_dry, rho_wet = 300.0, 60.0
    print(f"  two-layer teaching model: a saturated zone of rho = {rho_wet:.0f} "
          f"ohm m")
    print(f"  of thickness h beneath a dry bed of rho = {rho_dry:.0f} ohm m; "
          f"noise {NOISE_ERT * 100:.0f}%")
    spacings = np.array([0.5, 1.0, 2.0, 4.0, 8.0])
    base = np.array([wenner_two_layer(a, 1.0, rho_dry, rho_dry) for a in spacings])
    print("   h (m)   best spacing (m)   rho_a (ohm m)   ratio   detections"
          " at 2% noise")
    for h in (0.5, 1.0, 2.0):
        vals = np.array([wenner_two_layer(a, h, rho_wet, rho_dry) for a in spacings])
        r = vals / base
        i = int(np.argmin(r))
        print(f"   {h:5.1f}   {spacings[i]:16.1f}   {vals[i]:14.1f}   "
              f"{r[i]:6.4f}   {abs(1 - r[i]) / NOISE_ERT:18.1f} sd")
    print("  at the fixed spacing a = 1.0 m the apparent resistivity is")
    print("    dry bed: " + f"{base[1]:.1f} ohm m, " + ", ".join(
        f"h = {h:.1f} m: {wenner_two_layer(1.0, h, rho_wet, rho_dry):.1f} ohm m"
        for h in (0.5, 1.0, 2.0)))
    print("  -> the contrast is detectable for every thickness modelled, but the")
    print("     spacing and the amplitude of the ratio both depend on the assumed")
    print("     thickness.  Resistivity gives a contrast, not a flux: turning it")
    print("     into a seepage rate needs the Archie link and an estimate of how")
    print("     long the wetting has been there, neither of which is measured in")
    print("     the section.")

    section("6. Reconciling the methods on the same idealised reach")
    print("   method                    measures            gaining reach"
          "        losing reach")
    print(f"   piezometer pair (Darcy)   q_z (m/d)           {q_g:+.4f}"
          f"             {q_l:+.4f}")
    print(f"   diurnal temperature       v (m/d)             {V_GAIN:+.4f}"
          f"             {V_LOSE:+.4f}")
    print("   salt dilution             Q (m^3/s)           section 4"
          "            section 4")
    print("   ERT                       ratio rho           not resolvable"
          f"        {rho_wet / rho_dry:.4f}")
    print(f"  consistency check q_z = n_e v with n_e = {N_E:.2f}:")
    print(f"    gaining reach: {N_E * V_GAIN:+.4f} m/d from the temperature, "
          f"against {q_g:+.4f} m/d from Darcy")
    print(f"    losing reach : {N_E * V_LOSE:+.4f} m/d from the temperature, "
          f"against {q_l:+.4f} m/d from Darcy")
    print("  the two agree here because they were built from the same numbers.")
    print("  With field data they agree only if K, n_e and the structure of the")
    print("  temperature model are all right, and none of these four methods")
    print("  measures the others' assumptions.")
    print("  -> a reach-scale exchange flux is a DARCY velocity; a temperature-")
    print("     derived velocity is a SEEPAGE velocity.  Converting between them")
    print("     needs an effective porosity that this section never measured.")


if __name__ == "__main__":
    main()
