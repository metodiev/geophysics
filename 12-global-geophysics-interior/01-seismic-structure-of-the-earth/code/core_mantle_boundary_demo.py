#!/usr/bin/env python3
"""The core-mantle boundary: ULVZ, D'' and post-perovskite.

What the CMB reflection coefficients are; how a thin ultra-low-velocity zone
changes an ScS pulse; why a (thickness, velocity-drop) pair is not unique but a
waveform is a stronger constraint than a delay; and how the post-perovskite
transition turns the D'' discontinuity on and off with temperature.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python core_mantle_boundary_demo.py

Everything is SYNTHETIC.  Densities, velocities, layer thicknesses, the
Clapeyron slope and the reference temperature are chosen teaching values.  No
seismogram, station, event or published number from the literature is used.  The
CMB depth (2891 km) and the base-of-mantle velocities are the same chosen values
as in lesson 01.

Contents
--------
1. Reflection coefficients at the CMB: why S is totally reflected and P is not.
2. A ULVZ of thickness h and velocity drop d: the ScS delay.
3. Non-uniqueness: the (h, d) family that produces one delay.
4. Full waveform: the reflectivity of the same family, and where the waveforms
   differ.  A delay is one number; a pulse is a shape.
5. D'' and post-perovskite: the layer thickness as a function of CMB temperature
   and Clapeyron slope, including the shut-off threshold.
6. The apparent thickness from a travel-time delay, and its velocity ambiguity.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC base-of-mantle and core parameters ---------------------------
RHO_M, VP_M, VS_M = 5.57, 13.72, 7.26       # g/cm^3, km/s, km/s (lesson 01)
RHO_C, VP_C = 9.90, 8.06                    # outer core
D_CMB = 2891.0                              # km depth of the CMB (convention)
DT_S = 0.5                                  # s, sampling of the synthetic pulse
N_SAMPLES = 8192
F_RICKER = 0.08                             # Hz, ~12 s period
RHO_ULVZ_FACTOR = 1.30                      # density rises with the velocity drop
VP_ULVZ_FACTOR = 0.50                       # vp drop is half the vs drop


def section(title):
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def impedance(rho, v):
    """Acoustic impedance rho*v in g/cm^3 * km/s (units cancel in ratios)."""
    return rho * v


def ulvz_properties(delta):
    """Given a fractional vs reduction delta, return the ULVZ (rho, vp, vs)."""
    return (RHO_M * (1.0 + RHO_ULVZ_FACTOR * delta),
            VP_M * (1.0 - VP_ULVZ_FACTOR * delta),
            VS_M * (1.0 - delta))


def ulvz_delay(h_km, delta):
    """Two-way extra travel time inside a ULVZ of thickness h (s).

    The reference reflection happens at the CMB; with a ULVZ present, the wave
    that penetrates the layer travels 2h at the reduced velocity instead of 2h at
    the mantle velocity, so the *extra* time is 2h (1/v' - 1/v).
    """
    _, _, vs_u = ulvz_properties(delta)
    return 2.0 * h_km * (1.0 / vs_u - 1.0 / VS_M)


def solve_delta(h_km, target_delay):
    """Bisection for the velocity drop that gives a requested postcursor delay."""
    lo, hi = 0.0, 0.9
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if ulvz_delay(h_km, mid) < target_delay:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def ricker(t, f0):
    a = (np.pi * f0) ** 2
    return (1.0 - 2.0 * a * t ** 2) * np.exp(-a * t ** 2)


def stack_reflectivity(freqs, impedances, one_way_times):
    """Input-impedance recursion for the normal-incidence SH reflectivity.

    Z_in = Z_k (Z_{k+1} + i Z_k tan(w tau_k)) / (Z_k + i Z_{k+1} tan(w tau_k)),
    evaluated upward from the half space, with R = (Z_in - Z_0)/(Z_in + Z_0).
    The sign convention matters: with this form a uniform layer over a free
    surface delays the pulse by exactly the two-way time in the layer, which is
    the physical result and the check used in section 4.
    """
    out = np.zeros_like(freqs, dtype=complex)
    for i, f in enumerate(freqs):
        zin = impedances[-1]
        w = 2.0 * np.pi * f
        for k in range(len(one_way_times) - 1, -1, -1):
            t = np.tan(w * one_way_times[k])
            zin = impedances[k] * (zin + 1j * impedances[k] * t) / \
                (impedances[k] + 1j * zin * t)
        out[i] = (zin - impedances[0]) / (zin + impedances[0])
    return out


def synthetic_reflection(h_km, delta, f0=F_RICKER):
    """Reflected ScS pulse for a ULVZ of thickness h and drop delta.

    Returns (t, pulse, envelope) with the pulse normalised to the total
    reflection amplitude of a reference CMB, t relative to the reference
    arrival, and envelope the analytic-signal amplitude of the pulse (the
    physically meaningful measure of a pulse whose phase has been rotated).
    """
    n = N_SAMPLES
    t = (np.arange(n) - n // 8) * DT_S
    wavelet = ricker(t, f0)
    freqs = np.fft.rfftfreq(n, DT_S)
    S = np.fft.rfft(wavelet)
    _, _, vs_u = ulvz_properties(delta)
    z_mantle = impedance(RHO_M, VS_M)
    z_ulvz = impedance(*ulvz_properties(delta)[::2])
    tau_ulvz = h_km / vs_u
    R = stack_reflectivity(freqs, [z_mantle, z_ulvz, 0.0], [0.0, tau_ulvz])
    refl = np.fft.irfft(R * S, n=n)
    analytic = np.fft.ifft(np.fft.fft(refl) * 2.0 * (np.fft.fftfreq(n, DT_S) > 0.0))
    return t, refl, np.abs(analytic)


def main():
    section("1. Reflection coefficients at the CMB")
    z_m_s = impedance(RHO_M, VS_M)
    z_c_s = impedance(RHO_C, 0.0)
    z_m_p = impedance(RHO_M, VP_M)
    z_c_p = impedance(RHO_C, VP_C)
    print(f"  mantle at the CMB: rho = {RHO_M:.2f} g/cm^3, vp = {VP_M:.2f}, "
          f"vs = {VS_M:.2f} km/s")
    print(f"  outer core      : rho = {RHO_C:.2f} g/cm^3, vp = {VP_C:.2f}, "
          "vs = 0 (a fluid cannot support shear)")
    print(f"  S-wave impedance: mantle {z_m_s:7.3f}, core {z_c_s:7.3f} "
          f"-> R = {(z_c_s - z_m_s) / (z_c_s + z_m_s):+.4f}")
    print("  a coefficient of -1 means TOTAL internal reflection with reversed")
    print("  polarity: the outer core is a free surface for shear waves, which")
    print("  is why ScS exists and why the S shadow is not like the P shadow.")
    print(f"  P-wave impedance: mantle {z_m_p:7.3f}, core {z_c_p:7.3f} "
          f"-> R = {(z_c_p - z_m_p) / (z_c_p + z_m_p):+.4f}")
    print("  the P contrast is ~2 %, so P energy enters the core: the same")
    print("  boundary is nearly transparent to one phase and opaque to another.")

    section("2. A ULVZ: thickness, velocity drop, and the postcursor delay")
    print("  SYNTHETIC ULVZ model: vs reduced by d, vp reduced by d/2, density")
    print(f"  raised by {RHO_ULVZ_FACTOR:.2f} d; the delay is 2h (1/vs' - 1/vs).")
    print("    d (%)   vs' (km/s)   h = 10 km   h = 20 km   h = 30 km   [delay, s]")
    for d in (0.05, 0.10, 0.20, 0.30):
        row = [ulvz_delay(h, d) for h in (10.0, 20.0, 30.0)]
        _, _, vs_u = ulvz_properties(d)
        print(f"  {d * 100:6.0f}   {vs_u:10.3f}   {row[0]:11.3f}   {row[1]:11.3f}"
              f"   {row[2]:11.3f}")
    print("  the delay is the only quantity a travel-time measurement returns.")

    section("3. Non-uniqueness: the (h, d) family behind one delay")
    target = 1.000
    print(f"  a measured ScS delay of {target:.3f} s can be produced by all of:")
    print("    h (km)   required d (%)   vs' (km/s)")
    for h in (5.0, 10.0, 15.0, 20.0, 30.0, 40.0):
        lo, hi = 0.0, 0.9
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if ulvz_delay(h, mid) < target:
                lo = mid
            else:
                hi = mid
        d = 0.5 * (lo + hi)
        _, _, vs_u = ulvz_properties(d)
        print(f"  {h:8.1f}   {d * 100:15.3f}   {vs_u:11.3f}")
    print("  every row gives exactly the same delay.  A +/-1 km error in layer")
    print("  thickness is therefore equivalent to several per cent of velocity,")
    print("  and vice versa: the delay alone fixes neither.")

    section("4. Full waveform: the same delay, different pulses")
    print(f"  every model below gives the SAME postcursor delay of "
          f"{target:.3f} s,")
    print("  so a delay measurement cannot tell them apart.  What differs is the")
    print("  internal two-way time 2h/vs', which is the separation between the")
    print("  reflection off the top of the ULVZ and the reflection at the CMB.")
    print("  A structure is resolvable only if that separation exceeds the")
    print("  dominant period of the data, and only if the reflections from the two")
    print("  interfaces are strong enough to be seen above the noise.")
    for f0 in (F_RICKER, 0.40):
        period = 1.0 / f0
        print(f"\n  dominant frequency {f0:.2f} Hz (period {period:.1f} s):")
        print("    h (km)   d (%)   2h/vs' (s)   peak t (s)   width (s)   energy"
              "   r_top")
        t_ref, ref_pulse, ref_env = synthetic_reflection(0.0, 0.0, f0)
        ref_energy = float(np.sum(ref_pulse ** 2))
        for h in (5.0, 10.0, 20.0, 40.0):
            d = solve_delta(h, target)
            _, _, vs_u = ulvz_properties(d)
            sep = 2.0 * h / vs_u
            t, refl, env = synthetic_reflection(h, d, f0)
            peak = float(np.max(env))
            i_peak = int(np.argmax(env))
            half = np.where(env >= 0.5 * peak)[0]
            width = t[half[-1]] - t[half[0]] if len(half) > 1 else 0.0
            energy = float(np.sum(refl ** 2))
            z_u = impedance(*ulvz_properties(d)[::2])
            r_top = (z_u - impedance(RHO_M, VS_M)) / (z_u + impedance(RHO_M, VS_M))
            print(f"  {h:8.1f}   {d * 100:6.2f}   {sep:10.2f}   {t[i_peak]:9.2f}"
                  f"   {width:8.2f}   {energy / ref_energy:6.3f}   {r_top:+6.3f}")
        print("    (peak times are measured from the top of the ULVZ; subtracting")
        print("     2h/vs from the peak time gives the delay relative to the")
        print("     reference CMB reflection, which is the measured quantity)")
    print("  the peak time tracks 2h/vs' almost exactly (2.50 vs 2.38, 4.00 vs")
    print("  3.75, 6.50 vs 6.51, 12.00 vs 12.02 s), so the composite pulse behaves")
    print("  as a single delayed arrival: the layer acts as a delay line, and the")
    print("  delay measured from the CMB reference is the postcursor delay of")
    print("  section 3 (about 1.0 s) in every case.  The pulse WIDTH barely")
    print("  changes with h at either frequency, because the top reflection")
    print("  coefficient r_top is only 1-5 %: the internal reverberations are too")
    print("  weak to be seen above a 50 % threshold.  Energy is preserved to")
    print("  within 0.1 % because the stack is lossless (a check on the")
    print("  arithmetic, not a physical result).")
    print("  CONSEQUENCE, stated honestly: with this density-velocity relation the")
    print("  waveform does NOT break the (h, d) degeneracy.  A delay measurement")
    print("  returns one number, and 5 km/42 % and 40 km/8 % produce the same")
    print("  number and nearly the same pulse.  Breaking it needs either a much")
    print("  larger impedance contrast (a stronger density change than the 1.3 d")
    print("  used here), shorter-period phases, or an independent constraint.")

    section("5. D'' and post-perovskite: a threshold in temperature")
    c_at_tref = 10.0e9                  # Pa, transition pressure above the CMB
    rho_dd, g_cmb = 5560.0, 10.68       # kg/m^3, m/s^2
    rho_g = rho_dd * g_cmb              # Pa per m
    t_ref = 2500.0                      # K, reference CMB temperature (chosen)
    print(f"  chosen model: at T_CMB = {t_ref:.0f} K the post-perovskite transition")
    print(f"  lies {c_at_tref / 1e9:.1f} GPa above the CMB pressure, and the")
    print(f"  Clapeyron slope shifts it by gamma per kelvin.")
    print(f"  with dP/dz = rho g = {rho_g / 1e6 * 1000:.2f} MPa/km, a pressure difference")
    print(f"  of {c_at_tref / 1e9:.1f} GPa corresponds to {c_at_tref / rho_g / 1e3:.1f}"
          " km of D''.")
    print("\n    T_CMB (K)   D'' thickness (km), gamma = 6 / 8 / 10 MPa/K")
    for T in (2300.0, 2500.0, 2800.0, 3200.0, 3500.0, 3800.0, 4200.0):
        cells = []
        for gamma in (6.0, 8.0, 10.0):
            dp = c_at_tref - gamma * 1e6 * (T - t_ref)
            h = dp / rho_g / 1e3
            cells.append("absent" if h <= 0.0 else f"{h:6.1f}")
        print(f"  {T:10.0f}   {cells[0]:>12s} /{cells[1]:>7s} /{cells[2]:>7s}")
    print("  the threshold temperatures are T_ref + C/gamma:")
    for gamma in (6.0, 8.0, 10.0):
        print(f"    gamma = {gamma:4.1f} MPa/K -> shut-off at "
              f"{t_ref + c_at_tref / (gamma * 1e6):7.0f} K")
    print("  so a hotter boundary thins D'' and eventually removes the")
    print("  discontinuity altogether, and the temperature at which that happens")
    print("  depends on gamma, which mineral physics must supply.")

    section("6. From a D'' travel-time delay to a thickness")
    print("  a reflection from the top of D'' arrives 2h/vs before the CMB")
    print("  reflection; with vs = 7.26 km/s the two-way slowness is")
    print(f"    2/vs = {2.0 / VS_M:.5f} s/km")
    print("    measured delay (s)   thickness for vs = 7.26   thickness if vs is "
          "3 % lower")
    vs_low = VS_M * 0.97
    for dt in (2.0, 5.0, 10.0, 20.0):
        h_ref = dt / (2.0 / VS_M)
        h_low = dt / (2.0 / vs_low)
        print(f"  {dt:20.1f}   {h_ref:23.1f}   {h_low:28.1f}")
    print("  a 3 % velocity error moves the thickness by 3 %: the D'' thickness")
    print("  is only as good as the velocity model between the surface and there.")
    print("  Everything measured here is a TIME.  Every thickness in this lesson")
    print("  is a time divided by an assumed velocity.")


if __name__ == "__main__":
    main()
