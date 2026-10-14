#!/usr/bin/env python3
"""Outer core, inner core: what the phases through the core measure, how inner-core
anisotropy is detected, and why the inner core's rotation rate is not a number the
data can return on their own.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python outer_and_inner_core_demo.py

Everything is SYNTHETIC.  Velocities, densities, anisotropy parameters,
heterogeneity amplitudes and rotation rates are chosen teaching values.  No
seismogram, station, catalogue or published measurement is used.  The ICB radius
(1221.5 km) and the core velocities are the chosen values of lesson 01.

Contents
--------
1. The core's radial structure, vertical travel times, and the ICB reflection.
2. Inner-core anisotropy: the differential time between axial and equatorial paths,
   as a function of how deeply the path samples the inner core.
3. S-wave splitting in the inner core, and what an observed splitting requires.
4. Inner-core rotation: the travel-time change produced by a lateral heterogeneity
   rotating past a fixed path, and the rate implied by a measured secular change.
5. The degeneracy table: (rotation rate x heterogeneity) and (anisotropy x path
   geometry) combinations that fit the same numbers.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

R_CMB, R_ICB, R_EARTH = 3480.0, 1221.5, 6371.0     # km
# SYNTHETIC core profiles (linear in radius between the boundaries)
VP_OC_CMB, VP_OC_ICB = 8.06, 10.29                 # outer core, km/s
VP_IC_TOP, VP_IC_CEN = 11.03, 11.26                # inner core, km/s
VS_IC_TOP, VS_IC_CEN = 3.50, 3.67
RHO_OC_CMB, RHO_OC_ICB = 9.90, 12.17               # g/cm^3
RHO_IC_TOP, RHO_IC_CEN = 12.76, 13.09
ANIS_P = 0.030          # polar P velocity is 3 % higher than equatorial
ANIS_S = 0.010          # +/- fraction for the two S polarisations
SOLID_TOP_KM = 100.0    # weak-anisotropy skin at the top of the inner core


def section(title):
    print(f"\n{'=' * 76}\n{title}\n{'=' * 76}")


def vp_core(r):
    """P velocity at radius r (km) inside the CMB, before anisotropy."""
    r = np.asarray(r, dtype=float)
    out = np.where(r >= R_ICB,
                   VP_OC_CMB + (r - R_CMB) * (VP_OC_ICB - VP_OC_CMB) / (R_ICB - R_CMB),
                   VP_IC_TOP + (r - R_ICB) * (VP_IC_CEN - VP_IC_TOP) / (0.0 - R_ICB))
    return out


def vs_inner(r):
    """S velocity at radius r inside the ICB."""
    r = np.asarray(r, dtype=float)
    return VS_IC_TOP + (r - R_ICB) * (VS_IC_CEN - VS_IC_TOP) / (0.0 - R_ICB)


def rho_core(r):
    r = np.asarray(r, dtype=float)
    return np.where(r >= R_ICB,
                    RHO_OC_CMB + (r - R_CMB) * (RHO_OC_ICB - RHO_OC_CMB)
                    / (R_ICB - R_CMB),
                    RHO_IC_TOP + (r - R_ICB) * (RHO_IC_CEN - RHO_IC_TOP)
                    / (0.0 - R_ICB))


def anis_profile(r):
    """Radial shape of the inner-core anisotropy; zero outside the inner core.

    Weak in the top skin, full strength below, and identically zero in the outer
    core and mantle because those are not modelled as anisotropic here.
    """
    r = np.asarray(r, dtype=float)
    depth_from_icb = R_ICB - r
    # a smooth taper rather than a step: a velocity discontinuity would make the
    # turning-point search ambiguous exactly where the ray turns
    taper = 0.25 + 0.75 * 0.5 * (1.0 + np.tanh((depth_from_icb - 250.0) / 120.0))
    return np.where(r <= R_ICB, taper, 0.0)


def turning_radius(p, vfunc):
    """Inner-core turning radius for ray parameter p and velocity function vfunc."""
    radii = np.linspace(0.0, R_ICB - 0.5, 4001)   # stop short of the interface
    u = radii / vfunc(radii)          # u increases from the centre to the ICB
    if p > float(u[-1]):
        return None
    return float(np.interp(p, u, radii))


def core_leg_time(p, r_tp, vfunc, split_icb=True, n=8000):
    """Two-way P travel time through the core for a ray turning at r_tp.

    The integrand is dt = u/(v * sqrt(u^2 - p^2)) dr with u = r/v, integrated in
    the s variable (r = r_tp + s^2) so that the inverse-square-root singularity
    at the turning point is removed.  The velocity function is evaluated in the
    inner core and the outer core separately, and the outer-core part uses the
    unmodified velocity (no anisotropy outside the inner core).
    """
    s_max = np.sqrt(max(R_CMB - r_tp, 1.0))
    s = (np.arange(n) + 0.5) * (s_max / n)
    ds = s_max / n
    r = r_tp + s ** 2
    dr = 2.0 * s * ds
    v = vfunc(r)
    # (u - p)(u + p) avoids the cancellation of u^2 - p^2 near the turning point
    rad = np.sqrt(np.maximum((r / v - p) * (r / v + p), 0.0))
    # the turning point itself gives rad = 0; drop only the sample exactly there
    good = rad > 0.0
    t = float(np.sum((r[good] / v[good]) / (v[good] * rad[good]) * dr[good]))
    if split_icb:
        out = (r > R_ICB) & good
        if out.any():
            v_oc = vp_core(r[out])
            rad_oc = np.sqrt(np.maximum((r[out] / v_oc - p) * (r[out] / v_oc + p),
                                        0.0))
            t -= float(np.sum((r[out] / v_oc) / (v_oc * rad_oc) * dr[out]))
            t += float(np.sum((r[out] / v_oc) / (v_oc * rad_oc) * dr[out]))
    return 2.0 * t


def inner_core_leg(p, r_tp, n=20000):
    """Two-way travel time and length of the inner-core part of a ray path.

    Returns (time, length, anisotropy-weighted time) where the last is
    int A(r) * (dl/v) over the leg, i.e. the quantity that multiplies
    cos^2(theta) to give the first-order differential travel time.
    """
    s_max = np.sqrt(max(R_ICB - r_tp, 1e-9))
    s = (np.arange(n) + 0.5) * (s_max / n)
    ds = s_max / n
    r = r_tp + s ** 2
    dr = 2.0 * s * ds
    v = vp_core(r)
    rad = np.sqrt(np.maximum((r / v - p) * (r / v + p), 0.0))
    good = rad > 0.0
    path = (r[good] / v[good]) / rad[good] * dr[good]      # dl = (u/rad) dr
    return (2.0 * float(np.sum(path / v[good])),
            2.0 * float(np.sum(path)),
            2.0 * float(np.sum(anis_profile(r[good]) * path / v[good])))


def rotate_pattern(r, phi, phi0, amp=0.005):
    """Fractional slowness perturbation of a rotating inner-core heterogeneity.

    The physical structure is a cos(2*phi) pattern in the equatorial plane whose
    orientation is phi0; at time t it has rotated by dphi, so the pattern sampled
    by a fixed path is cos(2*(phi - phi0)).
    """
    return amp * np.tanh((R_ICB - r) / 200.0) * np.cos(2.0 * (phi - phi0))


def main():
    section("1. The core's radial structure and vertical travel times")
    print("  SYNTHETIC profiles (linear in radius between the boundaries):")
    print(f"    outer core: vp {VP_OC_CMB:.2f} at r = {R_CMB:.0f} km -> "
          f"{VP_OC_ICB:.2f} km/s at r = {R_ICB:.1f} km, rho "
          f"{RHO_OC_CMB:.2f} -> {RHO_OC_ICB:.2f} g/cm^3, vs = 0")
    print(f"    inner core: vp {VP_IC_TOP:.2f} -> {VP_IC_CEN:.2f} km/s, vs "
          f"{VS_IC_TOP:.2f} -> {VS_IC_CEN:.2f} km/s, rho "
          f"{RHO_IC_TOP:.2f} -> {RHO_IC_CEN:.2f} g/cm^3")
    r_oc = np.linspace(R_ICB, R_CMB, 20001)
    t_oc = float(np.trapezoid(1.0 / vp_core(r_oc), r_oc))
    r_ic = np.linspace(0.0, R_ICB, 20001)
    t_ic = float(np.trapezoid(1.0 / vp_core(r_ic), r_ic))
    print(f"  vertical (p = 0) travel time through the outer core: {t_oc:8.3f} s "
          f"over {R_CMB - R_ICB:.1f} km")
    print(f"  vertical travel time through the inner core:           {t_ic:8.3f} s "
          f"over {R_ICB:.1f} km")
    print(f"  mean inner-core vp implied: {R_ICB / t_ic:.4f} km/s")
    g_ic = RHO_IC_TOP * VS_IC_TOP ** 2
    k_ic = RHO_IC_TOP * (VP_IC_TOP ** 2 - 4.0 / 3.0 * VS_IC_TOP ** 2)
    nu_ic = (VP_IC_TOP ** 2 - 2 * VS_IC_TOP ** 2) / (2 * (VP_IC_TOP ** 2 - VS_IC_TOP ** 2))
    print(f"  inner-core elastic moduli at the ICB: G = {g_ic:.1f} GPa, "
          f"K = {k_ic:.1f} GPa, K/G = {k_ic / g_ic:.2f}")
    print(f"  Poisson's ratio of the inner core: {nu_ic:.4f} "
          "(a very soft solid: compare 0.25-0.28 for the mantle)")
    z_oc = RHO_OC_ICB * VP_OC_ICB
    z_ic = RHO_IC_TOP * VP_IC_TOP
    print(f"  P impedance just below the CMB: {RHO_OC_CMB * VP_OC_CMB:7.2f}; "
          f"at the ICB: {z_oc:7.2f} (outer core) vs {z_ic:7.2f} (inner core)")
    print(f"  P reflection coefficient at the ICB: "
          f"{(z_ic - z_oc) / (z_ic + z_oc):+.4f} "
          f"({(z_ic - z_oc) / (z_ic + z_oc) * 100:.1f} % amplitude)")
    print("  the ICB is therefore a strong P reflector and, because the inner core")
    print("  supports shear, a solid-solid boundary on its lower side.")

    section("2. Inner-core anisotropy: the differential time")
    print(f"  SYNTHETIC anisotropy: the axial P velocity is "
          f"{ANIS_P * 100:.1f} % above the equatorial one, tapering from a")
    print("  quarter of that value at the ICB to full strength below 400 km.")
    print("  The differential time at fixed ray parameter is computed to first")
    print("  order along the reference path (Fermat's principle makes the")
    print("  path change a second-order contribution to the time):")
    print("    dt_axial = -2 cos^2(theta) * ANIS_P * int A(r) dl/v")
    v_iso = vp_core
    print("    p (s/rad)   r_tp (km)   leg: length (km)   time (s)   "
          "mean A   dt (s)")
    for p_ in (10.0, 30.0, 50.0, 70.0, 90.0, 105.0):
        r_tp = turning_radius(p_, v_iso)
        t_leg, length, w_leg = inner_core_leg(p_, r_tp)
        dt = -ANIS_P * w_leg
        print(f"  {p_:10.1f}   {r_tp:9.1f}   {length:15.1f}   {t_leg:9.3f}   "
              f"{w_leg / t_leg:7.3f}   {dt:+7.3f}")
    print("  the last column is the whole measurement: a few seconds, of which")
    print("  the sign says the axial path is faster, and the size is")
    print("  ANIS_P x (leg time) x (mean taper).  The mean taper rises with")
    print("  depth because shallow-turning rays spend their time in the weak zone.")
    print("  A random ensemble of directions averages cos^2 theta to 1/3, so a")
    print("  uniformly sampled data set shows only a third of this effect: what")
    print("  a study reports as 'the' inner-core anisotropy depends on which")
    print("  paths it happens to have.")

    section("3. S-wave splitting in the inner core")
    r_chord = np.linspace(0.0, R_ICB, 40001)
    t_s = 2.0 * float(np.trapezoid(1.0 / vs_inner(r_chord), r_chord))
    print(f"  vertical S travel time through the inner core: {t_s:.3f} s")
    print(f"  with a +/-{ANIS_S * 100:.1f} % S anisotropy the two polarisations")
    print(f"  differ by 2 x {ANIS_S:.3f} x {t_s:.1f} s = {2 * ANIS_S * t_s:.3f} s")
    print("  for a path along the axis; an equatorial path shows no splitting.")
    print("    observed splitting (s)   implied S anisotropy (%)")
    for obs in (0.5, 1.0, 2.0, 4.0):
        b = obs / (2.0 * t_s)
        print(f"  {obs:22.1f}   {b * 100:23.3f}")
    print("  the P anisotropy and the S anisotropy are therefore separate")
    print("  measurements, and their RATIO is the diagnostic: a mechanism that")
    print("  aligns crystals produces both, in a fixed proportion that depends on")
    print("  the mineral's elastic tensor, while a mechanism based on melt or")
    print("  texture can produce them in a different ratio.")

    section("4. Inner-core rotation: a secular travel-time change")
    print("  model: a lateral heterogeneity of amplitude 0.5 % with a cos(2 phi)")
    print("  pattern, tapering over the outer 200 km of the inner core.  A path")
    print("  in the EQUATORIAL plane (cos^2 theta = 0) is insensitive to the P")
    print("  anisotropy, which separates the two effects by construction.")
    depth_km = 300.0
    r_ch = R_ICB - depth_km
    half = np.sqrt(max(R_ICB ** 2 - r_ch ** 2, 0.0))
    t_par = np.linspace(-half, half, 4000)
    x, y = t_par, r_ch * np.ones_like(t_par)
    phi = np.arctan2(y, x)
    r_pts = np.sqrt(x ** 2 + y ** 2)
    dl = np.hypot(np.diff(x), np.diff(y))
    v = vp_core(r_pts)
    print(f"  chord geometry: a straight chord at perpendicular distance "
          f"{r_ch:.1f} km, half-length {half:.1f} km")
    print(f"  inner-core leg length {2 * half:.1f} km, and its isotropic travel")
    t_leg = float(np.sum(0.5 * (dl / v[1:] + dl / v[:-1])))
    print(f"  time (one way across the inner core) = {t_leg:.3f} s")
    print("    rotation (deg)   travel-time change (s)")
    ref = None
    for rot_deg in (0, 30, 60, 90, 120, 150, 180):
        pert = rotate_pattern(r_pts, phi, np.radians(rot_deg))
        dts = -np.sum(0.5 * (pert[1:] + pert[:-1]) * dl / v[:-1])
        if ref is None:
            ref = dts
        print(f"  {rot_deg:16.0f}   {dts - ref:+21.4f}")
    print("  the signal is periodic in 180 degrees, because a cos(2 phi) pattern")
    print("  is invariant under a half turn: an observed oscillation cannot by")
    print("  itself distinguish a fast rotation from a slow one.")
    rates = []
    for phi0_deg in np.arange(0.0, 91.0, 5.0):
        pert0 = rotate_pattern(r_pts, phi, np.radians(phi0_deg))
        pert1 = rotate_pattern(r_pts, phi, np.radians(phi0_deg + 1.0))
        d0 = -np.sum(0.5 * (pert0[1:] + pert0[:-1]) * dl / v[:-1])
        d1 = -np.sum(0.5 * (pert1[1:] + pert1[:-1]) * dl / v[:-1])
        rates.append((phi0_deg, d1 - d0))
    rate_per_deg = min(rates, key=lambda pair: pair[1])[1]
    print("  the observed rate depends on the orientation of the pattern relative")
    print("  to the path; scanning the orientation gives:")
    print("    pattern orientation (deg)   travel-time change per degree (s/deg)")
    for phi0_deg, rate in rates:
        print(f"  {phi0_deg:24.0f}   {rate:+35.5f}")
    print(f"  the largest rate is {rate_per_deg:+.5f} s per degree of rotation,")
    print("  and it is ZERO when the pattern is symmetric about the path: a")
    print("  measured zero secular change does not mean no rotation.")
    print("    assumed rate (deg/yr)   predicted change (s/yr)")
    for omega in (0.05, 0.1, 0.5, 1.0, 2.0):
        print(f"  {omega:23.2f}   {omega * rate_per_deg:+24.4f}")

    section("5. The degeneracy table")
    target_rate = 0.02
    print(f"  suppose a study measures a secular change of {target_rate:.3f} s/yr.")
    print("    heterogeneity amplitude (%)   implied rotation rate (deg/yr)")
    for amp in (0.1, 0.25, 0.5, 1.0, 2.0):
        scale = amp / 0.5
        print(f"  {amp * 100:29.1f}   {target_rate / (rate_per_deg * scale):24.2f}")
    print("  the rate is measurable only as (rate x heterogeneity amplitude):")
    print("  without an independent constraint on the heterogeneity, the data fix")
    print("  the product and not the rate.  Adding axial paths breaks the")
    print("  degeneracy, because anisotropy affects them and rotation does not.")
    print("  There is a further degeneracy with the ANISOTROPY magnitude: an")
    print("  axial path's differential time is proportional to anisotropy x leg")
    print("  time, so a 1 % anisotropy over a 220 s leg and a 2 % anisotropy over")
    print("  a 110 s leg are the same measurement:")
    print("    anisotropy (%)   leg time giving the same 2.2 s differential (s)")
    for a in (0.5, 1.0, 2.0, 3.0):
        print(f"  {a:15.1f}   {2.2 / (a / 100):40.1f}")
    print("  This is why the inner core's anisotropy, its heterogeneity and its")
    print("  rotation are described as a coupled problem rather than three")
    print("  independent measurements.")


if __name__ == "__main__":
    main()
